import re
import os

# 1. Get the pure GSAP footer
footer_path = '/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html'
with open(footer_path, 'r', encoding='utf-8') as f:
    footer_lines = f.readlines()
# Pure GSAP footer is from line 5 to 447 (0-indexed 4 to 447)
pure_gsap_footer = "".join(footer_lines[4:447])

# 2. Extract dock from dystrybucja/index.html to be safe
with open('dystrybucja/index.html', 'r', encoding='utf-8') as f:
    dyst_html = f.read()

dock_match = re.search(r'(<!-- GLOBAL MENU START -->.*?<!-- GLOBAL TRANSLATE END -->\n<script src="/local-navigation.js\?v=20260901-white-dock" defer></script>)', dyst_html, re.DOTALL)
if dock_match:
    dock_snippet = dock_match.group(1)
else:
    print("Dock snippet not found in dystrybucja")
    exit(1)

# 3. Process baza-wiedzy
with open('baza-wiedzy/index.html.bak', 'r', encoding='utf-8') as f:
    baza_html = f.read()

baza_html = baza_html.replace('<!-- GLOBAL MENU START -->', pure_gsap_footer + '\n<!-- GLOBAL MENU START -->')

with open('baza-wiedzy/index.html', 'w', encoding='utf-8') as f:
    f.write(baza_html)
print("baza-wiedzy fixed successfully")

# 4. Process kontakt
with open('/tmp/prescot_kontakt.html', 'r', encoding='utf-8') as f:
    kontakt_html = f.read()

# Replace Webflow footer with GSAP footer + dock
footer_regex = re.compile(r'<div class="footer wf-section">.*?</div>\s*<script type="speculationrules">', re.DOTALL)
replacement = pure_gsap_footer + '\n' + dock_snippet + '\n<script type="speculationrules">'

if footer_regex.search(kontakt_html):
    kontakt_html = footer_regex.sub(replacement, kontakt_html, count=1)
else:
    print("Could not find Webflow footer in kontakt")
    kontakt_html = kontakt_html.replace('</body>', pure_gsap_footer + '\n' + dock_snippet + '\n</body>')

head_css = '<link rel="stylesheet" href="/prescot-global.css?v=20260901-white-dock">\n</head>'
kontakt_html = kontakt_html.replace('</head>', head_css)

with open('kontakt/index.html', 'w', encoding='utf-8') as f:
    f.write(kontakt_html)
print("kontakt fixed successfully")
