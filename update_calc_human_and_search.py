# -*- coding: utf-8 -*-
import os
import re

baza_fpath = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/baza-wiedzy/index.html"
with open(baza_fpath, "r", encoding="utf-8") as f:
    html = f.read()

# Replace recommendation card HTML
old_rec_card = re.search(r'<div class="calc-rec-card">.*?</div>\s*</div>\s*</div>\s*</section>', html, re.DOTALL)

new_rec_card = """<div class="calc-rec-card">
          <div class="calc-rec-tag">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            Dobieramy dla Ciebie
          </div>
          <div class="calc-rec-title" id="rec-psu-name">Zasilacz Prescot Ultra Slim 150W 24V</div>
          <p class="calc-rec-desc" id="rec-psu-text">Idealnie dobrana moc z bezpiecznym zapasem. Zasilacz nie będzie się przegrzewał, ma zabezpieczenia przed spięciem i posłuży na lata. Twój odcinek taśmy możesz bez problemu podłączyć z jednej strony.</p>
          <a href="https://www.prescot.com.pl/?s=zasilacz+150w+24v&post_type=product" id="rec-psu-link" target="_blank" rel="noopener" class="p-btn p-btn-primary calc-rec-btn">
            Kup ten zasilacz w sklepie &rarr;
          </a>
        </div>
      </div>
    </div>
  </section>"""

if old_rec_card:
    html = html[:old_rec_card.start()] + new_rec_card + html[old_rec_card.end():]

# Replace JS logic for recommendation text and dynamic search URL
js_update_old = re.search(r'// Recommendation text.*?updateCalculator\(\);', html, re.DOTALL)

js_update_new = """// Recommendation text & dynamic Prescot shop search URL
  var modelName = 'Zasilacz Prescot Ultra Slim ' + matchedPsu + 'W ' + state.voltage + 'V';
  document.getElementById('rec-psu-name').textContent = modelName;

  var advice = 'Idealnie dobrana moc z 20% bezpiecznego zapasu. Zasilacz nie będzie się przegrzewał, ma zabezpieczenia przed zwarciem i posłuży na lata. ';
  if (state.voltage === 12 && state.length > 5) {
    advice += 'Wskazówka: przy taśmie 12V i długości ' + state.length.toFixed(1) + 'm warto podpiąć zasilanie z obu stron, żeby na końcu taśmy nie tracić jasności.';
  } else if (lossPct > 3.0) {
    advice += 'Wskazówka: przewód ma ' + state.cable.toFixed(1) + 'm — wybierz grubszy kabel (np. 1.50 mm²), aby taśma świeciła pełną jasnością.';
  } else {
    advice += 'Twój odcinek ' + state.length.toFixed(1) + 'm możesz bez problemu podłączyć z jednej strony.';
  }
  document.getElementById('rec-psu-text').textContent = advice;

  // Dynamic search URL to prescot.com.pl
  var searchUrl = 'https://www.prescot.com.pl/?s=zasilacz+' + matchedPsu + 'w+' + state.voltage + 'v&post_type=product';
  var btnLink = document.getElementById('rec-psu-link');
  if (btnLink) {
    btnLink.href = searchUrl;
    btnLink.innerHTML = 'Kup zasilacz ' + matchedPsu + 'W w sklepie &rarr;';
  }
}

// 1. Voltage Segments"""

if js_update_old:
    html = html[:js_update_old.start()] + js_update_new + html[js_update_old.end():]

with open(baza_fpath, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated recommendation card with human copy and dynamic store search link.")
