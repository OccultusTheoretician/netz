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

PROJECTION_PROMPT = """You are a forecasting analyst. Before writing ANY projection, run this discipline silently and do not output the working, only the final JSON:
GATE 1 SCOPE — for each candidate, name exactly what would be observed at the deadline. If you cannot name a concrete observable, discard it.
GATE 2 EVIDENCE — cite which numbered report items support it. No item support = discard.
GATE 3 ATTACK — argue the OPPOSITE outcome. Ask: what is the base rate for this class of event? Most discrete events do NOT happen. If your probability ignores the base rate, correct it DOWN.
GATE 4 VERIFY — check the resolution criterion is adjudicable by a third party from public reporting, and the deadline is an absolute weekday date inside the window. Fix or discard.
GATE 5 REPORT — only projections that survive all four gates go in the array.
Apply the gates, then: From the intelligence report below, generate 8-10 falsifiable projections (keep each resolution under 40 words so the full JSON array fits) spanning at least 4 domains (military/conflict, economics/markets, cyber, political, crime/security, disaster).

Every projection MUST:
1. Be a single observable claim a third party could verify from public reporting at the deadline. No vague language ("tensions will continue", "pressure will mount"). ABSOLUTE DATES ONLY: never write "within 72 hours" or "within the next N days" — write the explicit window ("between 2026-07-21 and 2026-07-24") in both statement and resolution, matching the deadline field.
2. Carry "probability": an integer 5-95, never 0 or 100.
3. Carry "resolution": the exact criterion that settles it true or false.
4. Carry "deadline": an ISO date between {min_date} and {max_date}. If the resolution depends on a market close or settlement, the deadline must be a weekday.
5. Carry "citations": a list of item numbers from the report's record that ground it.
6. Base-rate discipline: most discrete events do not happen; do not cluster probabilities at 60-80%. At least two projections must be rated BELOW 35%.

Use plain ASCII straight quotes only. Do NOT use curly quotes. Do NOT put quotation marks inside any statement or resolution string — refer to names and phrases without quoting them.
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
                          json={"model": model, "temperature": 0.3, "max_tokens": 6000,
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
                                "max_tokens": 6000,
                                "messages": [{"role": "user", "content": prompt}]})
        r.raise_for_status()
        return "".join(b.get("text", "") for b in r.json().get("content", []))
    except Exception as exc:
        print(f"KKR · Anthropic call failed: {exc}", file=sys.stderr)
        return None


# ----------------------------------------------------------------------
# parsing + ledger
# ----------------------------------------------------------------------

def _normalize_json_text(txt: str) -> str:
    """Repair the typographic drift local models introduce that breaks JSON:
    curly quotes, curly apostrophes, en/em dashes inside strings, stray BOM."""
    repl = {
        "\u201c": "'", "\u201d": "'",          # curly DOUBLE quotes -> single (inner phrase quoting)
        "\u2018": "'", "\u2019": "'",          # curly single quotes / apostrophe -> straight apostrophe
        "\u2032": "'", "\u2033": "'",          # primes -> apostrophe
        "\u2013": "-", "\u2014": "-",            # en/em dash -> hyphen
        "\ufeff": "", "\u00a0": " ",             # BOM, non-breaking space
    }
    for a, b in repl.items():
        txt = txt.replace(a, b)
    return txt


def parse_projections(raw: str) -> list:
    txt = re.sub(r"```(?:json)?", "", raw).strip()
    txt = _normalize_json_text(txt)
    m = re.search(r"\[.*\]", txt, re.S)
    if not m:
        return []
    blob = m.group(0)
    arr = None
    for attempt in (blob, re.sub(r"[\r\n\t]+", " ", blob)):
        try:
            arr = json.loads(attempt)
            break
        except json.JSONDecodeError:
            continue
    if arr is None:
        # SALVAGE a truncated array (model hit its token limit mid-object):
        # keep everything up to the last complete "}", then close the bracket.
        last = blob.rfind("}")
        if last != -1:
            salvaged = blob[:last + 1] + "]"
            try:
                arr = json.loads(salvaged)
                print(f"CASSALVAGE: recovered {len(arr)} projections from truncated output",
                      file=sys.stderr)
            except json.JSONDecodeError:
                return []
        else:
            return []
    out = []
    for p in arr if isinstance(arr, list) else []:
        try:
            prob = max(5, min(95, int(p["probability"])))
            datetime.strptime(p["deadline"], "%Y-%m-%d")
            entry = {"statement": str(p["statement"]).strip(),
                     "domain": str(p.get("domain", "general")).strip().lower(),
                     "probability": prob,
                     "resolution": str(p["resolution"]).strip(),
                     "deadline": p["deadline"],
                     "citations": [int(c) for c in p.get("citations", [])
                                   if str(c).strip().lstrip("-").isdigit()]}
            # RPAS 4.02g passthrough: a batch arriving with its seal
            # fields enters sealed; absent fields change nothing.
            for k in ("failure_condition", "keyed_keyless",
                      "keyed_keyless_rationale"):
                if str(p.get(k, "")).strip():
                    entry[k] = str(p[k]).strip()
            out.append(entry)
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


# A settlement verb alone does not mean a market. A comment period closes; a
# vulnerability is closed; a border closes. The weekend rule fires only when a
# settlement token and a market referent BOTH appear, each word-boundaried.
SETTLE_TOKENS = re.compile(
    r"\b(?:clos(?:e|es|ing)|settl(?:e|es|ed|ing|ement)|trading\s+day|"
    r"market\s+data|last\s+trade)\b", re.I)
MARKET_REFERENT = re.compile(
    r"\b(?:price|prices|index|indices|share|shares|stock|stocks|equity|equities|"
    r"yield|yields|future|futures|contract|contracts|ticker|spot|barrel|bushel|"
    r"basis\s+point|basis\s+points|bond|bonds|treasury|treasuries|exchange\s+rate|"
    r"S&P|Nasdaq|Dow|Brent|WTI|NYMEX|Comex|ICE|Nikkei|FTSE|DAX|"
    r"per\s+barrel|per\s+ounce|per\s+share)\b", re.I)

# A statement a third party cannot read on its own is not a forecast.
BARE_TOKENS = {"yes", "no", "true", "false", "maybe", "n/a", "tbd",
               "confirmed", "unconfirmed", "correct", "incorrect"}


def validate_projection(p: dict, min_days: int = 3, max_days: int = 800) -> list:
    """Return list of rejection reasons; empty list = accepted."""
    reasons = []
    text = (p["statement"] + " " + p["resolution"]).lower()
    stmt = (p.get("statement") or "").strip()
    if stmt.lower().strip(".!? ") in BARE_TOKENS:
        reasons.append(f"statement is the bare token '{stmt}' — a statement must "
                       "carry the claim itself, not an answer to an unstated question")
    elif len(stmt) < 40:
        reasons.append(f"statement too thin to adjudicate ({len(stmt)} chars) — a "
                       "third party reading the statement alone must be able to say "
                       "what was claimed")
    elif len(stmt.split()) < 6:
        reasons.append(f"statement is {len(stmt.split())} words — too compressed to "
                       "adjudicate without the surrounding context")
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
    # citations == [0] is the sentinel for operator/human calls (no report record) — allowed
    if re.search(r"within\s+(?:the\s+)?(?:next\s+)?\d+\s+(?:hours|days)", p["statement"], re.I):
        reasons.append("relative timeframe in statement — use absolute date windows; "
                       "the deadline field governs and relative phrasing creates "
                       "adjudication conflict")
    both = p["statement"] + " " + p["resolution"]
    if SETTLE_TOKENS.search(both) and MARKET_REFERENT.search(both):
        try:
            if datetime.strptime(p["deadline"], "%Y-%m-%d").weekday() >= 5:
                reasons.append("market-price resolution with weekend deadline — no "
                               "settlement exists that day")
        except ValueError:
            pass
    res = p.get("resolution", "")
    if re.search(r"\b[A-Z][\w.&-]{1,}\s+or\s+(?:the\s+)?[A-Z]", res):
        reasons.append("resolution names alternative venues joined by 'or' \u2014 "
                       "name ONE source of record or define the venue class; "
                       "an adjudicator must not choose the venue after the fact")
    _src_hint = re.search(r"\b(?:per|according to|as (?:published|posted|listed|"
                          r"reported|recorded)|official|website|page|feed|register|"
                          r"filing|bulletin|dataset|catalog|api)\b", res, re.I)
    _src_noun = re.search(r"\S\s+[A-Z][A-Za-z]{2,}", res)
    _src_dom = re.search(r"\b[\w-]+\.(?:gov|org|com|net|int|mil|eu)\b", res, re.I)
    if not (_src_hint or _src_noun or _src_dom):
        reasons.append("resolution names no source of record \u2014 a stranger "
                       "must know exactly where to look on the deadline date")
    if re.search(r"\b(?:price|yield|rate|index|level|magnitude|count|total|"
                 r"threshold|close[sd]?|above|below|exceed)\b", both, re.I) \
            and not re.search(r"(?:above|below|exceed\w*|at least|at or|over|"
                              r"under|reach\w*|close[sd]?|threshold|magnitude|"
                              r"least)\D{0,12}[\$\u20ac]?\d", both, re.I):
        reasons.append("measurable claim without a numeric threshold \u2014 "
                       "a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count")
    if re.search(r"^\s*if\b|\bonly if\b|\bprovided that\b|\bin the event\b",
                 p["statement"], re.I) and "void" not in res.lower():
        reasons.append("conditional trigger without a void clause \u2014 "
                       "pre-register what happens when the antecedent fails")
    if not (5 <= p["probability"] <= 95):
        reasons.append("probability outside 5-95")
    return reasons


def render_kkr(accepted: list, rejected: list, model_tag: str, source_report: str):
    """The Kaos Kontrol Report — this run's validated forecasts + audit trail."""
    now = datetime.now(timezone.utc)
    dtg = now.strftime("%d%H%MZ %b %y").upper()
    data = load_ledger()
    below35 = sum(1 for p in accepted if p["probability"] < 35)
    out = ["**NOTHING CLASSIFIED OR PRIVILEGED**\n",
           f"# KAOS KONTROL REPORT — {dtg}\n",
           "**KKR is the Kaos Kontrol Report** \u2014 the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.\n",
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
    arms = arm_stats(data["projections"])
    plural = "s" if len(arms) != 1 else ""
    out.append(f"{len(data['projections'])} issued all-time across {len(arms)} "
               f"forecaster arm{plural} · {open_n} open "
               f"({len(overdue)} past deadline — run "
               f"`python kkr.py --resolve`). "
               f"**No pooled score is published** — a Brier score belongs to one "
               f"forecaster; an average across arms is nobody's record.\n")
    mine = arms.get(model_tag, {"issued": 0, "open": 0, "n_resolved": 0})
    if mine["n_resolved"]:
        skill = "—" if mine["skill"] is None else f"{mine['skill']:+.3f}"
        noise = " · under 30 resolved, this is noise" if mine["n_resolved"] < 30 else ""
        out.append(f"**This arm — `{model_tag}`:** {mine['issued']} issued · "
                   f"{mine['open']} open · {mine['n_resolved']} resolved · "
                   f"{mine['hits']} hits / {mine['misses']} misses · "
                   f"**Brier {mine['brier']:.3f}** against its own base rate "
                   f"{mine['base_rate']:.1%} (climatological {mine['clim']:.3f}) · "
                   f"**skill {skill}**{noise}.\n")
    else:
        out.append(f"**This arm — `{model_tag}`:** {mine['issued']} issued · "
                   f"{mine['open']} open · nothing resolved yet — this arm earns a "
                   f"score at its first resolution.\n")
    _void_n = sum(1 for _p in data["projections"] if _p.get("status") == "void")
    if _void_n:
        out.append(f"*{_void_n} projection(s) voided — terminated as unadjudicable, "
                   f"never edited; each is itemised with its reason in "
                   f"[the ledger](ledger.html).*\n")
    out.append("**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.\n")
    out.extend(_arm_table(arms))
    out.append("")
    out.append("\nFull ledger: ledger.html\n")
    out.append("---\n**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger "
               "is permanent; the system gets scored, not the operator.*")

    md = "\n".join(out)
    stamp = now.strftime("%Y-%m-%d")
    OUT.mkdir(exist_ok=True)
    (OUT / f"KKR_{stamp}.md").write_text(md, encoding="utf-8")
    html_doc = render_html(md, f"KKR {stamp}")
    (OUT / f"KKR_{stamp}.html").write_text(html_doc, encoding="utf-8")
    (OUT / "KKR_latest.html").write_text(html_doc, encoding="utf-8")
    publish_served()
    print(f"KKR · report → {OUT / ('KKR_' + stamp + '.md')} (+ KKR_latest.html)",
          file=sys.stderr)


def load_ledger() -> dict:
    if LEDGER.exists():
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    return {"projections": []}


LEDGER_SCHEMA = "kkr-ledger/1.1"
DOCS = HERE / "docs"

# RPAS 4.02g, wired at the choke point (rev of 2026-07-29). Every ledger write
# flows through save_ledger; entries issued from the cutover are sealed at first
# save — which for a new entry is seal-at-issue. Entries issued earlier stay
# bare per the finding printed on the ledger's face: no retro-binding (RPAS 4.01).
# One seal implementation exists (candidate_desk.seal); importing it is what
# keeps the desk's and a stranger's recomputation byte-identical.
from candidate_desk import seal as rpas_seal
RPAS_SEAL_CUTOVER = "2026-07-30"


# The dated finding, printed on the ledger's own face per RPAS 6.04 — the desk
# is bound by its standards in public, with the same ceremony as any finding it
# publishes about others. Emitted by every save so it cannot rot out of a copy.
RPAS_DISCLOSURE = (
    "FINDING 2026-07-29 (RPAS 4.02f, 4.02g, 4.03, 6.04). The 161 entries issued "
    "through 2026-07-29 carry no per-entry seal hash: their statements, "
    "probabilities, and deadlines are supported by this repository's public "
    "commit history (RPAS 4.04) and the external beacon (4.05), not by "
    "per-entry commitment. All 15 resolved entries lack a keyed/keyless "
    "determination made before resolution; by RPAS 4.03 their hits are KEYED "
    "by rule and bear on no faculty claim — the published Brier stands as "
    "arm-calibration arithmetic only, which is the only claim the arm ever "
    "made. Entries issued from 2026-07-30 are sealed at first save under the "
    "4.02g construction: SHA-256 over the sorted-JSON of the eight "
    "pre-registered fields (statement, resolution, deadline, probability, "
    "failure_condition, keyed_keyless, keyed_keyless_rationale, date_issued). "
    "Separately, ALL 161 entries issued through 2026-07-29 carry no "
    "substantive failure condition (RPAS 4.02e, 4.03): 94 hold no value and "
    "67 hold a migration placeholder. CORRECTION 2026-07-30: this finding "
    "previously stated 94, counting placeholder text as substance — the same "
    "defect class it reports; corrected in the open. None has resolved. Failure "
    "conditions and keyed/keyless determinations may still be added to open "
    "entries before their resolution (4.02f); an entry resolving without them "
    "is KEYED by rule and its miss stands. Entries issued from 2026-07-30 are "
    "refused a seal while the failure condition is absent (4.03). Nothing "
    "sealed or published is altered by this finding; it is printed, not "
    "repaired.")

RPAS_ANCHOR = {
    "mechanism": "public version-control history",
    "description": "This ledger is published in a public git repository. Every "
                   "write is a commit with an independent timestamp that the "
                   "desk cannot rewrite without the rewrite being visible to "
                   "anyone holding an earlier clone (RPAS 4.04); the commitment "
                   "hash is additionally beaconed to a channel the desk does "
                   "not control (RPAS 4.05).",
    "repository": "https://github.com/OccultusTheoretician/netz",
    "path": "docs/ledger.json",
    "history": "https://github.com/OccultusTheoretician/netz/commits/main/docs/ledger.json",
    "verify": "python rpas_verify.py https://raw.githubusercontent.com/"
              "OccultusTheoretician/netz/main/docs/ledger.json recomputes every "
              "seal and every figure; --previous asserts append-only across any "
              "two snapshots."}


def save_ledger(data: dict):
    """Write the ledger with a self-describing envelope.

    A copy of ledger.json that cannot state what produced it or when it was
    written is a file, not evidence. `projections` is unchanged and is what
    every reader keys off, so the envelope is additive.
    """
    out = {"schema": LEDGER_SCHEMA,
           "generator": "kkr.py",
           "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "disclosure": RPAS_DISCLOSURE,
           "anchor": RPAS_ANCHOR,
           "projections": data["projections"]}
    for e in out["projections"]:                      # RPAS 4.02g at the choke point
        if not e.get("seal_sha256") and str(e.get("date_issued", "")) >= RPAS_SEAL_CUTOVER:
            if not str(e.get("failure_condition", "")).strip():
                print(f"KKR · UNSEALED · {e.get('id','?')} lacks a failure condition "
                      f"— refusing the seal (RPAS 4.03); rpas_verify will flag it "
                      f"until the entry is falsifiable", file=sys.stderr)
                continue
            rpas_seal(e)
    for k, v in data.items():
        if k not in out:
            out[k] = v
    LEDGER.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")


def publish_served():
    """Copy the canonical artifacts into the directory Pages actually serves.

    Every time the served copy was left as a manual step it drifted. Making it a
    build product of the render is the only version that cannot rot.
    """
    if not DOCS.exists():
        return
    src_html = OUT / "ledger.html"
    if src_html.exists():
        (DOCS / "ledger.html").write_text(src_html.read_text(encoding="utf-8"),
                                          encoding="utf-8")
    if LEDGER.exists():
        (DOCS / "ledger.json").write_text(LEDGER.read_text(encoding="utf-8"),
                                          encoding="utf-8")
    # the report face is the third mirror that drifted; it is a build product too
    src_kkr = OUT / "KKR_latest.html"
    if src_kkr.exists():
        (DOCS / "kkr.html").write_text(src_kkr.read_text(encoding="utf-8"),
                                       encoding="utf-8")
    print(f"KKR · served copies synced -> {DOCS}", file=sys.stderr)


def append_projections(projs: list, model_tag: str, source_report: str) -> list:
    data = load_ledger()
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    existing_today = sum(1 for p in data["projections"] if p["id"].startswith(f"KKR-{today}"))
    added = []
    for i, p in enumerate(projs, existing_today + 1):
        p.update({"id": f"KKR-{today}-{i:02d}",
                  "date_issued": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                  "model": model_tag, "source_report": source_report, "source_packet": str(globals().get("_LAST_PACKET", "")),
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


def arm_stats(projs: list) -> dict:
    """Per-forecaster-arm record.

    A Brier score is a property of ONE forecaster. Averaging across arms produces
    a number that describes nobody and flatters or damns whichever arm has fewer
    resolved rows. Nothing in this file may publish a pooled score.
    """
    arms = {}
    for p in projs:
        arms.setdefault(p.get("model") or "unattributed", []).append(p)
    out = {}
    for tag, rows in sorted(arms.items()):
        s = brier_and_calibration(rows)
        rec = {"issued": len(rows),
               "open": sum(1 for p in rows if p["status"] == "open"),
               "void": sum(1 for p in rows if p["status"] == "void"),
               "n_resolved": s.get("n_resolved", 0)}
        if rec["n_resolved"]:
            base = s["hits"] / s["n_resolved"]      # realized base rate
            clim = base * (1 - base)                # climatological Brier
            rec.update({"hits": s["hits"], "misses": s["misses"],
                        "brier": s["brier"], "base_rate": base, "clim": clim,
                        "skill": (1 - s["brier"] / clim) if clim else None,
                        "calibration": s["calibration"]})
        out[tag] = rec
    return out


def _arm_table(arms: dict) -> list:
    """Per-arm standing table. Never emits a pooled row."""
    rows = ["| forecaster arm | issued | open | resolved | hits | misses | Brier | "
            "base rate | climatological | skill |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for tag, r in arms.items():
        if not r["n_resolved"]:
            rows.append(f"| {tag} | {r['issued']} | {r['open']} | 0 | — | — | "
                        f"not computed | — | — | — |")
            continue
        skill = "—" if r["skill"] is None else f"{r['skill']:+.3f}"
        rows.append(f"| {tag} | {r['issued']} | {r['open']} | {r['n_resolved']} | "
                    f"{r['hits']} | {r['misses']} | {r['brier']:.3f} | "
                    f"{r['base_rate']:.1%} | {r['clim']:.3f} | {skill} |")
    return rows


def render_ledger():
    data = load_ledger()
    projs = data["projections"]
    now = datetime.now(timezone.utc)
    open_p = [p for p in projs if p["status"] == "open"]
    resolved = [p for p in projs if p["status"] in ("hit", "miss")]
    voided = [p for p in projs if p["status"] == "void"]
    overdue = [p for p in open_p
               if datetime.strptime(p["deadline"], "%Y-%m-%d").date() < now.date()]

    out = ["**NOTHING CLASSIFIED OR PRIVILEGED**\n",
           f"# KAOS KONTROL REPORT — PREDICTIVE LEDGER — {now.strftime('%d%H%MZ %b %y').upper()}\n",
           "**KKR is the Kaos Kontrol Report** \u2014 the daily forecasting stage that issues these projections. This is its permanent record: every projection ever sealed, resolved or open, hits and misses alike, segregated by the forecaster arm that issued it.\n",
           "**A standing Retro-Prescient Audit™** · method: "
           "[RETRO_PRESCIENT_AUDIT.md](https://github.com/OccultusTheoretician/netz/blob/main/RETRO_PRESCIENT_AUDIT.md)\n"]
    arms = arm_stats(projs)
    plural = "s" if len(arms) != 1 else ""
    out.append(f"Window: all-time · {len(projs)} issued across {len(arms)} forecaster "
               f"arm{plural} · {len(open_p)} open "
               f"({len(overdue)} past deadline, unresolved)\n")
    out.append("**No pooled score is published.** A Brier score is a property of one "
               "forecaster; an average across arms is nobody's record. Every figure "
               "below is segregated by the arm that issued the projection. Skill is "
               "measured against that arm's OWN realized base rate — the strategy of "
               "stating the base rate every single time. Negative skill means the arm "
               "is losing to that strategy.\n")
    out.append("## STANDING BY FORECASTER ARM\n")
    out.extend(_arm_table(arms))
    out.append("")
    # --- arm independence disclosure (patch_pub_title) -----------------------
    # LIAS-26 requires instrument attribution. A reader comparing arms needs to
    # know that the elicited arms are not blind: they are given this desk's own
    # corpus and standing instructions, so their independence is procedural —
    # a separate instrument answering the same questions — not informational.
    if any(t.startswith("manual/") for t in arms):
        out.append(
            "\n> **Disclosure — what the elicited arms are.** Arms tagged `manual/*` "
            "are frontier language models elicited by the operator against the same "
            "packet the machine arm receives. They are **not informationally "
            "independent of this desk**: the model is given the desk's own corpus and "
            "standing instructions as context. Their independence is procedural — a "
            "separate instrument answering the same questions — not informational. "
            "Rows are segregated by model, and no pooled score is published, because "
            "a Brier belongs to one forecaster.\n")

    scored = [(t, r) for t, r in arms.items() if r["n_resolved"]]
    thin = [t for t, r in scored if r["n_resolved"] < 30]
    if thin:
        out.append("*Under 30 resolved a Brier score is noise, not a record: "
                   + ", ".join("`" + t + "`" for t in thin) + ".*\n")
    if scored:
        for tag, r in scored:
            out.append(f"**CALIBRATION — {tag}** ({r['n_resolved']} resolved)\n")
            out.append("| stated probability | n resolved | realized frequency |")
            out.append("|---|---|---|")
            for band, d in r["calibration"].items():
                out.append(f"| {band} | {d['n']} | {d['realized']:.0%} |")
            out.append("")
    else:
        out.append("Nothing resolved yet — the ledger earns meaning at first resolution.\n")

    if overdue:
        out.append("## PAST DEADLINE — RESOLVE THESE (`python kkr.py --resolve`)\n")
        out.append(
            "A projection appears here when its window has closed and it has "
            "not yet been adjudicated. That is not the same as neglect. Most "
            "criteria on this book ask whether an event *occurred* inside the "
            "window, not whether it was *reported* inside it — so an event "
            "confirmed on the 30th can satisfy a criterion that closed on the "
            "28th, and resolving before the sources land would be guessing. "
            "Collation takes the time it takes, and the queue is printed rather "
            "than hidden while it does.\n")
        out.append(
            "The bound that keeps this from becoming a parking space: a row "
            "sitting here more than **fourteen days** past its deadline is a "
            "defect in this desk, not in the world. The count is published on "
            "this page so that it is visible when it happens.\n")
        for p in overdue:
            out.append(f"- **{p['id']}** ({p['probability']}%, due {p['deadline']}) "
                       f"{p['statement']} — *resolves on:* {p['resolution']}")
        out.append("")

    out.append("## OPEN PROJECTIONS\n")
    if open_p:
        out.append("| id | arm | issued | deadline | p | domain | statement |")
        out.append("|---|---|---|---|---|---|---|")
        for p in sorted(open_p, key=lambda x: x["deadline"]):
            out.append(f"| {p['id']} | `{p.get('model') or 'unattributed'}` | "
                       f"{p['date_issued']} | {p['deadline']} | "
                       f"{p['probability']}% | {p.get('domain','\u2014')} | {p['statement']} |")
    else:
        out.append("None open.")
    out.append("")

    out.append("## RESOLVED — HITS AND MISSES, PERMANENTLY\n")
    if resolved:
        for p in sorted(resolved, key=lambda x: x["resolved_date"] or "", reverse=True):
            mark = "✓ HIT" if p["status"] == "hit" else "✗ MISS"
            out.append(f"- **{mark}** {p['id']} [`{p.get('model') or 'unattributed'}`] "
                       f"({p['probability']}%, due {p['deadline']}, "
                       f"resolved {p['resolved_date']}): {p['statement']}"
                       + (f" — *{p['notes']}*" if p["notes"] else ""))
    else:
        out.append("None yet. Misses will be listed here and never removed.")
    out.append("\n## VOIDED — TERMINATED, NOT CORRECTED\n")
    if voided:
        out.append("A sealed projection is never edited. Where one cannot be "
                   "adjudicated as written, the only legitimate disposition is to "
                   "terminate it and print why. The statement below is reproduced "
                   "exactly as sealed, defect included. A void removes a position "
                   "from scoring, which favours the forecaster — so every one is "
                   "itemised here with its reason rather than listed as an id.\n")
        out.append(f"*{len(voided)} of {len(projs)} issued "
                   f"({len(voided) / len(projs):.1%}) have been voided.*\n")
        for p in sorted(voided, key=lambda x: x["id"]):
            out.append(f"- **{p['id']}** [`{p.get('model') or 'unattributed'}`] "
                       f"({p['probability']}%, due {p['deadline']}"
                       + (f", voided {p['resolved_date']}" if p.get("resolved_date") else "")
                       + f") — statement as sealed: \u201c{p['statement']}\u201d"
                       + (f"\n    - *Reason:* {p['notes']}" if p.get("notes")
                          else "\n    - *Reason: NOT RECORDED — this void predates the "
                               "printed-reason rule and is itself a conformance defect.*"))
    else:
        out.append("None. No projection has been terminated.")
    out.append("\n---\n**NOTHING CLASSIFIED OR PRIVILEGED** · *the ledger scores the system, "
               "not the operator; consistency is not correctness — resolution is.*")

    md = "\n".join(out)
    OUT.mkdir(exist_ok=True)
    (OUT / "LEDGER.md").write_text(md, encoding="utf-8")
    (OUT / "ledger.html").write_text(render_html(md, "KKR Ledger"), encoding="utf-8")
    publish_served()
    print(f"KKR · ledger → {OUT / 'LEDGER.md'} + ledger.html", file=sys.stderr)


# ----------------------------------------------------------------------
# commands
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Rueckkopplungsverbot: no output of a forecasting run may appear in the
# input to a subsequent run. The battle report carries model-authored prose
# in Key Judgments, Indications & Warnings, and each category Synthesis
# block. All three are stripped before the report becomes the prompt, so a
# figure the model states cannot have been inherited from its own prior
# assessment. Headers are kept so structure and numbering survive.
# ----------------------------------------------------------------------
_PROSE_SECTIONS = ("KEY JUDGMENTS", "INDICATIONS & WARNINGS")
_WITHHELD = "*(prior-run analytic prose withheld from model input - record only)*"


def _record_only(text):
    out, skip_section, skip_synth = [], False, False
    for line in text.split("\n"):
        if line.startswith("## "):
            head = line[3:].upper()
            skip_section = any(s in head for s in _PROSE_SECTIONS)
            skip_synth = False
            out.append(line)
            if skip_section:
                out.append("")
                out.append(_WITHHELD)
            continue
        if skip_section:
            continue
        if line.startswith("**Synthesis**"):
            skip_synth = True
            out.append(_WITHHELD)
            continue
        if skip_synth:
            if line.startswith("**The record:**"):
                skip_synth = False
                out.append(line)
            continue
        out.append(line)
    return "\n".join(out)


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
        report=_record_only(report_text)[:60000])

    # the packet is always written — the manual Fable path costs nothing
    OUT.mkdir(exist_ok=True)
    packet = OUT / f"kkr_packet_{now.strftime('%Y-%m-%d_%H%M')}.md"
    _latest_packet = OUT / "kkr_packet_latest.md"
    globals()["_LAST_PACKET"] = packet.name
    packet.write_text(prompt, encoding="utf-8")
    _latest_packet.write_text(prompt, encoding="utf-8")
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
    (OUT / "kkr_raw_last.txt").write_text(raw, encoding="utf-8")  # audit copy, unconditional
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
    # Which packet was this arm forecasting against? cmd_generate records it;
    # this path never did, so every manual/fable row carried a blank
    # source_packet. An explicit --packet wins. Otherwise the newest packet on
    # disk is assumed AND PRINTED — a wrong assumption should be visible.
    pk = getattr(args, "packet", None)
    if not pk:
        packets = sorted(OUT.glob("kkr_packet_2*.md"))
        pk = packets[-1].name if packets else ""
        if pk:
            print(f"KKR · source_packet assumed: {pk} "
                  f"(newest on disk; pass --packet to override)", file=sys.stderr)
    globals()["_LAST_PACKET"] = pk
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
    # DEFECT D — the ingest path hardcoded one arm tag. Any second manual lane
    # (operator, a different frontier model, the ORBAT bridge) would have been
    # silently written into the ledger as manual/fable. Same attribution class as
    # the pooled Brier, one level down.
    arm = getattr(args, "arm", None) or "manual/fable"
    added = append_projections(accepted_raw, arm, src_name) if accepted_raw else []
    print(f"KKR · gate: {len(added)} accepted, {len(rejected)} rejected from "
          f"{args.ingest} [arm: {arm}]", file=sys.stderr)
    render_ledger()
    render_kkr(added, rejected, arm, src_name)


def cmd_resolve(args):
    data = load_ledger()
    today = datetime.now(timezone.utc).date()
    due = [p for p in data["projections"] if p["status"] == "open" and
           (args.all or datetime.strptime(p["deadline"], "%Y-%m-%d").date() < today)]
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



def cmd_mine(args):
    """Enter YOUR OWN forecasts. Same gate, same ledger, tagged operator/human —
    so your calls are scored on the identical Brier scale as every model lane."""
    print("YOUR FORECAST — one at a time. Blank statement to finish.\n"
          "The same gate applies: falsifiable, absolute-date window, "
          "probability 5-95, real resolution criterion.\n", file=sys.stderr)
    entered = []
    while True:
        stmt = input("statement (blank = done) > ").strip()
        if not stmt:
            break
        try:
            prob = int(input("  probability 5-95 > ").strip())
        except ValueError:
            print("  not a number — skipped", file=sys.stderr); continue
        resolution = input("  resolves TRUE when (exact criterion) > ").strip()
        print("  horizon: [s]hort (<30d)  [m]id (1-6mo)  [l]ong (6-24mo)", file=sys.stderr)
        hz = input("  horizon s/m/l (or blank) > ").strip().lower()
        horizon = {"s": "short", "m": "mid", "l": "long"}.get(hz, "unspecified")
        _sugg = {"short": 21, "mid": 120, "long": 400}.get(horizon)
        _hint = ""
        if _sugg:
            from datetime import datetime as _dt, timedelta as _td, timezone as _tz
            _d = (_dt.now(_tz.utc) + _td(days=_sugg)).strftime("%Y-%m-%d")
            _hint = f" (suggest ~{_d} for {horizon})"
        deadline = input(f"  deadline YYYY-MM-DD{_hint} > ").strip()
        domain = input("  domain (military/economics/cyber/political/disaster/crime) > ").strip() or "general"
        rationale = input("  your reasoning (optional, stored not scored) > ").strip()
        p = {"statement": stmt, "probability": prob, "resolution": resolution,
             "deadline": deadline, "domain": domain.lower(), "citations": [0],
             "rationale": rationale, "horizon": horizon}
        reasons = validate_projection(p)
        if reasons:
            print("  GATE REJECTED: " + "; ".join(reasons)
                  + "\n  (fix and re-enter, or press on)", file=sys.stderr)
            continue
        entered.append(p)
        print(f"  accepted ({len(entered)} so far)", file=sys.stderr)
    if not entered:
        print("KKR · nothing entered", file=sys.stderr)
        return
    rep = latest_report()
    added = append_projections(entered, "operator/human", rep.name if rep else "operator")
    print(f"KKR · {len(added)} of your forecasts on the ledger, tagged operator/human",
          file=sys.stderr)
    render_ledger()



AUDIT_PROMPT_HEADER = """# KKR RESOLUTION AUDIT PACKET
Generated {stamp} · {n} projections past deadline, awaiting adjudication.

## YOUR TASK (independent auditor)

For EACH projection below, search public reporting and determine whether its
resolution criterion was met. You are auditing forecasts you did not make.

RULES:
1. Work the RESOLUTION CRITERION as written, not the statement's spirit. If the
   criterion demands two independent sources, one is not enough.
2. Search for DISCONFIRMING evidence as hard as confirming evidence. Note both.
3. If the evidence is genuinely ambiguous or you cannot verify, say so — do NOT
   guess. AMBIGUOUS is a valid verdict and is the correct one when the record is
   unclear.
4. Cite what you found: outlet, date, and what it said. Never assert without a source.
5. You do not know who made these forecasts or at what probability. Do not speculate.

Return ONLY a JSON array, no commentary, no markdown fences. Use plain ASCII
straight quotes and do not put quotation marks inside any string value:

[{{"id": "KKR-YYYYMMDD-NN", "verdict": "HIT" | "MISS" | "AMBIGUOUS",
  "confidence": "high" | "moderate" | "low",
  "evidence": "what you found, with outlet and date, 1-3 sentences",
  "disconfirming": "contrary evidence found, or: none found",
  "note": "one line an adjudicator should know before ruling"}}]

## PROJECTIONS AWAITING AUDIT

"""


def cmd_audit_export(args):
    """Export past-deadline projections as a provider-agnostic audit packet.
    Any auditor (Claude, local Qwen, third-party) can work it; the verdict file
    comes back through --audit-ingest. Probabilities and lane tags are WITHHELD
    so the auditor cannot be anchored by them."""
    data = load_ledger()
    today = datetime.now(timezone.utc).date()
    due = [p for p in data["projections"] if p["status"] == "open" and
           (args.all or datetime.strptime(p["deadline"], "%Y-%m-%d").date() < today)]
    if not due:
        print("KKR · nothing past deadline to audit", file=sys.stderr)
        return
    due.sort(key=lambda p: p["deadline"])
    now = datetime.now(timezone.utc)
    body = AUDIT_PROMPT_HEADER.format(
        stamp=now.strftime("%d%H%MZ %b %y").upper(), n=len(due))
    for p in due:
        body += (f"\n### {p['id']}\n"
                 f"- **Issued:** {p['date_issued']}  ·  **Deadline:** {p['deadline']}\n"
                 f"- **Domain:** {p.get('domain','general')}\n"
                 f"- **Claim:** {p['statement']}\n"
                 f"- **Resolution criterion:** {p['resolution']}\n")
    OUT.mkdir(exist_ok=True)
    path = OUT / f"audit_packet_{now.strftime('%Y-%m-%d')}.md"
    path.write_text(body, encoding="utf-8")
    print(f"KKR · audit packet ({len(due)} projections) → {path}", file=sys.stderr)
    print("KKR · give it to any auditor; save their JSON as audit_verdicts.json",
          file=sys.stderr)


def cmd_audit_ingest(args):
    """Read an auditor's verdict JSON and present each for YOUR ruling.
    The auditor recommends; you decide. Nothing is written without your key."""
    raw = Path(args.audit_ingest).read_text(encoding="utf-8")
    txt = _normalize_json_text(re.sub(r"```(?:json)?", "", raw).strip())
    m = re.search(r"\[.*\]", txt, re.S)
    if not m:
        print("KKR · no JSON array found in the verdict file", file=sys.stderr)
        sys.exit(1)
    try:
        verdicts = json.loads(m.group(0))
    except json.JSONDecodeError:
        last = m.group(0).rfind("}")
        verdicts = json.loads(m.group(0)[:last + 1] + "]") if last != -1 else []
    if not verdicts:
        print("KKR · verdict file did not parse", file=sys.stderr)
        sys.exit(1)

    vmap = {v.get("id"): v for v in verdicts if v.get("id")}
    data = load_ledger()
    today = datetime.now(timezone.utc).date()
    ruled = 0
    print(f"\nAUDITOR RETURNED {len(vmap)} VERDICTS. You rule on each.\n"
          f"[a]ccept the auditor's verdict · [h]it · [m]iss · [v]oid · [s]kip\n",
          file=sys.stderr)
    for p in data["projections"]:
        if p["status"] != "open" or p["id"] not in vmap:
            continue
        v = vmap[p["id"]]
        print(f"\n{p['id']} · you stated {p['probability']}% · deadline {p['deadline']}")
        print(f"  CLAIM: {p['statement']}")
        print(f"  CRITERION: {p['resolution']}")
        print(f"  --- AUDITOR ({args.auditor}) ---")
        print(f"  VERDICT: {v.get('verdict','?')}  (confidence: {v.get('confidence','?')})")
        print(f"  EVIDENCE: {v.get('evidence','—')}")
        print(f"  DISCONFIRMING: {v.get('disconfirming','—')}")
        if v.get("note"):
            print(f"  NOTE: {v['note']}")
        ans = input("  [a]ccept / [h]it / [m]iss / [v]oid / [s]kip > ").strip().lower()
        mapped = None
        if ans == "a":
            mapped = {"HIT": "hit", "MISS": "miss",
                      "AMBIGUOUS": None}.get(str(v.get("verdict", "")).upper())
            if mapped is None:
                print("  auditor said AMBIGUOUS — left open for your later ruling",
                      file=sys.stderr)
                continue
        elif ans in ("h", "m", "v"):
            mapped = {"h": "hit", "m": "miss", "v": "void"}[ans]
        if mapped:
            p["status"] = mapped
            p["resolved_date"] = today.strftime("%Y-%m-%d")
            p["audit"] = {"auditor": args.auditor, "verdict": v.get("verdict"),
                          "confidence": v.get("confidence"),
                          "evidence": v.get("evidence", "")[:600],
                          "disconfirming": v.get("disconfirming", "")[:400]}
            note = input("  your note (enter = use auditor evidence) > ").strip()
            p["notes"] = note or f"[{args.auditor}] {v.get('evidence','')[:600]}"
            ruled += 1
    save_ledger(data)
    print(f"\nKKR · {ruled} projections ruled and written to the ledger", file=sys.stderr)
    render_ledger()


def main():
    ap = argparse.ArgumentParser(description="KKR — Kaos Kontrol Report: forecasts + predictive ledger")
    ap.add_argument("--provider", choices=["lmstudio", "anthropic", "auto"], default="lmstudio")
    ap.add_argument("--model", default=None)
    ap.add_argument("--lmstudio-url", default="http://localhost:1234/v1")
    ap.add_argument("--packet-only", action="store_true")
    ap.add_argument("--ingest", metavar="FILE")
    ap.add_argument("--packet", metavar="NAME",
                    help="with --ingest: the packet filename this arm forecast against")
    ap.add_argument("--arm", metavar="TAG",
                    help="with --ingest: forecaster arm tag (default manual/fable)")
    ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--all", action="store_true", help="with --resolve: include not-yet-due")
    ap.add_argument("--score", action="store_true")
    ap.add_argument("--mine", action="store_true", help="enter your own forecasts (operator/human lane)")
    ap.add_argument("--audit-export", action="store_true",
                    help="export past-deadline projections as an audit packet")
    ap.add_argument("--audit-ingest", metavar="FILE",
                    help="ingest an auditor's verdict JSON; you rule on each")
    ap.add_argument("--auditor", default="claude",
                    help="name of the auditor for provenance (claude/qwen/other)")
    args = ap.parse_args()

    if args.audit_export:
        cmd_audit_export(args)
    elif args.audit_ingest:
        cmd_audit_ingest(args)
    elif args.mine:
        cmd_mine(args)
    elif args.resolve:
        cmd_resolve(args)
    elif args.score:
        render_ledger()
        all_p = load_ledger()["projections"]
        _ov_arms = {}
        for _ov_x in (all_p or []):
            if isinstance(_ov_x, dict) and _ov_x.get("status") in ("hit", "miss"):
                _ov_k = _ov_x.get("model") or "(untagged)"
                _ov_arms[_ov_k] = _ov_arms.get(_ov_k, 0) + 1
        if len(_ov_arms) > 1:
            _ov_d = ", ".join("%s %d" % (k, v) for k, v in sorted(_ov_arms.items()))
            print("=== OVERALL - POOLED across %d arms (%s). NOT a forecaster's record. "
                  "Diagnostic only; do not publish or quote. See per-lane blocks. ===" % (len(_ov_arms), _ov_d))
        elif len(_ov_arms) == 1:
            _ov_k, _ov_v = list(_ov_arms.items())[0]
            print("=== OVERALL - one arm only (%s, %d resolved). Equals that arm's record; "
                  "label it by arm if quoted. ===" % (_ov_k, _ov_v))
        else:
            print("=== OVERALL - no resolved entries ===")
        print(json.dumps(brier_and_calibration(all_p), indent=2))
        lanes = {}
        for p in all_p:
            lanes.setdefault(p.get("model") or "unattributed", []).append(p)
        for lane, ps in sorted(lanes.items()):
            s = brier_and_calibration(ps)
            if s.get("n_resolved"):
                print(f"=== {lane.upper()} ==="); print(json.dumps(s, indent=2))
    elif args.ingest:
        cmd_ingest(args)
    else:
        cmd_generate(args)


if __name__ == "__main__":
    main()
