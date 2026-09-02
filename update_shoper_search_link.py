# -*- coding: utf-8 -*-
import os
import re

baza_fpath = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/baza-wiedzy/index.html"
with open(baza_fpath, "r", encoding="utf-8") as f:
    html = f.read()

# Update recommendation link and text
html = re.sub(
    r'var searchUrl = [^;]+;',
    "var query = encodeURIComponent('zasilacz ' + matchedPsu + 'W ' + state.voltage + 'V');\n    var searchUrl = 'https://www.prescot.com.pl/pl/searchquery/' + query + '/1/phot/5?url=' + query;",
    html
)

html = re.sub(
    r'href="https://www\.prescot\.com\.pl/\?s=[^"]*"',
    'href="https://www.prescot.com.pl/pl/searchquery/zasilacz+150W+24V/1/phot/5?url=zasilacz+150W+24V"',
    html
)

with open(baza_fpath, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated search link to exact Shoper searchquery format.")
