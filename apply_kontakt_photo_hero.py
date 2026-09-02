# -*- coding: utf-8 -*-
import os

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

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

  /* TOPBAR: SCHODZI I CHOWA SIĘ NA GÓRZE PRZY SCROLLU */
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

  /* HERO ZE ZDJĘCIEM ARCHITEKTONICZNYM W TLE */
  .p-hero {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.82) 0%, rgba(30, 41, 59, 0.88) 100%), 
                url('/wp-content/uploads/2026/01/18.lobby_.webp') center/cover no-repeat;
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

  /* 3 KARTY KONTAKTOWE */
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

  /* FORMULARZ & MAPA */
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
    <span>Kontakt</span>
  </nav>

  <div class="p-hero">
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
        <label class="p-checkbox-label">
          <input type="checkbox" required>
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

with open(os.path.join(base_dir, "kontakt/index.html"), "w", encoding="utf-8") as f:
    f.write(kontakt_html + footer_html + unified_dock)
print("Updated kontakt/index.html with photo hero and non-sticky header.")

