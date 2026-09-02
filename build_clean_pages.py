import re
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# Read reference shell from tasmy-led/index.html
with open(os.path.join(base_dir, "tasmy-led/index.html"), "r", encoding="utf-8") as f:
    tasmy_html = f.read()

# ----------------------------------------------------
# 1. FIX DYSTRYBUCJA
# ----------------------------------------------------
print("--- Fixing Dystrybucja ---")
with open(os.path.join(base_dir, "dystrybucja/index.html"), "r", encoding="utf-8") as f:
    dyst_html = f.read()

# Replace all https://tasmaled.com.pl/ with /
dyst_html = dyst_html.replace("https://tasmaled.com.pl/wp-content/", "/wp-content/")
dyst_html = dyst_html.replace("https://tasmaled.com.pl/wp-includes/", "/wp-includes/")
dyst_html = dyst_html.replace("https://tasmaled.com.pl/wp-json/", "/wp-json/")

# Ensure prescot-global.css is loaded in head
if "prescot-global.css" not in dyst_html:
    dyst_html = dyst_html.replace("</head>", '<link rel="stylesheet" href="/prescot-global.css?v=20260901-white-dock">\n</head>')

# Ensure dock is before </body>
with open(os.path.join(base_dir, "dystrybucja/index.html"), "w", encoding="utf-8") as f:
    f.write(dyst_html)
print("Dystrybucja fixed.")

