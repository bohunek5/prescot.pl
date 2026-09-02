# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
DARK_LOGO = "/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"
WHITE_LOGO = "/wp-content/uploads/2025/12/biale-z-kolorem.svg"

# 1. Update scratch/footer.html with DARK LOGO (PRESCOT_logo-podstawowe.svg)
footer_path = "/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html"
with open(footer_path, "r", encoding="utf-8") as f:
    footer_html = f.read()

# Ensure dark logo in footer
footer_html = re.sub(r'data-src="[^"]*logo[^"]*"', f'data-src="{DARK_LOGO}"', footer_html)
footer_html = re.sub(r'src="[^"]*biale-z-kolorem\.svg"', f'src="{DARK_LOGO}"', footer_html)
footer_html = re.sub(r'<div class="footerLogo">\s*<img[^>]*>', f'<div class="footerLogo">\n            <img src="{DARK_LOGO}" alt="Prescot LED Logo">', footer_html)

with open(footer_path, "w", encoding="utf-8") as f:
    f.write(footer_html)

print("Footer updated with DARK logo.")

# 2. Modern, Architectural, Authentic Prescot LED Calculator & FAQ Styling
prescot_calc_and_faq_css = """
  /* =========================================================
     AUTHENTIC PRESCOT ARCHITECTURAL STYLING (NO CHEAP PASTELS)
     ========================================================= */
  :root {
    --p-orange: #e55933;
    --p-orange-hover: #c94622;
    --p-carbon: #0f172a;
    --p-carbon-light: #1e293b;
    --p-slate: #64748b;
    --p-slate-dark: #334155;
    --p-bg: #f8fafc;
    --p-card: #ffffff;
    --p-border: #e2e8f0;
  }

  /* FAQ SECTION - MINIMALIST & TECHNICAL */
  .faq-search-wrap {
    margin-bottom: 28px;
    position: relative;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }
  .faq-search-input {
    width: 100%;
    padding: 16px 20px 16px 52px;
    font-size: 15px;
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 12px;
    outline: none;
    color: var(--p-carbon);
    font-family: inherit;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    transition: all 0.2s ease;
  }
  .faq-search-input:focus {
    border-color: var(--p-orange);
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.12);
  }
  .faq-search-icon {
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--p-slate);
    pointer-events: none;
  }
  .faq-filter-chips {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }
  .chip-btn {
    padding: 9px 20px;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 600;
    background: #ffffff;
    border: 1px solid var(--p-border);
    color: var(--p-slate-dark);
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
  }
  .chip-btn.active, .chip-btn:hover {
    background: var(--p-carbon);
    color: #ffffff;
    border-color: var(--p-carbon);
  }
  .faq-grid {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 80px;
    max-width: 960px;
    margin-left: auto;
    margin-right: auto;
  }
  .faq-card {
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.2s ease;
  }
  .faq-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  }
  .faq-btn {
    width: 100%;
    text-align: left;
    background: none;
    border: none;
    padding: 22px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    cursor: pointer;
    font-weight: 700;
    font-size: 16px;
    color: var(--p-carbon);
    font-family: 'Outfit', sans-serif;
  }
  .faq-btn-icon {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #f1f5f9;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--p-slate);
    transition: transform 0.25s ease, background 0.2s;
  }
  .faq-card.open .faq-btn-icon {
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-orange);
    transform: rotate(180deg);
  }
  .faq-card.open .faq-btn { color: var(--p-orange); }
  .faq-content {
    display: none;
    padding: 0 24px 22px 24px;
    color: #475569;
    font-size: 14.5px;
    line-height: 1.7;
  }
  .faq-card.open .faq-content {
    display: block;
    border-top: 1px solid #f1f5f9;
    padding-top: 16px;
  }

  /* =========================================================
     ARCHITECTURAL HIGH-END KALKULATOR (CARBON MATTE & ORANGE)
     ========================================================= */
  .calc-container {
    background: #0b1120;
    border: 1px solid #1e293b;
    border-radius: 18px;
    padding: 44px;
    color: #ffffff;
    box-shadow: 0 20px 40px -15px rgba(0,0,0,0.5);
    margin-bottom: 60px;
  }
  .calc-header-wrap {
    border-bottom: 1px solid #1e293b;
    padding-bottom: 24px;
    margin-bottom: 36px;
  }
  .calc-header-wrap h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
  }
  .calc-header-wrap p {
    color: #94a3b8;
    font-size: 14.5px;
    line-height: 1.5;
  }
  .calc-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 40px;
  }
  @media (max-width: 900px) {
    .calc-grid { grid-template-columns: 1fr; }
    .calc-container { padding: 28px 20px; }
  }
  .calc-form-col {
    display: flex;
    flex-direction: column;
    gap: 22px;
  }
  .calc-form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
  }
  @media (max-width: 550px) {
    .calc-form-row { grid-template-columns: 1fr; }
  }
  .calc-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .calc-group label {
    font-size: 13px;
    font-weight: 600;
    color: #cbd5e1;
    letter-spacing: 0.3px;
  }
  .calc-group select, .calc-group input {
    padding: 13px 16px;
    background: #131c2e;
    border: 1px solid #283548;
    border-radius: 10px;
    font-size: 14.5px;
    color: #ffffff;
    outline: none;
    font-family: inherit;
    transition: all 0.2s ease;
  }
  .calc-group select:focus, .calc-group input:focus {
    border-color: var(--p-orange);
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.2);
    background: #172237;
  }
  .calc-results-col {
    background: #131c2e;
    border: 1px solid #283548;
    border-radius: 14px;
    padding: 30px 28px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .calc-res-title {
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--p-orange);
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }
  .calc-res-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 11px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }
  .calc-res-row:last-of-type { border-bottom: none; }
  .calc-res-lbl {
    font-size: 13.5px;
    color: #94a3b8;
  }
  .calc-res-num {
    font-size: 21px;
    font-weight: 700;
    font-family: 'Outfit', sans-serif;
    color: #ffffff;
  }
  .calc-res-num.highlight {
    color: var(--p-orange);
    font-size: 25px;
  }
  .calc-rec-box {
    margin-top: 24px;
    background: rgba(229, 89, 51, 0.08);
    border: 1px solid rgba(229, 89, 51, 0.3);
    border-radius: 10px;
    padding: 16px 18px;
    font-size: 13.5px;
    color: #e2e8f0;
    line-height: 1.55;
  }
  .calc-rec-box strong { color: #ffffff; }
"""

