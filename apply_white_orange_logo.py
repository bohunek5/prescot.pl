# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

WHITE_ORANGE_LOGO = "/wp-content/uploads/2025/12/biale-z-kolorem.svg"

# 1. Update Homepage (index.html & prescotled/index.html)
home_logo_html = f'''
<!-- LOGO NA GÓRZE NA ŚRODKU: BIAŁE Z POMARAŃCZEM -->
<div class="prescot-top-centered-logo" style="position: absolute; top: 32px; left: 0; width: 100%; text-align: center; z-index: 999; pointer-events: auto;">
  <a href="/" title="Prescot LED Strona Główna" style="display: inline-block;">
    <img src="{WHITE_ORANGE_LOGO}" alt="Prescot LED" style="height: 52px; width: auto; filter: drop-shadow(0 2px 12px rgba(0,0,0,0.6));">
  </a>
</div>
'''

for fname in ["index.html", "prescotled/index.html"]:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace any old top-centered-logo
    content = re.sub(r'<!-- LOGO NA GÓRZE NA ŚRODKU.*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="prescot-top-centered-logo".*?</div>\s*', '', content, flags=re.DOTALL)
    
    content = content.replace('<div id="content" class="site-content">', home_logo_html + '\n<div id="content" class="site-content">')
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fname} with white-orange logo.")

# 2. Update Subpages: Baza Wiedzy, B2B, Dystrybucja, Kontakt
# Place the white-orange logo inside or directly atop the photo hero, no artificial top bars!

for fname in ["baza-wiedzy/index.html", "wspolpraca-b2b/index.html", "dystrybucja/index.html", "kontakt/index.html"]:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace any old top logo or topbar
    content = re.sub(r'<header class="prescot-topbar">.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="prescot-subpage-top-logo".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- LOGO NA GÓRZE.*?-->', '', content, flags=re.DOTALL)
    
    # Update logo in hero header to be biale-z-kolorem.svg
    # Put clean centered white-orange logo at top of hero or page
    subpage_top = f'''
  <div style="text-align: center; padding: 32px 20px 24px 20px;">
    <a href="/" title="Prescot LED Strona Główna" style="display: inline-block;">
      <img src="{WHITE_ORANGE_LOGO}" alt="Prescot LED" style="height: 48px; width: auto; filter: drop-shadow(0 2px 10px rgba(0,0,0,0.5));">
    </a>
  </div>
'''
    # Put it right after <body>
    content = re.sub(r'<body([^>]*)>', r'<body\1>\n' + subpage_top, content, count=1)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fname} with white-orange logo.")

print("All pages successfully updated with biale-z-kolorem.svg!")

