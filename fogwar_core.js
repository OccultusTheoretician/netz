/* fogwar_core.js - FOGWAR rules 1.0, the JavaScript twin of fogwar.py.
   Every function mirrors the Python by name and by operation order. A game is a
   pure function of (scenario bytes, rules version, seed, blue move log); the
   differential test (test_fogwar_parity.py) re-executes the same games in both
   engines and requires identical final state hashes and game ids.
   ASCII only. No UI here. Works in node (require) and the browser (window.FOGWAR). */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.FOGWAR = factory();
}(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  var RULES_VERSION = "fogwar/1.0";
  var TAG_COMMIT = "FOGWAR1|commit|", TAG_SALT = "FOGWAR1|salt|";
  var BLUE = "blue", RED = "red";

  /* ---------------------------------------------------------- primitives */
  var MASK = (1n << 64n) - 1n, MUL = 6364136223846793005n, INC = 1442695040888963407n, TWO53 = Math.pow(2, 53);
  function Rng(seed) { this.s = BigInt(seed) & MASK; }
  Rng.prototype.next = function () { this.s = (this.s * MUL + INC) & MASK; return Number(this.s >> 11n) / TWO53; };

  function canon(o) {
    if (o === null || typeof o !== "object") return JSON.stringify(o);
    if (Array.isArray(o)) return "[" + o.map(canon).join(",") + "]";
    return "{" + Object.keys(o).sort().map(function (k) { return JSON.stringify(k) + ":" + canon(o[k]); }).join(",") + "}";
  }

  /* sha256 over UTF-8 text: node crypto when present, else a synchronous pure-JS
     implementation so the engine has no async surface. */
  var nodeCrypto = null;
  try { nodeCrypto = (typeof require === "function") ? require("crypto") : null; } catch (e) { nodeCrypto = null; }
  function sha256(str) {
    if (nodeCrypto) return nodeCrypto.createHash("sha256").update(str, "utf8").digest("hex");
    return sha256js(str);
  }
  function sha256js(msg) {
    /* compact SHA-256 (FIPS 180-4) over a UTF-8 string; used only where node crypto is absent */
    var K = [], H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19];
    for (var i = 0, n = 2; K.length < 64; n++) { for (var j = 2; j * j <= n; j++) if (n % j === 0) break; if (j * j > n) { K[K.length] = Math.floor(Math.pow(n, 1 / 3) % 1 * 4294967296) | 0; } }
    var bytes = []; var enc = unescape(encodeURIComponent(msg)); for (i = 0; i < enc.length; i++) bytes.push(enc.charCodeAt(i));
    var l = bytes.length * 8; bytes.push(0x80); while (bytes.length % 64 !== 56) bytes.push(0);
    for (i = 7; i >= 0; i--) bytes.push(i >= 4 ? 0 : (l >>> (i * 8)) & 0xff);
    var w = new Array(64);
    for (var off = 0; off < bytes.length; off += 64) {
      for (i = 0; i < 16; i++) w[i] = (bytes[off + 4 * i] << 24) | (bytes[off + 4 * i + 1] << 16) | (bytes[off + 4 * i + 2] << 8) | bytes[off + 4 * i + 3];
      for (i = 16; i < 64; i++) { var s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^ (w[i - 15] >>> 3), s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^ (w[i - 2] >>> 10); w[i] = (w[i - 16] + s0 + w[i - 7] + s1) | 0; }
      var a = H[0], b = H[1], c = H[2], d = H[3], e = H[4], f = H[5], g = H[6], h = H[7];
      for (i = 0; i < 64; i++) {
        var S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25), ch = (e & f) ^ (~e & g), t1 = (h + S1 + ch + K[i] + w[i]) | 0;
        var S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22), maj = (a & b) ^ (a & c) ^ (b & c), t2 = (S0 + maj) | 0;
        h = g; g = f; f = e; e = (d + t1) | 0; d = c; c = b; b = a; a = (t1 + t2) | 0;
      }
      H[0] = (H[0] + a) | 0; H[1] = (H[1] + b) | 0; H[2] = (H[2] + c) | 0; H[3] = (H[3] + d) | 0; H[4] = (H[4] + e) | 0; H[5] = (H[5] + f) | 0; H[6] = (H[6] + g) | 0; H[7] = (H[7] + h) | 0;
    }
    return H.map(function (x) { return ("00000000" + (x >>> 0).toString(16)).slice(-8); }).join("");
    function rotr(x, n) { return (x >>> n) | (x << (32 - n)); }
  }
  function scenarioHashBytes(text) { return sha256(text.replace(/^\uFEFF/, "").replace(/\r\n/g, "\n")); }
  function saltFor(seed) { return sha256(TAG_SALT + String(seed)); }
  function commitment(sh, seed, hidden) { return sha256(TAG_COMMIT + sh + "|" + RULES_VERSION + "|" + String(seed) + "|" + canon(hidden) + "|" + saltFor(seed)); }

  /* ---------------------------------------------------------- state */
  function newState(sc) {
    var regions = {};
    sc.regions.forEach(function (r) { regions[r.id] = { owner: null, strength: 0 }; });
    [BLUE, RED].forEach(function (side) {
      Object.keys(sc[side].strengths).forEach(function (rid) { regions[rid] = { owner: side, strength: sc[side].strengths[rid] | 0 }; });
    });
    var seen = {}; seen[BLUE] = {}; seen[RED] = {};
    return { turn: 1, regions: regions, seen: seen, eliminated: null, outcome: null, log: [] };
  }
  function adj(sc) { var A = {}; sc.regions.forEach(function (r) { A[r.id] = r.adj.slice(); }); return A; }
  function rmeta(sc) { var M = {}; sc.regions.forEach(function (r) { M[r.id] = r; }); return M; }
  function sortedKeys(o) { return Object.keys(o).sort(); }

  function stateHash(state) {
    var regs = {};
    sortedKeys(state.regions).forEach(function (rid) { regs[rid] = { o: state.regions[rid].owner, s: state.regions[rid].strength }; });
    return sha256(canon({ turn: state.turn, regions: regs, eliminated: state.eliminated, outcome: state.outcome }));
  }

  function view(sc, state, side) {
    var A = adj(sc), own = {};
    Object.keys(state.regions).forEach(function (rid) { if (state.regions[rid].owner === side) own[rid] = true; });
    var out = {}, reveal = sc.parameters.scout_reveals_turns | 0;
    Object.keys(state.regions).forEach(function (rid) {
      var v = state.regions[rid];
      if (own[rid]) { out[rid] = { owner: v.owner, strength: v.strength, vis: "own" }; return; }
      var adjacent = A[rid].some(function (n) { return own[n]; });
      if (!adjacent) { out[rid] = { owner: null, strength: null, vis: "fog" }; return; }
      var seenTurn = state.seen[side][rid];
      var fresh = (seenTurn !== undefined) && seenTurn >= state.turn - reveal;
      out[rid] = { owner: v.owner, strength: fresh ? v.strength : null, vis: fresh ? "seen" : "adjacent" };
    });
    return out;
  }

  /* ---------------------------------------------------------- orders */
  function validateOrders(sc, state, side, orders) {
    var A = adj(sc), maxo = sc.parameters.max_orders | 0, acc = [], rej = [], committed = {};
    (orders || []).slice(0, maxo).forEach(function (o) {
      var t = o.type;
      if (t === "hold") { acc.push({ type: "hold" }); return; }
      if (t === "scout") {
        var tgt = o.target;
        if (state.regions[tgt] !== undefined && (A[tgt] || []).some(function (n) { return state.regions[n].owner === side; })) acc.push({ type: "scout", target: tgt });
        else rej.push({ order: o, why: "scout target must be adjacent to an own region" });
        return;
      }
      if (t === "move") {
        var f = o.from, to = o.to, n = o.n;
        if (state.regions[f] === undefined || state.regions[f].owner !== side) { rej.push({ order: o, why: "origin not owned" }); return; }
        if ((A[f] || []).indexOf(to) < 0) { rej.push({ order: o, why: "destination not adjacent" }); return; }
        n = Number(n);
        if (!Number.isInteger(n)) { rej.push({ order: o, why: "n not an integer" }); return; }
        var avail = state.regions[f].strength - 1 - (committed[f] || 0);
        if (n < 1 || n > avail) { rej.push({ order: o, why: "n must be 1..strength-1 net of orders already given" }); return; }
        committed[f] = (committed[f] || 0) + n;
        acc.push({ type: "move", from: f, to: to, n: n });
        return;
      }
      rej.push({ order: o, why: "unknown order type" });
    });
    return [acc, rej];
  }

  /* ---------------------------------------------------------- the rule AI */
  function aiOrders(sc, state, side) {
    var v = view(sc, state, side), A = adj(sc), M = rmeta(sc), maxo = sc.parameters.max_orders | 0;
    var own = Object.keys(v).filter(function (rid) { return v[rid].vis === "own"; }).sort();
    var orders = [];
    var known = [];
    Object.keys(v).forEach(function (rid) { var x = v[rid]; if (x.vis === "seen" && x.owner !== null && x.owner !== side) known.push(x.strength); });
    var estDefault = known.length ? Math.floor(known.reduce(function (a, b) { return a + b; }, 0) / known.length) : 30;
    function est(rid) { var x = v[rid]; if (x.owner === null && x.vis !== "fog") return 0; return x.strength !== null ? x.strength : estDefault; }
    /* 1. scout */
    var cands = [];
    Object.keys(v).forEach(function (rid) { var x = v[rid]; if (x.vis === "adjacent" && x.owner !== null) cands.push([-M[rid].value, rid]); });
    if (cands.length && orders.length < maxo) {
      cands.sort(function (p, q) { return p[0] !== q[0] ? p[0] - q[0] : (p[1] < q[1] ? -1 : p[1] > q[1] ? 1 : 0); });
      orders.push({ type: "scout", target: cands[0][1] });
    }
    /* 2. attack */
    var best = null;
    own.forEach(function (f) {
      var sf = v[f].strength - 1;
      if (sf < 1) return;
      A[f].forEach(function (t) {
        if (v[t].owner === side || v[t].vis === "fog") return;
        var e = est(t);
        var ratio = (e === 0) ? 99.0 : sf / e;
        if (ratio >= 1.5 && (best === null || ratio > best[0] || (ratio === best[0] && pairLess([f, t], [best[1], best[2]])))) best = [ratio, f, t, e];
      });
    });
    if (best && orders.length < maxo) {
      var f2 = best[1], t2 = best[2], e2 = best[3];
      var n2 = Math.min(v[f2].strength - 1, e2 > 0 ? (Math.floor(1.6 * e2) + 1) : Math.max(1, Math.floor((v[f2].strength - 1) / 2)));
      if (n2 >= 1) orders.push({ type: "move", from: f2, to: t2, n: n2 });
    }
    /* 3. reinforce */
    var frontier = own.filter(function (r) { return A[r].some(function (t) { return v[t].owner !== side; }); });
    var interior = own.filter(function (r) { return frontier.indexOf(r) < 0; });
    if (frontier.length && interior.length && orders.length < maxo) {
      var src = interior.slice().sort(function (p, q) { return v[q].strength - v[p].strength || (q < p ? -1 : q > p ? 1 : 0); })[0];
      var dsts = A[src].filter(function (t) { return frontier.indexOf(t) >= 0; });
      if (dsts.length && v[src].strength > 2) {
        var dst = dsts.slice().sort(function (p, q) { return v[p].strength - v[q].strength || (p < q ? -1 : p > q ? 1 : 0); })[0];
        orders.push({ type: "move", from: src, to: dst, n: Math.floor((v[src].strength - 1) / 2) });
      }
    }
    while (orders.length < maxo) orders.push({ type: "hold" });
    return orders;
  }
  function pairLess(a, b) { return a[0] < b[0] || (a[0] === b[0] && a[1] < b[1]); }

  /* ---------------------------------------------------------- resolution */
  function combat(rng, p, defense, att, dfn, effAtt, effDef) {
    var a0 = att, d0 = dfn, brk = +p.break_fraction, shock = +p.shock, dt = +p.dt;
    var a = att, d = dfn, ticks = p.combat_ticks | 0, t = 0;
    for (var i = 1; i <= ticks; i++) {
      t = i;
      var sa = 1 + (rng.next() - 0.5) * 2 * shock;
      var sd = 1 + (rng.next() - 0.5) * 2 * shock;
      var da = Math.floor(effDef * defense * d * sd * dt);
      var dd = Math.floor(effAtt * a * sa * dt);
      a = Math.max(0, a - da);
      d = Math.max(0, d - dd);
      if (d <= Math.floor(d0 * brk) || a <= Math.floor(a0 * brk)) break;
    }
    if (d <= Math.floor(d0 * brk) && a > Math.floor(a0 * brk)) return ["attacker", a, d, t];
    if (a <= Math.floor(a0 * brk) && d > Math.floor(d0 * brk)) return ["defender", a, d, t];
    if (d <= Math.floor(d0 * brk) && a <= Math.floor(a0 * brk)) return ["mutual", a, d, t];
    return ["undecided", a, d, t];
  }

  function resolveTurn(sc, state, rng, blueOrders, redOrders) {
    var p = sc.parameters, M = rmeta(sc), R = state.regions;
    var eff = {}; eff[BLUE] = +p.eff_blue; eff[RED] = +p.eff_red;
    var events = [];
    [[BLUE, blueOrders], [RED, redOrders]].forEach(function (pair) {
      pair[1].forEach(function (o) { if (o.type === "scout") state.seen[pair[0]][o.target] = state.turn; });
    });
    var arrivals = {};
    [[BLUE, blueOrders], [RED, redOrders]].forEach(function (pair) {
      pair[1].forEach(function (o) {
        if (o.type !== "move") return;
        R[o.from].strength -= o.n;
        if (!arrivals[o.to]) arrivals[o.to] = {};
        if (!arrivals[o.to][pair[0]]) arrivals[o.to][pair[0]] = [];
        arrivals[o.to][pair[0]].push([o.from, o.n]);
      });
    });
    sortedKeys(arrivals).forEach(function (rid) {
      var by = arrivals[rid], occ = R[rid].owner;
      var sides = [BLUE, RED].filter(function (s) { return by[s] !== undefined; });
      var tot = {}; sides.forEach(function (s) { tot[s] = by[s].reduce(function (acc, x) { return acc + x[1]; }, 0); });
      if (sides.length === 1 && (occ === null || occ === sides[0])) {
        var s1 = sides[0];
        R[rid].owner = s1; R[rid].strength += tot[s1];
        events.push({ t: state.turn, region: rid, kind: occ === null ? "occupy" : "reinforce", side: s1, n: tot[s1] });
        return;
      }
      var defender;
      if (occ !== null) defender = occ;
      else defender = (tot[RED] || 0) >= (tot[BLUE] || 0) ? RED : BLUE;
      var attacker = defender === RED ? BLUE : RED;
      var dForce = (occ === defender ? R[rid].strength : 0) + (tot[defender] || 0);
      var aForce = tot[attacker] || 0;
      if (aForce === 0) { R[rid].strength += (tot[defender] || 0); return; }
      var res = combat(rng, p, +M[rid].defense, aForce, dForce, eff[attacker], eff[defender]);
      var winner = res[0], aLeft = res[1], dLeft = res[2], ticks = res[3];
      state.seen[attacker][rid] = state.turn; state.seen[defender][rid] = state.turn;
      var origin = by[attacker][0][0];
      if (winner === "attacker") { R[rid].owner = attacker; R[rid].strength = aLeft; }
      else if (winner === "mutual") { R[rid].owner = dLeft > 0 ? defender : null; R[rid].strength = dLeft; if (aLeft > 0) R[origin].strength += aLeft; }
      else { R[rid].owner = defender; R[rid].strength = dLeft; R[origin].strength += aLeft; }
      events.push({ t: state.turn, region: rid, kind: "combat", attacker: attacker, defender: defender, a0: aForce, d0: dForce, a_left: aLeft, d_left: dLeft, ticks: ticks, winner: winner });
    });
    Object.keys(R).forEach(function (rid) { var v = R[rid]; if (v.strength <= 0 && v.owner !== null && arrivals[rid] === undefined) { v.owner = null; v.strength = 0; } });
    [BLUE, RED].forEach(function (side) {
      var owned = Object.keys(R).filter(function (rid) { return R[rid].owner === side; });
      if (!owned.length) return;
      var gain = Math.floor(owned.reduce(function (a, r) { return a + M[r].value; }, 0) * (+p.reinforce_rate));
      var cap = sc[side].capital;
      var target = R[cap].owner === side ? cap : owned.slice().sort(function (x, y) { return R[y].strength - R[x].strength || (y < x ? -1 : y > x ? 1 : 0); })[0];
      R[target].strength += gain;
      events.push({ t: state.turn, kind: "reinforce_income", side: side, n: gain, region: target });
    });
    state.log = state.log.concat(events);
    [BLUE, RED].forEach(function (side) {
      var any = Object.keys(R).some(function (rid) { return R[rid].owner === side; });
      if (!any) { state.eliminated = side; state.outcome = (side === BLUE ? RED : BLUE) + "_wins"; }
    });
    if (state.outcome === null && state.turn >= (p.turns | 0)) {
      var vb = 0, vr = 0;
      Object.keys(R).forEach(function (r) { if (R[r].owner === BLUE) vb += M[r].value; else if (R[r].owner === RED) vr += M[r].value; });
      state.outcome = vb > vr ? "blue_wins" : vr > vb ? "red_wins" : "draw";
    }
    state.turn += 1;
    return events;
  }

  /* ---------------------------------------------------------- a game */
  function play(sc, scenarioText, seed, blueMoves) {
    var sh = scenarioHashBytes(scenarioText);
    var hidden = { red_strengths: {} };
    sortedKeys(sc[RED].strengths).forEach(function (k) { hidden.red_strengths[k] = sc[RED].strengths[k] | 0; });
    var com = commitment(sh, seed, hidden);
    var rng = new Rng(seed), state = newState(sc), acceptedLog = [], rejectedLog = [], turnI = 0;
    while (state.outcome === null) {
      var orders = turnI < blueMoves.length ? blueMoves[turnI] : [];
      var b = validateOrders(sc, state, BLUE, orders), r = validateOrders(sc, state, RED, aiOrders(sc, state, RED));
      acceptedLog.push({ blue: b[0], red: r[0] });
      if (b[1].length) rejectedLog.push({ turn: state.turn, rejected: b[1] });
      resolveTurn(sc, state, rng, b[0], r[0]);
      turnI += 1;
      if (turnI > 10000) break;
    }
    var fh = stateHash(state);
    var finalRegions = {};
    sortedKeys(state.regions).forEach(function (rid) { finalRegions[rid] = { o: state.regions[rid].owner, s: state.regions[rid].strength }; });
    var receipt = { rules_version: RULES_VERSION, scenario_hash: sh, seed: seed, commitment: com, salt: saltFor(seed), hidden: hidden,
      moves: acceptedLog.map(function (t) { return t.blue; }), red_moves: acceptedLog.map(function (t) { return t.red; }),
      turns_played: turnI, outcome: state.outcome, eliminated: state.eliminated, final_state_hash: fh, final_regions: finalRegions };
    receipt.game_id = sha256(canon(receipt));
    receipt.rejected_orders = rejectedLog;
    return { receipt: receipt, state: state };
  }

  return { RULES_VERSION: RULES_VERSION, Rng: Rng, canon: canon, sha256: sha256, scenarioHashBytes: scenarioHashBytes,
    commitment: commitment, saltFor: saltFor, newState: newState, view: view, validateOrders: validateOrders,
    aiOrders: aiOrders, combat: combat, resolveTurn: resolveTurn, play: play, stateHash: stateHash, sha256js: sha256js };
}));
