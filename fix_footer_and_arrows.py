# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update prescot-global.css
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix body and html background and padding bottom
fix_css = """
/* =========================================================
   SEAMLESS WHITE FOOTER & BASE BACKGROUND FIX
   ========================================================= */
html, body {
  background-color: #ffffff !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}

#stopka, footer, .elementor-location-footer {
  background-color: #ffffff !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}

/* Ukrycie starych granatowych / zdublowanych strzałek z Elementora */
.elementor-widget-icon a.elementor-icon[href^="#"],
.premium-floating-effects-yes[data-widget_type="icon.default"],
[data-id="89ac1c6"],
[data-id="2635332e"],
[data-id="44cdc488"] {
  display: none !important;
}

/* =========================================================
   GLOBALNA STRZAŁKA W DÓŁ (BOUNCING ARROW) - CZYSTY BIAŁY GLASS NAD MENU
   ========================================================= */
.p-hero-arrow-down {
  position: absolute !important;
  bottom: 96px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  z-index: 99 !important;
  color: #ffffff !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  gap: 6px !important;
  text-decoration: none !important;
  cursor: pointer !important;
  opacity: 0.95 !important;
  transition: all 0.25s ease !important;
  font-size: 11.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.6px !important;
  text-transform: uppercase !important;
}
.p-hero-arrow-down span {
  color: #ffffff !important;
  text-shadow: 0 2px 10px rgba(0,0,0,0.6) !important;
}
.p-hero-arrow-down:hover {
  opacity: 1 !important;
  color: #ff8a65 !important;
  transform: translateX(-50%) translateY(2px) !important;
}
.p-hero-arrow-down:hover span {
  color: #ff8a65 !important;
}
.p-arrow-icon {
  width: 38px !important;
  height: 38px !important;
  border-radius: 50% !important;
  background: rgba(255, 255, 255, 0.2) !important;
  border: 1px solid rgba(255, 255, 255, 0.5) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
  animation: pBounce 2.2s infinite ease-in-out !important;
  color: #ffffff !important;
}
.p-arrow-icon svg {
  stroke: #ffffff !important;
  color: #ffffff !important;
}
@keyframes pBounce {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(-8px); }
  60% { transform: translateY(-4px); }
}

@media (max-width: 767px) {
  .p-hero-arrow-down {
    bottom: 84px !important;
  }
}
"""

# Replace or append the clean rules
if "SEAMLESS WHITE FOOTER" in css:
    css = re.sub(r'/\* =+ \s*SEAMLESS WHITE FOOTER.*?(?=\n/\*|\Z)', fix_css, css, flags=re.DOTALL)
else:
    css += "\n" + fix_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated prescot-global.css with seamless white footer and hidden old navy arrows.")

# 2. Update all HTML files so body doesn't have inline padding-bottom: 90px
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()
            orig = content
            content = content.replace("padding-bottom: 90px;", "padding-bottom: 0px;")
            content = content.replace("background: var(--p-bg);", "background: #ffffff;")
            if content != orig:
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Updated body styling in {fpath}")

print("All pages synchronized with pure white background ending seamlessly at the bottom.")
