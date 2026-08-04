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

from runguard import write_run_artifact   # KK21h: one definition, not four

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
GATE 4 VERIFY — check the resolution criterion is adjudicable by a third party from public reporting, and the deadline is an absolute weekday date at least 2 days after the event window closes. Fix or discard.
GATE 5 REPORT — only projections that survive all four gates go in the array.
Apply the gates, then: From the intelligence report below, generate 8-10 falsifiable projections (keep each resolution under 40 words so the full JSON array fits) spanning at least 4 domains (military/conflict, economics/markets, cyber, political, crime/security, disaster).

Every projection MUST:
1. Be a single observable claim a third party could verify from public reporting at the deadline. No vague language ("tensions will continue", "pressure will mount"). ABSOLUTE DATES ONLY: never write "within 72 hours" or "within the next N days" — write the explicit event window ("between 2026-07-21 and 2026-07-24") in both statement and resolution. The window is when the EVENT may occur; the deadline is when it is ADJUDICATED. They are not the same date.
2. Carry "probability": an integer 5-95, never 0 or 100.
3. Carry "resolution": the exact criterion that settles it true or false.
4. Carry "deadline": an ISO date between {min_date} and {max_date}. If the resolution depends on a market close or settlement, the deadline must be a weekday. If the resolution depends on third-party confirmation (two sources, hostile sides, an agency feed, a wire service), the deadline must fall at least 2 days AFTER the last day of the event window — corroboration does not exist on the day the event happens, and a row adjudicated the next morning is graded MISS before its own evidence can appear.
5. Carry "citations": a list of item numbers from the report's record that ground it.
6. Carry "failure_condition": one sentence naming what, observed at the deadline, makes this entry a MISS. State the CONDITION that must fail, not the source that reports it. Pre-register it now; it is not editable later.
7. Base-rate discipline: most discrete events do not happen; do not cluster probabilities at 60-80%. At least two projections must be rated BELOW 35%.
8. WINDOW, NOT DATE: an unscheduled event (strike, attack, wildfire, earthquake, outbreak, cyberattack, resignation, indictment) MUST be given a window of at least 7 days. Never require an unscheduled event to occur on one named calendar day. The probability of a stochastic event on a specific date is a small fraction of its probability across a window, and pricing a single date at window rates is the most common scoring error in this record. Only events with a published schedule (elections, central bank meetings, hearings, contract expiries, scheduled releases) may name one date.
9. NEVER write a condition about the ABSENCE of reporting. Phrases like "with no casualties reported" describe the source record, not the world. The report line "Casualties: none stated in the corroborating reports" is a statement about the reports themselves. Do not lift it into a projection; it cannot be adjudicated as a property of the event.
11. PREFER A MACHINE-READABLE SOURCE OF RECORD. Where the claim admits one, resolve against a named public register a script can fetch - CISA KEV or NVD for vulnerabilities, the Federal Register or a Congress.gov roll call for US government action, Treasury/FRED/ECB or a named exchange settlement for rates and prices, USGS/GDACS/NIFC/NWS for natural events, a court docket for legal outcomes. Write "the CISA KEV catalog carries a date-added value between A and B", not "two wire services report the vulnerability is exploited". Both are falsifiable; only one can be checked by anyone, in one fetch, years later. Where no such register exists - most military and conflict claims - name the outlets and the corroboration standard as before, and do not invent a register that does not exist.
10. CITE THE ITEM, NOT THE RECORD. "citations" names the specific numbered items that ground THIS claim - normally one to three, never more than seven. Citing the whole record is the same as citing nothing: a prior that excludes nothing predicts nothing, and a projection cited against every item cannot be graded for whether it went beyond its inputs. If no item grounds the claim, do not invent a citation - drop the projection.

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
            # A control row without its basis is not a control. baserate.py
            # writes the rate, the n behind it, the reference class and the
            # as-of date; the allowlist above used to drop the lot, sealing
            # nine rows whose provenance lived only in the packet file.
            # Structured passthrough, kept verbatim, never synthesised here.
            if isinstance(p.get("control_basis"), dict):
                entry["control_basis"] = p["control_basis"]
                entry["is_control"] = True
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


_CITE_STOP = set("""a an and are as at be been being between by for from had has have
her his in into is it its of on or that the their there these they this to was were
will with within after before during over under more most least than then when where
which who whom whose about above below across against among around because but each
either how if into just like near new now only other same since so some such through
until up upon very what while would could should may might must can also per not no
report reports reported reporting confirm confirms confirmed confirming public
statement source sources credible outlet outlets news least via data official"""
.split())


def _tokens_overlap(a: set, b: set) -> set:
    """Overlap tolerant of the demonym and adjectival forms news headlines use.

    Exact match, OR one token a prefix of the other at >= 4 chars
    (iran/iranian, israel/israeli), OR a shared prefix of >= 5
    (ukraine/ukrainian). KK21b judgment call: without it, a claim about
    "Iranian officials" shares nothing with an item about "Iran". It cuts both
    ways - looser matching also lets weak citations through - and the
    thresholds are printed here so they can be argued with rather than
    discovered.
    """
    hit = set()
    for x in a:
        for y in b:
            if x == y:
                hit.add(x)
            elif len(x) >= 4 and len(y) >= 4 and (x.startswith(y) or y.startswith(x)):
                hit.add(x)
            else:
                n = 0
                for cx, cy in zip(x, y):
                    if cx != cy:
                        break
                    n += 1
                if n >= 5:
                    hit.add(x)
    return hit


def _content_words(s: str) -> set:
    """Substantive vocabulary only. Dates, pure numbers and identifier tokens
    are stripped so a shared '2026' or 'CVE' can never read as support."""
    toks = re.findall(r"[A-Za-z][A-Za-z'-]{2,}", s.lower())
    out = set()
    for t in toks:
        t = t.strip("'-")
        if len(t) < 4 or t in _CITE_STOP:
            continue
        out.add(t[:-1] if t.endswith("s") and len(t) > 4 else t)
    return out


# --- citation gate v2 (KK21) -------------------------------------------
# The KK18 gate rejected a row only when the UNION of its cited items shared
# no substantive vocabulary with the claim. Three failures walked through it:
#
#   SHOTGUN   cite every item and overlap is guaranteed. A prior that
#             excludes nothing predicts nothing.
#   THIN      overlap only on words common across the whole report. Shared
#             vocabulary is not shared content.
#   AMBIGUOUS one number resolving to several items (see P1). Charitable
#             resolution: if ANY candidate supports, the row passes — the
#             gate must never reject on a reference it cannot resolve.
#
# All three push the keyed/keyless call toward KEYLESS by making priors look
# narrower than they are. That is the corruption the gate now closes.

_CITE_SHOTGUN_ABS = 8       # citing >=8 items is not citing
_CITE_SHOTGUN_FRAC = 0.50   # or >=50% of the record, whichever binds first
_CITE_DF_RARE_FRAC = 0.25   # token in <=25% of items = discriminating


def _report_items(path):
    """Numbered items -> {n: [text, ...]}. A number may carry several texts:
    that is the ambiguity, recorded rather than collapsed."""
    items = {}
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return items
    for line in lines:
        m = re.match(r"\s*(\d+)\.\s+(.*)", line)
        if m:
            items.setdefault(int(m.group(1)), []).append(
                re.sub(r"\[link\]\(\S+\)", "", m.group(2)))
    return items


def _rare_tokens(items):
    """Content words appearing in <= _CITE_DF_RARE_FRAC of this report's items.
    Rarity is measured inside the report: the discriminating question is
    whether a token separates the cited item from its neighbours."""
    from collections import Counter
    df, total = Counter(), 0
    for texts in items.values():
        for t in texts:
            total += 1
            for w in _content_words(t):
                df[w] += 1
    cut = max(1, int(max(1, total) * _CITE_DF_RARE_FRAC))
    return {w for w, c in df.items() if c <= cut}, total


