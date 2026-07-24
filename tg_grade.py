#!/usr/bin/env python3
"""
NETZ WAR DESK — Module 3: grade, render, publish.

Reads a clustered-events file from Module 2 (tg_cluster.py), RE-DERIVES the
cross-bias grade from primitives, renders the WAR DESK markdown section for the
daily battle report, and writes the live tile for the domain.

Inputs   forecasts/tg_events_YYYYMMDD_HHMM.json
Outputs  forecasts/WARDESK_YYYYMMDD_HHMM.md   (dated section)
         forecasts/WARDESK_latest.md          (stable path netz.py injects from)
         docs/war_desk.json                   (live tile for docs/index.html)

Grading ladder (recomputed here, never trusted from upstream):
  A  3+ independently-biased camps agree on a specific sub-zone anchor
  B  2 camps agree
  C  3+ reports, ONE camp   -- echo, NOT corroboration; printed under warning
  F  single source          -- counted, never published as an event

Usage
  python tg_grade.py --latest
  python tg_grade.py --file forecasts/tg_events_20260724_2104.json
  python tg_grade.py --latest --dry-run      # print to stdout, write nothing
  python tg_grade.py --latest --schema       # field-resolution report, then exit

Stdlib only. No utcnow(). All regex raw-stringed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECASTS = HERE / "forecasts"
DOCS = HERE / "docs"

ZONE_LABELS = {
    "russia_ukraine": "Russia-Ukraine Theatre",
    "israel_gaza": "Israel-Gaza-Levant Theatre",
    "iran": "Iran Theatre",
    "sudan": "Sudan",
    "sahel": "Sahel",
    "drc": "DR Congo",
    "myanmar": "Myanmar",
    "kurdistan": "Kurdistan",
    "taiwan": "Taiwan Strait",
    "yemen": "Yemen",
    "syria": "Syria",
    "lebanon": "Lebanon",
}

BAND = {"A": "\u2b1b", "B": "\u25fc", "C": "\u25a8", "F": "\u25fb"}

# ---------------------------------------------------------------- field resolve

_SCHEMA_HITS: dict[str, Counter] = {}


def pick(d: dict, *names, default=None):
    """Tolerant key lookup across plausible upstream names. Records which key hit
    so --schema can report exactly what Module 2 is emitting."""
    slot = names[0]
    _SCHEMA_HITS.setdefault(slot, Counter())
    for n in names:
        if isinstance(d, dict) and n in d and d[n] not in (None, "", [], {}):
            _SCHEMA_HITS[slot][n] += 1
            return d[n]
    _SCHEMA_HITS[slot]["<missing>"] += 1
    return default


def as_list(v) -> list:
    if v is None:
        return []
    if isinstance(v, (list, tuple, set)):
        return [x for x in v if x not in (None, "")]
    if isinstance(v, dict):
        return [k for k in v.keys()]
    return [v]


def parse_ts(v):
    if not v:
        return None
    if isinstance(v, (int, float)):
        try:
            return datetime.fromtimestamp(float(v), tz=timezone.utc)
        except (ValueError, OSError, OverflowError):
            return None
    s = str(v).strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(s)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def fmt_ts(dt) -> str:
    return dt.strftime("%d %b %H%MZ") if dt else "undated"


# ---------------------------------------------------------------- normalization

def normalize(raw: dict) -> dict:
    """Pull one clustered event down to the primitives the published claim rests on."""
    anchors = as_list(pick(raw, "anchors", "anchor", "specifics", "specific",
                           "key", "anchor_terms", default=[]))
    zone = pick(raw, "zone", "theatre", "theater", "region", default="unzoned")

    camps = sorted({str(c).strip().lower() for c in
                    as_list(pick(raw, "camps", "bias_camps", "biases", "bias",
                                 default=[])) if str(c).strip()})
    sides = sorted({str(x).strip().upper() for x in
                    as_list(pick(raw, "sides", "n_sides_list", default=[])) if str(x).strip()})
    balance = pick(raw, "report_balance", "side_balance", default={}) or {}
    variants = sorted({str(v).strip().lower() for v in
                       as_list(pick(raw, "anchor_aliases", default=[]))})
    chans_side = pick(raw, "channels_per_side", default={}) or {}
    solo = sorted(str(x).upper() for x in
                  as_list(pick(raw, "single_outlet_sides", default=[])))

    msgs = as_list(pick(raw, "sources", "messages", "reports", "items", "posts", default=[]))
    n_msgs = pick(raw, "n_reports", "report_count", "count", "n", "n_messages",
                  default=len(msgs) or 0)
    try:
        n_msgs = int(n_msgs)
    except (TypeError, ValueError):
        n_msgs = len(msgs)

    # distinct channels: a camp echoing itself six times is one voice, not six
    channels = set()
    per_camp = Counter()
    for m in msgs:
        if not isinstance(m, dict):
            continue
        ch = pick(m, "channel", "chan", "source", "username", default=None)
        cp = pick(m, "side", "camp", "bias", "bias_camp", default=None)
        if ch:
            channels.add(str(ch))
        if cp and ch:
            per_camp[str(cp).strip().lower()] += 1
    n_channels = len(channels) or pick(raw, "n_channels", "channel_count", default=0)

    # camps may only be recoverable from the messages
    if not camps and per_camp:
        camps = sorted(per_camp.keys())
    if not sides and per_camp:
        sides = sorted({k.upper() for k in per_camp})
    if not balance and per_camp:
        balance = dict(per_camp.most_common())

    span = pick(raw, "span_hours", "window_hours", "span", "duration_hours", default=None)
    try:
        span = float(span) if span is not None else None
    except (TypeError, ValueError):
        span = None

    first = parse_ts(pick(raw, "first_seen", "first", "earliest", "start", default=None))
    last = parse_ts(pick(raw, "last_seen", "last", "latest", "newest", "end", default=None))
    if span is None and first and last:
        span = (last - first).total_seconds() / 3600.0

    weapons = sorted({str(w).strip().lower() for w in
                      as_list(pick(raw, "weapons", "weapon", "munitions", default=[]))
                      if str(w).strip()})

    cas_raw = pick(raw, "casualties", "casualty", "casualty_figure", "killed",
                   "casualty_figures", default=None)

    return {
        "anchors": [str(a).strip().lower() for a in anchors],
        "zone": str(zone),
        "camps": camps,
        "sides": sides,
        "balance": {str(k): int(v) for k, v in dict(balance).items()},
        "variants": variants,
        "chans_side": {str(k): int(v) for k, v in dict(chans_side).items()},
        "solo_sides": solo,
        "digests": int(pick(raw, "digest_reports", default=0) or 0),
        "track": str(pick(raw, "track", default="kinetic")),
        "st_actors": [str(a) for a in as_list(pick(raw, "statement_actors", default=[]))],
        "n_msgs": n_msgs,
        "n_channels": int(n_channels or 0),
        "span": span,
        "first": first,
        "last": last,
        "weapons": weapons,
        "casualties": casualty_view(cas_raw, msgs),
        "upstream_grade": str(pick(raw, "grade", "admiralty", default="") or "").upper()[:1],
    }


def casualty_view(cas_raw, msgs: list) -> dict:
    """A cross-bias-confirmed EVENT does not confirm a cross-bias-claimed COUNT.
    Returns a range with camp attribution where the data allows it, and says so
    plainly when it does not."""
    figures: list[tuple[int, str]] = []

    for m in msgs:
        if not isinstance(m, dict):
            continue
        v = pick(m, "casualties", "casualty", "killed", default=None)
        camp = str(pick(m, "side", "camp", "bias", default="unattributed")).upper()
        for n in _ints(v):
            figures.append((n, camp))

    if not figures:
        for n in _ints(cas_raw):
            figures.append((n, "unattributed"))
        if figures:
            lo = min(f[0] for f in figures)
            hi = max(f[0] for f in figures)
            return {"kind": "unattributed", "lo": lo, "hi": hi,
                    "camps": [], "n": len(figures)}
        return {"kind": "none"}

    lo = min(f[0] for f in figures)
    hi = max(f[0] for f in figures)
    camps = sorted({c for _, c in figures if c != "UNATTRIBUTED"})
    return {"kind": "attributed" if camps else "unattributed",
            "lo": lo, "hi": hi, "camps": camps, "n": len(figures)}


def _ints(v) -> list[int]:
    out = []
    for x in as_list(v):
        if isinstance(x, bool):
            continue
        if isinstance(x, (int, float)):
            out.append(int(x))
        elif isinstance(x, str):
            out.extend(int(g) for g in re.findall(r"\d{1,5}", x))
        elif isinstance(x, dict):
            out.extend(_ints(x.get("n") or x.get("count") or x.get("killed")))
    return [n for n in out if 0 <= n <= 100000]


# ---------------------------------------------------------------------- grading

def recompute_grade(ev: dict) -> str:
    """The grade is re-derived here from camp count and report count, because the
    published sentence -- 'N hostile camps agreed' -- must be checkable against
    the same file it is printed from."""
    n_sides = len(ev["sides"]) or len(ev["camps"])
    n = max(ev["n_msgs"], ev["n_channels"], 1)
    if n_sides >= 3:
        return "A"
    if n_sides == 2:
        return "B"
    if n >= 3:
        return "C"
    return "F"


def zone_label(z: str) -> str:
    return ZONE_LABELS.get(z, z.replace("_", " ").title())


def anchor_label(a: list[str]) -> str:
    return "/".join(x.title() for x in a) if a else "unanchored"


# --------------------------------------------------------------------- renderer

def render_section(events: list[dict], src: Path, divergences: list[str]) -> str:
    now = datetime.now(timezone.utc)
    kin = [e for e in events if e.get("track") != "statement"]
    stm = [e for e in events if e.get("track") == "statement"]
    by = {g: [e for e in kin if e["grade"] == g] for g in "ABCF"}
    sby = {g: [e for e in stm if e["grade"] == g] for g in "ABCF"}
    for g in "ABC":
        sby[g].sort(key=lambda e: (-len(e["sides"]), -e["n_msgs"]))
    for g in "ABC":
        by[g].sort(key=lambda e: (-len(e["sides"]), -e["n_msgs"]))

    o: list[str] = []
    o.append("## WAR DESK \u2014 CROSS-BIAS CONFIRMED EVENTS\n")
    o.append("*Method: a claim is single-source until an independently-biased channel "
             "corroborates it. Grade A = three or more hostile SIDES agree on a specific "
             "sub-zone anchor. Grade B = two sides. Grade C = repeated inside one side, "
             "which is echo, not corroboration. Grade F = single source, counted and "
             "withheld. Sides are counted, not outlet labels: three Kremlin-aligned "
             "channels are one voice, not three.*\n")
    o.append(f"Pull: {src.name} \u00b7 {len(events)} clustered event{'s' if len(events)!=1 else ''} "
             f"({len(kin)} kinetic, {len(stm)} statement) \u00b7 "
             f"kinetic: **{len(by['A'])}A** {len(by['B'])}B {len(by['C'])}C {len(by['F'])} withheld \u00b7 "
             f"statements: **{len(sby['A'])}A** {len(sby['B'])}B \u00b7 "
             f"rendered {now.strftime('%d%H%MZ %b %y').upper()}\n")

    o.append("**\u2b1b GRADE A \u2014 CONFIRMED**\n")
    if by["A"]:
        for e in by["A"]:
            o.extend(event_block(e))
    else:
        o.append("No event reached three hostile sides this window. "
                 "The desk prints the null rather than promoting a Grade B.\n")

    o.append("**\u25fc GRADE B \u2014 CORROBORATED**\n")
    if by["B"]:
        for e in by["B"]:
            o.extend(event_block(e))
    else:
        o.append("None this window.\n")

    if by["C"]:
        o.append("**\u25a8 GRADE C \u2014 REPEATED WITHIN ONE SIDE \u2014 NOT CORROBORATED**\n")
        o.append("> These are the dangerous ones. Volume inside a single side reads "
                 "like confirmation and is not: allied outlets repeating each other "
                 "is still one voice. "
                 "Listed so the reader can see what the method rejected, not as reporting.\n")
        for e in by["C"]:
            zones = zone_label(e["zone"])
            camp = e["sides"][0] if e["sides"] else (e["camps"][0] if e["camps"] else "unattributed")
            o.append(f"- **{anchor_label(e['anchors'])}** \u00b7 {zones} \u2014 "
                     f"{e['n_msgs']} reports, all from *{camp}* \u00b7 "
                     f"{span_txt(e['span'])}")
        o.append("")

    o.append("**\u25fb WITHHELD \u2014 SINGLE-SOURCE (F)**\n")
    if by["F"]:
        zc = Counter(zone_label(e["zone"]) for e in by["F"])
        spread = ", ".join(f"{z} ({n})" for z, n in zc.most_common())
        o.append(f"{len(by['F'])} single-source claim{'s' if len(by['F']) != 1 else ''} "
                 f"across {len(zc)} zone{'s' if len(zc) != 1 else ''} \u2014 "
                 f"{spread}. Not reported. Logged and available on analyst query.\n")
    else:
        o.append("None this window.\n")

    o.append("**\u25c8 STATEMENT TRACK \u2014 CROSS-SIDE CONFIRMED CLAIMS**\n")
    o.append("*A statement confirmed across hostile sides means the claim circulated on "
             "both sides of the divide \u2014 it does not mean the claim is true. Kinetic "
             "cross-bias confirms an event happened; statement cross-bias confirms an "
             "utterance exists. The desk grades circulation, the reader judges content.*\n")
    if sby["A"] or sby["B"]:
        for e in sby["A"] + sby["B"]:
            o.extend(statement_block(e))
    else:
        o.append("No statement cleared two hostile sides this window.\n")
    if sby["C"]:
        o.append("*Single-side statement echo (not corroborated): " +
                 "; ".join(f"{anchor_label(e['anchors'])} \u00b7 {zone_label(e['zone'])} "
                           f"({e['n_msgs']} rpt, {(e['sides'] or ['?'])[0]})"
                           for e in sby["C"]) + ".*\n")
    if sby["F"]:
        o.append(f"*{len(sby['F'])} single-source statement claims logged, not reported.*\n")

    if divergences:
        o.append("**Grade divergence \u2014 recomputed vs. upstream**\n")
        for d in divergences:
            o.append(f"- {d}")
        o.append("")
        o.append("*The recomputed grade governs. Divergence is printed rather than "
                 "silently reconciled.*\n")

    return "\n".join(o).rstrip() + "\n"


def event_block(e: dict) -> list[str]:
    lines = [f"**{anchor_label(e['anchors'])} \u00b7 {zone_label(e['zone'])}**\n"]
    ch = f", {e['n_channels']} distinct channels" if e["n_channels"] else ""
    lines.append(f"- {e['n_msgs']} reports{ch} across **{len(e['sides'])} hostile sides** "
                 f"({', '.join(e['sides'])})")
    if e["balance"]:
        bal = " \u00b7 ".join(f"{k} {v}" for k, v in
                             sorted(e["balance"].items(), key=lambda kv: -kv[1]))
        lines.append(f"- Report balance: {bal}{balance_note(e['balance'])}")
    if e["camps"] and len(e["camps"]) != len(e["sides"]):
        lines.append(f"- Camp labels behind those sides: {', '.join(e['camps'])} "
                     f"\u2014 {len(e['camps'])} labels, {len(e['sides'])} sides. "
                     f"Labels do not grade.")
    if len(e["variants"]) > 1:
        lines.append(f"- Reported under {len(e['variants'])} spellings of the same place: "
                     f"{', '.join(v.title() for v in e['variants'])} \u2014 matched through "
                     f"the alias table. The sides do not use the same name for this ground.")
    if e["chans_side"]:
        cs = ", ".join(f"{k} {v}" for k, v in sorted(e["chans_side"].items()))
        note = ""
        if len(e["solo_sides"]) == len(e["chans_side"]) and len(e["chans_side"]) > 1:
            note = (" \u2014 **every side here is a single outlet**; this is corroboration "
                    "across bias, not across independent reporting")
        elif e["solo_sides"]:
            note = (f" \u2014 {', '.join(e['solo_sides'])} rest{'s' if len(e['solo_sides'])==1 else ''} "
                    f"on one outlet each")
        lines.append(f"- Channels per side: {cs}{note}")
    if e["digests"]:
        n = e["digests"]
        lines.append(f"- {n} of these report{'s is a roundup post' if n == 1 else 's are roundup posts'} "
                     f"naming four or more places \u2014 weaker evidence than a dedicated report.")
    if e["weapons"]:
        lines.append(f"- Weapons reported: {', '.join(e['weapons'])}")
    lines.append(f"- {cas_txt(e['casualties'])}")
    lines.append(f"- Window: {span_txt(e['span'])} \u00b7 first seen {fmt_ts(e['first'])}")
    lines.append("")
    return lines


def statement_block(e: dict) -> list[str]:
    g = e["grade"]
    lines = [f"**[{g}] \u201c{anchor_label(e['anchors'])}\u201d \u00b7 {zone_label(e['zone'])}"
             + (f" \u00b7 around: {', '.join(e['st_actors'])}" if e['st_actors'] else "") + "**\n"]
    lines.append(f"- {e['n_msgs']} reports across **{len(e['sides'])} hostile sides** "
                 f"({', '.join(e['sides'])})")
    if e["balance"]:
        bal = " \u00b7 ".join(f"{k} {v}" for k, v in sorted(e["balance"].items(), key=lambda kv: -kv[1]))
        lines.append(f"- Report balance: {bal}{balance_note(e['balance'])}")
    if e["chans_side"]:
        cs = ", ".join(f"{k} {v}" for k, v in sorted(e["chans_side"].items()))
        note = (" \u2014 **every side here is a single outlet**"
                if len(e["solo_sides"]) == len(e["chans_side"]) and len(e["chans_side"]) > 1 else "")
        lines.append(f"- Channels per side: {cs}{note}")
    lines.append(f"- Window: {span_txt(e['span'])} \u00b7 first seen {fmt_ts(e['first'])}")
    lines.append("")
    return lines


def balance_note(bal: dict) -> str:
    """A 17/1/1 split and a 5/5/5 split carry the same grade and very different
    evidence. Say which one this is."""
    v = sorted(bal.values(), reverse=True)
    if len(v) < 2 or sum(v) == 0:
        return ""
    if v[0] / sum(v) >= 0.75:
        return (" \u2014 **one side carries most of the volume**; the others corroborate "
                "but do not independently substantiate")
    return ""


def cas_txt(c: dict) -> str:
    if c.get("kind") == "none":
        return "Casualties: none stated in the corroborating reports."
    lo, hi = c.get("lo"), c.get("hi")
    rng = f"{lo}" if lo == hi else f"{lo}\u2013{hi}"
    if c.get("kind") == "attributed":
        return (f"Casualties **claimed**: {rng} across {c['n']} reports "
                f"({', '.join(c['camps'])}). Cross-bias agreement confirms the event, "
                f"not the count \u2014 the count is a claim.")
    return (f"Casualties **claimed**: {rng}, camp attribution unavailable from the "
            f"cluster file. Treat as a claim, not a figure.")


def span_txt(s) -> str:
    return f"{s:.1f}h" if isinstance(s, (int, float)) else "\u2014"


# ------------------------------------------------------------------------- tile

def build_tile(events: list[dict], src: Path) -> dict:
    now = datetime.now(timezone.utc)
    by = Counter(e["grade"] for e in events if e.get("track") != "statement")
    sby = Counter(e["grade"] for e in events if e.get("track") == "statement")
    tops = sorted([e for e in events if e["grade"] == "A" and e.get("track") != "statement"],
                  key=lambda e: (-len(e["sides"]), -e["n_msgs"]))
    top = tops[0] if tops else None
    return {
        "generated": now.isoformat(timespec="seconds"),
        "source_pull": src.name,
        "events_total": len(events),
        "grades": {"A": by["A"], "B": by["B"], "C": by["C"], "F": by["F"]},
        "statements": {"A": sby["A"], "B": sby["B"], "C": sby["C"], "F": sby["F"]},
        "confirmed": by["A"] + by["B"],
        "withheld": by["F"],
        "zones_covered": sorted({e["zone"] for e in events}),
        "top3": [{
            "grade": e["grade"], "track": e.get("track", "kinetic"),
            "anchor": anchor_label(e["anchors"]) if e.get("track") != "statement"
                      else "\u201c" + anchor_label(e["anchors"]) + "\u201d",
            "zone": zone_label(e["zone"]), "sides": len(e["sides"]),
            "reports": e["n_msgs"],
        } for e in sorted([e for e in events if e["grade"] in "AB"],
                          key=lambda e: (-len(e["sides"]), -e["n_msgs"]))[:3]],
        "top_confirmed": ({
            "anchor": anchor_label(top["anchors"]),
            "zone": zone_label(top["zone"]),
            "sides": len(top["sides"]),
            "side_names": top["sides"],
            "camp_labels": top["camps"],
            "report_balance": top["balance"],
            "reports": top["n_msgs"],
            "span_hours": round(top["span"], 1) if isinstance(top["span"], (int, float)) else None,
            "first_seen": top["first"].isoformat(timespec="seconds") if top["first"] else None,
        } if top else None),
        "method": "cross-bias corroboration; Grade A = 3+ hostile SIDES on a specific anchor",
        "schema": "war_desk/v3",
    }


# -------------------------------------------------------------------------- i/o

def latest_events_file() -> Path | None:
    cands = sorted(FORECASTS.glob("tg_events_*.json"))
    return cands[-1] if cands else None


def load_events(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        for k in ("events", "clusters", "results", "items"):
            if isinstance(data.get(k), list):
                return data[k]
        return []
    return data if isinstance(data, list) else []


def schema_report() -> str:
    rows = ["field slot".ljust(18) + "resolved from"]
    rows.append("-" * 52)
    for slot, c in _SCHEMA_HITS.items():
        hits = ", ".join(f"{k}\u00d7{v}" for k, v in c.most_common())
        rows.append(slot.ljust(18) + hits)
    return "\n".join(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description="NETZ WAR DESK — Module 3")
    ap.add_argument("--latest", action="store_true", help="use newest tg_events_*.json")
    ap.add_argument("--file", help="explicit events file")
    ap.add_argument("--dry-run", action="store_true", help="print, write nothing")
    ap.add_argument("--schema", action="store_true", help="field-resolution report, then exit")
    ap.add_argument("--no-tile", action="store_true", help="skip docs/war_desk.json")
    args = ap.parse_args()

    src = Path(args.file) if args.file else latest_events_file()
    if args.file and not src.is_absolute():
        src = HERE / src
    if not src or not src.exists():
        print("WARDESK · no events file found in forecasts/ — run tg_cluster.py first",
              file=sys.stderr)
        return 2

    raw = load_events(src)
    if not raw:
        print(f"WARDESK · {src.name} parsed but contained no events", file=sys.stderr)
        return 3

    events, divergences = [], []
    for r in raw:
        if not isinstance(r, dict):
            continue
        e = normalize(r)
        e["grade"] = recompute_grade(e)
        up = e["upstream_grade"]
        if up and up in "ABCF" and up != e["grade"]:
            divergences.append(
                f"**{anchor_label(e['anchors'])}** ({zone_label(e['zone'])}): "
                f"upstream **{up}**, recomputed **{e['grade']}** "
                f"({len(e['sides'])} side{'s' if len(e['sides']) != 1 else ''}, "
                f"{e['n_msgs']} reports)")
        events.append(e)

    if args.schema:
        print(f"WARDESK · schema resolution over {len(events)} events from {src.name}\n")
        print(schema_report())
        missing = [s for s, c in _SCHEMA_HITS.items() if c.get("<missing>") == len(events)]
        if missing:
            print("\nNEVER RESOLVED (upstream is not emitting these): " + ", ".join(missing))
        return 0

    section = render_section(events, src, divergences)
    tile = build_tile(events, src)

    if args.dry_run:
        print(section)
        print("--- docs/war_desk.json ---")
        print(json.dumps(tile, indent=2, ensure_ascii=False))
        return 0

    FORECASTS.mkdir(parents=True, exist_ok=True)
    stamp = re.sub(r"^tg_events_|\.json$", "", src.name)
    dated = FORECASTS / f"WARDESK_{stamp}.md"
    dated.write_text(section, encoding="utf-8")
    (FORECASTS / "WARDESK_latest.md").write_text(section, encoding="utf-8")
    print(f"WARDESK · section \u2192 {dated} (+ WARDESK_latest.md)", file=sys.stderr)

    if not args.no_tile:
        DOCS.mkdir(parents=True, exist_ok=True)
        (DOCS / "war_desk.json").write_text(
            json.dumps(tile, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"WARDESK · tile    \u2192 {DOCS / 'war_desk.json'}", file=sys.stderr)

    g = tile["grades"]
    print(f"WARDESK · {len(events)} events \u00b7 A:{g['A']} B:{g['B']} "
          f"C:{g['C']} withheld:{g['F']}"
          + (f" \u00b7 {len(divergences)} grade divergences printed" if divergences else ""),
          file=sys.stderr)
    print(dated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
