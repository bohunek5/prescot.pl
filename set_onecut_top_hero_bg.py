# -*- coding: utf-8 -*-
import re

hero_bg = "/wp-content/uploads/2026/03/12D018-010-10-_412D018-010-10-.webp"
hero_text = (
    "W serii Delux One Cut moc ustępuje miejsca precyzji w kreowaniu nastroju. "
    "Zamiast płaskiego światła, taśma subtelnie rzeźbi kontury i wydobywa głębię, "
    "tworząc luksusową grę półcieni."
)

custom_style = f"""
<style id="onecut-hero-custom-bg">
.elementor-19751 .elementor-element.elementor-element-19d3d39b,
.elementor-element-19d3d39b {{
  background-color: #000000 !important;
  background-image: linear-gradient(180deg, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.7) 100%), url('{hero_bg}') !important;
  background-position: center center !important;
  background-size: cover !important;
  background-repeat: no-repeat !important;
}}
</style>
"""

pairs = [
    ("2e7f411c", "/wp-content/uploads/2026/03/12d018-010-10-wl_4-2.webp"),             # Karta 1 Lewa (12d018-010-10-wl_4-2)
    ("37085f3", "/wp-content/uploads/2026/03/OKLAD-112d018-010-10-wl_1-2.webp"),        # Karta 1 Prawa (Okładka 1)
    ("1d3d2544", "/wp-content/uploads/2026/03/12D018-010-10-_1912D018-010-10-.webp"), # Karta 2 Lewa (Cięcie nożyczkami)
    ("376d34f7", "/wp-content/uploads/2026/03/12D018-010-10-_2612D018-010-10-.webp"), # Karta 2 Prawa (Cięcie precyzyjne)
    ("d79d0aa", "/wp-content/uploads/2026/03/OKL-212d018-010-10-wl_612d018-010-10-wl.webp"), # Karta 3 Lewa (Okładka 2)
    ("e966e83", "/wp-content/uploads/2026/03/12D018-010-10-_3112D018-010-10-.webp"), # Karta 3 Prawa (Taśma 3M)
    ("5fea4c7", "/wp-content/uploads/2026/03/12D018-010-10-_1212D018-010-10-.webp"), # Karta 4 Lewa (Rolka / szpula)
    ("fcf8d9d", "/wp-content/uploads/2026/03/12D018-010-10-_2012D018-010-10-.webp")  # Karta 4 Prawa (Kontrola cięcia)
]

for filepath in [
    "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/onecut/index.html",
    "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/onecut.html"
]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject or update Hero background style
    if 'id="onecut-hero-custom-bg"' in content:
        content = re.sub(r'<style id="onecut-hero-custom-bg">.*?</style>', custom_style.strip(), content, flags=re.DOTALL)
    else:
        content = content.replace("</head>", custom_style + "\n</head>")

    # 2. Update Top Hero lead text in both desktop and mobile containers
    content = re.sub(
        r'(data-id="11136000".*?<p[^>]*>).*?(<\/p>)',
        r'\g<1>' + hero_text + r'\2',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(data-id="69d90c3".*?<p[^>]*>).*?(<\/p>)',
        r'\g<1>' + hero_text + r'\2',
        content,
        flags=re.DOTALL
    )

    # 3. Update all 4 cards
    for widget_id, img_url in pairs:
        pattern = rf'(data-id="{widget_id}"[^>]*>.*?<div class="elementor-widget-container">)(.*?)(<\/div>\s*<\/div>)'
        def make_repl(m, url=img_url):
            header = m.group(1)
            closer = m.group(3)
            new_img = f'''
<img src="{url}" data-src="{url}" alt="Prescot Delux OneCut" class="attachment-large size-large" loading="lazy" decoding="async" />
'''
            return header + new_img + closer

        content = re.sub(pattern, make_repl, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated top Hero background and cards in:", filepath)
