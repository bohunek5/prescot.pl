# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
DARK_LOGO = "/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"

# Read existing footer
footer_path = "/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html"
with open(footer_path, "r", encoding="utf-8") as f:
    footer_html = f.read()

# Apple-Grade Prescot Engineering Calculator CSS & HTML
apple_calc_css = """
  /* =========================================================
     APPLE-GRADE ARCHITECTURAL CONFIGURATOR & CALCULATOR
     ========================================================= */
  .apple-calc-wrapper {
    width: 100%;
    max-width: 1240px;
    margin: 0 auto 90px auto;
    background: #ffffff;
    border: 1px solid rgba(15, 23, 42, 0.08);
    border-radius: 28px;
    box-shadow: 0 20px 50px -12px rgba(15, 23, 42, 0.06), 0 1px 3px rgba(0,0,0,0.02);
    overflow: hidden;
    color: #1e293b;
  }

  .apple-calc-hero {
    padding: 48px 48px 36px 48px;
    border-bottom: 1px solid #f1f5f9;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 30px;
    background: linear-gradient(180deg, #ffffff 0%, #fafbfc 100%);
  }
  @media (max-width: 800px) {
    .apple-calc-hero { padding: 32px 24px; flex-direction: column; }
  }

  .apple-calc-title-box h2 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(26px, 3vw, 34px);
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.02em;
    line-height: 1.2;
    margin-bottom: 8px;
  }
  .apple-calc-title-box p {
    color: #64748b;
    font-size: 15px;
    max-width: 680px;
    line-height: 1.6;
  }

  .apple-calc-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border-radius: 999px;
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    color: #334155;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    white-space: nowrap;
  }
  .apple-calc-badge svg { color: #e55933; }

  .apple-calc-body {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    min-height: 520px;
  }
  @media (max-width: 960px) {
    .apple-calc-body { grid-template-columns: 1fr; }
  }

  /* LEFT CONFIGURATION PANEL */
  .apple-calc-config {
    padding: 44px 48px;
    display: flex;
    flex-direction: column;
    gap: 32px;
    background: #ffffff;
  }
  @media (max-width: 800px) {
    .apple-calc-config { padding: 32px 24px; }
  }

  .calc-field-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .calc-field-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
  .calc-field-label {
    font-size: 13.5px;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: 0.01em;
  }
  .calc-field-val-display {
    font-family: 'Outfit', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #e55933;
  }

  /* Segmented Controls (Apple style) */
  .apple-segmented {
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: 1fr;
    gap: 6px;
    background: #f1f5f9;
    padding: 4px;
    border-radius: 12px;
  }
  .apple-seg-btn {
    border: none;
    background: transparent;
    padding: 10px 14px;
    border-radius: 9px;
    font-family: inherit;
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .apple-seg-btn span.sub {
    font-size: 10.5px;
    opacity: 0.75;
    font-weight: 500;
    margin-top: 2px;
  }
  .apple-seg-btn.active {
    background: #ffffff;
    color: #0f172a;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  }
  .apple-seg-btn:hover:not(.active) {
    color: #0f172a;
    background: rgba(255,255,255,0.5);
  }

  /* Slider & Stepper Row */
  .apple-slider-wrap {
    display: flex;
    align-items: center;
    gap: 18px;
  }
  .apple-range-slider {
    flex: 1;
    -webkit-appearance: none;
    height: 6px;
    border-radius: 4px;
    background: #e2e8f0;
    outline: none;
    transition: background 0.2s;
  }
  .apple-range-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #ffffff;
    border: 2px solid #e55933;
    box-shadow: 0 2px 8px rgba(229, 89, 51, 0.3);
    cursor: pointer;
    transition: transform 0.15s ease;
  }
  .apple-range-slider::-webkit-slider-thumb:hover {
    transform: scale(1.15);
  }
  .apple-num-input {
    width: 82px;
    padding: 8px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    font-family: 'Outfit', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #0f172a;
    text-align: center;
    outline: none;
    background: #f8fafc;
    transition: all 0.2s;
  }
  .apple-num-input:focus {
    border-color: #e55933;
    background: #ffffff;
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.12);
  }

  /* Chip grid for powers and wires */
  .apple-chip-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 8px;
  }
  .apple-chip-btn {
    border: 1px solid #e2e8f0;
    background: #ffffff;
    padding: 10px 12px;
    border-radius: 10px;
    font-family: inherit;
    font-size: 12.5px;
    font-weight: 600;
    color: #334155;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .apple-chip-btn span.tag {
    font-size: 10px;
    color: #64748b;
    margin-top: 2px;
  }
  .apple-chip-btn.active {
    border-color: #e55933;
    background: rgba(229, 89, 51, 0.05);
    color: #e55933;
    box-shadow: 0 0 0 1px #e55933;
  }
  .apple-chip-btn.active span.tag { color: #c94622; }
  .apple-chip-btn:hover:not(.active) {
    border-color: #cbd5e1;
    background: #f8fafc;
  }

  /* RIGHT SPEC & TELEMETRY READOUT */
  .apple-calc-results {
    background: #fafbfc;
    border-left: 1px solid #f1f5f9;
    padding: 44px 44px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 28px;
  }
  @media (max-width: 960px) {
    .apple-calc-results { border-left: none; border-top: 1px solid #f1f5f9; padding: 36px 24px; }
  }

  .calc-metrics-header {
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #64748b;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .calc-metrics-header::before {
    content: '';
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #e55933;
  }

  .calc-metric-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 24px;
  }
  .metric-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 16px 18px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  }
  .metric-card.hero-metric {
    grid-column: 1 / -1;
    background: linear-gradient(135deg, #ffffff 0%, #fffbf9 100%);
    border-color: rgba(229, 89, 51, 0.35);
    box-shadow: 0 4px 14px rgba(229, 89, 51, 0.08);
  }
  .metric-label {
    font-size: 12px;
    color: #64748b;
    margin-bottom: 4px;
    display: block;
  }
  .metric-val {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.1;
  }
  .metric-card.hero-metric .metric-val {
    font-size: 32px;
    color: #e55933;
  }

  /* Live Power Load Bar */
  .calc-load-bar-wrap {
    margin-bottom: 24px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 18px;
  }
  .calc-load-info {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 8px;
    color: #334155;
  }
  .calc-progress-track {
    width: 100%;
    height: 8px;
    background: #f1f5f9;
    border-radius: 999px;
    overflow: hidden;
  }
  .calc-progress-fill {
    height: 100%;
    width: 80%;
    background: linear-gradient(90deg, #10b981 0%, #e55933 100%);
    border-radius: 999px;
    transition: width 0.3s ease;
  }

  /* Recommendation Card */
  .calc-rec-card {
    background: #0f172a;
    border-radius: 18px;
    padding: 24px;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .calc-rec-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #ff8a65;
  }
  .calc-rec-title {
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.3;
  }
  .calc-rec-desc {
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.55;
  }
  .calc-rec-btn {
    align-self: flex-start;
    margin-top: 4px;
  }
"""

