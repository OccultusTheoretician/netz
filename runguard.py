#!/usr/bin/env python3
"""
runguard.py — ONE DEFINITION OF THE RUN-ARTIFACT WRITE GUARD

WHY THIS IS ITS OWN FILE

    On 2026-08-04 the same defect appeared five times in one day: an artifact
    whose name could not distinguish two runs was handed two runs and answered
    by discarding one, silently.

        ots_anchor            mutable filename; published digest drifted from
                              the receipt beside it
        control_packet.json   fixed default; cost KKR-20260803-01 its basis
                              permanently
        KKR_<stamp>.md        day resolution, then minute resolution, then
                              minute-plus-arm - each fix closed the case that
                              had just happened
        control_packet.json   again, in the command sequence written an hour
                              after the third fix

    Four of those fixes added a component to a filename. None of them closed
    the class, because the class is not about names: any scheme encodes what
    its author anticipated, and a run always has one more distinguishing
    property than that.

    KK21f stopped naming and started refusing, inside kkr.py. Three writers
    were still outside it - wardesk_evidence.py, tg_grade.py,
    desk_fragility.py - and wardesk_evidence.py is the one that produced
    KK20 defect #8, a file named WARDESK_2026-07-30_0745.md holding an 08-02
    render.

    A guard copied into four files is a guard that will diverge in three of
    them. It lives here.

CONTRACT

    Different bytes at an existing path -> suffix _2, _3 ... and print.
    Identical bytes -> rewrite silently; a rerun that reproduces its own
    artifact is not a collision.
    Path free -> write.

    Returns the path actually written, which the caller should use rather
    than the path it asked for.

DELIBERATELY NOT GUARDED

    "latest" pointers and published/served copies. A pointer is supposed to be
    replaced; guarding it would turn a working mechanism into noise. Guard the
    dated artifact, never the pointer at it.
"""

from pathlib import Path
import sys

__all__ = ["write_run_artifact"]


def write_run_artifact(path, text: str, tag: str = "netz",
                       encoding: str = "utf-8") -> Path:
    """Write a run artifact without ever destroying another run's."""
    path = Path(path)
    if path.exists():
        try:
            if path.read_text(encoding=encoding, errors="replace") == text:
                path.write_text(text, encoding=encoding)
                return path
        except Exception:
            # Unreadable existing file is treated as different bytes. Erring
            # toward a second file is always cheaper than erring toward a
            # destroyed one.
            pass
        n = 2
        while True:
            alt = path.with_name(f"{path.stem}_{n}{path.suffix}")
            if not alt.exists():
                break
            n += 1
        print(f"{tag} · {path.name} already holds a different run - writing "
              f"{alt.name} rather than discarding it", file=sys.stderr)
        path = alt
    path.write_text(text, encoding=encoding)
    return path
