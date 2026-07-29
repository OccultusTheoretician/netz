#!/usr/bin/env python3
"""
fogsim.py — deterministic scenario runs, sealed as a set with a declared count.

THE PROBLEM THIS SOLVES, AND IT IS NOT DDOS.

A scenario runner invites infinite attempts. Run a hundred, publish the three
that landed. Rate limiting does nothing about that — a patient operator spreads
a hundred runs over a month. Cherry-picking is an epistemic problem, not a
capacity problem, and KNM 3.02 already rules on it: commit the COUNT before you
run, or the denominator is unverifiable.

So a FogSim campaign seals a SET. Twenty commitments published up front, each
binding one run's scenario, rules, seed and index. Run 7 cannot be published
without run 3 being conspicuously absent, because run 3's commitment is already
on the record with nothing opened against it.

AND THE RUNS ARE DETERMINISTIC, WHICH IS THE STRONGER PROPERTY.

A run is a pure function of (scenario, rules version, seed). A third party does
not verify your hash and take your word for the output. They re-execute your run
and get your output, byte for byte. Recomputation replaces trust entirely — the
KNP 2.03 interoperability contract applied to a simulation rather than a string.

There is no server anywhere in this. Runs execute locally, seals are the
operator's own, and any aggregator reads published hashlogs and holds nothing
(KNM 1.05, KNP 1.02). Nothing to flood, nothing to store, nothing to moderate.

    python fogsim.py scenario --out s.json         a fillable scenario
    python fogsim.py seal --scenario s.json --runs 20 \\
           --question "..." --out fogsim_hashlog.json
    python fogsim.py run --scenario s.json --index 7
    python fogsim.py reveal --index 7 --out reveal.json
    python fogsim.py verify --hashlog fogsim_hashlog.json --reveal reveal.json \\
           --scenario s.json

THE MODEL IS A TOY AND SAYS SO. Stochastic Lanchester square-law attrition with
seeded per-tick shocks. It is not a claim about war. The machinery — sealed set,
declared count, deterministic re-execution — is the product; the model is a
socket you replace. Any replacement must remain a pure function of
(scenario, rules_version, seed) or the verification property is lost.

Standard library only.
"""

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY_STATE = HERE / "fogsim_campaign.json"
RULES_VERSION = "fogsim-lanchester/1.0"


def state_path(label):
    """Opening material is per-campaign.

    A single global state file means the next seal silently destroys the seeds
    and salts of every unopened run in the previous campaign - which is
    precisely what the count commitment exists to protect.
    """
    return HERE / ("fogsim_campaign_%s.json" % label)


def resolve_state(label=None, scenario=None):
    """Return the opening-material path for a campaign, or None.

    Order: explicit label, then the scenario's own hash, then the unsuffixed
    legacy file so campaigns sealed before this change keep working.
    """
    cands = []
    if label:
        cands.append(state_path(label))
    if scenario is not None:
        cands.append(state_path(scenario_hash(scenario)[:16]))
    cands.append(LEGACY_STATE)
    for p in cands:
        if p.exists():
            return p
    return None

SEP = "|"
PIPE_ESC = "\\u007C"


# ----------------------------------------------------------------------
# the model: replaceable, deterministic, and honest about being a toy
# ----------------------------------------------------------------------
class Rng:
    """Explicit LCG rather than random.seed(), because the standard library's
    generator is free to change between versions and determinism across time
    and across implementations is the whole point."""
    def __init__(self, seed: int):
        self.s = seed & 0xFFFFFFFFFFFFFFFF

    def next(self):
        self.s = (self.s * 6364136223846793005 + 1442695040888963407) & 0xFFFFFFFFFFFFFFFF
        return (self.s >> 11) / float(1 << 53)


