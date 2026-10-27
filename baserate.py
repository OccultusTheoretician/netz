#!/usr/bin/env python3
"""
baserate.py — the climatological control arm (RPAS 4.06).

WHY THIS EXISTS, AND WHY IT IS NOT COSMETIC.

The ledger already prints a "climatological" Brier and a skill score. Read how
it is computed (kkr.py, per-arm scoring):

    base = s["hits"] / s["n_resolved"]      # realized base rate
    clim = base * (1 - base)                # climatological Brier
    skill = 1 - brier / clim

The reference class is derived from the same resolved rows being scored. The
arm is measured against a number computed out of its own outcomes. That is an
in-sample reference, and it is the one figure on the board a stranger cannot
recompute from anything committed in advance. `lmstudio/auto[pre-verbot]`
currently reports skill -0.179 on exactly that basis.

A control ARM fixes it. Same packet, same claims, same deadlines, probability
set to a base rate computed from PRIOR resolved history and SEALED before the
outcome exists. Then "the model beat chance" is a comparison between two lines
on the same board, both pre-registered, both recomputable — instead of an
internal calculation that borrows the answers.

WHAT IT DOES NOT DO. It does not make the control smart. A climatological
forecaster says the same number about everything in a domain, and that is the
point: it is the floor any forecaster must clear to have earned anything.

METHOD, stated so it can be attacked.
  · Base rate = hits / (hits + misses) over resolved rows. Voids excluded —
    a void is not an outcome.
  · Domain-specific rate when that domain has >= MIN_DOMAIN_N resolved rows,
    otherwise the global rate. The choice is recorded per row, not inferred.
  · Rows are excluded from the rate if they resolved AFTER the packet date —
    a control may never see an outcome the forecast arm could not see.
  · Probability is clamped to the gate's 5-95 band, and clamping is recorded.
  · Every emitted row carries `control_basis`: the rate, the n behind it,
    whether it was domain or global, the source ledger's as_of, and the
    pairing target. Extra keys survive append_projections, so this rides on
    the sealed row and is auditable forever.

USAGE
  python baserate.py --rates
  python baserate.py --pair forecasts/kkr_raw_last.txt -o control_packet.json
  python kkr.py --ingest control_packet.json --arm control/baserate

  V4ADOPT-1027 (registration v4, Section 3): from v4's adoption on 2026-10-27
  the control is control/trailing; control/baserate is retired and mirrors
  nothing after that date. The method above stays so its rows recompute.
  python baserate.py --rates --method trailing --mirror-of manual/fable-5.1/unattested
  python baserate.py --from-ledger manual/fable-5.1/unattested --method trailing
      --date YYYY-MM-DD --as-of YYYY-MM-DD -o control_trailing_fable51_YYYY-MM-DD.json
  python kkr.py --ingest control_trailing_fable51_YYYY-MM-DD.json --arm control/trailing

The control is ingested through the same gate as every other arm. If the gate
rejects a control row, that is a finding about the row, not about the control.
"""
import argparse, hashlib, json, sys
from collections import Counter
from datetime import datetime, timezone   # KK21e: default packet name needs today
from datetime import date
from pathlib import Path

LEDGER = Path("ledger.json")
MIN_DOMAIN_N = 10
P_FLOOR, P_CEIL = 5, 95
ARM = "control/baserate"


def load_ledger(p: Path):
    if not p.exists():
        sys.exit(f"{p} not found — run from the repo root")
    return json.loads(p.read_text(encoding="utf-8"))


def canon(domain: str) -> str:
    """Collapse to the canonical domain set if domains.json is present."""
    dp = Path("domains.json")
    if not dp.exists():
        return (domain or "").strip().lower()
    try:
        m = json.loads(dp.read_text(encoding="utf-8"))
        table = (m.get("aliases") or m.get("canon") or m.get("map") or m)
        d = (domain or "").strip().lower()
        return table.get(d, d) if isinstance(table, dict) else d
    except Exception:
        return (domain or "").strip().lower()


def rates(data, as_of: date | None = None):
    """Base rates from resolved history. Voids excluded. Nothing counted that
    resolved after `as_of`, so a control never borrows a future outcome."""
    glob = Counter()
    dom = {}
    for p in data["projections"]:
        if p.get("status") not in ("hit", "miss"):
            continue
        rd = p.get("resolved_date")
        if as_of and rd:
            try:
                if date(*map(int, str(rd)[:10].split("-"))) > as_of:
                    continue
            except ValueError:
                pass
        k = "hit" if p["status"] == "hit" else "miss"
        glob[k] += 1
        d = canon(p.get("domain", ""))
        dom.setdefault(d, Counter())[k] += 1
    gn = glob["hit"] + glob["miss"]
    out = {"global": {"n": gn, "rate": (glob["hit"] / gn) if gn else None},
           "domains": {}}
    for d, c in sorted(dom.items()):
        n = c["hit"] + c["miss"]
        out["domains"][d] = {"n": n, "rate": (c["hit"] / n) if n else None}
    return out


