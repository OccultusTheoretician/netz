#!/usr/bin/env python3
"""
KKR — Kaos Kontrol Report: forecasting stage + predictive ledger for NETZ.

Reads the latest battle report, elicits falsifiable projections from a model,
and maintains a dated, misfire-inclusive ledger with Brier/calibration scoring.
The ledger is the point: a projection without a resolution criterion, deadline,
and permanent miss-record is astrology.

Usage:
    python kkr.py                    # generate from latest report → ledger
    python kkr.py --provider anthropic --model claude-sonnet-4-6
    python kkr.py --packet-only      # just write the paste-into-Claude packet
    python kkr.py --ingest file.json # ingest projections you got manually
    python kkr.py --resolve          # mark past-deadline projections hit/miss
    python kkr.py --score            # Brier + calibration table

Providers:
    lmstudio  (default) — local, no key, http://localhost:1234/v1
    anthropic — needs ANTHROPIC_API_KEY env var; model default claude-sonnet-4-6
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

from netz import render_html, llm_probe  # same directory

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"
OUT = HERE / "forecasts"
REPORTS = HERE / "reports"

PROJECTION_PROMPT = """You are a forecasting analyst. From the intelligence report below, generate 8-12 falsifiable projections spanning at least 4 domains (military/conflict, economics/markets, cyber, political, crime/security, disaster).

Every projection MUST:
1. Be a single observable claim a third party could verify from public reporting at the deadline. No vague language ("tensions will continue", "pressure will mount").
2. Carry "probability": an integer 5-95, never 0 or 100.
3. Carry "resolution": the exact criterion that settles it true or false.
4. Carry "deadline": an ISO date between {min_date} and {max_date}.
5. Carry "citations": a list of item numbers from the report's record that ground it.
6. Base-rate discipline: most discrete events do not happen; do not cluster probabilities at 60-80%. At least two projections must be rated BELOW 35%.

Return ONLY a JSON array — no markdown fences, no commentary before or after:
[{{"statement": "...", "domain": "...", "probability": 40, "resolution": "...", "deadline": "YYYY-MM-DD", "citations": [1, 4]}}]

