# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"
baza_path = os.path.join(base_dir, "baza-wiedzy/index.html")

footer_path = "/Users/karolbohdanowicz/.gemini/antigravity-ide/brain/7274a131-cab3-4aaa-bf74-0b7a719f26f4/scratch/footer.html"
with open(footer_path, "r", encoding="utf-8") as f:
    footer_html = f.read()

# 16 High-Quality Articles definition
articles = [
    {
        "id": 1,
        "cat": "zasilacze",
        "cat_label": "Zasilacze LED",
        "tag": "Nowość 2026",
        "tag_class": "tag-orange",
        "time": "4 min czytania",
        "img": "/wp-content/uploads/2026/03/akceosria-her-3-1024x744.webp",
        "title": "Inteligentny Zasilacz LED z auto-detekcją 12V/24V – rewolucja montażowa",
        "excerpt": "Jak działa technologia automatycznego rozpoznawania napięcia podłączonej taśmy LED i dlaczego eliminuje ryzyko spalenia instalacji przez pomyłkę instalatora.",
        "link": "https://www.prescot.com.pl/pl/n/34"
    },
    {
        "id": 2,
        "cat": "tasmy",
        "cat_label": "Taśmy LED",
        "tag": "Technologia COB",
        "tag_class": "",
        "time": "5 min czytania",
        "img": "/wp-content/uploads/2026/03/24e003-033-10-w_1424e003-033-10-w-1024x683.webp",
        "title": "Jednolita linia światła bez widocznych kropek – jak dobrać taśmę COB?",
        "excerpt": "Porównanie gęstości 320 vs 528 LED/m. Zobacz, jak uzyskać gładką wstęgę świetlną w płytkich profilach meblowych i sufitowych bez efektu koralików.",
        "link": "https://www.prescot.com.pl/pl/n/23"
    },
    {
        "id": 3,
        "cat": "zasilacze",
        "cat_label": "Normy & Strefy",
        "tag": "Bezpieczeństwo IP",
        "tag_class": "",
        "time": "6 min czytania",
        "img": "/wp-content/uploads/2026/03/AdobeStock_1392520552-1024x574.webp",
        "title": "Oświetlenie stref mokrych: łazienki, baseny i elewacje (IP20 vs IP65 vs IP68)",
        "excerpt": "Jak zgodnie ze sztuką zasilić i uszczelnić taśmy LED pod prysznicem, w fugach płytek i na tarasie. Przewodnik po powłokach silikonowych i żelowych.",
        "link": "https://www.prescot.com.pl/pl/n/33"
    },
    {
        "id": 4,
        "cat": "zlaczki",
        "cat_label": "Akcesoria & Montaż",
        "tag": "Szybki montaż",
        "tag_class": "tag-orange",
        "time": "3 min czytania",
        "img": "/wp-content/uploads/2026/03/profil-zlaczka-zapalona-768x974.webp",
        "title": "Szybkozłączki do taśm LED – jak łączyć taśmy bez lutownicy na budowie?",
        "excerpt": "Praktyczny test złączek zaciskowych MX2045 (8mm) i MN20 (10mm). Szybki montaż narożników 90°, połączeń prostych i przewodów zasilających.",
        "link": "https://www.prescot.com.pl/pl/c/Akcesoria-do-zasilaczy-i-tasm-LED/344"
    },
    {
        "id": 5,
        "cat": "profile",
        "cat_label": "Profile & Klosze",
        "tag": "Profile LED",
        "tag_class": "",
        "time": "5 min czytania",
        "img": "/wp-content/uploads/2026/03/AdobeStock_958838417-1024x574.webp",
        "title": "Dlaczego taśma LED musi być w profilu aluminiowym? Rola chłodzenia",
        "excerpt": "Wpływ temperatury na degradację luminoforu. Jak dobrać profil nawierzchniowy, wpuszczany lub bezramkowy do sufitów podwieszanych G-K.",
        "link": "https://www.prescot.com.pl/pl/n/12"
    },
    {
        "id": 6,
        "cat": "zasilacze",
        "cat_label": "Zasilanie 24V",
        "tag": "Poradnik B2B",
        "tag_class": "",
        "time": "4 min czytania",
        "img": "/wp-content/uploads/2026/03/led-strip-installation-on-wooden-stairs-2026-01-09-01-02-16-utc.webp",
        "title": "Jak prawidłowo dobrać moc zasilacza LED i zminimalizować spadek napięcia?",
        "excerpt": "Wzory na obliczenie zapasu mocy 20%, dobór przekroju żył przewodów (0.75mm² vs 1.50mm²) oraz zasady zasilania obustronnego dla długich linii.",
        "link": "https://www.prescot.com.pl/pl/n/28"
    },
    {
        "id": 7,
        "cat": "tasmy",
        "cat_label": "Jakość Światła",
        "tag": "CRI > 97",
        "tag_class": "tag-orange",
        "time": "5 min czytania",
        "img": "/wp-content/uploads/2026/03/tasma-cri97-biala-zimna_4-2.webp",
        "title": "Współczynnik oddawania barw CRI Ra > 97 – dlaczego ma znaczenie w salonie i kuchni?",
        "excerpt": "Różnice między tanimi taśmami Ra 70-80 a serią Prescot High CRI. Wierność odwzorowania kolorów drewna, blatów, tkanin i żywności.",
        "link": "https://www.prescot.com.pl/pl/n/23"
    },
    {
        "id": 8,
        "cat": "tasmy",
        "cat_label": "Taśmy Gięte",
        "tag": "S-Shape",
        "tag_class": "",
        "time": "4 min czytania",
        "img": "/wp-content/uploads/2026/03/s-shape_29s-shape-1024x683.webp",
        "title": "Taśmy LED zygzakowate S-Shape – oświetlenie łuków, liter 3D i zaokrągleń",
        "excerpt": "Elastyczny laminat boczny umożliwiający zginanie taśmy na płaszczyźnie pod kątem do 90° bez konieczności przecinania i lutowania narożników.",
        "link": "https://www.prescot.com.pl/pl/c/Tasmy-LED/1"
    },
    {
        "id": 9,
        "cat": "smart",
        "cat_label": "Sterowniki & Smart",
        "tag": "RF 2.4GHz",
        "tag_class": "",
        "time": "6 min czytania",
        "img": "/wp-content/uploads/2026/03/rozdzielacz-napiecia-768x900.webp",
        "title": "Sterowanie wielostrefowe LED – piloty RF 2.4GHz, panele naścienne i Tuya Zigbee",
        "excerpt": "Jak podzielić dom na niezależne strefy świetlne bez kucia ścian i prowadzenia dodatkowych przewodów sterujących. Retransmisja sygnału Mesh.",
        "link": "https://www.prescot.com.pl/pl/n/21"
    },
    {
        "id": 10,
        "cat": "profile",
        "cat_label": "Sufity & Ściany",
        "tag": "Architektura",
        "tag_class": "",
        "time": "5 min czytania",
        "img": "/wp-content/uploads/2026/03/AdobeStock_1084354660-1-1536x699.webp",
        "title": "Oświetlenie sufitów podwieszanych i gzymsów – profile do światła pośredniego",
        "excerpt": "Jak uzyskać efekt lewitującego sufitu za pomocą profili architektonicznych z kloszem skierowanym na ścianę lub sufit. Zasady doboru mocy taśmy.",
        "link": "https://www.prescot.com.pl/pl/n/11"
    },
    {
        "id": 11,
        "cat": "tasmy",
        "cat_label": "Temperatura Barwowa",
        "tag": "CCT Multiwhite",
        "tag_class": "tag-orange",
        "time": "4 min czytania",
        "img": "/wp-content/uploads/2026/03/24e006-033-10-ww_1224e006-033-10-ww-1024x659.webp",
        "title": "Taśmy CCT (Dual White) – płynna zmiana barwy od 2700K do 6500K",
        "excerpt": "Oświetlenie zgodne z rytmem dobowym (Human Centric Lighting). Zimne światło do pracy w dzień i ciepłe, relaksujące światło wieczorem.",
        "link": "https://www.prescot.com.pl/pl/n/23"
    },
    {
        "id": 12,
        "cat": "zlaczki",
        "cat_label": "Logistyka & B2B",
        "tag": "Magazyn 24h",
        "tag_class": "",
        "time": "3 min czytania",
        "img": "/wp-content/uploads/2026/03/maga2-1-1024x1024.webp",
        "title": "Dostępność stanów magazynowych od ręki – centralny magazyn Giżycko",
        "excerpt": "Jak Prescot realizuje zamówienia inwestycyjne w 24 godziny. Ponad 500 000 metrów taśm LED i zasilaczy gotowych do natychmiastowej wysyłki.",
        "link": "/dystrybucja/"
    },
    {
        "id": 13,
        "cat": "profile",
        "cat_label": "Oprawy Liniowe",
        "tag": "Biura & Salony",
        "tag_class": "",
        "time": "5 min czytania",
        "img": "/wp-content/uploads/2026/03/front-oprawy.webp",
        "title": "Tworzenie opraw wiszących i natynkowych na bazie profili architektonicznych",
        "excerpt": "Jak z profilu szerokiego, taśmy COB i zasilacza stworzyć designerską lampę wiszącą nad wyspę kuchenną, stół jadalniany lub biurko gabinetowe.",
        "link": "https://www.prescot.com.pl/pl/n/14"
    },
    {
        "id": 14,
        "cat": "smart",
        "cat_label": "Automatyka Domowa",
        "tag": "Schody LED",
        "tag_class": "tag-orange",
        "time": "4 min czytania",
        "img": "/wp-content/uploads/2026/03/AdobeStock_397049111-768x512.webp",
        "title": "Animowane podświetlenie schodów – sterowniki kaskadowe z czujnikami ruchu",
        "excerpt": "Płynne zapalanie stopień po stopniu w kierunku ruchu użytkownika. Dobór taśm bocznych, czujników optycznych i zasilacza 24V.",
        "link": "https://www.prescot.com.pl/pl/c/Sterowniki-LED/2"
    },
    {
        "id": 15,
        "cat": "zasilacze",
        "cat_label": "Zabudowa Meblowa",
        "tag": "Ultra Slim",
        "tag_class": "",
        "time": "4 min czytania",
        "img": "/wp-content/uploads/2025/12/wiz1-1-1024x585.png",
        "title": "Zasilacze meblowe Ultra Slim – montaż w płytkich wnękach i za lustrami",
        "excerpt": "Kompaktowa wysokość od 15 mm, chłodzenie pasywne bez hałaśliwego wentylatora i certyfikat niepalności MM dla mebli kuchennych i szaf.",
        "link": "https://www.prescot.com.pl/pl/n/29"
    },
    {
        "id": 16,
        "cat": "zlaczki",
        "cat_label": "Płytki & Gres",
        "tag": "Łazienki",
        "tag_class": "",
        "time": "5 min czytania",
        "img": "/wp-content/uploads/2026/03/AdobeStock_814475605.webp",
        "title": "Profile LED do wklejania w glazurę i gres – światło w narożnikach kabiny",
        "excerpt": "Profile ze skrzydełkami montażowymi zatapianymi w kleju do płytek. Zabezpieczenie przed wilgocią i czysty detal architektoniczny w łazience.",
        "link": "https://www.prescot.com.pl/pl/c/Profile-do-glazury/345"
    }
]

