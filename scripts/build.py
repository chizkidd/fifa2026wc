# -*- coding: utf-8 -*-
"""
Build the unified FIFA World Cup 2026 dataset.

Inputs (repo root):
  - 2026-fifa-wc-guardian-squad.json  : rich per-player data (bio, DOB, club, photo, epithet)
  - fifa2026wc-squads.md              : group assignments + manager per team
  - scripts/curated.py                : ranks, predicted standings, bracket, team meta, badges, lists

Outputs:
  - site/public/data/wc2026.json      : everything the website needs
  - data/players.csv                  : flat squad table (coach + GK/DEF/MID/FWD)
  - data/teams.json                   : compact per-team summary

Run:  python3 scripts/build.py
"""
import csv
import json
import os
import re
import unicodedata
from datetime import date

import curated as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQUAD_JSON = os.path.join(ROOT, "2026-fifa-wc-guardian-squad.json")
SQUAD_MD = os.path.join(ROOT, "fifa2026wc-squads.md")
OUT_WEB = os.path.join(ROOT, "site", "data", "wc2026.json")
OUT_CSV = os.path.join(ROOT, "data", "players.csv")
OUT_TEAMS = os.path.join(ROOT, "data", "teams.json")

KICKOFF = date(2026, 6, 11)
SPECIAL_FIELD = "special player? (eg. key player, promising talent, etc) OPTIONAL"


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def canon(name):
    name = (name or "").strip()
    return C.NAME_ALIASES.get(name, name)


