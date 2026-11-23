[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/akbare12/news-22-b7-headlines-poster/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/akbare12/news-22-b7-headlines-poster/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# THE WORLD TODAY — Sunday 22 November 2026

A headline-poster front page summing up the world's news of Sunday
22 November 2026. Three giant headlines lead the page, then a pinned
world map and a dense numbered list of 32 stories — every item first
reported on 22 November 2026, each with a named source and a
verification badge (REPORTED / CLAIM / ONGOING). The big-number strip
reads 258 House seats · 2 tankers hit · 194 COP31 parties · 330 vote
margin · 36 missing in Banten · 1,661 Gaza toll.

## The three headlines

1. **2 TANKERS HIT** — Two supertankers hit mines east of the Strait of
   Hormuz, north of Ghanam Island; both on fire. First reported 17:13
   UTC. (Iran navy · AP)
2. **NO DEAL** — COP31 in Antalya collapses with no agreement; the EU
   and about 130 parties reject a text with no fossil-fuel language.
   Longest COP ever, first collapse since 2009. (CNN · Reuters)
3. **258** — Democrats win the House with at least 258 seats, the
   largest majority since 1992; Hubbard beats Foxx by 330 votes in a
   North Carolina recount. GOP 173, 4 races uncalled. (AP · Reuters)

## The day in brief (stories 04–32)

| # | Story | Source |
|---|-------|--------|
| 04 | Dymer drone hits flats — Russian strike kills 11, 14 missing north of Kyiv | BBC |
| 05 | Merkury hit at Benghazi — Ukrainian sea drones sink Russian corvette [CLAIM] | BBC |
| 06 | Khartoum drones kill 4 — strikes blamed on RSF, UN building damaged [CLAIM] | AP |
| 07 | Zelenskyy pleads for Patriots — Russia fired ~2,700 drones in a week | Reuters |
| 08 | Iran shows missile city — dual-missile launcher in underground base | Al Jazeera |
| 09 | Saudis stop Houthi attack — drone and missile intercepted [CLAIM: Rabigh] | Reuters |
| 10 | Bahrain blames Iran — industrial site struck, 2 hurt; UAE condemns | France 24 |
| 11 | Europe protests, day 3 — cost and housing marches; 144 arrested in France | Le Monde |
| 12 | Settlers burn West Bank cars — 12 vehicles torched near Ramallah | WAFA |
| 13 | Benghazi depot blast — ammo depot explosion inside naval base | Local auth. |
| 14 | Unity talks stall — Eisenkot and Likud meet; wide gap on unity government | Al Jazeera |
| 15 | Finland: war spills over — drone hits Russian cargo ship in the Baltic | Finnish govt |
| 16 | Gaza aid van strike — World Central Kitchen: three killed were not its team | WCK |
| 17 | "Iran war was avoidable" — ex-UN envoy de Soto | MED Dialogues |
| 18 | Banten factory fire — candy-plant blaze kills 3; 36 missing in Serang | BBC |
| 19 | Turkey warns on Syria — Fidan: Israel may use Druze to provoke Syria op [CLAIM] | Anadolu |
| 20 | Pezeshkian: silent war — "silent economic war"; US blockade hits 130 days | IRNA |
| 21 | War fallout hits markets — Fidan: war burden threatens global markets | Anadolu |
| 22 | Aoun: Israel must leave — Lebanon's president demands full withdrawal | Al Jazeera |
| 23 | Gaza: 350,000 homeless — displaced protest near Yellow Line amid strikes | Al Jazeera |
| 24 | Settlers attack homes — homes attacked in Hebron, Ramallah; tear gas fired | WAFA |
| 25 | Gaza homes blocked — Turkey: Israel blocking container homes [CLAIM] | Anadolu |
| 26 | Germany urged to arrest — Hind Rajab Foundation files complaint vs soldier | HRF |
| 27 | Fred Nile dies at 92 — NSW figurehead dies; announced 22 Nov | Guardian |
| 28 | Gamer rescues girl — teen, 16, and his mother help FBI free missing girl | FBI |
| 29 | Gaza toll 1,661 — death toll since Oct 2025 reaches 1,661 | Gaza health min. |
| 30 | Trump: strikes if no deal — Trump may renew Iran strikes in 2027 | Times of Israel |
| 31 | Mongolia snap vote — Mongolia faces snap presidential vote | Euronews |
| 32 | Cartel boss captured — Mexico cartel boss held; 11 killed in the operation | Al Jazeera |

## Date check

Every story above was first reported on 22 November 2026. Deliberately
excluded, with their real dates: El Chapo Isidro captured 20 Nov ·
BepiColombo Mercury orbit 21 Nov · ICJ Myanmar ruling 19 Nov · Wall St
rout 20 Nov · FBI NCIC hack first reported 21 Nov.

## How it is built

`draw.py` draws `entry.png` (1024×1024, Pillow + DejaVu fonts, no
network). `main.py` (Python standard library only) copies `entry.png`
to `/output/entry.png` and verifies size, PNG magic and sha256, so both
grader runs write identical bytes. Reproduce the image with
`python3 draw.py`, then check the copy program with
`MAKEFUN_OUTPUT_DIR=out python3 main.py` twice and compare sha256 sums.

## Sources

AP · Reuters · BBC · CNN · France 24 · Al Jazeera · Guardian · SCMP ·
IRNA · Anadolu · WAFA · HRF · WCK · FBI · Euronews · dailysummaryof,
22 Nov 2026 edition. Cross-checked against two or more outlets for
the three headline stories.

## License

MIT — see LICENSE.
