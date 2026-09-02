import re

with open("/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/pusta/index.html", "r", encoding="utf-8") as f:
    pusta_html = f.read()

# Let's find content start
content_start = pusta_html.find('<div id="content" class="site-content">')
ast_container_start = pusta_html.find('<div class="ast-container">', content_start)

# Let's find footer start
footer_start = pusta_html.find('<footer data-elementor-type="footer"')

print(f"Content start: {content_start}")
print(f"Ast container start: {ast_container_start}")
print(f"Footer start: {footer_start}")