# New Complete Baza Wiedzy Page HTML
baza_content = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/wp-content/uploads/2025/09/cropped-favicon-1-32x32.png" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Krona+One&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/prescot-global.css?v=20260901-apple-calc">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <title>Baza Wiedzy & Kalkulator Doboru LED — Prescot LED</title>
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

  /* FAQ STYLING */
  .faq-search-wrap {
    margin-bottom: 28px;
    position: relative;
    max-width: 760px;
    margin-left: auto;
    margin-right: auto;
  }
  .faq-search-input {
    width: 100%;
    padding: 16px 20px 16px 52px;
    font-size: 15px;
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 14px;
    outline: none;
    color: #0f172a;
    font-family: inherit;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    transition: all 0.2s ease;
  }
  .faq-search-input:focus {
    border-color: var(--p-primary);
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.12);
  }
  .faq-search-icon {
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: #64748b;
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
    border-radius: 999px;
    font-size: 13.5px;
    font-weight: 600;
    background: #ffffff;
    border: 1px solid var(--p-border);
    color: #334155;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
  }
  .chip-btn.active, .chip-btn:hover {
    background: #0f172a;
    color: #ffffff;
    border-color: #0f172a;
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
    border-radius: 14px;
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
    color: #0f172a;
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
    color: #64748b;
    transition: transform 0.25s ease, background 0.2s;
  }
  .faq-card.open .faq-btn-icon {
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    transform: rotate(180deg);
  }
  .faq-card.open .faq-btn { color: var(--p-primary); }
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

  """ + apple_calc_css + """
  </style>
