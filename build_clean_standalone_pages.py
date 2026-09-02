# -*- coding: utf-8 -*-
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# Shared Global Head Elements
head_shared = """<!DOCTYPE html>
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
"""

# Shared CSS Design System
shared_css = """
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
  --p-radius: 16px;
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
  padding-bottom: 90px; /* Space for floating dock */
}

/* Minimalist Topbar */
.prescot-topbar {
  background: #ffffff;
  border-bottom: 1px solid var(--p-border);
  padding: 16px 24px;
  position: sticky;
  top: 0;
  z-index: 100;
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

/* Layout Container */
.prescot-main-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 40px 24px 80px 24px;
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
  opacity: 0.4;
}

/* Hero Section */
.p-hero {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: #ffffff;
  border-radius: var(--p-radius);
  padding: 56px 44px;
  margin-bottom: 48px;
  box-shadow: var(--p-shadow-lg);
  position: relative;
  overflow: hidden;
}
.p-hero::after {
  content: '';
  position: absolute;
  top: -40%;
  right: -10%;
  width: 380px;
  height: 380px;
  background: radial-gradient(circle, rgba(229, 89, 51, 0.28) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}
.p-hero-eyebrow {
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
  margin-bottom: 18px;
  border: 1px solid rgba(229, 89, 51, 0.35);
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
  color: #cbd5e1;
  max-width: 800px;
  line-height: 1.65;
  margin-bottom: 28px;
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
  background: transparent;
  color: #ffffff !important;
  border: 1px solid rgba(255, 255, 255, 0.35);
}
.p-btn-outline:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: #ffffff;
}

/* Section Headings */
.p-section-header {
  margin-bottom: 32px;
}
.p-section-header h2 {
  font-family: 'Outfit', sans-serif;
  font-size: 28px;
  color: var(--p-dark);
  margin-bottom: 8px;
}
.p-section-header p {
  color: var(--p-text-muted);
  font-size: 15px;
}

/* Feature Cards Grid */
.p-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-bottom: 56px;
}
.p-card {
  background: var(--p-card-bg);
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
.p-card a.card-link:hover {
  text-decoration: underline;
}

/* Form Styles */
.p-form-box {
  background: var(--p-card-bg);
  border: 1px solid var(--p-border);
  border-radius: var(--p-radius);
  padding: 36px;
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
.p-group.full {
  grid-column: 1 / -1;
}
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

/* Calculator Grid */
.calc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-bottom: 32px;
}
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

/* Search Box & Filters */
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
  font-family: inherit;
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
  font-family: inherit;
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
  font-family: inherit;
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
</style>
</head>
<body>
<!-- MINIMALIST TOPBAR -->
<header class="prescot-topbar">
  <div class="prescot-topbar-inner">
    <a href="/" class="prescot-logo-link" title="Prescot LED Strona Główna">
      <img src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg" alt="Prescot LED">
    </a>
    <span class="prescot-topbar-tagline">Polski Producent Oświetlenia LED &bull; Giżycko</span>
  </div>
</header>
"""