REPORT:
{report}"""


# ----------------------------------------------------------------------
# providers
# ----------------------------------------------------------------------

def call_lmstudio(base_url: str, model: str | None, prompt: str) -> str | None:
    model = model or llm_probe(base_url)
    if not model:
        print("KKR · no model loaded at LM Studio endpoint", file=sys.stderr)
        return None
    try:
        r = requests.post(f"{base_url.rstrip('/')}/chat/completions", timeout=600,
                          json={"model": model, "temperature": 0.3, "max_tokens": 3000,
                                "messages": [{"role": "user", "content": prompt}]})
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as exc:
        print(f"KKR · LM Studio call failed: {exc}", file=sys.stderr)
        return None


def call_anthropic(model: str | None, prompt: str) -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("KKR · ANTHROPIC_API_KEY not set — export it or use --provider lmstudio",
              file=sys.stderr)
        return None
    try:
        r = requests.post("https://api.anthropic.com/v1/messages", timeout=300,
                          headers={"x-api-key": key,
                                   "anthropic-version": "2023-06-01",
                                   "content-type": "application/json"},
                          json={"model": model or "claude-sonnet-4-6",
                                "max_tokens": 3000,
                                "messages": [{"role": "user", "content": prompt}]})
        r.raise_for_status()
        return "".join(b.get("text", "") for b in r.json().get("content", []))
    except Exception as exc:
        print(f"KKR · Anthropic call failed: {exc}", file=sys.stderr)
        return None


# ----------------------------------------------------------------------
# parsing + ledger
# ----------------------------------------------------------------------

def parse_projections(raw: str) -> list:
    txt = re.sub(r"```(?:json)?", "", raw).strip()
    m = re.search(r"\[.*\]", txt, re.S)
    if not m:
        return []
    try:
        arr = json.loads(m.group(0))
    except json.JSONDecodeError:
        return []
    out = []
    for p in arr if isinstance(arr, list) else []:
        try:
            prob = max(5, min(95, int(p["probability"])))
            datetime.strptime(p["deadline"], "%Y-%m-%d")
            out.append({"statement": str(p["statement"]).strip(),
                        "domain": str(p.get("domain", "general")).strip().lower(),
                        "probability": prob,
                        "resolution": str(p["resolution"]).strip(),
                        "deadline": p["deadline"],
                        "citations": [int(c) for c in p.get("citations", [])]})
        except (KeyError, ValueError, TypeError):
            continue
    return out


# ----------------------------------------------------------------------
# validation gate (deterministic — runs before anything reaches the ledger)
# ----------------------------------------------------------------------

VAGUE_PHRASES = ["tensions will", "tension will", "pressure will", "will continue",
                 "continues to", "remain elevated", "remains elevated", "may or may not",
                 "situation will", "instability will", "uncertainty will", "will persist",
                 "is expected to evolve", "will likely evolve", "dynamics will"]


def validate_projection(p: dict, min_days: int = 3, max_days: int = 240) -> list:
    """Return list of rejection reasons; empty list = accepted."""
    reasons = []
    text = (p["statement"] + " " + p["resolution"]).lower()
    if len(p["resolution"]) < 25:
        reasons.append("resolution criterion too thin to adjudicate")
    for v in VAGUE_PHRASES:
        if v in text:
            reasons.append(f"non-falsifiable phrasing: '{v}'")
            break
    try:
        dl = datetime.strptime(p["deadline"], "%Y-%m-%d").date()
        today = datetime.now(timezone.utc).date()
        if dl < today + timedelta(days=min_days):
            reasons.append(f"deadline inside {min_days}-day floor")
        if dl > today + timedelta(days=max_days):
            reasons.append(f"deadline beyond {max_days}-day ceiling")
    except ValueError:
        reasons.append("unparseable deadline")
    if not p.get("citations"):
        reasons.append("no grounding citations to the report record")
    if re.search(r"within\s+(?:the\s+)?(?:next\s+)?\d+\s+(?:hours|days)", p["statement"], re.I):
        reasons.append("relative timeframe in statement — use absolute date windows; "
                       "the deadline field governs and relative phrasing creates "
                       "adjudication conflict")
    if re.search(r"clos(?:e|ing)|settle|trading day|market data", 
                 p["statement"] + " " + p["resolution"], re.I):
        try:
            if datetime.strptime(p["deadline"], "%Y-%m-%d").weekday() >= 5:
                reasons.append("market-price resolution with weekend deadline — no "
                               "settlement exists that day")
        except ValueError:
            pass
    if not (5 <= p["probability"] <= 95):
        reasons.append("probability outside 5-95")
    return reasons


def render_kkr(accepted: list, rejected: list, model_tag: str, source_report: str):
    """The Kaos Kontrol Report — this run's validated forecasts + audit trail."""
    now = datetime.now(timezone.utc)
    dtg = now.strftime("%d%H%MZ %b %y").upper()
    data = load_ledger()
    stats = brier_and_calibration(data["projections"])
    below35 = sum(1 for p in accepted if p["probability"] < 35)
    out = ["**UNCLASSIFIED // OPEN SOURCES**\n",
           f"# KAOS KONTROL REPORT — {dtg}\n",
           f"Window: this run · source: {source_report} · forecaster: {model_tag} · "
           f"{len(accepted)} accepted / {len(rejected)} rejected by validation gate · "
           f"{below35} rated below 35% (base-rate discipline)\n"]

    out.append("## I. VALIDATED PROJECTIONS\n")
    if accepted:
        out.append("| id | p | deadline | domain | statement | resolves on |")
        out.append("|---|---|---|---|---|---|")
        for p in accepted:
            out.append(f"| {p['id']} | {p['probability']}% | {p['deadline']} | "
                       f"{p['domain']} | {p['statement']} | {p['resolution']} |")
    else:
        out.append("None survived validation this run.")
    out.append("")

    out.append("## II. REJECTED BY THE GATE — AUDIT TRAIL\n")
    if rejected:
        for p, reasons in rejected:
            out.append(f"- \"{p.get('statement','?')[:140]}\" → REJECTED: "
                       f"{'; '.join(reasons)}")
    else:
        out.append("Nothing rejected — every projection cleared the gate.")
    out.append("")

    out.append("## III. LEDGER STANDING\n")
    open_n = sum(1 for p in data["projections"] if p["status"] == "open")
    overdue = [p for p in data["projections"] if p["status"] == "open" and
               datetime.strptime(p["deadline"], "%Y-%m-%d").date() < now.date()]
    if stats.get("n_resolved"):
        out.append(f"{len(data['projections'])} issued all-time · {open_n} open "
                   f"({len(overdue)} past deadline — run `python kkr.py --resolve`) · "
                   f"{stats['hits']} hits / {stats['misses']} misses · "
                   f"**Brier {stats['brier']:.3f}** (0 = oracle, 0.25 = coin-flip on 50s)")
    else:
        out.append(f"{len(data['projections'])} issued all-time · {open_n} open · "
                   f"nothing resolved yet — the ledger earns meaning at first resolution.")
    out.append("\nFull ledger: LEDGER.md / ledger.html\n")
    out.append("---\n**UNCLASSIFIED // OPEN SOURCES** · *the gate is mechanical; the ledger "
               "is permanent; the system gets scored, not the operator.*")

    md = "\n".join(out)
    stamp = now.strftime("%Y-%m-%d")
    OUT.mkdir(exist_ok=True)
    (OUT / f"KKR_{stamp}.md").write_text(md, encoding="utf-8")
    html_doc = render_html(md, f"KKR {stamp}")
    (OUT / f"KKR_{stamp}.html").write_text(html_doc, encoding="utf-8")
    (OUT / "KKR_latest.html").write_text(html_doc, encoding="utf-8")
    print(f"KKR · report → {OUT / ('KKR_' + stamp + '.md')} (+ KKR_latest.html)",
          file=sys.stderr)


