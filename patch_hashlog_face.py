#!/usr/bin/env python3
"""
patch_hashlog_face.py — make the hashlog self-describing, so it verifies from
any route rather than only from the one that happens to carry its own anchor.

The finding: running knp_verify against the hashlog at retroprescientaudit.com
returns NONCONFORMANT on KNP 4.03, and running it against the identical bytes at
raw.githubusercontent.com returns CONFORMANT. Same file. The difference is that
the GitHub route carries the append-only mechanism implicitly in its own commit
history, and the custom domain does not. A reader who receives the file by any
other route — a download, an archive copy, an email attachment — cannot tell
what makes it append-only, and therefore cannot tell whether the count is honest.

That is a real defect on the primary public surface, and the fix is two fields.
KNP 4.02 forbids removing records or altering commitments; adding top-level
descriptive fields does neither, and every record is left untouched.

  python patch_hashlog_face.py [path]     default docs\\kalls_hashlog.json

Idempotent. Verify afterwards with:
  python knp_verify.py docs\\kalls_hashlog.json
which should then report CONFORMANT as a bare file, with no should-departures.
"""

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

TARGET = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/kalls_hashlog.json")

REPO = "https://github.com/OccultusTheoretician/netz"

ANCHOR = {
    "mechanism": "public version-control history",
    "description": (
        "This hashlog is published in a public git repository. Every append is a "
        "commit with an independent timestamp and hash chain that the committer "
        "cannot rewrite without the rewrite being visible to anyone holding an "
        "earlier clone. The commit history is the append-only mechanism required "
        "by KNP 4.03, and it is not under the committer's sole control."),
    "repository": REPO,
    "path": "docs/kalls_hashlog.json",
    "history": f"{REPO}/commits/main/docs/kalls_hashlog.json",
    "verify": ("Clone the repository, walk the history of this path, and confirm "
               "no record was ever removed and no commitment ever altered. "
               "python knp_verify.py <current> --previous <earlier> asserts it "
               "across any two snapshots."),
}

DISCLOSURE = (
    "probability, deadline and domain are published OUTSIDE the canonical "
    "preimage and are therefore NOT BOUND by the commitment hash. They are "
    "anchored only by the append-only record described in 'anchor'. The fields "
    "bound by the hash are exactly those named in 'construction.preimage_order'. "
    "A reader checking a reveal recomputes over the preimage fields alone; the "
    "published commitment governs."
)


def main():
    if not TARGET.exists():
        print(f"FAIL — no such file: {TARGET}")
        return 1
    raw = TARGET.read_text(encoding="utf-8")
    h = json.loads(raw)

    if not isinstance(h, dict) or "records" not in h:
        print("FAIL — not a KNP-26 hashlog object")
        return 1

    if h.get("anchor") and h.get("disclosure"):
        print("ALREADY PATCHED — anchor and disclosure are present. Nothing written.")
        return 0

    before = len(h["records"])
    commitments = [r.get("commitment") for r in h["records"]]

    out = {}
    for k in ("protocol", "construction"):
        if k in h:
            out[k] = h[k]
    out["anchor"] = ANCHOR
    out["disclosure"] = DISCLOSURE
    for k, v in h.items():
        if k not in out and k != "records":
            out[k] = v
    out["records"] = h["records"]

    assert len(out["records"]) == before, "record count changed"
    assert [r.get("commitment") for r in out["records"]] == commitments, \
        "a commitment changed"

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    backup = Path(__file__).resolve().parent / f"kalls_hashlog_BEFORE_face_{stamp}.json"
    shutil.copy2(TARGET, backup)
    TARGET.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")

    print(f"  added · anchor      (KNP 4.03 — names the append-only mechanism)")
    print(f"  added · disclosure  (KNP 4.01 — names what the hash does not bind)")
    print(f"\n  {before} records untouched, every commitment identical")
    print(f"  backup  → {backup}")
    print(f"  patched → {TARGET}")
    print(f"\nNext: python knp_verify.py {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
