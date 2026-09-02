# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update Asseco ABStore B2B Login Form in dystrybucja/index.html and wspolpraca-b2b/index.html
asseco_box_html = """    <!-- PANEL LOGOWANIA B2B ASSECO / ABSTORE -->
    <div class="b2b-login-box">
      <div>
        <div style="font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:#ff8a65; margin-bottom:8px;">
          Dla Zarejestrowanych Partnerów
        </div>
        <h3 style="font-family:'Outfit',sans-serif; font-size:24px; font-weight:800; color:#fff; margin-bottom:8px;">Portal Hurtowy B2B (Asseco)</h3>
        <p style="font-size:14px; color:#cbd5e1; line-height:1.55; margin-bottom:22px;">Zaloguj się do platformy handlowej Asseco ABStore, aby sprawdzić stany magazynowe w czasie rzeczywistym, swoje rabaty kontraktowe i złożyć zamówienie hurtowe.</p>
        
        <form action="https://prescot.abstore.pl/client/loginorcreate/login" method="GET" target="_blank" style="display:flex; flex-direction:column; gap:12px; margin-bottom: 20px;">
          <input type="text" name="login" placeholder="Login / E-mail w systemie Asseco" maxlength="100" autocomplete="username" style="padding:13px 16px; border-radius:10px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:#fff; outline:none; font-size:14px;">
          <input type="password" name="password" placeholder="Hasło" maxlength="64" autocomplete="current-password" style="padding:13px 16px; border-radius:10px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:#fff; outline:none; font-size:14px;">
          <button type="submit" class="p-btn p-btn-primary" style="width:100%; justify-content:center; margin-top:4px;">
            Zaloguj się do platformy B2B &rarr;
          </button>
        </form>

        <div style="margin-top: 14px;">
          <a href="https://prescot.abstore.pl/client/loginorcreate/login" target="_blank" rel="noopener" style="display:inline-flex; align-items:center; gap:6px; color:#ff8a65; font-size:13px; font-weight:700; text-decoration:none;">
            Otwórz portal Asseco ABStore w nowej karcie &rarr;
          </a>
        </div>
      </div>

      <div style="font-size:12.5px; color:#94a3b8; border-top:1px solid rgba(255,255,255,0.1); padding-top:16px; margin-top:20px;">
        Nie posiadasz jeszcze konta? Wypełnij formularz obok lub napisz: <a href="mailto:komponenty@prescot.pl" style="color:#ff8a65; text-decoration:none;">komponenty@prescot.pl</a>
      </div>
    </div>"""

for p in ["dystrybucja/index.html", "wspolpraca-b2b/index.html"]:
    fpath = os.path.join(base_dir, p)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<!-- PANEL LOGOWANIA B2B.*?</div>\s*</div>\s*</div>', asseco_box_html, c, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated Asseco B2B login portal in {p}")


# 2. Redesign B2C Modal in prescot-global.css to ULTRA-CLEAN APPLE LUXURY (No AI slop, no 90s graphics)
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

