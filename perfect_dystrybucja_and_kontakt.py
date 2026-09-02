# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
DARK_LOGO = "/wp-content/uploads/2025/12/PRESCOT_logo-podstawowe.svg"

footer_path = "/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html"
with open(footer_path, "r", encoding="utf-8") as f:
    footer_html = f.read()

# Common Dystrybucja & B2B Content
def generate_dystrybucja_html(is_dystrybucja=True):
    page_title = "Dystrybucja B2B & Współpraca Handlowa — Prescot LED"
    h1_title = "Dystrybucja & Strefa Partnera B2B"
    lead_text = "Dołącz do autoryzowanej sieci dystrybucji Prescot LED. Zapewniamy wysokie rabaty inwestycyjne, błyskawiczną wysyłkę z magazynu centralnego w Giżycku oraz dedykowanego doradcę technicznego."

    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/wp-content/uploads/2025/09/cropped-favicon-1-32x32.png" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Krona+One&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/prescot-global.css?v=20260901-dystrybucja-v4">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <title>{page_title}</title>
  <style>
  :root {{
    --p-primary: #e55933;
    --p-primary-hover: #c94622;
    --p-dark: #0f172a;
    --p-dark-soft: #1e293b;
    --p-text: #212a35;
    --p-text-muted: #64748b;
    --p-bg: #f8fafc;
    --p-card: #ffffff;
    --p-border: #e2e8f0;
    --p-radius: 20px;
    --p-radius-sm: 12px;
    --p-shadow-sm: 0 2px 8px rgba(0,0,0,0.04);
    --p-shadow-md: 0 12px 30px -10px rgba(0,0,0,0.08);
    --p-shadow-lg: 0 20px 45px -12px rgba(15,23,42,0.12);
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--p-text);
    background: var(--p-bg);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding-bottom: 90px;
  }}

  /* FULL-SCREEN 100VH HERO SLIDE */
  .p-full-hero {{
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
  }}
  .p-full-hero::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.65) 0%, rgba(15, 23, 42, 0.88) 100%);
    z-index: 1;
  }}
  .p-full-hero-content {{
    position: relative;
    z-index: 2;
    max-width: 920px;
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .p-hero-eyebrow {{
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
  }}
  .p-full-hero h1 {{
    font-family: 'Outfit', sans-serif;
    font-size: clamp(34px, 4.5vw, 54px);
    color: #ffffff;
    margin-bottom: 20px;
    line-height: 1.18;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.4);
  }}
  .p-full-hero p.lead {{
    font-size: clamp(16px, 1.9vw, 19px);
    color: #e2e8f0;
    max-width: 820px;
    line-height: 1.65;
    margin-bottom: 32px;
    text-shadow: 0 1px 4px rgba(0,0,0,0.4);
  }}
  .p-hero-actions {{
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    justify-content: center;
  }}

  .p-hero-arrow-down {{
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
  }}
  .p-hero-arrow-down:hover {{ opacity: 1; color: #ff8a65; }}
  .p-arrow-icon {{
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
  }}
  @keyframes pBounce {{
    0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
    40% {{ transform: translateY(-10px); }}
    60% {{ transform: translateY(-5px); }}
  }}

  /* TREŚĆ PONIŻEJ HERO */
  .prescot-main-container {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 60px 24px 80px 24px;
  }}
  .prescot-breadcrumbs {{
    font-size: 13px;
    color: var(--p-text-muted);
    margin-bottom: 32px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .prescot-breadcrumbs a {{ color: var(--p-text-muted); text-decoration: none; }}
  .prescot-breadcrumbs a:hover {{ color: var(--p-primary); }}
  .prescot-breadcrumbs .sep {{ opacity: 0.4; }}

  .b2b-action-grid {{
    display: grid;
    grid-template-columns: 1fr 1.15fr;
    gap: 32px;
    margin-bottom: 70px;
  }}
  @media (max-width: 880px) {{
    .b2b-action-grid {{ grid-template-columns: 1fr; }}
  }}

  .b2b-login-box {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: var(--p-radius);
    padding: 42px 36px;
    color: #ffffff;
    box-shadow: var(--p-shadow-lg);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: 1px solid rgba(229, 89, 51, 0.3);
  }}
  .b2b-login-box h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    margin-bottom: 12px;
    color: #ffffff;
    letter-spacing: -0.02em;
  }}
  .b2b-login-box p {{
    color: #94a3b8;
    font-size: 14.5px;
    line-height: 1.6;
    margin-bottom: 24px;
  }}

  .b2b-form-box {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 42px 36px;
    box-shadow: var(--p-shadow-md);
  }}
  .b2b-form-box h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    color: var(--p-dark);
    margin-bottom: 8px;
    letter-spacing: -0.02em;
  }}
  .b2b-form-box p.form-sub {{
    color: var(--p-text-muted);
    font-size: 14.5px;
    margin-bottom: 24px;
  }}

  .p-form-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }}
  @media (max-width: 550px) {{
    .p-form-grid {{ grid-template-columns: 1fr; }}
  }}
  .p-group {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .p-group.full {{ grid-column: 1 / -1; }}
  .p-group label {{
    font-size: 13px;
    font-weight: 700;
    color: var(--p-dark);
  }}
  .p-group input, .p-group select, .p-group textarea {{
    padding: 13px 16px;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius-sm);
    font-size: 14px;
    background: #f8fafc;
    color: var(--p-dark);
    outline: none;
    font-family: inherit;
    transition: all 0.2s;
  }}
  .p-group input:focus, .p-group select:focus, .p-group textarea:focus {{
    border-color: var(--p-primary);
    background: #ffffff;
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.12);
  }}
  .p-group textarea {{
    resize: vertical;
    min-height: 100px;
  }}

  /* BENEFITS GRID */
  .p-benefits-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
    margin-bottom: 50px;
  }}
  .p-benefit-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 18px;
    padding: 30px;
    box-shadow: var(--p-shadow-sm);
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .p-benefit-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--p-shadow-lg);
    border-color: var(--p-primary);
  }}
  .p-benefit-icon {{
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 18px;
  }}
  .p-benefit-card h4 {{
    font-family: 'Outfit', sans-serif;
    font-size: 19px;
    font-weight: 700;
    color: var(--p-dark);
    margin-bottom: 8px;
  }}
  .p-benefit-card p {{
    color: var(--p-text-muted);
    font-size: 14px;
    line-height: 1.6;
  }}
  </style>
