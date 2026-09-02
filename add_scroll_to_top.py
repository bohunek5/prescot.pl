# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update prescot-global.css
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

stt_css = """
/* =========================================================
   GLOBAL SCROLL TO TOP BUTTON (FLOATING ON RIGHT ABOVE MENU)
   ========================================================= */
.prescot-scroll-to-top {
  position: fixed !important;
  bottom: 96px !important;
  right: 28px !important;
  z-index: 998 !important;
  width: 46px !important;
  height: 46px !important;
  border-radius: 50% !important;
  background: rgba(15, 23, 42, 0.78) !important;
  color: #ffffff !important;
  border: 1px solid rgba(255, 255, 255, 0.22) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.28) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transform: translateY(14px) scale(0.92) !important;
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1) !important;
  outline: none !important;
  padding: 0 !important;
  font-family: inherit !important;
}

.prescot-scroll-to-top.stt-visible {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) scale(1) !important;
}

.prescot-scroll-to-top:hover {
  background: #e55933 !important;
  border-color: #e55933 !important;
  color: #ffffff !important;
  transform: translateY(-3px) scale(1.05) !important;
  box-shadow: 0 12px 28px rgba(229, 89, 51, 0.45) !important;
}

.prescot-scroll-to-top svg {
  width: 22px !important;
  height: 22px !important;
  stroke: currentColor !important;
  stroke-width: 2.5 !important;
  transition: transform 0.2s ease !important;
}

.prescot-scroll-to-top:hover svg {
  transform: translateY(-2px) !important;
}

@media (max-width: 768px) {
  .prescot-scroll-to-top {
    bottom: 86px !important;
    right: 18px !important;
    width: 42px !important;
    height: 42px !important;
  }
}
"""

if "GLOBAL SCROLL TO TOP BUTTON" in css:
    css = re.sub(r'/\* =+ \s*GLOBAL SCROLL TO TOP BUTTON.*?(?=\n/\*|\Z)', stt_css, css, flags=re.DOTALL)
else:
    css += "\n" + stt_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated prescot-global.css with Scroll To Top button styles.")


# 2. Update local-navigation.js
nav_js_path = os.path.join(base_dir, "local-navigation.js")
with open(nav_js_path, "r", encoding="utf-8") as f:
    nav_js = f.read()