# Generate Blog HTML items
blog_items_html = ""
for art in articles:
    tag_html = f'<span class="blog-card-tag {art["tag_class"]}">{art["tag"]}</span>' if art["tag"] else ""
    blog_items_html += f"""
      <article class="blog-card" data-cat="{art['cat']}">
        <div class="blog-thumb-wrap">
          <img src="{art['img']}" alt="{art['title']}" class="blog-thumb" loading="lazy">
          {tag_html}
        </div>
        <div class="blog-content">
          <div class="blog-meta">
            <span class="blog-meta-item">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              {art['time']}
            </span>
            <span>•</span>
            <span>{art['cat_label']}</span>
          </div>
          <h3 class="blog-title">{art['title']}</h3>
          <p class="blog-excerpt">{art['excerpt']}</p>
          <a href="{art['link']}" target="_blank" rel="noopener" class="blog-card-link">
            Czytaj artykuł &rarr;
          </a>
        </div>
      </article>
"""

html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/wp-content/uploads/2025/09/cropped-favicon-1-32x32.png" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Krona+One&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/prescot-global.css?v=20260901-baza-blog-v7">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  
  <title>Baza Wiedzy, Poradniki & Blog LED — Prescot</title>
  <meta name="description" content="Kompendium wiedzy oświetleniowej i 16 artykułów poradnikowych: taśmy COB, profile aluminiowe, złączki bez lutowania, kalkulator doboru zasilacza 24V i FAQ.">
  <meta name="keywords" content="baza wiedzy led, poradnik led, taśmy led cob, profile aluminiowe led, szybkozłączki do taśm led, kalkulator zasilacza led, spadek napięcia led, zasilacz ultra slim 24v">

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
              "text": "Taśmy COB (Chip on Board) posiadają gęsto upakowane chipy LED pokryte ciągłą warstwą luminoforu (np. 320-528 diod/m). Zapewnia to jednolitą linię światła bez widocznych punktów świetlnych, nawet w bardzo płytkich profilach aluminiowych."
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

  /* =========================================================
     BLOG & ARTYKUŁY PORADNIKOWE (3 W RZĘDZIE / 1 NA TELEFONIE)
     ========================================================= */
  .blog-section-header {{
    text-align: center;
    max-width: 780px;
    margin: 0 auto 36px auto;
  }}
  .blog-section-header h2 {{
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    color: var(--p-dark);
    margin-bottom: 10px;
    letter-spacing: -0.02em;
  }}
  .blog-section-header p {{
    color: var(--p-text-muted);
    font-size: 15.5px;
  }}

  /* KATEGORIE BLOGA (CHIPS) */
  .blog-category-filter {{
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }}
  .blog-filter-btn {{
    padding: 9px 20px;
    border: 1px solid var(--p-border);
    border-radius: 999px;
    background: #ffffff;
    font-size: 13px;
    font-weight: 700;
    color: var(--p-text-muted);
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: var(--p-shadow-sm);
  }}
  .blog-filter-btn:hover {{
    border-color: var(--p-primary);
    color: var(--p-primary);
  }}
  .blog-filter-btn.active {{
    background: var(--p-dark);
    color: #ffffff;
    border-color: var(--p-dark);
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
  }}

  /* GRID ARTYKUŁÓW: 3 KOLUMNY DESKTOP / 1 KOLUMNA TELEFON */
  .blog-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-bottom: 80px;
  }}
  @media (max-width: 1024px) {{
    .blog-grid {{ grid-template-columns: repeat(2, 1fr); }}
  }}
  @media (max-width: 768px) {{
    .blog-grid {{ grid-template-columns: 1fr; }}
  }}

  /* KAFELEK ARTYKUŁU */
  .blog-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    overflow: hidden;
    box-shadow: var(--p-shadow-sm);
    display: flex;
    flex-direction: column;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
  }}
  .blog-card:hover {{
    transform: translateY(-6px);
    box-shadow: var(--p-shadow-lg);
    border-color: rgba(229, 89, 51, 0.4);
  }}

  .blog-thumb-wrap {{
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 10;
    overflow: hidden;
    background: #0f172a;
  }}
  .blog-thumb {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }}
  .blog-card:hover .blog-thumb {{
    transform: scale(1.05);
  }}

  .blog-card-tag {{
    position: absolute;
    top: 14px;
    left: 14px;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(8px);
    color: #ffffff;
    font-size: 11.5px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, 0.2);
  }}
  .blog-card-tag.tag-orange {{
    background: var(--p-primary);
    border-color: var(--p-primary);
  }}

  .blog-content {{
    padding: 26px 24px 24px 24px;
    display: flex;
    flex-direction: column;
    flex: 1;
  }}
  .blog-meta {{
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 12px;
    color: var(--p-text-muted);
    margin-bottom: 12px;
  }}
  .blog-meta-item {{
    display: flex;
    align-items: center;
    gap: 4px;
  }}
  .blog-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 18.5px;
    font-weight: 700;
    color: var(--p-dark);
    line-height: 1.35;
    margin-bottom: 10px;
    transition: color 0.2s;
  }}
  .blog-card:hover .blog-title {{
    color: var(--p-primary);
  }}
  .blog-excerpt {{
    font-size: 13.5px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 20px;
    flex: 1;
  }}
  .blog-card-link {{
    font-size: 13.5px;
    font-weight: 700;
    color: var(--p-primary);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: auto;
    transition: gap 0.2s;
  }}
  .blog-card-link:hover {{
    text-decoration: underline;
    gap: 10px;
  }}

  /* APPLE-GRADE CALCULATOR (TERAZ PONIŻEJ BLOGA) */
  .apple-calc-card {{
    background: #ffffff;
    border: 1px solid var(--p-border);
    border-radius: var(--p-radius);
    box-shadow: var(--p-shadow-md);
    overflow: hidden;
    margin-bottom: 80px;
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
      Baza Wiedzy &amp; Poradniki LED
    </div>
    <h1>Baza Wiedzy, Poradniki &amp; Blog Prescot LED</h1>
    <p class="lead">Kompendium wiedzy oświetleniowej dla instalatorów, projektantów i dystrybutorów. Poznaj 16 praktycznych poradników o taśmach COB, profilach, zasilaczach i montażu bez lutowania.</p>
    <div class="p-hero-actions">
      <a href="#artykuly-blog" class="p-btn p-btn-primary">
        Przeglądaj Poradniki &amp; Blog
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
      <a href="#kalkulator-led" class="p-btn p-btn-outline">
        Kalkulator Zasilania &amp; Spadków ↓
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
    <span>Baza Wiedzy &amp; Poradniki</span>
  </nav>

  <!-- 1. BAZA WIEDZY / BLOG Z 16 ARTYKUŁAMI (3 W RZĘDZIE NA DESKTOPIE / 1 NA TELEFONIE) -->
  <section id="artykuly-blog" style="margin-bottom: 70px;">
    <div class="blog-section-header">
      <h2>Poradniki, Artykuły &amp; Wiedza Techniczna (16)</h2>
      <p>Wybierz kategorię tematyczną i dowiedz się, jak prawidłowo dobrać, zamontować i zasilić oświetlenie LED.</p>
    </div>

    <!-- KATEGORIE BLOGA (CHIPS) -->
    <div class="blog-category-filter">
      <button type="button" class="blog-filter-btn active" data-blog-cat="all">Wszystkie artykuły (16)</button>
      <button type="button" class="blog-filter-btn" data-blog-cat="tasmy">Taśmy LED &amp; COB</button>
      <button type="button" class="blog-filter-btn" data-blog-cat="profile">Profile Aluminiowe</button>
      <button type="button" class="blog-filter-btn" data-blog-cat="zlaczki">Złączki &amp; Montaż</button>
      <button type="button" class="blog-filter-btn" data-blog-cat="zasilacze">Zasilacze &amp; Dobór</button>
      <button type="button" class="blog-filter-btn" data-blog-cat="smart">Smart &amp; Sterowanie</button>
    </div>

    <!-- BLOG GRID (3 KOLUMNY DESKTOP / 1 TELEFON) -->
    <div class="blog-grid" id="blogGrid">
      {blog_items_html}
    </div>
  </section>

  <!-- 2. APPLE-GRADE CALCULATOR SECTION (PONIŻEJ BLOGA) -->
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

  <!-- 3. FAQ ACCORDION SECTION (6 ZWIĘZŁYCH, KONKRETNYCH PYTAŃ) -->
  <section id="faq-section" style="margin-bottom: 70px;">
    <div style="text-align:center; max-width:720px; margin:0 auto 36px auto;">
      <h2 style="font-family:'Outfit',sans-serif; font-size: 32px; color: var(--p-dark); margin-bottom: 10px;">Najczęściej zadawane pytania (FAQ)</h2>
      <p style="color: var(--p-text-muted); font-size: 15.5px;">Szybkie i konkretne odpowiedzi na najważniejsze pytania montażowe i techniczne.</p>
    </div>

    <div class="faq-search-wrap">
      <svg class="faq-search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" id="faqSearchInput" class="faq-search-input" placeholder="Wpisz szukaną frazę (np. spadek napięcia, zasilacz, COB, profil)...">
    </div>

    <div class="faq-grid" id="faqAccordion">
      <!-- Q1 -->
      <div class="faq-card">
        <button class="faq-btn" type="button">
          <span>Czym różnią się taśmy LED COB od tradycyjnych SMD?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Taśmy COB (Chip on Board) posiadają gęsto upakowane chipy LED pokryte ciągłą warstwą luminoforu (np. 320–528 chipów/m), co daje idealnie jednolitą linię światła bez widocznych punktów świetlnych (tzw. efektu kropkowania), nawet w bardzo płytkich profilach aluminiowych.</p>
        </div>
      </div>

      <!-- Q2 -->
      <div class="faq-card">
        <button class="faq-btn" type="button">
          <span>Dlaczego na długich odcinkach taśmy LED występuje spadek jasności?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Wynika to z oporu elektrycznego miedzianych ścieżek na laminacie PCB (zjawisko spadku napięcia). Dla taśm 12V zaleca się zasilanie odcinków maksymalnie do 5 metrów jednostronnie. Dla taśm 24V dystans ten wynosi do 10 metrów. Przy dłuższych liniach należy zastosować zasilanie dwustronne lub linię magistralną.</p>
        </div>
      </div>

      <!-- Q3 -->
      <div class="faq-card">
        <button class="faq-btn" type="button">
          <span>Jaki zapas mocy powinien mieć profesjonalny zasilacz LED?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Zalecany inżynieryjny margines bezpieczeństwa wynosi minimum <strong>15–20%</strong> ponad sumaryczną moc pobieraną przez podłączone taśmy. Chroni to zasilacz przed przegrzaniem i gwarantuje stabilną wieloletnią pracę.</p>
        </div>
      </div>

      <!-- Q4 -->
      <div class="faq-card">
        <button class="faq-btn" type="button">
          <span>Czy taśmę LED można nakleić bezpośrednio na mebel bez profilu?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Nie jest to zalecane. Profil aluminiowy pełni kluczową rolę radiatora odprowadzającego ciepło z diod LED. Bez profilu taśma ulega przegrzaniu, co powoduje szybsze wypalenie diod, utratę jasności i utratę gwarancji producenta.</p>
        </div>
      </div>

      <!-- Q5 -->
      <div class="faq-card">
        <button class="faq-btn" type="button">
          <span>Co oznacza parametr CRI / Ra &gt; 90 w taśmach Prescot?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>CRI (Color Rendering Index) określa wierność oddawania barw oświetlanych przedmiotów w porównaniu ze światłem słonecznym. Wartość Ra &gt; 90 oznacza, że kolory mebli, tkanin, jedzenia i skóry wyglądają naturalnie i nie są przekłamane.</p>
        </div>
      </div>

      <!-- Q6 -->
      <div class="faq-card">
        <button class="faq-btn" type="button">
          <span>Jak bezpiecznie łączyć taśmy bez lutownicy za pomocą złączek Prescot?</span>
          <span class="faq-btn-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span>
        </button>
        <div class="faq-content">
          <p>Wystarczy uciąć taśmę w oznaczonym punkcie cięcia, wsunąć laminat do złączki MX2045/MN20 tak, aby nożyce stykowe trafiły w miedziane pady, a następnie docisnąć przezroczystą klapkę szczypcami. Połączenie jest trwałe, estetyczne i mieści się w standardowym profilu.</p>
        </div>
      </div>
    </div>
  </section>
</main>

<script>
// Filter Blog Categories
var blogFilterBtns = document.querySelectorAll('.blog-filter-btn');
var blogCards = document.querySelectorAll('.blog-card');

blogFilterBtns.forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    blogFilterBtns.forEach(function(b) {{ b.classList.remove('active'); }});
    btn.classList.add('active');
    var cat = btn.dataset.blogCat;

    blogCards.forEach(function(card) {{
      if (cat === 'all' || card.dataset.cat === cat) {{
        card.style.display = 'flex';
      }} else {{
        card.style.display = 'none';
      }}
    }});
  }});
}});

// FAQ Accordion & Search
document.querySelectorAll('.faq-btn').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    var card = btn.closest('.faq-card');
    card.classList.toggle('open');
  }});
}});

var searchInput = document.getElementById('faqSearchInput');
var faqCards = document.querySelectorAll('.faq-card');

function filterFAQ() {{
  var query = searchInput.value.toLowerCase().trim();

  faqCards.forEach(function(card) {{
    var text = card.textContent.toLowerCase();
    var matchesQuery = query === '' || text.includes(query);

    if (matchesQuery) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}

searchInput.addEventListener('input', filterFAQ);

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
<script src="/local-navigation.js?v=20260901-baza-blog-v7" defer></script>
</body>
</html>
"""

with open(baza_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully created 16 article blog grid with unique photos and relocated calculator below.")
