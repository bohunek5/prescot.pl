# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update prescot-global.css with Global Button Architecture
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

button_global_css = """
/* =========================================================
   PRESCOT GLOBAL BUTTON ARCHITECTURE (EXACT ODKRYJ & WYŚLIJ)
   ========================================================= */

/* Base Pill Button */
.p-btn,
.elementor-button,
.submitBtn,
.b2b-btn,
.distBtn {
  font-family: var(--prescot-font-body, 'Manrope', sans-serif) !important;
  font-weight: 600 !important;
  font-size: 14px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  border-radius: 999px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  cursor: pointer !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  text-decoration: none !important;
  box-sizing: border-box !important;
}

/* 1. BUTTONS ON HERO / DARK SECTIONS ("Odkryj" style) */
.p-btn-primary,
.p-btn-hero-primary,
.catalog-button,
.hero-btn-primary {
  background: #e55933 !important;
  color: #ffffff !important;
  border: 1px solid #e55933 !important;
  padding: 15px 34px !important;
  box-shadow: 0 4px 14px rgba(229, 89, 51, 0.35) !important;
}

.p-btn-primary:hover,
.p-btn-hero-primary:hover,
.catalog-button:hover,
.hero-btn-primary:hover {
  transform: translateY(-2px) !important;
  background: #ffffff !important;
  color: #e55933 !important;
  border-color: #ffffff !important;
  box-shadow: 0 8px 24px rgba(229, 89, 51, 0.45) !important;
}

.p-btn-outline,
.p-btn-hero-outline,
.hero-btn-outline {
  background: rgba(255, 255, 255, 0.12) !important;
  color: #ffffff !important;
  border: 1px solid rgba(255, 255, 255, 0.4) !important;
  padding: 15px 34px !important;
  backdrop-filter: blur(8px) !important;
}

.p-btn-outline:hover,
.p-btn-hero-outline:hover,
.hero-btn-outline:hover {
  transform: translateY(-2px) !important;
  background: #ffffff !important;
  color: #212a35 !important;
  border-color: #ffffff !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
}

/* 2. BUTTONS ON WHITE / LIGHT SECTIONS ("Wyślij" / B2B style) */
.p-btn-dark,
.p-btn-white-surface,
.submitBtn,
.b2b-submit-btn,
.contact-submit-btn {
  background: #212a35 !important;
  color: #ffffff !important;
  border: 1px solid #212a35 !important;
  padding: 16px 32px !important;
  box-shadow: 0 2px 8px rgba(33, 42, 53, 0.1) !important;
}

.p-btn-dark:hover,
.p-btn-white-surface:hover,
.submitBtn:hover,
.b2b-submit-btn:hover,
.contact-submit-btn:hover {
  transform: translateY(-2px) !important;
  background: #ffffff !important;
  color: #212a35 !important;
  border-color: #212a35 !important;
  box-shadow: 0 6px 20px rgba(33, 42, 53, 0.18) !important;
}

.p-btn-orange-on-white,
.b2b-action-btn-orange {
  background: #e55933 !important;
  color: #ffffff !important;
  border: 1px solid #e55933 !important;
  padding: 16px 32px !important;
  box-shadow: 0 4px 14px rgba(229, 89, 51, 0.25) !important;
}

.p-btn-orange-on-white:hover,
.b2b-action-btn-orange:hover {
  transform: translateY(-2px) !important;
  background: #ffffff !important;
  color: #e55933 !important;
  border-color: #e55933 !important;
  box-shadow: 0 6px 20px rgba(229, 89, 51, 0.35) !important;
}
"""

if "PRESCOT GLOBAL BUTTON ARCHITECTURE" not in css_content:
    css_content += "\n" + button_global_css
else:
    css_content = re.sub(r'/\* ===+\s*PRESCOT GLOBAL BUTTON ARCHITECTURE.*', button_global_css, css_content, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print("Updated prescot-global.css with Global Button Architecture.")

# 2. Update local-navigation.js with Hero-Only Logo Logic
js_path = os.path.join(base_dir, "local-navigation.js")
js_content = """// Prescot LED — Global Navigation, Active Indicator, Dock & Hero-Locked Logo Controller
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

  // 2. Smart Scroll Controller:
  // - Logo jest widoczne TYLKO w sekcji Hero (ciemne zdjęcia na samej górze).
  // - Po zjechaniu w dół do białej treści logo natychmiast znika.
  // - Logo WRACA DOPIERO gdy użytkownik przewinie stronę z powrotem na samą górę do sekcji Hero!
  // - Dolny dock nawigacji płynnie reaguje na kierunek scrolla (chowa się przy scrollu w dół, wysuwa przy scrollu w górę).
  let lastScrollY = window.scrollY;
  const scrollThreshold = 8;
  const smartLogo = document.querySelector(".prescot-smart-logo");
  const dock = document.querySelector(".prescot-dock");

  function updateNavVisibility() {
    const currentScrollY = window.scrollY;
    
    // Oblicz wysokość sekcji Hero (domyślnie wysokość okna lub sekcji p-full-hero)
    const heroEl = document.querySelector(".p-full-hero, .hero-section, .hero, .catalog-hero, .elementor-top-section");
    const heroHeight = heroEl ? heroEl.offsetHeight : (window.innerHeight || 700);
    // Próg Hero: logo znika zanim opuścimy ciemne tło (60% wysokości hero)
    const heroThreshold = Math.max(200, heroHeight * 0.65);

    // LOGO: Widoczne TYLKO w sekcji Hero na samej górze
    if (smartLogo) {
      if (currentScrollY <= heroThreshold) {
        smartLogo.classList.remove("logo-hidden");
      } else {
        smartLogo.classList.add("logo-hidden");
      }
    }

    // DOCK: Smart reveal / hide
    if (dock) {
      if (currentScrollY < 30) {
        dock.classList.remove("dock-hidden");
      } else if (Math.abs(currentScrollY - lastScrollY) > scrollThreshold) {
        if (currentScrollY > lastScrollY && currentScrollY > 80) {
          dock.classList.add("dock-hidden");
        } else if (currentScrollY < lastScrollY) {
          dock.classList.remove("dock-hidden");
        }
      }
    }
    lastScrollY = currentScrollY;
  }

  window.addEventListener("scroll", updateNavVisibility, { passive: true });
  updateNavVisibility();
});
"""

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated local-navigation.js with Hero-Locked Logo Controller.")
