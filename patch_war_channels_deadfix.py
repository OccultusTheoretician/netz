#!/usr/bin/env python3
"""
patch_war_channels_deadfix.py — dead-channel registry cleanup, PROPOSAL FORM.

The 2026-07-30 --verify found 8 zero-yield channels. They are NOT one problem;
this patch treats each by its actual cause and REFUSES to invent handles it
cannot verify.

WHAT IT DOES WITHOUT ASKING (safe — these are structural, not guesses):
  - The three PLACEHOLDER slots (SyriaCivilDefense, sahel_intelligence,
    sdf_press) were never real handles — the registry says so (confidence:
    placeholder). They are marked status DManual-GAP with a dated note, so the
    silence block stops reading them as failures and starts reading them as
    known-empty coverage. No handle is guessed.

WHAT IT FLAGS FOR YOU (handle drift — needs a human to confirm the new handle):
  - russianlosses, Deepstate_UA, TimesofIsrael, sentdefender, Faytuks are real
    projects whose Telegram handle may have drifted. This patch writes a
    _dead_channel_review block listing each with its likely current handle as a
    SUGGESTION ONLY, and does NOT change the handle. You confirm the live handle
    (open Telegram, check it resolves), then edit the one field. Guessing a
    handle into a live pull is exactly the confabulation the desk forbids.

This writes war_channels.PROPOSED.json — NOT war_channels.json. Nothing the
desk reads is touched until you diff and rename. Run from C:\netz:
    python patch_war_channels_deadfix.py
    (review war_channels.PROPOSED.json, confirm the 5 handles, then rename)
"""
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "war_channels.json"
DST = HERE / "war_channels.PROPOSED.json"
TODAY = date.today().isoformat()

# placeholder slots: never real, mark as known gap (no handle invented)
GAPS = {"SyriaCivilDefense", "sahel_intelligence", "sdf_press"}

# handle-drift: real project, handle may have moved. SUGGESTION for operator to
# verify — NOT applied. Value is the candidate handle to CHECK, not to trust.
DRIFT_SUGGESTIONS = {
    "russianlosses": "check: project may post under a renamed channel; verify before use",
    "Deepstate_UA": "check: DeepState mapping — candidate 'DeepStateUA' (no underscore) on some mirrors; VERIFY it resolves",
    "TimesofIsrael": "check: candidate lowercase 'timesofisrael'; VERIFY the Telegram channel resolves",
    "sentdefender": "check: OSINTdefender moves handles; verify the current live channel before use",
    "Faytuks": "check: candidate 'Faytuks_News' or 'FaytuksNetwork'; VERIFY which resolves",
}


def main():
    if not SRC.exists():
        print("war_channels.json not found beside this script.", file=sys.stderr)
        return 1
    d = json.loads(SRC.read_text(encoding="utf-8"))
    ch = d["channels"]

    marked_gap, flagged = [], []
    for c in ch:
        h = c.get("handle", "").lstrip("@")
        if h in GAPS:
            c["status"] = "DManual-GAP"
            c["gap_note"] = (f"placeholder slot, never a live handle; confirmed "
                             f"zero-yield {TODAY}. Genuine coverage gap, not a "
                             f"dead channel. Fill with a real handle to close.")
            marked_gap.append(h)
        elif h in DRIFT_SUGGESTIONS:
            # DO NOT change the handle. Attach a review note only.
            c["_review"] = DRIFT_SUGGESTIONS[h]
            c["_review_date"] = TODAY
            flagged.append(h)

    d.setdefault("_dead_channel_review", {})
    d["_dead_channel_review"][TODAY] = {
        "marked_as_gap": sorted(marked_gap),
        "flagged_for_handle_check": sorted(flagged),
        "instruction": ("For each flagged channel: open Telegram, confirm the "
                        "current handle resolves, then set 'handle' to the "
                        "verified value and delete its _review fields. Do NOT "
                        "trust the candidate handles unverified — they are "
                        "leads, not facts."),
    }

    DST.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"wrote {DST.name} (war_channels.json UNTOUCHED)")
    print(f"  marked as known gap (no handle invented): {', '.join(marked_gap)}")
    print(f"  flagged for your handle-check (NOT changed): {', '.join(flagged)}")
    print()
    print("REVIEW STEP (yours, not automatable):")
    print("  1. open war_channels.PROPOSED.json")
    print("  2. for each flagged channel, verify the live handle on Telegram")
    print("  3. set its 'handle' to the confirmed value, delete _review fields")
    print("  4. diff against war_channels.json, then rename to replace")
    print("  5. python tg_fetch.py --verify   (confirm they now resolve)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