# Build the complete clean local-navigation.js
clean_nav_js = """// Prescot LED — Global Navigation, Active Indicator, Dock, Hero Logo & Scroll-To-Top Controller
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

  // 2. Utworzenie przycisku Scroll-To-Top (Do góry) jeśli nie istnieje
  let sttBtn = document.getElementById("prescotScrollToTop");
  if (!sttBtn) {
    sttBtn = document.createElement("button");
    sttBtn.type = "button";
    sttBtn.id = "prescotScrollToTop";
    sttBtn.className = "prescot-scroll-to-top";
    sttBtn.setAttribute("aria-label", "Przewiń na samą górę");
    sttBtn.setAttribute("title", "Do góry");
    sttBtn.innerHTML = `
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="18 15 12 9 6 15"></polyline>
      </svg>
    `;
    document.body.appendChild(sttBtn);

    sttBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // 3. Smart Scroll Controller:
  // - Logo jest widoczne TYLKO w sekcji Hero (ciemne zdjęcia na samej górze).
  // - Po zjechaniu w dół do białej treści logo znika.
  // - Przycisk "Do góry" pojawia się DOPIERO PO opuszczeniu Hero (z prawej strony nad menu).
  // - Dolny dock nawigacji płynnie reaguje na scroll.
  let lastScrollY = window.scrollY;
  const scrollThreshold = 8;
  const smartLogo = document.querySelector(".prescot-smart-logo");
  const dock = document.querySelector(".prescot-dock");

  function updateNavVisibility() {
    const currentScrollY = window.scrollY;
    
    // Oblicz wysokość sekcji Hero
    const heroEl = document.querySelector(".p-full-hero, .hero-section, .hero, .catalog-hero, .elementor-top-section");
    const heroHeight = heroEl ? heroEl.offsetHeight : (window.innerHeight || 700);
    const heroThreshold = Math.max(200, heroHeight * 0.65);

    // LOGO: Widoczne TYLKO w sekcji Hero na samej górze
    if (smartLogo) {
      if (currentScrollY <= heroThreshold) {
        smartLogo.classList.remove("logo-hidden");
      } else {
        smartLogo.classList.add("logo-hidden");
      }
    }

    // SCROLL-TO-TOP BUTTON: Widoczny TYLKO poniżej Hero
    if (sttBtn) {
      if (currentScrollY > heroThreshold) {
        sttBtn.classList.add("stt-visible");
      } else {
        sttBtn.classList.remove("stt-visible");
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

  // 4. B2C Store Redirect Popup Modal Controller
  function initB2CRedirectModal() {
    let dialog = document.getElementById('prescotB2CDialog');
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.id = 'prescotB2CDialog';
      dialog.className = 'prescot-b2c-dialog';
      dialog.innerHTML = `
        <div class="b2c-dialog-box">
          <button type="button" class="b2c-dialog-close" id="b2cCloseCross" aria-label="Zamknij">&times;</button>
          
          <div class="b2c-dialog-icon-wrap">
            <div class="b2c-dialog-icon">
              <svg viewBox="0 0 576 512" width="28" height="28" xmlns="http://www.w3.org/2000/svg">
                <path fill="currentColor" d="M576 216v16c0 13.255-10.745 24-24 24h-8l-26.113 182.788C514.509 462.435 494.257 480 470.37 480H105.63c-23.887 0-44.139-17.565-47.518-41.212L32 256h-8c-13.255 0-24-10.745-24-24v-16c0-13.255 10.745-24 24-24h67.341l106.78-146.821c10.395-14.292 30.407-17.453 44.701-7.058 14.293 10.395 17.453 30.408 7.058 44.701L170.477 192h235.046L326.12 82.821c-10.395-14.292-7.234-34.306 7.059-44.701 14.291-10.395 34.306-7.235 44.701 7.058L484.659 192H552c13.255 0 24 10.745 24 24zM312 392V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm112 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm-224 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24z"/>
              </svg>
            </div>
          </div>

          <div class="b2c-dialog-badge">Sklep Internetowy</div>
          <h3>Oficjalny Sklep Prescot</h3>
          <p class="b2c-main-desc">Zakupy detaliczne, taśmy LED na metry, zasilacze i profile aluminiowe kupisz bezpośrednio w naszym sklepie internetowym.</p>
          
          <div class="b2c-feature-pills">
            <span class="b2c-pill">⚡ Wysyłka 24h</span>
            <span class="b2c-pill">🔒 Zakupy online</span>
            <span class="b2c-pill">📦 Ponad 500+ produktów</span>
          </div>

          <div class="b2c-dialog-actions">
            <a href="https://prescot.com.pl/" id="b2cConfirmBtn" target="_blank" rel="noopener" class="b2c-btn-confirm">
              Przejdź do sklepu prescot.com.pl &rarr;
            </a>
            <button type="button" class="b2c-btn-cancel" id="b2cCancelBtn">
              Zostań na tej stronie
            </button>
          </div>
        </div>
      `;
      document.body.appendChild(dialog);

      const closeDialog = () => {
        if (typeof dialog.close === 'function') {
          dialog.close();
        } else {
          dialog.removeAttribute('open');
        }
      };

      document.getElementById('b2cCloseCross')?.addEventListener('click', closeDialog);
      document.getElementById('b2cCancelBtn')?.addEventListener('click', closeDialog);
      document.getElementById('b2cConfirmBtn')?.addEventListener('click', () => {
        closeDialog();
      });

      dialog.addEventListener('click', (e) => {
        if (e.target === dialog) {
          closeDialog();
        }
      });
    }

    document.querySelectorAll('.prescot-dock a[href*="prescot.com.pl"], .dock-item[data-tooltip*="B2C"], .dock-item[aria-label*="B2C"]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetHref = link.getAttribute('href') || 'https://prescot.com.pl/';
        const confirmBtn = document.getElementById('b2cConfirmBtn');
        if (confirmBtn) {
          confirmBtn.setAttribute('href', targetHref);
        }
        if (typeof dialog.showModal === 'function') {
          dialog.showModal();
        } else {
          dialog.setAttribute('open', '');
        }
      });
    });
  }

  initB2CRedirectModal();
});
"""

with open(nav_js_path, "w", encoding="utf-8") as f:
    f.write(clean_nav_js)

print("Updated local-navigation.js with Scroll-To-Top button and seamless controls.")