def pick(r, domain):
    d = canon(domain)
    ent = r["domains"].get(d)
    if ent and ent["n"] >= MIN_DOMAIN_N and ent["rate"] is not None:
        return ent["rate"], ent["n"], "domain", d
    g = r["global"]
    if g["rate"] is None:
        sys.exit("no resolved rows — the control has nothing to stand on yet")
    return g["rate"], g["n"], "global", d


# V4ADOPT-1027: control/trailing, the control of registration v4 (Section 3).
# Each mirror is priced at the realized hit rate of the mirrored arm's own resolved
# rows, counting only rows resolved on or before the packet date, by the first step
# of this ladder with at least TRAIL_MIN_N rows:
#   1. the mirrored arm, the row's canonical domain
#   2. the mirrored arm, all domains
#   3. every forecaster arm in scope, the row's canonical domain
#   4. every forecaster arm in scope, all domains
# Scope is the forecaster arms registration v4 Section 4 names. The control's own
# rows stay out of the reference class: they carry the claims, and so the outcomes,
# of the rows they mirror. Voids are not outcomes. A resolved row with no
# resolved_date cannot be shown to fall on or before the cut and is left out.
ARM_TRAILING = "control/trailing"
TRAIL_MIN_N = 10
V4_SCOPE = ("manual/fable-5.1/unattested", "manual/opus-5.5/unattested",
            "operator/cold", "operator/advised")
TRAIL_STEPS = {1: "mirrored arm, canonical domain", 2: "mirrored arm, all domains",
               3: "arms in scope, canonical domain", 4: "arms in scope, all domains"}


def cut_date(a):
    """The history cut: --as-of when given, else the UTC date of the run. A
    same-run lane seals before the UTC day rolls, so that is the packet date."""
    if a.as_of:
        return date(*map(int, a.as_of.split("-")))
    return datetime.now(timezone.utc).date()


def trailing_history(data, cut):
    """(arm, canonical domain) -> [hits, misses] over rows resolved on or before cut."""
    hist = {}
    for p in data["projections"]:
        if p.get("status") not in ("hit", "miss"):
            continue
        rd = str(p.get("resolved_date") or "")[:10]
        if not rd or rd > cut.isoformat():
            continue
        c = hist.setdefault((p.get("model") or "", canon(p.get("domain", ""))), [0, 0])
        c[0 if p["status"] == "hit" else 1] += 1
    return hist


def pick_trailing(hist, mirror_of, domain):
    """(rate, n, step, canonical domain) from the first step of the ladder
    with at least TRAIL_MIN_N resolved rows."""
    d = canon(domain)
    for step, arms, dom in ((1, (mirror_of,), d), (2, (mirror_of,), None),
                            (3, V4_SCOPE, d), (4, V4_SCOPE, None)):
        h = m = 0
        for (arm, dd), (x, y) in hist.items():
            if arm in arms and (dom is None or dd == dom):
                h, m = h + x, m + y
        if h + m >= TRAIL_MIN_N:
            return h / (h + m), h + m, step, d
    sys.exit("no step of the trailing ladder has %d resolved rows - the control "
             "has nothing to stand on yet" % TRAIL_MIN_N)


def trailing_setup(a, data):
    if a.mirror_of not in V4_SCOPE:
        sys.exit("refusing: control/trailing mirrors the arms registration v4 "
                 "Section 4 names (%s); got %r" % (", ".join(V4_SCOPE), a.mirror_of))
    cut = cut_date(a)
    lsha = hashlib.sha256(Path(a.ledger).read_bytes()
                          .replace(b"\r\n", b"\n")).hexdigest()[:16]
    return cut, trailing_history(data, cut), lsha


def trailing_basis(a, cut, lsha, data, rate, n, step, d, clamped):
    return {
        "arm": ARM_TRAILING,
        "rule": "climatological, trailing - the realized hit rate of the mirrored "
                "arm's own resolved rows, by the first step of the ladder with at "
                "least %d rows (registration v4, Section 3)" % TRAIL_MIN_N,
        "mirror_of": a.mirror_of,
        "step": step,
        "step_name": TRAIL_STEPS[step],
        "rate": round(rate, 4),
        "n": n,
        "domain_canonical": d,
        "min_n": TRAIL_MIN_N,
        "scope": list(V4_SCOPE),
        "history_cut": cut.isoformat(),
        "ledger_as_of": data.get("as_of"),
        "ledger_sha16": lsha,
        "clamped_to_gate_band": clamped,
        "registration": "KALIBRIERWARTE_REGISTERED_REPORT_v4.md, Section 3",
        "note": "pre-registered before the outcome existed. The floor the mirrored "
                "arm must clear, priced from its own record; it is not an attempt "
                "to be right.",
    }


