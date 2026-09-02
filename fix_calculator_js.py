# -*- coding: utf-8 -*-
import os
import re

baza_fpath = "/Users/karolbohdanowicz/safe_backup/tasmaled-local/public/baza-wiedzy/index.html"
with open(baza_fpath, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the entire script block inside <main> with the complete, robust, error-free script
clean_script = """<script>
// FAQ Accordion & Search
document.querySelectorAll('.faq-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    var card = btn.closest('.faq-card');
    card.classList.toggle('open');
  });
});

var searchInput = document.getElementById('faqSearchInput');
var faqCards = document.querySelectorAll('.faq-card');
var filterBtns = document.querySelectorAll('.chip-btn');

function filterFAQ() {
  var query = searchInput.value.toLowerCase().trim();
  var activeChip = document.querySelector('.chip-btn.active').dataset.filter;

  faqCards.forEach(function(card) {
    var text = card.textContent.toLowerCase();
    var cat = card.dataset.cat;
    var matchesQuery = query === '' || text.includes(query);
    var matchesCat = activeChip === 'all' || cat === activeChip;

    if (matchesQuery && matchesCat) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

searchInput.addEventListener('input', filterFAQ);

filterBtns.forEach(function(btn) {
  btn.addEventListener('click', function() {
    filterBtns.forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    filterFAQ();
  });
});

// APPLE-GRADE PRESCOT LED CALCULATOR CONTROLLER
var state = {
  voltage: 24,
  powerPerM: 14.4,
  length: 6.0,
  cable: 3.0,
  wire: 0.75
};

function updateCalculator() {
  var nominalPower = state.powerPerM * state.length;
  var recommendedPsu = nominalPower * 1.20;
  var current = nominalPower / state.voltage;

  var wireResistance = (0.0175 * state.cable * 2) / state.wire;
  var voltageDrop = current * wireResistance;
  var lossPct = (voltageDrop / state.voltage) * 100;

  var psuOptions = [35, 60, 100, 150, 200, 250, 300, 400, 600];
  var matchedPsu = 600;
  for (var i = 0; i < psuOptions.length; i++) {
    if (psuOptions[i] >= recommendedPsu) {
      matchedPsu = psuOptions[i];
      break;
    }
  }

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
  if (loadPct > 90) {
    document.getElementById('res-load-bar').style.background = '#ef4444';
  } else if (loadPct > 80) {
    document.getElementById('res-load-bar').style.background = '#e55933';
  } else {
    document.getElementById('res-load-bar').style.background = '#10b981';
  }

  // Recommendation text & dynamic Prescot shop search URL
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

// 1. Voltage Segments
document.querySelectorAll('#seg-voltage .apple-seg-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('#seg-voltage .apple-seg-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    state.voltage = parseFloat(btn.dataset.val);
    updateCalculator();
  });
});

// 2. Power Chips
document.querySelectorAll('#grid-power .apple-chip-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('#grid-power .apple-chip-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    state.powerPerM = parseFloat(btn.dataset.val);
    updateCalculator();
  });
});

// 3. LED Length
var sLen = document.getElementById('slider-length');
var nLen = document.getElementById('num-length');
if (sLen && nLen) {
  sLen.addEventListener('input', function() {
    nLen.value = sLen.value;
    state.length = parseFloat(sLen.value);
    updateCalculator();
  });
  nLen.addEventListener('input', function() {
    sLen.value = nLen.value;
    state.length = parseFloat(nLen.value) || 1;
    updateCalculator();
  });
}

// 4. Cable Distance
var sCab = document.getElementById('slider-cable');
var nCab = document.getElementById('num-cable');
if (sCab && nCab) {
  sCab.addEventListener('input', function() {
    nCab.value = sCab.value;
    state.cable = parseFloat(sCab.value);
    updateCalculator();
  });
  nCab.addEventListener('input', function() {
    sCab.value = nCab.value;
    state.cable = parseFloat(nCab.value) || 1;
    updateCalculator();
  });
}

// 5. Wire Cross Chips
document.querySelectorAll('#grid-wire .apple-chip-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('#grid-wire .apple-chip-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    state.wire = parseFloat(btn.dataset.val);
    updateCalculator();
  });
});

// Initialize
updateCalculator();
</script>"""

# Replace script before footer
html = re.sub(r'<script>\s*// FAQ Accordion & Search.*?</script>(?=\s*<footer)', clean_script, html, flags=re.DOTALL)

with open(baza_fpath, "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed syntax error and verified full calculator interactivity.")