</head>
<body>
<!-- SMART LOGO: WIDOCZNE WYŁĄCZNIE W HERO (ZNIKA PO ZJECHANIU DO BIAŁEJ TREŚCI) -->
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

  <!-- APPLE-GRADE ARCHITECTURAL CONFIGURATOR & CALCULATOR -->
  <section id="kalkulator-led" class="apple-calc-wrapper">
    <div class="apple-calc-hero">
      <div class="apple-calc-title-box">
        <h2>Kalkulator Doboru Zasilania & Spadków LED</h2>
        <p>Interaktywne narzędzie inżynieryjne Prescot. Dostosuj parametry instalacji, aby w czasie rzeczywistym otrzymać precyzyjny dobór mocy zasilacza, obliczenie strat na przewodzie i rekomendowany schemat połączeń.</p>
      </div>
      <div class="apple-calc-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        Prescot Engine 2026
      </div>
    </div>

    <div class="apple-calc-body">
      <!-- CONFIGURATION PANEL -->
      <div class="apple-calc-config">
        <!-- 1. Voltage -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Napięcie robocze instalacji</span>
            <span class="calc-field-val-display" id="disp-voltage">24V DC</span>
          </div>
          <div class="apple-segmented" id="seg-voltage">
            <button type="button" class="apple-seg-btn" data-val="12">
              12V DC
              <span class="sub">Krótkie linie</span>
            </button>
            <button type="button" class="apple-seg-btn active" data-val="24">
              24V DC
              <span class="sub">Standard Pro</span>
            </button>
            <button type="button" class="apple-seg-btn" data-val="48">
              48V DC
              <span class="sub">Szynoprzewody</span>
            </button>
          </div>
        </div>

        <!-- 2. Power per meter -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Moc znamionowa taśmy LED</span>
            <span class="calc-field-val-display" id="disp-power">14.4 W/m</span>
          </div>
          <div class="apple-chip-grid" id="grid-power">
            <button type="button" class="apple-chip-btn" data-val="4.8">
              4.8 W/m
              <span class="tag">Akcent / Cokół</span>
            </button>
            <button type="button" class="apple-chip-btn" data-val="9.6">
              9.6 W/m
              <span class="tag">Wnęki sufitowe</span>
            </button>
            <button type="button" class="apple-chip-btn active" data-val="14.4">
              14.4 W/m
              <span class="tag">Liniowe COB ★</span>
            </button>
            <button type="button" class="apple-chip-btn" data-val="19.2">
              19.2 W/m
              <span class="tag">Blaty robocze</span>
            </button>
            <button type="button" class="apple-chip-btn" data-val="24.0">
              24.0 W/m
              <span class="tag">Główne / Wysokie</span>
            </button>
          </div>
        </div>

        <!-- 3. LED Length -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Długość odcinka taśmy LED</span>
            <span class="calc-field-val-display" id="disp-length">6.0 m</span>
          </div>
          <div class="apple-slider-wrap">
            <input type="range" class="apple-range-slider" id="slider-length" min="0.5" max="50" step="0.5" value="6.0">
            <input type="number" class="apple-num-input" id="num-length" min="0.5" max="100" step="0.5" value="6.0">
          </div>
        </div>

        <!-- 4. Cable Distance -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Długość przewodu (zasilacz &rarr; taśma)</span>
            <span class="calc-field-val-display" id="disp-cable">3.0 m</span>
          </div>
          <div class="apple-slider-wrap">
            <input type="range" class="apple-range-slider" id="slider-cable" min="0.5" max="30" step="0.5" value="3.0">
            <input type="number" class="apple-num-input" id="num-cable" min="0.5" max="50" step="0.5" value="3.0">
          </div>
        </div>

        <!-- 5. Wire Cross-section -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Przekrój żyły przewodu zasilającego</span>
            <span class="calc-field-val-display" id="disp-wire">0.75 mm²</span>
          </div>
          <div class="apple-chip-grid" id="grid-wire">
            <button type="button" class="apple-chip-btn" data-val="0.5">
              0.50 mm²
              <span class="tag">Cienki</span>
            </button>
            <button type="button" class="apple-chip-btn active" data-val="0.75">
              0.75 mm²
              <span class="tag">Zalecany standard</span>
            </button>
            <button type="button" class="apple-chip-btn" data-val="1.0">
              1.00 mm²
              <span class="tag">Zwiększony</span>
            </button>
            <button type="button" class="apple-chip-btn" data-val="1.5">
              1.50 mm²
              <span class="tag">Długie dystanse</span>
            </button>
            <button type="button" class="apple-chip-btn" data-val="2.5">
              2.50 mm²
              <span class="tag">Magistrala</span>
            </button>
          </div>
        </div>
      </div>

      <!-- RESULTS & TELEMETRY PANEL -->
      <div class="apple-calc-results">
        <div>
          <div class="calc-metrics-header">Wyniki Obliczeń &amp; Analiza Obciążenia</div>

          <div class="calc-metric-cards">
            <!-- Hero Metric: Recommended PSU -->
            <div class="metric-card hero-metric">
              <span class="metric-label">Zalecana moc zasilacza (+20% zapasu bezpieczeństwa):</span>
              <div class="metric-val" id="res-psu-val">104 W</div>
            </div>

            <!-- Metric 1: Nominal LED power -->
            <div class="metric-card">
              <span class="metric-label">Moc znamionowa LED:</span>
              <div class="metric-val" id="res-power-val">86.4 W</div>
            </div>

            <!-- Metric 2: Circuit Current -->
            <div class="metric-card">
              <span class="metric-label">Prąd roboczy obwodu:</span>
              <div class="metric-val" id="res-current-val">3.60 A</div>
            </div>

            <!-- Metric 3: Voltage Drop -->
            <div class="metric-card">
              <span class="metric-label">Spadek na przewodzie:</span>
              <div class="metric-val" id="res-drop-val">0.34 V</div>
            </div>

            <!-- Metric 4: Loss percent -->
            <div class="metric-card">
              <span class="metric-label">Względna strata napięcia:</span>
              <div class="metric-val" id="res-loss-val">1.4%</div>
            </div>
          </div>

          <!-- Live Power Load Bar -->
          <div class="calc-load-bar-wrap">
            <div class="calc-load-info">
              <span>Współczynnik obciążenia zasilacza</span>
              <span id="res-load-pct" style="color:#0f172a; font-weight:700;">83% (Optymalny punkt)</span>
            </div>
            <div class="calc-progress-track">
              <div class="calc-progress-fill" id="res-load-bar"></div>
            </div>
          </div>
        </div>

        <!-- Recommendation Box -->
        <div class="calc-rec-card">
          <div class="calc-rec-tag">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            Rekomendacja Inżynieryjna Prescot
          </div>
          <div class="calc-rec-title" id="rec-psu-name">Prescot Ultra Slim 150W 24V IP20</div>
          <p class="calc-rec-desc" id="rec-psu-text">Aluminiowa obudowa slim, sprawność 93%, wbudowane filtry PFC oraz zabezpieczenia przeciążeniowe i termiczne. Zasilanie jednostronne odcinka 6m jest w 100% bezpieczne.</p>
          <a href="/produkty/" class="p-btn p-btn-primary calc-rec-btn">
            Zobacz zasilacze w ofercie &rarr;
          </a>
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

