# -*- coding: utf-8 -*-
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
WHITE_ORANGE_LOGO = "/wp-content/uploads/2025/12/biale-z-kolorem.svg"

smart_logo_html = '''<!-- SMART LOGO: BIAŁE Z POMARAŃCZEM (ZNIKA PRZY SCROLLU W DÓŁ, WRACA W GÓRĘ) -->
<div class="prescot-smart-logo">
  <a href="/" title="Prescot LED Strona Główna">
    <img src="/wp-content/uploads/2025/12/biale-z-kolorem.svg" alt="Prescot LED">
  </a>
</div>
'''

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

with open("/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

footer_html = footer_html.replace('data-src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"', 'src="/wp-content/uploads/2025/12/biale-z-kolorem.svg"')
footer_html = footer_html.replace('src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs="', 'src="/wp-content/uploads/2025/12/biale-z-kolorem.svg"')

# ==============================================================================
# CSS DEFINITIONS
# ==============================================================================
common_css = """
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

  html {
    scroll-behavior: smooth;
  }

  body {
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--p-text);
    background: var(--p-bg);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding-bottom: 90px;
  }

  /* FULL-SCREEN 100VH HERO SLIDE (NO SCROLL REQUIRED TO SEE FULL HERO) */
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
    background: rgba(229, 89, 51, 0.25);
    color: #ff8a65;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    padding: 7px 18px;
    border-radius: 30px;
    margin-bottom: 22px;
    border: 1px solid rgba(229, 89, 51, 0.45);
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

  /* STRZAŁKA W DÓŁ (BOUNCING ARROW) */
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
  .p-hero-arrow-down:hover {
    opacity: 1;
    color: #ff8a65;
  }
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

  /* TREŚĆ PONIŻEJ HERO */
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
  .prescot-breadcrumbs a {
    color: var(--p-text-muted);
    text-decoration: none;
    transition: color 0.2s;
  }
  .prescot-breadcrumbs a:hover {
    color: var(--p-primary);
  }
  .prescot-breadcrumbs .sep { opacity: 0.4; }
"""

# ==============================================================================
# 1. BAZA WIEDZY
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
""" + common_css + """
  /* FAQ STYLES */
  .faq-search-wrap { margin-bottom: 36px; position: relative; }
  .faq-search-input {
    width: 100%; padding: 16px 20px 16px 52px; font-size: 16px; background: #ffffff;
    border: 1px solid var(--p-border); border-radius: 30px; outline: none; box-shadow: var(--p-shadow-sm);
    font-family: inherit; transition: all 0.25s ease;
  }
  .faq-search-input:focus { border-color: var(--p-primary); box-shadow: 0 0 0 4px rgba(229, 89, 51, 0.15); }
  .faq-search-icon { position: absolute; left: 20px; top: 50%; transform: translateY(-50%); color: var(--p-text-muted); pointer-events: none; }
  .faq-filter-chips { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 32px; }
  .chip-btn {
    padding: 8px 18px; border-radius: 20px; font-size: 13px; font-weight: 600;
    background: #ffffff; border: 1px solid var(--p-border); color: #475569; cursor: pointer; transition: all 0.2s;
  }
  .chip-btn.active, .chip-btn:hover { background: var(--p-dark); color: #ffffff; border-color: var(--p-dark); }
  .faq-grid { display: flex; flex-direction: column; gap: 14px; margin-bottom: 70px; }
  .faq-card { background: #ffffff; border: 1px solid var(--p-border); border-radius: 14px; overflow: hidden; box-shadow: var(--p-shadow-sm); transition: all 0.2s; }
  .faq-card:hover { border-color: #cbd5e1; box-shadow: var(--p-shadow-md); }
  .faq-btn {
    width: 100%; text-align: left; background: none; border: none; padding: 20px 24px;
    display: flex; justify-content: space-between; align-items: center; gap: 16px; cursor: pointer;
    font-weight: 700; font-size: 16.5px; color: #0f172a; font-family: 'Outfit', sans-serif;
  }
  .faq-btn-icon {
    width: 32px; height: 32px; border-radius: 50%; background: #f1f5f9; display: flex;
    align-items: center; justify-content: center; flex-shrink: 0; color: #64748b; transition: all 0.25s ease;
  }
  .faq-card.open .faq-btn-icon { background: rgba(229, 89, 51, 0.12); color: var(--p-primary); transform: rotate(180deg); }
  .faq-card.open .faq-btn { color: var(--p-primary); }
  .faq-content { display: none; padding: 0 24px 22px 24px; color: #475569; font-size: 15px; line-height: 1.7; }
  .faq-card.open .faq-content { display: block; border-top: 1px solid #f1f5f9; padding-top: 16px; }

  /* KALKULATOR NA SAMYM DOLE */
  .calc-premium-wrapper { background: #ffffff; border: 1px solid var(--p-border); border-radius: 20px; padding: 40px; box-shadow: var(--p-shadow-lg); margin-bottom: 40px; }
  .calc-grid { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 36px; }
  @media (max-width: 900px) { .calc-grid { grid-template-columns: 1fr; } }
  .calc-form-col { display: flex; flex-direction: column; gap: 20px; }
  .calc-form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 550px) { .calc-form-row { grid-template-columns: 1fr; } }
  .calc-input-group { display: flex; flex-direction: column; gap: 6px; }
  .calc-input-group label { font-size: 13px; font-weight: 600; color: #334155; }
  .calc-input-group select, .calc-input-group input {
    padding: 12px 16px; border: 1px solid var(--p-border); border-radius: 8px; font-size: 14.5px;
    background: #f8fafc; color: #0f172a; outline: none; font-family: inherit; transition: all 0.2s;
  }
  .calc-input-group select:focus, .calc-input-group input:focus {
    border-color: var(--p-primary); background: #ffffff; box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.15);
  }
  .calc-results-box {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius: 16px;
    padding: 32px; color: #ffffff; display: flex; flex-direction: column; justify-content: space-between;
  }
  .calc-res-item { display: flex; justify-content: space-between; align-items: baseline; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
  .calc-res-item:last-child { border-bottom: none; }
  .calc-res-label { font-size: 13.5px; color: #94a3b8; }
  .calc-res-val { font-size: 22px; font-weight: 800; font-family: 'Outfit', sans-serif; color: #ffffff; }
  .calc-res-val.highlight { color: #ff8a65; }
  .calc-advice-card {
    background: rgba(229, 89, 51, 0.15); border: 1px solid rgba(229, 89, 51, 0.35);
    border-radius: 10px; padding: 14px 16px; margin-top: 20px; font-size: 13px; color: #cbd5e1; line-height: 1.5;
  }
  </style>
</head>
<body>
""" + smart_logo_html + """

<!-- FULL-SCREEN 100VH HERO SLIDE -->
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/03/AdobeStock_1101216226-1536x861.webp');">
  <div class="p-full-hero-content">
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

  <!-- 2. KALKULATOR NA SAMYM DOLE -->
  <section id="kalkulator-led" class="calc-premium-wrapper">
    <div style="margin-bottom: 28px;">
      <div class="p-hero-eyebrow" style="background:rgba(229,89,51,0.1); color:var(--p-primary); border-color:rgba(229,89,51,0.25);">
        Narzędzie Inżynieryjne
      </div>
      <h2 style="font-family:'Outfit',sans-serif; font-size: 28px; color: var(--p-dark); margin-bottom: 8px;">Kalkulator Zasilania &amp; Spadków Napięcia LED</h2>
      <p style="color: var(--p-text-muted); font-size: 15px;">Wprowadź parametry instalacji, aby automatycznie dobrać optymalną moc zasilacza, przekrój przewodu i schemat podłączenia.</p>
    </div>

    <div class="calc-grid">
      <!-- FORM COLUMN -->
      <div class="calc-form-col">
        <div class="calc-form-row">
          <div class="calc-input-group">
            <label for="calc-voltage">Napięcie taśmy LED</label>
            <select id="calc-voltage">
              <option value="24" selected>24V DC (Zalecane profesjonalne)</option>
              <option value="12">12V DC (Standardowe)</option>
              <option value="48">48V DC (Systemy szynowe)</option>
            </select>
          </div>

          <div class="calc-input-group">
            <label for="calc-power-per-m">Moc taśmy (W/metr)</label>
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
          <div class="calc-input-group">
            <label for="calc-length">Długość odcinka LED (m)</label>
            <input type="number" id="calc-length" value="6" min="0.5" max="100" step="0.5">
          </div>

          <div class="calc-input-group">
            <label for="calc-cable-len">Długość przewodu zasilającego (m)</label>
            <input type="number" id="calc-cable-len" value="3" min="0.5" max="50" step="0.5">
          </div>
        </div>

        <div class="calc-input-group">
          <label for="calc-wire-cross">Przekrój przewodu (mm²)</label>
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
      <div class="calc-results-box">
        <div>
          <div style="font-size: 13px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#ff8a65; margin-bottom:14px;">
            Wyniki obliczeń &amp; Dobór
          </div>

          <div class="calc-res-item">
            <span class="calc-res-label">Moc znamionowa LED:</span>
            <span class="calc-res-val" id="res-nominal-power">86.4 W</span>
          </div>

          <div class="calc-res-item">
            <span class="calc-res-label">Zalecany zasilacz (+20%):</span>
            <span class="calc-res-val highlight" id="res-power-supply">103.7 W</span>
          </div>

          <div class="calc-res-item">
            <span class="calc-res-label">Prąd roboczy (I):</span>
            <span class="calc-res-val" id="res-current">3.60 A</span>
          </div>

          <div class="calc-res-item">
            <span class="calc-res-label">Szacowany spadek na kablu:</span>
            <span class="calc-res-val" id="res-drop">0.34 V (1.4%)</span>
          </div>
        </div>

        <div class="calc-advice-card" id="res-advice">
          <strong>Rekomendacja Prescot:</strong> Dobierz zasilacz <strong>Prescot Ultra Slim 120W 24V IP20/IP67</strong>. Zasilanie jednostronne jest w pełni wystarczające.
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

with open(os.path.join(base_dir, "baza-wiedzy/index.html"), "w", encoding="utf-8") as f:
    f.write(baza_html + footer_html + unified_dock)
print("Updated baza-wiedzy with 100vh Full-Screen Photo Hero and Bouncing Down Arrow.")

# ==============================================================================
# 2. WSPOLPRACA-B2B & DYSTRYBUCJA
# ==============================================================================
def make_b2b_page(title, h1_title, eyebrow_text):
    return """<!DOCTYPE html>
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
  <title>""" + title + """</title>
  <style>
""" + common_css + """
  .b2b-action-grid {
    display: grid;
    grid-template-columns: 1fr 1.15fr;
    gap: 32px;
    margin-bottom: 60px;
  }
  @media (max-width: 850px) {
    .b2b-action-grid { grid-template-columns: 1fr; }
  }
  .b2b-login-box {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: var(--p-radius);
    padding: 38px 32px;
    color: #ffffff;
    box-shadow: var(--p-shadow-lg);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: 1px solid rgba(229, 89, 51, 0.3);
  }
  .b2b-login-box h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    margin-bottom: 12px;
    color: #ffffff;
  }
  .b2b-login-box p {
    color: #94a3b8;
    font-size: 14.5px;
    line-height: 1.6;
    margin-bottom: 24px;
  }
  .b2b-form-box {
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 38px 32px;
    box-shadow: var(--p-shadow-md);
  }
  .b2b-form-box h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    color: var(--p-dark);
    margin-bottom: 8px;
  }
  .b2b-form-box p.form-sub {
    color: var(--p-text-muted);
    font-size: 14px;
    margin-bottom: 24px;
  }
  .p-form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  @media (max-width: 550px) {
    .p-form-grid { grid-template-columns: 1fr; }
  }
  .p-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .p-group.full { grid-column: 1 / -1; }
  .p-group label {
    font-size: 13px;
    font-weight: 600;
    color: var(--p-dark);
  }
  .p-group input, .p-group select, .p-group textarea {
    padding: 12px 14px;
    border: 1px solid var(--p-border);
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
  .p-benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-bottom: 40px;
  }
  .p-benefit-card {
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 16px;
    padding: 26px;
    box-shadow: var(--p-shadow-sm);
    transition: all 0.25s ease;
  }
  .p-benefit-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--p-shadow-md);
    border-color: var(--p-primary);
  }
  .p-benefit-icon {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
  }
  .p-benefit-card h4 {
    font-family: 'Outfit', sans-serif;
    font-size: 17px;
    color: var(--p-dark);
    margin-bottom: 8px;
  }
  .p-benefit-card p {
    color: var(--p-text-muted);
    font-size: 13.5px;
    line-height: 1.55;
  }
  </style>
</head>
<body>
""" + smart_logo_html + """

<!-- FULL-SCREEN 100VH HERO SLIDE -->
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/02/aerial-drone-shot-of-a-modern-building-facade-illu-2024-08-23-14-38-48-utc-e1772569546453.webp');">
  <div class="p-full-hero-content">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
      """ + eyebrow_text + """
    </div>
    <h1>""" + h1_title + """</h1>
    <p class="lead">Dedykowane warunki handlowe, indywidualne progi rabatowe, stany magazynowe w czasie rzeczywistym oraz bezpośrednia wysyłka 24h z Centrali w Giżycku dla hurtowni, instalatorów i architektów.</p>
    <div class="p-hero-actions">
      <a href="#strefa-akcji" class="p-btn p-btn-primary">
        Przejdź do formularza &amp; logowania
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="tel:+48877776482" class="p-btn p-btn-outline">
        Infolinia Handlowa: +48 87 777 64 82
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
    <span>""" + title.split('—')[0].strip() + """</span>
  </nav>

  <div id="strefa-akcji" class="b2b-action-grid">
    <div class="b2b-login-box">
      <div>
        <div class="p-hero-eyebrow" style="background: rgba(229,89,51,0.2); color:#ff8a65; border-color: rgba(229,89,51,0.4); margin-bottom: 16px;">
          Dla Zarejestrowanych Partnerów
        </div>
        <h3>Portal Hurtowy B2B</h3>
        <p>Posiadasz już konto B2B w systemie Prescot? Zaloguj się, aby uzyskać dostęp do swoich rabatów kontraktowych, historii zamówień oraz integracji XML/EDI.</p>
        
        <div style="display:flex; flex-direction:column; gap:12px; margin-bottom: 24px;">
          <input type="email" placeholder="Login / E-mail firmowy" style="padding:13px 16px; border-radius:8px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:#fff; outline:none;">
          <input type="password" placeholder="Hasło" style="padding:13px 16px; border-radius:8px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:#fff; outline:none;">
          <button type="button" class="p-btn p-btn-primary" style="width:100%; justify-content:center; margin-top:4px;">
            Zaloguj się do platformy B2B &rarr;
          </button>
        </div>
      </div>

      <div style="font-size:12.5px; color:#64748b; border-top:1px solid rgba(255,255,255,0.1); padding-top:16px;">
        Zapomniałeś hasła? Skontaktuj się ze swoim opiekunem handlowym: <a href="mailto:komponenty@prescot.pl" style="color:#ff8a65; text-decoration:none;">komponenty@prescot.pl</a>
      </div>
    </div>

    <div class="b2b-form-box">
      <h3>Dołącz do sieci partnerskiej Prescot</h3>
      <p class="form-sub">Wypełnij zgłoszenie. Nasz doradca handlowy skontaktuje się z Tobą w ciągu 24h w celu ustalenia warunków rabatowych.</p>

      <form class="p-form-grid" id="b2b-reg-form" action="javascript:void(0);">
        <div class="p-group">
          <label for="b2b-company">Nazwa firmy *</label>
          <input type="text" id="b2b-company" placeholder="np. Elektro-Instal Sp. z o.o." required>
        </div>

        <div class="p-group">
          <label for="b2b-nip">NIP *</label>
          <input type="text" id="b2b-nip" placeholder="000-000-00-00" required>
        </div>

        <div class="p-group">
          <label for="b2b-name">Osoba kontaktowa *</label>
          <input type="text" id="b2b-name" placeholder="Imię i nazwisko" required>
        </div>

        <div class="p-group">
          <label for="b2b-email">Firmowy adres e-mail *</label>
          <input type="email" id="b2b-email" placeholder="biuro@twojafirma.pl" required>
        </div>

        <div class="p-group">
          <label for="b2b-phone">Numer telefonu *</label>
          <input type="tel" id="b2b-phone" placeholder="+48 000 000 000" required>
        </div>

        <div class="p-group">
          <label for="b2b-type">Profil działalności</label>
          <select id="b2b-type">
            <option value="hurtownia">Hurtownia Elektryczna / Oświetleniowa</option>
            <option value="instalator">Instalator / Elektryk</option>
            <option value="architekt">Architekt / Projektant Wnętrz</option>
            <option value="producent">Producent Mebli / Reklam</option>
            <option value="inwestor">Inwestor / Generalny Wykonawca</option>
          </select>
        </div>

        <div class="p-group full">
          <label for="b2b-msg">Uwagi / Zakres współpracy</label>
          <textarea id="b2b-msg" placeholder="Wpisz szacowane miesięczne zapotrzebowanie lub pytania o asortyment..."></textarea>
        </div>

        <div class="p-group full">
          <label style="display:flex; align-items:flex-start; gap:8px; font-size:12px; color:var(--p-text-muted); cursor:pointer;">
            <input type="checkbox" required style="margin-top:3px;">
            <span>Wyrażam zgodę na kontakt handlowy ze strony PRESCOT sp. z o.o. w celu przedstawienia oferty hurtowej.</span>
          </label>
        </div>

        <div class="p-group full">
          <button type="submit" class="p-btn p-btn-primary">
            Wyślij formularz zgłoszeniowy &rarr;
          </button>
        </div>

        <div id="b2b-feedback" class="p-group full" style="display:none; padding: 14px 18px; border-radius: 8px; font-size: 14px; background: #dcfce7; color: #166534; border: 1px solid #bbf7d0;">
          <strong>Dziękujemy za zgłoszenie!</strong> Dział handlowy Prescot LED skontaktuje się z Państwem niezwłocznie.
        </div>
      </form>
    </div>
  </div>

  <section style="margin-bottom: 40px;">
    <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 28px; color: var(--p-dark); margin-bottom: 8px;">Korzyści ze stałej współpracy B2B</h2>
      <p style="color: var(--p-text-muted); font-size: 15px;">Dostarczamy najwyższej klasy komponenty oświetleniowe wraz z pełnym wsparciem technicznym i logistycznym.</p>
    </div>

    <div class="p-benefits-grid">
      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h4>Rabaty Inwestycyjne</h4>
        <p>Przejrzyste progi rabatowe, stałe warunki handlowe oraz indywidualne wyceny dużych projektów komercyjnych.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
        </div>
        <h4>Wysyłka w 24h</h4>
        <p>Ponad 95% katalogowych taśm LED, zasilaczy i profili dostępnych od ręki w centralnym magazynie w Giżycku.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        </div>
        <h4>Wsparcie Inżynierskie</h4>
        <p>Doradztwo techniczne, obliczenia spadków napięć, dobór zasilaczy i systemów sterowania MiBoxer/DALI.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        </div>
        <h4>Materiały Marketingowe</h4>
        <p>Wzorniki taśm LED, ekspozytory handlowe, katalogi produktowe oraz pliki fotometryczne IES dla projektantów.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
        </div>
        <h4>Integracja XML / EDI</h4>
        <p>Automatyczny dostęp do baz produktowych, zdjęć w wysokiej rozdzielczości i aktualnych stanów magazynowych.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h4>Gwarancja Jakości</h4>
        <p>Nawet do 5 lat gwarancji na profesjonalne linie taśm LED Prescot COB oraz zasilacze przemysłowe.</p>
      </div>
    </div>
  </section>
</main>

<script>
document.getElementById('b2b-reg-form').addEventListener('submit', function(e) {
  e.preventDefault();
  document.getElementById('b2b-feedback').style.display = 'block';
  this.reset();
});
</script>
"""

wspol_html = make_b2b_page(
    title="Strefa B2B — Hurt & Współpraca Partnerska Prescot LED",
    h1_title="Strefa Partnerów B2B & Dystrybucja Prescot LED",
    eyebrow_text="Dla Profesjonalistów Branży Oświetleniowej"
)

with open(os.path.join(base_dir, "wspolpraca-b2b/index.html"), "w", encoding="utf-8") as f:
    f.write(wspol_html + footer_html + unified_dock)

dyst_html = make_b2b_page(
    title="Dystrybucja & Sieć Partnerska — Prescot LED",
    h1_title="Sieć Dystrybucji & Współpraca Hurtowa Prescot LED",
    eyebrow_text="Oficjalna Sieć Handlowa"
)

with open(os.path.join(base_dir, "dystrybucja/index.html"), "w", encoding="utf-8") as f:
    f.write(dyst_html + footer_html + unified_dock)

print("Updated wspolpraca-b2b and dystrybucja with 100vh Full-Screen Hero.")

# ==============================================================================
# 3. KONTAKT
# ==============================================================================
kontakt_html = """<!DOCTYPE html>
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
  <title>Kontakt — Prescot LED Centrala Giżycko</title>
  <style>
""" + common_css + """
  .p-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-bottom: 56px;
  }
  .p-card {
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 32px;
    box-shadow: var(--p-shadow-sm);
    transition: all 0.25s ease;
    display: flex;
    flex-direction: column;
  }
  .p-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--p-shadow-lg);
    border-color: var(--p-primary);
  }
  .p-card-icon {
    width: 50px;
    height: 50px;
    border-radius: 12px;
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
  }
  .p-card h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    color: var(--p-dark);
    margin-bottom: 12px;
  }
  .p-card p {
    color: var(--p-text-muted);
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 16px;
  }
  .p-card a.card-link {
    color: var(--p-primary);
    font-weight: 600;
    text-decoration: none;
    font-size: 14px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: auto;
  }
  .p-card a.card-link:hover { text-decoration: underline; }

  .p-form-box {
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 38px 32px;
    box-shadow: var(--p-shadow-md);
  }
  .p-form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  @media (max-width: 650px) {
    .p-form-grid { grid-template-columns: 1fr; }
  }
  .p-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .p-group.full { grid-column: 1 / -1; }
  .p-group label {
    font-size: 13px;
    font-weight: 600;
    color: var(--p-dark);
  }
  .p-group input, .p-group select, .p-group textarea {
    padding: 13px 16px;
    border: 1px solid var(--p-border);
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
    min-height: 120px;
  }
  </style>
</head>
<body>
""" + smart_logo_html + """

<!-- FULL-SCREEN 100VH HERO SLIDE -->
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/01/18.lobby_.webp');">
  <div class="p-full-hero-content">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      Jesteśmy do Twojej dyspozycji
    </div>
    <h1>Skontaktuj się z Centralą Prescot LED</h1>
    <p class="lead">Masz pytania techniczne, potrzebujesz wyceny inwestycyjnej lub chcesz nawiązać współpracę dystrybucyjną? Skontaktuj się bezpośrednio z naszym zespołem inżynierów i doradców handlowych w Giżycku.</p>
    <div class="p-hero-actions">
      <a href="#formularz-kontaktowy" class="p-btn p-btn-primary">
        Napisz do nas
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="tel:+48877776482" class="p-btn p-btn-outline">
        Zadzwoń: +48 87 777 64 82
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
    <span>Kontakt</span>
  </nav>

  <div class="p-cards-grid">
    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      </div>
      <h3>Siedziba &amp; Magazyn</h3>
      <p>PRESCOT sp. z o.o.<br>ul. Wileńska 1<br>11-500 Giżycko, Polska<br>NIP: 8451993424</p>
      <a href="#mapa-dojazdu" class="card-link">Zobacz mapę dojazdu &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      </div>
      <h3>Sekretariat &amp; Biuro</h3>
      <p>Poniedziałek – Piątek: 8:00 – 16:00<br>Tel: +48 87 428 21 18<br>E-mail: sekretariat@prescot.pl</p>
      <a href="mailto:sekretariat@prescot.pl" class="card-link">Napisz wiadomość &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </div>
      <h3>Dział Handlowy &amp; B2B</h3>
      <p>Wsparcie zamówień hurtowych, dystrybucji i wycen inwestycyjnych.<br>Tel: +48 87 777 64 82<br>E-mail: komponenty@prescot.pl</p>
      <a href="mailto:komponenty@prescot.pl" class="card-link">Skontaktuj się &rarr;</a>
    </div>
  </div>

  <div id="formularz-kontaktowy" class="p-form-box" style="margin-bottom: 56px;">
    <h2 style="font-family:'Outfit',sans-serif; font-size: 26px; color: var(--p-dark); margin-bottom: 8px;">Formularz kontaktowy</h2>
    <p style="color: var(--p-text-muted); font-size: 15px; margin-bottom: 28px;">Wypełnij poniższe pola. Nasi inżynierowie i doradcy odpowiedzą na Twoją wiadomość najszybciej jak to możliwe.</p>

    <form class="p-form-grid" id="contact-form-action" action="javascript:void(0);">
      <div class="p-group">
        <label for="c-name">Imię i nazwisko *</label>
        <input type="text" id="c-name" placeholder="np. Jan Kowalski" required>
      </div>

      <div class="p-group">
        <label for="c-email">Adres e-mail *</label>
        <input type="email" id="c-email" placeholder="twoj@email.pl" required>
      </div>

      <div class="p-group">
        <label for="c-phone">Numer telefonu</label>
        <input type="tel" id="c-phone" placeholder="+48 000 000 000">
      </div>

      <div class="p-group">
        <label for="c-dept">Dział docelowy</label>
        <select id="c-dept">
          <option value="sprzedaz">Dział Sprzedaży B2B &amp; Dystrybucja</option>
          <option value="techniczny">Wsparcie Techniczne &amp; Doradztwo LED</option>
          <option value="sekretariat">Sekretariat / Sprawy Ogólne</option>
          <option value="reklamacje">Serwis &amp; Reklamacje</option>
        </select>
      </div>

      <div class="p-group full">
        <label for="c-msg">Treść wiadomości *</label>
        <textarea id="c-msg" placeholder="W czym możemy pomóc? Opisz swoje zapytanie lub podaj specyfikację projektu..." required></textarea>
      </div>

      <div class="p-group full">
        <label style="display:flex; align-items:flex-start; gap:8px; font-size:12px; color:var(--p-text-muted); cursor:pointer;">
          <input type="checkbox" required style="margin-top:3px;">
          <span>Wyrażam zgodę na przetwarzanie moich danych osobowych przez PRESCOT sp. z o.o. w celu obsługi zapytania kontaktowego zgodnie z Polityką Prywatności.</span>
        </label>
      </div>

      <div class="p-group full">
        <button type="submit" class="p-btn p-btn-primary" style="justify-self:start;">
          Wyślij wiadomość &rarr;
        </button>
      </div>

      <div id="c-feedback" class="p-group full" style="display:none; padding: 14px 18px; border-radius: 8px; font-size: 14px; background: #dcfce7; color: #166534; border: 1px solid #bbf7d0;">
        <strong>Dziękujemy!</strong> Twoja wiadomość została pomyślnie wysłana. Skontaktujemy się z Tobą niezwłocznie.
      </div>
    </form>
  </div>

  <div id="mapa-dojazdu" style="border-radius: var(--p-radius); overflow: hidden; border: 1px solid var(--p-border); box-shadow: var(--p-shadow-sm); height: 420px; margin-bottom: 40px;">
    <iframe 
      title="Mapa Dojazdu Prescot LED Giżycko"
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2345.5034636923485!2d21.758416676991054!3d54.03859667249912!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46e166f272a7b67b%3A0xb35a3974c2d3c1eb!2sWile%C5%84ska%201%2C%2011-500%20Gi%C5%BCycko!5e0!3m2!1spl!2spl!4v1700000000000!5m2!1spl!2spl" 
      width="100%" 
      height="100%" 
      style="border:0;" 
      allowfullscreen="" 
      loading="lazy" 
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
  </div>
</main>

<script>
document.getElementById('contact-form-action').addEventListener('submit', function(e) {
  e.preventDefault();
  document.getElementById('c-feedback').style.display = 'block';
  this.reset();
});
</script>
"""

with open(os.path.join(base_dir, "kontakt/index.html"), "w", encoding="utf-8") as f:
    f.write(kontakt_html + footer_html + unified_dock)
print("Updated kontakt with 100vh Full-Screen Photo Hero.")

