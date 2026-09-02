import re

with open("kontakt/index.html", "r") as f:
    text = f.read()

# For kontakt, find where <main id="main"> starts
start = text.find('<main id="main">')
if start == -1:
    start = text.find('<div class="page-glow')

# The end is before `<nav class="prescot-dock"` or `<footer`
end = text.find('<footer')
if end == -1:
    end = text.find('<nav class="prescot-dock"')

print("Kontakt unique content length:", len(text[start:end]))
