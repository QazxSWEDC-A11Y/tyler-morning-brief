#!/usr/bin/env python3
import datetime, glob, json, sys
t = datetime.date.today()
jp = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日'][t.weekday()]
date_japanese = str(t.year) + '年' + str(t.month).zfill(2) + '月' + str(t.day).zfill(2) + '日'
reports_dir = sys.argv[1] if len(sys.argv) > 1 else '/workspace/brief/reports'
n = len(glob.glob(reports_dir + '/*.html'))
vol = 'Vol.' + str(n + 1).zfill(3)
print(json.dumps({
    'TODAY': t.strftime('%Y-%m-%d'),
    'DATE_COMPACT': t.strftime('%Y%m%d'),
    'DATE_DISPLAY': t.strftime('%Y.%m.%d'),
    'DATE_JAPANESE': date_japanese,
    'DAY_JP': jp,
    'VOL': vol
}))