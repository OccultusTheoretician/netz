/* brand.js — injects the angular field and the viewport reticle.
   No markup edits on any page, no dependency, transform-only motion, and it
   removes itself from the accessibility tree. If this file fails to load the
   pages are unchanged; nothing here is load-bearing. */
(function () {
  "use strict";
  if (document.getElementById("brandbg")) return;
  var reduce = window.matchMedia &&
               window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- the lattice ------------------------------------------------- */
  /* Irregular diagonals rather than a regular grid: a grid reads as graph
     paper, a scatter of hard chords reads as structure under stress. Seeded,
     so the field is identical on every load and every page. */
  function lattice() {
    var W = 1600, H = 1000, seed = 20260727, out = [];
    function rnd() { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return seed / 0x7fffffff; }
    var i, x, y, len, ang, x2, y2, w;
    for (i = 0; i < 46; i++) {
      x = rnd() * W * 1.2 - W * .1;
      y = rnd() * H * 1.2 - H * .1;
      ang = (rnd() < .5 ? 32 : -32) + (rnd() - .5) * 14;
      len = 180 + rnd() * 760;
      x2 = x + Math.cos(ang * Math.PI / 180) * len;
      y2 = y + Math.sin(ang * Math.PI / 180) * len;
      w = rnd() < .16 ? 1.6 : .7;
      out.push('<line x1="' + x.toFixed(0) + '" y1="' + y.toFixed(0) +
               '" x2="' + x2.toFixed(0) + '" y2="' + y2.toFixed(0) +
               '" stroke-width="' + w + '"/>');
    }
    /* a handful of chevrons — the angular motif at a larger scale */
    for (i = 0; i < 7; i++) {
      x = rnd() * W; y = rnd() * H; len = 60 + rnd() * 150;
      out.push('<path d="M' + (x - len) + ' ' + (y + len * .55) +
               ' L' + x + ' ' + y + ' L' + (x + len) + ' ' + (y + len * .55) +
               '" fill="none" stroke-width="1.1"/>');
    }
    return '<svg class="lattice" viewBox="0 0 ' + W + ' ' + H +
           '" preserveAspectRatio="xMidYMid slice" aria-hidden="true">' +
           '<g stroke="var(--brand-line-faint)" stroke-linecap="square">' +
           out.join("") + "</g></svg>";
  }

  var bg = document.createElement("div");
  bg.id = "brandbg";
  bg.setAttribute("aria-hidden", "true");
  bg.innerHTML =
    lattice() +
    '<div class="grain"></div>' +
    '<div class="sweep"></div>' +
    '<img class="watermark" src="crow_mark.svg" alt="">';
  document.body.insertBefore(bg, document.body.firstChild);

  var hud = document.createElement("div");
  hud.id = "brandhud";
  hud.setAttribute("aria-hidden", "true");
  hud.innerHTML = '<i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i>';
  document.body.appendChild(hud);

  /* ---- pointer parallax -------------------------------------------- */
  if (reduce || !window.requestAnimationFrame) return;
  var el = bg.querySelector(".lattice"), tx = 0, ty = 0, cx = 0, cy = 0, queued = false;
  function frame() {
    queued = false;
    cx += (tx - cx) * .08;
    cy += (ty - cy) * .08;
    el.style.transform = "translate3d(" + cx.toFixed(2) + "px," + cy.toFixed(2) + "px,0)";
    if (Math.abs(tx - cx) > .1 || Math.abs(ty - cy) > .1) { queued = true; requestAnimationFrame(frame); }
  }
  function move(e) {
    var w = window.innerWidth || 1, h = window.innerHeight || 1;
    tx = ((e.clientX / w) - .5) * 26;
    ty = ((e.clientY / h) - .5) * 18;
    if (!queued) { queued = true; requestAnimationFrame(frame); }
  }
  window.addEventListener("pointermove", move, { passive: true });
})();
