#!/usr/bin/env python3
"""fogwar.py - FOGWAR rules 1.0. The engine (P1). No UI here; the board comes later.

A wargame you can audit. A game is a pure function of (scenario bytes, rules
version, seed, blue's move log): anyone re-executes it and gets the same final
state hash, byte for byte, in Python or in the JavaScript twin
(fogwar_core.js). Red's dispositions - the fog - are committed before blue's
first move and opened in the receipt at the end. The commitment binds the
RECORD: a published receipt lets a third party check that the fog held what the
game says it held. It does not hide anything from a player reading their own
browser's memory, and this file does not pretend it does.

The model is a socket. Combat is stochastic Lanchester square-law attrition
with seeded per-tick shocks, lifted from fogsim.py; the PRNG is fogsim's LCG.
Nothing here is a claim about war. The machinery - determinism, commitment,
receipt, re-execution - is the product.

Rules, in one screen (full text in FOGWAR_RULES_1.0.md):
  Map: an abstract region graph. Each region: id, adjacency, defense (>=1.0),
       value. Two sides, blue (the player) and red (the rule AI), each with a
       capital and starting strengths (integer points).
  Turn: blue issues up to max_orders orders, then red does. Orders:
       hold | move(from,to,n) | scout(target). A move into an own or empty
       region reinforces or occupies; into an enemy region it attacks.
  Resolution: scouts first, then movements, then combat in every region where
       both sides stand, then reinforcements (value * reinforce_rate to the
       capital), then fog decay. Combat runs combat_ticks ticks of Lanchester
       with shocks; the defender's effectiveness is multiplied by the region's
       defense; whoever falls to break_fraction of their starting force breaks;
       a broken or undecided attacker withdraws to the first contributing
       origin. Both sides entering an empty region: the larger force defends;
       ties defend red.
  Fog: a side sees owner and strength of its own regions; the owner of any
       region adjacent to one it owns; the strength of an adjacent region
       only if scouted this turn or fought last turn. Everything else is fog.
  End: a side with no regions is eliminated; after `turns` turns the side
       controlling more value wins; equal value is a draw.
  Determinism: all strengths are integers; combat losses are floor() of double
       products evaluated in one fixed order; the AI is a fixed policy over
       regions in id order and uses no randomness; the only randomness is the
       combat shock stream from the LCG seeded once per game.

CLI:
  python fogwar.py scenario --out scenario.json          a fillable scenario
  python fogwar.py play --scenario s.json --seed 7 --moves moves.json --out receipt.json
  python fogwar.py verify --scenario s.json --receipt receipt.json
  python fogwar.py demo --scenario s.json --seed 7      play the built-in blue policy
  python fogwar.py hash --scenario s.json               scenario hash (file bytes, LF)
"""
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

RULES_VERSION = "fogwar/1.0"
TAG_COMMIT = "FOGWAR1|commit|"
TAG_SALT = "FOGWAR1|salt|"
BLUE, RED = "blue", "red"


# ---------------------------------------------------------------- primitives
class Rng:
    """fogsim.py's LCG, unchanged: determinism across time and implementations."""

    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFFFFFF

    def next(self):
        self.s = (self.s * 6364136223846793005 + 1442695040888963407) & 0xFFFFFFFFFFFFFFFF
        return (self.s >> 11) / float(1 << 53)


