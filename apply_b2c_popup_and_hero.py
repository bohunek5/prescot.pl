# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update dystrybucja/index.html hero background image
dystrybucja_path = os.path.join(base_dir, "dystrybucja/index.html")
with open(dystrybucja_path, "r", encoding="utf-8") as f:
    dystr_content = f.read()

dystr_content = re.sub(
    r"background-image:\s*url\('[^']+'\);",
    "background-image: url('/wp-content/uploads/2026/03/prescot-dystrybucja-hero.webp');",
    dystr_content,
    count=1
)

with open(dystrybucja_path, "w", encoding="utf-8") as f:
    f.write(dystr_content)
print("Updated hero image in dystrybucja/index.html")

# 2. Update prescot-global.css with dialog styles
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

b2c_dialog_css = """
/* =========================================================
   NATIVE B2C REDIRECT POPUP DIALOG (MODERN WEB GUIDANCE)
   ========================================================= */
.prescot-b2c-dialog {
  border: none !important;
  background: transparent !important;
  padding: 0 !important;
  max-width: 480px !important;
  width: 90% !important;
  margin: auto !important;
  border-radius: 24px !important;
  box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.45) !important;
  outline: none !important;
  overflow: visible !important;
}

.prescot-b2c-dialog::backdrop {
  background: rgba(15, 23, 42, 0.78) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
}

.b2c-dialog-box {
  background: #ffffff !important;
  border-radius: 24px !important;
  padding: 38px 32px 30px 32px !important;
  text-align: center !important;
  position: relative !important;
  border: 1px solid #e2e8f0 !important;
  box-sizing: border-box !important;
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.b2c-dialog-icon {
  width: 68px !important;
  height: 68px !important;
  border-radius: 20px !important;
  background: rgba(229, 89, 51, 0.1) !important;
  color: #e55933 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 16px auto !important;
}

.b2c-dialog-badge {
  display: inline-block !important;
  font-size: 11.5px !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  color: #e55933 !important;
  background: rgba(229, 89, 51, 0.08) !important;
  padding: 4px 14px !important;
  border-radius: 999px !important;
  margin-bottom: 12px !important;
}

.b2c-dialog-box h3 {
  font-family: 'Outfit', sans-serif !important;
  font-size: 22px !important;
  font-weight: 800 !important;
  color: #0f172a !important;
  margin-bottom: 12px !important;
  line-height: 1.25 !important;
}

.b2c-dialog-box p {
  font-size: 14.5px !important;
  color: #475569 !important;
  line-height: 1.6 !important;
  margin-bottom: 26px !important;
}

.b2c-dialog-actions {
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}

.b2c-btn-confirm {
  background: #e55933 !important;
  color: #ffffff !important;
  padding: 14px 20px !important;
  border-radius: 12px !important;
  font-weight: 800 !important;
  font-size: 14.5px !important;
  text-decoration: none !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 4px 14px rgba(229, 89, 51, 0.35) !important;
}

.b2c-btn-confirm:hover {
  background: #c94622 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(229, 89, 51, 0.45) !important;
}

.b2c-btn-cancel {
  background: #f1f5f9 !important;
  color: #64748b !important;
  border: none !important;
  padding: 12px 20px !important;
  border-radius: 12px !important;
  font-weight: 700 !important;
  font-size: 13.5px !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.b2c-btn-cancel:hover {
  background: #e2e8f0 !important;
  color: #0f172a !important;
}

.b2c-dialog-close {
  position: absolute !important;
  top: 16px !important;
  right: 18px !important;
  width: 32px !important;
  height: 32px !important;
  border-radius: 50% !important;
  border: none !important;
  background: #f1f5f9 !important;
  color: #64748b !important;
  font-size: 22px !important;
  line-height: 1 !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: all 0.2s !important;
}

.b2c-dialog-close:hover {
  background: #e2e8f0 !important;
  color: #0f172a !important;
}
"""

if "NATIVE B2C REDIRECT POPUP DIALOG" in css:
    css = re.sub(r'/\* =+ \s*NATIVE B2C REDIRECT POPUP DIALOG.*?(?=\n/\*|\Z)', b2c_dialog_css, css, flags=re.DOTALL)
else:
    css += "\n" + b2c_dialog_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated prescot-global.css with B2C redirect popup dialog styles.")

# 3. Update local-navigation.js with popup controller
nav_js_path = os.path.join(base_dir, "local-navigation.js")
with open(nav_js_path, "r", encoding="utf-8") as f:
    nav_js = f.read()

modal_js = """
  // 3. B2C Store Redirect Popup Modal Controller
  function initB2CRedirectModal() {
    let dialog = document.getElementById('prescotB2CDialog');
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.id = 'prescotB2CDialog';
      dialog.className = 'prescot-b2c-dialog';
      dialog.innerHTML = `
        <div class="b2c-dialog-box">
          <button type="button" class="b2c-dialog-close" id="b2cCloseCross" aria-label="Zamknij popup">&times;</button>
          <div class="b2c-dialog-icon">
            <svg viewBox="0 0 576 512" width="30" height="30" xmlns="http://www.w3.org/2000/svg">
              <path fill="currentColor" d="M576 216v16c0 13.255-10.745 24-24 24h-8l-26.113 182.788C514.509 462.435 494.257 480 470.37 480H105.63c-23.887 0-44.139-17.565-47.518-41.212L32 256h-8c-13.255 0-24-10.745-24-24v-16c0-13.255 10.745-24 24-24h67.341l106.78-146.821c10.395-14.292 30.407-17.453 44.701-7.058 14.293 10.395 17.453 30.408 7.058 44.701L170.477 192h235.046L326.12 82.821c-10.395-14.292-7.234-34.306 7.059-44.701 14.291-10.395 34.306-7.235 44.701 7.058L484.659 192H552c13.255 0 24 10.745 24 24zM312 392V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm112 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm-224 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24z"/>
            </svg>
          </div>
          <div class="b2c-dialog-badge">Przejście do Sklepu</div>
          <h3>Przechodzisz do oficjalnego sklepu Prescot (B2C)</h3>
          <p>Za chwilę zostaniesz przekierowany do naszego sklepu internetowego <strong>prescot.com.pl</strong> dla klientów detalicznych i instalatorów, gdzie możesz złożyć zamówienie online.</p>
          <div class="b2c-dialog-actions">
            <a href="https://prescot.com.pl/" id="b2cConfirmBtn" target="_blank" rel="noopener" class="b2c-btn-confirm">
              Przejdź do sklepu B2C &rarr;
            </a>
            <button type="button" class="b2c-btn-cancel" id="b2cCancelBtn">
              Zostań na tej stronie
            </button>
          </div>
        </div>
      `;
      document.body.appendChild(dialog);

      // Close handlers
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

      // Backdrop click
      dialog.addEventListener('click', (e) => {
        if (e.target === dialog) {
          closeDialog();
        }
      });
    }

    // Intercept clicks on B2C dock item and prescot.com.pl links (except the confirm button itself)
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
"""

if "initB2CRedirectModal" not in nav_js:
    # Insert before the closing brackets of DOMContentLoaded
    nav_js = nav_js.rstrip()
    if nav_js.endswith("});"):
        nav_js = nav_js[:-3] + modal_js + "\n});\n"
    else:
        nav_js += "\n" + modal_js
    with open(nav_js_path, "w", encoding="utf-8") as f:
        f.write(nav_js)
    print("Injected B2C redirect popup modal controller into local-navigation.js")
else:
    print("Modal controller already present in local-navigation.js")