// APPLE-GRADE PRESCOT LED CALCULATOR CONTROLLER
var state = {
  voltage: 24,
  powerPerM: 14.4,
  length: 6.0,
  cable: 3.0,
  wire: 0.75
};

function updateCalculator() {
  var nominalPower = state.powerPerM * state.length;
  var recommendedPsu = nominalPower * 1.20;
  var current = nominalPower / state.voltage;

  // Resistance of copper (0.0175 ohm*mm2/m) for 2 conductors (+ and -)
  var wireResistance = (0.0175 * state.cable * 2) / state.wire;
  var voltageDrop = current * wireResistance;
  var lossPct = (voltageDrop / state.voltage) * 100;

  // Standard Prescot PSU Steps: 35W, 60W, 100W, 150W, 200W, 250W, 300W, 400W, 600W
  var psuOptions = [35, 60, 100, 150, 200, 250, 300, 400, 600];
  var matchedPsu = 600;
  for (var i = 0; i < psuOptions.length; i++) {
    if (psuOptions[i] >= recommendedPsu) {
      matchedPsu = psuOptions[i];
      break;
    }
  }

  var loadPct = Math.round((nominalPower / matchedPsu) * 100);

  // Update UI values
  document.getElementById('disp-voltage').textContent = state.voltage + 'V DC';
  document.getElementById('disp-power').textContent = state.powerPerM + ' W/m';
  document.getElementById('disp-length').textContent = state.length.toFixed(1) + ' m';
  document.getElementById('disp-cable').textContent = state.cable.toFixed(1) + ' m';
  document.getElementById('disp-wire').textContent = state.wire.toFixed(2) + ' mm²';

  document.getElementById('res-psu-val').textContent = Math.ceil(recommendedPsu) + ' W';
  document.getElementById('res-power-val').textContent = nominalPower.toFixed(1) + ' W';
  document.getElementById('res-current-val').textContent = current.toFixed(2) + ' A';
  document.getElementById('res-drop-val').textContent = voltageDrop.toFixed(2) + ' V';
  document.getElementById('res-loss-val').textContent = lossPct.toFixed(1) + '%';

  // Load bar
  document.getElementById('res-load-pct').textContent = loadPct + '% obciążenia (' + matchedPsu + 'W)';
  document.getElementById('res-load-bar').style.width = Math.min(100, loadPct) + '%';
  if (loadPct > 90) {
    document.getElementById('res-load-bar').style.background = '#ef4444';
  } else if (loadPct > 80) {
    document.getElementById('res-load-bar').style.background = '#e55933';
  } else {
    document.getElementById('res-load-bar').style.background = '#10b981';
  }

  // Recommendation text
  var modelName = 'Prescot Ultra Slim ' + matchedPsu + 'W ' + state.voltage + 'V IP20';
  document.getElementById('rec-psu-name').textContent = modelName;

  var advice = 'Aluminiowa obudowa slim, sprawność 93%, wbudowane filtry PFC oraz zabezpieczenia przeciążeniowe i termiczne. ';
  if (state.voltage === 12 && state.length > 5) {
    advice += 'Dla instalacji 12V przy długości powyżej 5m rekomendujemy zasilenie obustronne.';
  } else if (lossPct > 3.0) {
    advice += 'Uwaga na spadek napięcia (' + lossPct.toFixed(1) + '%). Zalecamy zwiększenie przekroju żyły do 1.50 mm² lub skrócenie przewodu.';
  } else {
    advice += 'Zasilanie jednostronne odcinka ' + state.length.toFixed(1) + 'm jest w 100% bezpieczne.';
  }
  document.getElementById('rec-psu-text').textContent = advice;
}