def fold(s):
    """Lower-case, accent-stripped key for tolerant name matching."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).strip().lower()


def pos_group(raw):
    r = (raw or "").lower()
    if r.startswith("goalkeeper") or r == "gk":
        return "Goalkeeper"
    if r.startswith("defender") or r.startswith("full") or r.startswith("centre-back") or r.startswith("center-back") or r.startswith("wing-back"):
        return "Defender"
    if r.startswith("midfield"):
        return "Midfielder"
    if r.startswith("forward") or r.startswith("striker") or r.startswith("winger") or r.startswith("attack"):
        return "Forward"
    return "Midfielder"  # safe fallback


POS_ORDER = {"Goalkeeper": 0, "Defender": 1, "Midfielder": 2, "Forward": 3}


def age_at(dob_str, ref=KICKOFF):
    dob_str = (dob_str or "").strip()
    m = re.match(r"(\d{1,2})[/\-.](\d{1,2})[/\-.](\d{4})", dob_str)
    if not m:
        return None, None
    d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    try:
        dob = date(y, mo, d)
    except ValueError:
        return None, None
    yrs = ref.year - dob.year - ((ref.month, ref.day) < (dob.month, dob.day))
    return yrs, dob.isoformat()


def short_bio(bio, max_sentences=4, max_chars=480):
    bio = (bio or "").strip()
    if not bio:
        return ""
    # split on sentence enders while keeping it simple
    parts = re.split(r"(?<=[.!?])\s+", bio)
    out = ""
    for p in parts[:max_sentences]:
        if len(out) + len(p) > max_chars and out:
            break
        out = (out + " " + p).strip()
    return out


# --------------------------------------------------------------------------
# parse markdown for manager (+ sanity check group membership)
# --------------------------------------------------------------------------
def parse_md_managers(path):
    managers = {}
    md_groups = {}
    with open(path, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]

    # group membership header lines at top: "Group A: Team1, Team2, ..."
    for ln in lines[:20]:
        m = re.match(r"Group ([A-L]):\s*(.+)", ln.strip())
        if m:
            g = m.group(1)
            teams = [canon(t.strip()) for t in m.group(2).split(",")]
            md_groups[g] = teams

    pending = None
    cur_group = None
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        gm = re.match(r"GROUP ([A-L])$", s)
        if gm:
            cur_group = gm.group(1)
            pending = None
            continue
        if re.match(r"(Goalkeepers|Defenders|Midfielders|Forwards|Strikers):", s):
            continue
        mm = re.match(r"Manager:\s*(.+)", s)
        if mm and pending:
            managers[pending] = mm.group(1).strip()
            pending = None
            continue
        # announcement lines
        if re.search(r"(squad|roster).*(announced|named)|announced|provisional", s, re.I):
            continue
        if s.startswith("Group "):
            continue
        # plausible team name line (no colon, has letters)
        if ":" not in s and re.search(r"[A-Za-z]", s) and len(s) < 45:
            pending = canon(s)
    return managers, md_groups


# --------------------------------------------------------------------------
# badge assignment
# --------------------------------------------------------------------------
BADGE_KEYWORDS = {
    "captain": ["captain"],
    "star": ["super star", "superstar", "star player", "legend", "national hero", "talisman"],
    "breakout": ["teenage sensation", "wonderkid", "prodigy", "on the rise", "going places", "newcomer", "teen ", "rising"],
    "gem": ["one to watch", "late bloomer", "hidden gem", "surprise call-up", "going places", "under the radar"],
    "defender": ["defensive rock", "defensive leader", "no-nonsense", "rock", "colossus", "defensive stalwart", "ball-playing"],
    "midfielder": ["midfield engine", "creative force", "box-to-box", "key midfielder", "maestro", "playmaker", "running machine", "engine"],
    "attacker": ["goal machine", "main goalscorer", "goal threat", "game-changer", "lethal", "goal "],
}

BADGE_LABELS = {
    "star": "⭐ Star Player",
    "captain": "🎯 Captain",
    "breakout": "🚀 Breakout Kid",
    "gem": "💎 Hidden Gem",
    "defender": "🛡️ Defensive Stalwart",
    "midfielder": "🎩 Midfield Maestro",
    "attacker": "⚽ Attack Machine",
}
BADGE_POS = {  # position restriction for the positional badges
    "defender": "Defender",
    "midfielder": "Midfielder",
    "attacker": "Forward",
}


def assign_badges(team_name, players):
    """Return dict badge_key -> player_name."""
    overrides = C.BADGE_OVERRIDES.get(team_name, {})
    by_name = {p["name"]: p for p in players}
    chosen = {}

    def find_override(name):
        if not name:
            return None
        if name in by_name:
            return name
        norm = fold(name)
        for pn in by_name:
            if fold(pn) == norm:
                return pn
        # last-name match (accent-insensitive)
        ln = fold(name).split()[-1]
        cands = [pn for pn in by_name if fold(pn).split()[-1] == ln]
        return cands[0] if len(cands) == 1 else None

    for key in ["star", "captain", "breakout", "gem", "defender", "midfielder", "attacker"]:
        # 1) explicit override
        ov = find_override(overrides.get(key))
        if ov:
            chosen[key] = ov
            continue
        # 2) epithet keyword match
        kws = BADGE_KEYWORDS[key]
        posreq = BADGE_POS.get(key)
        cands = []
        for p in players:
            if posreq and p["position"] != posreq:
                continue
            ep = (p.get("epithet") or "").lower()
            if any(k in ep for k in kws):
                cands.append(p)
        if cands:
            if key == "breakout":
                cands.sort(key=lambda p: (p["age"] if p["age"] is not None else 99))
            chosen[key] = cands[0]["name"]
            continue

    # 3) sensible fallbacks
    if "captain" not in chosen:
        for p in players:
            ep = (p.get("epithet") or "").lower()
            if any(k in ep for k in ["leader", "veteran", "experienced"]):
                chosen["captain"] = p["name"]
                break
    if "breakout" not in chosen:
        young = [p for p in players if p["age"] is not None and p["age"] <= 21]
        young.sort(key=lambda p: (0 if p["position"] in ("Forward", "Midfielder") else 1, p["age"]))
        if young:
            chosen["breakout"] = young[0]["name"]
    for key, pos in BADGE_POS.items():
        if key not in chosen:
            grp = [p for p in players if p["position"] == pos]
            if grp:
                chosen[key] = grp[0]["name"]
    if "star" not in chosen:
        chosen["star"] = chosen.get("attacker") or chosen.get("midfielder") or players[0]["name"]
    if "gem" not in chosen:
        young = [p for p in players if p["age"] is not None and p["age"] <= 23]
        if young:
            young.sort(key=lambda p: p["age"])
            chosen["gem"] = young[0]["name"]

    return chosen


# --------------------------------------------------------------------------
# main build
# --------------------------------------------------------------------------
def main():
    squads = json.load(open(SQUAD_JSON, encoding="utf-8"))
    managers, md_groups = parse_md_managers(SQUAD_MD)

    # invert STANDINGS to get group + predicted finish per team
    team_group = {}
    team_finish = {}
    for g, order in C.STANDINGS.items():
        for i, t in enumerate(order):
            team_group[t] = g
            team_finish[t] = i + 1

    teams = []
    warnings = []

    for entry in squads:
        plist = entry["sheets"]["Players"]
        tname = canon(plist[0]["team"])
        code, flag = C.TEAM_CODES.get(tname, ("???", "🏳️"))
        meta = C.TEAM_META.get(tname, {})

        players = []
        for p in plist:
            raw_pos = (p.get("position") or "").strip()
            grp = pos_group(raw_pos)
            yrs, iso = age_at(p.get("date of birth"))
            players.append({
                "name": (p.get("name") or "").strip(),
                "position": grp,
                "detailPosition": raw_pos or grp,
                "number": (p.get("number") or "").strip(),
                "club": (p.get("club") or "").strip(),
                "dob": iso,
                "age": yrs,
                "epithet": (p.get(SPECIAL_FIELD) or "").strip(),
                "bio": (p.get("bio") or "").strip(),
                "shortBio": short_bio(p.get("bio")),
                "photo": (p.get("grid_image") or "").strip(),
                "badges": [],
            })

        badges = assign_badges(tname, players)
        name_to_badges = {}
        for key, pname in badges.items():
            name_to_badges.setdefault(pname, []).append(key)
        for p in players:
            p["badges"] = name_to_badges.get(p["name"], [])

        players.sort(key=lambda p: (POS_ORDER.get(p["position"], 9),
                                    int(p["number"]) if p["number"].isdigit() else 99))

        if tname not in C.RANKS:
            warnings.append(f"no FIFA rank for {tname}")
        if tname not in managers:
            warnings.append(f"no manager parsed for {tname}")
        if tname not in team_group:
            warnings.append(f"no group/standing for {tname}")

        teams.append({
            "name": tname,
            "code": code,
            "flag": flag,
            "group": team_group.get(tname),
            "fifaRank": C.RANKS.get(tname),
            "manager": managers.get(tname, ""),
            "predictedFinish": team_finish.get(tname),
            "advancesAsThird": tname in C.THIRD_PLACE_QUALIFIERS,
            "keyFact": meta.get("keyFact", ""),
            "funFact": meta.get("funFact", ""),
            "strengths": meta.get("strengths", []),
            "weaknesses": meta.get("weaknesses", []),
            "badges": badges,
            "badgeLabels": BADGE_LABELS,
            "players": players,
        })

    teams.sort(key=lambda t: (t["group"] or "Z", t["predictedFinish"] or 9))

    dataset = {
        "meta": {
            "tournament": "FIFA World Cup 2026",
            "hosts": ["United States", "Canada", "Mexico"],
            "kickoff": KICKOFF.isoformat(),
            "final": "2026-07-19",
            "finalVenue": "MetLife Stadium, New Jersey",
            "teamCount": len(teams),
            "rankingNote": "FIFA/Coca-Cola World Ranking, April 2026 (pre-tournament).",
            "picksNote": "Group standings & knockout bracket are Chizoba's own predictions.",
        },
        "badgeLabels": BADGE_LABELS,
        "groups": {g: C.STANDINGS[g] for g in sorted(C.STANDINGS)},
        "thirdPlaceQualifiers": C.THIRD_PLACE_QUALIFIERS,
        "bracket": C.BRACKET,
        "globalLists": enrich_lists(teams),
        "teams": teams,
    }

    os.makedirs(os.path.dirname(OUT_WEB), exist_ok=True)
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    json.dump(dataset, open(OUT_WEB, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # compact teams.json
    compact = [{k: t[k] for k in ("name", "code", "flag", "group", "fifaRank",
                                  "manager", "predictedFinish", "badges")} for t in teams]
    json.dump(compact, open(OUT_TEAMS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # flat CSV
    write_csv(teams)

    print(f"built {len(teams)} teams -> {OUT_WEB}")
    print(f"wrote {OUT_CSV} and {OUT_TEAMS}")
    if warnings:
        print("\nWARNINGS:")
        for w in sorted(set(warnings)):
            print("  -", w)
    else:
        print("no warnings — all teams have rank, manager, group.")


def enrich_lists(teams):
    """Attach club/age/position/flag to each curated global-list entry."""
    index = {}
    for t in teams:
        for p in t["players"]:
            index[(t["name"], fold(p["name"]))] = p
            index[(t["name"], fold(p["name"]).split()[-1])] = p
    out = {}
    for cat, items in C.GLOBAL_LISTS.items():
        enriched = []
        for it in items:
            team = it["team"]
            code, flag = C.TEAM_CODES.get(team, ("", "🏳️"))
            row = dict(it)
            row["flag"] = flag
            row["code"] = code
            p = index.get((team, fold(it["name"]))) or index.get((team, fold(it["name"]).split()[-1]))
            if p:
                row.setdefault("club", p["club"])
                row.setdefault("pos", p["detailPosition"])
                row.setdefault("age", p["age"])
                row.setdefault("photo", p["photo"])
            enriched.append(row)
        out[cat] = enriched
    return out


def write_csv(teams):
    cols = ["group", "team", "fifa_rank", "category", "shirt_number",
            "name", "club", "position_detail", "dob", "age", "badges", "epithet"]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for t in teams:
            # coach row first
            w.writerow([t["group"], t["name"], t["fifaRank"], "Coach", "",
                        t["manager"], "", "Manager", "", "", "", ""])
            for p in t["players"]:
                w.writerow([
                    t["group"], t["name"], t["fifaRank"], p["position"], p["number"],
                    p["name"], p["club"], p["detailPosition"], p["dob"] or "",
                    p["age"] if p["age"] is not None else "",
                    "|".join(p["badges"]), p["epithet"],
                ])


if __name__ == "__main__":
    main()