def _citation_support(p: dict):
    """Do the cited report items share ANY substantive vocabulary with the
    claim? Blunt by design - it cannot judge relevance, only whether the
    forecaster's declared priors are readable as priors at all.

    Returns a rejection reason, or None. Returns None (passes) whenever the
    source report is unavailable: an absent file is not evidence of a bad
    citation, and the gate must not reject on what it cannot see.
    """
    src = p.get("source_report") or ""
    if not src:
        return None
    path = Path(__file__).resolve().parent / "reports" / src
    if not path.exists():
        return None
    cites = {int(c) for c in (p.get("citations") or [])
             if str(c).strip().lstrip("-").isdigit() and int(c) > 0}
    if not cites:
        return None                       # [0] is the operator sentinel
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return None
    cited_text, found = [], set()
    for line in lines:
        m = re.match(r"\s*(\d+)\.\s+(.*)", line)
        if m and int(m.group(1)) in cites:
            cited_text.append(re.sub(r"\[link\]\(\S+\)", "", m.group(2)))
            found.add(int(m.group(1)))
    if not found:
        return None                       # cannot resolve; do not reject blind

    items = _report_items(path)
    total_items = sum(len(v) for v in items.values())
    if total_items and (len(cites) >= _CITE_SHOTGUN_ABS
                        or len(cites) / total_items >= _CITE_SHOTGUN_FRAC):
        return (f"cites {len(cites)} of {total_items} items in the record "
                "\u2014 a prior that excludes nothing predicts nothing, and a "
                "keyless determination against the whole record is a "
                "determination against no record; cite the items that ground "
                "THIS claim")

    rare, _ = _rare_tokens(items)
    claim = _content_words(p.get("statement", "") + " " + p.get("resolution", ""))
    if not claim:
        return None
    best, any_overlap = "NONE", False
    for c in sorted(cites):
        for txt in items.get(c, []):
            shared = _tokens_overlap(claim, _content_words(txt))
            if not shared:
                continue
            any_overlap = True
            if _tokens_overlap(shared, rare):
                best = "STRONG"
                break
        if best == "STRONG":
            break
    if best == "STRONG":
        return None
    if not any_overlap:
        return ("cited items share no substantive vocabulary with the claim "
                "\u2014 a citation that does not support its entry makes the "
                "4.02f priors unreadable and forces the keyed/keyless call to "
                "default; cite an item that grounds THIS claim")
    return ("cited items overlap the claim only on vocabulary common across "
            "the whole report \u2014 shared words are not shared content, and a "
            "prior that fits every item grounds none of them; cite an item "
            "carrying something specific to THIS claim")


_MARKET_ANCHOR_WARN_ONLY = True


