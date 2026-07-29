#!/usr/bin/env python3
"""
guest_gate.py — the mechanical gate for Guest Kalls, run by CI on issue open.

Reads the issue form from env, parses the structured sections, runs the SAME
validate_projection the desk's own arms face, then the published policy in
guest_policy.json. Writes:

    gate_verdict.json   {"accept": bool, "reasons": [...], "parsed": {...}}
    gate_comment.md     the comment CI posts on the issue, verdict either way

Rejections carry every reason, because the gate publishing its rejections is
the brand. This script ingests nothing and commits nothing — acceptance only
labels the issue for the operator, whose `seal` label is the sole ingestion
path (guest_seal.py).

Env in: ISSUE_BODY, ISSUE_AUTHOR, AUTHOR_CREATED_AT (ISO), OPEN_GUEST_COUNT.
Reads: ledger.json (per-login sealed/resolved counts, today's seal count),
guest_policy.json.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from kkr import validate_projection

HERE = Path(__file__).resolve().parent
FIELDS = ["Statement", "Probability (percent, 5-95)", "Deadline (YYYY-MM-DD)",
          "Resolution basis", "Failure condition",
          "Keyed or keyless (RPAS 4.02f)", "Keyed/keyless rationale"]
KEYMAP = {"Statement": "statement",
          "Probability (percent, 5-95)": "probability",
          "Deadline (YYYY-MM-DD)": "deadline",
          "Resolution basis": "resolution",
          "Failure condition": "failure_condition",
          "Keyed or keyless (RPAS 4.02f)": "keyed_keyless",
          "Keyed/keyless rationale": "keyed_keyless_rationale"}


def parse_form(body: str) -> dict:
    """GitHub issue forms render as '### Label\\n\\nvalue' blocks."""
    out = {}
    parts = re.split(r"^### ", body, flags=re.M)
    for part in parts:
        lines = part.splitlines()
        if not lines:
            continue
        label = lines[0].strip()
        value = "\n".join(lines[1:]).strip()
        if value == "_No response_":
            value = ""
        if label in KEYMAP:
            out[KEYMAP[label]] = value
    return out


def main() -> int:
    body = os.environ.get("ISSUE_BODY", "")
    author = os.environ.get("ISSUE_AUTHOR", "").strip()
    created = os.environ.get("AUTHOR_CREATED_AT", "")
    open_count = int(os.environ.get("OPEN_GUEST_COUNT", "0") or 0)

    policy = json.loads((HERE / "guest_policy.json").read_text(encoding="utf-8"))
    reasons = []
    p = parse_form(body)

    for k in ("statement", "probability", "deadline", "resolution",
              "failure_condition", "keyed_keyless", "keyed_keyless_rationale"):
        if not p.get(k, "").strip():
            reasons.append(f"form field missing or empty: {k}")

    # Normalize probability to int percent.
    try:
        p["probability"] = int(str(p.get("probability", "")).strip().rstrip("%"))
    except ValueError:
        reasons.append(f"probability {p.get('probability')!r} is not a whole "
                       f"percent")
        p["probability"] = 0

    if str(p.get("keyed_keyless", "")).lower() not in ("keyed", "keyless"):
        reasons.append("keyed/keyless must be exactly 'keyed' or 'keyless' "
                       "(RPAS 4.02f, decided before sealing)")
    else:
        p["keyed_keyless"] = p["keyed_keyless"].lower()

    # The same gate the desk's arms face — minus the one KKR-pipeline rule
    # that cannot apply: report-grounding citations. A model arm must cite
    # the battle report it forecast from; a guest has no report, and their
    # grounding is the named public instrument in the resolution basis,
    # enforced above by the policy's instrument classes.
    if not reasons:
        w = policy["deadline_window_days"]
        gate = {"statement": p["statement"], "resolution": p["resolution"],
                "deadline": p["deadline"], "probability": p["probability"],
                "domain": "guest"}
        reasons.extend(r for r in
                       validate_projection(gate, min_days=w["min"],
                                           max_days=w["max"])
                       if r != "no grounding citations to the report record")

    # Published policy.
    if author:
        if created:
            try:
                age_days = (datetime.now(timezone.utc) -
                            datetime.fromisoformat(created.replace("Z", "+00:00"))
                            ).days
                if age_days < policy["min_account_age_days"]:
                    reasons.append(
                        f"account age {age_days}d is under the published "
                        f"{policy['min_account_age_days']}d floor "
                        f"(guest_policy.json) — resubmit when it isn't")
            except ValueError:
                reasons.append("account creation date unreadable — gate "
                               "cannot apply the age floor; rejecting rather "
                               "than waiving a published rule")
        if open_count > policy["max_open_submissions_per_account"]:
            reasons.append(
                f"{open_count} open submissions from this account exceeds the "
                f"published cap of {policy['max_open_submissions_per_account']}")
        try:
            rows = json.loads((HERE / "ledger.json").read_text(
                encoding="utf-8")).get("projections", [])
            arm = f"guest/{author}"
            mine = [e for e in rows if e.get("model") == arm]
            resolved = [e for e in mine if e.get("status") in ("hit", "miss")]
            if (not resolved and
                    len(mine) >= policy["max_sealed_until_first_resolution"]):
                reasons.append(
                    f"{len(mine)} sealed and none resolved yet — the published "
                    f"cap is {policy['max_sealed_until_first_resolution']} "
                    f"until your first resolution lands. The record paces "
                    f"itself; so do its guests.")
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            sealed_today = sum(1 for e in rows
                               if str(e.get("model", "")).startswith("guest/")
                               and str(e.get("sealed_at", ""))[:10] == today)
            if sealed_today >= policy["global_daily_seal_cap"]:
                reasons.append(
                    f"the desk's global cap of "
                    f"{policy['global_daily_seal_cap']} guest seals today is "
                    f"reached — the queue holds; nothing about your "
                    f"submission is rejected on content")
        except Exception as e:
            reasons.append(f"ledger unreadable for policy checks ({e}) — "
                           f"failing closed")

    # Refused shapes, minimally and printed.
    low = (p.get("statement", "") + " " + p.get("resolution", "")).lower()
    if "retroprescientaudit" in low or "this desk" in low or "nebelkr" in low:
        reasons.append("resolution depends on this desk's own conduct — "
                       "refused shape (guest_policy.json)")

    accept = not reasons
    verdict = {"accept": accept, "reasons": reasons, "author": author,
               "parsed": p,
               "gated_at": datetime.now(timezone.utc)
               .strftime("%Y-%m-%dT%H:%M:%SZ")}
    (HERE / "gate_verdict.json").write_text(
        json.dumps(verdict, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = []
    if accept:
        lines.append("**GATE: PASSED.** Every mechanical check and every "
                     "published policy rule cleared.")
        lines.append("")
        lines.append(f"Parsed as — statement: “{p['statement'][:120]}”… · "
                     f"p={p['probability']}% · deadline {p['deadline']} · "
                     f"{p['keyed_keyless']}.")
        lines.append("")
        lines.append("What happens next: the operator reviews and applies the "
                     "`seal` label — the only path into the ledger. On "
                     "sealing you get the entry id, the seal hash, and the "
                     "one-line command that verifies it from the public URL. "
                     "The desk's clock, not yours; there is no deadline for "
                     "the operator and no appeal to speed.")
    else:
        lines.append(f"**GATE: REJECTED** — {len(reasons)} reason(s), printed "
                     f"in full, because this gate publishes its rejections:")
        lines.append("")
        for r in reasons:
            lines.append(f"- {r}")
        lines.append("")
        lines.append("Nothing here is a judgment of the forecast's merit — "
                     "the gate reads form, falsifiability, and published "
                     "policy only. Fix and submit a fresh issue; this one "
                     "closes to keep the queue honest.")
    (HERE / "gate_comment.md").write_text("\n".join(lines) + "\n",
                                          encoding="utf-8")
    print(f"gate: {'PASS' if accept else 'REJECT'} ({len(reasons)} reasons)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
