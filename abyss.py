#!/usr/bin/env python3
"""
abyss.py — the abyssal sequence tree over a sealed ledger.

THE THEOREM, MADE COUNTABLE.

To path is to commit. To commit under bound is to abstract. Abstraction is
lossy, and by a counting argument a lossy map must collapse distinct states
together — and those collapsed states ARE the blind region. Pathing does not
raise the risk of a blind region; it necessitates one. That is the keystone,
and until now it has been an argument.

A ledger of independent rows hides it. But forecasts are not independent. When
a sealed projection resolves, the world takes a branch, and every sealed
question that was conditional on the other branch stops being answerable. Those
questions were not wrong. They were COLLAPSED — foreclosed by a path the world
took. That set is the abyssal shadow the resolution casts, and its size is
measurable: shadow mass, the count of sealed questions a single resolution
killed.

STATUS CLASSES, AND WHY FORECLOSED IS NOT VOID

    hit / miss    met the world and was scored
    void          the question was defective; we withdrew it, with a reason
    FORECLOSED    the question was sound and never got to meet the world,
                  because a prior resolution removed the branch it stood on

Void is our failure. Foreclosed is the world's. They must not share a bucket,
and neither may enter the Brier — a foreclosed row was never adjudicated, and
scoring it in either direction would be inventing a result.

THE INTEGRITY PROBLEM, WHICH IS THE WHOLE DESIGN

A precondition declared AFTER its parent resolved is a way to launder a miss
into a foreclosure. Seal a row, watch it go wrong, then announce it depended on
something that had already gone the other way, and it leaves the scoring
population without ever being counted against you.

So: a precondition is only honoured when the child was sealed while the parent
was still OPEN. `check` reports every violation by id, and the tree renders a
retrofitted edge in red rather than silently trusting it.

    python abyss.py status              the frontier, the shadows, the mass
    python abyss.py check               retrofit detection
    python abyss.py tree --out t.svg    the board: solid live, dotted foreclosed

A projection declares its condition at seal time:

    "precondition": {"id": "KKR-20260727-01", "requires": "hit"}

Standard library only. Nothing here writes to the ledger.
"""

import argparse
import json
import sys
from datetime import datetime, date
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"
RESOLVED = ("hit", "miss")


def read_json(p):
    raw = Path(p).read_bytes()
    for bom, enc in ((b"\xff\xfe", "utf-16"), (b"\xfe\xff", "utf-16"),
                     (b"\xef\xbb\xbf", "utf-8-sig")):
        if raw.startswith(bom):
            return json.loads(raw.decode(enc))
    return json.loads(raw.decode("utf-8"))


def day(s):
    try:
        return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def load():
    d = read_json(LEDGER)
    return {p["id"]: p for p in d["projections"]}, d


# ----------------------------------------------------------------------
def classify(rows):
    """Walk the conditions to fixed point. A child is foreclosed when its parent
    resolved the other way, and foreclosure propagates: a question standing on a
    collapsed question is itself collapsed."""
    state = {i: r["status"] for i, r in rows.items()}
    shadow = {i: [] for i in rows}
    retrofit = []
    for i, r in rows.items():
        pre = r.get("precondition")
        if not pre:
            continue
        pid = pre.get("id")
        par = rows.get(pid)
        if par is None:
            retrofit.append((i, pid, "parent not in the ledger"))
            continue
        ci, pr = day(r.get("date_issued")), day(par.get("resolved_date"))
        if pr and ci and ci > pr:
            retrofit.append((i, pid, f"sealed {ci} — after its parent resolved {pr}; "
                                     f"a condition declared after the fact can launder "
                                     f"a miss into a foreclosure and is not honoured"))
    changed = True
    while changed:
        changed = False
        for i, r in rows.items():
            if state[i] != "open":
                continue
            pre = r.get("precondition")
            if not pre:
                continue
            pid, need = pre.get("id"), pre.get("requires")
            if any(x[0] == i for x in retrofit):
                continue
            ps = state.get(pid)
            if ps in RESOLVED and ps != need:
                state[i] = "foreclosed"; shadow[pid].append(i); changed = True
            elif ps == "foreclosed":
                state[i] = "foreclosed"; shadow[pid].append(i); changed = True
    return state, shadow, retrofit


def summarise(rows, state, shadow):
    live = [i for i in rows if state[i] == "open"]
    fore = [i for i in rows if state[i] == "foreclosed"]
    res = [i for i in rows if state[i] in RESOLVED]
    mass = sorted(((len(v), k) for k, v in shadow.items() if v), reverse=True)
    return live, fore, res, mass


def cmd_status(a):
    rows, _ = load()
    state, shadow, retro = classify(rows)
    live, fore, res, mass = summarise(rows, state, shadow)
    print("\nABYSSAL SEQUENCE — the shadow the record casts on itself")
    print("=" * 68)
    print(f"  {len(rows)} sealed · {len(res)} met the world · {len(live)} live frontier")
    print(f"  {len([i for i in rows if state[i]=='void'])} void (our defect)")
    print(f"  {len(fore)} FORECLOSED (the world's path)")
    conditional = sum(1 for r in rows.values() if r.get("precondition"))
    print(f"  {conditional} of {len(rows)} rows declare a condition"
          + ("" if conditional else "  — the tree is flat until they do"))
    if mass:
        print("\n  SHADOW MASS — sealed questions each resolution collapsed")
        for n, k in mass[:10]:
            r = rows[k]
            print(f"    {n:>3}  {k}  [{r.get('status')}]  {r['statement'][:56]}")
        print("\n  Each of those was a sound question that never met the world.")
        print("  Not a miss. Collapsed — the branch it stood on was removed.")
    if retro:
        print(f"\n  {len(retro)} RETROFITTED CONDITION(S) — not honoured:")
        for i, pid, why in retro[:8]:
            print(f"    {i} -> {pid}: {why}")
    if fore:
        print("\n  FORECLOSED, and excluded from every Brier on this desk:")
        for i in fore[:10]:
            pre = rows[i]["precondition"]
            print(f"    {i}  needed {pre['id']} to be {pre['requires']}")
    print("\n  A foreclosed row is never scored. It was never adjudicated, and")
    print("  scoring it in either direction would be inventing a result.\n")
    return 0