def _market_anchor(p: dict):
    """A price or yield threshold is keyed or keyless by the SIZE of the gap
    between the level held and the level claimed. With no reference stated the
    gap is unmeasurable and the row defaults to keyed forever - which would
    make the markets domain permanently unable to carry keyless weight (5.05).
    """
    both = (p.get("statement", "") + " " + p.get("resolution", ""))
    if not re.search(r"\b(settle[sd]?|close[sd]?|yield|per barrel|index|"
                     r"exchange rate|front-month)\b", both, re.I):
        return None
    if re.search(r"\b(reference|as of|currently|prevailing|last (?:close|settle))\b",
                 both, re.I):
        return None
    return ("market-threshold row states no reference level \u2014 without the "
            "level held at seal the keyed/keyless gap cannot be measured and "
            "the entry defaults to keyed (4.03/5.05); add e.g. "
            "'Reference: NN.NN on the packet date'")


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
    else:
        _unsup = _citation_support(p)
        if _unsup:
            reasons.append(_unsup)
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
    # KK18 patch: context-anchored venue-'or'. Old caps-or-caps proxy missed
    # lowercase alternatives and false-fired on actor disjunctions.
    _vmask = re.sub(r"\b(?:at|on)\s+or\s+(?:above|below|before|after)\b"
                    r"|\bor\s+(?:more|greater|higher|later|fewer|less)\b",
                    " ", res, flags=re.I)
    _vscopes = re.findall(
        r"(?:resolved from|reported by|verified by|confirmed by|published by|"
        r"according to|per|disclosure from|statement from|advisory from|"
        r"report from|releases? from|\bfrom)\s+([^;]*?)(?=\.\s|\.$|;|$)", _vmask, re.I)
    _vclass = re.search(
        r"\b(?:two|three|four|\d+)\s+(?:or more\s+)?(?:major\s+|independent\s+|"
        r"international\s+|credible\s+)*(?:news\s+)?"
        r"(?:sources|outlets|agencies|wire services)\b", _vmask, re.I)
    _vhit = False
    if _vscopes:
        _vhit = any(re.search(r"\s+or\s+", _s) for _s in _vscopes)
    elif not _vclass:
        _vhit = bool(
            re.search(r"\b[A-Z][\w.&'-]+,?\s+or\s+(?:the\s+)?[A-Z]", _vmask) or
            re.search(r"\b[A-Z][\w.&'-]+\s+or\s+an?\s+[\w-]+(?:\s+[\w-]+){0,3}\s+"
                      r"(?:firm|source|outlet|agency|service|publication)\b", _vmask))
    if _vhit:
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
    # KK21k: prefer a MECHANICALLY CHECKABLE source of record. A row resolving
    # on "two wire services report X" can never be settled by a script; the
    # same claim against a named public register settles in one fetch, by
    # anyone, forever. Mechanical coverage on 2026-08-04 was 10 of 265 rows,
    # and ~172 of the 234 narrative rows sit in domains that HAVE a register.
    # A NOTE, not a rejection: the operator may have a reason, and a warning
    # that blocks work is a warning that gets switched off.
    _MECH_BY_DOMAIN = {
        "cyber": "CISA KEV catalog, NVD, or the vendor's own advisory page",
        "economics/markets": "Treasury par-yield series, FRED, ECB Data Portal, "
                             "or a named exchange settlement",
        "economics": "Treasury par-yield series, FRED, or ECB Data Portal",
        "political": "the Federal Register API or a Congress.gov roll-call record",
        "disaster": "USGS FDSN, GDACS, NIFC situation reports, or NWS alerts",
        "crime/security": "a court docket or a DOJ press release",
        "public/health": "WHO, CDC, or HHS published data",
    }
    _dom_key = str(p.get("domain", "")).strip().lower().replace("_", "/")
    _mech = _MECH_BY_DOMAIN.get(_dom_key)
    if _mech and not re.search(
            r"\b(?:kev|known exploited|nvd|cve|advisory|federal register|"
            r"congress\.gov|roll[- ]call|treasury|fred|ecb|usgs|fdsn|gdacs|"
            r"nifc|nws|inciweb|docket|department of justice|doj|who|cdc|hhs|"
            r"eurostat|bls|census|sec\.gov|edgar|api|catalog|register|dataset)\b",
            res, re.I) and re.search(
            r"\b(?:wire service|news agency|news outlet|media report|press "
            r"report|reported by|two or more (?:independent )?(?:sources|"
            r"outlets|wire)|independent sources)\b", res, re.I):
        print(f"KKR · NOTE · {p.get('id','(new)')}: resolution rests "
              f"on press reporting in a domain that has a machine-readable "
              f"register ({_mech}). A row settled by a named register is "
              f"resolvable by anyone in one fetch, forever; a row settled by "
              f"'wire services report' is a search problem at every future "
              f"adjudication. Not rejected — name the register where the "
              f"claim admits one.", file=sys.stderr)
    if re.search(r"\b(?:price|yield|rate|level|magnitude|count|total|"
                 r"threshold|close[sd]?|above|below|exceed)\b", both, re.I) \
            and not re.search(r"(?:above|below|exceed\w*|at least|at or|over|"
                              r"under|reach\w*|close[sd]?|threshold|magnitude|"
                              r"least)\D{0,12}[\$\u20ac]?"
                              r"(?:\d|one\b|two\b|three\b|four\b|five\b|"
                              r"six\b|seven\b|eight\b|nine\b|ten\b)", both, re.I) \
            and not re.search(r"\d[\d.,]*\s*(?:percentage[ -]points?|pp\b|"
                              r"bps\b|basis[ -]points?|percent\b|%)", both, re.I) \
            and not re.search(r"\b(?:lower|higher|less|greater|above|below)\s+than\s+"
                              r"the\s+\w+(?:\s+\w+){0,5}\s+(?:set|published|announced|"
                              r"recorded|established|adopted)\b", both, re.I):
        reasons.append("measurable claim without a numeric threshold \u2014 "
                       "a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count")
    if re.search(r"^\s*if\b|\bonly if\b|\bprovided that\b|\bin the event\b",
                 p["statement"], re.I) and "void" not in res.lower():
        reasons.append("conditional trigger without a void clause \u2014 "
                       "pre-register what happens when the antecedent fails")
    _regp = Path(__file__).resolve().parent / "arms.json"
    if _regp.exists():
        try:
            _active = {a["tag"] for a in
                       json.loads(_regp.read_text(encoding="utf-8"))["arms"]
                       if a.get("status") == "active"}
        except Exception:
            _active = None
        if _active and p.get("model") and p["model"] not in _active:
            reasons.append("arm tag not registered active in arms.json \u2014 "
                           "identity is explicit this era: lane/model/access, "
                           "registered before sealing")
    if not (5 <= p["probability"] <= 95):
        reasons.append("probability outside 5-95")
    # --- KK19 gate: window discipline ---
    # KK21b: bounds are read by ROLE, not by position. Taking the earliest and
    # latest date anywhere in the row assumes every date is a window bound.
    # A confirmation date and a baseline anchor are neither, and reading them
    # as bounds rejected eight rows on 2026-08-03 for stating them explicitly.
    _all_dates = sorted(set(re.findall(r"\b(20\d{2}-\d{2}-\d{2})\b", both)))
    _win = re.search(r"\bbetween\s+(20\d{2}-\d{2}-\d{2})\s+and\s+"
                     r"(20\d{2}-\d{2}-\d{2})\b", both, re.I)
    _governed = set()
    for _m in re.finditer(r"\b(?:confirm\w*|verif\w*|report\w*|corroborat\w*)"
                          r"\s+(?:by|on)\s+(20\d{2}-\d{2}-\d{2})\b", both, re.I):
        _governed.add(_m.group(1))
    for _m in re.finditer(r"\b(?:in\s+effect\s+on|as\s+of|described\s+in\s+the|"
                          r"dated|on\s+or\s+before|the)\s+(20\d{2}-\d{2}-\d{2})\b",
                          both, re.I):
        _governed.add(_m.group(1))
    if _win:
        _dates = sorted({_win.group(1), _win.group(2)})
    else:
        _dates = [d for d in _all_dates if d not in _governed] or _all_dates
    _sched = re.search(r"\b(?:scheduled|calendar|election|referendum|summit|"
                       r"fomc|meeting|hearing|verdict|sentencing|expir\w*|"
                       r"settle\w*|auction|inaugurat\w*|swearing|"
                       r"regularly scheduled|already announced)\b", both, re.I)
    _confirm = re.search(r"\b(?:confirmed by|reported by|verified by|"
                         r"corroborat\w+|independent sources|hostile sides|"
                         r"wire services|news agencies)\b", both, re.I)
    if _dates and _dates[0] == _dates[-1] and not _sched:
        reasons.append("single-day resolution window for an unscheduled event — "
                       f"the row requires this to occur on {_dates[0]} exactly. "
                       "Price a day, not a window: widen the window or state why "
                       "the date is fixed")
    if _dates and _confirm:
        try:
            _wend = datetime.strptime(_dates[-1], "%Y-%m-%d").date()
            _dl = datetime.strptime(p["deadline"], "%Y-%m-%d").date()
            if (_dl - _wend).days < 2:
                reasons.append("deadline leaves no settling margin — resolution "
                               "requires third-party confirmation and the "
                               f"deadline ({_dl}) is {(_dl - _wend).days} day(s) "
                               f"after the window closes ({_wend}). Cross-bias "
                               "confirmation does not exist yet on the morning "
                               "the resolver walks the row; allow >= 2 days")
        except ValueError:
            pass
    if re.search(r"\bwith\s+no\s+\w+(?:\s+\w+){0,2}\s+"
                 r"(?:reported|stated|confirmed|recorded|observed)\b", both, re.I) \
            or re.search(r"\bno\s+casualties\s+(?:are\s+)?"
                         r"(?:reported|stated|mentioned)\b", both, re.I):
        reasons.append("negated-observation clause — 'with no X reported' is a "
                       "claim about the source record, not about the event. The "
                       "war desk prints it to describe its own reports; it "
                       "cannot be adjudicated as a property of the world")
    # --- KK20: window may not open before the seal ---
    if _dates:
        try:
            _open = datetime.strptime(_dates[0], "%Y-%m-%d").date()
            _now = datetime.now(timezone.utc).date()
            if _open < _now:
                reasons.append(
                    f"event window opens {_open}, before this row is sealed "
                    f"({_now}) — part of the window has already elapsed and the "
                    f"outcome may already exist. A commitment made after the "
                    f"fact is retrodiction, not forecast; open the window today "
                    f"or later")
        except ValueError:
            pass
    _anchor = _market_anchor(p)
    if _anchor:
        if _MARKET_ANCHOR_WARN_ONLY:
            print(f"KKR \u00b7 NOTE \u00b7 {p.get('id','(new)')}: {_anchor}",
                  file=sys.stderr)
        else:
            reasons.append(_anchor)
    return reasons


