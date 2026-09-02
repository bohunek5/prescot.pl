# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
baza_path = os.path.join(base_dir, "baza-wiedzy/index.html")

footer_path = "/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html"
with open(footer_path, "r", encoding="utf-8") as f:
    footer_html = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/wp-content/uploads/2025/09/cropped-favicon-1-32x32.png" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Krona+One&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/prescot-global.css?v=20260901-baza-seo-v5">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  
  <title>Baza Wiedzy LED, Poradnik Instalatora & Dobór Zasilacza — Prescot</title>
  <meta name="description" content="Kompleksowy poradnik oświetlenia LED: taśmy COB i SMD, profile aluminiowe, złączki bez lutowania, sterowanie DALI/Tuya oraz kalkulator doboru zasilacza i spadków napięć.">
  <meta name="keywords" content="baza wiedzy led, taśmy led cob, profil aluminiowy led, złączki do taśm led, kalkulator zasilacza led, spadek napięcia led, sterowanie led dali zigbee, zasilacz 24v ultra slim">

  <!-- SCHEMA.ORG FAQPAGE & ARTICLE FOR GOOGLE RICH SNIPPETS -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Strona główna",
            "item": "https://tasmaled.com.pl/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Baza Wiedzy & Poradniki LED",
            "item": "https://tasmaled.com.pl/baza-wiedzy/"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Czym różnią się taśmy LED COB od tradycyjnych SMD?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Taśmy COB (Chip on Board) posiadają gęsto upakowane chipy LED (np. 320-528 diod/m) pokryte ciągłą warstwą luminoforu. Zapewnia to jednolitą linię światła bez widocznych punktów świetlnych, nawet w bardzo płytkich profilach aluminiowych."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Dlaczego na długich odcinkach taśmy LED występuje spadek jasności?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Wynika to ze zjawiska spadku napięcia na miedzianych ścieżkach PCB. Dla taśm 12V zaleca się zasilanie odcinków do 5m jednostronnie, dla 24V do 10m, a dla 48V nawet do 20m. Przy dłuższych liniach stosuje się zasilanie obustronne lub magistralę."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Jaki zapas mocy powinien mieć profesjonalny zasilacz LED?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Zalecany margines bezpieczeństwa wynosi minimum 15-20% ponad sumaryczną moc podłączonych taśm LED. Zapobiega to przegrzewaniu zasilacza i wydłuża jego żywotność."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Po co stosować profile aluminiowe do taśm LED?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Profil aluminiowy pełni kluczową rolę radiatora odprowadzającego ciepło z diod LED. Chroni chipy przed degradacją termiczną, zapewniając deklarowaną żywotność do 50 000 godzin, a klosz dodatkowo zabezpiecza taśmę przed kurzem i wilgocią."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

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
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.68) 0%, rgba(15, 23, 42, 0.88) 100%);
    z-index: 1;
  }}
  .p-full-hero-content {{
    position: relative;
    z-index: 2;
    max-width: 940px;
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
    max-width: 840px;
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

  /* APPLE-GRADE CALCULATOR */
  .apple-calc-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    box-shadow: var(--p-shadow-md);
    overflow: hidden;
    margin-bottom: 70px;
  }}
  .apple-calc-header {{
    padding: 28px 36px;
    border-bottom: 1px solid var(--p-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ffffff;
    flex-wrap: wrap;
    gap: 16px;
  }}
  .apple-calc-header h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: var(--p-dark);
    letter-spacing: -0.02em;
    margin-bottom: 4px;
  }}
  .apple-calc-header p {{
    font-size: 14px;
    color: var(--p-text-muted);
  }}
  .apple-calc-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    font-weight: 700;
    color: var(--p-primary);
    background: rgba(229, 89, 51, 0.08);
    border: 1px solid rgba(229, 89, 51, 0.2);
    padding: 6px 14px;
    border-radius: 999px;
  }}

  .apple-calc-body {{
    display: grid;
    grid-template-columns: 1fr 1.05fr;
    background: #ffffff;
  }}
  @media (max-width: 920px) {{
    .apple-calc-body {{ grid-template-columns: 1fr; }}
  }}

  .apple-calc-config {{
    padding: 36px;
    border-right: 1px solid var(--p-border);
    display: flex;
    flex-direction: column;
    gap: 26px;
  }}
  @media (max-width: 920px) {{
    .apple-calc-config {{ border-right: none; border-bottom: 1px solid var(--p-border); }}
  }}

  .calc-field-group {{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .calc-field-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .calc-field-label {{
    font-size: 13.5px;
    font-weight: 700;
    color: var(--p-dark);
  }}
  .calc-field-val-display {{
    font-size: 13.5px;
    font-weight: 800;
    color: var(--p-primary);
    font-family: 'Outfit', sans-serif;
  }}

  .apple-segmented {{
    display: flex;
    background: #f1f5f9;
    padding: 4px;
    border-radius: 12px;
    gap: 4px;
  }}
  .apple-seg-btn {{
    flex: 1;
    padding: 10px 14px;
    border: none;
    background: transparent;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    color: #64748b;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .apple-seg-btn.active {{
    background: #ffffff;
    color: var(--p-dark);
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }}

  .apple-chip-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 8px;
  }}
  .apple-chip-btn {{
    padding: 9px 8px;
    border: 1px solid var(--p-border);
    background: #f8fafc;
    border-radius: 10px;
    font-size: 12.5px;
    font-weight: 700;
    color: #475569;
    cursor: pointer;
    text-align: center;
    transition: all 0.2s;
  }}
  .apple-chip-btn:hover {{ border-color: #cbd5e1; background: #ffffff; }}
  .apple-chip-btn.active {{
    border-color: var(--p-primary);
    background: rgba(229, 89, 51, 0.08);
    color: var(--p-primary);
  }}

  .apple-slider-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .apple-range-slider {{
    flex: 1;
    accent-color: var(--p-primary);
    cursor: pointer;
    height: 6px;
    border-radius: 4px;
    background: #e2e8f0;
  }}
  .apple-num-input {{
    width: 78px;
    padding: 8px 10px;
    border: 1px solid var(--p-border);
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    color: var(--p-dark);
    text-align: center;
    outline: none;
  }}
  .apple-num-input:focus {{ border-color: var(--p-primary); }}

  .apple-calc-results {{
    padding: 36px;
    background: #f8fafc;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 28px;
  }}
  .calc-metrics-header {{
    font-size: 11.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--p-text-muted);
    margin-bottom: 16px;
  }}
  .calc-metric-cards {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 22px;
  }}
  @media (max-width: 550px) {{
    .calc-metric-cards {{ grid-template-columns: 1fr; }}
  }}
  .metric-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 12px;
    padding: 16px;
    box-shadow: var(--p-shadow-sm);
  }}
  .metric-card.hero-metric {{
    grid-column: 1 / -1;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    border: 1px solid rgba(229, 89, 51, 0.3);
  }}
  .metric-label {{
    font-size: 12px;
    color: var(--p-text-muted);
    display: block;
    margin-bottom: 4px;
  }}
  .metric-card.hero-metric .metric-label {{ color: #94a3b8; }}
  .metric-val {{
    font-family: 'Outfit', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--p-dark);
  }}
  .metric-card.hero-metric .metric-val {{
    color: #ffffff;
    font-size: 28px;
  }}

  .calc-load-bar-wrap {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 22px;
  }}
  .calc-load-info {{
    display: flex;
    justify-content: space-between;
    font-size: 12.5px;
    margin-bottom: 8px;
    color: var(--p-text-muted);
  }}
  .calc-progress-track {{
    width: 100%;
    height: 8px;
    background: #e2e8f0;
    border-radius: 999px;
    overflow: hidden;
  }}
  .calc-progress-fill {{
    height: 100%;
    width: 80%;
    background: #10b981;
    transition: width 0.3s ease, background-color 0.3s ease;
  }}

  .calc-rec-card {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: 14px;
    padding: 24px;
    color: #ffffff;
    border: 1px solid rgba(229, 89, 51, 0.3);
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .calc-rec-tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #ff8a65;
  }}
  .calc-rec-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.3;
  }}
  .calc-rec-desc {{
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.55;
  }}
  .calc-rec-btn {{
    align-self: flex-start;
    margin-top: 4px;
  }}

  /* SEO PILLARS HUB (4 COLUMNS / GRID) */
  .seo-pillars-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-bottom: 70px;
  }}
  .seo-pillar-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 32px 28px;
    box-shadow: var(--p-shadow-sm);
    display: flex;
    flex-direction: column;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .seo-pillar-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--p-shadow-lg);
    border-color: var(--p-primary);
  }}
  .seo-pillar-icon {{
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
  }}
  .seo-pillar-card h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 21px;
    font-weight: 700;
    color: var(--p-dark);
    margin-bottom: 12px;
  }}
  .seo-pillar-card p {{
    font-size: 14px;
    color: var(--p-text-muted);
    line-height: 1.65;
    margin-bottom: 18px;
  }}
  .seo-pillar-card ul {{
    list-style: none;
    padding: 0;
    margin: 0 0 20px 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .seo-pillar-card ul li {{
    font-size: 13px;
    color: #475569;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }}
  .seo-pillar-card ul li svg {{
    color: var(--p-primary);
    flex-shrink: 0;
    margin-top: 3px;
  }}

  /* DEEP DIVE ARTICLES */
  .seo-article-block {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    padding: 44px 38px;
    margin-bottom: 40px;
    box-shadow: var(--p-shadow-sm);
  }}
  .seo-article-block h2 {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    color: var(--p-dark);
    margin-bottom: 14px;
    letter-spacing: -0.02em;
  }}
  .seo-article-block h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 19px;
    color: var(--p-dark);
    margin: 22px 0 10px 0;
  }}
  .seo-article-block p {{
    font-size: 14.5px;
    color: #475569;
    line-height: 1.7;
    margin-bottom: 14px;
  }}
  .seo-table-wrap {{
    overflow-x: auto;
    margin: 20px 0;
  }}
  .seo-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    text-align: left;
  }}
  .seo-table th, .seo-table td {{
    padding: 12px 16px;
    border: 1px solid var(--p-border);
  }}
  .seo-table th {{
    background: #f1f5f9;
    color: var(--p-dark);
    font-weight: 700;
  }}
  .seo-table tr:nth-child(even) {{
    background: #f8fafc;
  }}

  /* FAQ ACCORDION */
  .faq-search-wrap {{
    position: relative;
    max-width: 600px;
    margin: 0 auto 28px auto;
  }}
  .faq-search-icon {{
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--p-text-muted);
  }}
  .faq-search-input {{
    width: 100%;
    padding: 14px 20px 14px 50px;
    border: 1px solid var(--p-border);
    border-radius: 999px;
    font-size: 14.5px;
    background: #ffffff;
    box-shadow: var(--p-shadow-sm);
    outline: none;
    transition: all 0.2s;
  }}
  .faq-search-input:focus {{
    border-color: var(--p-primary);
    box-shadow: 0 0 0 3px rgba(229, 89, 51, 0.12);
  }}

  .faq-filter-chips {{
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 36px;
  }}
  .chip-btn {{
    padding: 8px 18px;
    border: 1px solid var(--p-border);
    border-radius: 999px;
    background: #ffffff;
    font-size: 13px;
    font-weight: 700;
    color: var(--p-text-muted);
    cursor: pointer;
    transition: all 0.2s;
  }}
  .chip-btn.active {{
    background: var(--p-dark);
    color: #ffffff;
    border-color: var(--p-dark);
  }}

  .faq-grid {{
    display: flex;
    flex-direction: column;
    gap: 14px;
    max-width: 960px;
    margin: 0 auto 70px auto;
  }}
  .faq-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: var(--p-shadow-sm);
    transition: all 0.2s;
  }}
  .faq-btn {{
    width: 100%;
    padding: 20px 24px;
    border: none;
    background: transparent;
    text-align: left;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Outfit', sans-serif;
    font-size: 16.5px;
    font-weight: 700;
    color: var(--p-dark);
    cursor: pointer;
    gap: 16px;
  }}
  .faq-btn-icon {{
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #f1f5f9;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--p-text-muted);
    transition: transform 0.25s ease;
    flex-shrink: 0;
  }}
  .faq-card.open .faq-btn-icon {{
    transform: rotate(180deg);
    background: rgba(229, 89, 51, 0.1);
    color: var(--p-primary);
  }}
  .faq-content {{
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out;
    background: #f8fafc;
    border-top: 1px solid transparent;
  }}
  .faq-card.open .faq-content {{
    max-height: 500px;
    border-top-color: var(--p-border);
  }}
  .faq-content p {{
    padding: 20px 24px;
    font-size: 14px;
    color: #475569;
    line-height: 1.65;
  }}

  /* GLOSSARY */
  .glossary-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-bottom: 70px;
  }}
  .glossary-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: 14px;
    padding: 22px;
    box-shadow: var(--p-shadow-sm);
  }}
  .glossary-term {{
    font-family: 'Outfit', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: var(--p-primary);
    margin-bottom: 6px;
  }}
  .glossary-def {{
    font-size: 13.5px;
    color: var(--p-text-muted);
    line-height: 1.55;
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
<section class="p-full-hero" style="background-image: url('/wp-content/uploads/2026/03/AdobeStock_1101216226-1536x861.webp');">
  <div class="p-full-hero-content">
    <div class="p-hero-eyebrow">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      Baza Wiedzy &amp; Poradnik LED
    </div>
    <h1>Baza Wiedzy, Poradniki &amp; FAQ Prescot LED</h1>
    <p class="lead">Kompendium wiedzy oświetleniowej dla instalatorów, projektantów i dystrybutorów. Dowiedz się, jak łączyć taśmy COB, dobierać zasilacze, eliminować spadki napięć i montować profile aluminiowe.</p>
    <div class="p-hero-actions">
      <a href="#kalkulator-led" class="p-btn p-btn-primary">
        Kalkulator Zasilania &amp; Spadków
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
      <a href="#artykuly-wiedza" class="p-btn p-btn-outline">
        Poradniki Techniczne ↓
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
    <span>Baza Wiedzy &amp; FAQ</span>
  </nav>

  <!-- 1. APPLE-GRADE CALCULATOR SECTION -->
  <section id="kalkulator-led" class="apple-calc-card">
    <div class="apple-calc-header">
      <div>
        <h3>Kalkulator Doboru Zasilacza &amp; Spadków Napięć</h3>
        <p>Wybierz parametry taśmy i instalacji, a dobierzemy właściwy zasilacz z bezpiecznym zapasem mocy.</p>
      </div>
      <div class="apple-calc-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        Kalkulator Prescot LED
      </div>
    </div>

    <div class="apple-calc-body">
      <!-- CONFIGURATION PANEL -->
      <div class="apple-calc-config">
        <!-- 1. Voltage -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Napięcie instalacji</span>
            <span class="calc-field-val-display" id="disp-voltage">24V DC</span>
          </div>
          <div class="apple-segmented" id="seg-voltage">
            <button type="button" class="apple-seg-btn" data-val="12">12V</button>
            <button type="button" class="apple-seg-btn active" data-val="24">24V</button>
            <button type="button" class="apple-seg-btn" data-val="48">48V</button>
          </div>
        </div>

        <!-- 2. Power per meter -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Moc taśmy LED</span>
            <span class="calc-field-val-display" id="disp-power">14.4 W/m</span>
          </div>
          <div class="apple-chip-grid" id="grid-power">
            <button type="button" class="apple-chip-btn" data-val="4.8">4.8 W/m</button>
            <button type="button" class="apple-chip-btn" data-val="9.6">9.6 W/m</button>
            <button type="button" class="apple-chip-btn active" data-val="14.4">14.4 W/m</button>
            <button type="button" class="apple-chip-btn" data-val="19.2">19.2 W/m</button>
            <button type="button" class="apple-chip-btn" data-val="24.0">24.0 W/m</button>
          </div>
        </div>

        <!-- 3. LED Length -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Długość odcinka LED</span>
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
            <span class="calc-field-label">Długość kabla zasilacz &rarr; taśma</span>
            <span class="calc-field-val-display" id="disp-cable">3.0 m</span>
          </div>
          <div class="apple-slider-wrap">
            <input type="range" class="apple-range-slider" id="slider-cable" min="0.5" max="40" step="0.5" value="3.0">
            <input type="number" class="apple-num-input" id="num-cable" min="0.5" max="50" step="0.5" value="3.0">
          </div>
        </div>

        <!-- 5. Wire Cross-section -->
        <div class="calc-field-group">
          <div class="calc-field-header">
            <span class="calc-field-label">Przekrój żyły przewodu</span>
            <span class="calc-field-val-display" id="disp-wire">0.75 mm²</span>
          </div>
          <div class="apple-chip-grid" id="grid-wire">
            <button type="button" class="apple-chip-btn" data-val="0.5">0.50 mm²</button>
            <button type="button" class="apple-chip-btn active" data-val="0.75">0.75 mm²</button>
            <button type="button" class="apple-chip-btn" data-val="1.0">1.00 mm²</button>
            <button type="button" class="apple-chip-btn" data-val="1.5">1.50 mm²</button>
            <button type="button" class="apple-chip-btn" data-val="2.5">2.50 mm²</button>
          </div>
        </div>
      </div>

      <!-- RESULTS & TELEMETRY PANEL -->
      <div class="apple-calc-results">
        <div>
          <div class="calc-metrics-header">Wyniki i Dobór Zasilacza</div>

          <div class="calc-metric-cards">
            <!-- Hero Metric: Recommended PSU -->
            <div class="metric-card hero-metric">
              <span class="metric-label">Zalecana moc zasilacza (+20% bezpiecznego zapasu):</span>
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
            Dobieramy dla Ciebie
          </div>
          <div class="calc-rec-title" id="rec-psu-name">Zasilacz Prescot Ultra Slim 150W 24V</div>
          <p class="calc-rec-desc" id="rec-psu-text">Idealnie dobrana moc z 20% bezpiecznego zapasu. Zasilacz nie będzie się przegrzewał, ma zabezpieczenia przed zwarciem i posłuży na lata. Twój odcinek 6.0m możesz bez problemu podłączyć z jednej strony.</p>
          <a href="https://www.prescot.com.pl/pl/searchquery/zasilacz+150W+24V/1/phot/5?url=zasilacz+150W+24V" id="rec-psu-link" target="_blank" rel="noopener" class="p-btn p-btn-primary calc-rec-btn">
            Kup zasilacz 150W w sklepie &rarr;
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. 4 FILARY WIEDZY LED (SEO PILLARS GRID) -->
  <section id="artykuly-wiedza" style="margin-bottom: 70px;">
    <div style="text-align:center; max-width:760px; margin:0 auto 40px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 32px; color: var(--p-dark); margin-bottom: 10px;">Główne Działy Bazy Wiedzy</h2>
      <p style="color: var(--p-text-muted); font-size: 15.5px;">Wybierz temat, aby zgłębić zasady projektowania, doboru komponentów i montażu nowoczesnego oświetlenia liniowego.</p>
    </div>

    <div class="seo-pillars-grid">
      <!-- Filar 1: Taśmy LED -->
      <div class="seo-pillar-card">
        <div class="seo-pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h3>Taśmy LED &amp; Technologia COB</h3>
        <p>Wszystko o jednolitej linii światła, gęstościach chipów, współczynniku CRI &gt; 90 oraz taśmach cyfrowych Digital i CCT.</p>
        <ul>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> COB vs SMD – różnice optyczne</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Dobór barwy (2700K – 6000K)</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Odcinki cięcia i zasilanie</li>
        </ul>
        <a href="#filar-tasmy" style="color:var(--p-primary); font-weight:700; text-decoration:none; margin-top:auto;">Czytaj poradnik &rarr;</a>
      </div>

      <!-- Filar 2: Profile Aluminiowe -->
      <div class="seo-pillar-card">
        <div class="seo-pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
        </div>
        <h3>Profile Aluminiowe LED &amp; Klosze</h3>
        <p>Odprowadzanie ciepła jako warunek 5-letniej gwarancji, profile wpuszczane, nawierzchniowe, gips-karton i rodzaje dyfuzorów.</p>
        <ul>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Profil jako radiator chłodzący</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Klosz mleczny, mrożony czy transparentny</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Profile bezramkowe w sufitach G-K</li>
        </ul>
        <a href="#filar-profile" style="color:var(--p-primary); font-weight:700; text-decoration:none; margin-top:auto;">Czytaj poradnik &rarr;</a>
      </div>

      <!-- Filar 3: Złączki i Montaż -->
      <div class="seo-pillar-card">
        <div class="seo-pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        </div>
        <h3>Złączki Bez Lutowania &amp; Akcesoria</h3>
        <p>Szybki i trwały montaż taśm LED bez użycia lutownicy. Szybkozłączki zaciskowe MX2045, narożniki L, rozdzielacze T i przewody.</p>
        <ul>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Złączki 8mm vs 10mm (seria MX/MN)</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Łączenie taśm RGBW / RGB+CCT</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Prawidłowe dociskanie styków</li>
        </ul>
        <a href="#filar-zlaczki" style="color:var(--p-primary); font-weight:700; text-decoration:none; margin-top:auto;">Czytaj poradnik &rarr;</a>
      </div>

      <!-- Filar 4: Zasilanie i Sterowanie -->
      <div class="seo-pillar-card">
        <div class="seo-pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
        </div>
        <h3>Zasilanie 24V &amp; Sterowanie RF / DALI</h3>
        <p>Eliminacja spadków napięć, obliczenia przekrojów żył, zasilacze Ultra Slim, sterowniki wielostrefowe 2.4GHz oraz Tuya Zigbee.</p>
        <ul>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Napięcie 12V vs 24V vs 48V</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Ściemnianie PWM bez migotania (Flicker-Free)</li>
          <li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Integracja z DALI-2 i Smart Home</li>
        </ul>
        <a href="#filar-zasilanie" style="color:var(--p-primary); font-weight:700; text-decoration:none; margin-top:auto;">Czytaj poradnik &rarr;</a>
      </div>
    </div>
  </section>

  <!-- 3. DEEP SEO ARTICLES / PORADNIKI (WABIK DLA GOOGLE) -->
  <section class="seo-article-block" id="filar-tasmy">
    <h2>1. Technologia Taśm LED: COB vs SMD i Jakość Światła (CRI &gt; 90)</h2>
    <p>Tradycyjne taśmy LED oparte na diodach SMD (np. 2835, 5050) emitują światło punktowe. W przypadku zastosowania płytkich profili aluminiowych (np. o głębokości 6–8 mm) punkty świetlne odbijają się na kloszu jako tzw. „efekt koralików”. Rozwiązaniem tego problemu jest <strong>technologia COB (Chip on Board)</strong> stosowana w profesjonalnych liniach Prescot.</p>
    
    <h3>Czym wyróżniają się taśmy Prescot COB?</h3>
    <p>W taśmach COB chipy półprzewodnikowe montowane są bezpośrednio na laminacie PCB z potrójną warstwą miedzi (3oz) i zalewane jednolitym luminoforem. Dzięki gęstości od <strong>320 do 528 diod na metr</strong> uzyskuje się idealnie gładką, ciągłą wstęgę światła pod kątem 180°.</p>

    <div class="seo-table-wrap">
      <table class="seo-table">
        <thead>
          <tr>
            <th>Parametr</th>
            <th>Tradycyjne SMD 2835</th>
            <th>Prescot COB Pro 24V</th>
            <th>Zastosowanie Rekomendowane</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Jednolitość linii</strong></td>
            <td>Widoczne punkty diod</td>
            <td>Idealnie jednolita linia (brak kropek)</td>
            <td>Płytkie profile, podświetlenie mebli, sufity</td>
          </tr>
          <tr>
            <td><strong>Współczynnik CRI (Ra)</strong></td>
            <td>Ra &gt; 80</td>
            <td>Ra &gt; 90 / Ra &gt; 95</td>
            <td>Wnętrza mieszkalne, salony, ekspozycje</td>
          </tr>
          <tr>
            <td><strong>Kąt rozsyłu światła</strong></td>
            <td>120°</td>
            <td>180°</td>
            <td>Szerokie oświetlenie bez cieni bocznych</td>
          </tr>
          <tr>
            <td><strong>Napięcie pracy</strong></td>
            <td>12V lub 24V</td>
            <td>24V DC / 48V DC</td>
            <td>Minimalizacja spadków napięcia na długości</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="seo-article-block" id="filar-profile">
    <h2>2. Profile Aluminiowe LED — Ochrona Termiczna i Estetyka Montażu</h2>
    <p>Wielu instalatorów traktuje profile aluminiowe wyłącznie jako element dekoracyjny. Z inżynieryjnego punktu widzenia profil pełni przede wszystkim rolę <strong>radiatora chłodzącego</strong>. Dioda LED podczas pracy przekształca znaczną część energii elektrycznej w ciepło. Brak skutecznego odprowadzania temperatury z laminatu PCB prowadzi do przegrzania luminoforu, zmiany barwy światła i drastycznego skrócenia żywotności taśmy.</p>

    <h3>Rodzaje Profili i Kloszy w Praktyce:</h3>
    <p>
      • <strong>Profile Nawierzchniowe (np. typ D/MICRO):</strong> Szybki montaż na uchwytach sprężystych lub taśmie montażowej pod szafkami kuchennymi.<br>
      • <strong>Profile Wpuszczane / Frezowane:</strong> Zlicowane z płytą meblową lub płytą gipsowo-kartonową.<br>
      • <strong>Profile Bezramkowe G-K:</strong> Montowane pod siatkę i gładź szpachlową — dają efekt czystej szczeliny świetlnej w suficie podwieszanym.<br>
      • <strong>Dobór Klosza:</strong> Klosz <em>mleczny (opal)</em> rozprasza światło i kryje strukturę taśmy kosztem ok. 25% strumienia lm. Klosz <em>mrożony (satynowy)</em> to idealny kompromis (strata ok. 10%), a klosz <em>transparentny</em> zapewnia 98% przepuszczalności światła.
    </p>
  </section>

  <section class="seo-article-block" id="filar-zlaczki">
    <h2>3. Złączki LED Bez Lutowania: Szybki i Niezawodny Montaż</h2>
    <p>Lutowanie taśm LED na drabinie lub we wnękach sufitowych jest czasochłonne i stwarza ryzyko przegrzania ścieżek PCB. Dlatego Prescot opracował <strong>beznarzędziowe szybkozłączki zaciskowe</strong> serii MX2045 (dla taśm o szerokości laminatu 8 mm) oraz MN20 (dla taśm 10 mm).</p>

    <p>
      Ostre nożyce stykowe złączki przebijają powłokę taśmy i wbijają się bezpośrednio w miedziany pad lutowniczy, gwarantując połączenie odporne na wibracje, utlenianie i obciążenia prądowe do 5A. W ofercie dostępne są złączki proste (taśma-taśma), zasilające (taśma-przewód), narożne 90° typu L oraz rozdzielacze wielostrefowe.
    </p>
  </section>

  <section class="seo-article-block" id="filar-zasilanie">
    <h2>4. Zasilanie 24V vs 12V i Eliminacja Spadków Napięcia</h2>
    <p>Dlaczego w profesjonalnych instalacjach standardem stało się <strong>napięcie 24V DC</strong>? Z prawa Ohma i wzoru na moc ($P = U \cdot I$) wynika, że przy tym samym poborze mocy taśma 24V pobiera <strong>dwukrotnie mniejszy prąd</strong> niż taśma 12V. Oznacza to 4-krotnie mniejsze straty cieplne na przewodach i możliwość zasilania odcinków do 10 metrów z jednego punktu bez utraty jasności na końcu linii.</p>

    <h3>Zasady Dobrego Doboru Przekroju Kabla:</h3>
    <p>
      Dla odległości zasilacza od taśmy powyżej 5 metrów należy stosować przewody miedziane o przekroju minimum <strong>1.50 mm²</strong> lub <strong>2.50 mm²</strong>. Skorzystaj z powyższego kalkulatora Prescot, aby sprawdzić spadek napięcia w woltach oraz procentową stratę mocy dla Twojego projektu.
    </p>
  </section>

  <!-- 4. FAQ ACCORDION SECTION (14 PYTAŃ & WYSZUKIWARKA) -->
  <section id="faq-section" style="margin-bottom: 70px;">
    <div style="text-align:center; max-width:720px; margin:0 auto 36px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 32px; color: var(--p-dark); margin-bottom: 10px;">Najczęściej zadawane pytania (FAQ)</h2>
      <p style="color: var(--p-text-muted); font-size: 15.5px;">Wyszukaj natychmiast odpowiedź na swoje pytanie techniczne lub wybierz interesującą Cię kategorię.</p>
    </div>

    <div class="faq-search-wrap">
      <svg class="faq-search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" id="faqSearchInput" class="faq-search-input" placeholder="Wpisz szukaną frazę (np. spadek napięcia, zasilacz, COB, złączka, profil)...">
    </div>

    <div class="faq-filter-chips">
      <button type="button" class="chip-btn active" data-filter="all">Wszystkie (14)</button>
      <button type="button" class="chip-btn" data-filter="tasmy">Taśmy &amp; COB (4)</button>
      <button type="button" class="chip-btn" data-filter="zasilanie">Zasilanie &amp; Spadki (4)</button>
      <button type="button" class="chip-btn" data-filter="sterowanie">Sterowniki &amp; RF (3)</button>
      <button type="button" class="chip-btn" data-filter="montaz">Profile &amp; Złączki (3)</button>
    </div>

    <div class="faq-grid" id="faqAccordion">
      <!-- Q1 -->
      <div class="faq-card" data-cat="tasmy">
        <button class="faq-btn" type="button">
          <span>Czym różnią się taśmy LED COB od tradycyjnych SMD?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśmy COB (Chip on Board) posiadają gęsto upakowane chipy LED pokryte ciągłą warstwą luminoforu (np. 320–528 chipów/m), co daje idealnie jednolitą linię światła bez widocznych punktów świetlnych (tzw. efektu kropkowania), nawet w bardzo płytkich profilach aluminiowych.</p>
        </div>
      </div>

      <!-- Q2 -->
      <div class="faq-card" data-cat="zasilanie">
        <button class="faq-btn" type="button">
          <span>Dlaczego na długich odcinkach taśmy LED 12V/24V występuje spadek jasności?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Wynika to z oporu elektrycznego miedzianych ścieżek na laminacie PCB (zjawisko spadku napięcia). Dla taśm 12V zaleca się zasilanie odcinków maksymalnie do 5 metrów jednostronnie. Dla taśm 24V dystans ten wynosi do 10 metrów. Przy dłuższych liniach należy zastosować zasilanie dwustronne lub linię magistralną.</p>
        </div>
      </div>

      <!-- Q3 -->
      <div class="faq-card" data-cat="zasilanie">
        <button class="faq-btn" type="button">
          <span>Jaki zapas mocy powinien mieć profesjonalny zasilacz LED?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Zalecany inżynieryjny margines bezpieczeństwa wynosi minimum <strong>15–20%</strong> ponad sumaryczną moc pobieraną przez podłączone taśmy. Chroni to zasilacz przed przegrzaniem i gwarantuje stabilną wieloletnią pracę.</p>
        </div>
      </div>

      <!-- Q4 -->
      <div class="faq-card" data-cat="montaz">
        <button class="faq-btn" type="button">
          <span>Czy taśmę LED można nakleić bezpośrednio na ścianę lub mebel bez profilu?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Nie jest to zalecane. Profil aluminiowy pełni rolę radiatora odprowadzającego ciepło z diod LED. Bez profilu taśma ulega przegrzaniu, co powoduje szybsze wypalenie diod, utratę jasności i utratę gwarancji producenta.</p>
        </div>
      </div>

      <!-- Q5 -->
      <div class="faq-card" data-cat="tasmy">
        <button class="faq-btn" type="button">
          <span>Co oznacza parametr CRI / Ra &gt; 90 w taśmach Prescot?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>CRI (Color Rendering Index) określa wierność oddawania barw oświetlanych przedmiotów w porównaniu ze światłem naturalnym (gdzie słońce = 100). Wartość Ra &gt; 90 oznacza, że kolory mebli, tkanin, jedzenia i skóry wyglądają naturalnie i soczyście.</p>
        </div>
      </div>

      <!-- Q6 -->
      <div class="faq-card" data-cat="sterowanie">
        <button class="faq-btn" type="button">
          <span>Jak działa sterowanie strefowe RF 2.4GHz w systemie Prescot?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Sterowniki radiowe Prescot pracują na częstotliwości 2.4GHz z automatyczną retransmisją sygnału (Mesh). Jeden pilot lub panel naścienny może niezależnie kontrolować od 1 do 8 oddzielnych stref oświetlenia w domu bez konieczności prowadzenia dodatkowych kabli sterujących.</p>
        </div>
      </div>

      <!-- Q7 -->
      <div class="faq-card" data-cat="tasmy">
        <button class="faq-btn" type="button">
          <span>Czym różni się taśma CCT (Multiwhite) od RGBW?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśma CCT posiada naprzemiennie diody ciepłe (np. 2700K) i zimne (np. 6500K), co pozwala płynnie regulować temperaturę bieli. Taśma RGBW łączy diody kolorowe RGB z osobną, czystą diodą białą (White), umożliwiając zarówno nastrojowe kolory, jak i funkcjonalne oświetlenie użytkowe.</p>
        </div>
      </div>

      <!-- Q8 -->
      <div class="faq-card" data-cat="montaz">
        <button class="faq-btn" type="button">
          <span>Jak bezpiecznie łączyć taśmy bez lutownicy za pomocą złączek Prescot?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Wystarczy uciąć taśmę w oznaczonym punkcie cięcia, wsunąć laminat do złączki MX2045/MN20 tak, aby nożyce stykowe trafiły w miedziane pady, a następnie docisnąć przezroczystą klapkę szczypcami. Połączenie jest trwałe, estetyczne i mieści się w standardowym profilu.</p>
        </div>
      </div>

      <!-- Q9 -->
      <div class="faq-card" data-cat="zasilanie">
        <button class="faq-btn" type="button">
          <span>Kiedy stosować zasilacze hermetyczne IP67, a kiedy meblowe Ultra Slim?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Zasilacze hermetyczne IP67 są w pełni zalane żywicą poliuretanową i dedykowane do łazienek, stref mokrych, elewacji zewnętrznych i ogrodów. Zasilacze Ultra Slim o smukłej wysokości (np. 15–18 mm) są idealne do zabudowy meblowej, za lustrami i w ciasnych wnękach GK.</p>
        </div>
      </div>

      <!-- Q10 -->
      <div class="faq-card" data-cat="sterowanie">
        <button class="faq-btn" type="button">
          <span>Czy oświetlenie LED Prescot można zintegrować z aplikacją Tuya / Smart Life?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Tak, poprzez zastosowanie kontrolerów Prescot Tuya Zigbee 3.0 lub bramki RF-WiFi. Umożliwia to sterowanie oświetleniem z telefonu, tworzenie scenariuszy czasowych oraz integrację z asystentami głosowymi Google Home i Amazon Alexa.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. SŁOWNICZEK POJĘĆ OŚWIETLENIOWYCH (GLOSSARY) -->
  <section style="margin-bottom: 60px;">
    <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 28px; color: var(--p-dark); margin-bottom: 8px;">Słowniczek Pojęć Technicznych</h2>
      <p style="color: var(--p-text-muted); font-size: 15px;">Najważniejsze parametry i pojęcia ze świata profesjonalnego oświetlenia LED.</p>
    </div>

    <div class="glossary-grid">
      <div class="glossary-card">
        <div class="glossary-term">Lumen (lm)</div>
        <div class="glossary-def">Jednostka strumienia świetlnego. Informuje o całkowitej ilości światła emitowanego przez taśmę lub oprawę LED.</div>
      </div>
      <div class="glossary-card">
        <div class="glossary-term">Luks (lx)</div>
        <div class="glossary-def">Jednostka natężenia oświetlenia na danej powierzchni ($1 lx = 1 lm / m^2$). Wyznacza standardy jasności w normach PN-EN 12464.</div>
      </div>
      <div class="glossary-card">
        <div class="glossary-term">CRI / Ra</div>
        <div class="glossary-def">Wskaźnik oddawania barw. Wartości powyżej 90 gwarantują naturalny, wierny wygląd oświetlanych przedmiotów i wnętrz.</div>
      </div>
      <div class="glossary-card">
        <div class="glossary-term">Klasa IP (IP20 / IP67)</div>
        <div class="glossary-def">Stopień ochrony obudowy przed wnikaniem ciał stałych (pierwsza cyfra) oraz cieczy i wody (druga cyfra).</div>
      </div>
      <div class="glossary-card">
        <div class="glossary-term">SDCM / MacAdam</div>
        <div class="glossary-def">Wskaźnik powtarzalności barwowej między poszczególnymi partiami taśm. Prescot gwarantuje SDCM ≤ 3 (brak widocznych różnic odcieni).</div>
      </div>
      <div class="glossary-card">
        <div class="glossary-term">Filtr PFC (Power Factor)</div>
        <div class="glossary-def">Korekcja współczynnika mocy w zasilaczach LED, redukująca pobór prądu biernego i chroniąca sieć elektryczną przed zakłóceniami.</div>
      </div>
    </div>
  </section>
</main>

<script>
// FAQ Accordion & Search
document.querySelectorAll('.faq-btn').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    var card = btn.closest('.faq-card');
    card.classList.toggle('open');
  }});
}});

