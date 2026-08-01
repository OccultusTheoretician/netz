#!/usr/bin/env python3
"""
fc_pass.py — the 4.02f content pass over open entries lacking a failure
condition. Two modes, review between them:

    python fc_pass.py --draft      write FC_REVIEW.md + fc_proposals.json
    python fc_pass.py --apply all              apply every proposal
    python fc_pass.py --apply KKR-...,KKR-...  apply named ids only

The proposal is always the mechanical negation of the row's own resolution
basis — no new facts, no invented specifics: "the named source does not report
the stated outcome by the deadline." Editing a proposal in fc_proposals.json
before applying is the intended workflow.

Applies ONLY empty -> value on OPEN rows (the 4.02f window the ledger's
disclosure grants and rpas_verify encodes). It never touches keyed_keyless:
the determination is a judgment about what priors the forecaster held, and a
script holds none. Rows write through kkr.save_ledger, so the envelope stamps
and the post-cutover seal hook run untouched; pre-cutover rows stay bare per
the finding.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import kkr

HERE = Path(__file__).resolve().parent
PROPOSALS = HERE / "fc_proposals.json"
REVIEW = HERE / "FC_REVIEW.md"


# Abbreviations whose internal period is not a sentence end. Without this
# guard the splitter cut "A U.S. presidential candidate ..." to "A U.S",
# yielding 13 truncated failure conditions on the 2026-07-30 pass.
_ABBR = (r"U\.S|U\.K|E\.U|U\.N|N\.Y|D\.C|i\.e|e\.g|etc|approx|est|no|vs"
         r"|Inc|Corp|Ltd|Co|Mr|Mrs|Ms|Dr|St|Mt|Ft|Sen|Rep|Gov|Gen|Lt|Col"
         r"|Adm|Capt|Sgt|Jr|Sr|a\.m|p\.m|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep"
         r"|Sept|Oct|Nov|Dec")
_GUARD = "\x00"


def first_sentence(text: str) -> str:
    """Split on the first real sentence end, protecting abbreviations."""
    t = (text or "").strip()
    t = re.sub(r"\b(" + _ABBR + r")\.", lambda m: m.group(1) + _GUARD, t,
               flags=re.I)
    first = re.split(r"(?<=[.!?])\s", t)[0]
    return first.replace(_GUARD, ".")


def miss_branch(resolution: str) -> str:
    """A 'hit if X, miss if Y' basis already states its own failure. Return Y.

    Negating such a basis produced self-contradicting text ("... hit if a
    different officer is named ... does not show the stated outcome"), so the
    stated miss branch is used verbatim instead. 11 rows on the 2026-07-30
    pass carried this shape.
    """
    m = re.search(r"\bmiss\s+(?:if\s+)?(.+?)\s*$", (resolution or "").strip(),
                  flags=re.I | re.S)
    if not m:
        return ""
    branch = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")
    return branch


def source_clause(resolution: str) -> str:
    first = first_sentence(resolution)
    first = re.sub(r"^resolved\s+(from|via|by|using)\s+", "", first,
                   flags=re.I).strip().rstrip(".")
    first = re.sub(r"\s+on\s+\d{4}-\d{2}-\d{2}$", "", first)
    # A bare URL is machinery, not prose the published face should carry.
    first = re.sub(r"https?://\S+", "the source of record", first)
    first = re.sub(r"\s*:\s*$", "", first).strip(" :")
    return first or "the named source in the resolution basis"


def condition_clause(resolution: str) -> str:
    """The Yes-if branch: the thing that must HOLD for a hit.

    The R2 manual arms write a two-sentence basis - venue first, condition
    second - so taking the first sentence returned a bare source of record
    and dropped the condition. A source cannot be met; a condition can.
    """
    t = re.sub(r"\s+", " ", (resolution or "").strip())
    m = re.search(r"\b(?:yes|hit)\s+if\s+(.+)$", t, flags=re.I)
    if not m:
        return ""
    body = m.group(1).strip()
    # drop the explicit otherwise-branch; the frame already states the miss
    body = re.sub(r"[;,]?\s*otherwise\s+(?:no|NO)\b.*$", "", body,
                  flags=re.I).strip()
    return body.rstrip(". ").strip()


def propose(e: dict) -> str:
    deadline = e.get("deadline", "the deadline")
    branch = miss_branch(e.get("resolution", ""))
    if branch:
        if branch.lower() in ("otherwise", "not otherwise", "in any other case"):
            return (f"the resolution basis does not report the stated outcome "
                    f"in the window; absence at {deadline} scores this entry "
                    f"a MISS.")
        return (f"{branch}, as read from the resolution basis on {deadline}; "
                f"that reading scores this entry a MISS.")
    # One frame that stays grammatical whether the basis names a SOURCE
    # ("a public notice from the Treasury") or states the CONDITION itself
    # ("the yield exceeds 4.8% on 2026-07-29"). The earlier template assumed
    # the former and produced "<whole condition> does not show the stated
    # outcome", which read as nonsense on the majority of rows.
    res = e.get("resolution", "")
    cond = condition_clause(res)
    if cond:
        src = source_clause(res)
        # If the condition already sits in the first sentence, the source
        # clause is the same text - state it once.
        tail = ""
        if src and src.lower() not in cond.lower() \
                and cond.lower() not in src.lower():
            tail = f" as read from {src}"
        return (f"the condition stated in this entry's resolution basis — "
                f"{cond} — is not met on or before {deadline}{tail}; "
                f"absence at the deadline scores this entry a MISS.")
    return (f"the condition stated in this entry's resolution basis — "
            f"{source_clause(res)} — is not met on or "
            f"before {deadline}; absence at the deadline scores this entry "
            f"a MISS.")


def cmd_draft() -> int:
    rows = kkr.load_ledger()["projections"]
    def _empty(v):
        v = str(v or "").strip()
        return not v or v.lower().startswith("unset")
    targets = [e for e in rows if e.get("status") == "open"
               and _empty(e.get("failure_condition"))]
    props = {e["id"]: propose(e) for e in targets}
    PROPOSALS.write_text(json.dumps(props, ensure_ascii=False, indent=2),
                         encoding="utf-8")
    lines = [f"# FAILURE-CONDITION REVIEW — {len(targets)} open entries, "
             f"drafted {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             "",
             "Each proposal is the mechanical negation of the row's own "
             "resolution basis. Edit fc_proposals.json where a row needs a "
             "sharper miss, then `python fc_pass.py --apply all` (or a "
             "comma-list of ids). Keyed/keyless stays yours; this pass "
             "touches nothing else.", ""]
    for e in targets:
        lines += [f"## {e['id']} · {e.get('model')} · deadline "
                  f"{e.get('deadline')}",
                  f"**statement:** {e.get('statement','')[:160]}",
                  f"**proposed fc:** {props[e['id']]}", ""]
    REVIEW.write_text("\n".join(lines), encoding="utf-8")
    print(f"drafted {len(targets)} proposals → {PROPOSALS.name}, "
          f"{REVIEW.name}")
    return 0


def cmd_apply(which: str) -> int:
    props = json.loads(PROPOSALS.read_text(encoding="utf-8-sig"))
    ids = set(props) if which == "all" else {i.strip()
                                            for i in which.split(",")}
    data = kkr.load_ledger()
    n = skipped = 0
    for e in data["projections"]:
        if e.get("id") not in ids:
            continue
        cur = str(e.get("failure_condition", "")).strip()
        if e.get("status") != "open" or (cur and not
                                         cur.lower().startswith("unset")):
            skipped += 1
            continue
        e["failure_condition"] = props[e["id"]]
        n += 1
    kkr.save_ledger(data)
    print(f"applied {n} failure condition(s); skipped {skipped} "
          f"(not open, or already filled). Envelope restamped by "
          f"save_ledger; copy to docs/ and commit both. Keyed/keyless "
          f"determinations remain undone — they are the operator's judgment "
          f"(RPAS 4.02f), and any row resolving without one is KEYED by "
          f"rule (4.03).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--draft", action="store_true")
    g.add_argument("--apply")
    a = ap.parse_args()
    return cmd_draft() if a.draft else cmd_apply(a.apply)


if __name__ == "__main__":
    sys.exit(main())