def _kk21f_write_run_artifact_superseded(path: Path, text: str,
                                         encoding: str = "utf-8") -> Path:
    """Superseded by runguard.write_run_artifact (KK21h). Kept unreferenced
    rather than deleted so the diff shows what moved and where."""
    """Write a run artifact without ever destroying another run's.

    KK21f. Five times in one day a run artifact was overwritten by a later run
    and nothing was printed: a mutable anchor target, a control packet twice, a
    report stamped by day, the same report stamped by minute and arm. Each fix
    added a component to a filename and closed only the case that had just
    happened, because a run always has one more distinguishing property than
    the naming scheme anticipated.

    So the guard is not a better name. If the path is taken by DIFFERENT bytes,
    suffix and print. Identical bytes rewrite silently, because a rerun that
    produces the same artifact is not a collision.
    """
    path = Path(path)
    if path.exists():
        try:
            if path.read_text(encoding=encoding, errors="replace") == text:
                path.write_text(text, encoding=encoding)
                return path
        except Exception:
            pass
        n = 2
        while True:
            alt = path.with_name(f"{path.stem}_{n}{path.suffix}")
            if not alt.exists():
                break
            n += 1
        print(f"KKR · {path.name} already holds a different run - writing "
              f"{alt.name} rather than discarding it", file=sys.stderr)
        path = alt
    path.write_text(text, encoding=encoding)
    return path


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
    mine = arms.get(model_tag)
    if mine is None:
        # KK18 patch: era-split registry tags never appear bare in arm_stats.
        # Show the CURRENT era bucket - the effective forecaster - per 84020db.
        _bk = sorted(k for k in arms if k.startswith(model_tag + "["))
        if _bk:
            _pick = _bk[-1]
            try:
                _eras = {a["tag"]: a.get("eras") for a in json.loads(
                    (Path(__file__).resolve().parent / "arms.json")
                    .read_text(encoding="utf-8"))["arms"]}.get(model_tag)
                _td = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                for _e in _eras or []:
                    if _e.get("from") and _td >= _e["from"] and not _e.get("until"):
                        _c = model_tag + "[" + _e["id"] + "]"
                        if _c in arms:
                            _pick = _c
            except Exception:
                pass
            model_tag = _pick
            mine = arms[_pick]
    if mine is None:
        mine = {"issued": 0, "open": 0, "n_resolved": 0}
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
    # KK20: per-run stamp. The report is a run artifact; a per-day name let
    # a second run of the same UTC date overwrite the first run's published
    # rejection trail. Minute resolution, war-desk pattern.
    stamp = now.strftime("%Y-%m-%d_%H%M")
    # KK21d: minute resolution still collides. Two arms ingested back to back
    # wrote the same filename on 2026-08-04 and the second erased the first's
    # rejection trail. A finer timestamp only postpones it; the arm is what
    # actually makes the two runs different, so the arm goes in the name.
    # No try/except here on purpose. The first cut of this patch wrapped the
    # slug in a bare except and referenced the wrong variable name; the
    # NameError was swallowed, the slug came back empty, and the two runs
    # collided again with nothing printed - the exact failure this patch
    # exists to remove, reintroduced by the fix. If model_tag is not there,
    # this should raise.
    _arm_slug = "".join(c if c.isalnum() else "-" for c in str(model_tag)).strip("-")
    if _arm_slug:
        stamp = f"{stamp}_{_arm_slug}"
    OUT.mkdir(exist_ok=True)
    _md_path = write_run_artifact(OUT / f"KKR_{stamp}.md", md)
    html_doc = render_html(md, f"KKR {stamp}")
    write_run_artifact(OUT / f"{_md_path.stem}.html", html_doc)
    (OUT / "KKR_latest.html").write_text(html_doc, encoding="utf-8")
    publish_served()
    print(f"KKR · report → {_md_path} (+ KKR_latest.html)", file=sys.stderr)


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


def canon_domain(raw) -> str:
    """Canonical domain for RPAS 5.05 counting.

    The book carries several spellings per domain. Counting them separately
    would make the multi-domain bar look cleared on one domain written five
    ways - an error that always flatters. Sealed rows keep their string
    (5.06); this resolves the reading.
    """
    s = str(raw or "").strip().lower()
    path = Path(__file__).resolve().parent / "domains.json"
    if not path.exists():
        return s or "unclassified"
    try:
        m = json.loads(path.read_text(encoding="utf-8"))["aliases"]
    except Exception:
        return s or "unclassified"
    if s in m:
        return m[s]
    norm = s.replace("_", "/").split("/")[0]
    return m.get(norm, s or "unclassified")


