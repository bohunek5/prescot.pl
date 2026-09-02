# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update prescot-global.css with absolute suppression of old scroll buttons
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

hide_old_arrows_css = """
/* =========================================================
   ABSOLUTE SUPPRESSION OF OLD SCROLL-TOP & FOOTER ARROWS
   ========================================================= */
#ast-scroll-top,
.ast-scroll-top,
.ast-scroll-to-top-right,
.ast-scroll-to-top-left,
.stopkaArrowUp,
a.stopkaArrowUp,
.footerSlide .stopkaArrowUp,
.scroll-to-top,
.back-to-top,
a[href="#page"][id*="scroll"],
a[href="#masthead"],
.elementor-element-89ac1c6,
.elementor-element-2635332e,
.elementor-element-44cdc488 {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
}
"""

if "ABSOLUTE SUPPRESSION OF OLD SCROLL-TOP" in css:
    css = re.sub(r'/\* =+ \s*ABSOLUTE SUPPRESSION OF OLD SCROLL-TOP.*?(?=\n/\*|\Z)', hide_old_arrows_css, css, flags=re.DOTALL)
else:
    css += "\n" + hide_old_arrows_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated prescot-global.css with permanent suppression of old scroll-top and footer arrows.")


# 2. Clean scratch/footer.html
footer_scratch_path = "/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html"
if os.path.exists(footer_scratch_path):
    with open(footer_scratch_path, "r", encoding="utf-8") as f:
        f_content = f.read()
    f_content = re.sub(r'<a href="[^"]*" class="stopkaArrowUp".*?</a>', '', f_content, flags=re.DOTALL)
    f_content = re.sub(r'<div class="stopkaArrowUp".*?</div>', '', f_content, flags=re.DOTALL)
    with open(footer_scratch_path, "w", encoding="utf-8") as f:
        f.write(f_content)
    print("Cleaned stopkaArrowUp from scratch/footer.html")


# 3. Clean stopkaArrowUp and ast-scroll-top from all HTML files in public directory
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()
            orig = content
            # Remove stopkaArrowUp
            content = re.sub(r'<a href="[^"]*" class="stopkaArrowUp".*?</a>', '', content, flags=re.DOTALL)
            content = re.sub(r'<div class="stopkaArrowUp".*?</div>', '', content, flags=re.DOTALL)
            # Remove ast-scroll-top divs
            content = re.sub(r'<div id="ast-scroll-top".*?</div>\s*</div>', '', content, flags=re.DOTALL)
            content = re.sub(r'<a id="ast-scroll-top".*?</a>', '', content, flags=re.DOTALL)
            if content != orig:
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Removed old scroll arrows from {fpath}")

print("All old theme scroll buttons and footer top arrows removed globally.")
