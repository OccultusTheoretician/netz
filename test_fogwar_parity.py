#!/usr/bin/env python3
"""test_fogwar_parity.py - the differential test that makes fogwar's determinism a
fact rather than a claim. For N seeds: generate a random but LEGAL blue move log
in Python (a separate RNG, never the game's), execute the game in fogwar.py and
in fogwar_core.js under node, and require identical final_state_hash, outcome,
turns_played and game_id. Then verify one receipt with `fogwar.py verify`.

    python test_fogwar_parity.py --games 40 [--scenario scenario.json]

Exit 0 on full agreement, 1 on any divergence (the first divergence is printed
with both receipts' final regions)."""
import argparse
import json
import random
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fogwar  # noqa: E402


def random_blue_moves(sc, seed, max_turns):
    """Play a game turn by turn, choosing random legal blue orders from blue's view."""
    r = random.Random(seed * 7919 + 13)
    rng = fogwar.Rng(seed)
    state = fogwar.new_state(sc)
    A = fogwar.adj(sc)
    moves = []
    while state["outcome"] is None and len(moves) < max_turns:
        v = fogwar.view(sc, state, fogwar.BLUE)
        own = sorted(rid for rid, x in v.items() if x["vis"] == "own")
        orders = []
        for _ in range(int(sc["parameters"]["max_orders"])):
            kind = r.choice(["move", "move", "scout", "hold"])
            if kind == "move" and own:
                f = r.choice(own)
                if v[f]["strength"] > 1:
                    to = r.choice(A[f])
                    orders.append({"type": "move", "from": f, "to": to, "n": r.randint(1, v[f]["strength"] - 1)})
                    continue
            if kind == "scout":
                cands = [rid for rid, x in v.items() if x["vis"] in ("adjacent", "seen")]
                if cands:
                    orders.append({"type": "scout", "target": r.choice(cands)})
                    continue
            orders.append({"type": "hold"})
        # include an occasional illegal order to exercise identical rejection in both engines
        if r.random() < 0.3:
            orders.insert(0, {"type": "move", "from": "ZZ", "to": "N1", "n": 5})
        moves.append(orders)
        b_acc, _ = fogwar.validate_orders(sc, state, fogwar.BLUE, orders)
        r_acc, _ = fogwar.validate_orders(sc, state, fogwar.RED, fogwar.ai_orders(sc, state, fogwar.RED))
        fogwar.resolve_turn(sc, state, rng, b_acc, r_acc)
    return moves


NODE_RUNNER = r"""
const F = require(process.argv[2]);
const fs = require("fs");
const job = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
const sc = JSON.parse(job.scenario_text.replace(/\r\n/g, "\n"));
const out = job.games.map(g => {
  const res = F.play(sc, job.scenario_text, g.seed, g.moves);
  const r = res.receipt;
  return { seed: g.seed, final_state_hash: r.final_state_hash, outcome: r.outcome, turns_played: r.turns_played, game_id: r.game_id, commitment: r.commitment, final_regions: r.final_regions, rejected: r.rejected_orders.length };
});
process.stdout.write(JSON.stringify(out));
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=40)
    ap.add_argument("--scenario", default=None)
    a = ap.parse_args()
    if a.scenario:
        sc, raw = fogwar.load_scenario(a.scenario)
    else:
        sc = fogwar.default_scenario()
        raw = (json.dumps(sc, indent=2) + "\n").encode("utf-8")
    text = raw.decode("utf-8")
    games = []
    for seed in range(1, a.games + 1):
        moves = random_blue_moves(sc, seed, int(sc["parameters"]["turns"]) + 2)
        rec, _ = fogwar.play(sc, raw, seed, moves)
        games.append({"seed": seed, "moves": moves, "py": rec})
    with tempfile.TemporaryDirectory() as td:
        job = Path(td) / "job.json"
        job.write_text(json.dumps({"scenario_text": text, "games": [{"seed": g["seed"], "moves": g["moves"]} for g in games]}), encoding="utf-8")
        runner = Path(td) / "run.js"
        runner.write_text(NODE_RUNNER, encoding="utf-8")
        r = subprocess.run(["node", str(runner), str(HERE / "fogwar_core.js"), str(job)], capture_output=True, text=True, timeout=600)
        if r.returncode != 0:
            print("node failed:", r.stderr[-800:])
            return 1
        js = json.loads(r.stdout)
    bad = 0
    outcomes = {}
    for g, j in zip(games, js):
        p = g["py"]
        outcomes[p["outcome"]] = outcomes.get(p["outcome"], 0) + 1
        same = (p["final_state_hash"] == j["final_state_hash"] and p["outcome"] == j["outcome"]
                and p["turns_played"] == j["turns_played"] and p["game_id"] == j["game_id"] and p["commitment"] == j["commitment"]
                and len(p["rejected_orders"]) == j["rejected"])
        if not same:
            bad += 1
            if bad == 1:
                print("DIVERGENCE seed", g["seed"])
                print("  py:", p["outcome"], p["turns_played"], p["final_state_hash"][:16], json.dumps(p["final_regions"]))
                print("  js:", j["outcome"], j["turns_played"], j["final_state_hash"][:16], json.dumps(j["final_regions"]))
    print("parity: %d games, %d divergent | outcomes %s | turns mean %.1f | rejected-order turns %d" % (
        a.games, bad, dict(sorted(outcomes.items())), sum(g["py"]["turns_played"] for g in games) / len(games),
        sum(len(g["py"]["rejected_orders"]) for g in games)))
    # receipt round trip through the CLI verifier
    with tempfile.TemporaryDirectory() as td:
        scp = Path(td) / "s.json"; scp.write_bytes(raw)
        rp = Path(td) / "r.json"; rp.write_text(json.dumps(games[0]["py"], indent=1) + "\n", encoding="utf-8")
        v = subprocess.run([sys.executable, str(HERE / "fogwar.py"), "verify", "--scenario", str(scp), "--receipt", str(rp)], capture_output=True, text=True)
        print(v.stdout.strip().replace("\n", " | "))
        # tamper: change one opened fog value -> must fail
        rec = json.loads(rp.read_text()); rec["hidden"]["red_strengths"]["S1"] += 1; rp.write_text(json.dumps(rec))
        v2 = subprocess.run([sys.executable, str(HERE / "fogwar.py"), "verify", "--scenario", str(scp), "--receipt", str(rp)], capture_output=True, text=True)
        print("tampered fog ->", "caught" if v2.returncode != 0 else "MISSED")
        if v.returncode != 0 or v2.returncode == 0:
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