def cmd_rates_trailing(a):
    data = load_ledger(Path(a.ledger))
    if a.mirror_of not in V4_SCOPE:
        sys.exit("refusing: %r is not an arm registration v4 Section 4 names" % (a.mirror_of,))
    cut = cut_date(a)
    hist = trailing_history(data, cut)
    print(f"control/trailing for {a.mirror_of}, history cut {cut.isoformat()} "
          f"(ledger as_of {data.get('as_of')})")
    for dd in sorted({dd for (arm, dd) in hist if arm in V4_SCOPE}):
        rate, n, step, _ = pick_trailing(hist, a.mirror_of, dd)
        print(f"  {dd:16} step {step} ({TRAIL_STEPS[step]:31}) n={n:<4} "
              f"rate={rate:.3f} -> {round(rate * 100)}%")


def cmd_rates(a):
    data = load_ledger(Path(a.ledger))
    r = rates(data)
    g = r["global"]
    print(f"ledger as_of {data.get('as_of')}")
    print(f"GLOBAL  n={g['n']:<4} rate={g['rate']:.3f}"
          f"  -> control would forecast {round(g['rate']*100)}%")
    print(f"\nper domain (domain-specific used at n >= {MIN_DOMAIN_N}):")
    for d, e in r["domains"].items():
        use = "domain" if e["n"] >= MIN_DOMAIN_N else "global (n too small)"
        print(f"  {d:22} n={e['n']:<4} rate={e['rate']:.3f}   -> {use}")


def cmd_pair(a):
    data = load_ledger(Path(a.ledger))
    src = json.loads(Path(a.pair).read_text(encoding="utf-8"))
    if isinstance(src, dict):
        src = src.get("projections") or src.get("rows") or []
    if not src:
        sys.exit("nothing to pair — expected a JSON array of projections")
    as_of = None
    if a.as_of:
        as_of = date(*map(int, a.as_of.split("-")))
    r = rates(data, as_of)
    trailing = getattr(a, "method", "baserate") == "trailing"  # V4ADOPT-1027
    if trailing:
        cut, hist, lsha = trailing_setup(a, data)
    out = []
    for p in src:
        if trailing:
            rate, n, step, d = pick_trailing(hist, a.mirror_of, p.get("domain", ""))
            basis = None
        else:
            rate, n, basis, d = pick(r, p.get("domain", ""))
        pct = round(rate * 100)
        clamped = False
        if pct < P_FLOOR:
            pct, clamped = P_FLOOR, True
        elif pct > P_CEIL:
            pct, clamped = P_CEIL, True
        row = {
            "statement": p["statement"],
            "resolution": p["resolution"],
            "failure_condition": p.get("failure_condition"),
            "domain": p.get("domain"),
            "deadline": p["deadline"],
            "probability": pct,
            "citations": p.get("citations", []),
            "control_basis": {
                "arm": ARM,
                "rule": "climatological — same probability for every row drawn "
                        "from the same reference class",
                "rate": round(rate, 4),
                "n": n,
                "basis": basis,
                "domain_canonical": d,
                "min_domain_n": MIN_DOMAIN_N,
                "ledger_as_of": data.get("as_of"),
                "history_cutoff": a.as_of or "none — all resolved rows",
                "clamped_to_gate_band": clamped,
                "note": "pre-registered before the outcome existed. This is the "
                        "floor the forecaster arm must clear; it is not an "
                        "attempt to be right.",
            },
        }
        if trailing:
            row["control_basis"] = trailing_basis(a, cut, lsha, data, rate, n, step, d, clamped)
        if p.get("id"):
            row["control_basis"]["control_for"] = p["id"]
        out.append(row)
    # KK21f: never destroy another run's packet. The fixed default did it on
    # 2026-08-03 and cost KKR-20260803-01 its basis permanently; the composed
    # default is better and still not a guarantee.
    _txt = json.dumps(out, indent=2, ensure_ascii=False) + "\n"
    _p = Path(a.out)
    if _p.exists() and _p.read_text(encoding="utf-8", errors="replace") != _txt:
        _n = 2
        while _p.with_name(f"{Path(a.out).stem}_{_n}{_p.suffix}").exists():
            _n += 1
        _alt = _p.with_name(f"{Path(a.out).stem}_{_n}{_p.suffix}")
        print(f"baserate · {_p.name} already holds a different run - writing "
              f"{_alt.name} rather than discarding it", file=sys.stderr)
        _p = _alt
        a.out = str(_p)
    _p.write_text(_txt, encoding="utf-8")
    b = Counter(x["control_basis"]["step" if trailing else "basis"] for x in out)
    pr = Counter(x["probability"] for x in out)
    print(f"{len(out)} control row(s) -> {a.out}")
    print(f"  {'step' if trailing else 'basis'}: {dict(b)}   probabilities: {dict(pr)}")
    print(f"  next: python kkr.py --ingest {a.out} --arm {ARM_TRAILING if trailing else ARM}")


