# -*- coding: utf-8 -*-
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# ==============================================================================
# 1. BAZA WIEDZY (baza-wiedzy/index.html)
# ==============================================================================
baza_html = """<!DOCTYPE html>
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
    --p-card-bg: #ffffff;
    --p-border: #e2e8f0;
    --p-radius: 20px;
    --p-radius-sm: 10px;
    --p-shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --p-shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -1px rgba(0,0,0,0.04);
    --p-shadow-lg: 0 10px 25px -3px rgba(0,0,0,0.09), 0 4px 6px -2px rgba(0,0,0,0.04);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--p-text);
    background: var(--p-bg);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding-bottom: 90px;
  }

  /* TOPBAR: SCHODZI I CHOWA SIĘ NA GÓRZE PRZY SCROLLU (POSITION: RELATIVE) */
  .prescot-topbar {
    background: #ffffff;
    border-bottom: 1px solid var(--p-border);
    padding: 16px 24px;
    position: relative; /* Scrolls naturally out of view */
    z-index: 10;
  }
  .prescot-topbar-inner {
    max-width: 1240px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .prescot-logo-link img {
    height: 38px;
    width: auto;
    display: block;
  }
  .prescot-topbar-tagline {
    font-size: 13px;
    color: var(--p-text-muted);
    font-weight: 500;
  }
  @media (max-width: 600px) {
    .prescot-topbar-tagline { display: none; }
  }

  .prescot-main-container {
    max-width: 1240px;
    margin: 0 auto;
    padding: 32px 24px 80px 24px;
  }

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
    opacity: 0.4;
  }

  /* =========================================================
     HERO ZE ZDJĘCIEM W TLE (ARCHITECTURAL LED PHOTO)
     ========================================================= */
  .p-hero {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.82) 0%, rgba(30, 41, 59, 0.88) 100%), 
                url('/wp-content/uploads/2026/03/AdobeStock_1101216226-1536x861.webp') center/cover no-repeat;
    color: #ffffff;
    border-radius: var(--p-radius);
    padding: 60px 48px;
    margin-bottom: 48px;
    box-shadow: var(--p-shadow-lg);
    position: relative;
    overflow: hidden;
  }
  .p-hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(229, 89, 51, 0.25);
    color: #ff8a65;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 6px 14px;
    border-radius: 30px;
    margin-bottom: 18px;
    border: 1px solid rgba(229, 89, 51, 0.4);
    backdrop-filter: blur(4px);
  }
  .p-hero h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(32px, 4vw, 44px);
    color: #ffffff;
    margin-bottom: 16px;
    line-height: 1.2;
    font-weight: 700;
  }
  .p-hero p.lead {
    font-size: clamp(15px, 1.8vw, 17px);
    color: #e2e8f0;
    max-width: 820px;
    line-height: 1.65;
    margin-bottom: 28px;
    text-shadow: 0 1px 2px rgba(0,0,0,0.4);
  }
  .p-hero-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
  }
  .p-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 26px;
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
    background: rgba(255, 255, 255, 0.1);
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(6px);
  }
  .p-btn-outline:hover {
    background: rgba(255, 255, 255, 0.2);
    border-color: #ffffff;
  }

  /* FAQ SECTION */
  .bw-section {
    margin-bottom: 60px;
  }
  .bw-header {
    margin-bottom: 28px;
  }
  .bw-header h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: var(--p-dark);
    margin-bottom: 8px;
  }
  .bw-header p {
    color: var(--p-text-muted);
    font-size: 15px;
  }

  .bw-search-box {
    position: relative;
    margin-bottom: 24px;
  }
  .bw-search-box input {
    width: 100%;
    padding: 16px 20px 16px 52px;
    border-radius: 14px;
    border: 1.5px solid var(--p-border);
    background: #ffffff;
    font-size: 15px;
    font-family: inherit;
    color: var(--p-dark);
    box-shadow: var(--p-shadow-sm);
    outline: none;
    transition: all 0.2s;
  }
  .bw-search-box input:focus {
    border-color: var(--p-primary);
    box-shadow: 0 0 0 4px rgba(229, 89, 51, 0.12);
  }
  .bw-search-icon {
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: #94a3b8;
    pointer-events: none;
  }

  .bw-filters {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 32px;
  }
  .bw-filter-btn {
    padding: 8px 18px;
    border-radius: 30px;
    background: #ffffff;
    border: 1px solid var(--p-border);
    font-size: 13.5px;
    font-weight: 600;
    color: #475569;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
  }
  .bw-filter-btn:hover {
    border-color: var(--p-primary);
    color: var(--p-primary);
  }
  .bw-filter-btn.active {
    background: var(--p-primary);
    border-color: var(--p-primary);
    color: #ffffff;
    box-shadow: 0 3px 10px rgba(229, 89, 51, 0.3);
  }

  .faq-list {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .faq-card {
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.2s ease;
    box-shadow: var(--p-shadow-sm);
  }
  .faq-card:hover {
    border-color: #cbd5e1;
    box-shadow: var(--p-shadow-md);
  }
  .faq-card.open {
    border-color: rgba(229, 89, 51, 0.4);
    box-shadow: 0 4px 20px rgba(229, 89, 51, 0.08);
  }
  .faq-btn {
    width: 100%;
    padding: 22px 26px;
    text-align: left;
    background: transparent;
    border: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    cursor: pointer;
    font-weight: 700;
    font-size: 16.5px;
    color: #0f172a;
    font-family: 'Outfit', sans-serif;
  }
  .faq-btn-icon {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #f1f5f9;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: #64748b;
    transition: all 0.25s ease;
  }
  .faq-card.open .faq-btn-icon {
    background: rgba(229, 89, 51, 0.12);
    color: var(--p-primary);
    transform: rotate(180deg);
  }
  .faq-card.open .faq-btn {
    color: var(--p-primary);
  }
  .faq-content {
    display: none;
    padding: 0 26px 24px 26px;
    color: #475569;
    font-size: 15px;
    line-height: 1.7;
    border-top: 1px solid transparent;
  }
  .faq-card.open .faq-content {
    display: block;
    border-top-color: #f1f5f9;
    padding-top: 18px;
  }
  .faq-content p { margin-bottom: 12px; }
  .faq-content p:last-child { margin-bottom: 0; }
  .faq-content ul { padding-left: 20px; margin-bottom: 12px; }
  .faq-content li { margin-bottom: 6px; }

  /* =========================================================
     KALKULATOR INŻYNIERSKI (NA SAMYM DOLE)
     ========================================================= */
  .calc-premium-wrapper {
    background: #ffffff;
    border: 1.5px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 44px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.05);
    margin-top: 60px;
    margin-bottom: 40px;
    position: relative;
  }
  @media (max-width: 768px) {
    .calc-premium-wrapper { padding: 28px 20px; }
  }

  .calc-kicker-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 5px 12px;
    border-radius: 999px;
    margin-bottom: 12px;
  }

  .calc-title-header {
    margin-bottom: 32px;
  }
  .calc-title-header h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: var(--p-dark);
    margin-bottom: 8px;
  }
  .calc-title-header p {
    color: var(--p-text-muted);
    font-size: 15px;
    max-width: 750px;
  }

  .calc-layout-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 36px;
    align-items: stretch;
  }
  @media (max-width: 950px) {
    .calc-layout-grid { grid-template-columns: 1fr; }
  }

  .calc-inputs-panel {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 30px;
    display: flex;
    flex-direction: column;
    gap: 22px;
  }

  .calc-field-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .calc-field-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 13.5px;
    font-weight: 700;
    color: #1e293b;
  }
  .calc-field-value {
    color: var(--p-primary);
    font-weight: 800;
    font-size: 14px;
  }

  .calc-select, .calc-input {
    width: 100%;
    padding: 12px 16px;
    border-radius: 10px;
    border: 1.5px solid #d1d5db;
    background: #ffffff;
    font-family: inherit;
    font-size: 14.5px;
    color: #0f172a;
    outline: none;
    transition: all 0.2s;
  }
  .calc-select:focus, .calc-input:focus {
    border-color: var(--p-primary);
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.15);
  }

  .calc-slider-wrap {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .calc-range {
    flex: 1;
    accent-color: var(--p-primary);
    cursor: pointer;
    height: 6px;
  }

  .calc-results-panel {
    background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%),
                url('/wp-content/uploads/2026/03/AdobeStock_1392520552-1024x574.webp') center/cover no-repeat;
    color: #ffffff;
    border-radius: 18px;
    padding: 32px 28px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: var(--p-shadow-lg);
    position: relative;
    overflow: hidden;
  }

  .calc-res-header {
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    padding-bottom: 14px;
  }

  .calc-cards-stack {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 24px;
  }
  @media (max-width: 480px) {
    .calc-cards-stack { grid-template-columns: 1fr; }
  }

  .calc-stat-box {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;
    padding: 16px;
    backdrop-filter: blur(8px);
  }
  .calc-stat-box.highlight-primary {
    background: rgba(229, 89, 51, 0.25);
    border-color: rgba(229, 89, 51, 0.6);
  }
  .calc-stat-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #cbd5e1;
    font-weight: 700;
    margin-bottom: 6px;
    display: block;
  }
  .calc-stat-box.highlight-primary .calc-stat-label {
    color: #ff8a65;
  }
  .calc-stat-val {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
  }
  .calc-stat-val.orange {
    color: #ff8a65;
  }

  .calc-advice-card {
    background: rgba(15, 23, 42, 0.75);
    border-left: 3px solid var(--p-primary);
    padding: 14px 18px;
    border-radius: 0 10px 10px 0;
    margin-top: auto;
    font-size: 13px;
    color: #e2e8f0;
    line-height: 1.5;
    backdrop-filter: blur(6px);
  }
  .calc-advice-card strong {
    color: #ffffff;
  }
  </style>
</head>
<body>
<!-- TOPBAR: SCHODZI PRZY SCROLLOWANIU -->
<header class="prescot-topbar">
  <div class="prescot-topbar-inner">
    <a href="/" class="prescot-logo-link" title="Prescot LED Strona Główna">
      <img src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg" alt="Prescot LED">
    </a>
    <span class="prescot-topbar-tagline">Polski Producent Oświetlenia LED &bull; Giżycko</span>
  </div>
</header>

<main class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Baza Wiedzy & FAQ</span>
  </nav>

  <!-- 1. HERO SECTION ZE ZDJĘCIEM W TLE -->
  <div class="p-hero">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      Oficjalne Kompendium Inżynieryjne
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

  <!-- 2. FAQ & WIEDZA SECTION (GÓRA I ŚRODEK STRONY) -->
  <section id="faq-section" class="bw-section">
    <div class="bw-header">
      <h2>Najczęściej Zadawane Pytania & Standardy Techniczne</h2>
      <p>Wyszukaj konkretne zagadnienie lub przefiltruj bazę wiedzy według kategorii.</p>
    </div>

    <!-- WYSZUKIWARKA -->
    <div class="bw-search-box">
      <svg class="bw-search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" id="bw-search-input" placeholder="Szukaj w bazie wiedzy (np. spadek napięcia, COB, 24V, ściemnianie, zasilacz)...">
    </div>

    <!-- FILTRY KATEGORII -->
    <div class="bw-filters">
      <button class="bw-filter-btn active" data-filter="all">Wszystkie zagadnienia</button>
      <button class="bw-filter-btn" data-filter="tasmy">Taśmy LED &amp; COB</button>
      <button class="bw-filter-btn" data-filter="zasilanie">Zasilacze &amp; Spadki</button>
      <button class="bw-filter-btn" data-filter="sterowanie">Sterowanie &amp; Smart</button>
      <button class="bw-filter-btn" data-filter="montaz">Montaż &amp; Profile</button>
    </div>

    <!-- LISTA PYTAŃ FAQ (14 PYTAŃ) -->
    <div class="faq-list" id="faq-container">
      
      <div class="faq-card" data-category="tasmy">
        <button class="faq-btn">
          <span>1. Czym różni się taśma COB od tradycyjnej taśmy SMD?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśmy COB (Chip on Board) posiadają setki miniaturowych diod zatopionych bezpośrednio w ciągłej warstwie luminoforu (np. 480–528 chipów/m). Daje to idealnie jednolitą, gładką linię światła bez widocznych punktów diodowych, nawet w bardzo płytkich profilach aluminiowych.</p>
          <p>Tradycyjne taśmy SMD (np. 2835, 5050) posiadają oddzielne punkty świetlne i w płytkich korytkach tworzą efekt "kropek". Ponadto taśmy COB charakteryzują się szerszym kątem rozsyłu światła (180° vs 120° w SMD) i wyższą estetyką wykończenia.</p>
        </div>
      </div>

      <div class="faq-card" data-category="zasilanie">
        <button class="faq-btn">
          <span>2. Dlaczego Prescot LED rekomenduje instalacje 24V DC zamiast 12V DC?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Zgodnie z prawem Ohma i formułą mocy (P = U &times; I), przy dwukrotnie wyższym napięciu (24V zamiast 12V) prąd płynący przez ścieżki taśmy i przewody jest o 50% mniejszy przy zachowaniu tej samej mocy świecenia.</p>
          <ul>
            <li><strong>4-krotnie mniejsze straty cieplne</strong> na przewodach i laminacie PCB (P_straty = I² &times; R).</li>
            <li><strong>Brak spadków jasności</strong> – możliwość zasilania odcinków do 10 m z jednego punktu bez widocznego ściemniania końca taśmy.</li>
            <li><strong>Cieńsze przewody zasilające</strong> – wystarczy przekrój 0.75–1.5 mm² zamiast grubych wiązek magistralnych.</li>
          </ul>
        </div>
      </div>

      <div class="faq-card" data-category="zasilanie">
        <button class="faq-btn">
          <span>3. Jak obliczyć wymaganą moc zasilacza i dlaczego bufor +20% jest obowiązkowy?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Wzór na minimalną moc zasilacza: <strong>P_zasilacza = (Moc taśmy W/m &times; Długość w metrach) &times; 1.20</strong>.</p>
          <p>Bufor bezpieczeństwa 20% gwarantuje, że zasilacz impulsowy nie pracuje na 100% swoich możliwości termicznych. Zapewnia to stabilną temperaturę pracy kondensatorów elektrolitycznych, brak przegrzewania, wyższą sprawność oraz wieloletnią bezawaryjną pracę instalacji.</p>
        </div>
      </div>

      <div class="faq-card" data-category="montaz">
        <button class="faq-btn">
          <span>4. Czy profil aluminiowy jest bezwzględnie wymagany do montażu taśmy LED?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p><strong>Tak, profil aluminiowy jest radiatorem.</strong> Diody LED podczas świecenia emitują ciepło na złączu p-n. Brak odprowadzania ciepła (np. montaż bezpośrednio na płycie meblowej, gips-kartonie lub drewnie) powoduje degradację luminoforu, zmianę barwy światła oraz szybkie wypalenie diod.</p>
          <p>Zastosowanie profilu z kloszem z tworzywa PMMA zabezpiecza także taśmę przed kurzem, parą wodną i uszkodzeniami mechanicznymi podczas sprzątania.</p>
        </div>
      </div>

      <div class="faq-card" data-category="sterowanie">
        <button class="faq-btn">
          <span>5. Jakie protokoły sterowania i ściemniania taśm LED oferuje Prescot?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>W ofercie Prescot LED znajdują się kontrolery i sterowniki dla każdego typu instalacji:</p>
          <ul>
            <li><strong>Sterowanie Radiowe RF 2.4GHz</strong> – piloty wielostrefowe i panele naścienne bez konieczności prowadzenia kabli sterujących.</li>
            <li><strong>Protokół DALI-2 &amp; 0-10V / 1-10V</strong> – profesjonalne systemy automatyki budynkowej (BMS) dla hoteli, biurowców i galerii handlowych.</li>
            <li><strong>Systemy Smart Home (Zigbee 3.0 / Tuya / Matter)</strong> – integracja z aplikacjami mobilnymi oraz asystentami głosowymi Google Home i Apple HomeKit.</li>
            <li><strong>Ściemnianie TRIAC (Phase Cut)</strong> – ściemniacze montowane po stronie 230V do tradycyjnych włączników obrotowych.</li>
          </ul>
        </div>
      </div>

      <div class="faq-card" data-category="tasmy">
        <button class="faq-btn">
          <span>6. Co oznacza współczynnik CRI (Ra) i dlaczego w Prescot stosujemy CRI &ge; 90?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>CRI (Color Rendering Index) określa stopień wierności oddawania barw oświetlanych przedmiotów w porównaniu ze światłem słonecznym (CRI 100). Tanie taśmy marketowe mają CRI ~70-80, co sprawia, że skóra, potrawy, drewno i tkaniny wyglądają na wyblakłe i szare.</p>
          <p>Wszystkie taśmy Prescot LED posiadają certyfikowane <strong>CRI &ge; 90 (z wysokim R9 &gt; 50 dla głębokiej czerwieni)</strong>, co jest kluczowe w architekturze wnętrz, salonach meblowych, gastronomii i rezydencjach premium.</p>
        </div>
      </div>

      <div class="faq-card" data-category="zasilanie">
        <button class="faq-btn">
          <span>7. Jak uniknąć spadków napięcia na długich odcinkach (powyżej 5–10 metrów)?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Przy długich ciągach oświetleniowych opór miedzianej ścieżki PCB taśmy powoduje spadek napięcia pod koniec linii. Aby temu zapobiec:</p>
          <ul>
            <li>Stosuj zasilanie <strong>obustronne</strong> (wpięcie kabla zasilającego z obu końców taśmy).</li>
            <li>Dla odcinków powyżej 10 m poprowadź równoległą magistralę zasilającą (np. przewód 2x1.5mm²) i wprowadzaj zasilanie co 5 metrów (tzw. zasilanie pętlowe).</li>
            <li>Wybieraj taśmy na napięcie 24V lub 48V zamiast 12V.</li>
          </ul>
        </div>
      </div>

      <div class="faq-card" data-category="montaz">
        <button class="faq-btn">
          <span>8. Jak prawidłowo docinać i lutować taśmy Prescot LED?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśmy można ciąć wyłącznie w wyznaczonych miejscach oznaczonych symbolem nożyczek lub polami lutowniczymi (co 2.5 cm, 5 cm lub 10 cm w zależności od modelu). Cięcie w innym miejscu uszkodzi sekcję diod.</p>
          <p>Do łączenia rekomendujemy <strong>lutowanie cyną ołowiową lub bezołowiową ze stopem srebra</strong> (temperatura grota ok. 320–350°C, czas przyłożenia max. 2–3 sekundy, aby nie przegrzać ścieżki). Alternatywnie można użyć dedykowanych złączek zaciskowych Prescot Quick-Connect.</p>
        </div>
      </div>

      <div class="faq-card" data-category="tasmy">
        <button class="faq-btn">
          <span>9. Jaką barwę światła (CCT) wybrać do poszczególnych pomieszczeń?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <ul>
            <li><strong>2700K (Bardzo Ciepła)</strong> – sypialnie, strefy relaksu, klimatyczne restauracje. Wprowadza przytulny, intymny nastrój.</li>
            <li><strong>3000K (Ciepła Biała)</strong> – standard mieszkaniowy: salony, jadalnie, korytarze, drewniane zabudowy meblowe.</li>
            <li><strong>4000K (Neutralna Dzienna)</strong> – kuchnie, łazienki, biura, gabinety, hale ekspozycyjne. Nie przekłamuje kolorów i sprzyja koncentracji.</li>
            <li><strong>CCT Tunable White (2700K–6500K)</strong> – taśmy ze zmienną barwą światła, dopasowujące się do rytmu dobowego człowieka (Human Centric Lighting).</li>
          </ul>
        </div>
      </div>

      <div class="faq-card" data-category="zasilanie">
        <button class="faq-btn">
          <span>10. Czym różnią się zasilacze stałonapięciowe (CV) od stałoprądowych (CC)?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśmy LED elastyczne (COB i SMD) wymagają zasilaczy <strong>stałonapięciowych CV (Constant Voltage – 12V DC, 24V DC lub 48V DC)</strong>, ponieważ na laminacie taśmy wbudowane są już rezystory ograniczające prąd diod.</p>
          <p>Zasilacze stałoprądowe CC (Constant Current – np. 350mA, 700mA) stosuje się do opraw typu downlight, paneli LED i modułów dużej mocy bez wbudowanych rezystorów.</p>
        </div>
      </div>

      <div class="faq-card" data-category="montaz">
        <button class="faq-btn">
          <span>11. Jaki stopień ochrony IP wybrać do łazienki, sauny lub na zewnątrz?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <ul>
            <li><strong>IP20</strong> – wnętrza suche: salony, sypialnie, meble pokojowe (taśma w profilu z kloszem).</li>
            <li><strong>IP65 / IP67 (Silicone Tube / Nano-coating)</strong> – łazienki, strefy pod prysznicem, blaty kuchenne, fasady zewnętrzne, tarasy i podbitki dachowe.</li>
            <li><strong>IP68</strong> – baseny, oczka wodne, strefy pod stałym zanurzeniem w wodzie.</li>
          </ul>
        </div>
      </div>

      <div class="faq-card" data-category="sterowanie">
        <button class="faq-btn">
          <span>12. Co to jest taśma cyfrowa adresowalna (Pixel / SPI)?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>W taśmie cyfrowej (np. układy WS2811, WS2812B, UCS1903) każdy moduł diodowy posiada mikrokontroler. Umożliwia to niezależne sterowanie kolorem i jasnością każdego pojedynczego punktu, tworząc dynamiczne efekty fali, płynącego światła ("running light"), tęczy czy integrację ze schodowymi sterownikami ruchu.</p>
        </div>
      </div>

      <div class="faq-card" data-category="zasilanie">
        <button class="faq-btn">
          <span>13. Czy zasilacz LED może być schowany w puszce lub za płytą G-K?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Tak, pod warunkiem zapewnienia minimalnej cyrkulacji powietrza. Do montażu w puszkach podtynkowych fi 60 stosuje się miniaturowe zasilacze dopuszkowe Prescot IP67.</p>
          <p>W sufitach podwieszanych G-K zasilacz należy umieścić w pobliżu rewizji lub otworu oprawy oświetleniowej, tak aby w razie potrzeby był do niego swobodny dostęp serwisowy.</p>
        </div>
      </div>

      <div class="faq-card" data-category="tasmy">
        <button class="faq-btn">
          <span>14. Jaka jest żywotność taśm Prescot LED i okres gwarancji?</span>
          <span class="faq-btn-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Profesjonalne taśmy Prescot LED na podwójnym podkładzie miedzi (2oz / 3oz PCB) posiadają żywotność L80B10 &gt; 50 000 godzin ciągłego świecenia przy prawidłowym montażu na profilu aluminiowym.</p>
          <p>Wszystkie serie profesjonalne objęte są pełną <strong>3-letnią lub 5-letnią gwarancją producenta</strong> dla firm i klientów indywidualnych.</p>
        </div>
      </div>

    </div>
  </section>

  <!-- 3. STATE-OF-THE-ART KALKULATOR LED (NA SAMYM DOLE STRONY) -->
  <section id="kalkulator-led" class="calc-premium-wrapper">
    <div class="calc-kicker-badge">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="12" y1="11" x2="12" y2="17"/><line x1="9" y1="14" x2="15" y2="14"/></svg>
      Narzędzie Inżynieryjne Prescot LED
    </div>
    
    <div class="calc-title-header">
      <h2>Kalkulator Doboru Zasilacza &amp; Spadków Napięcia</h2>
      <p>Wprowadź parametry instalacji, aby w czasie rzeczywistym wyliczyć minimalną moc zasilacza (z buforem +20%), pobór prądu, spadek napięcia i rekomendowany przekrój przewodu.</p>
    </div>

    <div class="calc-layout-grid">
      <!-- LEWY PANEL: PARAMETRY -->
      <div class="calc-inputs-panel">
        
        <!-- MOC TAŚMY -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span>Moc jednostkowa taśmy LED</span>
            <span class="calc-field-value" id="c-power-display">9.6 W/m</span>
          </div>
          <select class="calc-select" id="c-tape-power">
            <option value="4.8">4.8 W/m — Dekoracyjna Akcentowa SMD (300 LED)</option>
            <option value="9.6" selected>9.6 W/m — Standardowa Użytkowa SMD (600 LED)</option>
            <option value="10.0">10.0 W/m — Prescot COB Slim (Ciągła linia światła)</option>
            <option value="14.4">14.4 W/m — Mocna Użytkowa SMD (60 LED/m 5050)</option>
            <option value="15.0">15.0 W/m — Prescot COB High Lumen CRI>90</option>
            <option value="19.2">19.2 W/m — Super Jasna Główna SMD (120 LED/m 2835)</option>
            <option value="custom">Wpisz własną moc W/m...</option>
          </select>
          <input type="number" class="calc-input" id="c-custom-power" placeholder="Wpisz moc w W/m (np. 12.5)" style="display:none; margin-top:6px;" step="0.1" min="1" max="100">
        </div>

        <!-- DŁUGOŚĆ ODCINKA -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span>Długość montowanego odcinka taśmy</span>
            <span class="calc-field-value" id="c-len-display">5.0 m</span>
          </div>
          <div class="calc-slider-wrap">
            <input type="range" class="calc-range" id="c-tape-len" min="0.5" max="30" step="0.5" value="5">
          </div>
        </div>

        <!-- NAPIĘCIE INSTALACJI -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span>Napięcie robocze instalacji</span>
            <span class="calc-field-value" id="c-volt-display">24V DC</span>
          </div>
          <select class="calc-select" id="c-tape-voltage">
            <option value="12">12V DC (Krótkie odcinki do 5m)</option>
            <option value="24" selected>24V DC (Standard Prescot — rekomendowany)</option>
            <option value="48">48V DC (Długie ciągi magistralne do 25-50m)</option>
          </select>
        </div>

        <!-- PRZEWÓD ZASILAJĄCY -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span>Długość kabla (zasilacz &rarr; taśma)</span>
            <span class="calc-field-value" id="c-wire-display">3 m</span>
          </div>
          <select class="calc-select" id="c-wire-len">
            <option value="1">1 metr (Zasilacz tuż przy taśmie)</option>
            <option value="3" selected>3 metry (Standard w zabudowie)</option>
            <option value="5">5 metrów (Rozdzielnica w szafie)</option>
            <option value="10">10 metrów (Dłuższa trasa kablowa)</option>
            <option value="15">15 metrów</option>
            <option value="25">25 metrów</option>
          </select>
        </div>

        <!-- PRZEKRÓJ ŻYŁY KABLA -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span>Przekrój żyły przewodu (Cu)</span>
            <span class="calc-field-value">Miedź</span>
          </div>
          <select class="calc-select" id="c-wire-section">
            <option value="0.5">0.50 mm² (Bardzo cienki)</option>
            <option value="0.75" selected>0.75 mm² (Standard instalacyjny)</option>
            <option value="1.0">1.00 mm²</option>
            <option value="1.5">1.50 mm² (Rekomendowany)</option>
            <option value="2.5">2.50 mm² (Magistrala)</option>
          </select>
        </div>

      </div>

      <!-- PRAWY PANEL: WYNIKI -->
      <div class="calc-results-panel">
        <div>
          <div class="calc-res-header">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            Obliczone Parametry Instalacji
          </div>

          <div class="calc-cards-stack">
            
            <div class="calc-stat-box">
              <span class="calc-stat-label">Moc Znamionowa LED</span>
              <div class="calc-stat-val" id="res-p-nom">48.0 W</div>
            </div>

            <div class="calc-stat-box highlight-primary">
              <span class="calc-stat-label">Zasilacz z Buforem (+20%)</span>
              <div class="calc-stat-val orange" id="res-p-psu">min. 60 W</div>
            </div>

            <div class="calc-stat-box">
              <span class="calc-stat-label">Natężenie Prądu (I)</span>
              <div class="calc-stat-val" id="res-p-amp">2.00 A</div>
            </div>

            <div class="calc-stat-box" id="res-drop-box">
              <span class="calc-stat-label">Spadek Napięcia</span>
              <div class="calc-stat-val" id="res-p-drop">0.28 V (1.2%)</div>
            </div>

          </div>
        </div>

        <div class="calc-advice-card" id="res-p-advice">
          <strong>Rekomendacja inżynierska Prescot:</strong> Spadek napięcia poniżej 3% (norma). Zasilacz 60W 24V DC zapewni stabilną, cichą pracę z zapasem mocy.
        </div>
      </div>
    </div>
  </section>

</main>

<script>
// ==========================================
// FAQ ACCORDION & SEARCH & FILTERS CONTROLLER
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  const faqCards = document.querySelectorAll('.faq-card');
  const searchInput = document.getElementById('bw-search-input');
  const filterBtns = document.querySelectorAll('.bw-filter-btn');

  // Accordion toggle
  faqCards.forEach(card => {
    const btn = card.querySelector('.faq-btn');
    btn.addEventListener('click', () => {
      const isOpen = card.classList.contains('open');
      faqCards.forEach(c => c.classList.remove('open'));
      if (!isOpen) {
        card.classList.add('open');
      }
    });
  });

  // Filter functionality
  let currentFilter = 'all';
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.getAttribute('data-filter');
      applyFilterAndSearch();
    });
  });

  // Search functionality
  searchInput?.addEventListener('input', () => {
    applyFilterAndSearch();
  });

  function applyFilterAndSearch() {
    const q = (searchInput?.value || '').toLowerCase().trim();
    faqCards.forEach(card => {
      const cat = card.getAttribute('data-category');
      const text = card.textContent.toLowerCase();
      const matchFilter = (currentFilter === 'all' || cat === currentFilter);
      const matchSearch = (!q || text.includes(q));

      if (matchFilter && matchSearch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // ==========================================
  // INTERACTIVE LED CALCULATOR LOGIC
  // ==========================================
  const selTapePower = document.getElementById('c-tape-power');
  const inpCustomPower = document.getElementById('c-custom-power');
  const rngTapeLen = document.getElementById('c-tape-len');
  const selVoltage = document.getElementById('c-tape-voltage');
  const selWireLen = document.getElementById('c-wire-len');
  const selWireSection = document.getElementById('c-wire-section');

  const txtPowerDisplay = document.getElementById('c-power-display');
  const txtLenDisplay = document.getElementById('c-len-display');
  const txtVoltDisplay = document.getElementById('c-volt-display');
  const txtWireDisplay = document.getElementById('c-wire-display');

  const resPNom = document.getElementById('res-p-nom');
  const resPPsu = document.getElementById('res-p-psu');
  const resPAmp = document.getElementById('res-p-amp');
  const resPDrop = document.getElementById('res-p-drop');
  const resAdvice = document.getElementById('res-p-advice');

  function calculateLed() {
    let powerPerM = parseFloat(selTapePower.value);
    if (selTapePower.value === 'custom') {
      inpCustomPower.style.display = 'block';
      powerPerM = parseFloat(inpCustomPower.value) || 9.6;
      txtPowerDisplay.textContent = powerPerM.toFixed(1) + ' W/m';
    } else {
      inpCustomPower.style.display = 'none';
      txtPowerDisplay.textContent = powerPerM.toFixed(1) + ' W/m';
    }

    const lengthM = parseFloat(rngTapeLen.value) || 5;
    txtLenDisplay.textContent = lengthM.toFixed(1) + ' m';

    const voltage = parseFloat(selVoltage.value) || 24;
    txtVoltDisplay.textContent = voltage + 'V DC';

    const wireLen = parseFloat(selWireLen.value) || 3;
    txtWireDisplay.textContent = wireLen + ' m';

    const wireSection = parseFloat(selWireSection.value) || 0.75;

    // Obliczenia
    const nominalPower = powerPerM * lengthM;
    const psuBufferPower = nominalPower * 1.20;
    const currentAmp = nominalPower / voltage;

    const psuSizes = [15, 25, 35, 60, 75, 100, 150, 200, 250, 320, 350, 400, 500, 600];
    let recPsu = psuSizes.find(s => s >= psuBufferPower) || Math.ceil(psuBufferPower / 50) * 50;

    const rWire = (0.0175 * (wireLen * 2)) / wireSection;
    const vDrop = currentAmp * rWire;
    const vDropPercent = (vDrop / voltage) * 100;

    resPNom.textContent = nominalPower.toFixed(1) + ' W';
    resPPsu.textContent = 'min. ' + recPsu + ' W';
    resPAmp.textContent = currentAmp.toFixed(2) + ' A';
    resPDrop.textContent = vDrop.toFixed(2) + ' V (' + vDropPercent.toFixed(1) + '%)';

    let adviceHtml = '<strong>Rekomendacja inżynierska Prescot:</strong> ';
    if (vDropPercent > 5.0) {
      adviceHtml += '<span style="color:#f87171;">Uwaga: Spadek napięcia (' + vDropPercent.toFixed(1) + '%) przekracza 5%! Zwiększ przekrój przewodu do 1.5–2.5 mm² lub zastosuj zasilanie obustronne.</span>';
    } else if (lengthM > 5.0 && voltage === 12) {
      adviceHtml += 'Dla taśmy 12V o długości ' + lengthM + 'm zalecamy przejście na 24V lub zasilenie odcinka z obu stron (początek i koniec).';
    } else if (lengthM > 10.0) {
      adviceHtml += 'Dla odcinka ' + lengthM + 'm zastosuj magistralę zasilającą z wpięciem co 5 metrów.';
    } else {
      adviceHtml += 'Parametry w normie. Rekomendujemy zasilacz impulsowy Prescot <strong>' + recPsu + 'W ' + voltage + 'V DC</strong> o sprawności &gt;90%.';
    }
    resAdvice.innerHTML = adviceHtml;
  }

  selTapePower.addEventListener('change', calculateLed);
  inpCustomPower.addEventListener('input', calculateLed);
  rngTapeLen.addEventListener('input', calculateLed);
  selVoltage.addEventListener('change', calculateLed);
  selWireLen.addEventListener('change', calculateLed);
  selWireSection.addEventListener('change', calculateLed);

  calculateLed();
});
</script>
"""

