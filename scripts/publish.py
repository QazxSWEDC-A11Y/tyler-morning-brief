#!/usr/bin/env python3
"""TYLER MORNING BRIEF — index.html updater.
Usage: python3 publish.py DATE_COMPACT DATE_DISPLAY DAY_JP VOL HEADLINE TOPIC1 TOPIC2 TOPIC3 TOPIC4 TOPIC5
"""
import sys, re

DATE_COMPACT = sys.argv[1]   # e.g. 20260704
DATE_DISPLAY = sys.argv[2]   # e.g. 2026.07.04
DAY_JP       = sys.argv[3]   # e.g. 土曜日
VOL          = sys.argv[4]   # e.g. Vol.005
HEADLINE     = sys.argv[5]   # e.g. 不動産DX・AI物流・カーボンクレジット ほか
TOPICS       = sys.argv[6:]  # list of topic strings, prefix with SMB: for smb class

with open('/workspace/brief/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Change current "最新" badge to "前号"
html = html.replace(
    '<span class="badge-latest">最新</span>',
    '<span class="badge-latest" style="background:var(--navy);">前号</span>'
)

# 2. Build topic list items
li_items = []
for t in TOPICS:
    if t.startswith('SMB:'):
        li_items.append(f'        <li class="smb">{t[4:]}</li>')
    else:
        li_items.append(f'        <li>{t}</li>')
topics_html = '\n'.join(li_items)

# 3. Build new card
new_card = f"""
  <!-- {VOL} -->
  <a class="report-card" href="reports/morning-brief-{DATE_COMPACT}.html" target="_blank" rel="noopener">
    <span class="badge-latest">最新</span>
    <div class="card-header">
      <div class="card-vol">{VOL}</div>
      <div class="card-date">{DATE_DISPLAY}</div>
      <div class="card-day">{DAY_JP}</div>
    </div>
    <div class="card-body">
      <div class="card-format">世界5本 ＋ 日本5本</div>
      <div class="card-headline">{HEADLINE}</div>
      <ul class="card-topics">
{topics_html}
      </ul>
    </div>
    <div class="card-footer">
      <span class="card-cta">→ 読む</span>
      <span class="card-count">10トピックス</span>
    </div>
  </a>

"""

# 4. Insert before the last </div>\n\n<!-- FOOTER -->
insert_marker = '\n</div>\n\n<!-- FOOTER -->'
if insert_marker in html:
    html = html.replace(insert_marker, new_card + insert_marker)
else:
    # fallback: insert before last </div>
    last_div = html.rfind('\n</div>')
    html = html[:last_div] + new_card + html[last_div:]

# 5. Update footer date
import datetime
t = datetime.date.today()
new_date = f'{t.year}年{str(t.month).zfill(2)}月{str(t.day).zfill(2)}日'
html = re.sub(r'最終更新：\d{4}年\d{2}月\d{2}日', f'最終更新：{new_date}', html)

with open('/workspace/brief/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"index.html updated with {VOL} card")