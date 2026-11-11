/* marks_data.js — the expanded heraldry, data-driven.
   The nineteen curated originals above remain hand-authored in the HTML.
   This appends the wider roster and installs the control strip: tabs by
   region, filters by country / type / class, and a live operation search
   that lights only the services carrying a matching operation. Every sigil
   is an original abstraction — no official insignia is reproduced, and
   nothing of an atrocity apparatus is ever drawn. Conduct is graded per
   institution, on documented record; the wall grades organizations, never
   peoples. Display is not endorsement; the condemned hang barred.

   Class: craft (studied for tradecraft) · grau (craft and stain in one
   record) · cond (instruments of atrocity, under abatement).
   Fields: nm, country, region, type, era, cls, kf, rec, sigil (SVG inner),
   ops [{name, year, note}]. */
(function () {
  "use strict";

  // sigils — small original abstractions, deliberately generic
  var S = {
    star: '<path d="M22,6 L26,18 L38,22 L26,26 L22,38 L18,26 L6,22 L18,18 Z"/><circle cx="22" cy="22" r="2.2"/>',
    eye: '<path d="M8,22 Q22,10 36,22 Q22,34 8,22Z"/><circle cx="22" cy="22" r="4"/>',
    shield: '<path d="M22,7 L34,12 V22 Q34,32 22,37 Q10,32 10,22 V12 Z"/>',
    tower: '<rect x="16" y="12" width="12" height="24"/><path d="M16,12 L22,6 L28,12 M14,36 H30"/>',
    wave: '<path d="M6,20 Q14,12 22,20 T38,20 M6,28 Q14,20 22,28 T38,28"/>',
    key: '<circle cx="15" cy="22" r="7"/><path d="M22,22 H36 M32,22 V28 M36,22 V27"/>',
    bear: '<circle cx="22" cy="24" r="12"/><circle cx="14" cy="12" r="4"/><circle cx="30" cy="12" r="4"/>',
    sword: '<path d="M22,6 V30 M16,30 H28 M18,34 H26"/>',
    net: '<path d="M10,10 H34 V34 H10 Z M10,18 H34 M10,26 H34 M18,10 V34 M26,10 V34"/>',
    lotus: '<path d="M22,8 Q28,18 22,30 Q16,18 22,8 M12,20 Q18,26 22,30 M32,20 Q26,26 22,30"/>',
    crescent: '<path d="M30,10 A13,13 0 1 0 30,34 A10,10 0 1 1 30,10Z"/>',
    triangle: '<path d="M22,8 L34,32 H10 Z"/><path d="M22,18 V26"/>',
    compass: '<circle cx="22" cy="22" r="13"/><path d="M22,10 L26,22 L22,34 L18,22 Z"/>',
    cog: '<circle cx="22" cy="22" r="9"/><path d="M22,7 V11 M22,33 V37 M7,22 H11 M33,22 H37 M11,11 L14,14 M33,11 L30,14 M11,33 L14,30 M33,33 L30,30"/>',
    scroll: '<path d="M14,10 H30 V34 H14 Z M14,10 Q10,10 10,14 M30,34 Q34,34 34,30"/>',
    flame: '<path d="M22,6 Q30,16 24,24 Q28,20 22,34 Q16,20 20,24 Q14,16 22,6Z"/>',
    grid: '<circle cx="15" cy="22" r="6"/><circle cx="22" cy="22" r="6"/><circle cx="29" cy="22" r="6"/>',
    delta: '<path d="M22,7 L32,22 L22,37 L12,22 Z"/><path d="M22,14 Q26,20 22,26 Q18,20 22,14"/>'
  };

  var ROSTER = [
    // ---- North America
    { nm: "NSA", country: "United States", region: "North America",
      type: "SIGINT", era: "1952–", cls: "grau", sigil: S.eye,
      kf: "Signals at planetary scale; the largest collector ever built.",
      rec: "Unmatched cryptologic reach; its bulk-collection era its lasting scar.",
      ops: [{ name: "VENONA", year: "1943", note: "Soviet cable decryption, decades long." },
            { name: "Bullrun", year: "2013", note: "Countering commercial encryption; disclosed by Snowden." }] },
    { nm: "FBI Counterintelligence", country: "United States", region: "North America",
      type: "Domestic / CI", era: "1908–", cls: "grau", sigil: S.shield,
      kf: "Federal law enforcement with a counterintelligence mandate at home.",
      rec: "Broke major spy rings; COINTELPRO its documented abuse of the tool.",
      ops: [{ name: "COINTELPRO", year: "1956", note: "Domestic disruption of political groups; later condemned." },
            { name: "Ghost Stories", year: "2010", note: "Rolled up a deep-cover Russian illegals network." }] },
    { nm: "DIA", country: "United States", region: "North America",
      type: "Military", era: "1961–", cls: "craft", sigil: S.compass,
      kf: "Defense-wide military intelligence, all-source.",
      rec: "The Pentagon's own analytic corps; measured by the wars it read.",
      ops: [] },
    { nm: "CSIS", country: "Canada", region: "North America",
      type: "Domestic / CI", era: "1984–", cls: "craft", sigil: S.tower,
      kf: "Civilian service split from the RCMP after a commission of inquiry.",
      rec: "Born of oversight reform — a service created by cleaning one up.",
      ops: [] },
    { nm: "CSE", country: "Canada", region: "North America",
      type: "SIGINT", era: "1946–", cls: "craft", sigil: S.wave,
      kf: "Canada's signals arm and Five Eyes node.",
      rec: "Quiet partner in the anglophone collection alliance.",
      ops: [] },

    // ---- Europe
    { nm: "KGB", country: "Soviet Union", region: "Europe",
      type: "State security", era: "1954–1991", cls: "cond", sigil: S.star,
      kf: "Sword and shield of the party: foreign intelligence and internal terror in one body.",
      rec: "Vast tradecraft inseparable from the gulag apparatus it served.",
      ops: [{ name: "Operation RYAN", year: "1981", note: "Alert for a feared NATO first strike." },
            { name: "Active measures", year: "—", note: "Systematic disinformation abroad." }] },
    { nm: "Stasi", country: "East Germany", region: "Europe",
      type: "State security", era: "1950–1990", cls: "cond", sigil: S.net,
      kf: "The most saturated surveillance of a population in the modern record.",
      rec: "Zersetzung — the deliberate psychological destruction of citizens; condemned.",
      ops: [{ name: "Zersetzung", year: "—", note: "Decomposition: covert ruin of targeted lives." }] },
    { nm: "SVR", country: "Russia", region: "Europe",
      type: "Foreign intelligence", era: "1991–", cls: "grau", sigil: S.bear,
      kf: "The KGB First Directorate's foreign-intelligence successor.",
      rec: "Illegals and influence abroad; the lineage's outward face.",
      ops: [{ name: "Illegals Program", year: "2010", note: "Long-term deep-cover officers exposed in the US." }] },
    { nm: "GRU", country: "Russia", region: "Europe",
      type: "Military", era: "1918–", cls: "cond", sigil: S.sword,
      kf: "Military intelligence with its own special-operations reach.",
      rec: "Documented assassinations and sabotage abroad; graded on that conduct.",
      ops: [{ name: "Salisbury", year: "2018", note: "Novichok poisoning attributed to GRU officers." }] },
    { nm: "BND", country: "Germany", region: "Europe",
      type: "Foreign intelligence", era: "1956–", cls: "grau", sigil: S.compass,
      kf: "Federal foreign service grown from the Gehlen Organization.",
      rec: "Cold-War reach shadowed by its ex-Wehrmacht founding cadre.",
      ops: [] },
    { nm: "Mossad", country: "Israel", region: "Middle East",
      type: "Foreign intelligence", era: "1949–", cls: "grau", sigil: S.star,
      kf: "Small service, outsized operational reputation.",
      rec: "Celebrated captures and contested killings in one ledger.",
      ops: [{ name: "Finale (Eichmann)", year: "1960", note: "Capture of Adolf Eichmann in Argentina." },
            { name: "Wrath of God", year: "1972", note: "Killings after the Munich massacre; disputed." }] },
    { nm: "DGSE", country: "France", region: "Europe",
      type: "Foreign intelligence", era: "1982–", cls: "grau", sigil: S.key,
      kf: "France's external service, action and intelligence branches.",
      rec: "Reach across Françafrique; Rainbow Warrior its self-inflicted scandal.",
      ops: [{ name: "Rainbow Warrior", year: "1985", note: "Sinking of a Greenpeace vessel; an operative killed." }] },
    { nm: "MSS", country: "China", region: "Asia",
      type: "State security", era: "1983–", cls: "grau", sigil: S.eye,
      kf: "Civilian intelligence and security, foreign and domestic fused.",
      rec: "Industrial-scale collection; opacity is itself part of the record.",
      ops: [{ name: "APT-linked intrusion sets", year: "—", note: "Cyber-espionage campaigns attributed to MSS contractors." }] },

    // ---- Asia
    { nm: "R&AW", country: "India", region: "Asia",
      type: "Foreign intelligence", era: "1968–", cls: "craft", sigil: S.lotus,
      kf: "External service formed after intelligence failures in war.",
      rec: "Regional reach built the hard way, from a bad surprise.",
      ops: [] },
    { nm: "ISI", country: "Pakistan", region: "Asia",
      type: "Military / Foreign", era: "1948–", cls: "grau", sigil: S.crescent,
      kf: "Powerful military-intelligence directorate with deep regional role.",
      rec: "Kingmaker at home; proxy ties abroad shadow the craft.",
      ops: [] },
    { nm: "PSIA / Naichō", country: "Japan", region: "Asia",
      type: "Domestic / Cabinet", era: "1952–", cls: "craft", sigil: S.grid,
      kf: "Japan's constrained, oversight-bound intelligence apparatus.",
      rec: "A deliberately limited service in a constitutional cage.",
      ops: [] },
    { nm: "NIS", country: "South Korea", region: "Asia",
      type: "Foreign / Domestic", era: "1961–", cls: "grau", sigil: S.tower,
      kf: "Reorganized repeatedly from the KCIA's authoritarian roots.",
      rec: "Reformed toward oversight after a heavy-handed lineage.",
      ops: [] },

    // ---- Middle East / Africa
    { nm: "GID (Mukhabarat)", country: "Jordan", region: "Middle East",
      type: "Foreign / Domestic", era: "1964–", cls: "craft", sigil: S.crescent,
      kf: "Regionally respected liaison and counterterror service.",
      rec: "Trusted partner reputation across a hard neighborhood.",
      ops: [] },
    { nm: "BOSS", country: "South Africa", region: "Africa",
      type: "State security", era: "1969–1980", cls: "cond", sigil: S.triangle,
      kf: "Apartheid-era security service, instrument of the regime.",
      rec: "Repression and cross-border operations for apartheid; condemned.",
      ops: [] },

    // ---- South America / Oceania
    { nm: "DINA", country: "Chile", region: "South America",
      type: "State security", era: "1973–1977", cls: "cond", sigil: S.flame,
      kf: "Pinochet's secret police; the junta's coercive core.",
      rec: "Condor killings and disappearances; an atrocity apparatus, barred.",
      ops: [{ name: "Operation Condor", year: "1975", note: "Cross-border assassination pact of Southern-Cone regimes." }] },
    { nm: "ASIS", country: "Australia", region: "Oceania",
      type: "Foreign intelligence", era: "1952–", cls: "craft", sigil: S.wave,
      kf: "Australia's external service and Five Eyes partner.",
      rec: "Quiet regional collection under the anglophone umbrella.",
      ops: [] },
    { nm: "GCSB", country: "New Zealand", region: "Oceania",
      type: "SIGINT", era: "1977–", cls: "craft", sigil: S.wave,
      kf: "New Zealand's signals bureau; the smallest Five Eyes node.",
      rec: "Collection recalibrated after domestic surveillance findings.",
      ops: [] }
  ];

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function cardHTML(m) {
    var ops = (m.ops || []).map(function (o) {
      return '<li><b>' + esc(o.name) + '</b>' +
        (o.year && o.year !== "—" ? ' <span class="oy">' + esc(o.year) + '</span>' : '') +
        (o.note ? ' — ' + esc(o.note) : '') + '</li>';
    }).join("");
    var opsBlock = ops
      ? '<details class="ops"><summary>known operations</summary><ul>' + ops + '</ul></details>'
      : '';
    var opsAttr = (m.ops || []).map(function (o) { return o.name; }).join(" ｜ ");
    return '<div class="card ' + m.cls + '" data-region="' + esc(m.region) +
      '" data-country="' + esc(m.country) + '" data-type="' + esc(m.type) +
      '" data-cls="' + m.cls + '" data-ops="' + esc(opsAttr) + '">' +
      '<svg viewBox="0 0 44 44" fill="none" stroke="currentColor" ' +
      'stroke-width="1.6" aria-hidden="true">' + m.sigil + '</svg><div>' +
      '<p class="nm">' + esc(m.nm) + '</p>' +
      '<p class="meta">' + esc(m.country) + ' · ' + esc(m.era) + ' · ' + esc(m.type) + '</p>' +
      '<span class="cls ' + m.cls + '">' +
      (m.cls === "cond" ? "CONDEMNED" : m.cls === "grau" ? "GRAU" : "CRAFT") +
      '</span>' +
      '<p class="kf">' + esc(m.kf) + '</p><p class="rec">' + esc(m.rec) + '</p>' +
      opsBlock + '</div></div>';
  }

  function boot() {
    var host = document.getElementById("roster");
    if (!host) return;
    host.innerHTML = ROSTER.map(cardHTML).join("");

    var regions = ["All"].concat(
      ROSTER.map(function (m) { return m.region; })
        .filter(function (v, i, a) { return a.indexOf(v) === i; }).sort());
    var strip = document.getElementById("markctl");
    var tabs = regions.map(function (r) {
      return '<button class="mtab' + (r === "All" ? " on" : "") +
        '" data-region="' + esc(r) + '">' + esc(r) + '</button>';
    }).join("");
    var types = ["all types"].concat(
      ROSTER.map(function (m) { return m.type; })
        .filter(function (v, i, a) { return a.indexOf(v) === i; }).sort());
    var typeSel = '<select id="mtype">' + types.map(function (t) {
      return '<option value="' + (t === "all types" ? "" : esc(t)) + '">' +
        esc(t) + '</option>';
    }).join("") + '</select>';
    strip.innerHTML =
      '<div class="mtabs">' + tabs + '</div>' +
      '<div class="mfilters">' +
      '<input id="mq" placeholder="search operation or service…" ' +
      'aria-label="search operations and services">' + typeSel +
      '<select id="mcls"><option value="">all classes</option>' +
      '<option value="craft">CRAFT</option><option value="grau">GRAU</option>' +
      '<option value="cond">CONDEMNED</option></select>' +
      '<span id="mcount" class="mcount"></span></div>';

    var cards = [].slice.call(host.querySelectorAll(".card"));
    var region = "All";
    function apply() {
      var q = (document.getElementById("mq").value || "").toLowerCase();
      var ty = document.getElementById("mtype").value;
      var cl = document.getElementById("mcls").value;
      var shown = 0;
      cards.forEach(function (c) {
        var ok = (region === "All" || c.dataset.region === region) &&
          (!ty || c.dataset.type === ty) &&
          (!cl || c.dataset.cls === cl) &&
          (!q || (c.dataset.ops.toLowerCase().indexOf(q) >= 0 ||
            c.textContent.toLowerCase().indexOf(q) >= 0));
        c.style.display = ok ? "" : "none";
        if (ok) shown++;
      });
      document.getElementById("mcount").textContent =
        shown + " of " + cards.length + " shown";
    }
    strip.querySelectorAll(".mtab").forEach(function (b) {
      b.addEventListener("click", function () {
        strip.querySelectorAll(".mtab").forEach(function (x) {
          x.classList.remove("on"); });
        b.classList.add("on"); region = b.dataset.region; apply();
      });
    });
    ["mq", "mtype", "mcls"].forEach(function (id) {
      document.getElementById(id).addEventListener("input", apply);
      document.getElementById(id).addEventListener("change", apply);
    });
    apply();
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