def load_ledger() -> dict:
    if LEDGER.exists():
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    return {"projections": []}


def save_ledger(data: dict):
    LEDGER.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def append_projections(projs: list, model_tag: str, source_report: str) -> list:
    data = load_ledger()
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    existing_today = sum(1 for p in data["projections"] if p["id"].startswith(f"KKR-{today}"))
    added = []
    for i, p in enumerate(projs, existing_today + 1):
        p.update({"id": f"KKR-{today}-{i:02d}",
                  "date_issued": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                  "model": model_tag, "source_report": source_report,
                  "status": "open", "resolved_date": None, "notes": ""})
        data["projections"].append(p)
        added.append(p)
    save_ledger(data)
    return added


def latest_report() -> Path | None:
    if not REPORTS.exists():
        return None
    mds = sorted(REPORTS.glob("battle_report_*.md"))
    return mds[-1] if mds else None


# ----------------------------------------------------------------------
# scoring
# ----------------------------------------------------------------------

def brier_and_calibration(projs: list) -> dict:
    resolved = [p for p in projs if p["status"] in ("hit", "miss")]
    if not resolved:
        return {"n_resolved": 0}
    briers = []
    buckets = {}  # (lo,hi) -> [n, hits]
    for p in resolved:
        prob = p["probability"] / 100
        outcome = 1.0 if p["status"] == "hit" else 0.0
        briers.append((prob - outcome) ** 2)
        lo = (p["probability"] // 20) * 20
        b = buckets.setdefault((lo, min(lo + 20, 100)), [0, 0])
        b[0] += 1
        b[1] += outcome
    return {"n_resolved": len(resolved),
            "brier": sum(briers) / len(briers),
            "hits": sum(1 for p in resolved if p["status"] == "hit"),
            "misses": sum(1 for p in resolved if p["status"] == "miss"),
            "calibration": {f"{lo}-{hi}%": {"n": n, "realized": h / n}
                            for (lo, hi), (n, h) in sorted(buckets.items())}}


def render_ledger():
    data = load_ledger()
    projs = data["projections"]
    stats = brier_and_calibration(projs)
    now = datetime.now(timezone.utc)
    open_p = [p for p in projs if p["status"] == "open"]
    resolved = [p for p in projs if p["status"] in ("hit", "miss")]
    voided = [p for p in projs if p["status"] == "void"]
    overdue = [p for p in open_p
               if datetime.strptime(p["deadline"], "%Y-%m-%d").date() < now.date()]

    out = ["**UNCLASSIFIED // OPEN SOURCES**\n",
           f"# KKR PREDICTIVE LEDGER — {now.strftime('%d%H%MZ %b %y').upper()}\n"]
    if stats.get("n_resolved"):
        out.append(f"Window: all-time · {len(projs)} issued · {len(open_p)} open "
                   f"({len(overdue)} past deadline, unresolved) · "
                   f"{stats['hits']} hits / {stats['misses']} misses · "
                   f"**Brier {stats['brier']:.3f}** (0=oracle, 0.25=coin-flip on 50s)\n")
        out.append("| stated probability | n resolved | realized frequency |")
        out.append("|---|---|---|")
        for band, d in stats["calibration"].items():
            out.append(f"| {band} | {d['n']} | {d['realized']:.0%} |")
        out.append("")
    else:
        out.append(f"Window: all-time · {len(projs)} issued · {len(open_p)} open · "
                   f"nothing resolved yet — the ledger earns meaning at first resolution\n")

    if overdue:
        out.append("## PAST DEADLINE — RESOLVE THESE (`python kkr.py --resolve`)\n")
        for p in overdue:
            out.append(f"- **{p['id']}** ({p['probability']}%, due {p['deadline']}) "
                       f"{p['statement']} — *resolves on:* {p['resolution']}")
        out.append("")

    out.append("## OPEN PROJECTIONS\n")
    if open_p:
        out.append("| id | issued | deadline | p | domain | statement |")
        out.append("|---|---|---|---|---|---|")
        for p in sorted(open_p, key=lambda x: x["deadline"]):
            out.append(f"| {p['id']} | {p['date_issued']} | {p['deadline']} | "
                       f"{p['probability']}% | {p['domain']} | {p['statement']} |")
    else:
        out.append("None open.")
    out.append("")

    out.append("## RESOLVED — HITS AND MISSES, PERMANENTLY\n")
    if resolved:
        for p in sorted(resolved, key=lambda x: x["resolved_date"] or "", reverse=True):
            mark = "✓ HIT" if p["status"] == "hit" else "✗ MISS"
            out.append(f"- **{mark}** {p['id']} ({p['probability']}%, due {p['deadline']}, "
                       f"resolved {p['resolved_date']}): {p['statement']}"
                       + (f" — *{p['notes']}*" if p["notes"] else ""))
    else:
        out.append("None yet. Misses will be listed here and never removed.")
    if voided:
        out.append(f"\n*Voided (unresolvable as stated): "
                   f"{', '.join(p['id'] for p in voided)}*")
    out.append("\n---\n**UNCLASSIFIED // OPEN SOURCES** · *the ledger scores the system, "
               "not the operator; consistency is not correctness — resolution is.*")

    md = "\n".join(out)
    OUT.mkdir(exist_ok=True)
    (OUT / "LEDGER.md").write_text(md, encoding="utf-8")
    (OUT / "ledger.html").write_text(render_html(md, "KKR Ledger"), encoding="utf-8")
    print(f"KKR · ledger → {OUT / 'LEDGER.md'} + ledger.html", file=sys.stderr)


# ----------------------------------------------------------------------
# commands
# ----------------------------------------------------------------------

def cmd_generate(args):
    rep = latest_report()
    if not rep:
        print("KKR · no battle report found — run netz.py first", file=sys.stderr)
        sys.exit(1)
    report_text = rep.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc)
    prompt = PROJECTION_PROMPT.format(
        min_date=(now + timedelta(days=7)).strftime("%Y-%m-%d"),
        max_date=(now + timedelta(days=180)).strftime("%Y-%m-%d"),
        report=report_text[:60000])

    # the packet is always written — the manual Fable path costs nothing
    OUT.mkdir(exist_ok=True)
    packet = OUT / f"kkr_packet_{now.strftime('%Y-%m-%d')}.md"
    packet.write_text(prompt, encoding="utf-8")
    print(f"KKR · packet → {packet}", file=sys.stderr)
    if args.packet_only:
        return

    raw, tag = None, ""
    if args.provider in ("anthropic", "auto"):
        raw = call_anthropic(args.model, prompt)
        tag = f"anthropic/{args.model or 'claude-sonnet-4-6'}"
        if raw is None and args.provider == "auto":
            print("KKR · primary (anthropic) unavailable — failing over to LM Studio",
                  file=sys.stderr)
    if raw is None and args.provider in ("lmstudio", "auto"):
        raw = call_lmstudio(args.lmstudio_url, None if args.provider == "auto" else args.model,
                            prompt)
        tag = "lmstudio/auto" if args.provider == "auto" else f"lmstudio/{args.model or 'auto'}"
    if not raw:
        print("KKR · no model output — packet written, ledger unchanged", file=sys.stderr)
        return
    projs = parse_projections(raw)
    if not projs:
        print("KKR · model output unparseable — nothing ingested. Raw saved for audit.",
              file=sys.stderr)
        (OUT / "kkr_raw_last.txt").write_text(raw, encoding="utf-8")
        return
    accepted_raw, rejected = [], []
    for p in projs:
        reasons = validate_projection(p)
        (rejected.append((p, reasons)) if reasons else accepted_raw.append(p))
    added = append_projections(accepted_raw, tag, rep.name) if accepted_raw else []
    print(f"KKR · gate: {len(added)} accepted, {len(rejected)} rejected", file=sys.stderr)
    render_ledger()
    render_kkr(added, rejected, tag, rep.name)


