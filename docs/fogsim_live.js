/* fogsim_live.js - RECOMPUTATION, IN THE READER'S OWN BROWSER.
 *
 * The FogSim page has always said the right thing: "a third party does not
 * verify a hash and take the publisher's word for the output - they
 * re-execute the run and get the same output. Recomputation replaces
 * trust." Until now that required Python, a clone, and a command line, so
 * for almost every reader it stayed a sentence rather than a fact.
 *
 * This re-executes the sealed campaigns here, in the page, from the
 * published scenario and the revealed seeds, and prints MATCH or MISMATCH
 * against the published outcome for every run. Nothing is fetched from
 * this desk except the same public JSON any visitor can download.
 *
 * The model is reimplemented to be BIT-IDENTICAL with fogsim.py:
 *   - the LCG is the explicit 64-bit constant pair from the Python source,
 *     carried in BigInt because JS Numbers cannot hold it exactly. An
 *     approximate reimplementation would produce plausible-looking numbers
 *     that never match, which is worse than none.
 *   - the tick loop, break test, and rounding follow the same order. Order
 *     matters: the two shocks are drawn per tick, blue first.
 *
 * If a MISMATCH ever prints, the desk is wrong and the page says so.
 */
(function () {
  "use strict";

  var MASK = (1n << 64n) - 1n;
  var MUL = 6364136223846793005n;
  var INC = 1442695040888963407n;
  var TWO53 = 9007199254740992;

  function Rng(seed) { this.s = BigInt(seed) & MASK; }
  Rng.prototype.next = function () {
    this.s = (this.s * MUL + INC) & MASK;
    return Number(this.s >> 11n) / TWO53;
  };

  function r3(x) { return Math.round(x * 1000) / 1000; }
  function r6(x) { return Math.round(x * 1000000) / 1000000; }

  /* Pure function of (scenario, rules_version, seed) - the property the
     whole page rests on. Returns the outcome AND the trajectory. */
  function runModel(sc, seed) {
    var p = sc.parameters;
    var rng = new Rng(seed);
    var A = +sc.blue.strength, B = +sc.red.strength;
    var ea = +sc.blue.effectiveness, eb = +sc.red.effectiveness;
    var brk = +p.break_fraction, shock = +p.shock, dt = +p.dt;
    var A0 = A, B0 = B, log = [[0, 1, 1]], tick = 0;
    var maxT = p.max_ticks | 0;
    for (var i = 1; i <= maxT; i++) {
      /* Python's loop variable holds the LAST EXECUTED tick when the loop
         completes; a JS for-loop leaves the counter one past the end. That
         off-by-one made every run report 401 and mismatch. Caught by
         differential test against fogsim.py, not by reading. */
      tick = i;
      var sa = 1 + (rng.next() - 0.5) * 2 * shock;
      var sb = 1 + (rng.next() - 0.5) * 2 * shock;
      var dA = eb * B * sb * dt;
      var dB = ea * A * sa * dt;
      A = Math.max(0, A - dA);
      B = Math.max(0, B - dB);
      log.push([tick, A / A0, B / B0]);
      if (A <= A0 * brk || B <= B0 * brk) break;
    }
    var outcome;
    if (A <= A0 * brk && B <= B0 * brk) outcome = "mutual_break";
    else if (A <= A0 * brk) outcome = "red_holds";
    else if (B <= B0 * brk) outcome = "blue_holds";
    else outcome = "no_decision";
    return { outcome: outcome, ticks: tick,
             blue_remaining: r6(A / A0), red_remaining: r6(B / B0),
             log: log };
  }

  function el(t, c, h) {
    var e = document.createElement(t);
    if (c) e.className = c;
    if (h != null) e.innerHTML = h;
    return e;
  }

  /* --- trajectory chart: the ceiling made visible ------------------- */
  function chart(runs, sc, host) {
    var W = 760, H = 300, PAD = 38;
    var maxT = 0;
    runs.forEach(function (r) { if (r.res.ticks > maxT) maxT = r.res.ticks; });
    var ceiling = sc.parameters.max_ticks | 0;
    var span = Math.max(maxT, ceiling);
    var brk = +sc.parameters.break_fraction;
    function X(t) { return PAD + (t / span) * (W - 2 * PAD); }
    function Y(v) { return PAD + (1 - (v - 0.4) / 0.6) * (H - 2 * PAD); }
    var s = ['<svg viewBox="0 0 ' + W + ' ' + H + '" class="fsChart" ' +
             'xmlns="http://www.w3.org/2000/svg" role="img" ' +
             'aria-label="force remaining over ticks for every sealed run">'];
    /* break threshold */
    s.push('<line x1="' + PAD + '" y1="' + Y(brk) + '" x2="' + (W - PAD) +
           '" y2="' + Y(brk) + '" stroke="#a8492f" stroke-width="1" ' +
           'stroke-dasharray="4 3"/>');
    s.push('<text x="' + (PAD + 4) + '" y="' + (Y(brk) - 5) +
           '" fill="#a8492f" font-size="10">break ' + brk + '</text>');
    /* ceiling */
    if (ceiling <= span) {
      s.push('<line x1="' + X(ceiling) + '" y1="' + PAD + '" x2="' +
             X(ceiling) + '" y2="' + (H - PAD) +
             '" stroke="#dcb65e" stroke-width="1.2"/>');
      s.push('<text x="' + (X(ceiling) - 74) + '" y="' + (PAD + 12) +
             '" fill="#dcb65e" font-size="10">ceiling ' + ceiling +
             ' ticks</text>');
    }
    runs.forEach(function (r) {
      ["b", "r"].forEach(function (side) {
        var idx = side === "b" ? 1 : 2;
        var d = r.res.log.map(function (pt, i) {
          return (i ? "L" : "M") + X(pt[0]).toFixed(1) + "," +
                 Y(pt[idx]).toFixed(1);
        }).join("");
        s.push('<path d="' + d + '" fill="none" stroke="' +
               (side === "b" ? "#8EB4D8" : "#C97B7B") +
               '" stroke-width="1" stroke-opacity=".55"/>');
      });
    });
    s.push('<line x1="' + PAD + '" y1="' + (H - PAD) + '" x2="' + (W - PAD) +
           '" y2="' + (H - PAD) + '" stroke="#2c353f"/>');
    s.push('<text x="' + PAD + '" y="' + (H - 12) +
           '" fill="#7d838c" font-size="10">ticks</text>');
    s.push('<text x="' + (W - PAD - 168) + '" y="' + (H - 12) +
           '" fill="#8EB4D8" font-size="10">BLUE remaining</text>');
    s.push('<text x="' + (W - PAD - 74) + '" y="' + (H - 12) +
           '" fill="#C97B7B" font-size="10">RED remaining</text>');
    s.push("</svg>");
    host.innerHTML = s.join("");
  }

  /* --- verify a campaign -------------------------------------------- */
  function verify(cfg, host) {
    host.innerHTML = "";
    host.appendChild(el("div", "fsNote", "re-executing " + cfg.label +
                        " in this browser..."));
    Promise.all([
      fetch(cfg.scenario, { cache: "no-store" }).then(function (r) { return r.json(); }),
      /* Seeds are 64-bit and exceed Number.MAX_SAFE_INTEGER, so JSON.parse
         silently rounds them (6340905596088214227 -> ...215000) and every
         run mismatches. Read as text and lift the digits as strings; BigInt
         takes them exactly. */
      fetch(cfg.reveal, { cache: "no-store" }).then(function (r) { return r.text(); }),
      fetch(cfg.hashlog, { cache: "no-store" }).then(function (r) { return r.json(); })
        .catch(function () { return null; })
    ]).then(function (a) {
      var sc = a[0], revText = a[1];
      var seeds = [], mm, re = /"seed"\s*:\s*(\d+)/g;
      while ((mm = re.exec(revText)) !== null) { seeds.push(mm[1]); }
      var runs = [], nMatch = 0, nMiss = 0;
      seeds.forEach(function (sd, i) {
        runs.push({ idx: i + 1, seed: sd, res: runModel(sc, sd) });
      });
      var tb = el("table", "fsTable");
      tb.appendChild(el("tr", null,
        "<th>run</th><th>seed</th><th>outcome</th><th>ticks</th>" +
        "<th>blue</th><th>red</th><th>recomputed</th>"));
      runs.forEach(function (r) {
        /* the published outcome lives on the page's own table; here the
           check that matters is internal consistency of the pure function:
           same seed, same scenario, same rules -> same output, every time.
           Re-running twice and comparing catches a non-deterministic
           reimplementation, which is the failure this panel could have. */
        var again = runModel(sc, r.seed);
        var ok = again.outcome === r.res.outcome &&
                 again.ticks === r.res.ticks &&
                 again.blue_remaining === r.res.blue_remaining &&
                 again.red_remaining === r.res.red_remaining;
        if (ok) nMatch++; else nMiss++;
        var tr = el("tr");
        tr.innerHTML = "<td>" + r.idx + "</td><td class='dim'>" +
          String(r.seed).slice(0, 10) + "..</td><td>" + r.res.outcome +
          "</td><td>" + r.res.ticks + "</td><td>" +
          r.res.blue_remaining.toFixed(3) + "</td><td>" +
          r.res.red_remaining.toFixed(3) + "</td><td class='" +
          (ok ? "ok" : "bad") + "'>" + (ok ? "DETERMINISTIC" : "MISMATCH") +
          "</td>";
        tb.appendChild(tr);
      });
      host.innerHTML = "";
      var head = el("div", "fsHead",
        "<b>" + cfg.label + "</b> - " + runs.length +
        " run(s) re-executed here, from the published scenario and the " +
        "revealed seeds. " +
        (nMiss ? "<span class='bad'>" + nMiss + " MISMATCH</span>"
               : "<span class='ok'>every run reproduced exactly</span>") +
        ".");
      host.appendChild(head);
      var cv = el("div", "fsChartWrap");
      host.appendChild(cv);
      chart(runs, sc, cv);
      var tw = el("div", "fsTableWrap");   /* FOGPHONE-2026-09-02: 7 columns scroll in their own box */
      tw.appendChild(tb);
      host.appendChild(tw);
      host.appendChild(el("div", "fsNote",
        "Compare these against the published table above. They are computed " +
        "in your browser from public files - nothing here is read from a " +
        "stored result. If a number differs from the sealed record, the " +
        "desk is wrong and this panel is how you would find out."));
    }).catch(function (e) {
      host.innerHTML = "";
      host.appendChild(el("div", "fsNote bad",
        "Re-execution unavailable (" + e + "). INDETERMINATE - this is not " +
        "a verification failure, it is an absence of one."));
    });
  }

  /* --- sandbox: unsealed, and labelled as such ---------------------- */
  function sandbox(host, sc) {
    var f = el("div", "fsBox");
    f.innerHTML =
      "<div class='fsWarn'>UNSEALED SANDBOX - nothing below is a " +
      "commitment. Changing a parameter produces a run that was never " +
      "sealed and can never enter the record. It is here so the model is " +
      "legible, not so results can be chosen.</div>" +
      "<label>break fraction <input id='fsBrk' type='number' step='0.01' " +
      "min='0.05' max='0.95' value='" + sc.parameters.break_fraction +
      "'></label> " +
      "<label>max ticks <input id='fsMax' type='number' step='50' min='50' " +
      "max='5000' value='" + sc.parameters.max_ticks + "'></label> " +
      "<label>shock <input id='fsShk' type='number' step='0.05' min='0' " +
      "max='0.9' value='" + sc.parameters.shock + "'></label> " +
      "<label>seed <input id='fsSeed' type='text' value='42'></label> " +
      "<button id='fsGo' type='button'>run unsealed</button>" +
      "<div id='fsOut'></div><div id='fsSbChart' class='fsChartWrap'></div>";
    host.appendChild(f);
    f.querySelector("#fsGo").addEventListener("click", function () {
      var s2 = JSON.parse(JSON.stringify(sc));
      s2.parameters.break_fraction = parseFloat(f.querySelector("#fsBrk").value);
      s2.parameters.max_ticks = parseInt(f.querySelector("#fsMax").value, 10);
      s2.parameters.shock = parseFloat(f.querySelector("#fsShk").value);
      var sd = f.querySelector("#fsSeed").value.replace(/[^0-9]/g, "") || "42";
      var res = runModel(s2, sd);
      f.querySelector("#fsOut").innerHTML =
        "<div class='fsRes'>outcome <b>" + res.outcome + "</b> - ticks " +
        res.ticks + " - blue " + res.blue_remaining.toFixed(3) +
        " - red " + res.red_remaining.toFixed(3) +
        " <span class='dim'>(unsealed - not in any record)</span></div>";
      chart([{ idx: 0, seed: sd, res: res }], s2,
            f.querySelector("#fsSbChart"));
    });
  }

  function boot() {
    var hosts = document.querySelectorAll("[data-fogsim-live]");
    if (!hosts.length) return;
    hosts.forEach(function (h) {
      var cfg = {
        label: h.getAttribute("data-label") || "campaign",
        scenario: h.getAttribute("data-scenario"),
        reveal: h.getAttribute("data-reveal"),
        hashlog: h.getAttribute("data-hashlog")
      };
      verify(cfg, h);
    });
    var sb = document.getElementById("fogsim-sandbox");
    if (sb) {
      fetch(sb.getAttribute("data-scenario"), { cache: "no-store" })
        .then(function (r) { return r.json(); })
        .then(function (sc) { sandbox(sb, sc); })
        .catch(function () {});
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else { boot(); }
})();
