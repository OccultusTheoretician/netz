#!/usr/bin/env python3
"""lag_plot.py - the forgetting curve (LAG-1016).
How long a row waits past its deadline before the desk resolves it, and what
the wait costs. Reads ledger.json only; writes docs/LAG_latest.md. Nothing it
prints enters any forecasting input. DRAFT tier (instrument-authored).
"""
import json, sys, pathlib, datetime, collections, argparse

HERE = pathlib.Path(__file__).resolve().parent

def d(s):
    try:
        return datetime.date.fromisoformat(str(s)[:10])
    except ValueError:
        return None

def brier(rows):
    if not rows:
        return None
    return sum(((r["probability"] / 100.0) - (1.0 if r["status"] == "hit" else 0.0)) ** 2 for r in rows) / len(rows)

def bucket(days):
    if days <= 0: return "on-or-before deadline"
    if days <= 3: return "1-3 d"
    if days <= 7: return "4-7 d"
    if days <= 14: return "8-14 d"
    if days <= 30: return "15-30 d"
    return "over 30 d"

ORDER = ["on-or-before deadline", "1-3 d", "4-7 d", "8-14 d", "15-30 d", "over 30 d"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=str(HERE / "ledger.json"))
    ap.add_argument("--out", default=str(HERE / "docs" / "LAG_latest.md"))
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    today = d(a.today)
    P = json.loads(pathlib.Path(a.ledger).read_text(encoding="utf-8"))["projections"]
    scored, overdue = [], []
    for p in P:
        dl = d(p.get("deadline"))
        if not dl:
            continue
        if p.get("status") in ("hit", "miss"):
            rd = d(p.get("resolved_date"))
            if rd:
                p["_lag"] = (rd - dl).days
                scored.append(p)
        elif p.get("status") == "open" and dl < today:
            p["_age"] = (today - dl).days
            overdue.append(p)
    lines = []
    lines.append("# The forgetting curve - resolution lag (LAG-1016)\n")
    lines.append(f"As of {today}. Ledger rows: {len(P)}. Scored with a deadline and a resolved date: {len(scored)}. Open past deadline: {len(overdue)}.\n")
    lines.append("Lag = resolved_date minus deadline, in days. A row the desk forgets sits in the right-hand buckets. No pooled score is printed (RPAS 5.04: a Brier belongs to one forecaster); the lag table carries counts and hit share only, and Brier appears per arm below.\n")
    lines.append("## Lag of scored rows\n")
    lines.append("| bucket | rows | hit share |")
    lines.append("|---|---|---|")
    byb = collections.defaultdict(list)
    for p in scored:
        byb[bucket(p["_lag"])].append(p)
    for b in ORDER:
        rows = byb.get(b, [])
        if not rows:
            continue
        hs = sum(1 for r in rows if r["status"] == "hit") / len(rows)
        lines.append(f"| {b} | {len(rows)} | {hs:.2f} |")
    lags = sorted(p["_lag"] for p in scored)
    if lags:
        med = lags[len(lags) // 2]
        p90 = lags[min(len(lags) - 1, int(len(lags) * 0.9))]
        lines.append(f"\nMedian lag {med} d; 90th percentile {p90} d; max {lags[-1]} d; share resolved on or before deadline {sum(1 for x in lags if x <= 0) / len(lags):.2f}.\n")
    lines.append("## Lag by arm (scored rows)\n")
    lines.append("| arm | rows | median lag d | over 14 d | Brier |")
    lines.append("|---|---|---|---|---|")
    bya = collections.defaultdict(list)
    for p in scored:
        bya[p.get("model") or "?"].append(p)
    for arm, rows in sorted(bya.items(), key=lambda kv: -len(kv[1])):
        if len(rows) < 10:
            continue
        ls = sorted(r["_lag"] for r in rows)
        lines.append(f"| {arm} | {len(rows)} | {ls[len(ls) // 2]} | {sum(1 for x in ls if x > 14)} | {brier(rows):.3f} |")
    lines.append("\n## Open rows past deadline (the queue the desk is forgetting)\n")
    lines.append("| overdue age | rows | arms |")
    lines.append("|---|---|---|")
    byo = collections.defaultdict(list)
    for p in overdue:
        byo[bucket(p["_age"])].append(p)
    for b in ORDER[1:]:
        rows = byo.get(b, [])
        if not rows:
            continue
        arms = collections.Counter(r.get("model") for r in rows).most_common(3)
        lines.append(f"| {b} | {len(rows)} | " + ", ".join(f"{m} {n}" for m, n in arms) + " |")
    oldest = sorted(overdue, key=lambda r: -r["_age"])[:10]
    if oldest:
        lines.append("\nTen oldest open rows:\n")
        for r in oldest:
            lines.append(f"- {r.get('id')} deadline {r.get('deadline')} ({r['_age']} d) {r.get('model')} - {str(r.get('statement'))[:90]}")
    lines.append("\nReading rule: compare each arm's over-14-day count with its row count; an arm whose late rows cluster is an arm whose claims the desk cannot look up, and that is a property of the claims, not of the lateness. Either way the queue table is the to-do list; the keys pass runs before each sitting and the overdue rows are the sitting.\n")
    txt = "\n".join(lines)
    pathlib.Path(a.out).write_text(txt, encoding="ascii", errors="replace")
    print(txt)
    print(f"\nwritten: {a.out}")

if __name__ == "__main__":
    main()