# Update Baza Wiedzy
baza_fpath = os.path.join(base_dir, "baza-wiedzy/index.html")

baza_content = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/wp-content/uploads/2025/09/cropped-favicon-1-32x32.png" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Krona+One&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/prescot-global.css?v=20260901-white-dock">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <title>Baza Wiedzy & Kalkulator Zasilania LED — Prescot LED</title>
  <style>
  :root {
    --p-primary: #e55933;
    --p-primary-hover: #c94622;
    --p-dark: #0f172a;
    --p-dark-soft: #1e293b;
    --p-text: #212a35;
    --p-text-muted: #64748b;
    --p-bg: #f8fafc;
    --p-border: #e2e8f0;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--p-text);
    background: var(--p-bg);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding-bottom: 90px;
  }

  /* FULL-SCREEN 100VH HERO SLIDE */
  .p-full-hero {
    position: relative;
    width: 100%;
    min-height: 100vh;
    height: 100vh;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 80px 24px 70px 24px;
    color: #ffffff;
    overflow: hidden;
  }
  .p-full-hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.65) 0%, rgba(15, 23, 42, 0.85) 100%);
    z-index: 1;
  }
  .p-full-hero-content {
    position: relative;
    z-index: 2;
    max-width: 920px;
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .p-hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(229, 89, 51, 0.2);
    color: #ff8a65;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    padding: 7px 18px;
    border-radius: 30px;
    margin-bottom: 22px;
    border: 1px solid rgba(229, 89, 51, 0.4);
    backdrop-filter: blur(6px);
  }
  .p-full-hero h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(34px, 4.5vw, 54px);
    color: #ffffff;
    margin-bottom: 20px;
    line-height: 1.18;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.4);
  }
  .p-full-hero p.lead {
    font-size: clamp(16px, 1.9vw, 19px);
    color: #e2e8f0;
    max-width: 820px;
    line-height: 1.65;
    margin-bottom: 32px;
    text-shadow: 0 1px 4px rgba(0,0,0,0.4);
  }
  .p-hero-actions {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    justify-content: center;
  }
  .p-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 14px 28px;
    border-radius: 30px;
    font-weight: 600;
    font-size: 15px;
    text-decoration: none;
    transition: all 0.25s ease;
    cursor: pointer;
    border: none;
    font-family: inherit;
  }
  .p-btn-primary {
    background: var(--p-primary);
    color: #ffffff !important;
    box-shadow: 0 4px 14px rgba(229, 89, 51, 0.35);
  }
  .p-btn-primary:hover {
    background: var(--p-primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(229, 89, 51, 0.5);
  }
  .p-btn-outline {
    background: rgba(255, 255, 255, 0.12);
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(8px);
  }
  .p-btn-outline:hover {
    background: rgba(255, 255, 255, 0.22);
    border-color: #ffffff;
  }

  .p-hero-arrow-down {
    position: absolute;
    bottom: 28px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    text-decoration: none;
    cursor: pointer;
    opacity: 0.85;
    transition: all 0.25s ease;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .p-hero-arrow-down:hover { opacity: 1; color: #ff8a65; }
  .p-arrow-icon {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(6px);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: pBounce 2.2s infinite ease-in-out;
  }
  @keyframes pBounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
  }

  .prescot-main-container {
    max-width: 1240px;
    margin: 0 auto;
    padding: 60px 24px 80px 24px;
  }
  .prescot-breadcrumbs {
    font-size: 13px;
    color: var(--p-text-muted);
    margin-bottom: 32px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .prescot-breadcrumbs a { color: var(--p-text-muted); text-decoration: none; }
  .prescot-breadcrumbs a:hover { color: var(--p-primary); }
  .prescot-breadcrumbs .sep { opacity: 0.4; }

  """ + prescot_calc_and_faq_css + """
  </style>
</head>
<body>
<!-- SMART LOGO: BIAŁE Z POMARAŃCZEM (ZNIKA PRZY SCROLLU W DÓŁ, WRACA W GÓRĘ) -->
<div class="prescot-smart-logo">
  <a href="/" title="Prescot LED Strona Główna">
    <img src="/wp-content/uploads/2025/12/biale-z-kolorem.svg" alt="Prescot LED">
  </a>
</div>

<!-- FULL-SCREEN 100VH HERO SLIDE -->
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/03/AdobeStock_1101216226-1536x861.webp');">
  <div class="p-full-hero-content">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      Kompendium Inżynieryjne
    </div>
    <h1>Baza Wiedzy, Poradniki & FAQ Prescot LED</h1>
    <p class="lead">Profesjonalna wiedza techniczna dla instalatorów, projektantów i dystrybutorów. Poznaj zasady doboru taśm COB, eliminacji spadków napięć, obliczania zasilaczy i automatyki sterowania oświetleniem.</p>
    <div class="p-hero-actions">
      <a href="#faq-section" class="p-btn p-btn-primary">
        Przeglądaj Zagadnienia FAQ
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 14l-7 7m0 0l-7-7m7 7V3"/></svg>
      </a>
      <a href="#kalkulator-led" class="p-btn p-btn-outline">
        Kalkulator Zasilania & Spadków ↓
      </a>
    </div>
  </div>

  <a href="#content-start" class="p-hero-arrow-down" aria-label="Przewiń do treści">
    <span>Przewiń niżej</span>
    <div class="p-arrow-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
    </div>
  </a>
</section>

<!-- TREŚĆ PONIŻEJ HERO -->
<main id="content-start" class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Baza Wiedzy & FAQ</span>
  </nav>

  <!-- FAQ SECTION -->
  <section id="faq-section" style="margin-bottom: 70px;">
    <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 32px; color: var(--p-dark); margin-bottom: 10px;">Najczęściej zadawane pytania</h2>
      <p style="color: var(--p-text-muted); font-size: 15.5px;">Wyszukaj odpowiedź na swoje pytanie techniczne lub wybierz interesującą Cię kategorię.</p>
    </div>

    <div class="faq-search-wrap">
      <svg class="faq-search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" id="faqSearchInput" class="faq-search-input" placeholder="Wpisz szukaną frazę (np. spadek napięcia, zasilacz, COB, montaż profilu)...">
    </div>

    <div class="faq-filter-chips">
      <button type="button" class="chip-btn active" data-filter="all">Wszystkie (14)</button>
      <button type="button" class="chip-btn" data-filter="tasmy">Taśmy &amp; COB (4)</button>
      <button type="button" class="chip-btn" data-filter="zasilanie">Zasilanie &amp; Spadki (4)</button>
      <button type="button" class="chip-btn" data-filter="sterowanie">Sterowniki &amp; RF (3)</button>
      <button type="button" class="chip-btn" data-filter="montaz">Profile &amp; Montaż (3)</button>
    </div>

    <div class="faq-grid" id="faqAccordion">
      <div class="faq-card" data-cat="tasmy">
        <button class="faq-btn" type="button">
          <span>Czym różnią się taśmy LED COB od tradycyjnych SMD?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśmy COB (Chip on Board) posiadają gęsto upakowane chipy LED pokryte ciągłą warstwą luminoforu (np. 320–528 chipów/m), co daje idealnie jednolitą linię światła bez widocznych punktów świetlnych (tzw. efektu kropkowania), nawet w bardzo płytkich profilach aluminiowych.</p>
        </div>
      </div>

      <div class="faq-card" data-cat="zasilanie">
        <button class="faq-btn" type="button">
          <span>Dlaczego na długich odcinkach taśmy LED 12V/24V występuje spadek jasności?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Wynika to z oporu elektrycznego miedzianych ścieżek na laminacie PCB (zjawisko spadku napięcia). Dla taśm 12V zaleca się zasilanie odcinków maksymalnie do 5 metrów jednostronnie. Dla taśm 24V dystans ten wynosi do 10 metrów. Przy dłuższych liniach należy zastosować zasilanie dwustronne lub linię magistralną.</p>
        </div>
      </div>

      <div class="faq-card" data-cat="zasilanie">
        <button class="faq-btn" type="button">
          <span>Jaki zapas mocy powinien mieć profesjonalny zasilacz LED?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Zalecany inżynieryjny margines bezpieczeństwa wynosi minimum <strong>15–20%</strong> ponad sumaryczną moc pobieraną przez podłączone taśmy. Chroni to zasilacz przed przegrzaniem i gwarantuje stabilną wieloletnią pracę.</p>
        </div>
      </div>

      <div class="faq-card" data-cat="tasmy">
        <button class="faq-btn" type="button">
          <span>Co oznacza wskaźnik CRI (Ra) &gt; 90 w taśmach Prescot LED?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>CRI (Color Rendering Index) określa wierność oddawania barw oświetlanych przedmiotów w porównaniu do światła słonecznego. Taśmy Prescot o CRI &gt; 90 gwarantują naturalny wygląd potraw, drewna, tkanin i skóry, nie męcząc wzroku.</p>
        </div>
      </div>

      <div class="faq-card" data-cat="sterowanie">
        <button class="faq-btn" type="button">
          <span>Jak sparować pilot strefowy RF z odbiornikiem Prescot / MiBoxer?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>1. Odłącz zasilanie odbiornika na 10 sekund i włącz je ponownie.<br>2. W ciągu 3 sekund od włączenia naciśnij krótko 3-krotnie przycisk „ON” wybranej strefy na pilocie.<br>3. Pomyślne parowanie potwierdza 3-krotne mrugnięcie podłączonej taśmy LED.</p>
        </div>
      </div>

      <div class="faq-card" data-cat="montaz">
        <button class="faq-btn" type="button">
          <span>Czy taśmę LED można montować bezpośrednio na płycie meblowej lub gips-kartonie?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Zdecydowanie odradzamy montaż bezpośredni bez profilu aluminiowego. Aluminium działa jak radiator odprowadzający ciepło z diod. Bez chłodzenia diody ulegają szybkiej degradacji termicznej i utracie jasności.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ARCHITECTURAL KALKULATOR NA SAMYM DOLE -->
  <section id="kalkulator-led" class="calc-container">
    <div class="calc-header-wrap">
      <h2>Kalkulator Zasilania &amp; Spadków Napięcia LED</h2>
      <p>Precyzyjny dobór inżynieryjny zasilacza, obliczenie spadku napięcia na przewodzie miedzianym i rekomendacja schematu zasilania.</p>
    </div>

    <div class="calc-grid">
      <!-- FORM COLUMN -->
      <div class="calc-form-col">
        <div class="calc-form-row">
          <div class="calc-group">
            <label for="calc-voltage">Napięcie taśmy LED</label>
            <select id="calc-voltage">
              <option value="24" selected>24V DC (Zalecane profesjonalne)</option>
              <option value="12">12V DC (Standardowe)</option>
              <option value="48">48V DC (Systemy szynowe)</option>
            </select>
          </div>

          <div class="calc-group">
            <label for="calc-power-per-m">Moc taśmy (W/m)</label>
            <select id="calc-power-per-m">
              <option value="4.8">4.8 W/m — Oświetlenie akcentowe</option>
              <option value="9.6">9.6 W/m — Dekoracyjne / wnęki</option>
              <option value="14.4" selected>14.4 W/m — Główne liniowe / COB</option>
              <option value="19.2">19.2 W/m — Mocne robocze / blaty</option>
              <option value="24">24.0 W/m — Super jasne / architektura</option>
            </select>
          </div>
        </div>

        <div class="calc-form-row">
          <div class="calc-group">
            <label for="calc-length">Długość odcinka LED (m)</label>
            <input type="number" id="calc-length" value="6" min="0.5" max="100" step="0.5">
          </div>

          <div class="calc-group">
            <label for="calc-cable-len">Długość przewodu zasilającego (m)</label>
            <input type="number" id="calc-cable-len" value="3" min="0.5" max="50" step="0.5">
          </div>
        </div>

        <div class="calc-group">
          <label for="calc-wire-cross">Przekrój żyły przewodu (mm²)</label>
          <select id="calc-wire-cross">
            <option value="0.5">0.50 mm² (Cienki instalacyjny)</option>
            <option value="0.75" selected>0.75 mm² (Zalecany standard)</option>
            <option value="1.0">1.00 mm² (Zwiększony)</option>
            <option value="1.5">1.50 mm² (Mocne linie / długie dystanse)</option>
            <option value="2.5">2.50 mm² (Magistralny)</option>
          </select>
        </div>
      </div>

      <!-- RESULTS COLUMN -->
      <div class="calc-results-col">
        <div>
          <div class="calc-res-title">Specyfikacja techniczna obliczeń</div>

          <div class="calc-res-row">
            <span class="calc-res-lbl">Moc znamionowa LED:</span>
            <span class="calc-res-num" id="res-nominal-power">86.4 W</span>
          </div>

          <div class="calc-res-row">
            <span class="calc-res-lbl">Zalecana moc zasilacza (+20%):</span>
            <span class="calc-res-num highlight" id="res-power-supply">104 W</span>
          </div>

          <div class="calc-res-row">
            <span class="calc-res-lbl">Prąd roboczy obwodu (I):</span>
            <span class="calc-res-num" id="res-current">3.60 A</span>
          </div>

          <div class="calc-res-row">
            <span class="calc-res-lbl">Szacowany spadek na kablu:</span>
            <span class="calc-res-num" id="res-drop">0.34 V (1.4%)</span>
          </div>
        </div>

        <div class="calc-rec-box" id="res-advice">
          <strong>Rekomendacja Prescot:</strong> Rekomendowany zasilacz <strong>Prescot Ultra Slim 150W 24V</strong>. Zasilanie jednostronne jest w pełni bezpieczne.
        </div>
      </div>
    </div>
  </section>
</main>

<script>
// FAQ Accordion & Search
document.querySelectorAll('.faq-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    var card = btn.closest('.faq-card');
    card.classList.toggle('open');
  });
});

