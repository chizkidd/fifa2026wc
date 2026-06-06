/* World Cup 2026 interactive hub — vanilla JS, no build step. */
(() => {
  "use strict";
  const app = document.getElementById("app");
  let DATA = null;
  let TEAMS = {}; // name -> team

  const BADGE_ORDER = ["star", "captain", "breakout", "gem", "defender", "midfielder", "attacker"];
  const POS_GROUPS = ["Goalkeeper", "Defender", "Midfielder", "Forward"];
  const POS_LABEL = { Goalkeeper: "Goalkeepers", Defender: "Defenders", Midfielder: "Midfielders", Forward: "Forwards" };
  const CAT_META = {
    superstars: { ico: "⭐", title: "The Superstars", sub: "The established kings who will define the tournament." },
    breakoutKids: { ico: "🚀", title: "The Breakout Kids", sub: "The next global icons, ready to announce themselves." },
    surpriseOfTheTournament: { ico: "🎁", title: "Surprise of the Tournament", sub: "The teams nobody is talking about — yet." },
    onesToWatch: { ico: "👀", title: "Ones to Watch", sub: "Players who could swing a knockout tie on their own." },
    hiddenGems: { ico: "💎", title: "Hidden Gems", sub: "Lesser-known names primed for a breakout and a big move." },
    coachesToWatch: { ico: "🧠", title: "Coaches to Watch", sub: "The minds who decide everything in a short tournament." },
  };

  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const photo = (url, alt) => url
    ? `<img loading="lazy" src="${esc(url)}" alt="${esc(alt)}" referrerpolicy="no-referrer" onerror="this.style.display='none'">`
    : "";

  function badgeChips(keys, labels) {
    return (keys || []).map((k) => {
      const lab = (labels[k] || k).split(" ");
      return `<span class="badge ${k}">${esc(labels[k] || k)}</span>`;
    }).join("");
  }

  /* ---------------- views ---------------- */
  function viewHome() {
    const m = DATA.meta;
    const champ = TEAMS[DATA.bracket.champion];
    const featured = DATA.globalLists.superstars.slice(0, 4);
    return `
      <section class="hero">
        <span class="kicker">Part 3 · The X-Factors, Stars &amp; The Bracket</span>
        <h1>The <span class="hl">2026 World Cup</span><br>has 48 teams. Here's all of it.</h1>
        <p>Every squad, every coach, FIFA ranks, player profiles and badges — plus my group predictions and a full bracket from the Round of 32 to a champion. Explore it, then tell me I'm wrong.</p>
        <div class="hero-meta">
          <div class="chip"><b>48</b><span>Teams</span></div>
          <div class="chip"><b>1,248</b><span>Players</span></div>
          <div class="chip"><b>3</b><span>Host nations 🇺🇸 🇨🇦 🇲🇽</span></div>
          <div class="chip"><b>Jun 11</b><span>Kickoff</span></div>
          <div class="chip"><b>${esc(champ ? champ.flag : "")} ${esc(DATA.bracket.champion)}</b><span>My champion pick</span></div>
        </div>
      </section>

      <div class="section-head"><h2>Start exploring</h2></div>
      <div class="grid cols-3">
        ${navCard("#/groups", "🗺️", "Groups &amp; Teams", "All 12 groups, predicted standings, FIFA ranks. Tap any team for its full squad.")}
        ${navCard("#/watch", "⭐", "Players to Watch", "Superstars, breakout kids, hidden gems and the coaches who'll decide it all.")}
        ${navCard("#/bracket", "🏆", "Bracket Prediction", "My full knockout call — Round of 32 to the final at MetLife.")}
      </div>

      <div class="section-head"><h2>Headline acts</h2><span class="sub">The superstars who define the tournament</span></div>
      <div class="grid cols-4">
        ${featured.map(watchCard).join("")}
      </div>
    `;
  }
  const navCard = (href, ico, title, body) => `
    <a class="group-card" href="${href}" style="padding:22px;display:block">
      <div style="font-size:30px">${ico}</div>
      <h3 style="margin:10px 0 6px;font-size:18px">${title}</h3>
      <p class="muted" style="margin:0;font-size:14px">${body}</p>
    </a>`;

  function viewGroups() {
    const order = Object.keys(DATA.groups).sort();
    return `
      <div class="section-head"><h2>Groups &amp; Predicted Standings</h2>
        <span class="sub">Tap a team for squad, coach &amp; profile · <span style="color:var(--accent)">●</span> top two advance · <span style="color:var(--gold)">●</span> qualifies as best third</span>
      </div>
      <div class="grid cols-3">
        ${order.map(groupCard).join("")}
      </div>`;
  }
  function groupCard(g) {
    const rows = DATA.groups[g].map((tn, i) => {
      const t = TEAMS[tn]; if (!t) return "";
      const adv = t.advancesAsThird ? "adv" : "";
      return `<div class="team-row q${i + 1} ${adv}" data-team="${esc(tn)}">
        <span class="pos">${i + 1}</span>
        <span class="qual-dot"></span>
        <span class="flag">${esc(t.flag)}</span>
        <span class="tn">${esc(tn)}<small>${esc(t.manager)}</small></span>
        <span class="rank">#${t.fifaRank}</span>
      </div>`;
    }).join("");
    return `<div class="group-card">
      <div class="gc-head"><h3>GROUP ${g}</h3><span class="tag">predicted finish</span></div>
      ${rows}
    </div>`;
  }

  function viewTeam(name) {
    const t = TEAMS[name];
    if (!t) return `<p class="loading">Team not found. <a href="#/groups">Back to groups</a></p>`;
    const byPos = {};
    POS_GROUPS.forEach((p) => (byPos[p] = []));
    t.players.forEach((p) => (byPos[p.position] || (byPos[p.position] = [])).push(p));

    const facts = `
      <div class="facts">
        <div class="fact"><h4>Key Fact</h4><p>${esc(t.keyFact)}</p></div>
        <div class="fact fun"><h4>Fun Fact</h4><p>${esc(t.funFact)}</p></div>
      </div>
      <div class="sw">
        <div class="box s"><h4>✅ Strengths</h4><ul>${t.strengths.map((s) => `<li>${esc(s)}</li>`).join("")}</ul></div>
        <div class="box w"><h4>⚠️ Weaknesses</h4><ul>${t.weaknesses.map((s) => `<li>${esc(s)}</li>`).join("")}</ul></div>
      </div>`;

    const squad = POS_GROUPS.map((pos) => {
      const list = byPos[pos]; if (!list || !list.length) return "";
      return `<div class="pos-block">
        <h3>${POS_LABEL[pos]} <span class="faint">· ${list.length}</span></h3>
        <div class="grid cols-4">${list.map(playerCard).join("")}</div>
      </div>`;
    }).join("");

    const fin = t.predictedFinish;
    const finTxt = fin === 1 ? "1st" : fin === 2 ? "2nd" : fin === 3 ? "3rd" : "4th";
    return `
      <a class="back-link" href="#/groups">← All groups</a>
      <div class="team-hero">
        <div class="big-flag">${esc(t.flag)}</div>
        <div style="flex:1;min-width:240px">
          <h1>${esc(t.name)}</h1>
          <div class="th-meta">
            <span class="pill rank-pill">FIFA #${t.fifaRank}</span>
            <span class="pill">Group <b>${t.group}</b></span>
            <span class="pill">🧠 <b>${esc(t.manager)}</b></span>
            <span class="pill">My call: <b>${finTxt} in group${fin > 2 && t.advancesAsThird ? " · advances" : ""}</b></span>
          </div>
        </div>
      </div>
      ${facts}
      ${squad}
    `;
  }

  function playerCard(p) {
    const badges = badgeChips(p.badges, DATA.badgeLabels);
    return `<div class="player-card" data-player="${esc(p.name)}" data-team="${esc(p.team || "")}">
      <div class="pc-photo">
        ${p.number ? `<span class="pc-num">${esc(p.number)}</span>` : ""}
        ${photo(p.photo, p.name)}
        ${badges ? `<div class="pc-badges">${badges}</div>` : ""}
      </div>
      <div class="pc-body">
        <div class="nm">${esc(p.name)}</div>
        <div class="meta">${esc(p.detailPosition)}${p.age ? " · " + p.age : ""}<br>${esc(p.club)}</div>
        ${p.epithet ? `<div class="epi">“${esc(p.epithet)}”</div>` : ""}
      </div>
    </div>`;
  }

  function viewWatch() {
    let html = `<div class="section-head"><h2>Players (&amp; Coaches) to Watch</h2>
      <span class="sub">The stars who will define the 2026 World Cup</span></div>`;
    Object.keys(CAT_META).forEach((cat) => {
      const meta = CAT_META[cat];
      const items = DATA.globalLists[cat] || [];
      html += `<div class="cat-title"><span class="ico">${meta.ico}</span>
        <div><h2>${meta.title}</h2><p>${meta.sub}</p></div></div>
        <div class="grid cols-2">${items.map(watchCard).join("")}</div>`;
    });
    return html;
  }
  function watchCard(it) {
    const ph = it.photo
      ? `<img class="wc-photo" loading="lazy" referrerpolicy="no-referrer" src="${esc(it.photo)}" alt="${esc(it.name)}" onerror="this.outerHTML='<div class=&quot;ph-fallback&quot;>${esc(it.flag)}</div>'">`
      : `<div class="ph-fallback">${esc(it.flag)}</div>`;
    const sub = [it.pos, it.age ? it.age + " yrs" : "", it.club].filter(Boolean).join(" · ");
    const clickable = it.name !== it.team; // coaches/teams aren't player cards
    const attrs = clickable ? `data-player="${esc(it.name)}" data-team="${esc(it.team)}" style="cursor:pointer"` : "";
    return `<div class="watch-card" ${attrs}>
      ${ph}
      <div>
        <h4>${esc(it.flag)} ${esc(it.name)}</h4>
        <div class="wmeta">${esc(it.team)}${sub ? " — " + esc(sub) : ""}</div>
        <p>${esc(it.blurb)}</p>
      </div>
    </div>`;
  }

  function viewBracket() {
    const b = DATA.bracket;
    const champ = TEAMS[b.champion] || { flag: "" };
    const tie = (m) => {
      const [a, c, w] = m;
      const A = TEAMS[a] || {}, B = TEAMS[c] || {};
      const sideA = `<span class="side ${w === a ? "win" : "lose"}">${esc(A.flag || "")} ${esc(a)}</span>`;
      const sideB = `<span class="side ${w === c ? "win" : "lose"}">${esc(B.flag || "")} ${esc(c)}</span>`;
      return `<div class="tie">${sideA}<span class="vs">v</span>${sideB}<span class="arrow">→ ${esc(w)}</span></div>`;
    };
    const round = (title, ties) => `<div class="round"><h3>${title}</h3>
      <div class="grid cols-2">${ties.map(tie).join("")}</div></div>`;

    return `
      <div class="champ-banner">
        <div class="cflag">${esc(champ.flag)}</div>
        <div><div class="ct">My Champion</div><h2>${esc(b.champion)} lift the trophy 🏆</h2></div>
      </div>
      <div class="section-head"><h2>The Road to MetLife</h2>
        <span class="sub">My full knockout call · final July 19, MetLife Stadium</span></div>
      <div class="bracket-wrap">
        <div class="rounds">
          ${round("Final", [b.final])}
          ${round("Third-place play-off", [b.third_place])}
          ${round("Semi-finals", b.semi_finals)}
          ${round("Quarter-finals", b.quarter_finals)}
          ${round("Round of 16", b.round_of_16)}
          ${round("Round of 32", b.round_of_32)}
        </div>
        <img class="bracket-img" src="assets/knockout-bracket.png" alt="Knockout bracket prediction">
      </div>`;
  }

  /* ---------------- modal ---------------- */
  function openPlayer(name, teamName) {
    const t = TEAMS[teamName];
    let p = t && t.players.find((x) => x.name === name);
    if (!p) { // search all
      for (const tn in TEAMS) { const f = TEAMS[tn].players.find((x) => x.name === name); if (f) { p = f; break; } }
    }
    if (!p) return;
    const badges = badgeChips(p.badges, DATA.badgeLabels);
    document.getElementById("modalBody").innerHTML = `
      <div class="modal-hero">
        ${p.photo ? `<img referrerpolicy="no-referrer" src="${esc(p.photo)}" alt="${esc(p.name)}" onerror="this.style.display='none'">` : ""}
        <div>
          <div class="mh-num">${esc(t ? t.flag : "")} ${esc(teamName)}${p.number ? " · #" + esc(p.number) : ""}</div>
          <h3>${esc(p.name)}</h3>
          <div class="mh-meta">${esc(p.detailPosition)}${p.age ? " · " + p.age + " yrs" : ""}<br>${esc(p.club)}</div>
        </div>
      </div>
      ${badges ? `<div class="modal-badges">${badges}</div>` : ""}
      <div class="modal-bio">
        ${p.epithet ? `<div class="epi">“${esc(p.epithet)}”</div>` : ""}
        ${esc(p.bio || p.shortBio || "No profile available.")}
      </div>`;
    const modal = document.getElementById("modal");
    modal.hidden = false;
    document.body.style.overflow = "hidden";
  }
  function closeModal() {
    document.getElementById("modal").hidden = true;
    document.body.style.overflow = "";
  }

  /* ---------------- router ---------------- */
  function render() {
    const hash = location.hash || "#/home";
    const parts = hash.replace(/^#\//, "").split("/");
    const route = parts[0] || "home";
    let html;
    if (route === "groups") html = viewGroups();
    else if (route === "team") html = viewTeam(decodeURIComponent(parts.slice(1).join("/")));
    else if (route === "watch") html = viewWatch();
    else if (route === "bracket") html = viewBracket();
    else html = viewHome();
    app.innerHTML = html;
    window.scrollTo(0, 0);
    document.querySelectorAll(".tabs a").forEach((a) =>
      a.classList.toggle("active", a.dataset.route === (route === "team" ? "groups" : route)));
    document.getElementById("tabs").classList.remove("open");
  }

  /* ---------------- events ---------------- */
  document.addEventListener("click", (e) => {
    const teamRow = e.target.closest("[data-team]");
    const playerEl = e.target.closest("[data-player]");
    if (playerEl) {
      e.preventDefault();
      openPlayer(playerEl.dataset.player, playerEl.dataset.team);
      return;
    }
    if (teamRow && teamRow.dataset.team && !teamRow.dataset.player) {
      location.hash = "#/team/" + encodeURIComponent(teamRow.dataset.team);
      return;
    }
    if (e.target.closest("[data-close]")) closeModal();
  });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeModal(); });
  document.getElementById("menuBtn").addEventListener("click", () =>
    document.getElementById("tabs").classList.toggle("open"));
  window.addEventListener("hashchange", render);

  /* ---------------- boot ---------------- */
  fetch("data/wc2026.json")
    .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then((d) => {
      DATA = d;
      d.teams.forEach((t) => {
        t.players.forEach((p) => (p.team = t.name)); // backref for modal
        TEAMS[t.name] = t;
      });
      render();
    })
    .catch((err) => {
      app.innerHTML = `<p class="loading">Couldn't load tournament data (${esc(err.message)}).<br>
        If you opened this file directly, run a local server:<br>
        <code>cd site &amp;&amp; python3 -m http.server 8000</code></p>`;
    });
})();
