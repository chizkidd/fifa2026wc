# ⚽ World Cup 2026 Hub

Everything behind **Part 3** of my [substack](https://chizobao.substack.com) 2026 World Cup series: a clean dataset of all 48 squads, an interactive website, the curated watch lists, and the article in two forms.

> **A note on the picks:** group standings and the knockout bracket are *my own predictions* (from `assets/`). FIFA rankings are the April 2026 (pre-tournament) edition. Squad lists, bios and player photos come from the Guardian's World Cup 2026 player guide (`2026-fifa-wc-guardian-squad.json`) and the squad markdown (`fifa2026wc-squads.md`), used for reference, not republished wholesale.

## What's in here

```
.
├── 2026-fifa-wc-guardian-squad.json   # source: rich per-player data (bio, DOB, club, photo, epithet)
├── fifa2026wc-squads.md / .txt        # source: groups + squads + managers
├── assets/                            # my group-standings + bracket images
├── scripts/
│   ├── curated.py                     # editorial layer: ranks, standings, bracket, team profiles, badges, lists
│   └── build.py                       # pipeline → builds the dataset, CSV, site data
├── data/
│   ├── players.csv                    # flat squad table (coach + GK/DEF/MID/FWD, badges, ages)
│   └── teams.json                     # compact per-team summary
├── site/                              # the interactive website (static, no build step)
│   ├── index.html · styles.css · app.js
│   └── data/wc2026.json               # generated dataset the site reads
├── vercel.json · netlify.toml         # deploy configs
```

## The dataset

Per **team**: FIFA rank, group, manager, predicted finish, key fact, fun fact, strengths, weaknesses, and seven badge picks.<br>
Per **player** (1,248 of them): name, position, club, age, shirt number, full bio + a short bio, photo, the Guardian "special player" epithet, and any badges.

**Badges:** ⭐ Star Player · 🎯 Captain · 🚀 Breakout Kid · 💎 Hidden Gem · 🛡️ Defensive Stalwart · 🎩 Midfield Maestro · ⚽ Attack Machine. Marquee names are pinned in `scripts/curated.py → BADGE_OVERRIDES`; the rest are derived automatically from the squad data + epithets.

### Rebuild it

```bash
python3 scripts/build.py
```

Regenerates `site/data/wc2026.json`, `data/players.csv` and `data/teams.json`. The build prints a warning for any team missing a rank, manager or group (currently: none).

## Run the website locally

It's a dependency-free static site (vanilla JS, hash routing). Don't open `index.html` via `file://`, the browser blocks `fetch`. Serve it:

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

**Views:** Overview · Groups (predicted standings + FIFA ranks, tap a team) · Team detail (profile, strengths/weaknesses, full squad with badges, tap a player for their bio) · Players to Watch (the six lists) · Bracket (the full knockout call + the bracket image).

## Deploy (Vercel or Netlify)

The site is fully static. The configs point both hosts at `site/`.

- **Vercel:** import the repo. `vercel.json` sets the output directory to `site/` with no build step. (Or just set *Root Directory → `site`* in the dashboard.)
- **Netlify:** import the repo. `netlify.toml` sets `publish = "site"` with no build command. (Or drag the `site/` folder into Netlify Drop.)

No environment variables, no server, no build needed.

## Deliverables map

| Task | Where it is |
|---|---|
| Squads grouped by coach/GK/DEF/MID/FWD, in a usable format | `data/players.csv`, `site/data/wc2026.json` |
| Interactive site (groups, FIFA rank, team facts, player cards, badges) | `site/` → deploy to Vercel/Netlify |
