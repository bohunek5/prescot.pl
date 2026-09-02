import re
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Read pusta/index.html as the gold standard shell
with open(os.path.join(base_dir, "pusta/index.html"), "r", encoding="utf-8") as f:
    pusta_html = f.read()

# Make sure pusta URLs are all local relative
pusta_html = pusta_html.replace("https://tasmaled.com.pl/wp-content/", "/wp-content/")
pusta_html = pusta_html.replace("https://tasmaled.com.pl/wp-includes/", "/wp-includes/")
pusta_html = pusta_html.replace("https://tasmaled.com.pl/wp-json/", "/wp-json/")

content_start = pusta_html.find('<div id="content" class="site-content">')
ast_container_start = pusta_html.find('<div class="ast-container">', content_start) + len('<div class="ast-container">\n')
footer_start = pusta_html.find('<footer data-elementor-type="footer"')

top_shell_base = pusta_html[:ast_container_start]
bottom_shell_base = '\t\t</div> <!-- ast-container -->\n\t</div><!-- #content -->\n' + pusta_html[footer_start:]

# ----------------------------------------------------
# STYLES FOR BAZA WIEDZY & KONTAKT (ASTRA COMPATIBLE)
# ----------------------------------------------------
custom_styles = """
<style id="prescot-custom-page-styles">
/* Modern Web & Astra Harmonized Styles */
:root {
  --p-primary: #e55933;
  --p-primary-hover: #c94622;
  --p-dark: #0F172A;
  --p-text: #334155;
  --p-text-muted: #64748b;
  --p-bg-subtle: #f8fafc;
  --p-border: #e2e8f0;
  --p-card-bg: #ffffff;
  --p-radius: 16px;
  --p-shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --p-shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -1px rgba(0,0,0,0.04);
  --p-shadow-lg: 0 10px 25px -3px rgba(0,0,0,0.08), 0 4px 6px -2px rgba(0,0,0,0.03);
}

.prescot-page-wrapper {
  padding: 40px 0 80px 0;
  font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--p-text);
}

/* Breadcrumbs */
.prescot-breadcrumbs {
  font-size: 13px;
  color: var(--p-text-muted);
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.prescot-breadcrumbs a {
  color: var(--p-text-muted);
  text-decoration: none;
  transition: color 0.2s;
}
.prescot-breadcrumbs a:hover {
  color: var(--p-primary);
}
.prescot-breadcrumbs .sep {
  opacity: 0.5;
}

/* Hero Header */
.prescot-hero-header {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: #ffffff;
  border-radius: var(--p-radius);
  padding: 48px 40px;
  margin-bottom: 48px;
  box-shadow: var(--p-shadow-lg);
  position: relative;
  overflow: hidden;
}
.prescot-hero-header::after {
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(229, 89, 51, 0.25) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}
.prescot-hero-header .eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(229, 89, 51, 0.2);
  color: #ff8a65;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 6px 14px;
  border-radius: 30px;
  margin-bottom: 16px;
  border: 1px solid rgba(229, 89, 51, 0.3);
}
.prescot-hero-header h1 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(32px, 4vw, 44px);
  color: #ffffff;
  margin: 0 0 16px 0;
  line-height: 1.2;
  font-weight: 700;
}
.prescot-hero-header p.lead {
  font-size: clamp(15px, 1.8vw, 17px);
  color: #cbd5e1;
  max-width: 780px;
  line-height: 1.6;
  margin: 0 0 28px 0;
}
.prescot-hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}
.prescot-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 30px;
  font-weight: 600;
  font-size: 15px;
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
  border: none;
}
.prescot-btn-primary {
  background: var(--p-primary);
  color: #ffffff !important;
  box-shadow: 0 4px 14px rgba(229, 89, 51, 0.4);
}
.prescot-btn-primary:hover {
  background: var(--p-primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(229, 89, 51, 0.5);
}
.prescot-btn-outline {
  background: transparent;
  color: #ffffff !important;
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.prescot-btn-outline:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: #ffffff;
}

/* Section Title */
.prescot-section-title {
  margin-bottom: 32px;
}
.prescot-section-title h2 {
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  color: var(--p-dark);
  margin: 0 0 8px 0;
}
.prescot-section-title p {
  color: var(--p-text-muted);
  font-size: 15px;
  margin: 0;
}

/* Calculator Grid */
.calc-card {
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  border-radius: var(--p-radius);
  padding: 36px;
  box-shadow: var(--p-shadow-md);
  margin-bottom: 56px;
}
.calc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-bottom: 32px;
}
.calc-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.calc-group label {
  font-size: 14px;
  font-weight: 600;
  color: var(--p-dark);
  display: flex;
  justify-content: space-between;
}
.calc-group select, .calc-group input {
  padding: 12px 16px;
  border: 1px solid var(--p-border);
  border-radius: 8px;
  font-size: 15px;
  background: var(--p-bg-subtle);
  color: var(--p-dark);
  transition: border-color 0.2s, box-shadow 0.2s;
  outline: none;
}
.calc-group select:focus, .calc-group input:focus {
  border-color: var(--p-primary);
  box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.15);
  background: #ffffff;
}

/* Calculator Results Box */
.calc-results-box {
  background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%);
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  padding: 28px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}
.calc-res-item {
  display: flex;
  flex-direction: column;
}
.calc-res-label {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--p-text-muted);
  font-weight: 600;
  margin-bottom: 4px;
}
.calc-res-val {
  font-size: 24px;
  font-weight: 700;
  color: var(--p-dark);
}
.calc-res-val.highlight {
  color: var(--p-primary);
}
.calc-res-tip {
  grid-column: 1 / -1;
  margin-top: 12px;
  padding-top: 16px;
  border-top: 1px solid rgba(0,0,0,0.08);
  font-size: 14px;
  color: #334155;
  display: flex;
  align-items: center;
  gap: 10px;
}
.calc-res-tip svg {
  flex-shrink: 0;
  color: var(--p-primary);
}

/* Search Box */
.bw-search-wrapper {
  position: relative;
  margin-bottom: 24px;
}
.bw-search-wrapper input {
  width: 100%;
  padding: 16px 20px 16px 48px;
  font-size: 16px;
  border: 1px solid var(--p-border);
  border-radius: 12px;
  background: var(--p-card-bg);
  box-shadow: var(--p-shadow-sm);
  outline: none;
  transition: all 0.2s;
}
.bw-search-wrapper input:focus {
  border-color: var(--p-primary);
  box-shadow: 0 0 0 4px rgba(229, 89, 51, 0.15);
}
.bw-search-wrapper svg {
  position: absolute;
  left: 18px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--p-text-muted);
}

/* Category Filter Pills */
.bw-filter-pills {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 32px;
}
.bw-pill {
  padding: 8px 18px;
  border-radius: 30px;
  font-size: 14px;
  font-weight: 600;
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  color: var(--p-text);
  cursor: pointer;
  transition: all 0.2s;
}
.bw-pill:hover {
  border-color: var(--p-primary);
  color: var(--p-primary);
}
.bw-pill.active {
  background: var(--p-dark);
  color: #ffffff;
  border-color: var(--p-dark);
}

/* FAQ Accordion List */
.faq-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 60px;
}
.faq-item {
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--p-shadow-sm);
  transition: border-color 0.2s, box-shadow 0.2s;
}
.faq-item:hover {
  border-color: #cbd5e1;
  box-shadow: var(--p-shadow-md);
}
.faq-item.open {
  border-color: var(--p-primary);
}
.faq-question {
  width: 100%;
  padding: 20px 24px;
  text-align: left;
  background: transparent;
  border: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  font-weight: 600;
  font-size: 16px;
  color: var(--p-dark);
}
.faq-question svg {
  flex-shrink: 0;
  transition: transform 0.3s ease;
  color: var(--p-primary);
}
.faq-item.open .faq-question svg {
  transform: rotate(180deg);
}
.faq-answer {
  display: none;
  padding: 0 24px 24px 24px;
  color: #475569;
  font-size: 15px;
  line-height: 1.65;
  border-top: 1px solid transparent;
}
.faq-item.open .faq-answer {
  display: block;
  border-top-color: var(--p-border);
  padding-top: 16px;
}

/* Contact Cards Grid */
.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
  margin-bottom: 48px;
}
.contact-card {
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  border-radius: var(--p-radius);
  padding: 32px;
  box-shadow: var(--p-shadow-sm);
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
}
.contact-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--p-shadow-lg);
  border-color: var(--p-primary);
}
.contact-card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(229, 89, 51, 0.1);
  color: var(--p-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}
.contact-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 20px;
  color: var(--p-dark);
  margin: 0 0 12px 0;
}
.contact-card p {
  color: var(--p-text-muted);
  font-size: 14px;
  line-height: 1.6;
  margin: 0 0 16px 0;
}
.contact-card a.link {
  color: var(--p-primary);
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: auto;
}
.contact-card a.link:hover {
  text-decoration: underline;
}

/* Contact Form & Map Layout */
.contact-main-layout {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 36px;
  margin-bottom: 60px;
}
@media (max-width: 920px) {
  .contact-main-layout {
    grid-template-columns: 1fr;
  }
}
.contact-form-box {
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  border-radius: var(--p-radius);
  padding: 36px;
  box-shadow: var(--p-shadow-md);
}
.contact-form-box h3 {
  font-family: 'Playfair Display', serif;
  font-size: 24px;
  margin: 0 0 8px 0;
  color: var(--p-dark);
}
.contact-form-box p.subtitle {
  color: var(--p-text-muted);
  font-size: 14px;
  margin: 0 0 24px 0;
}
.c-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.c-form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
@media (max-width: 600px) {
  .c-form-row {
    grid-template-columns: 1fr;
  }
}
.c-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.c-group label {
  font-size: 13px;
  font-weight: 600;
  color: var(--p-dark);
}
.c-group input, .c-group select, .c-group textarea {
  padding: 12px 16px;
  border: 1px solid var(--p-border);
  border-radius: 8px;
  font-size: 14px;
  background: var(--p-bg-subtle);
  color: var(--p-dark);
  outline: none;
  transition: all 0.2s;
}
.c-group input:focus, .c-group select:focus, .c-group textarea:focus {
  border-color: var(--p-primary);
  background: #ffffff;
  box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.15);
}
.c-group textarea {
  resize: vertical;
  min-height: 120px;
}
.c-checkbox {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 12px;
  color: var(--p-text-muted);
}
.c-checkbox input {
  margin-top: 3px;
}

.contact-map-box {
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  border-radius: var(--p-radius);
  overflow: hidden;
  box-shadow: var(--p-shadow-md);
  display: flex;
  flex-direction: column;
}
.map-frame {
  width: 100%;
  height: 320px;
  border: none;
}
.map-details {
  padding: 24px;
  background: var(--p-card-bg);
}
.map-details h4 {
  font-size: 16px;
  font-weight: 700;
  margin: 0 0 8px 0;
  color: var(--p-dark);
}
.map-details p {
  font-size: 13px;
  color: var(--p-text-muted);
  line-height: 1.5;
  margin: 0;
}
</style>
"""