var searchInput = document.getElementById('faqSearchInput');
var faqCards = document.querySelectorAll('.faq-card');
var filterBtns = document.querySelectorAll('.chip-btn');

function filterFAQ() {
  var query = searchInput.value.toLowerCase().trim();
  var activeChip = document.querySelector('.chip-btn.active').dataset.filter;

  faqCards.forEach(function(card) {
    var text = card.textContent.toLowerCase();
    var cat = card.dataset.cat;
    var matchesQuery = query === '' || text.includes(query);
    var matchesCat = activeChip === 'all' || cat === activeChip;

    if (matchesQuery && matchesCat) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

searchInput.addEventListener('input', filterFAQ);

filterBtns.forEach(function(btn) {
  btn.addEventListener('click', function() {
    filterBtns.forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    filterFAQ();
  });
});

// LED Engineering Calculator
function runLedCalc() {
  var voltage = parseFloat(document.getElementById('calc-voltage').value) || 24;
  var powerPerM = parseFloat(document.getElementById('calc-power-per-m').value) || 14.4;
  var length = parseFloat(document.getElementById('calc-length').value) || 5;
  var cableLen = parseFloat(document.getElementById('calc-cable-len').value) || 2;
  var wireCross = parseFloat(document.getElementById('calc-wire-cross').value) || 0.75;

  var nominalPower = powerPerM * length;
  var recommendedPsu = nominalPower * 1.20;
  var current = nominalPower / voltage;

  var wireResistance = (0.0175 * cableLen * 2) / wireCross;
  var voltageDrop = current * wireResistance;
  var dropPercent = (voltageDrop / voltage) * 100;

  document.getElementById('res-nominal-power').textContent = nominalPower.toFixed(1) + ' W';
  document.getElementById('res-power-supply').textContent = Math.ceil(recommendedPsu) + ' W';
  document.getElementById('res-current').textContent = current.toFixed(2) + ' A';
  document.getElementById('res-drop').textContent = voltageDrop.toFixed(2) + ' V (' + dropPercent.toFixed(1) + '%)';

  var psuSize = 60;
  if (recommendedPsu > 60 && recommendedPsu <= 100) psuSize = 100;
  else if (recommendedPsu > 100 && recommendedPsu <= 150) psuSize = 150;
  else if (recommendedPsu > 150 && recommendedPsu <= 200) psuSize = 200;
  else if (recommendedPsu > 200 && recommendedPsu <= 300) psuSize = 300;
  else if (recommendedPsu > 300) psuSize = Math.ceil(recommendedPsu / 50) * 50;

  var connAdvice = 'Zasilanie jednostronne jest w pełni bezpieczne.';
  if (voltage === 12 && length > 5) {
    connAdvice = '<span style="color:#ff8a65; font-weight:700;">Uwaga 12V:</span> Zalecane zasilanie dwustronne (lub magistrala), aby uniknąć spadków jasności.';
  } else if (voltage === 24 && length > 10) {
    connAdvice = '<span style="color:#ff8a65; font-weight:700;">Długi odcinek 24V:</span> Zastosuj zasilanie obustronne.';
  }

  document.getElementById('res-advice').innerHTML = '<strong>Rekomendacja Prescot:</strong> Rekomendowany zasilacz <strong>Prescot Ultra Slim ' + psuSize + 'W ' + voltage + 'V</strong>. ' + connAdvice;
}

['calc-voltage', 'calc-power-per-m', 'calc-length', 'calc-cable-len', 'calc-wire-cross'].forEach(function(id) {
  document.getElementById(id).addEventListener('input', runLedCalc);
  document.getElementById(id).addEventListener('change', runLedCalc);
});
runLedCalc();
</script>
"""

with open(baza_fpath, "w", encoding="utf-8") as f:
    f.write(baza_content + footer_html + """
<!-- GLOBAL MENU START -->
<nav class="prescot-dock" aria-label="Nawigacja główna">
  <a href="/prescotled/" class="dock-item" data-tooltip="Prescot LED" aria-label="Prescot LED">
    <svg class="dock-logo-icon" viewBox="0 0 378 258" xmlns="http://www.w3.org/2000/svg">
      <path fill="#e14e26" d="M0,0h106.7v50H0V0ZM0,100.9h97.7v48.2H0v-48.2ZM0,206.6h106.7v51.2H0v-51.2h0ZM149.3,100.7h82v48.4h-82v-48.4h0ZM149.3,0h87.4C317.7,0,377.9,42.6,377.9,128.9s-60.1,128.9-141.2,128.9h-87.4v-51.2h90.8c47.8,0,76.6-29.1,76.6-77.7s-27.6-78.8-76.6-78.8h-90.8V0h0Z"/>
    </svg>
  </a>
  <a href="/produkty/" class="dock-item" data-tooltip="Oferta" aria-label="Oferta">
    <svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M542.22 32.05c-54.8 3.11-163.72 14.43-230.96 55.59-4.64 2.84-7.27 7.89-7.27 13.17v363.87c0 11.55 12.63 18.85 23.28 13.49 69.18-34.82 169.23-44.32 218.7-46.92 16.89-.89 30.02-14.43 30.02-30.66V62.75c.01-17.71-15.35-31.74-33.77-30.7zM264.73 87.64C197.5 46.48 88.58 35.17 33.78 32.05 15.36 31.01 0 45.04 0 62.75V400.6c0 16.24 13.13 29.78 30.02 30.66 49.49 2.6 149.59 12.11 218.77 46.95 10.62 5.35 23.21-1.94 23.21-13.46V100.63c0-5.29-2.62-10.14-7.27-12.99z"/></svg>
  </a>
  <a href="/tasmy-led/" class="dock-item" data-tooltip="Taśmy LED" aria-label="Taśmy LED">
    <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M224 192c-35.3 0-64 28.7-64 64s28.7 64 64 64 64-28.7 64-64-28.7-64-64-64zm400 224H380.6c41.5-40.7 67.4-97.3 67.4-160 0-123.7-100.3-224-224-224S0 132.3 0 256s100.3 224 224 224h400c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zm-400-64c-53 0-96-43-96-96s43-96 96-96 96 43 96 96-43 96-96 96z"/></svg>
  </a>
  <a href="/produkcja/" class="dock-item" data-tooltip="Produkcja" aria-label="Produkcja">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M475.115 163.781L336 252.309v-68.28c0-18.916-20.931-30.399-36.885-20.248L160 252.309V56c0-13.255-10.745-24-24-24H24C10.745 32 0 42.745 0 56v400c0 13.255 10.745 24 24 24h464c13.255 0 24-10.745 24-24V184.029c0-18.917-20.931-30.399-36.885-20.248z"/></svg>
  </a>
  <a href="/wspolpraca-b2b/" class="dock-item" data-tooltip="Strefa B2B" aria-label="Strefa B2B">
    <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128 352H32c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32zm-24-80h192v48h48v-48h192v48h48v-57.59c0-21.17-17.23-38.41-38.41-38.41H344v-64h40c17.67 0 32-14.33 32-32V32c0-17.67-14.33-32-32-32H256c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h40v64H94.41C73.23 224 56 241.23 56 262.41V320h48v-48zm264 80h-96c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32zm240 0h-96c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32z"/></svg>
  </a>
  <a href="/baza-wiedzy/" class="dock-item" data-tooltip="Baza Wiedzy" aria-label="Baza Wiedzy & FAQ">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M256 32C132.3 32 32 132.3 32 256s100.3 224 224 224 224-100.3 224-224S379.7 32 256 32zm0 376c-17.7 0-32-14.3-32-32s14.3-32 32-32 32 14.3 32 32-14.3 32-32 32zm42.7-142.1c-13.8 11.2-26.7 21.6-26.7 46.1v10c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-14c0-38.4 22.8-56.9 44.4-74.4 14.1-11.4 27.6-22.3 27.6-39.6 0-21.2-18.7-36-44-36-24.6 0-41.9 14.2-46.7 32.5-2.2 8.5-10.4 13.9-19.1 12.3l-30.8-5.6c-9.1-1.7-14.8-10.7-12.4-19.7C180.7 132.2 214.2 104 256 104c53 0 96 34.3 96 82 0 35.8-21.7 61.2-53.3 83.9z"/></svg>
  </a>
  <a href="https://prescot.com.pl/" class="dock-item" data-tooltip="Sklep B2C" aria-label="Sklep B2C" target="_blank" rel="noopener">
    <svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M576 216v16c0 13.255-10.745 24-24 24h-8l-26.113 182.788C514.509 462.435 494.257 480 470.37 480H105.63c-23.887 0-44.139-17.565-47.518-41.212L32 256h-8c-13.255 0-24-10.745-24-24v-16c0-13.255 10.745-24 24-24h67.341l106.78-146.821c10.395-14.292 30.407-17.453 44.701-7.058 14.293 10.395 17.453 30.408 7.058 44.701L170.477 192h235.046L326.12 82.821c-10.395-14.292-7.234-34.306 7.059-44.701 14.291-10.395 34.306-7.235 44.701 7.058L484.659 192H552c13.255 0 24 10.745 24 24zM312 392V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm112 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm-224 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24z"/></svg>
  </a>
  <a href="/kontakt/" class="dock-item" data-tooltip="Kontakt" aria-label="Kontakt">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M493.4 24.6l-104-24c-11.3-2.6-22.9 3.3-27.5 14l-48 112c-4.2 9.8-1.4 21.3 6.9 28l60.6 49.6c-36 76.7-98.9 140.5-177.2 177.2l-49.6-60.6c-6.8-8.3-18.2-11.1-28-6.9l-112 48C4.1 366.5-1.8 378.1.8 389.4l24 104C27.3 504.2 36.7 512 48 512c256.1 0 464-207.5 464-464 0-11.2-7.7-21-18.6-23.4z"/></svg>
  </a>
  <div class="dock-lang-item">
    <div class="gtranslate_wrapper" id="gt-wrapper-85632840"></div>
  </div>
</nav>
<script>
window.gtranslateSettings = window.gtranslateSettings || {};
window.gtranslateSettings['85632840'] = {"default_language":"pl","languages":["ar","zh-CN","cs","da","en","et","fi","fr","de","it","lt","pl","es","sv"],"url_structure":"none","flag_style":"3d","wrapper_selector":"#gt-wrapper-85632840","alt_flags":[],"float_switcher_open_direction":"top","switcher_horizontal_position":"inline","flags_location":"/wp-content/plugins/gtranslate/flags/"};
</script>
<script src="/wp-content/plugins/gtranslate/js/float.js?ver=3.1.1" data-no-optimize="1" data-no-minify="1" data-gt-widget-id="85632840" defer></script>
<script src="/local-navigation.js?v=20260901-white-dock" defer></script>
</body>
</html>
""")

print("Updated baza-wiedzy with architectural dark carbon LED calculator & dark footer logo.")

# 3. Update all other subpages footers with dark logo
for page in ["wspolpraca-b2b/index.html", "dystrybucja/index.html", "kontakt/index.html", "index.html", "prescotled/index.html"]:
    p = os.path.join(base_dir, page)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        # Replace footer logo
        c = re.sub(r'<div class="footerLogo">\s*<img[^>]*>', f'<div class="footerLogo">\n            <img src="{DARK_LOGO}" alt="Prescot LED Logo">', c)
        c = re.sub(r'src="[^"]*biale-z-kolorem\.svg"(?=[^<]*alt="Prescot LED Logo")', f'src="{DARK_LOGO}"', c)
        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated footer in {page} with dark logo.")

