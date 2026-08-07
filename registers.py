#!/usr/bin/env python3
"""registers.py — the runtime face of `registers.json`, the register of record.

Standard library only. Nothing here writes to the ledger, and nothing here
rejects anything: it returns verdicts and reasons, and the caller decides
severity. That split is deliberate — a gate that owns both the test and the
sentence is a gate whose reasoning cannot be audited separately from its
outcome.

    python registers.py hash              canonical digest, for hash-commitment
    python registers.py show              what the register holds
    python registers.py verify            drift + internal-consistency check
    python registers.py selftest          the four primitives against KK24 rows
    python registers.py check --row ID    run the primitives over a sealed row

The four primitives, each answering one KK24 finding:

    geo_support(...)      §11.2  a row claiming Arizona cited GDACS items for
                                 Angola, Zambia and Russia. Content-word
                                 overlap matched "forest fire" and the
                                 geography sailed through.
    venue_scope(...)      §11.3  the old rule matched DISJUNCTION, not venue:
                                 false-positived "Washington, Oregon, or
                                 Northern California", false-negatived "a
                                 U.S. government or international disaster
                                 alert system (e.g., GDACS)".
    calendar_scope(...)   §11.4  35% on a Fed hike in a window containing no
                                 scheduled FOMC meeting. NOTE, never REJECT:
                                 suppressing it would hide a calibration
                                 failure that belongs on the arm's score.
    complementarity(...)  §11.5  resolution required coordinates AND
                                 protocols; the failure condition dropped
                                 coordinates. Both can fail at once and the
                                 row has no verdict. RPAS 4.03 tests that a
                                 failure condition EXISTS, not that it
                                 complements.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REG_PATH = HERE / "registers.json"
SCHEMA = "registers/1.0"

_CACHE: dict | None = None


# ---------------------------------------------------------------- loading

def load(path: Path | None = None) -> dict:
    global _CACHE
    if _CACHE is not None and path is None:
        return _CACHE
    p = path or REG_PATH
    if not p.exists():
        raise FileNotFoundError(
            f"registers.py: {p} not found. The gates fail OPEN without it — "
            "a missing register must never silently pass rows as clean.")
    data = json.loads(p.read_text(encoding="utf-8"))
    if data.get("schema") != SCHEMA:
        raise ValueError(f"registers.py: schema {data.get('schema')!r} "
                         f"!= {SCHEMA!r}")
    if path is None:
        _CACHE = data
    return data


def canonical_bytes(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":")).encode("utf-8")


def digest(path: Path | None = None) -> str:
    return hashlib.sha256(canonical_bytes(load(path))).hexdigest()


def citation(path: Path | None = None) -> str:
    """What a row writes when it settles a term against this register."""
    return f"{SCHEMA}@{digest(path)[:16]}"


# ---------------------------------------------------------------- sides

def side_of(bias: str) -> str:
    """Camp label -> side, register-of-record version. Mirrors tg_cluster."""
    table = load()["registers"]["sides"]["label_to_side"]
    b = (bias or "").strip().lower()
    camp = b.split()[0] if b else ""
    return table.get(camp) or table.get(b) or ("UNMAPPED:" + (camp or "?"))


def sides() -> list:
    return list(load()["registers"]["sides"]["distinct_sides"])


# ---------------------------------------------------------------- geo

_WORD = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'.\-]*")


def _geo_index() -> dict:
    """surface form (lower) -> canonical entity name."""
    g = load()["registers"]["geo"]
    idx: dict[str, str] = {}
    for c in g["countries"]:
        idx[c["name"].lower()] = c["name"]
        for k in ("common_name", "official_name"):
            if c.get(k):
                idx[c[k].lower()] = c["name"]
    for s in g["us_subdivisions"]:
        idx[s["name"].lower()] = s["name"]
    for surface, target in g["aliases"].items():
        idx[surface.lower()] = target
    for surface, target in g.get("demonyms", {}).items():
        idx[surface.lower()] = target
    gz = g.get("gazetteer", {})
    for place, zone in gz.get("place_zone", {}).items():
        idx[place] = "zone:" + zone
    for surface, canon in gz.get("place_aliases", {}).items():
        z = gz.get("place_zone", {}).get(canon)
        if z:
            idx[surface] = "zone:" + z
    return idx


def _region_index() -> dict:
    return {k.lower(): v for k, v in load()["registers"]["geo"]["regions"].items()}


def entities(text: str, expand_regions: bool = True) -> set:
    """Canonical geographic entities named in `text`.

    Longest-match over a lowercased surface index. Regions expand to their
    asserted members, and the region name is kept alongside so a reader can
    see which assertion did the work.
    """
    t = " " + re.sub(r"[^\w\s'.\-]+", " ", (text or "").lower()) + " "
    t = re.sub(r"\s+", " ", t)
    found: set[str] = set()

    for surface, members in _region_index().items():
        if f" {surface} " in t:
            found.add("region:" + surface)
            if expand_regions:
                found.update(members)

    idx = _geo_index()
    for surface, canon in idx.items():
        s = surface.lower()
        if len(s) <= 2 and s not in ("us", "uk"):
            continue                      # two-letter codes are too noisy
        if f" {s} " in t:
            found.add(canon)
    return found


def _lift(ents: set) -> set:
    """Expand entities upward: a US state implies the United States, a zone
    token implies its countries. Containment runs on both sides or the test
    reads 'United States' vs 'Florida' as disjoint."""
    g = load()["registers"]["geo"]
    parents = g.get("parents", {})
    zones = g.get("zone_countries", {})
    out = set(ents)
    for e in ents:
        if e in parents:
            out.add(parents[e])
        if e.startswith("zone:"):
            out.update(zones.get(e[5:], []))
    return out


_LOCATIVE = re.compile(
    r"\b(?:in|into|near|across|within|throughout|inside|around|over|at|on|"
    r"from|to|targeting|striking|based in|located in|territory of|"
    r"airspace of|waters of|coast of|border with)\b", re.I)


def locational_entities(text: str) -> set:
    """Entities the claim places an EVENT in, not entities it names
    institutionally. 'a wildfire IN Arizona' is locational; 'the U.S. Senate
    votes' is not, and 'ICE Brent crude' has no geography at all. Without this
    distinction the check reads an on-point Senate row as disjoint because one
    shotgun citation mentioned Ukraine."""
    # Collapse single-letter abbreviations FIRST: "U.S. Southwest" otherwise
    # ends the span at "U." and every entity after it is lost. This bug ate
    # the finding the check was built for, twice.
    t = re.sub(r"\b([A-Za-z])\.", r"\1", (text or ""))
    t = re.sub(r"\s+", " ", t)
    out: set = set()
    for m in _LOCATIVE.finditer(t):
        span = t[m.end():]
        # NOT a bare [.;] — "the U.S. Southwest (Arizona…)" splits at the
        # abbreviation's first period and loses every entity after it.
        span = re.split(r"\.\s|\.$|;|\bwith\b|\bbetween\b|\bby\b|"
                        r"\bthat\b|\bwhich\b|\bduring\b|\bfor\b", span,
                        maxsplit=1)[0][:160]
        out |= entities(span)
    return out


def geo_support(statement: str, resolution: str, cited_texts: list) -> dict:
    """§11.2. Do the cited items concern the geography the claim names?

    Returns {"verdict": OK | DISJOINT | NO_GEO | NO_CITES,
             "claim": [...], "cited": [...], "shared": [...], "reason": str}

    DISJOINT is the finding: the claim names entities, the cited record names
    entities, and the two sets do not intersect. Silence on either side is
    never a finding — an absent geography is not a wrong geography.
    """
    claim = {e for e in locational_entities(f"{statement} {resolution}")
             if not e.startswith("region:")}
    if not cited_texts:
        return {"verdict": "NO_CITES", "claim": sorted(claim), "cited": [],
                "shared": [], "reason": "no cited item text available"}
    per_item = [{e for e in entities(t) if not e.startswith("region:")}
                for t in cited_texts]
    cited = set().union(*per_item) if per_item else set()
    if not claim or not cited:
        return {"verdict": "NO_GEO", "claim": sorted(claim),
                "cited": sorted(cited), "shared": [],
                "reason": "claim or cited record names no registered entity — "
                          "silence is not a wrong geography"}
    lifted_claim = _lift(claim)
    shared = lifted_claim & _lift(cited)
    if shared:
        return {"verdict": "OK", "claim": sorted(claim), "cited": sorted(cited),
                "shared": sorted(shared), "reason": ""}
    # An item naming no geography abstains; it is not evidence against. Only
    # when EVERY geo-naming item points somewhere else is the record disjoint.
    speaking = [s_ for s_ in per_item if s_]
    if not speaking:
        return {"verdict": "NO_GEO", "claim": sorted(claim), "cited": [],
                "shared": [],
                "reason": "no cited item names a registered entity"}
    return {
        "verdict": "DISJOINT", "claim": sorted(claim), "cited": sorted(cited),
        "shared": [],
        "reason": ("cited items name " + ", ".join(sorted(cited)[:6]) +
                   "; the claim is about " + ", ".join(sorted(claim)[:6]) +
                   " — not one cited item concerns the geography of this "
                   "claim, so the declared prior is a prior about somewhere "
                   "else"),
    }


# ---------------------------------------------------------------- venues

def _venue_alias_index() -> dict:
    idx = {}
    for v in load()["registers"]["venues"]["named"]:
        idx[v["name"].lower()] = v["id"]
        for a in v.get("aliases", []):
            idx[a.lower()] = v["id"]
    return idx


def named_venues(text: str) -> set:
    t = " " + re.sub(r"[^\w\s'.\-]+", " ", (text or "").lower()) + " "
    t = re.sub(r"\s+", " ", t)
    return {vid for alias, vid in _venue_alias_index().items()
            if f" {alias} " in t}


# threshold / geography / actor 'or's that the venue rule must not see
_MASK = re.compile(
    r"\b(?:at|on)\s+or\s+(?:above|below|before|after)\b"
    r"|\bor\s+(?:more|greater|higher|later|fewer|less|larger|lower|above|below)\b"
    r"|\bor\s+equal\b", re.I)


def venue_scope(resolution: str) -> dict:
    """§11.3, re-anchored on VENUE NOUNS rather than on disjunction.

    Returns {"verdict": OK | DISJUNCT | EXEMPLARY | NO_VENUE,
             "named": [...], "reason": str}

    DISJUNCT   both sides of an `or` carry a venue noun or a named venue.
    EXEMPLARY  a venue appears but a softener ("e.g.", "such as") makes it an
               example, so the adjudicator still chooses. This is the half the
               old rule missed entirely.
    NO_VENUE   nothing venue-shaped at all.
    """
    reg = load()["registers"]["venues"]
    nouns = [n.lower() for n in reg["class_nouns"]]
    markers = [m.lower() for m in reg["exemplary_markers"]]
    res = resolution or ""
    masked = _MASK.sub(" ", res)
    low = masked.lower()
    found = named_venues(res)

    def _venueish(fragment: str) -> bool:
        f = " " + re.sub(r"\s+", " ", fragment.lower().strip()) + " "
        if any(f" {a} " in f for a in _venue_alias_index()):
            return True
        return any(f" {n} " in f or f.rstrip().endswith(" " + n)
                   for n in nouns)

    disj = []
    # modifier disjunction over a shared venue head: "a U.S. government or
    # international disaster alert system". Two adjectives pick out two
    # different systems; the noun being shared does not make it one venue.
    _nounalt = "|".join(re.escape(n) for n in sorted(nouns, key=len, reverse=True))
    _mod = re.search(
        r"\b(?:a|an|the)\s+([\w.\-]+(?:\s+[\w.\-]+){0,3})\s+or\s+"
        r"([\w.\-]+(?:\s+[\w.\-]+){0,3}?)\s+(?:" + _nounalt + r")\b",
        low)
    if _mod and not _MASK.search(_mod.group(0)):
        disj.append((_mod.group(1)[-45:], _mod.group(2)[:45]))
    for m in re.finditer(r"\bor\b", low):
        left = low[max(0, m.start() - 90):m.start()]
        right = low[m.end():m.end() + 90]
        # clause boundaries: an 'or' does not reach across them
        left = re.split(r"[;.]|\bif\b|\bwhen\b", left)[-1]
        right = re.split(r"[;.]|\bwith\b|\bbetween\b", right)[0]
        if _venueish(left) and _venueish(right):
            disj.append((left.strip()[-45:], right.strip()[:45]))

    # EXEMPLARY only when the softener attaches to the VENUE. "(e.g., cabinet
    # member, senator, or agency head)" softens the claim's subject class,
    # not the source of record, and firing on it rejects the right rows for
    # the wrong reason -- the exact failure shape 11.3 documents. Attachment
    # site = the text immediately BEFORE the marker (or before the paren the
    # marker opens): softeners postmodify their head. Counted venue classes
    # ("at least two independent outlets, including X") are exempt -- the
    # count defines the class and examples do not reopen adjudicator choice.
    _counted = re.compile(
        r"\b(?:two|three|four|\d+)\s+(?:or more\s+)?(?:major\s+|"
        r"independent\s+|international\s+|credible\s+|financial\s+)*"
        r"(?:news\s+)?(?:sources|outlets|agencies|wire services)\b")
    marker = None
    for mk in markers:
        for mm in re.finditer(re.escape(mk), low):
            pre_at = mm.start()
            popen = low.rfind("(", max(0, mm.start() - 4), mm.start())
            if popen != -1:
                pre_at = popen
            head = low[max(0, pre_at - 55):pre_at]
            if _counted.search(head):
                continue
            if _venueish(head):
                marker = mk
                break
        if marker:
            break

    if disj:
        l, r = disj[0]
        return {"verdict": "DISJUNCT", "named": sorted(found),
                "reason": (f"resolution offers alternative VENUES joined by "
                           f"'or' (\u2026{l} | or | {r}\u2026) — name ONE "
                           f"source of record or define the venue class; an "
                           f"adjudicator must not choose the venue after the "
                           f"fact")}
    if marker and (found or any(f" {n} " in " " + low + " " for n in nouns)):
        return {"verdict": "EXEMPLARY", "named": sorted(found),
                "reason": (f"the named venue is introduced by '{marker}', "
                           f"which makes it an example rather than the source "
                           f"of record — the adjudicator still chooses. Strike "
                           f"the softener or name the class exhaustively")}
    if not found and not any(f" {n} " in " " + low + " " for n in nouns):
        return {"verdict": "NO_VENUE", "named": [],
                "reason": ("resolution names no source of record — a stranger "
                           "must know exactly where to look on the deadline "
                           "date")}
    return {"verdict": "OK", "named": sorted(found), "reason": ""}


# ---------------------------------------------------------------- calendars

_DATE = re.compile(r"(20\d\d)-(\d\d)-(\d\d)")


_EXPLICIT_WINDOW = re.compile(
    r"\bbetween\s+(20\d\d-\d\d-\d\d)\s+and\s+(20\d\d-\d\d-\d\d)\b", re.I)

# A DECISION ACT inside the window. A claim about a persisting STATE ("the
# upper bound is above 3.75 percent on 2026-10-30") needs no meeting: the
# range set in July is still in effect in October. Conflating the two is what
# made this test wrong on three of its first five flags.
_DECISION_VERB = re.compile(
    r"\b(?:announc\w*|issu\w*|rais\w*|hik\w*|cut\w*|lower\w*|increas\w*|"
    r"reduc\w*|set|sets|vot\w*|decid\w*|deliver\w*|mov\w*)\b", re.I)
_STATE_SHAPE = re.compile(
    r"\b(?:is|are|remains?|stays?|holds?|stands?|equals?)\s+(?:above|below|at|"
    r"unchanged|higher|lower|between)\b", re.I)


def _window(statement: str, resolution: str) -> tuple:
    """Prefer an EXPLICIT 'between A and B' event window. Bare dates are
    usually the deadline, and a deadline is not a window: 'the September FOMC
    statement published on or before 2026-09-30' is satisfied by the Sept
    15-16 meeting, which sits before that date, not inside a point."""
    m = _EXPLICIT_WINDOW.search(f"{statement} {resolution}")
    if m:
        return m.group(1), m.group(2)
    return None, None


def scheduled_bodies(text: str) -> set:
    t = " " + re.sub(r"[^\w\s'.\-]+", " ", (text or "").lower()) + " "
    t = re.sub(r"\s+", " ", t)
    out = set()
    for bid, b in load()["registers"]["calendars"]["bodies"].items():
        if any(f" {term.lower()} " in t for term in b.get("terms", [])):
            out.add(bid)
    return out


def calendar_scope(statement: str, resolution: str) -> dict:
    """§11.4. Does the row's window contain a scheduled meeting of a body it names?

    Returns {"verdict": OK | PRECLUDED | UNPOPULATED | UNVERIFIED | NA,
             "body": id|None, "window": [start, end], "reason": str}

    PRECLUDED is advisory by ruling: the arm should be SCORED for pricing a
    ~1% event at 35%, not protected from it. And the register cannot verify
    itself — every calendar ships `verified: false`, so a PRECLUDED verdict
    carries the provenance of the dates that produced it.
    """
    bodies = scheduled_bodies(f"{statement} {resolution}")
    if not bodies:
        return {"verdict": "NA", "body": None, "window": [None, None],
                "reason": ""}
    bid = sorted(bodies)[0]
    b = load()["registers"]["calendars"]["bodies"][bid]
    both = f"{statement} {resolution}"
    if _STATE_SHAPE.search(both) or not _DECISION_VERB.search(both):
        return {"verdict": "NA", "body": bid, "window": [None, None],
                "reason": ("claim is about a persisting STATE, not a decision "
                           "act — a target range set at an earlier meeting is "
                           "still in effect between meetings, so no meeting "
                           "need fall inside the window")}
    start, end = _window(statement, resolution)
    if not start:
        return {"verdict": "NA", "body": bid, "window": [None, None],
                "reason": ("no explicit 'between A and B' event window — bare "
                           "dates are deadlines, and a deadline-bounded row is "
                           "satisfied by any meeting before it")}
    if not b.get("meetings"):
        return {"verdict": "UNPOPULATED", "body": bid, "window": [start, end],
                "reason": (f"{b['body']} is registered but its calendar is "
                           f"empty — the advisory refuses to fire rather than "
                           f"guess. Populate from {b['source_url']}")}
    if not re.search(r"\b(?:statement|decision|announcement|implementation "
                     r"note|minutes|policy statement|rate decision|meeting)\b",
                     both, re.I) and re.search(
                         r"\b(?:outlets?|news|report(?:s|ed|ing)?|coverage|"
                         r"publish\w*)\b", both, re.I):
        return {"verdict": "NA", "body": bid, "window": [start, end],
                "reason": ("row resolves on press reporting ABOUT the body, "
                           "not on an act OF the body — speeches, minutes and "
                           "balance-sheet releases fall between meetings, so "
                           "the calendar does not bound it")}
    hit = [m for m in b["meetings"]
           if not (m["end"] < start or m["start"] > end)]
    prov = ("dates UNVERIFIED against the body's own calendar; provenance: "
            + b.get("provenance", "?")) if not b.get("verified") else \
        f"verified {b.get('verified_on')} by {b.get('verified_by')}"
    if hit:
        return {"verdict": "OK", "body": bid, "window": [start, end],
                "reason": f"window contains {len(hit)} scheduled meeting(s); "
                          f"{prov}"}
    return {
        "verdict": "PRECLUDED", "body": bid, "window": [start, end],
        "reason": (f"window {start}..{end} contains NO scheduled meeting of "
                   f"{b['body']} — only an unscheduled inter-meeting action "
                   f"satisfies this row. "
                   + (b.get("unscheduled_note", "") + " ")
                   + prov),
    }


# ---------------------------------------------------------------- complementarity

_STOP = {
    "the", "a", "an", "of", "and", "or", "to", "in", "on", "at", "by", "for",
    "with", "from", "is", "are", "be", "been", "no", "not", "any", "all",
    "that", "this", "these", "those", "its", "it", "as", "if", "than", "then",
    "during", "between", "within", "inside", "window", "event", "true",
    "false", "resolves", "resolve", "otherwise", "such", "does", "do", "has",
    "have", "will", "shall", "both", "either", "neither", "one", "two",
    "more", "least", "over", "under", "per", "via", "close", "closes",
}


def _terms(text: str) -> set:
    return {w.lower() for w in _WORD.findall(text or "")
            if len(w) > 2 and w.lower() not in _STOP}


def complementarity(resolution: str, failure_condition: str) -> dict:
    """§11.5. Is the failure condition the negation of the resolution?

    Conservative by construction: it reports only the case where the
    resolution imposes requirements the failure condition drops, which is
    exactly the shape that leaves outcomes satisfying neither. Returns

        {"verdict": OK | GAP | NO_FC, "dropped": [...], "reason": str}

    This is a heuristic over content terms and it will not catch a semantic
    negation gap expressed in different vocabulary. It catches the printed
    one. State the limit rather than overclaiming the test.
    """
    if not (failure_condition or "").strip():
        return {"verdict": "NO_FC", "dropped": [],
                "reason": "no failure condition — RPAS 4.03"}
    r, f = _terms(resolution), _terms(failure_condition)
    dropped = sorted(r - f)
    # requirement-bearing terms only: a dropped adjective is noise, a dropped
    # noun that the resolution REQUIRES is the gap.
    # Only CONJUNCTIVE requirement clauses count. "naming X in field A or B"
    # is descriptive; "specifying A and B" imposes two conditions, and a
    # failure condition that negates only one of them leaves outcomes with no
    # verdict. Verbs restricted accordingly, and the clause must carry an
    # "and" — that is the exact shape of the finding this test exists for.
    # Trigger set narrowed after the KK25 sweep flagged 11 rows and 10 were
    # vocabulary variation, not dropped requirements. `specif\w+` matched the
    # ADJECTIVE "specific"; `including` enumerates examples (which is the
    # venue test's job, not this one); `lists` and `naming` are descriptive.
    # What is left imposes conditions.
    req = re.findall(r"\b(?:specify|specifies|specifying|specified|"
                     r"requir\w+|detailing|detailed|comprising|consisting|"
                     r"must\s+(?:also\s+)?(?:include|state|name))"
                     r"\s+([^.;]{0,140})", resolution, re.I)
    reqterms = set()
    for chunk in req:
        if not re.search(r"\band\b", chunk, re.I):
            continue
        reqterms |= _terms(chunk)
    hard = sorted(t for t in dropped if t in reqterms)
    if hard:
        return {
            "verdict": "GAP", "dropped": hard,
            "reason": ("the resolution requires " + ", ".join(hard) +
                       " and the failure condition does not mention "
                       + ("it" if len(hard) == 1 else "them") +
                       " — an outcome missing " +
                       ("it" if len(hard) == 1 else "them") +
                       " satisfies neither clause and the row has no verdict. "
                       "4.03 tests that a failure condition exists; it does "
                       "not test that it complements"),
        }
    return {"verdict": "OK", "dropped": dropped[:8], "reason": ""}


# ---------------------------------------------------------------- verify

def verify(repo: Path) -> int:
    """Drift against the tree + internal consistency. Non-zero on any FAIL."""
    reg = load()
    r = reg["registers"]
    fails, warns = [], []

    def ok(label, detail=""):
        print(f"  [OK]   {label}" + (f" — {detail}" if detail else ""))

    def fail(label, detail):
        fails.append(label)
        print(f"  [FAIL] {label} — {detail}")

    def warn(label, detail):
        warns.append(label)
        print(f"  [WARN] {label} — {detail}")

    print(f"registers.py verify · {SCHEMA} · {digest()[:16]}")

    # 1. sides drift against tg_cluster.py
    src = repo / "tg_cluster.py"
    if not src.exists():
        warn("sides drift", f"{src} not found; cannot compare")
    else:
        m = re.search(r"^SIDES\s*=\s*(\{.*?^\})",
                      src.read_text(encoding="utf-8"), re.S | re.M)
        if not m:
            fail("sides drift", "SIDES literal not found in tg_cluster.py")
        else:
            live = {str(k): str(v) for k, v in ast.literal_eval(m.group(1)).items()}
            held = r["sides"]["label_to_side"]
            if live == held:
                ok("sides drift", f"{len(held)} labels identical to tg_cluster")
            else:
                only_tree = sorted(set(live) - set(held))
                only_reg = sorted(set(held) - set(live))
                diff = sorted(k for k in set(live) & set(held)
                              if live[k] != held[k])
                fail("sides drift",
                     f"tree-only {only_tree} · register-only {only_reg} · "
                     f"disagree {diff}")

    # 2. venue resolver / lookup names must exist
    res_src = (repo / "resolvers.py")
    if res_src.exists():
        live_res = {m.group(1) for m in re.finditer(
            r"^def\s+resolve_([a-z0-9_]+)\s*\(",
            res_src.read_text(encoding="utf-8"), re.M)}
        bad = [v["id"] for v in r["venues"]["named"]
               if v.get("resolver") and v["resolver"] not in live_res]
        if bad:
            fail("resolver names", f"no resolve_* in resolvers.py for {bad}")
        else:
            ok("resolver names", f"{len(live_res)} resolvers, all references live")
    lk_src = (repo / "desk_lookup.py")
    if lk_src.exists():
        live_lk = {m.group(1) for m in re.finditer(
            r'sub\.add_parser\(\s*"([a-z0-9_]+)"',
            lk_src.read_text(encoding="utf-8"))}
        bad = [v["id"] for v in r["venues"]["named"]
               if v.get("lookup") and v["lookup"] not in live_lk]
        if bad:
            fail("lookup names", f"no desk_lookup subcommand for {bad}")
        else:
            ok("lookup names", f"{len(live_lk)} subcommands, all references live")

    # 3. region members must be registered entities
    known = set(_geo_index().values())
    bad = {reg_name: [m for m in members if m not in known]
           for reg_name, members in r["geo"]["regions"].items()}
    bad = {k: v for k, v in bad.items() if v}
    if bad:
        fail("region members", f"unregistered: {bad}")
    else:
        ok("region members", f"{len(r['geo']['regions'])} regions resolve")

    # 4. alias targets must be registered entities
    bad = [k for k, v in r["geo"]["aliases"].items() if v not in known]
    if bad:
        fail("geo aliases", f"targets not in ISO list: {bad}")
    else:
        ok("geo aliases", f"{len(r['geo']['aliases'])} aliases resolve")

    # 5. calendars disclose their own state
    for bid, b in r["calendars"]["bodies"].items():
        if not b.get("meetings"):
            warn(f"calendar:{bid}", "UNPOPULATED — advisory will not fire")
        elif not b.get("verified"):
            warn(f"calendar:{bid}",
                 f"{len(b['meetings'])} meetings, UNVERIFIED against "
                 f"{b['source_url']}")
        else:
            ok(f"calendar:{bid}", f"{len(b['meetings'])} meetings, verified")

    print(f"\n  {len(fails)} FAIL · {len(warns)} WARN")
    if warns and not fails:
        print("  WARNs are the register printing its own holes. That is the "
              "intended behaviour, not a defect to silence.")
    return 1 if fails else 0


# ---------------------------------------------------------------- selftest

def _fixtures() -> list:
    """Bound to the 2026-08-06 04:28Z run. SEALED cases are verbatim from
    ledger.json; the RECONSTRUCTED case is the rejected quake row, whose
    resolution text is not in the tree (kkr_raw_last.txt is gitignored and
    section II truncates at 140 chars) — its statement fragment is verbatim
    and its resolution is rebuilt from the KK24 finding. Labelled as such
    because a fixture that pretends to be evidence is worse than no fixture.
    """
    return [
        # -- venue_scope ------------------------------------------------
        dict(name="quake row, false POSITIVE of the old rule",
             kind="venue", provenance="RECONSTRUCTED",
             resolution=("A magnitude 6.0 or greater earthquake recorded in "
                         "the USGS Significant Earthquakes database with an "
                         "epicenter in Washington, Oregon, or Northern "
                         "California between 2026-08-20 and 2026-08-27."),
             expect="OK",
             why="one venue; the 'or's are a threshold and a geography"),
        dict(name="KKR-20260806-35, false NEGATIVE of the old rule",
             kind="venue", provenance="SEALED",
             resolution=("A wildfire in Arizona, New Mexico, or Nevada is "
                         "reported by a U.S. government or international "
                         "disaster alert system (e.g., GDACS) with a "
                         "containment status of 'under control' or "
                         "'contained' by 2026-09-05."),
             expect="DISJUNCT",
             why="genuine venue disjunction, softened by an e.g."),
        dict(name="S&P row, correctly rejected",
             kind="venue", provenance="RECONSTRUCTED",
             resolution=("The S&P 500 closing level as published by FRED or "
                         "a major exchange is above 7,800 on at least one "
                         "trading day between 2026-08-16 and 2026-08-23."),
             expect="DISJUNCT", why="two venues, correctly caught"),
        dict(name="KKR-20260806-04, clean single venue",
             kind="venue", provenance="SEALED",
             resolution=("A CISA KEV entry naming Gitea in vendorProject or "
                         "product carries a dateAdded value inside the "
                         "window. No such entry resolves false."),
             expect="OK", why="'or' joins two FIELDS of one catalog"),
        # -- geo_support ------------------------------------------------
        dict(name="KKR-20260806-35 citations",
             kind="geo", provenance="SEALED",
             statement=("Between 2026-08-25 and 2026-09-01, a verified "
                        "wildfire will be reported in the U.S. Southwest "
                        "(Arizona, New Mexico, or Nevada) with a containment "
                        "status of 'under control' or 'contained'."),
             resolution="",
             cited=["GDACS Green forest fire notification for Angola",
                    "GDACS Green forest fire notification for Zambia",
                    "GDACS Green forest fire notification for the Russian "
                    "Federation"],
             expect="DISJOINT", why="not one cited item concerns the US"),
        dict(name="KKR-20260806-10 citations (Kyiv)",
             kind="geo", provenance="SEALED",
             statement=("A Russian missile or drone strike on Kyiv city "
                        "kills at least 5 people in a single attack between "
                        "2026-08-06 and 2026-10-31."),
             resolution="",
             cited=["Ukraine reports overnight drone strikes on Kyiv",
                    "Russian Federation defence ministry claims strikes on "
                    "Ukraine military targets"],
             expect="OK", why="claim and record share Ukraine"),
        # -- calendar_scope ---------------------------------------------
        dict(name="KKR-20260806-33, Fed hike in a scheduled gap",
             kind="calendar", provenance="SEALED",
             statement=("Between 2026-08-22 and 2026-08-29, the U.S. Federal "
                        "Reserve will announce a rate hike of at least 25 "
                        "basis points in a public statement."),
             resolution=("The Federal Reserve issues a public statement "
                         "announcing a 25 basis point or greater increase in "
                         "the federal funds rate between 2026-08-22 and "
                         "2026-08-29."),
             expect="PRECLUDED", why="July-September FOMC gap"),
        dict(name="a September FOMC window",
             kind="calendar", provenance="SYNTHETIC",
             statement=("Between 2026-09-14 and 2026-09-18 the FOMC "
                        "announces a rate cut."),
             resolution="The Federal Open Market Committee statement dated "
                        "between 2026-09-14 and 2026-09-18 announces a cut.",
             expect="OK", why="contains the Sept 15-16 meeting"),
        dict(name="an ECB row, register unpopulated",
             kind="calendar", provenance="SYNTHETIC",
             statement=("Between 2026-09-01 and 2026-09-30 the European "
                        "Central Bank Governing Council cuts the deposit "
                        "facility rate."),
             resolution="An ECB Governing Council decision dated in the "
                        "window lowers the deposit facility rate.",
             expect="UNPOPULATED", why="refuses to guess at a calendar"),
        # -- complementarity --------------------------------------------
        dict(name="KKR-20260806-31, the printed gap",
             kind="comp", provenance="SEALED",
             resolution=("A joint statement issued by the foreign ministries "
                         "of Iran and Oman confirms the establishment of a "
                         "maritime coordination agreement for the Strait of "
                         "Hormuz, specifying route coordinates and "
                         "operational protocols."),
             failure=("No joint statement from the foreign ministries of Iran "
                      "and Oman confirms a maritime coordination agreement "
                      "for the Strait of Hormuz during the event window."),
             expect="GAP", why="'specifying route coordinates' dropped"),
        dict(name="KKR-20260806-04, clean complement",
             kind="comp", provenance="SEALED",
             resolution=("A CISA KEV entry naming Gitea in vendorProject or "
                         "product carries a dateAdded value inside the "
                         "window. No such entry resolves false."),
             failure=("The KEV catalog holds no Gitea entry with a dateAdded "
                      "value inside the window."),
             expect="OK", why="failure is the negation"),
    ]


def selftest() -> int:
    passed = failed = 0
    print(f"registers.py selftest · {citation()}\n")
    for fx in _fixtures():
        k = fx["kind"]
        if k == "venue":
            got = venue_scope(fx["resolution"])
        elif k == "geo":
            got = geo_support(fx["statement"], fx.get("resolution", ""),
                              fx["cited"])
        elif k == "calendar":
            got = calendar_scope(fx["statement"], fx["resolution"])
        else:
            got = complementarity(fx["resolution"], fx["failure"])
        good = got["verdict"] == fx["expect"]
        passed += good
        failed += not good
        mark = "PASS" if good else "FAIL"
        print(f"  [{mark}] {k:8} {fx['provenance']:13} {fx['name']}")
        print(f"         expect {fx['expect']:11} got {got['verdict']}"
              f"   ({fx['why']})")
        if not good and got.get("reason"):
            print(f"         reason: {got['reason'][:160]}")
    print(f"\n  {passed} pass · {failed} fail")
    return 1 if failed else 0


# ---------------------------------------------------------------- row check

def check_row(row_id: str, repo: Path) -> int:
    led = json.loads((repo / "ledger.json").read_text(encoding="utf-8"))
    rows = led["projections"] if isinstance(led, dict) else led
    row = next((r for r in rows if str(r.get("id")) == row_id), None)
    if row is None:
        print(f"registers.py: row {row_id} not in ledger.json", file=sys.stderr)
        return 2
    s = row.get("statement", "")
    res = row.get("resolution", "")
    fc = row.get("failure_condition", "")
    print(f"{row_id} · {row.get('model')} · {row.get('probability')}% · "
          f"{row.get('domain')}")
    print(f"  register {citation()}")
    v = venue_scope(res)
    print(f"  venue        {v['verdict']:11} {v['reason'][:150]}")
    c = calendar_scope(s, res)
    print(f"  calendar     {c['verdict']:11} {c['reason'][:150]}")
    k = complementarity(res, fc)
    print(f"  complement   {k['verdict']:11} {k['reason'][:150]}")
    print(f"  geo(claim)   {sorted(e for e in entities(s + ' ' + res) if not e.startswith('region:'))}")
    print("  geo(cited)   needs the source report; run inside kkr.py where "
          "cited item text is resolved")
    return 0


# ---------------------------------------------------------------- cli

def show() -> int:
    r = load()["registers"]
    print(f"{SCHEMA} · generated {load()['generated']} · {citation()}")
    print(f"  sides      {len(r['sides']['label_to_side'])} labels -> "
          f"{len(r['sides']['distinct_sides'])} sides: "
          f"{' '.join(r['sides']['distinct_sides'])}")
    print(f"  geo        {len(r['geo']['countries'])} countries · "
          f"{len(r['geo']['us_subdivisions'])} US subdivisions · "
          f"{len(r['geo']['aliases'])} aliases · "
          f"{len(r['geo']['regions'])} regions")
    named = r["venues"]["named"]
    print(f"  venues     {len(named)} named · "
          f"{sum(1 for v in named if v.get('resolver'))} with a resolver · "
          f"{sum(1 for v in named if v.get('lookup'))} with a keyless lookup")
    for v in named:
        tail = []
        if v.get("resolver"):
            tail.append("resolver:" + v["resolver"])
        if v.get("lookup"):
            tail.append("lookup:" + v["lookup"])
        print(f"             {v['id']:18} {v['name'][:44]:46}"
              f"{' '.join(tail)}")
    for bid, b in r["calendars"]["bodies"].items():
        state = ("UNPOPULATED" if not b["meetings"]
                 else ("UNVERIFIED" if not b["verified"] else "verified"))
        print(f"  calendar   {bid:6} {b['body'][:44]:46}"
              f"{len(b['meetings'])} meetings, {state}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="the desk's register of record")
    ap.add_argument("cmd", choices=["hash", "show", "verify", "selftest",
                                    "check"])
    ap.add_argument("--repo", default=str(HERE))
    ap.add_argument("--row")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    if a.cmd == "hash":
        print(digest())
        print(citation())
        return 0
    if a.cmd == "show":
        return show()
    if a.cmd == "verify":
        return verify(repo)
    if a.cmd == "selftest":
        return selftest()
    if a.cmd == "check":
        if not a.row:
            print("registers.py check needs --row ID", file=sys.stderr)
            return 2
        return check_row(a.row, repo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