def domain_spread(projs: list) -> dict:
    """Canonical domain -> count. What 5.05 should actually be reading."""
    out = {}
    for p in projs:
        d = canon_domain(p.get("domain"))
        out[d] = out.get(d, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


def arm_stats(projs: list) -> dict:
    """Per-forecaster-arm record.

    A Brier score is a property of ONE forecaster. Averaging across arms produces
    a number that describes nobody and flatters or damns whichever arm has fewer
    resolved rows. Nothing in this file may publish a pooled score.
    """
    arms = {}
    for p in projs:
        arms.setdefault(p.get("model") or "unattributed", []).append(p)
    # era split (arms-registry): a tag whose registry entry carries eras is
    # bucketed by date_issued - pre and post are different effective
    # forecasters and a Brier belongs to one forecaster.
    _regp = Path(__file__).resolve().parent / "arms.json"
    if _regp.exists():
        try:
            _reg = {a["tag"]: a for a in
                    json.loads(_regp.read_text(encoding="utf-8"))["arms"]}
        except Exception:
            _reg = {}
        for _tag in list(arms):
            _eras = _reg.get(_tag, {}).get("eras")
            if not _eras:
                continue
            _rows = arms.pop(_tag)
            for _p in _rows:
                _d = str(_p.get("date_issued") or "")
                _bucket = _tag
                for _e in _eras:
                    if _e.get("until") and _d and _d < _e["until"]:
                        _bucket = _tag + "[" + _e["id"] + "]"
                        break
                    if _e.get("from") and _d and _d >= _e["from"]:
                        _bucket = _tag + "[" + _e["id"] + "]"
                arms.setdefault(_bucket, []).append(_p)
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
    # KK21l: through the guard, and _LAST_PACKET set from the path ACTUALLY
    # written. This writer destroyed 19 elicitation inputs between 07-20 and
    # 07-26 — the filename carried a date while the reports carried a time, so
    # eight runs on 07-20 left one packet. 96 sealed entries name a report
    # whose packet no longer exists. Setting _LAST_PACKET before the write
    # would, the first time the guard suffixed, make every entry in that run
    # cite a packet it never read: a caught collision turned into a silent
    # misattribution, which is worse than the collision.
    packet = write_run_artifact(packet, prompt, tag="packet")
    globals()["_LAST_PACKET"] = packet.name
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
    # KK21c: the report is resolved BEFORE validation and stamped on each row.
    # It used to be resolved three lines after the gate ran, so
    # _citation_support saw an empty source_report and returned pass every
    # time. Every row that ever entered through --ingest was ungated on
    # citations; cmd_generate set the field first, so only lmstudio/auto was
    # ever checked.
    _rep_name = getattr(args, "report", None)
    if _rep_name:
        rep = REPORTS / _rep_name
        if not rep.exists():
            print(f"KKR · no such report: {rep} — an arm cannot be attributed "
                  f"to a record that is not on disk", file=sys.stderr)
            sys.exit(1)
    else:
        rep = latest_report()
        if rep:
            print(f"KKR · source_report assumed: {rep.name} (newest on disk; "
                  f"pass --report to name the record this arm actually read)",
                  file=sys.stderr)
    src_name = rep.name if rep else "manual"
    accepted_raw, rejected = [], []
    for p in projs:
        if rep:
            p["source_report"] = src_name
        reasons = validate_projection(p)
        _cs = _citation_support(p)
        if _cs:
            reasons = list(reasons) + [_cs]
        (rejected.append((p, reasons)) if reasons else accepted_raw.append(p))
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
    import hashlib as _hl
    body = AUDIT_PROMPT_HEADER.format(
        stamp=now.strftime("%d%H%MZ %b %y").upper(), n=len(due))
    body += ("\n_adjudication-prompt sha256: "
             + _hl.sha256(AUDIT_PROMPT_HEADER.encode("utf-8")).hexdigest() + "_\n")
    for p in due:
        body += (f"\n### {p['id']}\n"
                 f"- **Issued:** {p['date_issued']}  ·  **Deadline:** {p['deadline']}\n"
                 f"- **Domain:** {p.get('domain','general')}\n"
                 f"- **Claim:** {p['statement']}\n"
                 f"- **Resolution criterion:** {p['resolution']}\n"
                 f"- **Failure condition:** {p.get('failure_condition') or '(none recorded)'}\n")
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


def _jury_parse(path):
    raw = Path(path).read_text(encoding="utf-8")
    txt = _normalize_json_text(re.sub(r"```(?:json)?", "", raw).strip())
    m = re.search(r"\[.*\]", txt, re.S)
    if not m:
        print(f"KKR - no JSON array in {path}", file=sys.stderr); sys.exit(1)
    try:
        vs = json.loads(m.group(0))
    except json.JSONDecodeError:
        last = m.group(0).rfind("}")
        vs = json.loads(m.group(0)[:last + 1] + "]") if last != -1 else []
    return {v.get("id"): v for v in vs if v.get("id")}


def cmd_jury_ingest(args):
    """Blind jury: two adjudicators, same blinded packet, same committed
    prompt. Concordance resolves as a recommendation; discord escalates to
    the operator with both opinions printed. The jury recommends; you rule;
    nothing is written without your key. Kappa is printed and logged."""
    import hashlib as _hl
    a_name, b_name = args.auditors
    A = _jury_parse(args.jury[0])
    B = _jury_parse(args.jury[1])
    ph = _hl.sha256(AUDIT_PROMPT_HEADER.encode("utf-8")).hexdigest()
    data = load_ledger()
    today = datetime.now(timezone.utc).date()
    open_ids = [p["id"] for p in data["projections"] if p["status"] == "open"]
    both = [i for i in open_ids if i in A and i in B]
    agree = sum(1 for i in both if str(A[i].get("verdict", "")).upper()
                == str(B[i].get("verdict", "")).upper())
    kappa = None
    if len(both) >= 2:
        cats = ("HIT", "MISS", "AMBIGUOUS")
        na = {c: 0 for c in cats}
        nb = {c: 0 for c in cats}
        for i in both:
            va = str(A[i].get("verdict", "")).upper()
            vb = str(B[i].get("verdict", "")).upper()
            na[va if va in cats else "AMBIGUOUS"] += 1
            nb[vb if vb in cats else "AMBIGUOUS"] += 1
        po = agree / len(both)
        pe = sum(na[c] * nb[c] for c in cats) / (len(both) ** 2)
        kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
    print(f"\nBLIND JURY - {a_name} + {b_name} - prompt sha256 {ph[:16]}...")
    print(f"rows juried by both: {len(both)} - concordant: {agree}"
          + (f" - kappa {kappa:+.3f}" if kappa is not None else " - kappa n/a (n<2)"))
    print("[a]ccept concordant - [1] take " + a_name + " - [2] take " + b_name
          + " - [h]it [m]iss [v]oid [s]kip\n", file=sys.stderr)
    ruled = 0
    vmapd = {"HIT": "hit", "MISS": "miss"}
    for p in data["projections"]:
        if p["status"] != "open" or (p["id"] not in A and p["id"] not in B):
            continue
        va = A.get(p["id"])
        vb = B.get(p["id"])
        print(f"\n{p['id']} - deadline {p['deadline']}")
        print(f"  CLAIM: {p['statement']}")
        print(f"  CRITERION: {p['resolution']}")
        for nm, v in ((a_name, va), (b_name, vb)):
            if v is None:
                print(f"  --- {nm}: no verdict ---")
                continue
            print(f"  --- {nm}: {v.get('verdict','?')} (conf {v.get('confidence','?')}) ---")
            print(f"      EVIDENCE: {str(v.get('evidence','-'))[:300]}")
            print(f"      DISCONFIRMING: {str(v.get('disconfirming','-'))[:200]}")
        conc = bool(va and vb and str(va.get("verdict", "")).upper()
                    == str(vb.get("verdict", "")).upper())
        print("  JURY: " + ("CONCORDANT - " + str(va.get("verdict")).upper() if conc
                            else "DISCORD - operator rules"))
        ans = input("  [a/1/2/h/m/v/s] > ").strip().lower()
        mapped = None
        basis = None
        if ans == "a" and conc:
            mapped = vmapd.get(str(va.get("verdict", "")).upper())
            basis = "jury-concordant"
            if mapped is None:
                print("  jury said AMBIGUOUS - left open", file=sys.stderr)
                continue
        elif ans == "1" and va:
            mapped = vmapd.get(str(va.get("verdict", "")).upper())
            basis = a_name
        elif ans == "2" and vb:
            mapped = vmapd.get(str(vb.get("verdict", "")).upper())
            basis = b_name
        elif ans in ("h", "m", "v"):
            mapped = {"h": "hit", "m": "miss", "v": "void"}[ans]
            basis = "operator"
        if mapped:
            p["status"] = mapped
            p["resolved_date"] = today.strftime("%Y-%m-%d")
            p["audit"] = {"mode": "blind-jury", "auditors": [a_name, b_name],
                          "prompt_sha256": ph, "concordant": conc,
                          "basis": basis,
                          "verdicts": {a_name: (va or {}).get("verdict"),
                                       b_name: (vb or {}).get("verdict")},
                          "evidence": str(((va or vb) or {}).get("evidence", ""))[:600]}
            note = input("  your note (enter = juror evidence) > ").strip()
            p["notes"] = note or f"[jury] {str(((va or vb) or {}).get('evidence',''))[:600]}"
            ruled += 1
    save_ledger(data)
    logp = HERE / "jury_log.json"
    log = []
    if logp.exists():
        try:
            log = json.loads(logp.read_text(encoding="utf-8"))
        except Exception:
            log = []
    log.append({"date": today.strftime("%Y-%m-%d"), "auditors": [a_name, b_name],
                "prompt_sha256": ph, "juried_by_both": len(both),
                "concordant": agree,
                "kappa": (round(kappa, 3) if kappa is not None else None),
                "ruled": ruled})
    logp.write_text(json.dumps(log, indent=1) + "\n", encoding="utf-8")
    print(f"\nKKR - {ruled} ruled and written - jury_log.json appended", file=sys.stderr)
    render_ledger()


def call_anthropic_search(model: str | None, prompt: str) -> str | None:
    """Juror A: Anthropic API with server-side web search enabled.
    Returns concatenated text blocks, or None (no key / call failed)."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    try:
        r = requests.post("https://api.anthropic.com/v1/messages", timeout=600,
                          headers={"x-api-key": key,
                                   "anthropic-version": "2023-06-01",
                                   "content-type": "application/json"},
                          json={"model": model or "claude-sonnet-4-6",
                                "max_tokens": 6000,
                                "tools": [{"type": "web_search_20250305",
                                           "name": "web_search",
                                           "max_uses": 8}],
                                "messages": [{"role": "user", "content": prompt}]})
        r.raise_for_status()
        return "".join(b.get("text", "") for b in r.json().get("content", [])
                       if b.get("type") == "text")
    except Exception as exc:
        print(f"KKR - searched-juror call failed: {exc}", file=sys.stderr)
        return None


def cmd_jury_run(args):
    """The whole jury loop, one command. Export -> two jurors -> your ruling.
    Juror A = Anthropic API with web search (access: searched).
    Juror B = local LM Studio model on the same blinded packet (access: cold,
    until evidence-attachment lands - weigh B's verdict accordingly).
    The interactive ruling is unchanged: nothing writes without your key."""
    import types as _types
    cmd_audit_export(args)
    now = datetime.now(timezone.utc)
    packet = OUT / f"audit_packet_{now.strftime('%Y-%m-%d')}.md"
    if not packet.exists():
        return  # audit_export already said nothing is due
    prompt = packet.read_text(encoding="utf-8")
    stamp = now.strftime("%Y-%m-%d")
    a_path = OUT / f"jury_A_{stamp}.json"
    b_path = OUT / f"jury_B_{stamp}.json"

    print("KKR - juror A (API, searched) ...", file=sys.stderr)
    a_txt = call_anthropic_search(None, prompt)
    if a_txt is None:
        print("KKR - no ANTHROPIC_API_KEY in the environment.\n"
              "      One-time setup:  setx ANTHROPIC_API_KEY <key>  (new shell after)\n"
              "      Until then, manual path: give the packet to Claude, save the\n"
              "      JSON as " + str(a_path) + " and run:\n"
              "      python kkr.py --jury " + a_path.name + " " + b_path.name,
              file=sys.stderr)
    else:
        a_path.write_text(a_txt, encoding="utf-8")
        print(f"KKR - juror A verdicts -> {a_path}", file=sys.stderr)

    print("KKR - juror B (local, cold) ...", file=sys.stderr)
    b_txt = call_lmstudio(args.lmstudio_url,
                          None if args.provider == "auto" else args.model, prompt)
    if b_txt is None:
        print("KKR - local juror unavailable (is LM Studio serving?). "
              "Run daily.bat or `lms server start` and retry.", file=sys.stderr)
    else:
        b_path.write_text(b_txt, encoding="utf-8")
        print(f"KKR - juror B verdicts -> {b_path}", file=sys.stderr)

    if a_txt is None or b_txt is None:
        print("KKR - jury needs both verdict files; ruling not started.",
              file=sys.stderr)
        return
    j = _types.SimpleNamespace(jury=[str(a_path), str(b_path)],
                               auditors=args.auditors)
    cmd_jury_ingest(j)


LANE_MODELS = {
    "opus-5": "claude-opus-5",
    "sonnet-5": "claude-sonnet-5",
    "fable-5": "claude-fable-5",
}


def call_anthropic_lane(model_id: str, prompt: str, searched: bool):
    """One manual-lane forecast call. Tools attached only when searched.

    A bare call carries no tools, so cold is a property of the call rather
    than an assumption about a session - which is what lets the row tag
    /cold as an instrument fact.
    """
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    body = {"model": model_id, "max_tokens": 6000,
            "messages": [{"role": "user", "content": prompt}]}
    if searched:
        body["tools"] = [{"type": "web_search_20250305", "name": "web_search",
                          "max_uses": 10}]
    try:
        r = requests.post("https://api.anthropic.com/v1/messages", timeout=900,
                          headers={"x-api-key": key,
                                   "anthropic-version": "2023-06-01",
                                   "content-type": "application/json"},
                          json=body)
        r.raise_for_status()
        return "".join(b.get("text", "") for b in r.json().get("content", [])
                       if b.get("type") == "text")
    except Exception as exc:
        print(f"KKR - {model_id} lane call failed: {exc}", file=sys.stderr)
        return None


def cmd_lane_run(args):
    """The manual R2 lane without the hand-carry.

    Writes the packet, fires it at each selected lane over the API in
    parallel, writes each arm's projections file, and ingests each under its
    own arm tag. The gate, the seal rules and the ledger writes are the
    existing ones - nothing about adjudication or scoring changes here.
    """
    import concurrent.futures as _cf
    import types as _types

    args.packet_only = True
    cmd_generate(args)                       # writes kkr_packet_<stamp>.md
    packet = OUT / "kkr_packet_latest.md"
    if not packet.exists():
        print("KKR - no packet written; nothing to run", file=sys.stderr)
        return
    prompt = packet.read_text(encoding="utf-8")
    packet_name = str(globals().get("_LAST_PACKET", packet.name))

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("KKR - no ANTHROPIC_API_KEY in the environment.\n"
              "      setx ANTHROPIC_API_KEY <key>   (new shell after)\n"
              "      Packet is written; the manual paste path still works.",
              file=sys.stderr)
        return

    want = [s.strip() for s in (getattr(args, "lanes", None) or
                                "opus-5,sonnet-5,fable-5").split(",") if s.strip()]
    bad = [w for w in want if w not in LANE_MODELS]
    if bad:
        print(f"KKR - unknown lane(s): {', '.join(bad)}. "
              f"Known: {', '.join(LANE_MODELS)}", file=sys.stderr)
        return
    access = "searched" if getattr(args, "lane_searched", False) else "cold"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"KKR - lane run: {', '.join(want)} (access: {access})", file=sys.stderr)
    with _cf.ThreadPoolExecutor(max_workers=len(want)) as ex:
        futs = {ex.submit(call_anthropic_lane, LANE_MODELS[w], prompt,
                          access == "searched"): w for w in want}
        out = {}
        for f in _cf.as_completed(futs):
            w = futs[f]
            txt = f.result()
            if txt:
                p = OUT / f"{w.replace('-', '')}_projections_{stamp}.json"
                p.write_text(txt, encoding="utf-8")
                out[w] = p
                print(f"KKR - {w} -> {p.name}", file=sys.stderr)
            else:
                print(f"KKR - {w} returned nothing; skipped", file=sys.stderr)

    if getattr(args, "no_ingest", False):
        print("KKR - --no-ingest: files written, ledger untouched", file=sys.stderr)
        return
    for w, p in sorted(out.items()):
        tag = f"manual/{w}/{access}"
        print(f"\nKKR - ingesting {p.name} as {tag}", file=sys.stderr)
        a = _types.SimpleNamespace(ingest=str(p), arm=tag, packet=packet_name)
        try:
            cmd_ingest(a)
        except SystemExit:
            raise
        except Exception as exc:
            print(f"KKR - ingest failed for {tag}: {exc}", file=sys.stderr)


def _priors_for(p: dict) -> list:
    """The forecaster's declared priors: the cited items of its source report.

    RPAS 4.02f wants the priors recorded, not just a label. For these lanes
    the priors are exactly the numbered report items the entry cites, so they
    are recoverable verbatim rather than reconstructed from memory.
    """
    cites = [int(c) for c in (p.get("citations") or [])
             if str(c).strip().lstrip("-").isdigit() and int(c) > 0]
    if not cites:
        return []
    src = p.get("source_report") or ""
    path = HERE / "reports" / src
    if not src or not path.exists():
        return [f"(source report {src or 'unnamed'} not on disk - "
                f"cites items {', '.join(map(str, cites))})"]
    # KK21n: EVERY candidate, not the first. Report sections renumbered from 1
    # before 2026-08-04, so one citation number resolves to as many as eight
    # items and 286 sealed entries carry at least one. `want.discard()` took
    # the first match and dropped the rest without saying so — and this is the
    # text a human reads before ruling 1.04, the master law. Choosing one
    # arbitrary candidate on the operator's behalf and presenting it as the
    # record is the worst place on the desk for that to happen.
    found = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"\s*(\d+)\.\s+(.*)", line)
        if m and int(m.group(1)) in set(cites):
            body = re.sub(r"\[link\]\(\S+\)", "", m.group(2))
            body = re.sub(r"[*_`]|\ud83c[\udd70-\udfff]|\ud83d[\udc00-\ude4f]",
                          "", body)
            found.setdefault(int(m.group(1)), []).append(
                re.sub(r"  +", " ", body).strip())
    out = []
    for n in sorted(set(cites)):
        items = found.get(n)
        if not items:
            out.append(f"[{n}] (item not found in {src})")
        elif len(items) == 1:
            out.append(f"[{n}] {items[0]}")
        else:
            out.append(f"[{n}] AMBIGUOUS — this number names {len(items)} "
                       f"different items in {src}. The forecaster cited one of "
                       f"these and the record does not say which:")
            for it in items:
                out.append(f"      · {it}")
    return out


TEMPLATE_WHY = "(state the priors YOU held at seal - this row is yours)"


def _keys_pending(data, due_days=None):
    today = datetime.now(timezone.utc).date()

    def empty(v):
        v = str(v or "").strip()
        return not v or v.lower().startswith("unset")

    out = []
    for p in data["projections"]:
        if p.get("status") != "open" or not empty(p.get("keyed_keyless")):
            continue
        try:
            dl = datetime.strptime(p["deadline"], "%Y-%m-%d").date()
        except Exception:
            continue
        if due_days and (dl - today).days > int(due_days):
            continue
        out.append((dl, p))
    out.sort(key=lambda t: t[0])
    return out


def cmd_keys_export(args):
    """Write the pass as a packet: a review sheet and a fill-in worksheet."""
    data = load_ledger()
    todo = _keys_pending(data, getattr(args, "keys_due", None))
    if not todo:
        print("KKR - nothing pending in scope", file=sys.stderr)
        return
    today = datetime.now(timezone.utc).date()
    OUT.mkdir(exist_ok=True)
    stamp = today.isoformat()

    md = [f"# KEYED / KEYLESS WORKSHEET - {len(todo)} row(s)",
          "",
          f"Generated {stamp}. RPAS 4.02f: decided BEFORE resolution; after "
          f"resolution the entry is KEYED by rule (4.03).",
          "",
          "**keyed** - a hit would be deducible from the priors listed. "
          "**keyless** - no listed prior is sufficient.",
          "",
          "Fill `ruling` and `why` in the matching worksheet JSON, then:",
          f"`python kkr.py --keys-import forecasts/keys_worksheet_{stamp}.json`",
          ""]
    sheet = {}
    manual = 0
    for dl, p in todo:
        is_manual = str(p.get("model", "")).startswith("operator/")
        if is_manual:
            manual += 1
        priors = _priors_for(p)
        md.append("---")
        md.append(f"\n## {p['id']} · {p.get('model')} · {p['deadline']} "
                  f"({(dl - today).days}d) · {p.get('probability')}%"
                  + ("  **[MANUAL - YOUR PRIORS]**" if is_manual else ""))
        md.append(f"\n**Claim:** {p['statement']}")
        md.append(f"\n**Resolves on:** {p['resolution']}")
        if p.get("rationale"):
            md.append(f"\n**Your seal-day rationale:** {p['rationale']}")
        md.append("\n**Priors cited:**\n")
        for pr in (priors or ["*(none cited)*"]):
            md.append(f"- {pr}")
        if is_manual:
            md.append("\n> This row is yours. Its priors are not in any file - "
                      "state what YOU held at seal. The import refuses a "
                      "template rationale here.")
        md.append("")
        sheet[p["id"]] = {"ruling": "", "why": TEMPLATE_WHY if is_manual else "",
                          "_claim": p["statement"][:160],
                          "_arm": p.get("model"), "_deadline": p["deadline"]}

    pmd = OUT / f"keys_packet_{stamp}.md"
    pjs = OUT / f"keys_worksheet_{stamp}.json"
    pmd.write_text("\n".join(md), encoding="utf-8")
    pjs.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"KKR - keys packet ({len(todo)} rows, {manual} manual) -> {pmd}",
          file=sys.stderr)
    print(f"KKR - worksheet -> {pjs}", file=sys.stderr)
    print("KKR - fill ruling (keyed|keyless) and why, then --keys-import",
          file=sys.stderr)


def cmd_keys_import(args):
    """Validate a filled worksheet, then write. All-or-nothing."""
    path = Path(args.keys_import)
    sheet = json.loads(path.read_text(encoding="utf-8"))
    data = load_ledger()
    today = datetime.now(timezone.utc).date()
    index = {p["id"]: p for p in data["projections"]}

    def empty(v):
        v = str(v or "").strip()
        return not v or v.lower().startswith("unset")

    errs, staged = [], []
    for rid, rec in sheet.items():
        ruling = str(rec.get("ruling", "")).strip().lower()
        why = str(rec.get("why", "")).strip()
        if not ruling:
            continue                                  # left blank = skipped
        p = index.get(rid)
        if p is None:
            errs.append(f"{rid}: not in the ledger"); continue
        if p.get("status") != "open":
            errs.append(f"{rid}: status is {p['status']}, not open - "
                        f"4.03 has already ruled it KEYED"); continue
        if not empty(p.get("keyed_keyless")):
            errs.append(f"{rid}: already determined "
                        f"({p['keyed_keyless']}) - sealed rows are not edited")
            continue
        if ruling not in ("keyed", "keyless"):
            errs.append(f"{rid}: ruling '{ruling}' is not keyed or keyless")
            continue
        if not why:
            errs.append(f"{rid}: no rationale - 4.02f requires the priors and "
                        f"the deducibility condition, not a bare label")
            continue
        if str(p.get("model", "")).startswith("operator/") and \
                why.strip() == TEMPLATE_WHY:
            errs.append(f"{rid}: operator row still carries the template "
                        f"rationale - state the priors YOU held at seal")
            continue
        staged.append((p, ruling, why))

    if errs:
        print(f"KKR - {len(errs)} problem(s). NOTHING WRITTEN:", file=sys.stderr)
        for e in errs:
            print(f"    {e}", file=sys.stderr)
        return
    if not staged:
        print("KKR - no rulings filled in; nothing to write", file=sys.stderr)
        return
    for p, ruling, why in staged:
        p["keyed_keyless"] = ruling
        p["keyed_keyless_rationale"] = why[:400]
        p["keyed_keyless_dated"] = today.strftime("%Y-%m-%d")
    save_ledger(data)
    k = sum(1 for _, r, _ in staged if r == "keyed")
    print(f"KKR - {len(staged)} determination(s) written "
          f"({k} keyed, {len(staged) - k} keyless)", file=sys.stderr)
    render_ledger()


def cmd_keys(args):
    """The keyed/keyless pass. RPAS 4.02f, the one call no script can make.

    Keyed   - a hit here would be DEDUCIBLE from the priors above. Arithmetic.
    Keyless - no prior above is sufficient to deduce it. Only these bear on a
              faculty claim (5.04).

    The instrument grades the forecaster, never the operator. Ruling a row
    keyed costs nothing but an honest label; ruling it keyless when the priors
    hand you the answer is the failure mode this field exists to prevent.
    """
    data = load_ledger()
    today = datetime.now(timezone.utc).date()

    def empty(v):
        v = str(v or "").strip()
        return not v or v.lower().startswith("unset")

    due_days = getattr(args, "keys_due", None)
    todo = []
    for p in data["projections"]:
        if p.get("status") != "open" or not empty(p.get("keyed_keyless")):
            continue
        try:
            dl = datetime.strptime(p["deadline"], "%Y-%m-%d").date()
        except Exception:
            continue
        if due_days and (dl - today).days > int(due_days):
            continue
        todo.append((dl, p))
    todo.sort(key=lambda t: t[0])

    if not todo:
        print("KKR - every open row in scope carries a determination.",
              file=sys.stderr)
        return
    done_n = sum(1 for p in data["projections"]
                 if not empty(p.get("keyed_keyless")))
    print(f"\nKEYED / KEYLESS - {len(todo)} row(s) to rule "
          f"({done_n} already determined on the book)")
    print("RPAS 4.02f. Decided BEFORE resolution; after resolution it is "
          "KEYED by rule (4.03).")
    print("  [k]eyed    a hit would be deducible from the priors shown - arithmetic")
    print("  [l]eyless  no prior shown is sufficient to deduce it")
    print("  [s]kip     leave undetermined    [q]uit - everything ruled is "
          "already saved\n")

    ruled = 0
    for dl, p in todo:
        days = (dl - today).days
        print("=" * 70)
        print(f"{p['id']} · {p.get('model','?')} · deadline {p['deadline']} "
              f"({days}d) · stated {p.get('probability','?')}%")
        print(f"\n  CLAIM: {p['statement']}")
        print(f"  RESOLVES ON: {p['resolution'][:300]}")
        # KK21n: what cite_integrity already knows about this entry's
        # citations, printed before the determination rather than after it.
        # An entry whose cited items support nothing cannot honestly be ruled
        # KEYLESS: "it went beyond its declared priors" is unanswerable when
        # the declared priors ground nothing.
        try:
            _civ = HERE / "cite_integrity_2026-08-04.json"
            if not _civ.exists():
                _civ = max(HERE.glob("cite_integrity_*.json"), default=None)
            if _civ:
                _ci = json.loads(Path(_civ).read_text(encoding="utf-8"))
                _row = next((r for r in _ci.get("rows", [])
                             if r.get("id") == p.get("id")), None)
                if _row and _row.get("flags"):
                    print(f"\n  CITATION AUDIT: {'/'.join(_row['flags'])} "
                          f"({_row.get('strong',0)} strong, "
                          f"{_row.get('weak',0)} weak, {_row.get('none',0)} "
                          f"unsupporting)")
                    if "UNSUPPORTED" in _row["flags"]:
                        print("    Nothing cited supports this claim. A KEYLESS "
                              "ruling here asserts the entry went beyond priors "
                              "that ground nothing — KEYED by rule is the "
                              "defensible read (4.03).")
                    if "SHOTGUN" in _row["flags"]:
                        print("    This entry cites most of the record. A prior "
                              "that excludes nothing cannot make a hit "
                              "deducible, and cannot make it non-deducible "
                              "either.")
        except Exception:
            pass
        priors = _priors_for(p)
        print("\n  PRIORS THE FORECASTER HELD (its cited report items):")
        if priors:
            for pr in priors:
                print(f"    - {pr[:220]}")
        else:
            print("    - none cited. An entry with no declared prior cannot "
                  "make a hit deducible; keyless is the usual reading.")
        print("\n  Could this outcome be DEDUCED from those priors alone?")
        try:
            ans = input("  [k]eyed / [l]eyless / [s]kip / [q]uit > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nKKR - stopped. Everything ruled so far is saved.",
                  file=sys.stderr)
            break
        if ans == "q":
            print("KKR - stopped. Everything ruled so far is saved.",
                  file=sys.stderr)
            break
        if ans not in ("k", "l"):
            continue
        val = "keyed" if ans == "k" else "keyless"
        try:
            why = input("  why (one line, recorded in the entry) > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nKKR - stopped before recording that row.", file=sys.stderr)
            break
        if not why:
            why = ("deducible from the cited report items" if val == "keyed"
                   else "no cited item is sufficient to deduce the outcome")
        p["keyed_keyless"] = val
        p["keyed_keyless_rationale"] = why[:400]
        p["keyed_keyless_dated"] = today.strftime("%Y-%m-%d")
        # Written after EVERY row: an interrupt must never discard the pass.
        save_ledger(data)
        ruled += 1
        print(f"  -> {val.upper()}  (saved)\n")

    print(f"\nKKR - {ruled} determination(s) written. "
          f"{len(todo) - ruled} left in scope.", file=sys.stderr)
    if ruled:
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
    ap.add_argument("--report", metavar="NAME",
                    help="with --ingest: the battle report this arm read. "
                         "Citations resolve against it, so an assumed report "
                         "checks the arm's priors against a record it never "
                         "saw. Defaults to newest on disk and says so.")
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
    ap.add_argument("--jury", nargs=2, metavar=("A.json", "B.json"),
                    help="blind jury: two verdict files from the same blinded packet")
    ap.add_argument("--keys-export", action="store_true",
                    help="write the keys pass as a packet + fill-in worksheet")
    ap.add_argument("--keys-import", metavar="FILE",
                    help="apply a filled keys worksheet; validates all or none")
    ap.add_argument("--keys", action="store_true",
                    help="rule the keyed/keyless determination on open rows "
                         "(RPAS 4.02f); deadline order, saves after each row")
    ap.add_argument("--keys-due", metavar="DAYS",
                    help="with --keys: only rows resolving within DAYS")
    ap.add_argument("--lane-run", action="store_true",
                    help="write the packet, run every manual lane over the API, "
                         "and ingest each under its own arm tag")
    ap.add_argument("--lanes", metavar="LIST",
                    help="comma list of lanes (default opus-5,sonnet-5,fable-5)")
    ap.add_argument("--lane-searched", action="store_true",
                    help="attach web search to the lane calls; tags /searched")
    ap.add_argument("--no-ingest", action="store_true",
                    help="with --lane-run: write the files, do not touch the ledger")
    ap.add_argument("--jury-run", action="store_true",
                    help="one command: export packet, run API-searched juror + "
                         "local juror, then the interactive jury ruling")
    ap.add_argument("--auditors", nargs=2, default=["claude", "qwen"],
                    metavar=("NAME_A", "NAME_B"),
                    help="juror names for provenance (default claude qwen)")
    ap.add_argument("--auditor", default="claude",
                    help="name of the auditor for provenance (claude/qwen/other)")
    args = ap.parse_args()

    if args.audit_export:
        cmd_audit_export(args)
    elif args.audit_ingest:
        cmd_audit_ingest(args)
    elif args.keys_export:
        cmd_keys_export(args)
    elif args.keys_import:
        cmd_keys_import(args)
    elif args.keys or args.keys_due:
        cmd_keys(args)
    elif args.lane_run:
        cmd_lane_run(args)
    elif args.jury_run:
        cmd_jury_run(args)
    elif args.jury:
        cmd_jury_ingest(args)
    elif args.mine:
        cmd_mine(args)
    elif args.resolve:
        cmd_resolve(args)
    elif args.score:
        render_ledger()
        all_p = load_ledger()["projections"]
        _ov_arms = {}
        # era-aware (arms-registry): the overall census counts effective
        # forecasters, so era-carrying tags bucket by date_issued here too.
        _ov_regp = Path(__file__).resolve().parent / "arms.json"
        _ov_reg = {}
        if _ov_regp.exists():
            try:
                _ov_reg = {a["tag"]: a for a in
                           json.loads(_ov_regp.read_text(encoding="utf-8"))["arms"]}
            except Exception:
                _ov_reg = {}
        for _ov_x in (all_p or []):
            if isinstance(_ov_x, dict) and _ov_x.get("status") in ("hit", "miss"):
                _ov_k = _ov_x.get("model") or "(untagged)"
                _ov_e = _ov_reg.get(_ov_k, {}).get("eras")
                if _ov_e:
                    _ov_d2 = str(_ov_x.get("date_issued") or "")
                    for _e in _ov_e:
                        if _e.get("until") and _ov_d2 and _ov_d2 < _e["until"]:
                            _ov_k = _ov_k + "[" + _e["id"] + "]"
                            break
                        if _e.get("from") and _ov_d2 and _ov_d2 >= _e["from"]:
                            _ov_k = _ov_k + "[" + _e["id"] + "]"
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
        # era split (arms-registry): same law as the ledger face - a tag
        # with registry eras buckets by date_issued before scoring.
        _regp = Path(__file__).resolve().parent / "arms.json"
        if _regp.exists():
            try:
                _reg = {a["tag"]: a for a in
                        json.loads(_regp.read_text(encoding="utf-8"))["arms"]}
            except Exception:
                _reg = {}
            for _tag in list(lanes):
                _eras = _reg.get(_tag, {}).get("eras")
                if not _eras:
                    continue
                _rows = lanes.pop(_tag)
                for _p in _rows:
                    _d = str(_p.get("date_issued") or "")
                    _bucket = _tag
                    for _e in _eras:
                        if _e.get("until") and _d and _d < _e["until"]:
                            _bucket = _tag + "[" + _e["id"] + "]"
                            break
                        if _e.get("from") and _d and _d >= _e["from"]:
                            _bucket = _tag + "[" + _e["id"] + "]"
                    lanes.setdefault(_bucket, []).append(_p)
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