def canon(obj):
    """Canonical JSON for hashed structures: ints, ASCII strings, bools, null,
    sorted keys, no spaces. Floats never enter a hashed structure."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def scenario_hash_bytes(raw):
    """The scenario is hashed as served bytes, LF-normalised, so both engines
    hash identical text and float formatting never matters."""
    b = raw.replace(b"\r\n", b"\n")
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]   # a Windows editor's BOM is not part of the scenario
    return hashlib.sha256(b).hexdigest()


def salt_for(seed):
    return sha256(TAG_SALT + str(seed))


def commitment(sh, seed, hidden):
    return sha256(TAG_COMMIT + sh + "|" + RULES_VERSION + "|" + str(seed) + "|" + canon(hidden) + "|" + salt_for(seed))


# ---------------------------------------------------------------- scenario
def default_scenario():
    """Two capitals, a contested centre. Abstract; no real force is represented."""
    return {
        "name": "TWO CAPITALS - abstract theatre, no real force represented",
        "note": "A game is a pure function of (scenario bytes, fogwar/1.0, seed, blue move log). Edit freely; the hash of these bytes is the scenario's identity.",
        "regions": [
            {"id": "N1", "name": "North Capital", "adj": ["N2", "N3"], "defense": 1.4, "value": 3},
            {"id": "N2", "name": "North Coast", "adj": ["N1", "N3", "C1"], "defense": 1.1, "value": 2},
            {"id": "N3", "name": "North Hills", "adj": ["N1", "N2", "C2"], "defense": 1.3, "value": 1},
            {"id": "C1", "name": "West Plain", "adj": ["N2", "C2", "C3", "S2"], "defense": 1.0, "value": 2},
            {"id": "C2", "name": "Central Ridge", "adj": ["N3", "C1", "C3", "C4"], "defense": 1.3, "value": 2},
            {"id": "C3", "name": "River Crossing", "adj": ["C1", "C2", "C4", "S1", "S2"], "defense": 1.0, "value": 3},
            {"id": "C4", "name": "East Marsh", "adj": ["C2", "C3", "S3"], "defense": 1.2, "value": 1},
            {"id": "S1", "name": "South Capital", "adj": ["C3", "S2", "S3"], "defense": 1.4, "value": 3},
            {"id": "S2", "name": "South Coast", "adj": ["C1", "C3", "S1"], "defense": 1.1, "value": 2},
            {"id": "S3", "name": "South Hills", "adj": ["C4", "S1"], "defense": 1.3, "value": 1},
        ],
        "blue": {"capital": "N1", "strengths": {"N1": 60, "N2": 40, "N3": 30}},
        "red": {"capital": "S1", "strengths": {"S1": 60, "S2": 40, "S3": 30}},
        "parameters": {"turns": 10, "max_orders": 3, "combat_ticks": 6, "dt": 0.12, "shock": 0.3,
                       "break_fraction": 0.4, "eff_blue": 1.0, "eff_red": 1.0, "reinforce_rate": 1.0,
                       "scout_reveals_turns": 1},
    }


# ---------------------------------------------------------------- state
def new_state(sc):
    regions = {}
    for r in sc["regions"]:
        regions[r["id"]] = {"owner": None, "strength": 0}
    for side in (BLUE, RED):
        for rid, n in sc[side]["strengths"].items():
            regions[rid] = {"owner": side, "strength": int(n)}
    return {"turn": 1, "regions": regions,
            "seen": {BLUE: {}, RED: {}},      # side -> region -> turn last seen (scout or fight)
            "eliminated": None, "outcome": None, "log": []}


def adj(sc):
    return {r["id"]: list(r["adj"]) for r in sc["regions"]}


def rmeta(sc):
    return {r["id"]: r for r in sc["regions"]}


def state_hash(state):
    regs = {rid: {"o": v["owner"], "s": v["strength"]} for rid, v in sorted(state["regions"].items())}
    return sha256(canon({"turn": state["turn"], "regions": regs, "eliminated": state["eliminated"],
                         "outcome": state["outcome"]}))


def view(sc, state, side):
    """What `side` can see. owner: known|unknown; strength: int|null."""
    A = adj(sc)
    own = {rid for rid, v in state["regions"].items() if v["owner"] == side}
    out = {}
    for rid, v in state["regions"].items():
        if rid in own:
            out[rid] = {"owner": v["owner"], "strength": v["strength"], "vis": "own"}
            continue
        adjacent = any(n in own for n in A[rid])
        if not adjacent:
            out[rid] = {"owner": None, "strength": None, "vis": "fog"}
            continue
        seen_turn = state["seen"][side].get(rid)
        fresh = seen_turn is not None and seen_turn >= state["turn"] - int(sc["parameters"]["scout_reveals_turns"])
        out[rid] = {"owner": v["owner"], "strength": v["strength"] if fresh else None,
                    "vis": "seen" if fresh else "adjacent"}
    return out


# ---------------------------------------------------------------- orders
def validate_orders(sc, state, side, orders):
    """Returns (accepted, rejected) - identical behaviour in the twin."""
    A = adj(sc)
    maxo = int(sc["parameters"]["max_orders"])
    acc, rej = [], []
    committed = {}  # from -> points already ordered out this turn
    for o in list(orders)[:maxo]:
        t = o.get("type")
        if t == "hold":
            acc.append({"type": "hold"})
            continue
        if t == "scout":
            tgt = o.get("target")
            if tgt in state["regions"] and any(state["regions"][n]["owner"] == side for n in A.get(tgt, [])):
                acc.append({"type": "scout", "target": tgt})
            else:
                rej.append({"order": o, "why": "scout target must be adjacent to an own region"})
            continue
        if t == "move":
            f, to, n = o.get("from"), o.get("to"), o.get("n")
            if f not in state["regions"] or state["regions"][f]["owner"] != side:
                rej.append({"order": o, "why": "origin not owned"})
                continue
            if to not in A.get(f, []):
                rej.append({"order": o, "why": "destination not adjacent"})
                continue
            try:
                n = int(n)
            except Exception:
                rej.append({"order": o, "why": "n not an integer"})
                continue
            avail = state["regions"][f]["strength"] - 1 - committed.get(f, 0)
            if n < 1 or n > avail:
                rej.append({"order": o, "why": "n must be 1..strength-1 net of orders already given"})
                continue
            committed[f] = committed.get(f, 0) + n
            acc.append({"type": "move", "from": f, "to": to, "n": n})
            continue
        rej.append({"order": o, "why": "unknown order type"})
    return acc, rej


# ---------------------------------------------------------------- the rule AI (red)
def ai_orders(sc, state, side):
    """A fixed policy over regions in id order. No randomness. Sees only its view."""
    v = view(sc, state, side)
    A = adj(sc)
    M = rmeta(sc)
    maxo = int(sc["parameters"]["max_orders"])
    own = sorted(rid for rid, x in v.items() if x["vis"] == "own")
    orders = []
    known = [x["strength"] for rid, x in v.items() if x["vis"] == "seen" and x["owner"] not in (None, side)]
    est_default = int(sum(known) / len(known)) if known else 30

    def est(rid):
        x = v[rid]
        if x["owner"] is None and x["vis"] != "fog":
            return 0
        return x["strength"] if x["strength"] is not None else est_default

    # 1. scout: adjacent non-own region with unknown strength, highest value, then id
    cands = []
    for rid, x in v.items():
        if x["vis"] == "adjacent" and x["owner"] not in (None,):
            cands.append((-M[rid]["value"], rid))
    if cands and len(orders) < maxo:
        cands.sort()
        orders.append({"type": "scout", "target": cands[0][1]})
    # 2. attack: best ratio of own strength-1 to estimate, needs >= 1.5x (empty regions always taken)
    best = None
    for f in own:
        sf = v[f]["strength"] - 1
        if sf < 1:
            continue
        for t in A[f]:
            if v[t]["owner"] == side or v[t]["vis"] == "fog":
                continue
            e = est(t)
            if e == 0:
                ratio = 99.0
            else:
                ratio = sf / e
            if ratio >= 1.5 and (best is None or ratio > best[0] or (ratio == best[0] and (f, t) < (best[1], best[2]))):
                best = (ratio, f, t, e)
    if best and len(orders) < maxo:
        ratio, f, t, e = best
        n = min(v[f]["strength"] - 1, (math.floor(1.6 * e) + 1) if e > 0 else max(1, (v[f]["strength"] - 1) // 2))
        if n >= 1:
            orders.append({"type": "move", "from": f, "to": t, "n": n})
    # 3. reinforce: strongest interior -> weakest adjacent frontier
    frontier = [r for r in own if any(v[t]["owner"] != side for t in A[r])]
    interior = [r for r in own if r not in frontier]
    if frontier and interior and len(orders) < maxo:
        src = max(interior, key=lambda r: (v[r]["strength"], r))
        dsts = [t for t in A[src] if t in frontier]
        if dsts and v[src]["strength"] > 2:
            dst = min(dsts, key=lambda r: (v[r]["strength"], r))
            orders.append({"type": "move", "from": src, "to": dst, "n": (v[src]["strength"] - 1) // 2})
    while len(orders) < maxo:
        orders.append({"type": "hold"})
    return orders


# ---------------------------------------------------------------- resolution
def combat(rng, p, defense, att, dfn, eff_att, eff_def):
    """Lanchester square law with shocks; integer strengths; floor losses.
    Returns (winner, att_left, def_left, ticks)."""
    a0, d0 = att, dfn
    brk, shock, dt = float(p["break_fraction"]), float(p["shock"]), float(p["dt"])
    a, d = att, dfn
    ticks = int(p["combat_ticks"])
    t = 0
    for i in range(1, ticks + 1):
        t = i
        sa = 1 + (rng.next() - 0.5) * 2 * shock
        sd = 1 + (rng.next() - 0.5) * 2 * shock
        da = math.floor(eff_def * defense * d * sd * dt)
        dd = math.floor(eff_att * a * sa * dt)
        a = max(0, a - da)
        d = max(0, d - dd)
        if d <= math.floor(d0 * brk) or a <= math.floor(a0 * brk):
            break
    if d <= math.floor(d0 * brk) and a > math.floor(a0 * brk):
        return "attacker", a, d, t
    if a <= math.floor(a0 * brk) and d > math.floor(d0 * brk):
        return "defender", a, d, t
    if d <= math.floor(d0 * brk) and a <= math.floor(a0 * brk):
        return "mutual", a, d, t
    return "undecided", a, d, t


def resolve_turn(sc, state, rng, blue_orders, red_orders):
    p = sc["parameters"]
    M = rmeta(sc)
    R = state["regions"]
    eff = {BLUE: float(p["eff_blue"]), RED: float(p["eff_red"])}
    events = []
    # 1. scouts
    for side, orders in ((BLUE, blue_orders), (RED, red_orders)):
        for o in orders:
            if o["type"] == "scout":
                state["seen"][side][o["target"]] = state["turn"]
    # 2. movements: subtract from origins, pool arrivals by region and side (origin order kept)
    arrivals = {}
    for side, orders in ((BLUE, blue_orders), (RED, red_orders)):
        for o in orders:
            if o["type"] != "move":
                continue
            R[o["from"]]["strength"] -= o["n"]
            arrivals.setdefault(o["to"], {}).setdefault(side, []).append((o["from"], o["n"]))
    # 3. resolve each destination in id order
    for rid in sorted(arrivals):
        by = arrivals[rid]
        occ = R[rid]["owner"]
        sides = [s for s in (BLUE, RED) if s in by]
        tot = {s: sum(n for _, n in by[s]) for s in sides}
        if len(sides) == 1 and (occ is None or occ == sides[0]):
            s = sides[0]
            R[rid]["owner"] = s
            R[rid]["strength"] += tot[s]
            events.append({"t": state["turn"], "region": rid, "kind": "occupy" if occ is None else "reinforce", "side": s, "n": tot[s]})
            continue
        # someone is fighting. Determine defender and attacker.
        if occ is not None:
            defender = occ
        else:
            # both arrive into empty ground: the larger force defends; ties defend red
            defender = RED if tot.get(RED, 0) >= tot.get(BLUE, 0) else BLUE
        attacker = BLUE if defender == RED else RED
        # the defender's force is what stands there plus its own arrivals; if the ground
        # was empty the defender's force is just its arrivals
        d_force = (R[rid]["strength"] if occ == defender else 0) + tot.get(defender, 0)
        a_force = tot.get(attacker, 0)
        if a_force == 0:
            # reinforcement into a region the other side already holds without attackers: just add
            R[rid]["strength"] += tot.get(defender, 0)
            continue
        winner, a_left, d_left, ticks = combat(rng, p, float(M[rid]["defense"]), a_force, d_force, eff[attacker], eff[defender])
        # record contact for both sides' fog
        state["seen"][attacker][rid] = state["turn"]
        state["seen"][defender][rid] = state["turn"]
        origin = by[attacker][0][0]
        if winner == "attacker":
            R[rid]["owner"] = attacker
            R[rid]["strength"] = a_left
        elif winner == "mutual":
            R[rid]["owner"] = defender if d_left > 0 else None
            R[rid]["strength"] = d_left
            if a_left > 0:
                R[origin]["strength"] += a_left
        else:  # defender holds or undecided: attacker withdraws
            R[rid]["owner"] = defender
            R[rid]["strength"] = d_left
            R[origin]["strength"] += a_left
        events.append({"t": state["turn"], "region": rid, "kind": "combat", "attacker": attacker, "defender": defender,
                       "a0": a_force, "d0": d_force, "a_left": a_left, "d_left": d_left, "ticks": ticks, "winner": winner})
    # 4. regions emptied by movement lose ownership if strength is 0 (cannot happen with leave-one rule, kept for safety)
    for rid, v in R.items():
        if v["strength"] <= 0 and v["owner"] is not None and rid not in arrivals:
            v["owner"] = None
            v["strength"] = 0
    # 5. reinforcements
    for side in (BLUE, RED):
        owned = [rid for rid, v in R.items() if v["owner"] == side]
        if not owned:
            continue
        gain = math.floor(sum(M[r]["value"] for r in owned) * float(p["reinforce_rate"]))
        cap = sc[side]["capital"]
        target = cap if R[cap]["owner"] == side else max(owned, key=lambda r: (R[r]["strength"], r))
        R[target]["strength"] += gain
        events.append({"t": state["turn"], "kind": "reinforce_income", "side": side, "n": gain, "region": target})
    state["log"].extend(events)
    # 6. end conditions
    for side in (BLUE, RED):
        if not any(v["owner"] == side for v in R.values()):
            state["eliminated"] = side
            state["outcome"] = (RED if side == BLUE else BLUE) + "_wins"
    if state["outcome"] is None and state["turn"] >= int(p["turns"]):
        vb = sum(M[r]["value"] for r, v in R.items() if v["owner"] == BLUE)
        vr = sum(M[r]["value"] for r, v in R.items() if v["owner"] == RED)
        state["outcome"] = "blue_wins" if vb > vr else "red_wins" if vr > vb else "draw"
    state["turn"] += 1
    return events


# ---------------------------------------------------------------- a game
def play(sc, raw_bytes, seed, blue_moves):
    """blue_moves: list per turn of order lists. Returns the receipt."""
    sh = scenario_hash_bytes(raw_bytes)
    hidden = {"red_strengths": {k: int(v) for k, v in sorted(sc[RED]["strengths"].items())}}
    com = commitment(sh, seed, hidden)
    rng = Rng(seed)
    state = new_state(sc)
    accepted_log, rejected_log = [], []
    turn_i = 0
    while state["outcome"] is None:
        orders = blue_moves[turn_i] if turn_i < len(blue_moves) else []
        b_acc, b_rej = validate_orders(sc, state, BLUE, orders)
        r_acc, _ = validate_orders(sc, state, RED, ai_orders(sc, state, RED))
        accepted_log.append({"blue": b_acc, "red": r_acc})
        if b_rej:
            rejected_log.append({"turn": state["turn"], "rejected": b_rej})
        resolve_turn(sc, state, rng, b_acc, r_acc)
        turn_i += 1
        if turn_i > 10000:
            break
    fh = state_hash(state)
    receipt = {"rules_version": RULES_VERSION, "scenario_hash": sh, "seed": seed, "commitment": com,
               "salt": salt_for(seed), "hidden": hidden, "moves": [t["blue"] for t in accepted_log],
               "red_moves": [t["red"] for t in accepted_log], "turns_played": turn_i,
               "outcome": state["outcome"], "eliminated": state["eliminated"], "final_state_hash": fh,
               "final_regions": {rid: {"o": v["owner"], "s": v["strength"]} for rid, v in sorted(state["regions"].items())}}
    receipt["game_id"] = sha256(canon(receipt))
    receipt["rejected_orders"] = rejected_log   # outside the id: they are not part of the game
    return receipt, state


def blue_policy_demo(sc, state):
    """A built-in blue for demos and the parity harness: mirror the AI."""
    return ai_orders(sc, state, BLUE)


# ---------------------------------------------------------------- CLI
def load_scenario(path):
    raw = Path(path).read_bytes()
    return json.loads(raw.replace(b"\r\n", b"\n").decode("utf-8-sig")), raw


def cmd_scenario(a):
    Path(a.out).write_text(json.dumps(default_scenario(), indent=2) + "\n", encoding="utf-8")
    print("scenario -> %s" % a.out)
    return 0


def cmd_hash(a):
    sc, raw = load_scenario(a.scenario)
    print(scenario_hash_bytes(raw))
    return 0


def cmd_play(a):
    sc, raw = load_scenario(a.scenario)
    moves = json.loads(Path(a.moves).read_text(encoding="utf-8")) if a.moves else []
    receipt, state = play(sc, raw, int(a.seed), moves)
    if a.out:
        Path(a.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print("game %s | %s after %d turn(s) | final %s | commitment %s" % (
        receipt["game_id"][:16], receipt["outcome"], receipt["turns_played"], receipt["final_state_hash"][:16], receipt["commitment"][:16]))
    return 0


def cmd_demo(a):
    sc, raw = load_scenario(a.scenario)
    # blue plays the mirror policy: generate its moves turn by turn against a live state
    rng = Rng(int(a.seed))
    state = new_state(sc)
    moves = []
    while state["outcome"] is None:
        b = blue_policy_demo(sc, state)
        b_acc, _ = validate_orders(sc, state, BLUE, b)
        r_acc, _ = validate_orders(sc, state, RED, ai_orders(sc, state, RED))
        moves.append(b_acc)
        resolve_turn(sc, state, rng, b_acc, r_acc)
    receipt, _ = play(sc, raw, int(a.seed), moves)
    if a.out:
        Path(a.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print("demo game %s | %s after %d turn(s) | final %s" % (receipt["game_id"][:16], receipt["outcome"], receipt["turns_played"], receipt["final_state_hash"][:16]))
    for e in [x for x in receipt.get("rejected_orders", [])][:3]:
        print("  rejected:", e)
    return 0


def cmd_verify(a):
    sc, raw = load_scenario(a.scenario)
    rec = json.loads(Path(a.receipt).read_text(encoding="utf-8"))
    ok = True
    sh = scenario_hash_bytes(raw)
    if sh != rec.get("scenario_hash"):
        print("FAIL scenario hash: receipt %s vs file %s" % (str(rec.get("scenario_hash"))[:16], sh[:16]))
        ok = False
    com = commitment(sh, int(rec["seed"]), rec["hidden"])
    print("%s commitment reproduces from the opened fog" % ("ok  " if com == rec.get("commitment") else "FAIL"))
    ok = ok and com == rec.get("commitment")
    if rec["hidden"].get("red_strengths") != {k: int(v) for k, v in sorted(sc[RED]["strengths"].items())}:
        print("FAIL opened fog does not match the scenario's red dispositions")
        ok = False
    re_rec, _ = play(sc, raw, int(rec["seed"]), rec["moves"])
    same = re_rec["final_state_hash"] == rec.get("final_state_hash")
    print("%s re-execution reproduces the final state hash %s" % ("ok  " if same else "FAIL", str(rec.get("final_state_hash"))[:16]))
    ok = ok and same
    gid = sha256(canon({k: v for k, v in rec.items() if k not in ("game_id", "rejected_orders")}))
    print("%s game id %s" % ("ok  " if gid == rec.get("game_id") else "FAIL", str(rec.get("game_id"))[:16]))
    ok = ok and gid == rec.get("game_id")
    print("VERIFIED" if ok else "VERIFICATION FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="FOGWAR rules 1.0 - deterministic committed-fog wargame engine (P1)")
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("scenario"); s.add_argument("--out", required=True)
    s = sub.add_parser("hash"); s.add_argument("--scenario", required=True)
    s = sub.add_parser("play"); s.add_argument("--scenario", required=True); s.add_argument("--seed", required=True); s.add_argument("--moves"); s.add_argument("--out")
    s = sub.add_parser("demo"); s.add_argument("--scenario", required=True); s.add_argument("--seed", required=True); s.add_argument("--out")
    s = sub.add_parser("verify"); s.add_argument("--scenario", required=True); s.add_argument("--receipt", required=True)
    a = ap.parse_args()
    if a.cmd == "scenario":
        return cmd_scenario(a)
    if a.cmd == "hash":
        return cmd_hash(a)
    if a.cmd == "play":
        return cmd_play(a)
    if a.cmd == "demo":
        return cmd_demo(a)
    if a.cmd == "verify":
        return cmd_verify(a)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