# Shared Footer & Dock
with open("/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

# Make sure footer logo has src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"
footer_html = footer_html.replace('data-src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"', 'src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"')
footer_html = footer_html.replace('src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs="', 'src="/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"')

shared_dock_and_scripts = """
<!-- GLOBAL MENU START -->
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

  <a href="/dystrybucja/" class="dock-item" data-tooltip="Dystrybucja" aria-label="Dystrybucja">
    <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M128 352H32c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32zm-24-80h192v48h48v-48h192v48h48v-57.59c0-21.17-17.23-38.41-38.41-38.41H344v-64h40c17.67 0 32-14.33 32-32V32c0-17.67-14.33-32-32-32H256c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h40v64H94.41C73.23 224 56 241.23 56 262.41V320h48v-48zm264 80h-96c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32zm240 0h-96c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h96c17.67 0 32-14.33 32-32v-96c0-17.67-14.33-32-32-32z"/>
    </svg>
  </a>

  <a href="/baza-wiedzy/" class="dock-item" data-tooltip="Baza Wiedzy" aria-label="Baza Wiedzy & FAQ">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M256 32C132.3 32 32 132.3 32 256s100.3 224 224 224 224-100.3 224-224S379.7 32 256 32zm0 376c-17.7 0-32-14.3-32-32s14.3-32 32-32 32 14.3 32 32-14.3 32-32 32zm42.7-142.1c-13.8 11.2-26.7 21.6-26.7 46.1v10c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-14c0-38.4 22.8-56.9 44.4-74.4 14.1-11.4 27.6-22.3 27.6-39.6 0-21.2-18.7-36-44-36-24.6 0-41.9 14.2-46.7 32.5-2.2 8.5-10.4 13.9-19.1 12.3l-30.8-5.6c-9.1-1.7-14.8-10.7-12.4-19.7C180.7 132.2 214.2 104 256 104c53 0 96 34.3 96 82 0 35.8-21.7 61.2-53.3 83.9z"/>
    </svg>
  </a>

  <a href="https://prescot.abstore.pl/client/loginorcreate/login" class="dock-item b2b-trigger" data-tooltip="Strefa B2B" aria-label="B2B">
    <svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M576 216v16c0 13.255-10.745 24-24 24h-8l-26.113 182.788C514.509 462.435 494.257 480 470.37 480H105.63c-23.887 0-44.139-17.565-47.518-41.212L32 256h-8c-13.255 0-24-10.745-24-24v-16c0-13.255 10.745-24 24-24h67.341l106.78-146.821c10.395-14.292 30.407-17.453 44.701-7.058 14.293 10.395 17.453 30.408 7.058 44.701L170.477 192h235.046L326.12 82.821c-10.395-14.292-7.234-34.306 7.059-44.701 14.291-10.395 34.306-7.235 44.701 7.058L484.659 192H552c13.255 0 24 10.745 24 24zM312 392V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm112 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24zm-224 0V280c0-13.255-10.745-24-24-24s-24 10.745-24 24v112c0 13.255 10.745 24 24 24s24-10.745 24-24z"/>
    </svg>
  </a>

  <a href="/kontakt/" class="dock-item" data-tooltip="Kontakt" aria-label="Kontakt">
    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M493.4 24.6l-104-24c-11.3-2.6-22.9 3.3-27.5 14l-48 112c-4.2 9.8-1.4 21.3 6.9 28l60.6 49.6c-36 76.7-98.9 140.5-177.2 177.2l-49.6-60.6c-6.8-8.3-18.2-11.1-28-6.9l-112 48C4.1 366.5-1.8 378.1.8 389.4l24 104C27.3 504.2 36.7 512 48 512c256.1 0 464-207.5 464-464 0-11.2-7.7-21-18.6-23.4z"/>
    </svg>
  </a>

  <a href="https://prescot.com.pl/" class="dock-item" data-tooltip="Sklep B2C" aria-label="Sklep B2C" target="_blank">
    <svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg">
      <path fill="currentColor" d="M528.12 301.319l47.273-208C578.806 78.301 567.391 64 551.99 64H159.208l-9.166-44.81C147.758 8.021 137.93 0 126.529 0H24C10.745 0 0 10.745 0 24v16c0 13.255 10.745 24 24 24h69.883l70.248 343.435C147.325 417.1 136 435.222 136 456c0 30.928 25.072 56 56 56s56-25.072 56-56c0-15.674-6.447-29.835-16.824-40h209.647C430.447 426.165 424 440.326 424 456c0 30.928 25.072 56 56 56s56-25.072 56-56c0-22.172-12.888-41.332-31.579-50.405l5.517-24.276c3.413-15.018-8.002-29.319-23.403-29.319H218.117l-6.545-32h293.145c11.206 0 20.92-7.754 23.403-18.681z"/>
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

# ==============================================================================
# 1. BAZA WIEDZY PAGE
# ==============================================================================
bw_title = "<title>Baza Wiedzy & Kalkulator LED — Prescot LED</title>"
bw_body = """
<main class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Baza Wiedzy & FAQ</span>
  </nav>

  <div class="p-hero">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      Oficjalne Kompendium Inżynieryjne
    </div>
    <h1>Baza Wiedzy & Kalkulator Zasilania LED</h1>
    <p class="lead">Profesjonalna wiedza techniczna dla instalatorów, projektantów i dystrybutorów. Poznaj fizykę taśm COB/SMD, zasady eliminacji spadków napięć, dobór zasilaczy i automatykę sterowania oświetleniem.</p>
    <div class="p-hero-actions">
      <a href="#kalkulator" class="p-btn p-btn-primary">
        Kalkulator Zasilania & Spadków
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="#faq" class="p-btn p-btn-outline">Przeglądaj Zagadnienia FAQ</a>
    </div>
  </div>

  <!-- KALKULATOR SECTION -->
  <section id="kalkulator" class="p-form-box" style="margin-bottom: 56px;">
    <div class="p-section-header">
      <h2>Interaktywny Kalkulator Zasilania i Spadków Napięcia LED</h2>
      <p>Wprowadź parametry instalacji, aby natychmiast obliczyć minimalną moc zasilacza (z buforem +20%), pobór prądu i spadek napięcia na przewodzie.</p>
    </div>

    <div class="calc-grid">
      <div class="p-group">
        <label for="tape-power">Moc jednostkowa taśmy LED: <span id="tape-power-val" style="color:var(--p-primary); font-weight:700;">9.6 W/m</span></label>
        <select id="tape-power">
          <option value="4.8">4.8 W/m — Dekoracyjna SMD (300 LED)</option>
          <option value="9.6" selected>9.6 W/m — Standardowa Akcentowa SMD (600 LED)</option>
          <option value="10.0">10.0 W/m — Prescot COB Slim (Ciągła linia światła)</option>
          <option value="14.4">14.4 W/m — Główna Użytkowa SMD (60 LED/m 5050)</option>
          <option value="15.0">15.0 W/m — Prescot COB High Lumen CRI>90</option>
          <option value="19.2">19.2 W/m — Super Jasna SMD (120 LED/m 2835)</option>
          <option value="custom">Wpisz własną moc...</option>
        </select>
        <input type="number" id="custom-power-inp" placeholder="Wpisz moc W/m" style="display:none; margin-top:8px;" step="0.1" min="1" max="100">
      </div>

      <div class="p-group">
        <label for="tape-length">Długość odcinka taśmy: <span id="tape-length-val" style="color:var(--p-primary); font-weight:700;">5 m</span></label>
        <input type="number" id="tape-length" value="5" min="0.5" max="100" step="0.5">
      </div>

      <div class="p-group">
        <label for="tape-voltage">Napięcie zasilania instalacji:</label>
        <select id="tape-voltage">
          <option value="12">12V DC (Krótkie odcinki do 5m)</option>
          <option value="24" selected>24V DC (Standard Prescot — odcinki do 10m)</option>
          <option value="48">48V DC (Długie ciągi do 25-50m)</option>
        </select>
      </div>

      <div class="p-group">
        <label for="wire-len">Długość kabla (zasilacz &rarr; taśma):</label>
        <input type="number" id="wire-len" value="3" min="0.1" max="50" step="0.5">
      </div>

      <div class="p-group">
        <label for="wire-section">Przekrój żyły przewodu (Cu):</label>
        <select id="wire-section">
          <option value="0.5">0.50 mm²</option>
          <option value="0.75" selected>0.75 mm² (Standard)</option>
          <option value="1.0">1.00 mm²</option>
          <option value="1.5">1.50 mm² (Zalecany)</option>
          <option value="2.5">2.50 mm² (Magistrala B2B)</option>
        </select>
      </div>

      <div class="p-group">
        <label for="feed-mode">Sposób wpięcia zasilania:</label>
        <select id="feed-mode">
          <option value="single" selected>Jednostronne (Początek taśmy)</option>
          <option value="double">Obustronne (Z obu stron odcinka)</option>
          <option value="loop">Pętla magistralna (Wpięcia co 5m)</option>
        </select>
      </div>
    </div>

    <!-- WYNIKI KALKULATORA -->
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
        <span class="calc-res-label">Prąd roboczy instalacji</span>
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
  </section>

  <!-- FAQ SECTION -->
  <section id="faq">
    <div class="p-section-header">
      <h2>Baza Wiedzy Inżynierskiej & FAQ</h2>
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
  </section>
</main>

<script>
(function() {
  // CALCULATOR LOGIC
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

    const totalWireLen = wireLen * 2;
    const wireResistance = (0.0175 * totalWireLen) / wireSection;
    
    let effectiveCurrent = current;
    if (feedMode === 'double') effectiveCurrent = current / 2;
    if (feedMode === 'loop') effectiveCurrent = current / 2.5;

    const vDrop = effectiveCurrent * wireResistance;
    const vDropPercent = (vDrop / voltage) * 100;

    resNominal.innerText = nominalPower.toFixed(1) + ' W';
    resPsu.innerText = 'min. ' + Math.ceil(minPsuPower) + ' W';
    resCurrent.innerText = current.toFixed(2) + ' A';
    resVoltageDrop.innerText = vDrop.toFixed(2) + ' V (' + vDropPercent.toFixed(1) + '%)';

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

  // FAQ ACCORDION LOGIC
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  // FAQ FILTER PILLS
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

  // FAQ SEARCH
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
    f.write(head_shared + bw_title + shared_css + bw_body + footer_html + shared_dock_and_scripts)
print("1. Baza Wiedzy created.")

# ==============================================================================
# 2. DYSTRYBUCJA PAGE
# ==============================================================================
dyst_title = "<title>Dystrybucja & Program Partnerski B2B — Prescot LED</title>"
dyst_body = """
<main class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Dystrybucja</span>
  </nav>

  <div class="p-hero">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      Oficjalna Sieć Dystrybucji B2B
    </div>
    <h1>Program Partnerski & Dystrybucja Prescot LED</h1>
    <p class="lead">Dołącz do grona autoryzowanych dystrybutorów, hurtowni elektrotechnicznych i certyfikowanych instalatorów. Zyskaj bezpośredni dostęp do magazynu centralnego, indywidualnych progów rabatowych i pełnego wsparcia inżynieryjnego.</p>
    <div class="p-hero-actions">
      <a href="#formularz-b2b" class="p-btn p-btn-primary">
        Zgłoś firmę do programu B2B
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="https://prescot.abstore.pl/client/loginorcreate/login" class="p-btn p-btn-outline" target="_blank">Platforma Zamówień B2B (Logowanie)</a>
    </div>
  </div>

  <!-- 4 FILARY PARTNERSTWA -->
  <div class="p-section-header">
    <h2>Dlaczego warto współpracować z Prescot LED?</h2>
    <p>Standardy logistyczne, technologiczne i handlowe stworzone z myślą o profesjonalistach.</p>
  </div>

  <div class="p-cards-grid">
    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
      </div>
      <h3>Wysyłka 24h z Centrali</h3>
      <p>Centrum logistyczne w Giżycku utrzymuje stałe stany magazynowe ponad 100 000 metrów taśm LED, zasilaczy i profili. Zamówienia złożone do 13:00 wysyłamy tego samego dnia.</p>
      <a href="#formularz-b2b" class="card-link">Sprawdź warunki dostaw &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      </div>
      <h3>Dedykowane Rabaty B2B</h3>
      <p>Przejrzyste progi rabatowe dopasowane do skali Twojej działalności (instalator, projektant, hurtownia). Kredyt kupiecki i odroczone terminy płatności dla stałych partnerów.</p>
      <a href="#formularz-b2b" class="card-link">Zyskaj cennik hurtowy &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
      </div>
      <h3>Wsparcie Inżynieryjne & Pliki IES</h3>
      <p>Nasz dział techniczny bezpłatnie wykonuje kalkulacje oświetleniowe w DIALux, dobiera zasilanie i dostarcza kompletne karty katalogowe, certyfikaty CE/RoHS oraz pliki fotometryczne.</p>
      <a href="/baza-wiedzy/" class="card-link">Przejdź do bazy wiedzy &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
      </div>
      <h3>Wzorniki & Standy Ekspozycyjne</h3>
      <p>Dla salonów sprzedaży i biur projektowych zapewniamy eleganckie ekspozytory ścienne, walizki demonstracyjne z taśmami COB/SMD oraz wzorniki profili aluminiowych.</p>
      <a href="#formularz-b2b" class="card-link">Zamów stand pokazowy &rarr;</a>
    </div>
  </div>

  <!-- FORMULARZ DLA DYSTRYBUTORÓW -->
  <div id="formularz-b2b" class="p-form-box" style="margin-bottom: 60px;">
    <div class="p-section-header">
      <h2>Zgłoszenie do Sieci Partnerskiej B2B</h2>
      <p>Wypełnij krótki formularz rejestracyjny. Nasz opiekun handlowy skontaktuje się z Tobą w ciągu 4 godzin roboczych w celu aktywacji konta hurtowego.</p>
    </div>

    <form class="p-form-grid" id="dyst-register-form" action="javascript:void(0);">
      <div class="p-group">
        <label for="d-company">Nazwa firmy *</label>
        <input type="text" id="d-company" placeholder="np. Elektro-Instal Sp. z o.o." required>
      </div>

      <div class="p-group">
        <label for="d-nip">Numer NIP *</label>
        <input type="text" id="d-nip" placeholder="np. 8451993424" required>
      </div>

      <div class="p-group">
        <label for="d-name">Imię i nazwisko osoby kontaktowej *</label>
        <input type="text" id="d-name" placeholder="np. Marek Wiśniewski" required>
      </div>

      <div class="p-group">
        <label for="d-phone">Numer telefonu *</label>
        <input type="tel" id="d-phone" placeholder="+48 000 000 000" required>
      </div>

      <div class="p-group">
        <label for="d-email">Firmowy adres e-mail *</label>
        <input type="email" id="d-email" placeholder="kontakt@twojafirma.pl" required>
      </div>

      <div class="p-group">
        <label for="d-type">Profil działalności</label>
        <select id="d-type">
          <option value="instalator">Instalator / Elektryk / Montażysta</option>
          <option value="projektant">Biuro Architektoniczne / Projektant Wnętrz</option>
          <option value="hurtownia">Hurtownia Elektrotechniczna / Sklep Oświetleniowy</option>
          <option value="producent">Producent mebli / reklam / zabudów</option>
          <option value="inny">Inny profil działalności</option>
        </select>
      </div>

      <div class="p-group full">
        <label for="d-notes">Uwagi / Oczekiwany asortyment (opcjonalnie)</label>
        <textarea id="d-notes" placeholder="Opisz swoje potrzeby, np. zapotrzebowanie na taśmy COB 24V, zasilacze meblowe, próbki materiałowe..."></textarea>
      </div>

      <div class="p-group full">
        <label class="p-checkbox-label">
          <input type="checkbox" required>
          <span>Wyrażam zgodę na przetwarzanie danych firmy w celu weryfikacji i założenia konta w programie partnerskim PRESCOT sp. z o.o. zgodnie z Polityką Prywatności.</span>
        </label>
      </div>

      <div class="p-group full">
        <button type="submit" class="p-btn p-btn-primary" style="justify-self:start;">
          Wyślij zgłoszenie partnerskie
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
        </button>
      </div>

      <div id="d-feedback" class="p-group full" style="display:none; padding:14px 18px; border-radius:8px; font-size:14px; background:#dcfce7; color:#166534; border:1px solid #bbf7d0;">
        <strong>Dziękujemy!</strong> Zgłoszenie partnerskie zostało pomyślnie przesłane. Dział handlowy Prescot LED skontaktuje się z Państwem niezwłocznie.
      </div>
    </form>
  </div>
</main>

<script>
document.getElementById('dyst-register-form').addEventListener('submit', function(e) {
  e.preventDefault();
  document.getElementById('d-feedback').style.display = 'block';
  this.reset();
});
</script>
"""

with open(os.path.join(base_dir, "dystrybucja/index.html"), "w", encoding="utf-8") as f:
    f.write(head_shared + dyst_title + shared_css + dyst_body + footer_html + shared_dock_and_scripts)
print("2. Dystrybucja created.")

# ==============================================================================
# 3. KONTAKT PAGE
# ==============================================================================
kt_title = "<title>Kontakt — Prescot LED Centrala Giżycko</title>"
kt_body = """
<main class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>Kontakt</span>
  </nav>

  <div class="p-hero">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      Oficjalny Kontakt & Centrala
    </div>
    <h1>Skontaktuj się z zespołem Prescot LED</h1>
    <p class="lead">Nasi doradcy techniczno-handlowi i inżynierowie oświetlenia są do Twojej dyspozycji. Zapewniamy pełne wsparcie inwestycyjne, wyceny hurtowe oraz bezpośrednią obsługę magazynową.</p>
    <div class="p-hero-actions">
      <a href="#formularz-kontaktowy" class="p-btn p-btn-primary">
        Napisz wiadomość
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
      <a href="tel:+48877776482" class="p-btn p-btn-outline">Zadzwoń do działu sprzedaży</a>
    </div>
  </div>

  <!-- 3 KARTY KONTAKTOWE -->
  <div class="p-cards-grid">
    <!-- KARTA 1: SIEDZIBA -->
    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      </div>
      <h3>Siedziba & Magazyn Główny</h3>
      <p>
        <strong>PRESCOT sp. z o.o.</strong><br>
        ul. Wileńska 1<br>
        11-500 Giżycko, Polska<br>
        <span style="font-size: 12px; color: var(--p-text-muted);">NIP: 8451993424 | KRS: 0000882894</span>
      </p>
      <p style="margin-bottom:0; font-size:13px;">
        <strong>Godziny pracy:</strong><br>
        Pn – Pt: 07:30 – 16:30
      </p>
    </div>

    <!-- KARTA 2: SEKRETARIAT -->
    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      </div>
      <h3>Biuro & Sekretariat</h3>
      <p>Obsługa korespondencji administracyjnej, formalności spółki oraz ogólne zapytania firmowe.</p>
      <p>
        <strong>Telefon:</strong> <a href="tel:+48874282118" style="color:var(--p-dark); font-weight:600; text-decoration:none;">+48 87 428 21 18</a><br>
        <strong>E-mail:</strong> <a href="mailto:sekretariat@prescot.pl" style="color:var(--p-primary); text-decoration:none; font-weight:600;">sekretariat@prescot.pl</a>
      </p>
      <a href="mailto:sekretariat@prescot.pl" class="card-link">Napisz do sekretariatu &rarr;</a>
    </div>

    <!-- KARTA 3: SPRZEDAŻ B2B -->
    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </div>
      <h3>Dział Handlowy & B2B</h3>
      <p>Wyceny inwestycyjne, obsługa hurtowa, doradztwo techniczne w doborze taśm i zasilaczy.</p>
      <p>
        <strong>Telefon:</strong> <a href="tel:+48877776482" style="color:var(--p-dark); font-weight:600; text-decoration:none;">+48 87 777 64 82</a><br>
        <strong>E-mail:</strong> <a href="mailto:komponenty@prescot.pl" style="color:var(--p-primary); text-decoration:none; font-weight:600;">komponenty@prescot.pl</a>
      </p>
      <a href="mailto:komponenty@prescot.pl" class="card-link">Skontaktuj się z doradcą &rarr;</a>
    </div>
  </div>

  <!-- FORMULARZ & MAPA -->
  <div id="formularz-kontaktowy" style="display:grid; grid-template-columns:1.2fr 0.8fr; gap:32px; margin-bottom:60px;">
    <!-- FORM BOX -->
    <div class="p-form-box">
      <div class="p-section-header">
        <h2>Wyślij zapytanie handlowe</h2>
        <p>Wypełnij formularz — nasz doradca odpowie najszybciej jak to możliwe.</p>
      </div>

      <form class="p-form-grid" id="main-contact-form" action="javascript:void(0);">
        <div class="p-group">
          <label for="c-name">Imię i nazwisko / Firma *</label>
          <input type="text" id="c-name" placeholder="np. Jan Kowalski" required>
        </div>
        <div class="p-group">
          <label for="c-nip">NIP (dla firm B2B)</label>
          <input type="text" id="c-nip" placeholder="np. 8451993424">
        </div>
        <div class="p-group">
          <label for="c-email">Adres e-mail *</label>
          <input type="email" id="c-email" placeholder="twoj-email@firma.pl" required>
        </div>
        <div class="p-group">
          <label for="c-phone">Numer telefonu *</label>
          <input type="tel" id="c-phone" placeholder="+48 000 000 000" required>
        </div>
        <div class="p-group full">
          <label for="c-dept">Dział docelowy</label>
          <select id="c-dept">
            <option value="sprzedaz">Dział Sprzedaży Hurtowej i Współpracy B2B</option>
            <option value="techniczne">Doradztwo Techniczne i Dobór Komponentów LED</option>
            <option value="zamowienia">Logistyka, Realizacja Zamówień i Magazyn</option>
            <option value="inne">Inny temat / Zapytanie ogólne</option>
          </select>
        </div>
        <div class="p-group full">
          <label for="c-msg">Wiadomość / Zestawienie materiałowe *</label>
          <textarea id="c-msg" placeholder="Wpisz treść zapytania lub specyfikację projektu..." required></textarea>
        </div>
        <div class="p-group full">
          <label class="p-checkbox-label">
            <input type="checkbox" required>
            <span>Wyrażam zgodę na przetwarzanie danych osobowych w celu obsługi zapytania zgodnie z Polityką Prywatności.</span>
          </label>
        </div>
        <div class="p-group full">
          <button type="submit" class="p-btn p-btn-primary" style="justify-self:start;">
            Wyślij wiadomość
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          </button>
        </div>
        <div id="c-feedback" class="p-group full" style="display:none; padding:14px 18px; border-radius:8px; font-size:14px; background:#dcfce7; color:#166534; border:1px solid #bbf7d0;">
          <strong>Dziękujemy!</strong> Wiadomość została pomyślnie wysłana. Skontaktujemy się z Państwem niezwłocznie.
        </div>
      </form>
    </div>

    <!-- MAP BOX -->
    <div class="p-form-box" style="padding:0; overflow:hidden; display:flex; flex-direction:column;">
      <iframe style="width:100%; height:320px; border:none;" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2342.348614488344!2d21.761278177114674!3d54.041697972498775!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46e16a247ea762a5%3A0x6d88b48858a74e50!2sWile%C5%84ska%201%2C%2011-500%20Gi%C5%BCycko!5e0!3m2!1spl!2spl!4v1710000000000!5m2!1spl!2spl" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      <div style="padding:24px;">
        <h4 style="font-family:'Outfit',sans-serif; font-size:18px; color:var(--p-dark); margin-bottom:8px;">Centrala & Magazyn Giżycko</h4>
        <p style="font-size:13px; color:var(--p-text-muted); line-height:1.6; margin-bottom:12px;">
          ul. Wileńska 1, 11-500 Giżycko<br>
          Dostępny wygodny parking dla instalatorów i rampa rozładunkowa dla pojazdów dostawczych B2B.
        </p>
        <span style="font-size:12px; font-weight:700; color:var(--p-primary); text-transform:uppercase; letter-spacing:0.5px;">Odbiór osobisty: Pn–Pt 07:30 – 16:30</span>
      </div>
    </div>
  </div>
</main>

<style>
@media (max-width: 900px) {
  #formularz-kontaktowy { grid-template-columns: 1fr !important; }
}
</style>

<script>
document.getElementById('main-contact-form').addEventListener('submit', function(e) {
  e.preventDefault();
  document.getElementById('c-feedback').style.display = 'block';
  this.reset();
});
</script>
"""

with open(os.path.join(base_dir, "kontakt/index.html"), "w", encoding="utf-8") as f:
    f.write(head_shared + kt_title + shared_css + kt_body + footer_html + shared_dock_and_scripts)
print("3. Kontakt created.")

