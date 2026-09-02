# -*- coding: utf-8 -*-
import re

c1_left = "/wp-content/uploads/2026/03/12d018-010-10-wl_4-2.webp"
c1_right = "/wp-content/uploads/2026/03/OKLAD-112d018-010-10-wl_1-2.webp"
c2_left = "/wp-content/uploads/2026/03/12D018-010-10-_1212D018-010-10-.webp"
c2_right = "/wp-content/uploads/2026/03/12D018-010-10-_1912D018-010-10-.webp"
c3_left = "/wp-content/uploads/2026/03/OKL-212d018-010-10-wl_612d018-010-10-wl.webp"
c3_right = "/wp-content/uploads/2026/03/12D018-010-10-_3112D018-010-10-.webp"
c4_left = "/wp-content/uploads/2026/03/12D018-010-10-_412D018-010-10-.webp"
c4_right = "/wp-content/uploads/2026/03/12D018-010-10-_2012D018-010-10-.webp"

for filepath in ["/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/onecut/index.html", "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/onecut.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 2e7f411c (card1 left - HERO)
    content = re.sub(r'(data-id="2e7f411c"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c1_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="2e7f411c"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c1_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="2e7f411c"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c1_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="2e7f411c"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c1_left + r'\2', content, flags=re.DOTALL)

    # 37085f3 (card1 right)
    content = re.sub(r'(data-id="37085f3"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c1_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="37085f3"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c1_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="37085f3"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c1_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="37085f3"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c1_right + r'\2', content, flags=re.DOTALL)

    # 1d3d2544 (card2 left)
    content = re.sub(r'(data-id="1d3d2544"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c2_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="1d3d2544"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c2_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="1d3d2544"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c2_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="1d3d2544"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c2_left + r'\2', content, flags=re.DOTALL)

    # 376d34f7 (card2 right)
    content = re.sub(r'(data-id="376d34f7"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c2_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="376d34f7"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c2_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="376d34f7"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c2_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="376d34f7"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c2_right + r'\2', content, flags=re.DOTALL)

    # d79d0aa (card3 left)
    content = re.sub(r'(data-id="d79d0aa"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c3_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="d79d0aa"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c3_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="d79d0aa"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c3_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="d79d0aa"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c3_left + r'\2', content, flags=re.DOTALL)

    # e966e83 (card3 right)
    content = re.sub(r'(data-id="e966e83"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c3_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="e966e83"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c3_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="e966e83"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c3_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="e966e83"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c3_right + r'\2', content, flags=re.DOTALL)

    # 5fea4c7 (card4 left)
    content = re.sub(r'(data-id="5fea4c7"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c4_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="5fea4c7"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c4_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="5fea4c7"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c4_left + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="5fea4c7"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c4_left + r'\2', content, flags=re.DOTALL)

    # fcf8d9d (card4 right)
    content = re.sub(r'(data-id="fcf8d9d"[^>]*>.*?<img[^>]+src=")[^"]+(")', r'\g<1>' + c4_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="fcf8d9d"[^>]*>.*?<img[^>]+data-src=")[^"]+(")', r'\g<1>' + c4_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="fcf8d9d"[^>]*>.*?srcset=")[^"]+(")', r'\g<1>' + c4_right + r'\2', content, flags=re.DOTALL)
    content = re.sub(r'(data-id="fcf8d9d"[^>]*>.*?data-srcset=")[^"]+(")', r'\g<1>' + c4_right + r'\2', content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated One Cut images in:", filepath)
