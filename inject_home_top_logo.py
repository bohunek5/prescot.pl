# -*- coding: utf-8 -*-
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

top_logo_centered = """
<!-- LOGO NA GÓRZE NA ŚRODKU (STRONA GŁÓWNA) -->
<div class="prescot-top-centered-logo" style="position: absolute; top: 28px; left: 0; width: 100%; text-align: center; z-index: 999; pointer-events: auto;">
  <a href="/" title="Prescot LED Strona Główna" style="display: inline-block;">
    <img src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg" alt="Prescot LED Logo" style="height: 52px; width: auto; filter: drop-shadow(0 2px 10px rgba(0,0,0,0.4));">
  </a>
</div>
"""

for fname in ["index.html", "prescotled/index.html"]:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '<div class="prescot-top-centered-logo"' not in content:
        content = content.replace('<div id="content" class="site-content">', top_logo_centered + '\n<div id="content" class="site-content">')
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected top logo in {fname}")
    else:
        print(f"Top logo already in {fname}")

