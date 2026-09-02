# -*- coding: utf-8 -*-
import re

# Exact image mapping based on user Finder screenshot
# Card 1: Hero (Glowing illuminated mood shot on dark background + Cover 1)
# Card 2: One Cut 10mm cutting shots
# Card 3: Detail & tape peel
# Card 4: Macro LED & full spool

pairs = [
    ("2e7f411c", "/wp-content/uploads/2026/03/12D018-010-10-_412D018-010-10-.webp"), # HERO GŁÓWNY - ŚWIECĄCA TAŚMA W MROKU
    ("37085f3", "/wp-content/uploads/2026/03/OKLAD-112d018-010-10-wl_1-2.webp"),        # Karta 1 Prawa (Okładka 1)
    ("1d3d2544", "/wp-content/uploads/2026/03/12D018-010-10-_1912D018-010-10-.webp"), # Karta 2 Lewa (Cięcie nożyczkami)
    ("376d34f7", "/wp-content/uploads/2026/03/12D018-010-10-_2612D018-010-10-.webp"), # Karta 2 Prawa (Cięcie precyzyjne)
    ("d79d0aa", "/wp-content/uploads/2026/03/OKL-212d018-010-10-wl_612d018-010-10-wl.webp"), # Karta 3 Lewa (Okładka 2)
    ("e966e83", "/wp-content/uploads/2026/03/12D018-010-10-_3112D018-010-10-.webp"), # Karta 3 Prawa (Taśma 3M)
    ("5fea4c7", "/wp-content/uploads/2026/03/12d018-010-10-wl_4-2.webp"),              # Karta 4 Lewa (Makro detal)
    ("fcf8d9d", "/wp-content/uploads/2026/03/12D018-010-10-_1212D018-010-10-.webp")  # Karta 4 Prawa (Rolka na szpuli)
]

for filepath in [
    "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/onecut/index.html",
    "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/onecut.html"
]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    for widget_id, img_url in pairs:
        pattern = rf'(data-id="{widget_id}"[^>]*>.*?<div class="elementor-widget-container">)(.*?)(<\/div>\s*<\/div>)'
        
        def make_repl(m, url=img_url):
            header = m.group(1)
            closer = m.group(3)
            new_img = f'''
<img src="{url}" data-src="{url}" alt="Prescot Delux OneCut 12V" class="attachment-large size-large" loading="lazy" decoding="async" />
'''
            return header + new_img + closer

        content = re.sub(pattern, make_repl, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated hero and all cards in:", filepath)

# Also update the card in /tasmy-led/ catalog
tasmy_path = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/tasmy-led/index.html"
if True:
    with open(tasmy_path, "r", encoding="utf-8") as f:
        t_content = f.read()
    
    # Replace onecut thumbnail in catalog to glowing shot
    t_content = t_content.replace(
        '/wp-content/uploads/2026/03/12d018-010-10-wl_4-2.webp',
        '/wp-content/uploads/2026/03/12D018-010-10-_412D018-010-10-.webp'
    )
    with open(tasmy_path, "w", encoding="utf-8") as f:
        f.write(t_content)
    print("Updated One Cut thumbnail in /tasmy-led/")
