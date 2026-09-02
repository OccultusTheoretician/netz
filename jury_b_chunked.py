#!/usr/bin/env python3
"""jury_b_chunked.py -- JURYB-CHUNK-2026-09-02: the cold seat, paginated.

WHY. kkr.py's local-juror call caps the reply at 6,000 tokens. A 109-row
docket needs roughly five times that, so juror B's array died mid-object at
row ~30 and the jury refused to empanel (no complete JSON array). The fix is
pagination, not prompting: the same blinded packet, served to the same local
model in chunks small enough to finish, the juror's own outputs concatenated.
Every verdict remains the model's; this tool only cuts the docket on its own
### row seams and staples the replies.

    python jury_b_chunked.py                          today's packet, defaults
    python jury_b_chunked.py --packet FILE --out FILE --rows-per-chunk 22

A chunk whose reply will not parse or misses ids is split in half and retried
(floor 4 rows). An existing output file is kept aside as <name>.partial.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kkr  # call_lmstudio, the desk's own client

ROW = re.compile(r"(?m)^### (KKR-\d{8}-\d+)\s*$")


def split_packet(text: str):
    """(header, [(id, section_text), ...]) cut on the packet's own seams."""
    marks = list(ROW.finditer(text))
    if not marks:
        raise SystemExit("jury_b_chunked: no '### KKR-' rows found in the packet")
    header = text[: marks[0].start()]
    rows = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        rows.append((m.group(1), text[m.start():end]))
    return header, rows


def parse_array(reply: str):
    if not reply:
        return None
    i, j = reply.find("["), reply.rfind("]")
    if i < 0 or j <= i:
        return None
    try:
        arr = json.loads(reply[i:j + 1])
        return arr if isinstance(arr, list) else None
    except Exception:
        return None


def run_chunk(call, header: str, rows: list, depth: int = 0) -> list:
    ids = [r[0] for r in rows]
    tag = f"{ids[0]}..{ids[-1]} ({len(rows)} rows)"
    prompt = header + "".join(t for _i, t in rows)
    print(f"jury_b: chunk {tag}{' [retry-split]' if depth else ''} ...", file=sys.stderr)
    reply = call(prompt)
    arr = parse_array(reply) or []
    got = {v.get("id") for v in arr if isinstance(v, dict)}
    missing = [i for i in ids if i not in got]
    if not missing:
        print(f"jury_b:   {len(arr)} verdict(s), coverage complete", file=sys.stderr)
        return [v for v in arr if isinstance(v, dict) and v.get("id") in ids]
    if len(rows) <= 4:
        print(f"jury_b:   STILL SHORT at floor: missing {missing}", file=sys.stderr)
        return [v for v in arr if isinstance(v, dict) and v.get("id") in ids]
    print(f"jury_b:   incomplete ({len(missing)} missing) - splitting", file=sys.stderr)
    mid = len(rows) // 2
    return run_chunk(call, header, rows[:mid], depth + 1) + run_chunk(call, header, rows[mid:], depth + 1)


def run(packet_text: str, call, rows_per_chunk: int = 22) -> tuple[list, list]:
    header, rows = split_packet(packet_text)
    out, seen = [], set()
    for k in range(0, len(rows), rows_per_chunk):
        for v in run_chunk(call, header, rows[k:k + rows_per_chunk]):
            if v.get("id") not in seen:
                seen.add(v["id"]); out.append(v)
    missing = [i for i, _t in rows if i not in seen]
    return out, missing


def main() -> int:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packet", default=str(HERE / "forecasts" / f"audit_packet_{today}.md"))
    ap.add_argument("--out", default=str(HERE / "forecasts" / f"jury_B_{today}.json"))
    ap.add_argument("--rows-per-chunk", type=int, default=22)
    ap.add_argument("--lmstudio-url", default="http://127.0.0.1:1234/v1")
    ap.add_argument("--model", default=None, help="default: whatever LM Studio has loaded")
    a = ap.parse_args()
    packet = Path(a.packet)
    if not packet.exists():
        print(f"jury_b_chunked: {packet} not found", file=sys.stderr); return 2
    call = lambda prompt: kkr.call_lmstudio(a.lmstudio_url, a.model, prompt)
    verdicts, missing = run(packet.read_text(encoding="utf-8"), call, a.rows_per_chunk)
    outp = Path(a.out)
    if outp.exists():
        outp.replace(outp.with_suffix(outp.suffix + ".partial"))
        print(f"jury_b: existing file kept as {outp.name}.partial", file=sys.stderr)
    outp.write_text(json.dumps(verdicts, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"jury_b: {len(verdicts)} verdict(s) -> {outp.name}"
          + (f" | MISSING {len(missing)}: {missing[:6]}" if missing else " | coverage complete"))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