var searchInput = document.getElementById('faqSearchInput');
var faqCards = document.querySelectorAll('.faq-card');
var filterBtns = document.querySelectorAll('.chip-btn');

function filterFAQ() {{
  var query = searchInput.value.toLowerCase().trim();
  var activeChip = document.querySelector('.chip-btn.active').dataset.filter;

  faqCards.forEach(function(card) {{
    var text = card.textContent.toLowerCase();
    var cat = card.dataset.cat;
    var matchesQuery = query === '' || text.includes(query);
    var matchesCat = activeChip === 'all' || cat === activeChip;

    if (matchesQuery && matchesCat) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}

searchInput.addEventListener('input', filterFAQ);

filterBtns.forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    filterBtns.forEach(function(b) {{ b.classList.remove('active'); }});
    btn.classList.add('active');
    filterFAQ();
  }});
}});

// APPLE-GRADE PRESCOT LED CALCULATOR CONTROLLER
var state = {{
  voltage: 24,
  powerPerM: 14.4,
  length: 6.0,
  cable: 3.0,
  wire: 0.75
}};

function updateCalculator() {{
  var nominalPower = state.powerPerM * state.length;
  var recommendedPsu = nominalPower * 1.20;
  var current = nominalPower / state.voltage;

  var wireResistance = (0.0175 * state.cable * 2) / state.wire;
  var voltageDrop = current * wireResistance;
  var lossPct = (voltageDrop / state.voltage) * 100;

  var psuOptions = [35, 60, 100, 150, 200, 250, 300, 400, 600];
  var matchedPsu = 600;
  for (var i = 0; i < psuOptions.length; i++) {{
    if (psuOptions[i] >= recommendedPsu) {{
      matchedPsu = psuOptions[i];
      break;
    }}
  }}

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
  if (loadPct > 90) {{
    document.getElementById('res-load-bar').style.background = '#ef4444';
  }} else if (loadPct > 80) {{
    document.getElementById('res-load-bar').style.background = '#e55933';
  }} else {{
    document.getElementById('res-load-bar').style.background = '#10b981';
  }}

  // Recommendation text & dynamic Prescot shop search URL
  var modelName = 'Zasilacz Prescot Ultra Slim ' + matchedPsu + 'W ' + state.voltage + 'V';
  document.getElementById('rec-psu-name').textContent = modelName;

  var advice = 'Idealnie dobrana moc z 20% bezpiecznego zapasu. Zasilacz nie będzie się przegrzewał, ma zabezpieczenia przed zwarciem i posłuży na lata. ';
  if (state.voltage === 12 && state.length > 5) {{
    advice += 'Wskazówka: przy taśmie 12V i długości ' + state.length.toFixed(1) + 'm warto podpiąć zasilanie z obu stron, żeby na końcu taśmy nie tracić jasności.';
  }} else if (lossPct > 3.0) {{
    advice += 'Wskazówka: przewód ma ' + state.cable.toFixed(1) + 'm — wybierz grubszy kabel (np. 1.50 mm²), aby taśma świeciła pełną jasnością.';
  }} else {{
    advice += 'Twój odcinek ' + state.length.toFixed(1) + 'm możesz bez problemu podłączyć z jednej strony.';
  }}
  document.getElementById('rec-psu-text').textContent = advice;

  // Dynamic search URL to prescot.com.pl (Shoper format)
  var query = encodeURIComponent('zasilacz ' + matchedPsu + 'W ' + state.voltage + 'V');
  var searchUrl = 'https://www.prescot.com.pl/pl/searchquery/' + query + '/1/phot/5?url=' + query;
  var btnLink = document.getElementById('rec-psu-link');
  if (btnLink) {{
    btnLink.href = searchUrl;
    btnLink.innerHTML = 'Kup zasilacz ' + matchedPsu + 'W w sklepie &rarr;';
  }}
}}