# ----------------------------------------------------
# 2. GENERATE BAZA WIEDZY
# ----------------------------------------------------
print("--- Generating Baza Wiedzy ---")

bw_head = top_shell_base.replace("<title>pusta &#8211; Prescot LED</title>", "<title>Baza Wiedzy & FAQ &#8211; Prescot LED</title>")
bw_head = bw_head.replace("</head>", custom_styles + "\n</head>")

bw_content = """
<div class="prescot-page-wrapper">
  <!-- Breadcrumbs -->
  <nav class="prescot-breadcrumbs" aria-label="Nawigacja okruszkowa">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Baza Wiedzy & FAQ</span>
  </nav>

  <!-- Hero -->
  <div class="prescot-hero-header">
    <div class="eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      Oficjalne Kompendium Inżynieryjne
    </div>
    <h1>Baza Wiedzy & Kalkulator LED</h1>
    <p class="lead">Praktyczna wiedza inżynieryjna dla instalatorów, projektantów i dystrybutorów. Poznaj fizykę taśm COB/SMD, zasady doboru zasilaczy, eliminację spadków napięć i automatykę sterowania.</p>
    <div class="prescot-hero-actions">
      <a href="#kalkulator" class="prescot-btn prescot-btn-primary">
        Kalkulator Zasilania & Spadków
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="#faq" class="prescot-btn prescot-btn-outline">Przeglądaj Zagadnienia Techniczne</a>
    </div>
  </div>

  <!-- Calculator Section -->
  <div id="kalkulator" class="calc-card">
    <div class="prescot-section-title">
      <h2>Interaktywny Kalkulator Doboru Zasilacza i Spadków Napięcia</h2>
      <p>Wprowadź parametry instalacji, aby natychmiast obliczyć wymaganą moc zasilacza (z buforem +20%), pobór prądu i spadek napięcia na przewodzie.</p>
    </div>

    <div class="calc-grid">
      <div class="calc-group">
        <label for="tape-power">Moc taśmy LED na metr (W/m): <span id="tape-power-val" style="color:var(--p-primary); font-weight:700;">9.6 W/m</span></label>
        <select id="tape-power">
          <option value="4.8">4.8 W/m — Dekoracyjna SMD (300 LED)</option>
          <option value="9.6" selected>9.6 W/m — Standardowa Akcentowa SMD (600 LED)</option>
          <option value="10.0">10.0 W/m — Prescot COB Slim (Ciągła linia)</option>
          <option value="14.4">14.4 W/m — Główna Użytkowa SMD (60 LED/m 5050)</option>
          <option value="15.0">15.0 W/m — Prescot COB High Lumen CRI>90</option>
          <option value="19.2">19.2 W/m — Super Jasna SMD (120 LED/m 2835)</option>
          <option value="custom">Wpisz własną moc...</option>
        </select>
        <input type="number" id="custom-power-inp" placeholder="Wpisz moc W/m" style="display:none; margin-top:8px;" step="0.1" min="1" max="100">
      </div>

      <div class="calc-group">
        <label for="tape-length">Długość odcinka taśmy: <span id="tape-length-val" style="color:var(--p-primary); font-weight:700;">5 m</span></label>
        <input type="number" id="tape-length" value="5" min="0.5" max="100" step="0.5">
      </div>

      <div class="calc-group">
        <label for="tape-voltage">Napięcie zasilania:</label>
        <select id="tape-voltage">
          <option value="12">12V DC (Odcinki do 5m)</option>
          <option value="24" selected>24V DC (Rekomendowane Prescot — odcinki do 10m)</option>
          <option value="48">48V DC (Długie ciągi do 25-50m)</option>
        </select>
      </div>

      <div class="calc-group">
        <label for="wire-len">Długość przewodu (zasilacz -> taśma):</label>
        <input type="number" id="wire-len" value="3" min="0.1" max="50" step="0.5">
      </div>

      <div class="calc-group">
        <label for="wire-section">Przekrój żyły przewodu (miedź Cu):</label>
        <select id="wire-section">
          <option value="0.5">0.50 mm²</option>
          <option value="0.75" selected>0.75 mm² (Standard instalacyjny)</option>
          <option value="1.0">1.00 mm²</option>
          <option value="1.5">1.50 mm² (Zalecany dla długich tras)</option>
          <option value="2.5">2.50 mm² (Profesjonalny magiel B2B)</option>
        </select>
      </div>

      <div class="calc-group">
        <label for="feed-mode">Sposób podłączenia zasilania:</label>
        <select id="feed-mode">
          <option value="single" selected>Jednostronne (Początek odcinka)</option>
          <option value="double">Obustronne (Z obu stron odcinka)</option>
          <option value="loop">Przelotowe / Pętla magistrali</option>
        </select>
      </div>
    </div>

    <!-- Results Box -->
    <div class="calc-results-box">
      <div class="calc-res-item">
        <span class="calc-res-label">Moc znamionowa LED</span>
        <span class="calc-res-val" id="res-nominal-power">48.0 W</span>
      </div>

      <div class="calc-res-item">
        <span class="calc-res-label">Rekomendowany Zasilacz (+20%)</span>
        <span class="calc-res-val highlight" id="res-psu-power">min. 60 W</span>
      </div>

      <div class="calc-res-item">
        <span class="calc-res-label">Prąd roboczy (I)</span>
        <span class="calc-res-val" id="res-current">2.00 A</span>
      </div>

      <div class="calc-res-item">
        <span class="calc-res-label">Spadek napięcia na kablu</span>
        <span class="calc-res-val" id="res-voltage-drop">0.27 V (1.1%)</span>
      </div>

      <div class="calc-res-tip" id="calc-advice">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <span id="calc-advice-text"><strong>Rekomendacja inżyniera:</strong> Parametry optymalne. Spadek napięcia poniżej 3% gwarantuje jednolitą jasność na całej długości.</span>
      </div>
    </div>
  </div>

  <!-- FAQ Section -->
  <div id="faq" style="margin-top: 60px;">
    <div class="prescot-section-title">
      <h2>Baza Pytań i Odpowiedzi Inżynierów</h2>
      <p>Wyszukaj interesujące Cię zagadnienie lub wybierz kategorię tematyczną poniżej.</p>
    </div>

    <!-- Search -->
    <div class="bw-search-wrapper">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      <input type="search" id="faq-search" placeholder="Wpisz szukaną frazę (np. 48V, spadek napięcia, COB, ściemnianie, profil, gwarancja)...">
    </div>

    <!-- Filter Pills -->
    <div class="bw-filter-pills" id="faq-filters">
      <button type="button" class="bw-pill active" data-cat="all">Wszystkie (14)</button>
      <button type="button" class="bw-pill" data-cat="tasmy">Taśmy LED (5)</button>
      <button type="button" class="bw-pill" data-cat="zasilacze">Zasilacze & Dobór (3)</button>
      <button type="button" class="bw-pill" data-cat="sterowniki">Sterowniki & Ściemnianie (3)</button>
      <button type="button" class="bw-pill" data-cat="montaz">Montaż & Profile (3)</button>
    </div>

    <!-- FAQ Items -->
    <div class="faq-list" id="faq-items-container">
      <div class="faq-item" data-category="tasmy">
        <button type="button" class="faq-question">
          <span>1. Jaka jest kluczowa różnica między taśmami LED 12V, 24V a 48V?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Główną różnicą jest wartość prądu płynącego przez ścieżki miedziane PCB przy tej samej mocy. Zgodnie z prawem Ohma (P = U × I), przy napięciu 24V płynie 2-krotnie mniejszy prąd niż przy 12V, co 4-krotnie zmniejsza straty cieplne i spadki napięcia. Taśmy 24V pozwalają na zasilanie odcinków do 10m z jednego punktu bez utraty jasności, a systemy 48V aż do 25-50 metrów.
        </div>
      </div>

      <div class="faq-item" data-category="tasmy">
        <button type="button" class="faq-question">
          <span>2. Czym różni się technologia COB (Chip on Board) od tradycyjnych diod SMD?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          W taśmach COB setki mikroskopijnych chipów LED są montowane bezpośrednio na elastycznym podłożu miedzianym i pokrywane ciągłą warstwą luminoforu. Daje to idealnie jednolitą linię światła (bez widocznych punktów świetlnych) nawet w bardzo płytkich profilach aluminiowych oraz szeroki kąt świecenia 180°.
        </div>
      </div>

      <div class="faq-item" data-category="zasilacze">
        <button type="button" class="faq-question">
          <span>3. Jak prawidłowo dobrać moc zasilacza do długości taśmy LED?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Moc zasilacza obliczamy mnożąc łączną długość taśmy przez jej moc jednostkową (W/m), a następnie dodając <strong>minimum 20% buforu bezpieczeństwa</strong>: Moc zasilacza = (Długość × Moc/m) × 1.20. Bufor zapobiega pracy zasilacza na skraju wydajności prądowej, chroni przed przegrzaniem i wydłuża żywotność komponentów do ponad 50 000 godzin.
        </div>
      </div>

      <div class="faq-item" data-category="tasmy">
        <button type="button" class="faq-question">
          <span>4. Jak uniknąć spadków napięcia na długich odcinkach (powyżej 5m)?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Dla odcinków powyżej 5m (w systemach 12V) lub powyżej 10m (w systemach 24V) zaleca się: 1) zasilenie obustronne (doprowadzenie przewodów zasilacza do obu końców taśmy), 2) zastosowanie magistrali zasilającej z przewodu o przekroju 1.5–2.5 mm² z wpięciami co 5 metrów, lub 3) wybór taśm wysokonapięciowych 48V.
        </div>
      </div>

      <div class="faq-item" data-category="montaz">
        <button type="button" class="faq-question">
          <span>5. Dlaczego profil aluminiowy jest bezwzględnie wymagany przy mocach powyżej 9.6W/m?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Aluminium pełni funkcję radiatora odprowadzającego ciepło z chipów LED. Praca taśmy o mocy >9.6W/m naklejonej bezpośrednio na drewno, karton-gips czy tworzywo sztuczne powoduje degradację złącza p-n diody, przyspieszoną utratę strumienia świetlnego (L70) oraz odbarwienie luminoforu w ciągu kilku miesięcy.
        </div>
      </div>

      <div class="faq-item" data-category="sterowniki">
        <button type="button" class="faq-question">
          <span>6. Czy taśmy LED Prescot można ściemniać za pomocą protokołów DALI, 0-10V, Tuya i Triac?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Tak, wszystkie stałonapięciowe taśmy LED Prescot współpracują ze ściemniaczami PWM w technologiach: DALI-2, 0/1-10V, PUSH-DIM, Zigbee 3.0, Tuya Wi-Fi, MiBoxer 2.4GHz oraz zasilaczami ściemnianymi fazowo (Triac/Faza).
        </div>
      </div>

      <div class="faq-item" data-category="tasmy">
        <button type="button" class="faq-question">
          <span>7. Jakie znaczenie ma współczynnik oddawania barw CRI (Ra) w oświetleniu wnętrz?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          CRI (Color Rendering Index) określa wierność odwzorowania barw oświetlanych przedmiotów w porównaniu do światła słonecznego (CRI=100). Taśmy profesjonalne Prescot oferują CRI > 90 i CRI > 95 (z wysokim R9 dla czerwieni), co eliminuje szary, nienaturalny odcień skóry, potraw i mebli.
        </div>
      </div>

      <div class="faq-item" data-category="montaz">
        <button type="button" class="faq-question">
          <span>8. Czym różnią się klasy szczelności IP20, IP65 i IP68 w zastosowaniach zewnętrznych?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          IP20: brak ochrony przed wilgocią (suche wnętrza). IP65: powłoka nano-hydrofobowa lub silikonowa chroniąca przed zachlapaniem (łazienki, kuchnie). IP68: pełna osłona silikonowa / poliuretanowa odporna na ciągłe zanurzenie w wodzie i promieniowanie UV (elewacje, baseny, ogrody).
        </div>
      </div>

      <div class="faq-item" data-category="zasilacze">
        <button type="button" class="faq-question">
          <span>9. Jak dobrać odpowiedni przekrój przewodu między zasilaczem a taśmą LED?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Dla odległości do 2m wystarcza przewód 0.75 mm². Przy odległościach 3–10m zaleca się 1.50 mm², a powyżej 10m – 2.50 mm². W instalacjach niskonapięciowych zbyt cienki kabel działa jak opornik, nagrzewa się i powoduje widoczny spadek jasności diod.
        </div>
      </div>

      <div class="faq-item" data-category="tasmy">
        <button type="button" class="faq-question">
          <span>10. Czy taśmy LED 48V można ciąć w dowolnym miejscu?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Taśmy LED można ciąć wyłącznie w wyznaczonych punktach oznaczonych symbolem nożyczek lub padów lutowniczych. Ze względu na wyższe napięcie, moduł cięcia w taśmach 48V wynosi zazwyczaj od 10cm do 16.6cm (w zależności od serii).
        </div>
      </div>

      <div class="faq-item" data-category="montaz">
        <button type="button" class="faq-question">
          <span>11. Jak poprawnie połączyć taśmy LED w narożnikach – lutowanie czy szybkozłączki?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Dla instalacji profesjonalnych i komercyjnych bezwzględnie rekomendujemy lutowanie miękkie cyną ołowiową/bezołowiową z zabezpieczeniem koszulką termokurczliwą. Szybkozłączki wciskane z czasem mogą utracić docisk pod wpływem cykli nagrzewania i stygnięcia profilu.
        </div>
      </div>

      <div class="faq-item" data-category="sterowniki">
        <button type="button" class="faq-question">
          <span>12. Co oznacza pojęcie SDCM (MacAdam Ellipse) w selekcji barwowej diod?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          SDCM (Standard Deviation Colour Matching) określa tolerancję barwową między partiami diod. Taśmy Prescot w standardzie PRO posiadają binowanie SDCM &le; 3, co oznacza, że różnice w odcieniu bieli są całkowicie niedostrzegalne dla ludzkiego oka nawet przy bezpośrednim łączeniu rolek z różnych partii produkcyjnych.
        </div>
      </div>

      <div class="faq-item" data-category="zasilacze">
        <button type="button" class="faq-question">
          <span>13. Jakie zabezpieczenia powinien posiadać profesjonalny zasilacz impulsowy LED?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Zasilacze Prescot wyposażone są w potrójny układ zabezpieczeń: OVP (nadnapięciowe), OCP (przeciążeniowe), SCP (zwarciowe z automatycznym powrotem do pracy po ustąpieniu awarii) oraz OTP (termiczne wyłączające zasilacz przy przekroczeniu bezpiecznej temperatury).
        </div>
      </div>

      <div class="faq-item" data-category="sterowniki">
        <button type="button" class="faq-question">
          <span>14. Jaka jest gwarancja na profesjonalne serie taśm Prescot LED?</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="faq-answer">
          Seria Prescot Professional i COB objęta jest 5-letnią gwarancją producenta dla partnerów B2B oraz certyfikatem żywotności L80B10 &gt; 54 000 godzin przy zachowaniu odpowiednich profili aluminiowych.
        </div>
      </div>
    </div>
  </div>
</div>

<!-- CALCULATOR & FAQ JAVASCRIPT LOGIC -->
<script>
(function() {
  // --- CALCULATOR LOGIC ---
  const tapePowerSelect = document.getElementById('tape-power');
  const customPowerInp = document.getElementById('custom-power-inp');
  const tapeLengthInp = document.getElementById('tape-length');
  const tapeVoltageSelect = document.getElementById('tape-voltage');
  const wireLenInp = document.getElementById('wire-len');
  const wireSectionSelect = document.getElementById('wire-section');
  const feedModeSelect = document.getElementById('feed-mode');

  const resNominal = document.getElementById('res-nominal-power');
  const resPsu = document.getElementById('res-psu-power');
  const resCurrent = document.getElementById('res-current');
  const resVoltageDrop = document.getElementById('res-voltage-drop');
  const resAdviceText = document.getElementById('calc-advice-text');

  function calculate() {
    let powerPerM = parseFloat(tapePowerSelect.value);
    if (tapePowerSelect.value === 'custom') {
      powerPerM = parseFloat(customPowerInp.value) || 10;
    }
    const length = parseFloat(tapeLengthInp.value) || 1;
    const voltage = parseFloat(tapeVoltageSelect.value) || 24;
    const wireLen = parseFloat(wireLenInp.value) || 1;
    const wireSection = parseFloat(wireSectionSelect.value) || 0.75;
    const feedMode = feedModeSelect.value;

    const nominalPower = powerPerM * length;
    const minPsuPower = nominalPower * 1.20;
    const current = nominalPower / voltage;

    // Resistance of copper (rho = 0.0175 Ohm*mm2/m)
    // 2 wires (positive + negative) -> 2 * length
    const totalWireLen = wireLen * 2;
    const wireResistance = (0.0175 * totalWireLen) / wireSection;
    
    // Effective current on wire depends on feed mode
    let effectiveCurrent = current;
    if (feedMode === 'double') effectiveCurrent = current / 2;
    if (feedMode === 'loop') effectiveCurrent = current / 2.5;

    const vDrop = effectiveCurrent * wireResistance;
    const vDropPercent = (vDrop / voltage) * 100;

    resNominal.innerText = nominalPower.toFixed(1) + ' W';
    resPsu.innerText = 'min. ' + Math.ceil(minPsuPower) + ' W';
    resCurrent.innerText = current.toFixed(2) + ' A';
    resVoltageDrop.innerText = vDrop.toFixed(2) + ' V (' + vDropPercent.toFixed(1) + '%)';

    // Status advice
    if (vDropPercent > 5) {
      resVoltageDrop.style.color = '#ef4444';
      resAdviceText.innerHTML = '<strong>Uwaga:</strong> Spadek napięcia przekracza 5%! Zalecamy zwiększenie przekroju przewodu na ' + (wireSection < 1.5 ? '1.5 mm² lub 2.5 mm²' : '2.5 mm²') + ' lub zasilenie obustronne.';
    } else if (vDropPercent > 3) {
      resVoltageDrop.style.color = '#f59e0b';
      resAdviceText.innerHTML = '<strong>Wskazówka:</strong> Spadek napięcia (3-5%) jest dopuszczalny, ale dla idealnej jednolitości zalecamy zasilenie obustronne.';
    } else {
      resVoltageDrop.style.color = 'var(--p-primary)';
      resAdviceText.innerHTML = '<strong>Rekomendacja inżyniera:</strong> Parametry optymalne. Spadek napięcia poniżej 3% gwarantuje jednolitą jasność na całej długości.';
    }
  }

  tapePowerSelect.addEventListener('change', function() {
    if (this.value === 'custom') {
      customPowerInp.style.display = 'block';
    } else {
      customPowerInp.style.display = 'none';
      document.getElementById('tape-power-val').innerText = this.options[this.selectedIndex].text.split('—')[0].trim();
    }
    calculate();
  });

  tapeLengthInp.addEventListener('input', function() {
    document.getElementById('tape-length-val').innerText = this.value + ' m';
    calculate();
  });

  customPowerInp.addEventListener('input', calculate);
  tapeVoltageSelect.addEventListener('change', calculate);
  wireLenInp.addEventListener('input', calculate);
  wireSectionSelect.addEventListener('change', calculate);
  feedModeSelect.addEventListener('change', calculate);

  calculate();

  // --- FAQ ACCORDION LOGIC ---
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const isOpen = item.classList.contains('open');
      // close all
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  // --- FAQ FILTER PILLS ---
  const filterPills = document.querySelectorAll('.bw-pill');
  const faqItems = document.querySelectorAll('.faq-item');

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const cat = pill.getAttribute('data-cat');
      
      faqItems.forEach(item => {
        if (cat === 'all' || item.getAttribute('data-category') === cat) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // --- FAQ SEARCH ---
  const searchInp = document.getElementById('faq-search');
  searchInp.addEventListener('input', function() {
    const q = this.value.toLowerCase().trim();
    faqItems.forEach(item => {
      const text = item.innerText.toLowerCase();
      if (text.includes(q)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
})();
</script>
"""

