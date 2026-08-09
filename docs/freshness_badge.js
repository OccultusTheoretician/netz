/* freshness_badge.js - EVERY PAGE CARRIES ITS OWN GRADE.
 *
 * The desk grades 25 served surfaces against cadences it published as
 * commitments, and prints LATE and STALE as findings. That board has
 * always been one page a reader had to go and find. Meanwhile a data-
 * backed page would render "generated 2026-07-27" and leave the reader to
 * do date arithmetic against a commitment stated somewhere else.
 *
 * This puts the grade where the data is. Each page declares which surface
 * it is built from; the badge reads the SAME health.json the board reads -
 * no second computation, no second source of truth - and prints that
 * surface's state, age, and cadence commitment inline.
 *
 * The design commitment that matters: A PAGE THAT CANNOT ESTABLISH ITS
 * OWN FRESHNESS SAYS SO. If health.json is unreachable or names no
 * matching surface, the badge prints UNGRADED and states that this is an
 * absence of a check rather than a passing one. A silent badge would be
 * the fail-open the rest of this desk refuses.
 *
 * Usage: <span data-freshness="docs/ledger.json"></span>
 * or     <span data-freshness-name="Kalibrierwarte"></span>
 */
(function () {
  "use strict";

  var COLOR = { OK: "#7fb08a", LATE: "#d29922", STALE: "#a8492f",
                EVENT: "#8b949e", "NO-DATE": "#a8492f",
                UNGRADED: "#7d838c" };
  var MEAN = {
    OK: "moved inside its published cadence",
    LATE: "past its cadence - a printed finding, not a hidden one",
    STALE: "more than twice its cadence - a printed finding",
    EVENT: "no cadence commitment; moves on events, age printed never graded",
    "NO-DATE": "no extractable date - itself a finding",
    UNGRADED: "this page could not establish its own freshness"
  };

  function human(h) {
    if (h == null) return "unknown age";
    if (h < 1) return Math.round(h * 60) + " min old";
    if (h < 48) return (Math.round(h * 10) / 10) + "h old";
    return (Math.round(h / 2.4) / 10) + "d old";
  }

  function paint(node, s, why) {
    var st = (s && s.state) || "UNGRADED";
    var c = COLOR[st] || COLOR.UNGRADED;
    var bits = [];
    bits.push('<span style="color:' + c + ';border:1px solid ' + c +
              ';padding:0 .4rem;font-size:.68rem;letter-spacing:.1em">' +
              st + "</span>");
    if (s) {
      bits.push('<span style="color:#7d838c;font-size:.75rem"> ' +
                human(s.age_hours) +
                (s.cadence_hours ? " - commitment " + s.cadence_hours + "h"
                                 : " - no cadence commitment") +
                (s.last_moved_utc ? " - moved " + s.last_moved_utc : "") +
                "</span>");
    } else {
      bits.push('<span style="color:#7d838c;font-size:.75rem"> ' +
                (why || "no grade available") +
                " - an absence of a check, not a passing one</span>");
    }
    bits.push('<span style="color:#7d838c;font-size:.72rem;display:block">' +
              (MEAN[st] || "") +
              ' - <a href="health.html" style="color:#dcb65e">the board</a>' +
              "</span>");
    node.innerHTML = bits.join("");
  }

  function boot() {
    var nodes = document.querySelectorAll(
      "[data-freshness],[data-freshness-name]");
    if (!nodes.length) return;
    fetch("health.json", { cache: "no-store" }).then(function (r) {
      if (!r.ok) throw new Error("health.json HTTP " + r.status);
      return r.json();
    }).then(function (h) {
      var surf = h.surfaces || [];
      nodes.forEach(function (n) {
        var byPath = n.getAttribute("data-freshness");
        var byName = n.getAttribute("data-freshness-name");
        var hit = null;
        for (var i = 0; i < surf.length; i++) {
          if (byPath && surf[i].path === byPath) { hit = surf[i]; break; }
          if (byName && surf[i].name === byName) { hit = surf[i]; break; }
        }
        paint(n, hit, hit ? null :
              "health.json names no surface " + (byPath || byName));
      });
    }).catch(function (e) {
      nodes.forEach(function (n) {
        paint(n, null, "health board unreachable (" + e.message + ")");
      });
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else { boot(); }
})();