// 1. Voltage Segments
document.querySelectorAll('#seg-voltage .apple-seg-btn').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    document.querySelectorAll('#seg-voltage .apple-seg-btn').forEach(function(b) {{ b.classList.remove('active'); }});
    btn.classList.add('active');
    state.voltage = parseFloat(btn.dataset.val);
    updateCalculator();
  }});
}});

// 2. Power Chips
document.querySelectorAll('#grid-power .apple-chip-btn').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    document.querySelectorAll('#grid-power .apple-chip-btn').forEach(function(b) {{ b.classList.remove('active'); }});
    btn.classList.add('active');
    state.powerPerM = parseFloat(btn.dataset.val);
    updateCalculator();
  }});
}});

// 3. LED Length
var sLen = document.getElementById('slider-length');
var nLen = document.getElementById('num-length');
if (sLen && nLen) {{
  sLen.addEventListener('input', function() {{
    nLen.value = sLen.value;
    state.length = parseFloat(sLen.value);
    updateCalculator();
  }});
  nLen.addEventListener('input', function() {{
    sLen.value = nLen.value;
    state.length = parseFloat(nLen.value) || 1;
    updateCalculator();
  }});
}}

// 4. Cable Distance
var sCab = document.getElementById('slider-cable');
var nCab = document.getElementById('num-cable');
if (sCab && nCab) {{
  sCab.addEventListener('input', function() {{
    nCab.value = sCab.value;
    state.cable = parseFloat(sCab.value);
    updateCalculator();
  }});
  nCab.addEventListener('input', function() {{
    sCab.value = nCab.value;
    state.cable = parseFloat(nCab.value) || 1;
    updateCalculator();
  }});
}}