// 1. Voltage Segments
document.querySelectorAll('#seg-voltage .apple-seg-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('#seg-voltage .apple-seg-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    state.voltage = parseFloat(btn.dataset.val);
    updateCalculator();
  });
});

// 2. Power Chips
document.querySelectorAll('#grid-power .apple-chip-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('#grid-power .apple-chip-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    state.powerPerM = parseFloat(btn.dataset.val);
    updateCalculator();
  });
});

// 3. LED Length (Slider & Input sync)
var sLen = document.getElementById('slider-length');
var nLen = document.getElementById('num-length');
sLen.addEventListener('input', function() {
  nLen.value = sLen.value;
  state.length = parseFloat(sLen.value);
  updateCalculator();
});
nLen.addEventListener('input', function() {
  sLen.value = nLen.value;
  state.length = parseFloat(nLen.value) || 1;
  updateCalculator();
});

// 4. Cable Distance (Slider & Input sync)
var sCab = document.getElementById('slider-cable');
var nCab = document.getElementById('num-cable');
sCab.addEventListener('input', function() {
  nCab.value = sCab.value;
  state.cable = parseFloat(sCab.value);
  updateCalculator();
});
nCab.addEventListener('input', function() {
  sCab.value = nCab.value;
  state.cable = parseFloat(nCab.value) || 1;
  updateCalculator();
});

// 5. Wire Cross Chips
document.querySelectorAll('#grid-wire .apple-chip-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('#grid-wire .apple-chip-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    state.wire = parseFloat(btn.dataset.val);
    updateCalculator();
  });
});

updateCalculator();
</script>
"""

# Write to file
baza_fpath = os.path.join(base_dir, "baza-wiedzy/index.html")
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
<script src="/local-navigation.js?v=20260901-apple-calc" defer></script>
</body>
</html>
""")

print("Successfully generated Apple-Grade Prescot Configurator on Baza Wiedzy.")