with open(os.path.join(base_dir, "baza-wiedzy/index.html"), "w", encoding="utf-8") as f:
    f.write(bw_head + bw_content + bottom_shell_base)
print("Baza Wiedzy generated successfully.")


# ----------------------------------------------------
# 3. GENERATE KONTAKT
# ----------------------------------------------------
print("--- Generating Kontakt ---")

kt_head = top_shell_base.replace("<title>pusta &#8211; Prescot LED</title>", "<title>Kontakt &#8211; Prescot LED</title>")
kt_head = kt_head.replace("</head>", custom_styles + "\n</head>")

kt_content = """
<div class="prescot-page-wrapper">
  <!-- Breadcrumbs -->
  <nav class="prescot-breadcrumbs" aria-label="Nawigacja okruszkowa">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Kontakt</span>
  </nav>

  <!-- Hero -->
  <div class="prescot-hero-header">
    <div class="eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      Oficjalny Kontakt i Dystrybucja B2B
    </div>
    <h1>Skontaktuj się z zespołem Prescot LED</h1>
    <p class="lead">Nasi inżynierowie i doradcy techniczno-handlowi są do Twojej dyspozycji. Zapewniamy kompleksowe doradztwo projektowe, wyceny inwestycyjne oraz bezpośrednią obsługę hurtową.</p>
    <div class="prescot-hero-actions">
      <a href="#formularz" class="prescot-btn prescot-btn-primary">
        Napisz do nas
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="tel:+48877776482" class="prescot-btn prescot-btn-outline">Zadzwoń do działu sprzedaży</a>
    </div>
  </div>

  <!-- Contact Cards Grid -->
  <div class="contact-grid">
    <!-- Card 1: Adres & Siedziba -->
    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      </div>
      <h3>Siedziba & Salon Firmowy</h3>
      <p>
        <strong>PRESCOT sp. z o.o.</strong><br>
        ul. Wileńska 1<br>
        11-500 Giżycko, Polska<br>
        <span style="font-size: 12px; color: var(--p-text-muted);">NIP: 8451993424 | KRS: 0000882894</span>
      </p>
      <p style="margin-bottom:0; font-size:13px;">
        <strong>Godziny otwarcia:</strong><br>
        Pn – Pt: 07:30 – 16:30
      </p>
    </div>

    <!-- Card 2: Biuro & Sekretariat -->
    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      </div>
      <h3>Biuro & Sekretariat</h3>
      <p>
        Obsługa korespondencji, administracja oraz ogólne zapytania firmowe.
      </p>
      <p>
        <strong>Telefon:</strong> <a href="tel:+48874282118" style="color:var(--p-dark); font-weight:600; text-decoration:none;">+48 87 428 21 18</a><br>
        <strong>E-mail:</strong> <a href="mailto:sekretariat@prescot.pl" style="color:var(--p-primary); text-decoration:none; font-weight:600;">sekretariat@prescot.pl</a>
      </p>
      <a href="mailto:sekretariat@prescot.pl" class="link">Napisz do sekretariatu &rarr;</a>
    </div>

    <!-- Card 3: Dział Sprzedaży B2B -->
    <div class="contact-card">
      <div class="contact-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </div>
      <h3>Dział Sprzedaży & B2B</h3>
      <p>
        Wyceny hurtowe, rabaty dla instalatorów, wsparcie projektowe i doradztwo LED.
      </p>
      <p>
        <strong>Telefon:</strong> <a href="tel:+48877776482" style="color:var(--p-dark); font-weight:600; text-decoration:none;">+48 87 777 64 82</a><br>
        <strong>E-mail:</strong> <a href="mailto:komponenty@prescot.pl" style="color:var(--p-primary); text-decoration:none; font-weight:600;">komponenty@prescot.pl</a>
      </p>
      <a href="mailto:komponenty@prescot.pl" class="link">Skontaktuj się ze sprzedażą &rarr;</a>
    </div>
  </div>

  <!-- Form & Map Section -->
  <div id="formularz" class="contact-main-layout">
    <!-- Form Box -->
    <div class="contact-form-box">
      <h3>Wyślij zapytanie handlowe lub techniczne</h3>
      <p class="subtitle">Wypełnij formularz — nasz doradca skontaktuje się z Tobą w ciągu maksymalnie 4 godzin roboczych.</p>

      <form class="c-form" id="main-contact-form" action="javascript:void(0);">
        <div class="c-form-row">
          <div class="c-group">
            <label for="c-name">Imię i nazwisko / Firma *</label>
            <input type="text" id="c-name" placeholder="np. Jan Kowalski / Elektro-Projekt" required>
          </div>
          <div class="c-group">
            <label for="c-nip">NIP (dla klientów B2B)</label>
            <input type="text" id="c-nip" placeholder="np. 8451993424">
          </div>
        </div>

        <div class="c-form-row">
          <div class="c-group">
            <label for="c-email">Adres e-mail *</label>
            <input type="email" id="c-email" placeholder="twoj-email@firma.pl" required>
          </div>
          <div class="c-group">
            <label for="c-phone">Numer telefonu *</label>
            <input type="tel" id="c-phone" placeholder="+48 000 000 000" required>
          </div>
        </div>

        <div class="c-group">
          <label for="c-dept">Dział docelowy zapytania</label>
          <select id="c-dept">
            <option value="sprzedaz">Dział Sprzedaży Hurtowej i Współpracy B2B</option>
            <option value="techniczne">Doradztwo Techniczne i Dobór Komponentów LED</option>
            <option value="zamowienia">Logistyka, Realizacja Zamówień i Magazyn</option>
            <option value="inne">Inny temat / Zapytanie ogólne</option>
          </select>
        </div>

        <div class="c-group">
          <label for="c-msg">Wiadomość / Zestawienie materiałowe *</label>
          <textarea id="c-msg" placeholder="Wpisz treść zapytania, specyfikację taśm, zasilaczy lub założeń projektu..." required></textarea>
        </div>

        <div class="c-checkbox">
          <input type="checkbox" id="c-rodo" required>
          <label for="c-rodo">Wyrażam zgodę na przetwarzanie danych osobowych przez PRESCOT sp. z o.o. w celu obsługi zapytania zgodnie z Polityką Prywatności.</label>
        </div>

        <button type="submit" class="prescot-btn prescot-btn-primary" style="align-self: flex-start; margin-top: 8px;">
          Wyślij wiadomość
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
        </button>

        <div id="c-feedback" style="display:none; padding:12px 16px; border-radius:8px; font-size:14px; margin-top:10px;"></div>
      </form>
    </div>

    <!-- Map Box -->
    <div class="contact-map-box">
      <iframe class="map-frame" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2342.348614488344!2d21.761278177114674!3d54.041697972498775!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46e16a247ea762a5%3A0x6d88b48858a74e50!2sWile%C5%84ska%201%2C%2011-500%20Gi%C5%BCycko!5e0!3m2!1spl!2spl!4v1710000000000!5m2!1spl!2spl" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      <div class="map-details">
        <h4>Centrum Dystrybucyjne Giżycko</h4>
        <p><strong>Lokalizacja:</strong> ul. Wileńska 1, 11-500 Giżycko</p>
        <p style="margin-top:6px;">Dostępny bezpłatny parking dla instalatorów i pojazdów dostawczych B2B. Odbiór osobisty towaru po wcześniejszym potwierdzeniu.</p>
      </div>
    </div>
  </div>
</div>

<script>
document.getElementById('main-contact-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const fb = document.getElementById('c-feedback');
  fb.style.display = 'block';
  fb.style.background = '#dcfce7';
  fb.style.color = '#166534';
  fb.style.border = '1px solid #bbf7d0';
  fb.innerHTML = '<strong>Dziękujemy!</strong> Twoja wiadomość została pomyślnie wysłana do działu ' + document.getElementById('c-dept').options[document.getElementById('c-dept').selectedIndex].text + '. Skontaktujemy się z Tobą niezwłocznie.';
  this.reset();
});
</script>
"""

with open(os.path.join(base_dir, "kontakt/index.html"), "w", encoding="utf-8") as f:
    f.write(kt_head + kt_content + bottom_shell_base)
print("Kontakt generated successfully.")

