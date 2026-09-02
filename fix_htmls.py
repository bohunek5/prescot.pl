import re
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
template_path = os.path.join(base_dir, "index.html")

# Read the template
with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

# Extract top shell
# The top shell should be everything up to `<div id="content"` 
# or `<div data-elementor-type="wp-page"`
content_split = template_html.split('<div id="content" class="site-content">')
top_shell = content_split[0] + '<div id="content" class="site-content">\n\t\t<div class="ast-container">\n'

# Extract bottom shell
# In index.html, the wp-page div ends just before </div><!-- #content -->
# Let's find the footer
footer_split = template_html.split('<footer data-elementor-type="footer"')
bottom_shell = '\t\t</div><!-- .ast-container -->\n\t</div><!-- #content -->\n\t<footer data-elementor-type="footer"' + footer_split[1]

pages_to_fix = [
    "kontakt/index.html",
    "dystrybucja/index.html",
    "baza-wiedzy/index.html"
]

for page in pages_to_fix:
    path = os.path.join(base_dir, page)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We need to extract the actual content of the page.
    # In kontakt/index.html, it's inside <main id="main"> or <div class="page-glow">
    # Actually, for kontakt, it's everything between <body ...> and <nav class="prescot-dock"> (or the footer).
    # Wait, dystrybucja has <div data-elementor-type="wp-page"...> inside it, but the inner content might be wiped?
    print(f"Inspecting {page}")
