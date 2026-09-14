#!/usr/bin/env python3
"""warte_frame.py - Kalibrierwarte Section 14: the H6 read (frame drift).

Applies the Section 6 H4 decile test to a FRAME instead of a version:
lmstudio/auto[post-window] against lmstudio/realist within one cohort. Within
one cohort, for each decile in which both arms clear the bin floor, H6 is
SUPPORTED if the observed frequencies differ by more than the wider of the two
bootstrap 95% intervals; FALSIFIED if no decile differs at that margin;
UNTESTABLE until both arms clear their floors and every quality check passes.

Every estimator, floor, bin, bootstrap unit, method and seed is imported from
warte_report.py (the Section 13 pin) and used unchanged, so the two instruments
cannot disagree on a figure. This file adds only the pairing and the verdict.
warte_report.py's pin stands; this file is pinned by its own amendment.

  python warte_frame.py                      read (cohort default = warte_report's)
  python warte_frame.py --cohort <prefix>    another cohort
  python warte_frame.py --frame-hash <hex>   restrict the frame arm to rows carrying this frame_hash prefix
                                             (a frame revision is a new population; rows under the earlier
                                             text are printed as a pre-revision class, not read)
  python warte_frame.py --write              write forecasts/warte_frame_<UTC date>.json
  python warte_frame.py --json               also print the report JSON (first line exactly "{")
  python warte_frame.py --self-hash          print this file's LF-normalised SHA-256 and exit

Exit 0 read (any verdict), 2 usage, 3 halted (a quality check failed for either arm).
"""
import argparse
import hashlib
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import warte_report as W  # the pinned estimator; nothing in it is redefined here

INSTRUMENT = "warte_frame/1.0"
PLAIN_TAG = "lmstudio/auto"
PLAIN_BUCKET_SUFFIX = "[post-window]"
FRAME_TAG = "lmstudio/realist"