def cmd_ingest(args):
    raw = Path(args.ingest).read_text(encoding="utf-8")
    projs = parse_projections(raw)
    if not projs:
        print("KKR · file unparseable — need the JSON array format", file=sys.stderr)
        sys.exit(1)
    accepted_raw, rejected = [], []
    for p in projs:
        reasons = validate_projection(p)
        (rejected.append((p, reasons)) if reasons else accepted_raw.append(p))
    rep = latest_report()
    src_name = rep.name if rep else "manual"
    added = append_projections(accepted_raw, "manual/fable", src_name) if accepted_raw else []
    print(f"KKR · gate: {len(added)} accepted, {len(rejected)} rejected from {args.ingest}",
          file=sys.stderr)
    render_ledger()
    render_kkr(added, rejected, "manual/fable", src_name)


def cmd_resolve(args):
    data = load_ledger()
    today = datetime.now(timezone.utc).date()
    due = [p for p in data["projections"] if p["status"] == "open" and
           (args.all or datetime.strptime(p["deadline"], "%Y-%m-%d").date() <= today)]
    if not due:
        print("KKR · nothing due for resolution", file=sys.stderr)
        render_ledger()
        return
    for p in due:
        print(f"\n{p['id']} · stated {p['probability']}% · deadline {p['deadline']}")
        print(f"  {p['statement']}")
        print(f"  resolves on: {p['resolution']}")
        ans = input("  [h]it / [m]iss / [v]oid / [s]kip > ").strip().lower()
        if ans in ("h", "m", "v"):
            p["status"] = {"h": "hit", "m": "miss", "v": "void"}[ans]
            p["resolved_date"] = today.strftime("%Y-%m-%d")
            note = input("  note (enter to skip) > ").strip()
            p["notes"] = note
    save_ledger(data)
    render_ledger()


def main():
    ap = argparse.ArgumentParser(description="KKR — Kaos Kontrol Report: forecasts + predictive ledger")
    ap.add_argument("--provider", choices=["lmstudio", "anthropic", "auto"], default="lmstudio")
    ap.add_argument("--model", default=None)
    ap.add_argument("--lmstudio-url", default="http://localhost:1234/v1")
    ap.add_argument("--packet-only", action="store_true")
    ap.add_argument("--ingest", metavar="FILE")
    ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--all", action="store_true", help="with --resolve: include not-yet-due")
    ap.add_argument("--score", action="store_true")
    args = ap.parse_args()

    if args.resolve:
        cmd_resolve(args)
    elif args.score:
        render_ledger()
        stats = brier_and_calibration(load_ledger()["projections"])
        print(json.dumps(stats, indent=2))
    elif args.ingest:
        cmd_ingest(args)
    else:
        cmd_generate(args)


if __name__ == "__main__":
    main()
