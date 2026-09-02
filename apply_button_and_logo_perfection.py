# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public"

# 1. Update contact and B2B forms to use submitBtn class for perfect consistency with the footer submit button
for fname in ["wspolpraca-b2b/index.html", "dystrybucja/index.html", "kontakt/index.html"]:
    fpath = os.path.join(base_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        # Update form submit buttons inside main container to use class="submitBtn"
        c = re.sub(r'<button type="submit" class="p-btn p-btn-primary"[^>]*>', '<button type="submit" class="submitBtn">', c)
        c = re.sub(r'<button class="p-btn p-btn-primary" style="width:100%;[^>]*>', '<button class="submitBtn" style="width:100%; justify-content:center;">', c)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated submit buttons in {fname}")

print("All form buttons synchronized with footer submitBtn style.")