def run_model(scenario: dict, seed: int) -> dict:
    """Lanchester square law with a seeded multiplicative shock per side per tick.

    dA/dt = -b * B * shock ; dB/dt = -a * A * shock
    Terminates when a side falls below its break threshold, or at max_ticks.
    """
    a = dict(scenario["blue"]); b = dict(scenario["red"])
    p = scenario["parameters"]
    rng = Rng(seed)
    A, B = float(a["strength"]), float(b["strength"])
    ea, eb = float(a["effectiveness"]), float(b["effectiveness"])
    brk = float(p["break_fraction"])
    A0, B0 = A, B
    shock = float(p["shock"])
    log = []
    tick = 0
    for tick in range(1, int(p["max_ticks"]) + 1):
        sa = 1.0 + (rng.next() - 0.5) * 2 * shock
        sb = 1.0 + (rng.next() - 0.5) * 2 * shock
        dA = eb * B * sb * p["dt"]
        dB = ea * A * sa * p["dt"]
        A = max(0.0, A - dA)
        B = max(0.0, B - dB)
        log.append((tick, round(A, 3), round(B, 3)))
        if A <= A0 * brk or B <= B0 * brk:
            break
    if A <= A0 * brk and B <= B0 * brk:
        outcome = "mutual_break"
    elif A <= A0 * brk:
        outcome = "red_holds"
    elif B <= B0 * brk:
        outcome = "blue_holds"
    else:
        outcome = "no_decision"
    return {"outcome": outcome, "ticks": tick,
            "blue_remaining": round(A / A0, 6), "red_remaining": round(B / B0, 6),
            "rules_version": RULES_VERSION}


DEFAULT_SCENARIO = {
    "name": "EXAMPLE — two aggregates, no real force is represented",
    "note": ("A toy. Replace with your own scenario. Whatever the model becomes, it "
             "must stay a pure function of (scenario, rules_version, seed) or a third "
             "party cannot re-execute your run, and re-execution is the point."),
    "blue": {"label": "BLUE", "strength": 1000.0, "effectiveness": 0.0012},
    "red": {"label": "RED", "strength": 900.0, "effectiveness": 0.0014},
    "parameters": {"dt": 1.0, "max_ticks": 400, "break_fraction": 0.55, "shock": 0.35},
}


# ----------------------------------------------------------------------
def read_json(path):
    """Read JSON whatever encoding it arrived in.

    PowerShell's `>` redirection writes UTF-16LE, and Out-File -Encoding utf8
    writes UTF-8 with a BOM. Both make json.loads fail at byte zero on a file
    that is otherwise perfectly good. Sniff rather than assume.
    """
    raw = Path(path).read_bytes()
    for bom, enc in ((b"\xff\xfe", "utf-16"), (b"\xfe\xff", "utf-16"),
                     (b"\xef\xbb\xbf", "utf-8-sig")):
        if raw.startswith(bom):
            return json.loads(raw.decode(enc))
    return json.loads(raw.decode("utf-8"))


def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def esc(v: str) -> str:
    return str(v).replace(SEP, PIPE_ESC)


def scenario_hash(scenario: dict) -> str:
    return hashlib.sha256(canon(scenario).encode("utf-8")).hexdigest()


def commitment(sh: str, index: int, seed: int, question: str, salt: str) -> str:
    pre = SEP.join([sh, RULES_VERSION, str(index), str(seed),
                    esc(question), salt])
    return hashlib.sha256(pre.encode("utf-8")).hexdigest(), pre


def seed_for(master: str, index: int) -> int:
    h = hashlib.sha256(f"{master}|{index}".encode("utf-8")).hexdigest()
    return int(h[:16], 16)


# ----------------------------------------------------------------------
def cmd_scenario(a):
    text = json.dumps(DEFAULT_SCENARIO, indent=2, ensure_ascii=False) + "\n"
    if getattr(a, "out", None):
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"written → {a.out}  (UTF-8, written by python rather than redirected)")
    else:
        print(text, end="")
    return 0


