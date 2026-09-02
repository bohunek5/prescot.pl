# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update prescot-global.css with .prescot-smart-logo styles
css_fpath = os.path.join(base_dir, "prescot-global.css")
with open(css_fpath, "r", encoding="utf-8") as f:
    css_content = f.read()

smart_logo_css = """
/* =========================================================
   PRESCOT SMART TOP LOGO (Hides on Scroll Down, Shows on Scroll Up)
   ========================================================= */
.prescot-smart-logo {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  padding: 24px 20px 16px 20px !important;
  text-align: center !important;
  z-index: 99999 !important;
  pointer-events: none !important;
  transform: translateY(0);
  opacity: 1;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease !important;
}

.prescot-smart-logo a {
  display: inline-block !important;
  pointer-events: auto !important;
}

.prescot-smart-logo img {
  height: 48px !important;
  width: auto !important;
  display: block !important;
  filter: drop-shadow(0 2px 10px rgba(0,0,0,0.6)) !important;
  transition: transform 0.2s ease !important;
}

.prescot-smart-logo img:hover {
  transform: scale(1.03) !important;
}

.prescot-smart-logo.logo-hidden {
  transform: translateY(-120%) !important;
  opacity: 0 !important;
  pointer-events: none !important;
}
"""

if ".prescot-smart-logo" not in css_content:
    css_content += "\n" + smart_logo_css
    with open(css_fpath, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Added .prescot-smart-logo CSS to prescot-global.css")
else:
    # Replace existing block
    css_content = re.sub(r'/\* =========================================================\s*PRESCOT SMART TOP LOGO.*?\*/.*?\.prescot-smart-logo\.logo-hidden\s*\{[^}]*\}', smart_logo_css, css_content, flags=re.DOTALL)
    with open(css_fpath, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated .prescot-smart-logo CSS in prescot-global.css")

# 2. Update local-navigation.js with Smart Scroll handler
js_content = """// Prescot LED — Global Navigation, Active Indicator, Dock & Smart Top Logo Controller
document.addEventListener("DOMContentLoaded", () => {
  // 1. Podświetlanie aktywnej pozycji w menu dock
  const currentPath = `/${window.location.pathname.replace(/^\\/+|\\/+$/g, "")}/`.replace("//", "/");
  document.querySelectorAll(".prescot-dock .dock-item").forEach((item) => {
    const href = item.getAttribute("href");
    if (!href) return;
    const normalizedHref = `/${href.replace(/^\\/+|\\/+$/g, "")}/`.replace("//", "/");
    if (normalizedHref === currentPath) {
      item.classList.add("url-active");
    }
  });

  // 2. Smart Scroll Controller for Top Logo & Bottom Dock
  let lastScrollY = window.scrollY;
  const scrollThreshold = 8;
  const smartLogo = document.querySelector(".prescot-smart-logo");
  const dock = document.querySelector(".prescot-dock");

  window.addEventListener("scroll", () => {
    const currentScrollY = window.scrollY;
    
    // Always show at the very top
    if (currentScrollY < 30) {
      if (smartLogo) smartLogo.classList.remove("logo-hidden");
      if (dock) dock.classList.remove("dock-hidden");
      lastScrollY = currentScrollY;
      return;
    }

    if (Math.abs(currentScrollY - lastScrollY) > scrollThreshold) {
      if (currentScrollY > lastScrollY && currentScrollY > 80) {
        // SCROLLING DOWN -> HIDE LOGO & DOCK
        if (smartLogo) smartLogo.classList.add("logo-hidden");
        if (dock) dock.classList.add("dock-hidden");
      } else if (currentScrollY < lastScrollY) {
        // SCROLLING UP -> SHOW LOGO & DOCK
        if (smartLogo) smartLogo.classList.remove("logo-hidden");
        if (dock) dock.classList.remove("dock-hidden");
      }
      lastScrollY = currentScrollY;
    }
  }, { passive: true });
});
"""

with open(os.path.join(base_dir, "local-navigation.js"), "w", encoding="utf-8") as f:
    f.write(js_content)
print("Updated local-navigation.js with smart scroll controller.")

# 3. Update HTML files: index.html, prescotled, baza-wiedzy, wspolpraca-b2b, dystrybucja, kontakt
WHITE_ORANGE_LOGO = "/wp-content/uploads/2025/12/biale-z-kolorem.svg"
smart_logo_markup = f"""<!-- SMART LOGO: BIAŁE Z POMARAŃCZEM (ZNIKA PRZY SCROLLU W DÓŁ, WRACA W GÓRĘ) -->
<div class="prescot-smart-logo">
  <a href="/" title="Prescot LED Strona Główna">
    <img src="{WHITE_ORANGE_LOGO}" alt="Prescot LED">
  </a>
</div>
"""

pages = [
    "index.html",
    "prescotled/index.html",
    "baza-wiedzy/index.html",
    "wspolpraca-b2b/index.html",
    "dystrybucja/index.html",
    "kontakt/index.html",
    "tasmy-led/index.html",
    "produkty/index.html",
    "produkcja/index.html"
]

for p in pages:
    fpath = os.path.join(base_dir, p)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove old top logo blocks
    content = re.sub(r'<!-- (?:SMART LOGO|LOGO NA GÓRZE).*?-->\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="prescot-top-centered-logo".*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="prescot-subpage-top-logo".*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="prescot-smart-logo".*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div style="text-align:\s*center;\s*padding:\s*32px 20px 24px 20px;".*?</div>\s*', '', content, flags=re.DOTALL)
    
    # Insert smart_logo_markup right after <body>
    content = re.sub(r'(<body[^>]*>)', r'\1\n' + smart_logo_markup, content, count=1)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated smart logo in {p}")

print("All smart logo integrations complete!")