</head>
<body>
<!-- SMART LOGO: TYLKO W SEKCJI HERO -->
<div class="prescot-smart-logo">
  <a href="/" title="Prescot LED Strona Główna">
    <img src="/wp-content/uploads/2025/12/biale-z-kolorem.svg" alt="Prescot LED">
  </a>
</div>

<!-- FULL-SCREEN 100VH HERO SLIDE -->
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/02/aerial-drone-shot-of-a-modern-building-facade-illu-2024-08-23-14-38-48-utc-e1772569546453.webp');">
  <div class="p-full-hero-content">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7.5" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
      Strefa B2B & Dystrybucja
    </div>
    <h1>{h1_title}</h1>
    <p class="lead">{lead_text}</p>
    <div class="p-hero-actions">
      <a href="#rejestracja-b2b" class="p-btn p-btn-primary">
        Dołącz do sieci partnerskiej
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
      <a href="#korzysci-b2b" class="p-btn p-btn-outline">
        Poznaj warunki handlowe ↓
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
    <span>Dystrybucja & B2B</span>
  </nav>

  <!-- MODUŁ AKCJI B2B -->
  <div class="b2b-action-grid" id="rejestracja-b2b">
    <!-- PANEL LOGOWANIA B2B -->
    <div class="b2b-login-box">
      <div>
        <div style="font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:#ff8a65; margin-bottom:8px;">
          Dla Zarejestrowanych Partnerów
        </div>
        <h3>Portal Hurtowy B2B</h3>
        <p>Posiadasz już konto hurtowe w systemie Prescot? Zaloguj się, aby uzyskać dostęp do swoich rabatów kontraktowych, stanów magazynowych live oraz integracji XML/EDI.</p>
        
        <form action="javascript:void(0);" method="POST" style="display:flex; flex-direction:column; gap:12px; margin-bottom: 24px;">
          <input type="email" placeholder="Login / E-mail firmowy" maxlength="100" autocomplete="username" required style="padding:13px 16px; border-radius:10px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:#fff; outline:none;">
          <input type="password" placeholder="Hasło" maxlength="64" autocomplete="current-password" required style="padding:13px 16px; border-radius:10px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:#fff; outline:none;">
          <button type="submit" class="p-btn p-btn-primary" style="width:100%; justify-content:center; margin-top:4px;">
            Zaloguj się do platformy B2B &rarr;
          </button>
        </form>
      </div>

      <div style="font-size:12.5px; color:#94a3b8; border-top:1px solid rgba(255,255,255,0.1); padding-top:16px;">
        Zapomniałeś hasła? Skontaktuj się ze swoim opiekunem: <a href="mailto:komponenty@prescot.pl" style="color:#ff8a65; text-decoration:none;">komponenty@prescot.pl</a>
      </div>
    </div>

    <!-- FORMULARZ REJESTRACJI PARTNERA (BEZPIECZNY & ZWALIDOWANY) -->
    <div class="b2b-form-box">
      <h3>Dołącz do sieci partnerskiej Prescot</h3>
      <p class="form-sub">Wypełnij zgłoszenie rejestracyjne. Nasz doradca handlowy skontaktuje się z Tobą w ciągu 24h w celu ustalenia indywidualnych warunków rabatowych.</p>

      <form class="p-form-grid" id="b2b-reg-form" action="javascript:void(0);" novalidate>
        <!-- Honeypot spam trap -->
        <input type="text" name="b2b_hp" style="display:none;" tabindex="-1" autocomplete="off">

        <div class="p-group">
          <label for="b2b-company">Nazwa firmy *</label>
          <input type="text" id="b2b-company" placeholder="np. Elektro-Instal Sp. z o.o." maxlength="120" autocomplete="organization" required>
        </div>

        <div class="p-group">
          <label for="b2b-nip">NIP *</label>
          <input type="text" id="b2b-nip" placeholder="np. 8451996500" maxlength="15" autocomplete="off" required>
        </div>

        <div class="p-group">
          <label for="b2b-name">Osoba kontaktowa *</label>
          <input type="text" id="b2b-name" placeholder="Imię i nazwisko" maxlength="80" autocomplete="name" required>
        </div>

        <div class="p-group">
          <label for="b2b-email">Firmowy adres e-mail *</label>
          <input type="email" id="b2b-email" placeholder="biuro@twojafirma.pl" maxlength="100" autocomplete="email" required>
        </div>

        <div class="p-group">
          <label for="b2b-phone">Numer telefonu *</label>
          <input type="tel" id="b2b-phone" placeholder="+48 000 000 000" maxlength="20" autocomplete="tel" required>
        </div>

        <div class="p-group">
          <label for="b2b-type">Profil działalności</label>
          <select id="b2b-type">
            <option value="hurtownia">Hurtownia Elektryczna / Oświetleniowa</option>
            <option value="instalator" selected>Instalator / Elektryk</option>
            <option value="architekt">Architekt / Projektant Wnętrz</option>
            <option value="producent">Producent Mebli / Reklam</option>
            <option value="inwestor">Inwestor / Generalny Wykonawca</option>
          </select>
        </div>

        <div class="p-group full">
          <label for="b2b-msg">Uwagi / Szacowany wolumen</label>
          <textarea id="b2b-msg" placeholder="Wpisz szacowane miesięczne zapotrzebowanie lub pytania o asortyment..." maxlength="1000"></textarea>
        </div>

        <div class="p-group full">
          <label style="display:flex; align-items:flex-start; gap:10px; font-size:12.5px; color:var(--p-text-muted); cursor:pointer;">
            <input type="checkbox" id="b2b-agree" required style="margin-top:3px; accent-color: var(--p-primary);">
            <span>Wyrażam zgodę na kontakt handlowy ze strony PRESCOT sp. z o.o. w celu przedstawienia oferty hurtowej i założenia konta B2B.</span>
          </label>
        </div>

        <div class="p-group full">
          <button type="submit" class="submitBtn">
            Wyślij formularz zgłoszeniowy &rarr;
          </button>
        </div>

        <div id="b2b-feedback" class="p-group full" style="display:none; padding: 16px 20px; border-radius: 12px; font-size: 14.5px; background: #dcfce7; color: #166534; border: 1px solid #bbf7d0;">
          <strong>Dziękujemy za zgłoszenie!</strong> Dział handlowy Prescot LED skontaktuje się z Państwem niezwłocznie.
        </div>
      </form>
    </div>
  </div>

  <!-- KORZYŚCI HANDLOWE (6 KAFELKÓW) -->
  <section id="korzysci-b2b" style="margin-bottom: 60px;">
    <div style="text-align:center; max-width:720px; margin:0 auto 40px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 30px; color: var(--p-dark); margin-bottom: 10px;">Dlaczego profesjonaliści wybierają Prescot LED?</h2>
      <p style="color: var(--p-text-muted); font-size: 15.5px;">Zbuduj przewagę konkurencyjną dzięki bezpośredniemu dostępowi do polskiego producenta taśm COB, zasilaczy Ultra Slim i systemów sterowania.</p>
    </div>

    <div class="p-benefits-grid">
      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h4>Rabaty Inwestycyjne</h4>
        <p>Przejrzyste progi rabatowe, stałe warunki handlowe oraz indywidualne kalkulacje cenowe dla dużych projektów kubaturowych i mieszkaniowych.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
        </div>
        <h4>Wysyłka w 24h</h4>
        <p>Ponad 95% katalogowych taśm LED, zasilaczy i profili stale dostępnych od ręki w centralnym magazynie wysokiego składowania w Giżycku.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        </div>
        <h4>Wsparcie Inżyniera</h4>
        <p>Bezpłatna weryfikacja schematów elektrycznych, dobór przekrojów przewodów, eliminacja spadków napięć i doradztwo techniczne.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h4>Gwarancja do 5 Lat</h4>
        <p>Komponenty poddawane rygorystycznym testom fotometrycznym i termicznym w laboratorium Prescot. Pewność i spokój Twoich inwestycji.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
        </div>
        <h4>Integracje XML / EDI</h4>
        <p>Automatyczna synchronizacja bazy produktowej, zdjęć wysokiej rozdzielczości, kart katalogowych ETIM oraz stanów magazynowych z Twoim systemem ERP.</p>
      </div>

      <div class="p-benefit-card">
        <div class="p-benefit-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
        </div>
        <h4>Wzorniki & Ekspozytory</h4>
        <p>Wspieramy naszych dystrybutorów dostarczając gotowe tablice ekspozycyjne, próbniki taśm COB oraz materiały marketingowe do salonu sprzedaży.</p>
      </div>
    </div>
  </section>
