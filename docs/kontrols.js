/* kontrols.js — KONSOLE KONTROLS for the desk's data surfaces.
   One file, no dependencies, no data leaves the page. Table mode: any
   .tablewrap table with enough rows gains a control strip — live text
   search, facet filters for low-cardinality columns, click-to-sort headers
   (numeric-, percent-, and date-aware), and a shown-of-total count. Node
   mode: pages carrying the ForeKaster's .node tree gain a filter lamp that
   dims non-matching nodes and their map markers in place. Enhancement only:
   with scripts off, every page reads exactly as before. */
(function () {
  "use strict";
  var LINE = "#26292f", DIM = "#7d838c", BRASS = "#dcb65e";

  function mk(tag, css, txt) {
    var e = document.createElement(tag);
    if (css) e.style.cssText = css;
    if (txt !== undefined) e.textContent = txt;
    return e;
  }
  function cellVal(td) { return (td.textContent || "").trim(); }
  function sortKey(v) {
    var s = v.replace(/[%$,]/g, "");
    if (/^\d{4}-\d{2}-\d{2}/.test(s)) return { t: 1, v: s };
    var f = parseFloat(s);
    if (!isNaN(f) && /^[\d.\-+]/.test(s)) return { t: 0, v: f };
    return { t: 2, v: v.toLowerCase() };
  }

  function enhanceTable(tb) {
    var body = tb.tBodies[0];
    if (!body || body.rows.length < 7 || !tb.tHead) return;
    var rows = [].slice.call(body.rows);
    var heads = [].slice.call(tb.tHead.rows[0].cells);

    var strip = mk("div",
      "display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;" +
      "margin:.4rem 0 .5rem;font-size:.72rem;font-family:inherit");
    var q = mk("input",
      "background:transparent;border:1px solid " + LINE + ";color:inherit;" +
      "padding:.28rem .5rem;font:inherit;font-size:.72rem;min-width:11rem");
    q.placeholder = "filter rows…";
    q.setAttribute("aria-label", "filter table rows");
    strip.appendChild(q);

    var sels = [];
    heads.forEach(function (h, ci) {
      var vals = {};
      rows.forEach(function (r) {
        var v = cellVal(r.cells[ci] || {});
        if (v && v.length <= 24) vals[v] = 1;
      });
      var ks = Object.keys(vals);
      if (ks.length >= 2 && ks.length <= 8 && rows.length / ks.length >= 2) {
        var s = mk("select",
          "background:transparent;border:1px solid " + LINE +
          ";color:inherit;padding:.24rem .3rem;font:inherit;font-size:.72rem");
        s.setAttribute("aria-label", "filter by " + cellVal(h));
        s.appendChild(new Option("all " + cellVal(h).toLowerCase(), ""));
        ks.sort().forEach(function (k) { s.appendChild(new Option(k, k)); });
        s.dataset.col = ci;
        strip.appendChild(s);
        sels.push(s);
      }
    });
    var count = mk("span", "color:" + DIM + ";margin-left:auto");
    strip.appendChild(count);

    function apply() {
      var needle = q.value.toLowerCase(), shown = 0;
      rows.forEach(function (r) {
        var ok = !needle || r.textContent.toLowerCase().indexOf(needle) >= 0;
        if (ok) sels.forEach(function (s) {
          if (s.value && cellVal(r.cells[+s.dataset.col] || {}) !== s.value)
            ok = false;
        });
        r.style.display = ok ? "" : "none";
        if (ok) shown++;
      });
      count.textContent = shown === rows.length
        ? rows.length + " rows"
        : shown + " of " + rows.length + " shown";
    }
    q.addEventListener("input", apply);
    sels.forEach(function (s) { s.addEventListener("change", apply); });

    heads.forEach(function (h, ci) {
      h.style.cursor = "pointer";
      h.title = "sort";
      h.addEventListener("click", function () {
        var dir = h.dataset.dir === "asc" ? -1 : 1;
        heads.forEach(function (x) { delete x.dataset.dir;
          x.textContent = x.textContent.replace(/ [▲▼]$/, ""); });
        h.dataset.dir = dir === 1 ? "asc" : "desc";
        h.textContent += dir === 1 ? " ▲" : " ▼";
        rows.sort(function (a, b) {
          var ka = sortKey(cellVal(a.cells[ci] || {})),
              kb = sortKey(cellVal(b.cells[ci] || {}));
          if (ka.t !== kb.t) return (ka.t - kb.t) * dir;
          return (ka.v < kb.v ? -1 : ka.v > kb.v ? 1 : 0) * dir;
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });

    var wrap = tb.closest(".tablewrap") || tb;
    wrap.parentNode.insertBefore(strip, wrap);
    apply();
  }

  function enhanceNodes() {
    var nodes = [].slice.call(document.querySelectorAll(".node"));
    if (nodes.length < 6) return;
    var host = nodes[0].parentNode;
    var strip = mk("div",
      "display:flex;gap:.5rem;align-items:center;margin:.4rem 0;" +
      "font-size:.72rem;font-family:inherit");
    var q = mk("input",
      "background:transparent;border:1px solid " + LINE + ";color:inherit;" +
      "padding:.28rem .5rem;font:inherit;font-size:.72rem;min-width:12rem");
    q.placeholder = "filter the board…";
    q.setAttribute("aria-label", "filter nodes and markers");
    var count = mk("span", "color:" + DIM);
    strip.appendChild(q); strip.appendChild(count);
    host.insertBefore(strip, nodes[0]);

    q.addEventListener("input", function () {
      var needle = q.value.toLowerCase(), shown = 0;
      nodes.forEach(function (n) {
        var hit = !needle ||
                  n.textContent.toLowerCase().indexOf(needle) >= 0;
        n.style.opacity = hit ? "" : ".18";
        var id = n.getAttribute("data-id");
        if (id) {
          var m = document.querySelector('.mk[data-id="' +
                    id.replace(/"/g, '\\"') + '"]');
          if (m) m.style.opacity = hit ? "" : "0.06";
        }
        if (hit) shown++;
      });
      count.textContent = needle
        ? shown + " of " + nodes.length + " lit"
        : "";
    });
  }

  function boot() {
    try {
      [].slice.call(document.querySelectorAll(".tablewrap table"))
        .forEach(enhanceTable);
      enhanceNodes();
    } catch (e) { /* enhancement never breaks the page */ }
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
