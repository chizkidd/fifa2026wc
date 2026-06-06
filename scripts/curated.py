# -*- coding: utf-8 -*-
"""
Hand-authored data for the FIFA World Cup 2026 hub.

Everything here is *editorial* / reference data layered on top of the raw
Guardian squad JSON (2026-fifa-wc-guardian-squad.json) and the squad markdown
(fifa2026wc-squads.md). Keys use the CANONICAL team names that come out of the
Guardian JSON (see TEAM_CODES for the full list).

Sources:
  - Predicted group standings + knockout bracket: Chizoba's own picks
    (assets/groups-*.jpeg and assets/knockout-bracket.png).
  - FIFA/Coca-Cola World Ranking, April 2026 edition (pre-tournament).
"""

# ---------------------------------------------------------------------------
# Canonical team name -> (3-letter code, flag emoji)
# ---------------------------------------------------------------------------
TEAM_CODES = {
    "Czechia": ("CZE", "🇨🇿"),
    "Mexico": ("MEX", "🇲🇽"),
    "South Africa": ("RSA", "🇿🇦"),
    "South Korea": ("KOR", "🇰🇷"),
    "Bosnia and Herzegovina": ("BIH", "🇧🇦"),
    "Canada": ("CAN", "🇨🇦"),
    "Qatar": ("QAT", "🇶🇦"),
    "Switzerland": ("SUI", "🇨🇭"),
    "Brazil": ("BRA", "🇧🇷"),
    "Haiti": ("HAI", "🇭🇹"),
    "Morocco": ("MAR", "🇲🇦"),
    "Scotland": ("SCO", "🏴󠁧󠁢󠁳󠁣󠁴󠁿"),
    "Australia": ("AUS", "🇦🇺"),
    "Paraguay": ("PAR", "🇵🇾"),
    "Turkey": ("TUR", "🇹🇷"),
    "USA": ("USA", "🇺🇸"),
    "Curaçao": ("CUW", "🇨🇼"),
    "Ecuador": ("ECU", "🇪🇨"),
    "Germany": ("GER", "🇩🇪"),
    "Côte d'Ivoire": ("CIV", "🇨🇮"),
    "Japan": ("JPN", "🇯🇵"),
    "Netherlands": ("NED", "🇳🇱"),
    "Sweden": ("SWE", "🇸🇪"),
    "Tunisia": ("TUN", "🇹🇳"),
    "Belgium": ("BEL", "🇧🇪"),
    "Egypt": ("EGY", "🇪🇬"),
    "Iran": ("IRN", "🇮🇷"),
    "New Zealand": ("NZL", "🇳🇿"),
    "Cape Verde": ("CPV", "🇨🇻"),
    "Saudi Arabia": ("KSA", "🇸🇦"),
    "Spain": ("ESP", "🇪🇸"),
    "Uruguay": ("URU", "🇺🇾"),
    "France": ("FRA", "🇫🇷"),
    "Iraq": ("IRQ", "🇮🇶"),
    "Norway": ("NOR", "🇳🇴"),
    "Senegal": ("SEN", "🇸🇳"),
    "Algeria": ("ALG", "🇩🇿"),
    "Argentina": ("ARG", "🇦🇷"),
    "Austria": ("AUT", "🇦🇹"),
    "Jordan": ("JOR", "🇯🇴"),
    "Colombia": ("COL", "🇨🇴"),
    "DR Congo": ("COD", "🇨🇩"),
    "Portugal": ("POR", "🇵🇹"),
    "Uzbekistan": ("UZB", "🇺🇿"),
    "Croatia": ("CRO", "🇭🇷"),
    "England": ("ENG", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
    "Ghana": ("GHA", "🇬🇭"),
    "Panama": ("PAN", "🇵🇦"),
}

# ---------------------------------------------------------------------------
# Name normalisation: maps the spellings used in the squad markdown / images
# to the canonical Guardian-JSON spelling above.
# ---------------------------------------------------------------------------
NAME_ALIASES = {
    "United States": "USA",
    "Bosnia-Herzegovina": "Bosnia and Herzegovina",
    "Türkiye": "Turkey",
    "Turkiye": "Turkey",
    "Curacao": "Curaçao",
    "Ivory Coast": "Côte d'Ivoire",
    "Congo DR": "DR Congo",
    "Cote d'Ivoire": "Côte d'Ivoire",
    # image 3-letter codes -> canonical
    "MEX": "Mexico", "KOR": "South Korea", "CZE": "Czechia", "RSA": "South Africa",
    "SWI": "Switzerland", "CAN": "Canada", "BIH": "Bosnia and Herzegovina", "QAT": "Qatar",
    "BRA": "Brazil", "MOR": "Morocco", "SCO": "Scotland", "HAI": "Haiti",
    "TUR": "Turkey", "USA": "USA", "AUS": "Australia", "PAR": "Paraguay",
    "GER": "Germany", "CIV": "Côte d'Ivoire", "ECU": "Ecuador", "CUR": "Curaçao",
    "NED": "Netherlands", "JPN": "Japan", "SWE": "Sweden", "TUN": "Tunisia",
    "BEL": "Belgium", "EGY": "Egypt", "IRN": "Iran", "NZL": "New Zealand",
    "SPA": "Spain", "URU": "Uruguay", "CPV": "Cape Verde", "SAU": "Saudi Arabia",
    "FRA": "France", "SEN": "Senegal", "NOR": "Norway", "IRQ": "Iraq",
    "ARG": "Argentina", "AUT": "Austria", "ALG": "Algeria", "JOR": "Jordan",
    "POR": "Portugal", "COL": "Colombia", "DRC": "DR Congo", "UZB": "Uzbekistan",
    "ENG": "England", "CRO": "Croatia", "GHA": "Ghana", "PAN": "Panama",
}

# ---------------------------------------------------------------------------
# FIFA/Coca-Cola World Ranking — April 2026 (pre-tournament).
# ---------------------------------------------------------------------------
RANKS = {
    "France": 1, "Spain": 2, "Argentina": 3, "England": 4, "Portugal": 5,
    "Brazil": 6, "Netherlands": 7, "Morocco": 8, "Belgium": 9, "Germany": 10,
    "Croatia": 11, "Colombia": 13, "Senegal": 14, "Mexico": 15, "USA": 16,
    "Uruguay": 17, "Japan": 18, "Switzerland": 19, "Iran": 21, "Turkey": 22,
    "Ecuador": 23, "Austria": 24, "South Korea": 25, "Australia": 27,
    "Algeria": 28, "Egypt": 29, "Canada": 30, "Norway": 31, "Panama": 33,
    "Côte d'Ivoire": 34, "Sweden": 38, "Paraguay": 40, "Czechia": 41,
    "Scotland": 43, "Tunisia": 44, "DR Congo": 46, "Uzbekistan": 50,
    "Qatar": 55, "Iraq": 57, "South Africa": 60, "Saudi Arabia": 61,
    "Jordan": 63, "Bosnia and Herzegovina": 65, "Cape Verde": 69, "Ghana": 74,
    "Curaçao": 82, "Haiti": 83, "New Zealand": 85,
}

# ---------------------------------------------------------------------------
# Predicted group finishing order (Chizoba's picks, top -> bottom).
# ---------------------------------------------------------------------------
STANDINGS = {
    "A": ["Mexico", "South Korea", "Czechia", "South Africa"],
    "B": ["Switzerland", "Canada", "Bosnia and Herzegovina", "Qatar"],
    "C": ["Brazil", "Morocco", "Scotland", "Haiti"],
    "D": ["Turkey", "USA", "Australia", "Paraguay"],
    "E": ["Germany", "Côte d'Ivoire", "Ecuador", "Curaçao"],
    "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "G": ["Belgium", "Egypt", "Iran", "New Zealand"],
    "H": ["Spain", "Uruguay", "Cape Verde", "Saudi Arabia"],
    "I": ["France", "Senegal", "Norway", "Iraq"],
    "J": ["Argentina", "Austria", "Algeria", "Jordan"],
    "K": ["Portugal", "Colombia", "DR Congo", "Uzbekistan"],
    "L": ["England", "Croatia", "Ghana", "Panama"],
}

# Eight best third-placed teams that advance (Chizoba's picks).
THIRD_PLACE_QUALIFIERS = [
    "Scotland", "Australia", "Ecuador", "Sweden",
    "Norway", "Algeria", "DR Congo", "Ghana",
]

# ---------------------------------------------------------------------------
# Knockout bracket (Chizoba's picks). Each tie lists [teamA, teamB, winner].
# ---------------------------------------------------------------------------
BRACKET = {
    "round_of_32": [
        ["Germany", "Scotland", "Germany"],
        ["France", "Sweden", "France"],
        ["Canada", "South Korea", "Canada"],
        ["Netherlands", "Morocco", "Netherlands"],
        ["Colombia", "Croatia", "Colombia"],
        ["Spain", "Austria", "Spain"],
        ["Czechia", "Belgium", "Czechia"],
        ["Turkey", "Norway", "Turkey"],
        ["Brazil", "Japan", "Brazil"],
        ["Côte d'Ivoire", "Senegal", "Senegal"],
        ["Mexico", "Ecuador", "Ecuador"],
        ["England", "DR Congo", "England"],
        ["Argentina", "Uruguay", "Argentina"],
        ["USA", "Egypt", "USA"],
        ["Switzerland", "Algeria", "Switzerland"],
        ["Portugal", "Ghana", "Portugal"],
    ],
    "round_of_16": [
        ["Germany", "France", "France"],
        ["Canada", "Netherlands", "Netherlands"],
        ["Colombia", "Spain", "Spain"],
        ["Czechia", "Turkey", "Czechia"],
        ["Brazil", "Senegal", "Brazil"],
        ["Ecuador", "England", "England"],
        ["Argentina", "USA", "Argentina"],
        ["Switzerland", "Portugal", "Portugal"],
    ],
    "quarter_finals": [
        ["France", "Netherlands", "France"],
        ["Spain", "Czechia", "Spain"],
        ["Brazil", "England", "Brazil"],
        ["Argentina", "Portugal", "Argentina"],
    ],
    "semi_finals": [
        ["France", "Spain", "France"],
        ["Brazil", "Argentina", "Brazil"],
    ],
    "third_place": ["Spain", "Argentina", "Spain"],
    "final": ["France", "Brazil", "France"],
    "champion": "France",
}

# ---------------------------------------------------------------------------
# Per-team profile: key fact, fun fact, strengths, weaknesses.
# ---------------------------------------------------------------------------
TEAM_META = {
    "Mexico": {
        "keyFact": "Co-hosts and a fixture at every World Cup since 1994, chasing the elusive 'quinto partido' — a first run past the round of 16 since 1986.",
        "funFact": "The Estadio Azteca will become the first stadium to host matches at three different men's World Cups (1970, 1986, 2026).",
        "strengths": ["Home advantage and a raucous crowd", "Deep, experienced spine", "Tournament know-how"],
        "weaknesses": ["History of freezing in the round of 16", "Reliance on an ageing core", "Inconsistent goalscoring"],
    },
    "South Africa": {
        "keyFact": "Bafana Bafana are back at the World Cup for the first time since they hosted it in 2010.",
        "funFact": "Their squad leans heavily on champions Mamelodi Sundowns, the backbone of the national side.",
        "strengths": ["Cohesive, club-based core", "Athleticism and pace", "Belief from a strong qualifying run"],
        "weaknesses": ["Limited big-tournament experience", "Lack of a proven elite striker", "Largely home-based squad"],
    },
    "South Korea": {
        "keyFact": "Asia's most reliable qualifiers, reaching an 11th straight World Cup.",
        "funFact": "Captain Son Heung-min swapped the Premier League for MLS with LAFC ahead of the tournament.",
        "strengths": ["World-class talisman in Son", "European-based attackers", "Relentless work rate"],
        "weaknesses": ["Defensive fragility", "Over-dependence on Son", "Thin at centre-forward"],
    },
    "Czechia": {
        "keyFact": "Back at the World Cup after missing 2018 and 2022, sealing it through the play-offs.",
        "funFact": "Goalkeeper Matej Kovar has won league titles in three different countries — Czechia, Germany and the Netherlands.",
        "strengths": ["Organised, physical defence", "Set-piece threat", "Battle-hardened from play-offs"],
        "weaknesses": ["Short on top-end creativity", "Questions in goal", "Limited squad depth"],
    },
    "Switzerland": {
        "keyFact": "Quietly consistent, the Swiss have reached the knockout stage at four of the last five major tournaments.",
        "funFact": "Captain Granit Xhaka dropped to the Championship with Sunderland yet remains the team's metronome.",
        "strengths": ["Tournament resilience", "Leadership and experience", "Solid defensive structure"],
        "weaknesses": ["Ageing midfield", "Lack of a clinical striker", "Can be passive in big games"],
    },
    "Canada": {
        "keyFact": "Co-hosts who are far more dangerous than at their 2022 return, now coached by Jesse Marsch.",
        "funFact": "Alphonso Davies and Jonathan David give Canada genuine top-table speed and finishing.",
        "strengths": ["Electric pace out wide", "Improved tactical identity", "Home crowds"],
        "weaknesses": ["Shaky in central defence", "Tournament inexperience", "Squad depth behind the stars"],
    },
    "Qatar": {
        "keyFact": "The 2022 hosts return as Asian Cup winners, this time having actually qualified on the pitch.",
        "funFact": "Akram Afif, their talisman, famously produced a 'magic trick' card celebration at the Asian Cup.",
        "strengths": ["Settled, well-drilled unit", "Match-winner in Afif", "Asian Cup-winning belief"],
        "weaknesses": ["Untested against elite opposition", "Domestic-league heavy squad", "Lack of physicality"],
    },
    "Brazil": {
        "keyFact": "Five-time champions chasing a first title since 2002, now under Carlo Ancelotti — their first permanent foreign manager.",
        "funFact": "Ancelotti is the first non-Brazilian to lead the Seleção at a World Cup.",
        "strengths": ["Frightening attacking depth", "Elite individual quality", "Ancelotti's tournament pedigree"],
        "weaknesses": ["Defensive reliability", "Midfield balance", "Weight of expectation"],
    },
    "Morocco": {
        "keyFact": "The 2022 semi-finalists who stunned the world are now Africa's highest-ranked side and no longer underdogs.",
        "funFact": "They were the first African and first Arab nation to reach a World Cup semi-final.",
        "strengths": ["Elite, organised defence", "World-class wide players", "Unshakeable team spirit"],
        "weaknesses": ["Reliable centre-forward", "Pressure of expectation", "Squad rotation depth"],
    },
    "Haiti": {
        "keyFact": "A fairy-tale return to the World Cup for the first time since 1974, only their second ever appearance.",
        "funFact": "Much of their qualifying campaign was played away from home due to instability in Haiti.",
        "strengths": ["Nothing to lose mentality", "Diaspora talent", "Genuine pace"],
        "weaknesses": ["Vast gulf in experience", "Defensive organisation", "Lack of preparation time"],
    },
    "Scotland": {
        "keyFact": "Back at a World Cup for the first time since 1998, ending a 28-year wait.",
        "funFact": "The Tartan Army travels in numbers few nations can match — expect a sea of kilts.",
        "strengths": ["Quality wing-backs", "Set-piece danger", "Togetherness and intensity"],
        "weaknesses": ["Goals from open play", "Thin striking options", "History of group-stage exits"],
    },
    "USA": {
        "keyFact": "Co-hosts and the centre of the tournament, under huge pressure to deliver a deep run on home soil.",
        "funFact": "This is the first 48-team World Cup, and the US will play the opener as one of the lead hosts.",
        "strengths": ["Young, European-based core", "Home advantage", "Pace and athleticism"],
        "weaknesses": ["No reliable No.9", "Defensive lapses", "Managing expectation"],
    },
    "Paraguay": {
        "keyFact": "Back at the World Cup for the first time since 2010, ending a long absence.",
        "funFact": "Veteran Gustavo Gómez anchors a defence built on classic Paraguayan grit.",
        "strengths": ["Defensive resilience", "Physicality", "Counter-attacking threat"],
        "weaknesses": ["Lack of cutting edge", "Limited creativity", "Long absence from the big stage"],
    },
    "Turkey": {
        "keyFact": "A gifted young generation, led by Arda Güler, returning to the World Cup after missing the last two.",
        "funFact": "Real Madrid's Arda Güler is the jewel of a genuinely thrilling Turkish attack.",
        "strengths": ["Exciting young creators", "Goals throughout the team", "Attacking ambition"],
        "weaknesses": ["Defensive discipline", "Tournament inexperience", "Emotional volatility"],
    },
    "Australia": {
        "keyFact": "The Socceroos reach a sixth consecutive World Cup, ever-reliable in the knockout-or-bust moments.",
        "funFact": "Teenager Nestory Irankunda is one of the tournament's most-hyped breakout prospects.",
        "strengths": ["Organisation and fitness", "Never-say-die spirit", "Emerging young talent"],
        "weaknesses": ["Lack of star quality", "Goalscoring", "Ageing in key areas"],
    },
    "Germany": {
        "keyFact": "Four-time champions rebuilding under Julian Nagelsmann after dismal recent World Cups.",
        "funFact": "Florian Wirtz and Jamal Musiala headline the most exciting German attack in a decade.",
        "strengths": ["Outstanding creative midfield", "Big-tournament DNA", "Tactical flexibility"],
        "weaknesses": ["Centre-back stability", "Reliable goalscorer", "Recent fragility under pressure"],
    },
    "Côte d'Ivoire": {
        "keyFact": "The reigning Africa Cup of Nations champions, who won it on home soil in 2024.",
        "funFact": "Their 2024 AFCON title came after they nearly went out in the group stage — the ultimate comeback.",
        "strengths": ["Power and pace in attack", "Winning momentum", "Strong spine"],
        "weaknesses": ["Squad consistency", "Defensive concentration", "Big-stage World Cup pedigree"],
    },
    "Ecuador": {
        "keyFact": "A young, fearless side with one of the best defensive records in South American qualifying.",
        "funFact": "Moisés Caicedo, the world's most expensive midfielder, drives the team from deep.",
        "strengths": ["Miserly defence", "Elite midfield engine", "Youth and energy"],
        "weaknesses": ["Lack of goals", "Inexperience in attack", "Squad depth"],
    },
    "Curaçao": {
        "keyFact": "The smallest nation ever to qualify for a World Cup — a Caribbean island of around 150,000 people.",
        "funFact": "Their squad is built almost entirely from Dutch-born players of Curaçaoan heritage.",
        "strengths": ["Surprise factor", "Dutch-schooled technique", "Fearlessness"],
        "weaknesses": ["Tiny talent pool", "No World Cup experience", "Physical mismatch with elites"],
    },
    "Netherlands": {
        "keyFact": "Perennial contenders chasing a first-ever World Cup title after three final defeats.",
        "funFact": "The Dutch have lost three World Cup finals (1974, 1978, 2010) without ever lifting the trophy.",
        "strengths": ["Elite individuals across the pitch", "Tactical intelligence", "Big-game experience"],
        "weaknesses": ["Recurring defensive doubts", "Squad harmony", "Tendency to underwhelm"],
    },
    "Japan": {
        "keyFact": "Asia's standard-bearers, who have openly set winning the World Cup as their goal.",
        "funFact": "Japan beat both Germany and Spain in the 2022 group stage before falling in the last 16.",
        "strengths": ["Superb technical level", "European-based squad", "High-energy pressing"],
        "weaknesses": ["Knockout-round ceiling", "Aerial vulnerability", "Clinical finishing"],
    },
    "Sweden": {
        "keyFact": "Back at the World Cup with a fearsome new strike pairing after missing 2022.",
        "funFact": "Alexander Isak and Viktor Gyökeres may be the most expensive forward line at the tournament.",
        "strengths": ["World-class strikers", "Set-piece threat", "Physical presence"],
        "weaknesses": ["Creativity in midfield", "Pace in defence", "Over-reliance on the front two"],
    },
    "Tunisia": {
        "keyFact": "Reliable African qualifiers, back for a third straight World Cup.",
        "funFact": "Tunisia famously beat holders France in the 2022 group stage.",
        "strengths": ["Defensive organisation", "Tournament experience", "Discipline"],
        "weaknesses": ["Lack of attacking quality", "Goalscoring", "Squad star power"],
    },
    "Belgium": {
        "keyFact": "A new-look side trying to move past the faded 'golden generation' tag.",
        "funFact": "Kevin De Bruyne, now in MLS, remains the creative heartbeat at what could be his last World Cup.",
        "strengths": ["Elite creativity", "Goal threat in Lukaku", "Emerging young talent"],
        "weaknesses": ["Ageing defence", "Goalkeeping questions", "Transition between generations"],
    },
    "Egypt": {
        "keyFact": "Back at the World Cup for the first time since 2018, built around a generational talent.",
        "funFact": "Mohamed Salah carried the qualifying campaign almost single-handedly with his goals.",
        "strengths": ["A genuine superstar in Salah", "Defensive solidity", "Experience"],
        "weaknesses": ["Over-reliance on Salah", "Lack of secondary scorers", "Depth in attack"],
    },
    "Iran": {
        "keyFact": "Asia's most consistent qualifiers, reaching a fourth consecutive World Cup.",
        "funFact": "Mehdi Taremi and Sardar Azmoun give Iran one of Asia's most experienced strike forces.",
        "strengths": ["Defensive discipline", "Experienced forwards", "Physical resilience"],
        "weaknesses": ["Struggle to break down deep blocks", "Squad ageing", "Off-pitch disruption"],
    },
    "New Zealand": {
        "keyFact": "Oceania's flag-bearers, back at the World Cup for the first time since 2010.",
        "funFact": "The All Whites have never lost a match at a World Cup finals (three draws in 2010).",
        "strengths": ["Team spirit", "Aerial strength", "Nothing-to-lose mentality"],
        "weaknesses": ["Huge gulf in quality", "Lack of elite experience", "Limited squad depth"],
    },
    "Cape Verde": {
        "keyFact": "The Blue Sharks reach their first-ever World Cup — one of the great qualifying stories.",
        "funFact": "With a population of around 500,000, they are among the smallest nations ever to qualify.",
        "strengths": ["Fearless underdog spirit", "Diaspora-fuelled talent", "Strong unity"],
        "weaknesses": ["No World Cup pedigree", "Squad depth", "Step up in class"],
    },
    "Saudi Arabia": {
        "keyFact": "Regular qualifiers and future hosts (2034), aiming to build on their famous 2022 win over Argentina.",
        "funFact": "Their 2-1 victory over eventual champions Argentina in 2022 was one of the great World Cup shocks.",
        "strengths": ["Organisation and discipline", "Home-league cohesion", "Capacity for a shock"],
        "weaknesses": ["Lack of European experience", "Goalscoring", "Inconsistency"],
    },
    "Spain": {
        "keyFact": "Reigning European champions and many people's favourites, blending tiki-taka with ruthless youth.",
        "funFact": "Lamine Yamal could become one of the youngest superstars ever to dominate a World Cup.",
        "strengths": ["Best midfield in the world", "Generational young talent", "Possession dominance"],
        "weaknesses": ["No out-and-out elite striker", "High defensive line", "Pressure of favouritism"],
    },
    "Uruguay": {
        "keyFact": "A dangerous, well-coached side under Marcelo Bielsa blending grizzled winners and exciting youth.",
        "funFact": "Bielsa's intense, all-action style has transformed a traditionally pragmatic Uruguay.",
        "strengths": ["Bielsa's tactical edge", "Blend of youth and experience", "Defensive steel"],
        "weaknesses": ["Squad fitness under Bielsa's demands", "Discipline", "Depth at the back"],
    },
    "France": {
        "keyFact": "Beaten 2022 finalists and the world's No.1 side — the most complete squad in the tournament.",
        "funFact": "Captain Kylian Mbappé is already among France's all-time leading World Cup scorers at just 27.",
        "strengths": ["Frightening squad depth", "World's best attacker in Mbappé", "Winning experience"],
        "weaknesses": ["Midfield balance", "Occasional complacency", "Internal harmony"],
    },
    "Iraq": {
        "keyFact": "The Lions of Mesopotamia return to the World Cup for the first time since 1986.",
        "funFact": "Iraq's only previous World Cup appearance came 40 years ago in Mexico 1986.",
        "strengths": ["Passionate support", "Underdog freedom", "Emerging talent"],
        "weaknesses": ["Massive experience gap", "Defensive frailty", "Step up in level"],
    },
    "Norway": {
        "keyFact": "Back at the World Cup for the first time since 1998, dragged there by a generational attack.",
        "funFact": "Erling Haaland and Martin Ødegaard finally bring Norway's superstars to the global stage.",
        "strengths": ["Two world-class talents", "Goalscoring power", "Momentum and belief"],
        "weaknesses": ["Defensive quality", "Tournament inexperience", "Depth behind the stars"],
    },
    "Senegal": {
        "keyFact": "Former AFCON champions and Africa's powerhouse, packed with Premier League quality.",
        "funFact": "Sadio Mané remains the iconic figure of Senegal's golden generation.",
        "strengths": ["Power and pace everywhere", "Elite defenders and keeper", "Strong spine"],
        "weaknesses": ["Reliable goalscorer", "Squad harmony", "Converting dominance into goals"],
    },
    "Algeria": {
        "keyFact": "Back at the World Cup after missing 2018 and 2022, built around a thrilling forward line.",
        "funFact": "The Desert Foxes reached the last 16 in 2014, their best-ever World Cup run.",
        "strengths": ["Pace and flair in attack", "Match-winners out wide", "Technical quality"],
        "weaknesses": ["Defensive consistency", "Big-game temperament", "Balance"],
    },
    "Argentina": {
        "keyFact": "Defending world champions chasing back-to-back titles in what is likely Lionel Messi's farewell.",
        "funFact": "A second straight crown would put this Argentina side among the greatest of all time.",
        "strengths": ["Winning machine mentality", "Messi's genius", "Deep, balanced squad"],
        "weaknesses": ["Ageing core", "Reliance on Messi", "Defensive pace"],
    },
    "Austria": {
        "keyFact": "An organised, well-coached side enjoying a strong run under Ralf Rangnick.",
        "funFact": "Rangnick, the godfather of modern gegenpressing, has turned Austria into a pressing machine.",
        "strengths": ["Relentless pressing", "Tactical organisation", "Strong collective"],
        "weaknesses": ["Lack of a superstar", "Goalscoring", "Squad depth"],
    },
    "Jordan": {
        "keyFact": "A historic first-ever World Cup qualification for the Chastity Eagles.",
        "funFact": "Jordan stunned the continent by reaching the 2023 Asian Cup final.",
        "strengths": ["Fearless underdogs", "Counter-attacking threat", "Strong team unity"],
        "weaknesses": ["No World Cup experience", "Quality gap", "Squad depth"],
    },
    "Colombia": {
        "keyFact": "Back at the World Cup after missing 2022, blending flair with a strong qualifying run.",
        "funFact": "Luis Díaz leads a Colombia side that beat Brazil and Argentina during qualifying.",
        "strengths": ["Star power in Díaz", "Technical midfield", "Attacking flair"],
        "weaknesses": ["Defensive lapses", "Consistency", "Squad depth at the back"],
    },
    "DR Congo": {
        "keyFact": "The Leopards return to the World Cup for the first time since 1974, when they played as Zaire.",
        "funFact": "As Zaire in 1974, they were the first sub-Saharan African nation to reach a World Cup.",
        "strengths": ["Athleticism and power", "Emerging European-based talent", "Underdog spirit"],
        "weaknesses": ["Huge experience gap", "Defensive organisation", "Tournament naivety"],
    },
    "Portugal": {
        "keyFact": "A golden generation chasing the trophy in what is almost certainly Cristiano Ronaldo's final World Cup.",
        "funFact": "Ronaldo is the only player to score at five different World Cups.",
        "strengths": ["Extraordinary squad depth", "Elite attacking options", "Big-game experience"],
        "weaknesses": ["Balancing Ronaldo and the new generation", "Defensive age", "Tactical clarity"],
    },
    "Uzbekistan": {
        "keyFact": "A historic first-ever World Cup qualification for the White Wolves.",
        "funFact": "Uzbekistan reached the finals on the back of one of Asia's most impressive young cores.",
        "strengths": ["Exciting young talent", "Underdog freedom", "Strong team identity"],
        "weaknesses": ["No World Cup experience", "Quality gap with elites", "Squad depth"],
    },
    "Croatia": {
        "keyFact": "Beaten 2018 finalists and 2022 semi-finalists who simply refuse to fade.",
        "funFact": "Luka Modrić is set to become one of the oldest outfield players in World Cup history.",
        "strengths": ["Elite midfield control", "Tournament know-how", "Mental toughness"],
        "weaknesses": ["Ageing spine", "Lack of pace", "Goalscoring"],
    },
    "England": {
        "keyFact": "Perennial nearly-men, top-four ranked and desperate to end a trophy drought since 1966.",
        "funFact": "England have reached a final and two semis in recent major tournaments without winning any.",
        "strengths": ["Extraordinary attacking depth", "Elite individuals", "Tournament experience"],
        "weaknesses": ["History of choking", "Midfield balance", "Pressure and scrutiny"],
    },
    "Ghana": {
        "keyFact": "The Black Stars return hungry to restore pride after a group-stage exit in 2022.",
        "funFact": "Ghana came within a missed penalty of reaching the semi-finals back in 2010.",
        "strengths": ["Athletic, powerful squad", "Emerging European talent", "Passionate support"],
        "weaknesses": ["Defensive reliability", "Consistency", "Finishing"],
    },
    "Panama": {
        "keyFact": "A vastly improved side reaching their second-ever World Cup, now genuinely competitive.",
        "funFact": "Panama reached the 2023 Concacaf Gold Cup final, signalling their rise.",
        "strengths": ["Defensive organisation", "Team spirit", "Set-piece threat"],
        "weaknesses": ["Lack of elite quality", "Goalscoring", "Experience against top sides"],
    },
}

# ---------------------------------------------------------------------------
# Badge overrides. The build script auto-assigns badges from the Guardian
# "special player" epithets, but for the marquee names we pin them explicitly
# so the obvious star/captain is never missed. Names must match the squad.
# Badge keys: star, captain, breakout, gem, defender, midfielder, attacker
# ---------------------------------------------------------------------------
BADGE_OVERRIDES = {
    "France": {"star": "Kylian Mbappé", "captain": "Kylian Mbappé", "attacker": "Kylian Mbappé", "midfielder": "Aurélien Tchouaméni", "defender": "William Saliba", "breakout": "Rayan Cherki"},
    "Spain": {"star": "Lamine Yamal", "captain": "Álvaro Morata", "midfielder": "Pedri", "attacker": "Lamine Yamal", "defender": "Pau Cubarsí", "breakout": "Lamine Yamal"},
    "Argentina": {"star": "Lionel Messi", "captain": "Lionel Messi", "attacker": "Julián Álvarez", "midfielder": "Enzo Fernández", "defender": "Cristian Romero", "breakout": "Nico Paz"},
    "Brazil": {"star": "Vinícius Júnior", "attacker": "Vinícius Júnior", "midfielder": "Bruno Guimarães", "defender": "Marquinhos", "captain": "Marquinhos", "breakout": "Endrick"},
    "Portugal": {"star": "Cristiano Ronaldo", "captain": "Cristiano Ronaldo", "attacker": "Cristiano Ronaldo", "midfielder": "Bruno Fernandes", "defender": "Rúben Dias"},
    "England": {"star": "Jude Bellingham", "midfielder": "Jude Bellingham", "captain": "Harry Kane", "attacker": "Harry Kane", "defender": "John Stones"},
    "Germany": {"star": "Florian Wirtz", "midfielder": "Florian Wirtz", "captain": "Joshua Kimmich", "attacker": "Jamal Musiala", "breakout": "Jamal Musiala"},
    "Netherlands": {"star": "Virgil van Dijk", "captain": "Virgil van Dijk", "defender": "Virgil van Dijk", "midfielder": "Frenkie de Jong", "attacker": "Cody Gakpo"},
    "Norway": {"star": "Erling Haaland", "attacker": "Erling Haaland", "captain": "Martin Ødegaard", "midfielder": "Martin Ødegaard"},
    "Belgium": {"star": "Kevin De Bruyne", "captain": "Kevin De Bruyne", "midfielder": "Kevin De Bruyne", "attacker": "Romelu Lukaku"},
    "Egypt": {"star": "Mohamed Salah", "captain": "Mohamed Salah", "attacker": "Mohamed Salah"},
    "Morocco": {"star": "Achraf Hakimi", "captain": "Achraf Hakimi", "defender": "Achraf Hakimi", "midfielder": "Brahim Díaz"},
    "Croatia": {"star": "Luka Modrić", "captain": "Luka Modrić", "midfielder": "Luka Modrić"},
    "Uruguay": {"star": "Federico Valverde", "midfielder": "Federico Valverde", "attacker": "Darwin Núñez"},
    "Colombia": {"star": "Luis Díaz", "captain": "James Rodríguez", "attacker": "Luis Díaz", "midfielder": "James Rodríguez"},
    "Senegal": {"star": "Sadio Mané", "captain": "Kalidou Koulibaly", "attacker": "Nicolas Jackson", "defender": "Kalidou Koulibaly"},
    "Japan": {"star": "Takefusa Kubo", "attacker": "Takefusa Kubo", "midfielder": "Wataru Endo"},
    "Mexico": {"star": "Santiago Gimenez", "captain": "Edson Álvarez", "midfielder": "Edson Álvarez", "attacker": "Raúl Jiménez", "breakout": "Gilberto Mora"},
    "USA": {"star": "Christian Pulisic", "captain": "Christian Pulisic", "attacker": "Christian Pulisic", "midfielder": "Weston McKennie"},
    "Canada": {"star": "Alphonso Davies", "defender": "Alphonso Davies", "attacker": "Jonathan David", "captain": "Alphonso Davies"},
    "Switzerland": {"star": "Granit Xhaka", "captain": "Granit Xhaka", "midfielder": "Granit Xhaka", "defender": "Manuel Akanji"},
    "Turkey": {"star": "Arda Guler", "midfielder": "Arda Guler", "breakout": "Arda Guler", "defender": "Merih Demiral", "attacker": "Kenan Yildiz"},
    "Sweden": {"star": "Alexander Isak", "attacker": "Alexander Isak"},
    "Austria": {"star": "David Alaba", "captain": "David Alaba", "defender": "David Alaba", "midfielder": "Konrad Laimer"},
    "Ecuador": {"star": "Moisés Caicedo", "midfielder": "Moisés Caicedo", "defender": "Piero Hincapié"},
    "South Korea": {"star": "Son Heung-min", "captain": "Son Heung-min", "attacker": "Son Heung-min", "midfielder": "Lee Kang-in", "defender": "Kim Min-Jae"},
    "Côte d'Ivoire": {"star": "Simon Adingra", "attacker": "Sébastien Haller"},
    "Australia": {"star": "Nestory Irankunda", "breakout": "Nestory Irankunda"},
}

# ---------------------------------------------------------------------------
# Global editorial lists for the article + the "Players to Watch" hub.
# Each entry: name, team, club, pos, age (filled by build where possible), blurb.
# ---------------------------------------------------------------------------
GLOBAL_LISTS = {
    "superstars": [
        {"name": "Kylian Mbappé", "team": "France", "blurb": "The world's best player at his peak, captaining the No.1 side. A World Cup final hat-trick already on his CV — this is his stage to win it as the main man."},
        {"name": "Lamine Yamal", "team": "Spain", "blurb": "Still a teenager, already the most electric dribbler on the planet. If Spain win it, he'll be the face of the tournament and probably its best player."},
        {"name": "Lionel Messi", "team": "Argentina", "blurb": "The defending champion and almost certainly his last dance. Logic says the body fades; history says never write him off."},
        {"name": "Vinícius Júnior", "team": "Brazil", "blurb": "Brazil's talisman and the man who must finally deliver a deep World Cup run for the Seleção under Ancelotti."},
        {"name": "Erling Haaland", "team": "Norway", "blurb": "A goalscoring machine finally on the World Cup stage. The most ruthless No.9 alive, with everything to prove."},
        {"name": "Jude Bellingham", "team": "England", "blurb": "England's heartbeat and a player who saves his biggest moments for the biggest games. Carries a nation's hopes."},
        {"name": "Cristiano Ronaldo", "team": "Portugal", "blurb": "The only man to score at five World Cups, chasing the one trophy that has eluded him in his final attempt."},
        {"name": "Mohamed Salah", "team": "Egypt", "blurb": "Dragged Egypt to the finals almost by himself. A genuine superstar who can light up any group."},
    ],
    "breakoutKids": [
        {"name": "Lamine Yamal", "team": "Spain", "blurb": "Already a superstar, but a World Cup could turn him into the undisputed best player on earth before he's 19."},
        {"name": "Rayan Cherki", "team": "France", "blurb": "A 22-year-old playmaker now at Manchester City with elite vision, ready to step into France's spotlight."},
        {"name": "Nico Paz", "team": "Argentina", "blurb": "A 21-year-old creative force out of Real Madrid, now starring at Como and playing with genuine joy — Totti is a fan."},
        {"name": "Ibrahim Maza", "team": "Algeria", "blurb": "A 20-year-old attacking midfielder already making waves at Bayer Leverkusen."},
        {"name": "Endrick", "team": "Brazil", "blurb": "Brazil's next great No.9, hungry to announce himself on the global stage."},
        {"name": "Arda Guler", "team": "Turkey", "blurb": "Real Madrid's silky left-footer is the jewel of a thrilling young Turkey side."},
        {"name": "Gilberto Mora", "team": "Mexico", "blurb": "A teenage midfielder carrying real hype for the co-hosts — one of the youngest players at the tournament."},
        {"name": "Jamal Musiala", "team": "Germany", "blurb": "A ball-gliding genius who, with Wirtz, makes Germany must-watch again."},
    ],
    "surpriseOfTheTournament": [
        {"name": "Curaçao", "team": "Curaçao", "blurb": "The smallest nation ever to qualify. Just being here is a shock — anything else is a fairy tale."},
        {"name": "Cape Verde", "team": "Cape Verde", "blurb": "The Blue Sharks' first World Cup, with a diaspora-fuelled squad that fears no one."},
        {"name": "Uzbekistan", "team": "Uzbekistan", "blurb": "A historic debut built on one of Asia's most exciting young cores."},
        {"name": "Ecuador", "team": "Ecuador", "blurb": "Young, fearless and miserly at the back — a genuine threat to spoil bigger nations' plans."},
        {"name": "Austria", "team": "Austria", "blurb": "Rangnick's relentless pressing machine could ambush a heavyweight or two."},
    ],
    "onesToWatch": [
        {"name": "Moisés Caicedo", "team": "Ecuador", "blurb": "The world's most expensive midfielder, the engine of a stubborn Ecuador."},
        {"name": "Florian Wirtz", "team": "Germany", "blurb": "Germany's creative fulcrum and one of the best young playmakers in the world."},
        {"name": "Alexander Isak", "team": "Sweden", "blurb": "A silky, lethal striker leading a fearsome Swedish front line."},
        {"name": "Achraf Hakimi", "team": "Morocco", "blurb": "Arguably the best right-back on earth and Morocco's attacking weapon."},
        {"name": "Pedri", "team": "Spain", "blurb": "The metronome of the world's best midfield — control personified."},
        {"name": "Federico Valverde", "team": "Uruguay", "blurb": "An all-action engine who does everything for club and country."},
    ],
    "hiddenGems": [
        {"name": "Valentín Barco", "team": "Argentina", "blurb": "A 21-year-old left-sided talent with Boca pedigree, now in Ligue 1 — the future of Argentina's flank."},
        {"name": "Kerim Alajbegovic", "team": "Bosnia and Herzegovina", "blurb": "An 18-year-old talent already turning heads at Bayer Leverkusen."},
        {"name": "Nestory Irankunda", "team": "Australia", "blurb": "A raw, thrilling winger who could earn a big move with one tournament moment."},
        {"name": "Simon Adingra", "team": "Côte d'Ivoire", "blurb": "A direct, fearless wide man capable of unlocking any defence."},
        {"name": "Relebohile Mofokeng", "team": "South Africa", "blurb": "A gifted young attacker and one of African football's brightest prospects."},
        {"name": "Hugo Sochurek", "team": "Czechia", "blurb": "A genuine wonderkid in a Czech side short on stardust."},
    ],
    "coachesToWatch": [
        {"name": "Carlo Ancelotti", "team": "Brazil", "blurb": "The most decorated coach in club history, now the first foreigner to lead Brazil at a World Cup. Tournament football is his art form."},
        {"name": "Marcelo Bielsa", "team": "Uruguay", "blurb": "El Loco has reinvented Uruguay in his own relentless, high-octane image. Box-office football guaranteed."},
        {"name": "Julian Nagelsmann", "team": "Germany", "blurb": "A young tactical obsessive rebuilding Germany around a generation of creators."},
        {"name": "Ralf Rangnick", "team": "Austria", "blurb": "The godfather of gegenpressing has turned Austria into a suffocating, overachieving unit."},
        {"name": "Didier Deschamps", "team": "France", "blurb": "A serial winner managing his final tournament with France — and the man who knows how to get this squad over the line."},
        {"name": "Jesse Marsch", "team": "Canada", "blurb": "An energetic American coach who has given the co-hosts a fearless, aggressive identity."},
    ],
}
