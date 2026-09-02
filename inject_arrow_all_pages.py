# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

ARROW_HTML = """
  <a href="#content-start" class="p-hero-arrow-down" aria-label="Przewiń do treści">
    <span>Przewiń niżej</span>
    <div class="p-arrow-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
    </div>
  </a>
"""

ARROW_HTML_KRECI = """
  <a href="#kreci" class="p-hero-arrow-down" aria-label="Przewiń do treści">
    <span>Przewiń niżej</span>
    <div class="p-arrow-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
    </div>
  </a>
"""

ARROW_HTML_MAIN = """
  <a href="#sekcja-glowna" class="p-hero-arrow-down" aria-label="Przewiń do treści">
    <span>Przewiń niżej</span>
    <div class="p-arrow-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
    </div>
  </a>
"""

# 1. Update prescot-global.css with the perfect elevated arrow style
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

arrow_css = """
/* =========================================================
   GLOBALNA STRZAŁKA W DÓŁ (BOUNCING ARROW) - ZAWSZE CZYSTO NAD MENU
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
  opacity: 0.9 !important;
  transition: all 0.25s ease !important;
  font-size: 11.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.6px !important;
  text-transform: uppercase !important;
}
.p-hero-arrow-down:hover {
  opacity: 1 !important;
  color: #ff8a65 !important;
  transform: translateX(-50%) translateY(2px) !important;
}
.p-arrow-icon {
  width: 36px !important;
  height: 36px !important;
  border-radius: 50% !important;
  background: rgba(255, 255, 255, 0.15) !important;
  border: 1px solid rgba(255, 255, 255, 0.35) !important;
  backdrop-filter: blur(8px) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
  animation: pBounce 2.2s infinite ease-in-out !important;
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

if ".p-hero-arrow-down" not in css:
    css += "\n" + arrow_css
else:
    css = re.sub(r'/\* =+ \s*GLOBALNA STRZAŁKA.*?(?=\n/\*|\Z)', arrow_css, css, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated prescot-global.css with elevated arrow above dock.")

# 2. Add/ensure arrow on index.html (Główna)
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_html = f.read()

# Make sure hero container has position: relative and target id
idx_html = re.sub(r'<div class="elementor-element elementor-element-216d8696([^"]*)"', r'<div class="elementor-element elementor-element-216d8696\1" style="position:relative;"', idx_html)
# Next container after hero gets id="sekcja-glowna"
idx_html = re.sub(r'(<div class="elementor-element elementor-element-270aa43b[^"]*)"', r'\1 id="sekcja-glowna"', idx_html)

if 'class="p-hero-arrow-down"' not in idx_html:
    # Insert inside first hero container right before its closing div or after inner
    idx_html = re.sub(r'(<div class="elementor-element elementor-element-216d8696.*?</video>\s*</div>)', r'\1' + ARROW_HTML_MAIN, idx_html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_html)
print("Updated index.html (Główna) with elevated arrow.")

# 3. Add/ensure arrow on prescotled/index.html
pled_path = os.path.join(base_dir, "prescotled/index.html")
if os.path.exists(pled_path):
    with open(pled_path, "r", encoding="utf-8") as f:
        pled_html = f.read()
    pled_html = re.sub(r'<div class="elementor-element elementor-element-216d8696([^"]*)"', r'<div class="elementor-element elementor-element-216d8696\1" style="position:relative;"', pled_html)
    pled_html = re.sub(r'(<div class="elementor-element elementor-element-270aa43b[^"]*)"', r'\1 id="sekcja-glowna"', pled_html)
    if 'class="p-hero-arrow-down"' not in pled_html:
        pled_html = re.sub(r'(<div class="elementor-element elementor-element-216d8696.*?</video>\s*</div>)', r'\1' + ARROW_HTML_MAIN, pled_html, flags=re.DOTALL)
    with open(pled_path, "w", encoding="utf-8") as f:
        f.write(pled_html)
    print("Updated prescotled/index.html with elevated arrow.")

# 4. Add/ensure arrow on produkcja/index.html
prod_path = os.path.join(base_dir, "produkcja/index.html")
if os.path.exists(prod_path):
    with open(prod_path, "r", encoding="utf-8") as f:
        prod_html = f.read()
    # Hero containers get position: relative
    prod_html = re.sub(r'(<div class="elementor-element elementor-element-629d57a0[^"]*)"', r'\1 style="position:relative;"', prod_html)
    prod_html = re.sub(r'(<div class="elementor-element elementor-element-280b012[^"]*)"', r'\1 style="position:relative;"', prod_html)
    if 'class="p-hero-arrow-down"' not in prod_html:
        # Insert inside desktop hero container
        prod_html = re.sub(r'(<div class="elementor-element elementor-element-629d57a0.*?</video>\s*</div>)', r'\1' + ARROW_HTML_KRECI, prod_html, flags=re.DOTALL)
        prod_html = re.sub(r'(<div class="elementor-element elementor-element-280b012.*?</video>\s*</div>)', r'\1' + ARROW_HTML_KRECI, prod_html, flags=re.DOTALL)
    with open(prod_path, "w", encoding="utf-8") as f:
        f.write(prod_html)
    print("Updated produkcja/index.html with elevated arrow.")

# 5. Dystrybucja, B2B, Kontakt, Baza Wiedzy (already have .p-hero-arrow-down inside .p-full-hero)
# Make sure their bottom CSS matches bottom: 96px above the dock!
for page in ["dystrybucja/index.html", "wspolpraca-b2b/index.html", "kontakt/index.html", "baza-wiedzy/index.html"]:
    p_path = os.path.join(base_dir, page)
    if os.path.exists(p_path):
        with open(p_path, "r", encoding="utf-8") as f:
            p_html = f.read()
        p_html = re.sub(r'bottom:\s*28px;', 'bottom: 96px;', p_html)
        with open(p_path, "w", encoding="utf-8") as f:
            f.write(p_html)
        print(f"Updated {page} with bottom: 96px.")

print("All 7 pages configured with elevated arrow cleanly above the dock menu.")