def cmd_seal(a):
    scenario = read_json(Path(a.scenario))
    sh = scenario_hash(scenario)
    label = getattr(a, "campaign", None) or sh[:16]
    sp = state_path(label)
    if sp.exists() and not getattr(a, "force", False):
        prev = read_json(sp)
        print("FAIL - opening material already exists for this campaign.",
              file=sys.stderr)
        print("  file     : %s" % sp.name, file=sys.stderr)
        print("  scenario : %s" % str(prev.get("scenario_hash", "?"))[:16],
              file=sys.stderr)
        print("  runs     : %s" % prev.get("runs", "?"), file=sys.stderr)
        print("  Overwriting destroys the seeds and salts of every unopened run",
              file=sys.stderr)
        print("  in that campaign. Use --campaign NAME for a distinct campaign,",
              file=sys.stderr)
        print("  or --force only if that campaign is fully revealed and finished.",
              file=sys.stderr)
        return 1
    master = hashlib.sha256(
        (sh + datetime.now(timezone.utc).isoformat() + str(a.runs)).encode()).hexdigest()
    salts = [hashlib.sha256(f"{master}|salt|{i}".encode()).hexdigest()[:32]
             for i in range(1, a.runs + 1)]
    recs, opens = [], []
    for i in range(1, a.runs + 1):
        sd = seed_for(master, i)
        c, _ = commitment(sh, i, sd, a.question, salts[i - 1])
        recs.append({"index": i, "commitment": c, "status": "SEALED"})
        opens.append({"index": i, "seed": sd, "salt": salts[i - 1]})
    hashlog = {
        "protocol": "FOGSIM-26",
        "construction": {
            "preimage_order": ["scenario_hash", "rules_version", "index", "seed",
                               "question", "salt"],
            "separator": SEP, "hash": "SHA-256", "encoding": "UTF-8",
            "pipe_escape": PIPE_ESC},
        "declared_runs": a.runs,
        "scenario_hash": sh,
        "rules_version": RULES_VERSION,
        "question": a.question,
        "sealed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count_commitment": (
            f"This campaign declares {a.runs} runs and publishes {a.runs} commitments "
            f"before any run is executed. Publishing a subset of outcomes is therefore "
            f"detectable: an index with a commitment and no reveal is a run that was "
            f"executed and withheld, or never executed. Either is visible. (KNM 3.02)"),
        "records": recs,
    }
    Path(a.out).write_text(json.dumps(hashlog, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    sp.write_text(json.dumps({"scenario_hash": sh, "question": a.question,
                              "master": master, "runs": a.runs, "opens": opens},
                             indent=2), encoding="utf-8")
    print(f"sealed {a.runs} runs · scenario {sh[:16]}…")
    print(f"  hashlog → {a.out}   (publish this)")
    print(f"  opening material → {sp.name}   (KEEP PRIVATE until reveal)")
    print("\nNothing has been executed yet. That is the point: the count is committed")
    print("before the first result exists.")
    return 0


def cmd_run(a):
    scenario = read_json(Path(a.scenario))
    sp = resolve_state(getattr(a, "campaign", None), scenario)
    if sp is None:
        print("FAIL - no opening material for this scenario. Seal a campaign first.",
              file=sys.stderr)
        return 1
    print("campaign state: %s" % sp.name, file=sys.stderr)
    st = read_json(sp)
    if scenario_hash(scenario) != st["scenario_hash"]:
        print("FAIL — this scenario does not hash to the sealed one. Editing the "
              "scenario after sealing breaks every commitment in the campaign.",
              file=sys.stderr)
        return 1
    o = next((x for x in st["opens"] if x["index"] == a.index), None)
    if not o:
        print(f"FAIL — index {a.index} is not in this campaign", file=sys.stderr)
        return 1
    r = run_model(scenario, o["seed"])
    print(json.dumps({"index": a.index, "seed": o["seed"], **r}, indent=2))
    return 0


def cmd_reveal(a):
    scen = read_json(Path(a.scenario)) if getattr(a, "scenario", None) else None
    sp = resolve_state(getattr(a, "campaign", None), scen)
    if sp is None:
        print("FAIL - no opening material found. Pass --campaign or --scenario.",
              file=sys.stderr)
        return 1
    st = read_json(sp)
    if scen is not None and scenario_hash(scen) != st["scenario_hash"]:
        print("FAIL - resolved campaign does not match the supplied scenario.",
              file=sys.stderr)
        return 1
    print("campaign state: %s" % sp.name, file=sys.stderr)
    idxs = [a.index] if a.index else [x["index"] for x in st["opens"]]
    out = []
    for i in idxs:
        o = next(x for x in st["opens"] if x["index"] == i)
        out.append({"index": i, "scenario_hash": st["scenario_hash"],
                    "rules_version": RULES_VERSION, "seed": o["seed"],
                    "question": st["question"], "salt": o["salt"]})
    Path(a.out).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(f"revealed {len(out)} run(s) → {a.out}")
    return 0


def cmd_verify(a):
    h = read_json(Path(a.hashlog))
    reveals = read_json(Path(a.reveal))
    if isinstance(reveals, dict):
        reveals = [reveals]
    scenario = read_json(Path(a.scenario)) if a.scenario else None
    by = {r["index"]: r for r in h["records"]}
    musts = []
    print(f"\nFOGSIM-26 VERIFICATION — {a.hashlog}")
    print("-" * 66)
    print(f"  declared runs   : {h.get('declared_runs')}")
    print(f"  commitments     : {len(h['records'])}")
    if h.get("declared_runs") != len(h["records"]):
        musts.append("declared_runs does not match the number of commitments — "
                     "the count commitment is void")
    revealed = {r["index"] for r in reveals}
    withheld = sorted(set(by) - revealed)
    print(f"  revealed        : {len(revealed)}")
    print(f"  withheld        : {len(withheld)}" +
          (f"  indices {withheld}" if withheld else ""))

    if scenario is not None:
        sh = scenario_hash(scenario)
        print(f"  scenario hash   : {'MATCH' if sh == h.get('scenario_hash') else 'MISMATCH'}")
        if sh != h.get("scenario_hash"):
            musts.append("the supplied scenario does not hash to the sealed one")

    ok_c = ok_r = 0
    for r in reveals:
        i = r["index"]
        if i not in by:
            musts.append(f"index {i}: revealed but never committed"); continue
        c, _ = commitment(r["scenario_hash"], i, r["seed"], r["question"], r["salt"])
        if c == by[i]["commitment"]:
            ok_c += 1
        else:
            musts.append(f"index {i}: commitment does not recompute")
        if scenario is not None:
            out = run_model(scenario, r["seed"])
            r["_recomputed"] = out
            ok_r += 1
    print(f"  commitments recompute : {ok_c}/{len(reveals)}")
    if scenario is not None:
        print(f"  runs re-executed      : {ok_r}/{len(reveals)}")
        for r in reveals:
            if "_recomputed" in r:
                o = r["_recomputed"]
                print(f"    run {r['index']:>3}  {o['outcome']:<14} "
                      f"{o['ticks']:>4} ticks  blue {o['blue_remaining']:.3f} "
                      f"red {o['red_remaining']:.3f}")
        print("\n  These outputs were produced here, not read from the publisher's file.")
        print("  A publisher cannot misreport an outcome that anyone can re-execute.")
    if withheld:
        print(f"\n  {len(withheld)} committed run(s) unopened. That is not necessarily")
        print("  misconduct — a campaign may reveal in stages — but the count is on the")
        print("  record, so a permanently unopened index is a visible fact rather than")
        print("  an invisible one. (KNM 3.02)")
    print()
    if musts:
        for m in musts:
            print(f"  FAIL · {m}")
        return 1
    print("  PASS — commitments recompute, count is intact.")
    print("  Verification certifies the integrity of the campaign record. It certifies")
    print("  nothing about whether the model resembles war.\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="FogSim — sealed deterministic scenario runs")
    sub = ap.add_subparsers(dest="cmd")
    sc = sub.add_parser("scenario")
    sc.add_argument("--out", help="write here in UTF-8 rather than to stdout")
    s = sub.add_parser("seal")
    s.add_argument("--scenario", required=True)
    s.add_argument("--runs", type=int, required=True)
    s.add_argument("--question", required=True)
    s.add_argument("--out", default="fogsim_hashlog.json")
    s.add_argument("--campaign",
                   help="label for this campaign's opening material; defaults to "
                        "the first 16 hex of the scenario hash")
    s.add_argument("--force", action="store_true",
                   help="overwrite existing opening material - destroys the seeds "
                        "and salts of every unopened run in that campaign")
    r = sub.add_parser("run")
    r.add_argument("--scenario", required=True)
    r.add_argument("--index", type=int, required=True)
    r.add_argument("--campaign")
    v = sub.add_parser("reveal")
    v.add_argument("--index", type=int)
    v.add_argument("--out", default="fogsim_reveal.json")
    v.add_argument("--campaign")
    v.add_argument("--scenario")
    w = sub.add_parser("verify")
    w.add_argument("--hashlog", required=True)
    w.add_argument("--reveal", required=True)
    w.add_argument("--scenario")
    a = ap.parse_args()
    if not a.cmd:
        ap.print_help(); return 0
    return {"scenario": cmd_scenario, "seal": cmd_seal, "run": cmd_run,
            "reveal": cmd_reveal, "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
