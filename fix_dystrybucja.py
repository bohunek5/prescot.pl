import re

with open('/tmp/live_dystrybucja.html', 'r', encoding='utf-8') as f:
    dystrybucja_html = f.read()

with open('baza-wiedzy/index.html.bak', 'r', encoding='utf-8') as f:
    baza_html = f.read()

# Extract dock snippet
dock_match = re.search(r'(<!-- GLOBAL MENU START -->.*?<!-- GLOBAL TRANSLATE END -->\n<script src="/local-navigation.js\?v=20260901-white-dock" defer></script>)', baza_html, re.DOTALL)
if dock_match:
    dock_snippet = dock_match.group(1)
else:
    print("Dock snippet not found in baza-wiedzy.bak")
    exit(1)

# Add CSS to head
head_css = '<link rel="stylesheet" href="/prescot-global.css?v=20260901-white-dock">\n</head>'
dystrybucja_html = dystrybucja_html.replace('</head>', head_css)

# Add dock to body
dystrybucja_html = dystrybucja_html.replace('</body>', dock_snippet + '\n</body>')

with open('dystrybucja/index.html', 'w', encoding='utf-8') as f:
    f.write(dystrybucja_html)
    
print("Dystrybucja fixed successfully")
