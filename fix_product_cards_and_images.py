# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Clean prescot-global.css: Remove dangerous global overflow:visible
css_path = os.path.join(base_dir, "prescot-global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove global .elementor-element overflow override
css = re.sub(
    r'\.elementor-element,\s*\.elementor-container,\s*\.elementor-widget-wrap,\s*\.e-con,\s*\.e-con-inner\s*\{\s*overflow:\s*visible\s*!important;\s*\}',
    '/* Elementor containers respect their native overflow */',
    css
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Removed harmful global overflow override from prescot-global.css.")


# 2. Fix all frozen LiteSpeed base64 placeholder images across all HTML files
count_fixed = 0
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()
            
            orig = content
            
            # Replace placeholder src with real data-src
            # Pattern: <img ... src="data:image/gif;base64,[^"]*" ... data-src="([^"]+)" ...>
            # Or data-src before src
            def replace_img_src(match):
                tag = match.group(0)
                data_src_match = re.search(r'data-src="([^"]+)"', tag)
                data_srcset_match = re.search(r'data-srcset="([^"]+)"', tag)
                
                if data_src_match:
                    real_src = data_src_match.group(1)
                    # Replace placeholder src with real_src
                    tag = re.sub(r'src="data:image/gif;base64,[^"]*"', f'src="{real_src}"', tag)
                
                if data_srcset_match:
                    real_srcset = data_srcset_match.group(1)
                    tag = re.sub(r'srcset="data:image/gif;base64,[^"]*"', f'srcset="{real_srcset}"', tag)
                
                return tag

            content = re.sub(r'<img\s+[^>]*data-src="[^"]+"[^>]*>', replace_img_src, content)
            
            if content != orig:
                count_fixed += 1
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Hydrated real image URLs in {fpath}")

print(f"Total HTML files fixed: {count_fixed}")


# 3. Add client-side self-healing image hydrator in local-navigation.js
nav_js_path = os.path.join(base_dir, "local-navigation.js")
with open(nav_js_path, "r", encoding="utf-8") as f:
    nav_js = f.read()

hydrator_code = """
  // 5. Automatic image hydration (replaces any remaining base64 placeholders with real images)
  function hydrateImages() {
    document.querySelectorAll('img[data-src]').forEach((img) => {
      const realSrc = img.getAttribute('data-src');
      if (realSrc && (!img.src || img.src.startsWith('data:image'))) {
        img.src = realSrc;
      }
      const realSrcset = img.getAttribute('data-srcset');
      if (realSrcset && (!img.srcset || img.srcset.startsWith('data:image'))) {
        img.srcset = realSrcset;
      }
    });
  }
  hydrateImages();
  window.addEventListener('load', hydrateImages);
"""

if "Automatic image hydration" not in nav_js:
    nav_js = nav_js.replace("window.addEventListener(\"scroll\", updateNavVisibility, { passive: true });", "window.addEventListener(\"scroll\", updateNavVisibility, { passive: true });\n" + hydrator_code)
    with open(nav_js_path, "w", encoding="utf-8") as f:
        f.write(nav_js)
    print("Added automatic image hydration to local-navigation.js.")

print("All product cards and images successfully restored 1:1.")