def lf_sha256(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def load():
    led = json.loads((HERE / "ledger.json").read_text(encoding="utf-8"))
    rows = led["projections"]
    try:
        reg = {x["tag"]: x for x in json.loads((HERE / "arms.json").read_text(encoding="utf-8-sig"))["arms"]}
    except Exception:
        reg = {}
    defective = set()
    try:
        ci = json.loads((HERE / "cite_integrity_latest.json").read_text(encoding="utf-8"))
        defective = {r["id"] for r in ci.get("rows", []) if r.get("defective")}
    except Exception:
        pass
    return led, rows, reg, defective


def resolve_cohort(rows, coh):
    coh = (coh or "").strip()
    if coh.lower() == "none":
        return None, [r for r in rows if not r.get("rubric_hash")], "cohort 0 - no hash - descriptive only"
    fulls = sorted({r["rubric_hash"] for r in rows if str(r.get("rubric_hash", "")).startswith(coh)})
    if not fulls:
        print("REFUSE - prefix %s matches no rubric hash on the ledger" % coh)
        sys.exit(2)
    if len(fulls) > 1:
        print("REFUSE - prefix %s matches %d rubric hashes: %s" % (coh, len(fulls), fulls))
        sys.exit(2)
    full = fulls[0]
    return full, [r for r in rows if r.get("rubric_hash") == full], "cohort %s" % full[:16]


def arm_report(bucket, tag, brows, cohort_full, controls, ctl_cohort, ctl_all, defective):
    res = [r for r in brows if r["status"] in ("hit", "miss")]
    m = W.point(res)
    b = W.bootstrap(res) if res else {}
    q = W.quality(bucket, tag, brows, brows, cohort_full, controls, ctl_cohort, ctl_all)
    stage = ("checkpoint" if len(res) >= W.CHECKPOINT else
             "interim - noise line, not a result" if len(res) >= W.INTERIM else "counts-only")
    return {"bucket": bucket, "tag": tag, "issued": len(brows),
            "open": sum(1 for r in brows if r["status"] == "open"),
            "void": sum(1 for r in brows if r["status"] == "void"),
            "resolved": len(res), "stage": stage, "point": m, "bootstrap": b, "quality": q,
            "defective_citation_rows": sum(1 for r in res if r["id"] in defective)}


def h6(plain, frame):
    """The Section 6 H4 test, applied to a frame: the same code path as warte_report's comparator."""
    if plain["resolved"] < W.CHECKPOINT or frame["resolved"] < W.CHECKPOINT:
        return {"result": "UNTESTABLE - checkpoint floor %d not met (plain %d, frame %d resolved within cohort)" % (
            W.CHECKPOINT, plain["resolved"], frame["resolved"]), "deciles_both_clear": []}
    if not plain["quality"].get("all_pass") or not frame["quality"].get("all_pass"):
        return {"result": "HALTED - a quality check failed (plain all_pass=%s, frame all_pass=%s)" % (
            plain["quality"].get("all_pass"), frame["quality"].get("all_pass")), "deciles_both_clear": []}
    dec = []
    for x in plain["point"]["bins"]:
        ox = next((y for y in frame["point"]["bins"] if y["bin"] == x["bin"]), None)
        if not ox or x["n"] < W.N_FLOOR_BIN or ox["n"] < W.N_FLOOR_BIN:
            continue
        ca = plain["bootstrap"]["bins"].get(x["bin"], {}).get("ci95")
        cb = frame["bootstrap"]["bins"].get(x["bin"], {}).get("ci95")
        if not ca or not cb:
            continue
        wider = max(ca[1] - ca[0], cb[1] - cb[0])
        dec.append({"bin": x["bin"], "obs_plain": x["obs"], "obs_frame": ox["obs"],
                    "abs_diff": round(abs(x["obs"] - ox["obs"]), 3),
                    "wider_ci_width": round(wider, 3),
                    "drift": abs(x["obs"] - ox["obs"]) > wider})
    if not dec:
        return {"result": "UNTESTABLE - no decile clears the bin floor on both sides", "deciles_both_clear": dec}
    n_drift = sum(1 for z in dec if z["drift"])
    return {"result": ("SUPPORTED - drift in %d decile(s)" % n_drift) if n_drift
            else "FALSIFIED - no decile differs at that margin", "deciles_both_clear": dec}


def main():
    ap = argparse.ArgumentParser(description="Kalibrierwarte Section 14 - the H6 frame-drift read")
    ap.add_argument("--cohort", default=W.DEFAULT_COHORT)
    ap.add_argument("--frame-hash", default=None, help="frame_hash prefix that defines the H6 population for the frame arm")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-hash", action="store_true")
    a = ap.parse_args()
    me = Path(__file__).resolve()
    self_lf = lf_sha256(me)
    if a.self_hash:
        print("warte_frame.py sha256 LF-normalised %s" % self_lf)
        return 0

    led, rows, reg, defective = load()
    cohort_full, cohort_rows, label = resolve_cohort(rows, a.cohort)
    controls = [r for r in rows if r["model"] == W.CONTROL]
    ctl_cohort = [r for r in cohort_rows if r["model"] == W.CONTROL and r["status"] in ("hit", "miss")]
    ctl_all = [r for r in controls if r["status"] in ("hit", "miss")]   # exactly as warte_report.main builds them

    # the plain arm: the same era bucketing as warte_report
    plain_rows = [r for r in cohort_rows if W.bucket_of(r, reg)[1] == PLAIN_TAG + PLAIN_BUCKET_SUFFIX]
    plain_bucket = PLAIN_TAG + PLAIN_BUCKET_SUFFIX
    # the frame arm: rows carrying the tag, grouped by frame_hash; the H6 population is one frame text
    frame_all = [r for r in cohort_rows if r["model"] == FRAME_TAG]
    by_hash = defaultdict(list)
    for r in frame_all:
        by_hash[str(r.get("frame_hash") or "")[:16] or "(none)"].append(r)
    if a.frame_hash:
        pop_key = next((k for k in by_hash if k.startswith(a.frame_hash[:16])), None)
        if pop_key is None:
            print("REFUSE - frame_hash prefix %s matches no realist row in %s" % (a.frame_hash, label))
            return 2
    else:
        pop_key = max(by_hash, key=lambda k: max(r.get("date_issued", "") for r in by_hash[k])) if by_hash else None
    frame_rows = by_hash.get(pop_key, [])
    pre_revision = {k: len(v) for k, v in by_hash.items() if k != pop_key}

    plain = arm_report(plain_bucket, PLAIN_TAG, plain_rows, cohort_full, controls, ctl_cohort, ctl_all, defective)
    frame = arm_report(FRAME_TAG + "[" + (pop_key or "-") + "]", FRAME_TAG, frame_rows, cohort_full, controls, ctl_cohort, ctl_all, defective)
    verdict = h6(plain, frame)
    halted = bool(plain["resolved"] >= W.CHECKPOINT and frame["resolved"] >= W.CHECKPOINT
                  and verdict["result"].startswith("HALTED"))

    now = datetime.now(timezone.utc)
    regpath = HERE / W.REGISTRATION
    rep = {"instrument": INSTRUMENT, "self_sha256": self_lf, "estimator": "warte_report.py " + lf_sha256(HERE / "warte_report.py")[:16],
           "registration": W.REGISTRATION, "registration_lf_sha16": lf_sha256(regpath)[:16] if regpath.exists() else None,
           "generated": now.isoformat(), "ledger_as_of": led.get("as_of"), "cohort": cohort_full, "label": label,
           "bootstrap": {"reps": W.BOOT_N, "seed": W.BOOT_SEED, "unit": "row"},
           "frame_population_hash16": pop_key, "frame_pre_revision_classes": pre_revision,
           "plain": plain, "frame": frame, "H6_frame_drift": verdict, "halted": halted}

    print("WARTE FRAME - %s - %s - ledger %d rows as of %s" % (INSTRUMENT, label, len(rows), led.get("as_of")))
    print("estimator warte_report.py %s (imported, unchanged) - self %s" % (rep["estimator"].split()[1], self_lf[:16]))
    for arm in (plain, frame):
        p = arm["point"]
        print("== %s == issued %d - open %d - resolved %d (%d hit / %d miss) - void %d - stage %s" % (
            arm["bucket"], arm["issued"], arm["open"], arm["resolved"], p.get("hits", 0), p.get("misses", 0), arm["void"], arm["stage"]))
        if arm["resolved"]:
            b = arm["bootstrap"]
            print("   Brier %s %s - base rate %s - climatological %s - skill %s %s - n=%d - floors are conventions, not power; a null is absence of evidence" % (
                p["brier"], b.get("brier_ci95"), p["base_rate"], p["climatological"], p["skill"], b.get("skill_ci95"), arm["resolved"]))
            for x in p["bins"]:
                print("   bin %-6s n %3d  mean p %.3f  obs %s  ci95 %s" % (x["bin"], x["n"], x["mean_p"], x["obs"] if x["obs"] is not None else "n<%d" % W.N_FLOOR_BIN,
                                                                          b.get("bins", {}).get(x["bin"], {}).get("ci95", "-")))
        print("   quality all_pass: %s" % arm["quality"].get("all_pass"))
    if pre_revision:
        print("   frame pre-revision classes (printed, outside the H6 population): %s" % pre_revision)
    print("-- H6 frame drift (Section 14) --")
    print("   " + verdict["result"])
    for z in verdict["deciles_both_clear"]:
        print("   bin %-6s plain %.3f  frame %.3f  |diff| %.3f  wider ci %.3f  drift %s" % (
            z["bin"], z["obs_plain"], z["obs_frame"], z["abs_diff"], z["wider_ci_width"], z["drift"]))
    if a.write:
        out = HERE / "forecasts" / ("warte_frame_%s.json" % now.strftime("%Y-%m-%d"))
        out.write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8")
        print("WARTE FRAME - written %s (sha256 LF %s)" % (out, lf_sha256(out)[:16]))
    if a.json:
        print(json.dumps(rep, indent=1))
    return 3 if halted else 0


if __name__ == "__main__":
    sys.exit(main())