// 5. Wire Cross Chips
document.querySelectorAll('#grid-wire .apple-chip-btn').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    document.querySelectorAll('#grid-wire .apple-chip-btn').forEach(function(b) {{ b.classList.remove('active'); }});
    btn.classList.add('active');
    state.wire = parseFloat(btn.dataset.val);
    updateCalculator();
  }});
}});

// Initialize
updateCalculator();
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
window.gtranslateSettings = window.gtranslateSettings || {{}};
window.gtranslateSettings['85632840'] = {{"default_language":"pl","languages":["ar","zh-CN","cs","da","en","et","fi","fr","de","it","lt","pl","es","sv"],"url_structure":"none","flag_style":"3d","wrapper_selector":"#gt-wrapper-85632840","alt_flags":[],"float_switcher_open_direction":"top","switcher_horizontal_position":"inline","flags_location":"/wp-content/plugins/gtranslate/flags/"}};
</script>
<script src="/wp-content/plugins/gtranslate/js/float.js?ver=3.1.1" data-no-optimize="1" data-no-minify="1" data-gt-widget-id="85632840" defer></script>
<script src="/local-navigation.js?v=20260901-baza-seo-v5" defer></script>
</body>
</html>
"""

with open(baza_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully created massive, SEO-rich Baza Wiedzy without AI buzzwords.")