luxury_dialog_css = """
/* =========================================================
   ULTRA-CLEAN 2026 LUXURY B2C REDIRECT MODAL (NO AI SLOP)
   ========================================================= */
.prescot-b2c-dialog {
  border: none !important;
  background: transparent !important;
  padding: 0 !important;
  max-width: 420px !important;
  width: calc(100% - 32px) !important;
  margin: auto !important;
  outline: none !important;
  overflow: visible !important;
}

.prescot-b2c-dialog::backdrop {
  background: rgba(15, 23, 42, 0.65) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
}

.b2c-dialog-box {
  background: #ffffff !important;
  border-radius: 20px !important;
  padding: 36px 30px 28px 30px !important;
  text-align: center !important;
  position: relative !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 24px 60px -10px rgba(15, 23, 42, 0.35) !important;
  box-sizing: border-box !important;
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.b2c-dialog-box .b2c-top-label {
  font-size: 11px !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  letter-spacing: 1.2px !important;
  color: #e55933 !important;
  margin-bottom: 10px !important;
}

.b2c-dialog-box h3 {
  font-family: 'Outfit', sans-serif !important;
  font-size: 22px !important;
  font-weight: 800 !important;
  color: #0f172a !important;
  margin-bottom: 10px !important;
  letter-spacing: -0.02em !important;
  line-height: 1.25 !important;
}

.b2c-dialog-box p.b2c-main-desc {
  font-size: 14px !important;
  color: #475569 !important;
  line-height: 1.55 !important;
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
  padding: 13px 20px !important;
  border-radius: 12px !important;
  font-weight: 700 !important;
  font-size: 14.5px !important;
  text-decoration: none !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  transition: background-color 0.2s ease, transform 0.15s ease !important;
  box-shadow: 0 4px 12px rgba(229, 89, 51, 0.25) !important;
}

.b2c-btn-confirm:hover {
  background: #c94622 !important;
  transform: translateY(-1px) !important;
}

.b2c-btn-cancel {
  background: transparent !important;
  color: #64748b !important;
  border: none !important;
  padding: 10px 16px !important;
  font-weight: 600 !important;
  font-size: 13px !important;
  cursor: pointer !important;
  transition: color 0.2s ease !important;
}

.b2c-btn-cancel:hover {
  color: #0f172a !important;
}

.b2c-dialog-close {
  position: absolute !important;
  top: 14px !important;
  right: 16px !important;
  width: 28px !important;
  height: 28px !important;
  border-radius: 50% !important;
  border: none !important;
  background: #f1f5f9 !important;
  color: #64748b !important;
  font-size: 18px !important;
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

if "ULTRA-CLEAN 2026 LUXURY B2C REDIRECT MODAL" in css:
    css = re.sub(r'/\* =+ \s*ULTRA-CLEAN 2026 LUXURY B2C REDIRECT MODAL.*?(?=\n/\*|\Z)', luxury_dialog_css, css, flags=re.DOTALL)
else:
    css += "\n" + luxury_dialog_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated prescot-global.css with sleek minimalist B2C modal.")


# 3. Update local-navigation.js with clean minimalist HTML for B2C dialog
nav_js_path = os.path.join(base_dir, "local-navigation.js")
with open(nav_js_path, "r", encoding="utf-8") as f:
    nav_js = f.read()

clean_dialog_markup = """        <div class="b2c-dialog-box">
          <button type="button" class="b2c-dialog-close" id="b2cCloseCross" aria-label="Zamknij">&times;</button>
          
          <div class="b2c-top-label">Sklep Internetowy</div>
          <h3>Przejście do prescot.com.pl</h3>
          <p class="b2c-main-desc">Zamówienia detaliczne oraz taśmy LED na wymiar realizujemy w naszym oficjalnym sklepie internetowym.</p>
          
          <div class="b2c-dialog-actions">
            <a href="https://prescot.com.pl/" id="b2cConfirmBtn" target="_blank" rel="noopener" class="b2c-btn-confirm">
              Otwórz sklep prescot.com.pl &rarr;
            </a>
            <button type="button" class="b2c-btn-cancel" id="b2cCancelBtn">
              Wróć do strony
            </button>
          </div>
        </div>"""

nav_js = re.sub(
    r'<div class="b2c-dialog-box">.*?</div>\s*`;',
    clean_dialog_markup + '\n      `;',
    nav_js,
    flags=re.DOTALL
)

with open(nav_js_path, "w", encoding="utf-8") as f:
    f.write(nav_js)
print("Updated local-navigation.js with minimalist clean B2C modal.")


# 4. Verify GTranslate language scripts across all HTML files
gtranslate_footer = """<script>
window.gtranslateSettings = window.gtranslateSettings || {};
window.gtranslateSettings['85632840'] = {"default_language":"pl","languages":["ar","zh-CN","cs","da","en","et","fi","fr","de","it","lt","pl","es","sv"],"url_structure":"none","flag_style":"3d","wrapper_selector":"#gt-wrapper-85632840","alt_flags":[],"float_switcher_open_direction":"top","switcher_horizontal_position":"inline","flags_location":"/wp-content/plugins/gtranslate/flags/"};
</script>
<script src="/wp-content/plugins/gtranslate/js/float.js?ver=3.1.1" data-no-optimize="1" data-no-minify="1" data-gt-widget-id="85632840" defer></script>
"""

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()
            if 'float.js' not in content and '</body>' in content:
                content = content.replace('</body>', gtranslate_footer + '\n</body>')
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Injected GTranslate language flags script into {fpath}")

print("All tasks completed: Asseco B2B login integrated, sleek Apple B2C modal applied, GTranslate verified.")