</main>

<script>
// Bezpieczna walidacja i obsługa formularza rejestracji B2B
document.getElementById('b2b-reg-form').addEventListener('submit', function(e) {{
  e.preventDefault();
  
  var hp = document.querySelector('input[name="b2b_hp"]').value;
  if (hp) return; // Spam bot detected

  var company = document.getElementById('b2b-company').value.trim();
  var nip = document.getElementById('b2b-nip').value.trim();
  var name = document.getElementById('b2b-name').value.trim();
  var email = document.getElementById('b2b-email').value.trim();
  var phone = document.getElementById('b2b-phone').value.trim();
  var agree = document.getElementById('b2b-agree').checked;

  if (!company || !nip || !name || !email || !phone || !agree) {{
    alert('Prosimy o wypełnienie wszystkich wymaganych pól oraz akceptację zgody.');
    return;
  }}

  // Sukces - prezentacja komunikatu
  var fb = document.getElementById('b2b-feedback');
  fb.style.display = 'block';
  this.reset();
}});
</script>
""" + footer_html + """
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
<script src="/local-navigation.js?v=20260901-dystrybucja-v4" defer></script>
</body>
</html>
"""

# Write Dystrybucja and Wspolpraca-B2B
dystr_path = os.path.join(base_dir, "dystrybucja/index.html")
with open(dystr_path, "w", encoding="utf-8") as f:
    f.write(generate_dystrybucja_html(True))
print("Wrote perfected dystrybucja/index.html")

b2b_path = os.path.join(base_dir, "wspolpraca-b2b/index.html")
with open(b2b_path, "w", encoding="utf-8") as f:
    f.write(generate_dystrybucja_html(False))
print("Wrote perfected wspolpraca-b2b/index.html")

# Write Kontakt
kontakt_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/wp-content/uploads/2025/09/cropped-favicon-1-32x32.png" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Krona+One&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/prescot-global.css?v=20260901-kontakt-v4">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <title>Kontakt & Dane Spółki — Prescot LED Giżycko</title>
  <style>
  :root {{
    --p-primary: #e55933;
    --p-primary-hover: #c94622;
    --p-dark: #0f172a;
    --p-dark-soft: #1e293b;
    --p-text: #212a35;
    --p-text-muted: #64748b;
    --p-bg: #f8fafc;
    --p-card: #ffffff;
    --p-border: #e2e8f0;
    --p-radius: 20px;
    --p-radius-sm: 12px;
    --p-shadow-sm: 0 2px 8px rgba(0,0,0,0.04);
    --p-shadow-md: 0 12px 30px -10px rgba(0,0,0,0.08);
    --p-shadow-lg: 0 20px 45px -12px rgba(15,23,42,0.12);
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--p-text);
    background: var(--p-bg);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding-bottom: 90px;
  }}

  /* FULL-SCREEN 100VH HERO SLIDE */
  .p-full-hero {{
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
  }}
  .p-full-hero::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.65) 0%, rgba(15, 23, 42, 0.88) 100%);
    z-index: 1;
  }}
  .p-full-hero-content {{
    position: relative;
    z-index: 2;
    max-width: 920px;
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .p-hero-eyebrow {{
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
  }}
  .p-full-hero h1 {{
    font-family: 'Outfit', sans-serif;
    font-size: clamp(34px, 4.5vw, 54px);
    color: #ffffff;
    margin-bottom: 20px;
    line-height: 1.18;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.4);
  }}
  .p-full-hero p.lead {{
    font-size: clamp(16px, 1.9vw, 19px);
    color: #e2e8f0;
    max-width: 820px;
    line-height: 1.65;
    margin-bottom: 32px;
    text-shadow: 0 1px 4px rgba(0,0,0,0.4);
  }}
  .p-hero-actions {{
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    justify-content: center;
  }}

  .p-hero-arrow-down {{
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
  }}
  .p-hero-arrow-down:hover {{ opacity: 1; color: #ff8a65; }}
  .p-arrow-icon {{
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
  }}
  @keyframes pBounce {{
    0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
    40% {{ transform: translateY(-10px); }}
    60% {{ transform: translateY(-5px); }}
  }}

  /* TREŚĆ PONIŻEJ HERO */
  .prescot-main-container {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 60px 24px 80px 24px;
  }}
  .prescot-breadcrumbs {{
    font-size: 13px;
    color: var(--p-text-muted);
    margin-bottom: 32px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .prescot-breadcrumbs a {{ color: var(--p-text-muted); text-decoration: none; }}
  .prescot-breadcrumbs a:hover {{ color: var(--p-primary); }}
  .prescot-breadcrumbs .sep {{ opacity: 0.4; }}

  /* KONTAKT CARDS */
  .p-contact-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
    margin-bottom: 50px;
  }}
  .p-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 36px 32px;
    box-shadow: var(--p-shadow-sm);
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
  }}
  .p-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--p-shadow-lg);
    border-color: var(--p-primary);
  }}
  .p-card-icon {{
    width: 52px;
    height: 52px;
    border-radius: 14px;
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
  }}
  .p-card h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 21px;
    font-weight: 700;
    color: var(--p-dark);
    margin-bottom: 12px;
  }}
  .p-card p {{
    color: var(--p-text-muted);
    font-size: 14px;
    line-height: 1.65;
    margin-bottom: 18px;
  }}
  .p-card a.card-link {{
    color: var(--p-primary);
    font-weight: 700;
    text-decoration: none;
    font-size: 14.5px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: auto;
    transition: gap 0.2s;
  }}
  .p-card a.card-link:hover {{ text-decoration: underline; gap: 10px; }}

  .p-form-box {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 44px 38px;
    box-shadow: var(--p-shadow-md);
    margin-bottom: 50px;
  }}
  .p-form-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }}
  @media (max-width: 650px) {{
    .p-form-grid {{ grid-template-columns: 1fr; }}
  }}
  .p-group {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .p-group.full {{ grid-column: 1 / -1; }}
  .p-group label {{
    font-size: 13px;
    font-weight: 700;
    color: var(--p-dark);
  }}
  .p-group input, .p-group select, .p-group textarea {{
    padding: 13px 16px;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius-sm);
    font-size: 14px;
    background: #f8fafc;
    color: var(--p-dark);
    outline: none;
    font-family: inherit;
    transition: all 0.2s;
  }}
  .p-group input:focus, .p-group select:focus, .p-group textarea:focus {{
    border-color: var(--p-primary);
    background: #ffffff;
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.12);
  }}
  .p-group textarea {{
    resize: vertical;
    min-height: 130px;
  }}
  </style>
</head>
<body>
<!-- SMART LOGO: TYLKO W SEKCJI HERO -->
<div class="prescot-smart-logo">
  <a href="/" title="Prescot LED Strona Główna">
    <img src="/wp-content/uploads/2025/12/biale-z-kolorem.svg" alt="Prescot LED">
  </a>
</div>

<!-- FULL-SCREEN 100VH HERO SLIDE -->
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/01/18.lobby_.webp');">
  <div class="p-full-hero-content">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      Kontakt & Centrala Giżycko
    </div>
    <h1>Skontaktuj się z Zespołem Prescot LED</h1>
    <p class="lead">Działamy na terenie całej Polski i Europy. Skontaktuj się z naszym biurem handlowym, inżynierami oświetlenia lub odwiedź naszą centralę produkcyjno-magazynową w Giżycku.</p>
    <div class="p-hero-actions">
      <a href="#formularz-kontaktowy" class="p-btn p-btn-primary">
        Napisz do nas
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
      <a href="#mapa-dojazdu" class="p-btn p-btn-outline">
        Mapa dojazdu ↓
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

  <!-- 3 KARTY KONTAKTOWE -->
  <div class="p-contact-grid">
    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      </div>
      <h3>Centrala & Magazyn</h3>
      <p>
        <strong>PRESCOT sp. z o.o.</strong><br>
        ul. Wileńska 1<br>
        11-500 Giżycko, Polska<br>
        NIP: 8451996500 | KRS: 0001004381
      </p>
      <a href="#mapa-dojazdu" class="card-link">Sprawdź dojazd na mapie &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </div>
      <h3>Dział Sprzedaży B2B</h3>
      <p>
        Zamówienia hurtowe, zapytania ofertowe dla dystrybutorów, instalatorów i deweloperów.<br><br>
        <strong>E-mail:</strong> <a href="mailto:komponenty@prescot.pl" style="color:var(--p-primary); text-decoration:none;">komponenty@prescot.pl</a><br>
        <strong>Telefon:</strong> +48 87 732 30 00
      </p>
      <a href="mailto:komponenty@prescot.pl" class="card-link">Napisz e-mail &rarr;</a>
    </div>

    <div class="p-card">
      <div class="p-card-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      </div>
      <h3>Wsparcie Techniczne</h3>
      <p>
        Konsultacje inżynieryjne, dobór zasilaczy, schematy instalacji wielostrefowych RF i protokołów DALI / Tuya Zigbee.<br><br>
        <strong>Dostępność:</strong> Pon – Pt: 8:00 – 16:00
      </p>
      <a href="/baza-wiedzy/" class="card-link">Przejdź do Bazy Wiedzy &rarr;</a>
    </div>
  </div>

  <!-- FORMULARZ KONTAKTOWY (BEZPIECZNY & ZWALIDOWANY) -->
  <div class="p-form-box" id="formularz-kontaktowy">
    <div style="margin-bottom: 28px;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 28px; color: var(--p-dark); margin-bottom: 8px;">Napisz bezpośrednio do nas</h2>
      <p style="color: var(--p-text-muted); font-size: 15px;">Wypełnij krótki formularz, a właściwy dział odpowie na Twoją wiadomość najszybciej jak to możliwe.</p>
    </div>

    <form class="p-form-grid" id="contact-form" action="javascript:void(0);" novalidate>
      <!-- Honeypot spam trap -->
      <input type="text" name="contact_hp" style="display:none;" tabindex="-1" autocomplete="off">

      <div class="p-group">
        <label for="c-name">Imię i nazwisko / Nazwa firmy *</label>
        <input type="text" id="c-name" placeholder="np. Jan Kowalski" maxlength="100" autocomplete="name" required>
      </div>

      <div class="p-group">
        <label for="c-email">Adres e-mail *</label>
        <input type="email" id="c-email" placeholder="twoj@email.pl" maxlength="100" autocomplete="email" required>
      </div>

      <div class="p-group">
        <label for="c-phone">Numer telefonu</label>
        <input type="tel" id="c-phone" placeholder="+48 000 000 000" maxlength="20" autocomplete="tel">
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
        <textarea id="c-msg" placeholder="W czym możemy pomóc? Opisz swoje zapytanie lub podaj specyfikację projektu..." maxlength="1500" required></textarea>
      </div>

      <div class="p-group full">
        <label style="display:flex; align-items:flex-start; gap:10px; font-size:12.5px; color:var(--p-text-muted); cursor:pointer;">
          <input type="checkbox" id="c-agree" required style="margin-top:3px; accent-color: var(--p-primary);">
          <span>Wyrażam zgodę na przetwarzanie moich danych osobowych przez PRESCOT sp. z o.o. w celu obsługi zapytania kontaktowego zgodnie z Polityką Prywatności.</span>
        </label>
      </div>

      <div class="p-group full">
        <button type="submit" class="submitBtn" style="justify-self:start;">
          Wyślij wiadomość &rarr;
        </button>
      </div>

      <div id="c-feedback" class="p-group full" style="display:none; padding: 16px 20px; border-radius: 12px; font-size: 14.5px; background: #dcfce7; color: #166534; border: 1px solid #bbf7d0;">
        <strong>Dziękujemy!</strong> Twoja wiadomość została pomyślnie wysłana. Skontaktujemy się z Tobą niezwłocznie.
      </div>
    </form>
  </div>

  <!-- MAPA GOOGLE -->
  <div id="mapa-dojazdu" style="border-radius: var(--p-radius); overflow: hidden; border: 1px solid var(--p-border); box-shadow: var(--p-shadow-sm); height: 420px; margin-bottom: 50px;">
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
// Bezpieczna walidacja i obsługa formularza kontaktowego
document.getElementById('contact-form').addEventListener('submit', function(e) {{
  e.preventDefault();

  var hp = document.querySelector('input[name="contact_hp"]').value;
  if (hp) return; // Spam bot detected

  var name = document.getElementById('c-name').value.trim();
  var email = document.getElementById('c-email').value.trim();
  var msg = document.getElementById('c-msg').value.trim();
  var agree = document.getElementById('c-agree').checked;

  if (!name || !email || !msg || !agree) {{
    alert('Prosimy o uzupełnienie wymaganych pól (imię, e-mail, treść) i zaznaczenie zgody.');
    return;
  }}

  var fb = document.getElementById('c-feedback');
  fb.style.display = 'block';
  this.reset();
}});
</script>
""" + footer_html + """
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
<script src="/local-navigation.js?v=20260901-kontakt-v4" defer></script>
</body>
</html>
"""

kontakt_path = os.path.join(base_dir, "kontakt/index.html")
with open(kontakt_path, "w", encoding="utf-8") as f:
    f.write(kontakt_content)
print("Wrote perfected kontakt/index.html")