def cmd_check(a):
    rows, _ = load()
    state, shadow, retro = classify(rows)
    print("\nCONDITION INTEGRITY")
    print("-" * 60)
    if not retro:
        print("  PASS — every declared condition was sealed while its parent was open.")
        print("  No row can have been moved out of the scoring population after")
        print("  the fact.\n")
        return 0
    for i, pid, why in retro:
        print(f"  FAIL  {i} -> {pid}\n        {why}")
    print(f"\n  {len(retro)} condition(s) not honoured. Those rows stay in the")
    print("  scoring population and will be scored as issued.\n")
    return 1


def cmd_tree(a):
    rows, _ = load()
    state, shadow, retro = classify(rows)
    kids = {}
    for i, r in rows.items():
        pre = r.get("precondition")
        if pre and pre.get("id") in rows:
            kids.setdefault(pre["id"], []).append(i)
    roots = [i for i, r in rows.items()
             if not r.get("precondition") and (i in kids or state[i] != "open")]
    roots.sort(key=lambda i: (rows[i].get("date_issued", ""), i))
    COL = {"hit": "#7fb08a", "miss": "#a8492f", "void": "#6e6a63",
           "open": "#c9a227", "foreclosed": "#4a5058"}
    W, rowh, x0 = 1500, 46, 60
    out, y = [], 70
    retro_ids = {x[0] for x in retro}

    def draw(i, depth, y):
        r, st = rows[i], state[i]
        x = x0 + depth * 46
        c = COL.get(st, "#8b8d92")
        dash = ' stroke-dasharray="5 5"' if st == "foreclosed" else ""
        out.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{"none" if st=="foreclosed" else c}" '
                   f'stroke="{c}" stroke-width="2"{dash}/>')
        op = ".45" if st == "foreclosed" else "1"
        out.append(f'<text x="{x+18}" y="{y-4}" font-family="ui-monospace,monospace" '
                   f'font-size="13" fill="#cfd3d8" fill-opacity="{op}">{i}</text>')
        out.append(f'<text x="{x+18}" y="{y+13}" font-family="ui-monospace,monospace" '
                   f'font-size="11.5" fill="#8b8d92" fill-opacity="{op}">'
                   f'{r["statement"][:104].replace("&","&amp;").replace("<","&lt;")}</text>')
        out.append(f'<text x="{W-70}" y="{y+3}" text-anchor="end" '
                   f'font-family="ui-monospace,monospace" font-size="11.5" fill="{c}">'
                   f'{st.upper()}{"" if st!="foreclosed" else " · collapsed"}</text>')
        ny = y + rowh
        for k in sorted(kids.get(i, [])):
            kst = state[k]
            edge = ("#a8492f" if k in retro_ids else
                    ("#4a5058" if kst == "foreclosed" else "#3a424b"))
            ed = ' stroke-dasharray="4 5"' if kst == "foreclosed" else ""
            out.append(f'<path d="M{x} {y+8} L{x} {ny} L{x+40} {ny}" fill="none" '
                       f'stroke="{edge}" stroke-width="1.6"{ed}/>')
            ny = draw(k, depth + 1, ny)
        return ny

    for r0 in roots:
        y = draw(r0, 0, y)
    H = max(240, y + 60)
    legend = ("".join(
        f'<circle cx="{70+i*230}" cy="{H-32}" r="6" fill="{"none" if k=="foreclosed" else v}" '
        f'stroke="{v}" stroke-width="2"'
        f'{" stroke-dasharray=\'5 5\'" if k=="foreclosed" else ""}/>'
        f'<text x="{84+i*230}" y="{H-27}" font-family="ui-monospace,monospace" '
        f'font-size="12" fill="#8b8d92">{k}</text>'
        for i, (k, v) in enumerate(COL.items())))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="#080B0F"/>'
           f'<text x="60" y="40" font-family="ui-monospace,monospace" font-size="15" '
           f'letter-spacing="4" fill="#c9a227">ABYSSAL SEQUENCE &#183; '
           f'dotted is collapsed, not wrong</text>'
           + "".join(out) + legend + "</svg>\n")
    Path(a.out).write_text(svg, encoding="utf-8")
    print(f"  tree → {a.out}  ({len(roots)} root(s), {len(rows)} row(s))")
    return 0


def main():
    ap = argparse.ArgumentParser(description="abyss — the sequence tree over the ledger")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("status"); sub.add_parser("check")
    t = sub.add_parser("tree"); t.add_argument("--out", default="docs/abyss_tree.svg")
    a = ap.parse_args()
    if not a.cmd:
        ap.print_help(); return 0
    return {"status": cmd_status, "check": cmd_check, "tree": cmd_tree}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
