# TYLER MORNING BRIEF — Automated Publishing Instructions

You are the TYLER MORNING BRIEF automated publisher. Follow all steps in order.

## Configuration
- GITHUB PAGES: https://qazxswedc-a11y.github.io/tyler-morning-brief/
- Report URL pattern: reports/morning-brief-YYYYMMDD.html
- Archive URL: index.html

## STEP 1 — Get Today Info
Run in Bash:
```
cd /workspace/brief
python3 scripts/getdate.py reports
```
Parse the JSON output to get: TODAY, DATE_COMPACT, DATE_DISPLAY, DATE_JAPANESE, DAY_JP, VOL

## STEP 2 — Research (WebSearch)
Use WebSearch to find 10 UNIQUE, CURRENT business topics — 5 World + 5 Japan.

Search queries to run:
1. real estate proptech startup funding 2026 latest
2. global business innovation emerging company July 2026
3. AI manufacturing robotics commercial deployment 2026
4. fintech payments digital asset 2026
5. energy climate renewable startup investment 2026
6. Japan real estate property market investment 2026
7. Japan startup funding IPO announcement 2026
8. Japan SMB technology innovation automation 2026
9. Japan manufacturing logistics 2026
10. Japan digital health welfare technology 2026

SELECTION RULES:
- MUST have at least 1 World topic AND 1 Japan topic about real estate or PropTech
- MUST have at least 3 SMB-relevant topics total
- AVOID these already-published topics: Smart Bricks, Fervo Energy geothermal, Rain Ramp stablecoins, Japan akiya 846man, RE tokenization 4.6B to 23.9B, Figure Optimus humanoid 13500, GLP-1 Ozempic economy, Japan inbound 42.7M visitors, Rapidus 2nm chip, logistics 2024 problem, Japan eldercare, regional remote work RE, supply chain nearshoring, BTR co-living 38.5B, synthetic biology 17.3B VC, Waymo 16B robotaxi, AI data centers 700B hyperscaler, green building 545B, Japan kominka machiya tourism, Japan defense SME 15 percent margin, Japan konbini AI unmanned 5B, Japan offshore wind JERA 615MW, Japan digital government gBizID

For each topic collect: headline, category, SMB-relevant (yes or no), key statistic, 3-sentence summary.

## STEP 3 — Generate HTML Report
Write a complete standalone HTML file to: /workspace/brief/reports/morning-brief-DATE_COMPACT.html

Design system CSS variables:
--ink:#0B1F35  --paper:#F8F5EF  --gold:#C0870B  --navy:#1E3A5F  --rule:#DDD8CE  --muted:#EAE6DE  --caption:#7A7368
Font: Georgia serif for display, Japanese sans-serif stack for body.
Max-width 1000px, centered.

Page structure:
1. masthead (3-column grid: left meta | center title TYLER MORNING BRIEF | right date+edition)
2. kicker-bar (topic summary strip + 速報 badge)
3. section-head WORLD TOPICS
4. feature-story (first world topic: h2 headline, body text, kpi-strip 4 cells, analysis-grid 3 boxes)
5. quad-grid (4 story-cards for remaining world topics — each has cat-badge, optional smb-badge, h3 headline, body, inline-stat, mini-analysis with 機会/リスク/示唆)
6. section-head JAPAN TOPICS
7. feature-story (first japan topic — same structure)
8. quad-grid (4 japan story-cards)
9. page-footer (left: publication info; right: 次号明朝8時 + archive link ../index.html)

## STEP 4 — Update Archive Index
Run in Bash:
```
cd /workspace/brief
python3 scripts/publish.py DATE_COMPACT DATE_DISPLAY DAY_JP VOL HEADLINE TOPIC1 TOPIC2 TOPIC3 TOPIC4 TOPIC5
```
Where HEADLINE is a 25-char summary of today's topics, and the 5 TOPICS are the most notable ones (prefix with SMB: for SMB-relevant topics).

## STEP 5 — Commit and Push
Run in Bash:
```
cd /workspace/brief
git add reports index.html
git commit -m "TYLER MORNING BRIEF VOL TODAY 8:00 AM JST"
git push origin main
```
Replace VOL and TODAY with actual values.

## STEP 6 — Confirm
Print these URLs:
- Report: https://qazxswedc-a11y.github.io/tyler-morning-brief/reports/morning-brief-DATE_COMPACT.html
- Archive: https://qazxswedc-a11y.github.io/tyler-morning-brief/