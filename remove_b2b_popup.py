# -*- coding: utf-8 -*-
import os
import glob

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update local-navigation.js to remove popup interceptor
clean_js = """// Prescot LED — Global Navigation, Active Indicator & Dock Scroll Controller
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

  // 2. Smart Hide on Scroll
  let lastScrollY = window.scrollY;
  const scrollThreshold = 10;
  const dock = document.querySelector(".prescot-dock");

  if (dock) {
    window.addEventListener("scroll", () => {
      const currentScrollY = window.scrollY;
      if (Math.abs(currentScrollY - lastScrollY) > scrollThreshold) {
        if (currentScrollY > lastScrollY && currentScrollY > 120) {
          dock.classList.add("dock-hidden");
        } else {
          dock.classList.remove("dock-hidden");
        }
        lastScrollY = currentScrollY;
      }
    }, { passive: true });
  }
});
"""

with open(os.path.join(base_dir, "local-navigation.js"), "w", encoding="utf-8") as f:
    f.write(clean_js)
print("local-navigation.js updated: popup removed.")

# 2. Update dock in all HTML files
html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)
count = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    old_needle = '<a href="https://prescot.abstore.pl/client/loginorcreate/login" class="dock-item b2b-trigger" data-tooltip="Strefa B2B" aria-label="B2B">'
    new_needle = '<a href="/wspolpraca-b2b/" class="dock-item" data-tooltip="Strefa B2B" aria-label="B2B">'
    
    if old_needle in content:
        content = content.replace(old_needle, new_needle)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Updated dock link in {count} HTML files to navigate directly to /wspolpraca-b2b/.")