def cmd_from_ledger(a):
    """Pair against rows an arm sealed on one day, read from the ledger.

    Ids travel with the rows, so every control row records what it controls.
    Refuses to cross a day boundary unless told: a control issued after the
    gate moved cannot mirror rows sealed under the old gate, and a control
    that does not mirror its arm is not a control.
    """
    from datetime import datetime, timezone
    data = load_ledger(Path(a.ledger))
    day = a.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if day != today and not a.any_date:
        sys.exit(f"refusing: {day} is not today ({today}). A control paired "
                 f"across days may face a different gate than the arm did. "
                 f"Pass --any-date if that is understood and intended.")
    rows = [p for p in data["projections"]
            if p.get("model") == a.from_ledger
            and str(p.get("date_issued", ""))[:10] == day
            and p.get("status") == "open"]
    if not rows:
        sys.exit(f"no open rows for arm {a.from_ledger} issued {day}")
    a.pair = None
    src = [{"statement": r["statement"], "resolution": r["resolution"],
            "failure_condition": r.get("failure_condition"),
            "domain": r.get("domain"), "deadline": r["deadline"],
            "citations": r.get("citations", []), "id": r["id"]} for r in rows]
    tmp = Path(a.out).with_suffix(".src.json")
    tmp.write_text(json.dumps(src, ensure_ascii=False), encoding="utf-8")
    a.pair = str(tmp)
    cmd_pair(a)
    tmp.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser(description="climatological control arm (RPAS 4.06)")
    ap.add_argument("--ledger", default="ledger.json")
    ap.add_argument("--rates", action="store_true")
    ap.add_argument("--pair", metavar="FILE")
    ap.add_argument("--from-ledger", metavar="ARM_TAG",
                    help="pair against rows this arm sealed today, taken from "
                         "the ledger so ids travel with them")
    ap.add_argument("--date", metavar="YYYY-MM-DD",
                    help="with --from-ledger: the issue date (default today UTC)")
    ap.add_argument("--any-date", action="store_true",
                    help="permit pairing rows issued on an earlier day. A control "
                         "issued after a gate change cannot mirror the arm it is "
                         "supposed to control; this switch says you know that.")
    ap.add_argument("-o", "--out", default=None,
                    help="output packet. Defaults to a name composed from the "
                         "arm and date (--from-ledger) or the input filename "
                         "(--pair). The old fixed default silently discarded "
                         "the previous run's packet.")
    ap.add_argument("--as-of", dest="as_of", metavar="YYYY-MM-DD",
                    help="exclude rows resolved after this date from the rate")
    # V4ADOPT-1027: the trailing method (registration v4, Section 3)
    ap.add_argument("--method", choices=("baserate", "trailing"), default="baserate",
                    help="baserate: control/baserate, retired 2026-10-27 and kept so "
                         "its rows recompute. trailing: control/trailing, priced from "
                         "the mirrored arm's own resolved rows")
    ap.add_argument("--mirror-of", dest="mirror_of", metavar="ARM_TAG",
                    help="with --method trailing: the arm being mirrored (defaults "
                         "to the --from-ledger arm)")
    a = ap.parse_args()
    if a.method == "trailing" and not a.mirror_of and a.from_ledger:
        a.mirror_of = a.from_ledger
    if a.method == "trailing" and not a.mirror_of:
        ap.error("--method trailing needs --mirror-of (or --from-ledger)")
    # KK21e: compose a run-distinguishing default. A fixed filename cannot hold
    # two runs and answers a second one by discarding the first, without error.
    if not a.out:
        if a.from_ledger:
            _slug = "".join(c if c.isalnum() else "-"
                            for c in str(a.from_ledger)).strip("-")
            _day = a.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
            a.out = f"control_packet_{_day}_{_slug}.json"
        elif a.pair:
            _stem = Path(a.pair).stem
            a.out = f"control_packet_{_stem}.json"
        else:
            a.out = "control_packet.json"
    if a.rates:
        return cmd_rates_trailing(a) if a.method == "trailing" else cmd_rates(a)
    if a.from_ledger:
        return cmd_from_ledger(a)
    if a.pair:
        return cmd_pair(a)
    ap.print_help()


if __name__ == "__main__":
    main()