with open("/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

footer_html = footer_html.replace('data-src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"', 'src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"')
footer_html = footer_html.replace('src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs="', 'src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"')

unified_dock = """<!-- GLOBAL MENU START -->
<nav class="prescot-dock" aria-label="Nawigacja główna">
  <a href="/prescotled/" class="dock-item" data-tooltip="Prescot LED" aria-label="Prescot LED">
    <svg class="dock-logo-icon" viewBox="0 0 378 258" xmlns="http://www.w3.org/2000/svg">
      <path fill="#e14e26" d="M0,0h106.7v50H0V0ZM0,100.9h97.7v48.2H0v-48.2ZM0,206.6h106.7v51.2H0v-51.2h0ZM149.3,100.7h82v48.4h-82v-48.4h0ZM149.3,0h87.4C317.7,0,377.9,42.6,377.9,128.9s-60.1,128.9-141.2,128.9h-87.4v-51.2h90.8c47.8,0,76.6-29.1,76.6-77.7s-27.6-78.8-76.6-78.8h-90.8V0h0Z"/>
    </svg>
  </a>

  <a href="/produkty/" class="dock-item" data-tooltip="Oferta" aria-label="Oferta">
    <svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M542.22 32.05c-54.8 3.11-163.72 14.43-230.96 55.59-4.64 2.84-7.27 7.89-7.27 13.17v363.87c0 11.55 12.63 18.85 23.28 13.49 69.18-34.82 169.23-44.32 218.7-46.92 16.89-.89 30.02-14.43 30.02-30.66V62.75c.01-17.71-15.35-31.74-33.77-30.7zM264.73 87.64C197.5 46.48 88.58 35.17 33.78 32.05 15.36 31.01 0 45.04 0 62.75V400.6c0 16.24 13.13 29.78 30.02 30.66 49.49 2.6 149.59 12.11 218.77 46.95 10.62 5.35 23.21-1.94 23.21-13.46V100.63c0-5.29-2.62-10.14-7.27-12.99z"/>
    </svg>
  </a>

  <a href="/tasmy-led/" class="dock-item" data-tooltip="Taśmy LED" aria-label="Taśmy LED">
    <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M224 192c-35.3 0-64 28.7-64 64s28.7 64 64 64 64-28.7 64-64-28.7-64-64-64zm400 224H380.6c41.5-40.7 67.4-97.3 67.4-160 0-123.7-100.3-224-224-224S0 132.3 0 256s100.3 224 224 224h400c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zm-400-64c-53 0-96-43-96-96s43-96 96-96 96 43 96 96-43 96-96 96z"/>
    </svg>
  </a>

  <a href="/produkcja/" class="dock-item" data-tooltip="Produkcja" aria-label="Produkcja">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M475.115 163.781L336 252.309v-68.28c0-18.916-20.931-30.399-36.885-20.248L160 252.309V56c0-13.255-10.745-24-24-24H24C10.745 32 0 42.745 0 56v400c0 13.255 10.745 24 24 24h464c13.255 0 24-10.745 24-24V184.029c0-18.917-20.931-30.399-36.885-20.248z"/>
    </svg>
  </a>

  <a href="/wspolpraca-b2b/" class="dock-item" data-tooltip="Strefa B2B" aria-label="Strefa B2B">
    <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M128 352H32c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32zm-24-80h192v48h48v-48h192v48h48v-57.59c0-21.17-17.23-38.41-38.41-38.41H344v-64h40c17.67 0 32-14.33 32-32V32c0-17.67-14.33-32-32-32H256c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h40v64H94.41C73.23 224 56 241.23 56 262.41V320h48v-48zm264 80h-96c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32zm240 0h-96c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32z"/>
    </svg>
  </a>

  <a href="/baza-wiedzy/" class="dock-item" data-tooltip="Baza Wiedzy" aria-label="Baza Wiedzy & FAQ">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M256 32C132.3 32 32 132.3 32 256s100.3 224 224 224 224-100.3 224-224S379.7 32 256 32zm0 376c-17.7 0-32-14.3-32-32s14.3-32 32-32 32 14.3 32 32-14.3 32-32 32zm42.7-142.1c-13.8 11.2-26.7 21.6-26.7 46.1v10c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-14c0-38.4 22.8-56.9 44.4-74.4 14.1-11.4 27.6-22.3 27.6-39.6 0-21.2-18.7-36-44-36-24.6 0-41.9 14.2-46.7 32.5-2.2 8.5-10.4 13.9-19.1 12.3l-30.8-5.6c-9.1-1.7-14.8-10.7-12.4-19.7C180.7 132.2 214.2 104 256 104c53 0 96 34.3 96 82 0 35.8-21.7 61.2-53.3 83.9z"/>
    </svg>
  </a>

  <a href="https://prescot.com.pl/" class="dock-item" data-tooltip="Sklep B2C" aria-label="Sklep B2C" target="_blank" rel="noopener">
    <svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M576 216v16c0 13.255-10.745 24-24 24h-8l-26.113 182.788C514.509 462.435 494.257 480 470.37 480H105.63c-23.887 0-44.139-17.565-47.518-41.212L32 256h-8c-13.255 0-24-10.745-24-24v-16c0-13.255 10.745-24 24-24h67.341l106.78-146.821c10.395-14.292 30.407-17.453 44.701-7.058 14.293 10.395 17.453 30.408 7.058 44.701L170.477 192h235.046L326.12 82.821c-10.395-14.292-7.234-34.306 7.059-44.701 14.291-10.395 34.306-7.235 44.701 7.058L484.659 192H552c13.255 0 24 10.745 24 24zM312 392V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm112 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm-224 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24z"/>
    </svg>
  </a>

  <a href="/kontakt/" class="dock-item" data-tooltip="Kontakt" aria-label="Kontakt">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M493.4 24.6l-104-24c-11.3-2.6-22.9 3.3-27.5 14l-48 112c-4.2 9.8-1.4 21.3 6.9 28l60.6 49.6c-36 76.7-98.9 140.5-177.2 177.2l-49.6-60.6c-6.8-8.3-18.2-11.1-28-6.9l-112 48C4.1 366.5-1.8 378.1.8 389.4l24 104C27.3 504.2 36.7 512 48 512c256.1 0 464-207.5 464-464 0-11.2-7.7-21-18.6-23.4z"/>
    </svg>
  </a>

  <div class="dock-lang-item">
    <div class="gtranslate_wrapper" id="gt-wrapper-85632840"></div>
  </div>
</nav>
<!-- GLOBAL MENU END -->
<script>
window.gtranslateSettings = window.gtranslateSettings || {};
window.gtranslateSettings['85632840'] = {"default_language":"pl","languages":["ar","zh-CN","cs","da","en","et","fi","fr","de","it","lt","pl","es","sv"],"url_structure":"none","flag_style":"3d","wrapper_selector":"#gt-wrapper-85632840","alt_flags":[],"float_switcher_open_direction":"top","switcher_horizontal_position":"inline","flags_location":"/wp-content/plugins/gtranslate/flags/"};
</script>
<script src="/wp-content/plugins/gtranslate/js/float.js?ver=3.1.1" data-no-optimize="1" data-no-minify="1" data-gt-widget-id="85632840" defer></script>
<script src="/local-navigation.js?v=20260901-white-dock" defer></script>
</body>
</html>
"""

with open(os.path.join(base_dir, "baza-wiedzy/index.html"), "w", encoding="utf-8") as f:
    f.write(baza_html + footer_html + unified_dock)
print("Updated baza-wiedzy/index.html with photo hero and non-sticky header.")

# ==============================================================================
# 2. WSPÓŁPRACA B2B & DYSTRYBUCJA (Photo Hero & Non-sticky Topbar)
# ==============================================================================
b2b_shared_css = """
<style>
:root {
  --p-primary: #e55933;
  --p-primary-hover: #c94622;
  --p-dark: #0f172a;
  --p-dark-soft: #1e293b;
  --p-text: #212a35;
  --p-text-muted: #64748b;
  --p-bg: #f8fafc;
  --p-card-bg: #ffffff;
  --p-border: #e2e8f0;
  --p-radius: 20px;
  --p-radius-sm: 8px;
  --p-shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --p-shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -1px rgba(0,0,0,0.04);
  --p-shadow-lg: 0 10px 25px -3px rgba(0,0,0,0.09), 0 4px 6px -2px rgba(0,0,0,0.04);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--p-text);
  background: var(--p-bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  padding-bottom: 90px;
}

/* TOPBAR: SCHODZI I CHOWA SIĘ NA GÓRZE (POSITION: RELATIVE) */
.prescot-topbar {
  background: #ffffff;
  border-bottom: 1px solid var(--p-border);
  padding: 16px 24px;
  position: relative;
  z-index: 10;
}
.prescot-topbar-inner {
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.prescot-logo-link img {
  height: 38px;
  width: auto;
  display: block;
}
.prescot-topbar-tagline {
  font-size: 13px;
  color: var(--p-text-muted);
  font-weight: 500;
}
@media (max-width: 600px) {
  .prescot-topbar-tagline { display: none; }
}

.prescot-main-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 32px 24px 80px 24px;
}

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
  opacity: 0.4;
}

/* HERO ZE ZDJĘCIEM W TLE */
.p-hero {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.82) 0%, rgba(30, 41, 59, 0.88) 100%), 
              url('/wp-content/uploads/2026/02/aerial-drone-shot-of-a-modern-building-facade-illu-2024-08-23-14-38-48-utc-e1772569546453.webp') center/cover no-repeat;
  color: #ffffff;
  border-radius: var(--p-radius);
  padding: 60px 48px;
  margin-bottom: 48px;
  box-shadow: var(--p-shadow-lg);
  position: relative;
  overflow: hidden;
}
.p-hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(229, 89, 51, 0.25);
  color: #ff8a65;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 6px 14px;
  border-radius: 30px;
  margin-bottom: 18px;
  border: 1px solid rgba(229, 89, 51, 0.4);
  backdrop-filter: blur(4px);
}
.p-hero h1 {
  font-family: 'Outfit', sans-serif;
  font-size: clamp(32px, 4vw, 44px);
  color: #ffffff;
  margin-bottom: 16px;
  line-height: 1.2;
  font-weight: 700;
}
.p-hero p.lead {
  font-size: clamp(15px, 1.8vw, 17px);
  color: #e2e8f0;
  max-width: 800px;
  line-height: 1.65;
  margin-bottom: 28px;
  text-shadow: 0 1px 2px rgba(0,0,0,0.4);
}
.p-hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}
.p-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 26px;
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
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff !important;
  border: 1px solid rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(6px);
}
.p-btn-outline:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: #ffffff;
}

/* B2B DUAL ACTION CARDS */
.b2b-action-layout {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 32px;
  margin-bottom: 56px;
  align-items: stretch;
}
@media (max-width: 950px) {
  .b2b-action-layout { grid-template-columns: 1fr; }
}

.b2b-login-card-light {
  background: #ffffff;
  border: 1.5px solid rgba(229, 89, 51, 0.35);
  border-radius: var(--p-radius);
  padding: 40px 36px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 30px rgba(229, 89, 51, 0.08);
  position: relative;
  transition: all 0.25s ease;
}
.b2b-login-card-light:hover {
  border-color: var(--p-primary);
  transform: translateY(-3px);
  box-shadow: 0 12px 35px rgba(229, 89, 51, 0.15);
}

.b2b-pill-orange {
  display: inline-block;
  align-self: flex-start;
  padding: 5px 14px;
  border-radius: 999px;
  background: #e55933;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #ffffff;
  margin-bottom: 16px;
}

.b2b-pill-slate {
  display: inline-block;
  align-self: flex-start;
  padding: 5px 14px;
  border-radius: 999px;
  background: #e2e8f0;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #334155;
  margin-bottom: 16px;
}

.b2b-login-card-light h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 12px;
}
.b2b-login-card-light p {
  color: #475569;
  font-size: 14.5px;
  line-height: 1.65;
  margin-bottom: 24px;
}
.b2b-login-features-light {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 32px;
}
.b2b-login-features-light li {
  font-size: 14px;
  color: #334155;
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 500;
}
.b2b-login-features-light svg {
  color: var(--p-primary);
  flex-shrink: 0;
}
.b2b-login-card-light .p-btn {
  margin-top: auto;
  align-self: flex-start;
}

.p-form-box-light {
  background: #ffffff;
  border: 1.5px solid #cbd5e1;
  border-radius: var(--p-radius);
  padding: 40px 36px;
  box-shadow: var(--p-shadow-sm);
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
}
.p-form-box-light:hover {
  border-color: #94a3b8;
  box-shadow: var(--p-shadow-md);
}
.p-form-box-light h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 8px;
}
.p-form-box-light p.form-desc {
  color: #64748b;
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 24px;
}
.p-form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}
@media (max-width: 600px) {
  .p-form-grid { grid-template-columns: 1fr; }
}
.p-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.p-group.full {
  grid-column: 1 / -1;
}
.p-group label {
  font-size: 13px;
  font-weight: 600;
  color: var(--p-dark);
}
.p-group input, .p-group select, .p-group textarea {
  padding: 12px 16px;
  border: 1px solid #d1d5db;
  border-radius: var(--p-radius-sm);
  font-size: 14px;
  background: #f8fafc;
  color: var(--p-dark);
  outline: none;
  font-family: inherit;
  transition: all 0.2s;
}
.p-group input:focus, .p-group select:focus, .p-group textarea:focus {
  border-color: var(--p-primary);
  background: #ffffff;
  box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.15);
}
.p-group textarea {
  resize: vertical;
  min-height: 100px;
}
.p-checkbox-label {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 12px;
  color: var(--p-text-muted);
  cursor: pointer;
}
.p-checkbox-label input {
  margin-top: 3px;
}

.delicate-benefits-section {
  background: #ffffff;
  border: 1px solid var(--p-border);
  border-radius: var(--p-radius);
  padding: 48px 40px;
  margin-bottom: 60px;
  box-shadow: var(--p-shadow-sm);
}
.delicate-benefits-header {
  text-align: center;
  max-width: 650px;
  margin: 0 auto 40px auto;
}
.delicate-benefits-header h2 {
  font-family: 'Outfit', sans-serif;
  font-size: 26px;
  color: var(--p-dark);
  margin-bottom: 8px;
}
.delicate-benefits-header p {
  color: var(--p-text-muted);
  font-size: 14px;
}
.delicate-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
.delicate-item {
  padding: 20px;
  border-radius: 14px;
  background: #f8fafc;
  border: 1px solid #edf2f7;
  transition: all 0.2s;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}
.delicate-item:hover {
  background: #ffffff;
  border-color: var(--p-primary);
  box-shadow: var(--p-shadow-md);
  transform: translateY(-2px);
}
.delicate-icon-wrap {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background: rgba(229, 89, 51, 0.12);
  color: var(--p-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.delicate-content h4 {
  font-family: 'Outfit', sans-serif;
  font-size: 16px;
  color: var(--p-dark);
  margin-bottom: 4px;
}
.delicate-content p {
  font-size: 13px;
  color: var(--p-text-muted);
  line-height: 1.5;
  margin: 0;
}
</style>
</head>
<body>
<!-- TOPBAR: SCHODZI PRZY SCROLLU -->
<header class="prescot-topbar">
  <div class="prescot-topbar-inner">
    <a href="/" class="prescot-logo-link" title="Prescot LED Strona Główna">
      <img src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg" alt="Prescot LED">
    </a>
    <span class="prescot-topbar-tagline">Polski Producent Oświetlenia LED &bull; Giżycko</span>
  </div>
</header>
"""

def generate_b2b_page(breadcrumb_name, page_title):
    head_b2b = """<!DOCTYPE html>
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
  <title>""" + page_title + """</title>
"""
    body_content = """
<main class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>""" + breadcrumb_name + """</span>
  </nav>

  <!-- HERO ZE ZDJĘCIEM W TLE -->
  <div class="p-hero">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      Oficjalna Strefa Partnerska B2B
    </div>
    <h1>Program Partnerski & Dystrybucja Prescot LED</h1>
    <p class="lead">Dołącz do grona autoryzowanych dystrybutorów, hurtowni elektrotechnicznych i certyfikowanych instalatorów. Zyskaj bezpośredni dostęp do magazynu centralnego, indywidualnych progów rabatowych i pełnego wsparcia inżynieryjnego.</p>
    <div class="p-hero-actions">
      <a href="#strefa-rejestracji" class="p-btn p-btn-primary">
        Zgłoś firmę do programu B2B
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="https://prescot.abstore.pl/client/loginorcreate/login" class="p-btn p-btn-outline" target="_blank">
        Platforma Zamówień B2B (Logowanie)
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
      </a>
    </div>
  </div>

  <!-- B2B DUAL ACTION CARDS -->
  <div id="strefa-rejestracji" class="b2b-action-layout">
    
    <!-- LEWA KARTA: LOGOWANIE -->
    <div class="b2b-login-card-light">
      <span class="b2b-pill-orange">Mam już konto B2B</span>
      <h3>Logowanie do Hurtowni</h3>
      <p>Dla zarejestrowanych dystrybutorów, instalatorów i partnerów handlowych. Dostęp do cen hurtowych, stanów magazynowych live i szybkiego zamawiania 24/7.</p>
      
      <ul class="b2b-login-features-light">
        <li>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Podgląd stanów magazynowych na żywo w Giżycku
        </li>
        <li>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Indywidualne ceny hurtowe przypisane do Twojego NIP
        </li>
        <li>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Błyskawiczne ponawianie zamówień i e-faktury
        </li>
        <li>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Pobieranie plików produktowych XML / CSV
        </li>
      </ul>

      <a href="https://prescot.abstore.pl/client/loginorcreate/login" target="_blank" class="p-btn p-btn-primary">
        Przejdź do logowania &rarr;
      </a>
    </div>

    <!-- PRAWA KARTA: FORMULARZ -->
    <div class="p-form-box-light">
      <span class="b2b-pill-slate">Nowy Partner</span>
      <h3>Zarejestruj się / Dołącz</h3>
      <p class="form-desc">Chcesz zostać dystrybutorem lub zaopatrywać swoje inwestycje w taśmy i sterowniki Prescot? Wypełnij formularz — aktywujemy rabat startowy.</p>

      <form class="p-form-grid" id="b2b-form-action" action="javascript:void(0);">
        <div class="p-group">
          <label for="b-company">Nazwa firmy *</label>
          <input type="text" id="b-company" placeholder="np. Elektro-Instal Sp. z o.o." required>
        </div>

        <div class="p-group">
          <label for="b-nip">Numer NIP *</label>
          <input type="text" id="b-nip" placeholder="np. 8451993424" required>
        </div>

        <div class="p-group">
          <label for="b-name">Osoba kontaktowa *</label>
          <input type="text" id="b-name" placeholder="np. Marek Wiśniewski" required>
        </div>

        <div class="p-group">
          <label for="b-phone">Numer telefonu *</label>
          <input type="tel" id="b-phone" placeholder="+48 000 000 000" required>
        </div>

        <div class="p-group">
          <label for="b-email">Firmowy adres e-mail *</label>
          <input type="email" id="b-email" placeholder="kontakt@twojafirma.pl" required>
        </div>

        <div class="p-group">
          <label for="b-type">Profil działalności</label>
          <select id="b-type">
            <option value="instalator">Instalator / Elektryk / Montażysta</option>
            <option value="projektant">Biuro Architektoniczne / Projektant Wnętrz</option>
            <option value="hurtownia">Hurtownia Elektrotechniczna / Sklep Oświetleniowy</option>
            <option value="producent">Producent mebli / reklam / zabudów</option>
            <option value="inny">Inny profil działalności</option>
          </select>
        </div>

        <div class="p-group full">
          <label for="b-notes">Uwagi / Oczekiwany asortyment (opcjonalnie)</label>
          <textarea id="b-notes" placeholder="np. stałe zapotrzebowanie na taśmy COB 24V, zasilacze meblowe, wzorniki dla klientów..."></textarea>
        </div>

        <div class="p-group full">
          <label class="p-checkbox-label">
            <input type="checkbox" required>
            <span>Wyrażam zgodę na przetwarzanie danych firmy w celu weryfikacji i aktywacji konta hurtowego w programie partnerskim PRESCOT sp. z o.o. zgodnie z Polityką Prywatności.</span>
          </label>
        </div>

        <div class="p-group full">
          <button type="submit" class="p-btn p-btn-primary" style="justify-self:start;">
            Wypełnij formularz partnerski &rarr;
          </button>
        </div>

        <div id="b-feedback" class="p-group full" style="display:none; padding:14px 18px; border-radius:8px; font-size:14px; background:#dcfce7; color:#166534; border:1px solid #bbf7d0;">
          <strong>Dziękujemy!</strong> Zgłoszenie partnerskie zostało pomyślnie przesłane. Dział handlowy Prescot LED skontaktuje się z Państwem niezwłocznie.
        </div>
      </form>
    </div>
  </div>

  <!-- DELIKATNA SEKCJA KORZYŚCI -->
  <section class="delicate-benefits-section">
    <div class="delicate-benefits-header">
      <h2>Korzyści ze stałej współpracy partnerskiej</h2>
      <p>Przejrzyste, partnerskie zasady bez zbędnej biurokracji i sztucznych barier wejścia.</p>
    </div>

    <div class="delicate-grid">
      <div class="delicate-item">
        <div class="delicate-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        </div>
        <div class="delicate-content">
          <h4>Wysyłka w 24h z Giżycka</h4>
          <p>Zamówienia złożone do godziny 13:00 wysyłamy tego samego dnia bezpośrednio z magazynu centralnego.</p>
        </div>
      </div>

      <div class="delicate-item">
        <div class="delicate-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <div class="delicate-content">
          <h4>Minimum logistyczne 0 zł</h4>
          <p>Zamawiaj dokładnie tyle, ile potrzebujesz na dany etap montażu – bez dopłat do małych paczek.</p>
        </div>
      </div>

      <div class="delicate-item">
        <div class="delicate-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        </div>
        <div class="delicate-content">
          <h4>Odroczony termin płatności</h4>
          <p>Dla stałych partnerów oferujemy wygodny kredyt kupiecki na 14 lub 30 dni.</p>
        </div>
      </div>

      <div class="delicate-item">
        <div class="delicate-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <div class="delicate-content">
          <h4>Dedykowany opiekun B2B</h4>
          <p>Bezpośredni kontakt telefoniczny i mailowy do inżyniera handlowego prowadzącego Twoją firmę.</p>
        </div>
      </div>

      <div class="delicate-item">
        <div class="delicate-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
        </div>
        <div class="delicate-content">
          <h4>Próbki & Standy pokazowe</h4>
          <p>Bezpłatne wzorniki profili i taśm COB dla Twojego biura projektowego lub salonu sprzedaży.</p>
        </div>
      </div>

      <div class="delicate-item">
        <div class="delicate-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <div class="delicate-content">
          <h4>Pliki IES & Wsparcie CAD</h4>
          <p>Kompletna dokumentacja fotometryczna, certyfikaty i wsparcie obliczeń oświetlenia w DIALux.</p>
        </div>
      </div>
    </div>
  </section>
</main>

<script>
document.getElementById('b2b-form-action').addEventListener('submit', function(e) {
  e.preventDefault();
  document.getElementById('b-feedback').style.display = 'block';
  this.reset();
});
</script>
"""
    return head_b2b + b2b_shared_css + body_content + footer_html + unified_dock

# Write wspolpraca-b2b/index.html
with open(os.path.join(base_dir, "wspolpraca-b2b/index.html"), "w", encoding="utf-8") as f:
    f.write(generate_b2b_page("Współpraca B2B", "Współpraca B2B & Strefa Hurtowa — Prescot LED"))
print("Updated wspolpraca-b2b/index.html with photo hero and non-sticky header.")

# Write dystrybucja/index.html
with open(os.path.join(base_dir, "dystrybucja/index.html"), "w", encoding="utf-8") as f:
    f.write(generate_b2b_page("Dystrybucja", "Dystrybucja & Program Partnerski B2B — Prescot LED"))
print("Updated dystrybucja/index.html with photo hero and non-sticky header.")

