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

The control is ingested through the same gate as every other arm. If the gate
rejects a control row, that is a finding about the row, not about the control.
"""
import argparse, json, sys
from collections import Counter
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
        table = m.get("canon") or m.get("map") or m
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
    out = []
    for p in src:
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
        if p.get("id"):
            row["control_basis"]["control_for"] = p["id"]
        out.append(row)
    Path(a.out).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    b = Counter(x["control_basis"]["basis"] for x in out)
    pr = Counter(x["probability"] for x in out)
    print(f"{len(out)} control row(s) -> {a.out}")
    print(f"  basis: {dict(b)}   probabilities: {dict(pr)}")
    print(f"  next: python kkr.py --ingest {a.out} --arm {ARM}")


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
    ap.add_argument("-o", "--out", default="control_packet.json")
    ap.add_argument("--as-of", dest="as_of", metavar="YYYY-MM-DD",
                    help="exclude rows resolved after this date from the rate")
    a = ap.parse_args()
    if a.rates:
        return cmd_rates(a)
    if a.from_ledger:
        return cmd_from_ledger(a)
    if a.pair:
        return cmd_pair(a)
    ap.print_help()


if __name__ == "__main__":
    main()
