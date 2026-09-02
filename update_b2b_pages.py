# -*- coding: utf-8 -*-
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

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

.prescot-main-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 40px 24px 80px 24px;
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

/* =========================================================
   B2B DUAL ACTION CARDS (EXACT MATCH MODAL & KONTAKT THEME)
   ========================================================= */
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

/* KARTA LEWA: LOGOWANIE (Styl z lewej kolorki - ciepły pomarańczowy akcent) */
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

/* KARTA PRAWA: FORMULARZ (Styl czysty slate z dopasowaną ramką) */
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

/* Delicate Benefits Section */
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

with open("/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

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

def generate_b2b_content(breadcrumb_label):
    return """
<main class="prescot-main-container">
  <nav class="prescot-breadcrumbs" aria-label="Okruszki">
    <a href="/">Strona główna</a>
    <span class="sep">/</span>
    <span>""" + breadcrumb_label + """</span>
  </nav>

  <!-- HERO SECTION -->
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

  <!-- B2B DUAL ACTION CARDS: LOGOWANIE (STYL Z LEWEJ KOLORKI) + REJESTRACJA (FORMULARZ) -->
  <div id="strefa-rejestracji" class="b2b-action-layout">
    
    <!-- LEWA KARTA: LOGOWANIE DO HURTOWNI (Styl z lewej kolorki - biała karta, pomarańczowy badge i ramka) -->
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

    <!-- PRAWA KARTA: REJESTRACJA / DOŁĄCZ (Formularz dla nowych partnerów) -->
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

  <!-- DELIKATNA SEKCJA KORZYŚCI ZE WSPÓŁPRACY B2B -->
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

# Write to dystrybucja/index.html
dyst_title = "<title>Dystrybucja & Program Partnerski B2B — Prescot LED</title>"
with open(os.path.join(base_dir, "dystrybucja/index.html"), "w", encoding="utf-8") as f:
    f.write(head_shared + dyst_title + shared_css + generate_b2b_content("Dystrybucja") + footer_html + shared_dock_and_scripts)
print("Updated dystrybucja/index.html.")

# Write to wspolpraca-b2b/index.html
wspol_title = "<title>Współpraca B2B & Strefa Hurtowa — Prescot LED</title>"
with open(os.path.join(base_dir, "wspolpraca-b2b/index.html"), "w", encoding="utf-8") as f:
    f.write(head_shared + wspol_title + shared_css + generate_b2b_content("Współpraca B2B") + footer_html + shared_dock_and_scripts)
print("Updated wspolpraca-b2b/index.html.")

