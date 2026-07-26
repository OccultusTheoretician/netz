#!/usr/bin/env python3
"""NETZ syndication — posts the KKR ledger state to Bluesky as a commitment beacon.

Each post carries the ledger stat-line, the full SHA-256 of ledger.json, and the
public ledger link: a dated, third-party-hosted record of ledger state on a clock
the operator does not control.

Credentials live in environment variables, never in this repository:
    BSKY_HANDLE        e.g. occultustheoretician.bsky.social
    BSKY_APP_PASSWORD  a Bluesky app password (Settings -> App Passwords)

Usage:
    python syndicate.py            post the current ledger state
    python syndicate.py --dry-run  print the post without sending
"""
import hashlib
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"
LEDGER_URL = "https://retroprescientaudit.com/ledger.html"


def build_post() -> tuple[str, str]:
    raw = LEDGER.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    projs = json.loads(raw)["projections"]
    c = Counter(p.get("status", "open") for p in projs)

    briers = []
    for p in projs:
        if p.get("status") in ("hit", "miss"):
            f = int(p["probability"]) / 100.0
            o = 1.0 if p["status"] == "hit" else 0.0
            briers.append((f - o) ** 2)
    brier = sum(briers) / len(briers) if briers else None

    dtg = datetime.now(timezone.utc).strftime("%d%H%MZ %b %y").upper()
    line = (
        f"KKR LEDGER {dtg} · {len(projs)} issued · {c.get('open', 0)} open · "
        f"{c.get('hit', 0)}H/{c.get('miss', 0)}M"
        + (f" · Brier {brier:.3f}" if brier is not None else "")
        + (f" · {c.get('void', 0)} void" if c.get("void") else "")
    )
    return line, sha


def kalls_line() -> str:
    """Kalls hashlog stat + full SHA-256; empty string if no hashlog."""
    p = HERE / "docs" / "kalls_hashlog.json"
    if not p.exists():
        return ""
    raw = p.read_bytes()
    ksha = hashlib.sha256(raw).hexdigest()
    recs = json.loads(raw).get("records", [])
    c = Counter(r.get("status", "SEALED") for r in recs)
    resolved = c.get("RESOLVED_HIT", 0) + c.get("RESOLVED_MISS", 0)
    return (f"KALLS · {c.get('SEALED',0)} sealed · {c.get('REVEALED',0)} revealed · "
            f"{resolved} resolved\nkalls_hashlog sha256: {ksha}\n")


def main() -> None:
    line, sha = build_post()
    body = f"{line}\nledger.json sha256: {sha}\n"
    body += kalls_line()
    print(body + LEDGER_URL)

    if "--dry-run" in sys.argv:
        print("[dry-run] not posted")
        return

    handle = os.environ.get("BSKY_HANDLE")
    password = os.environ.get("BSKY_APP_PASSWORD")
    if not handle or not password:
        sys.exit("Set BSKY_HANDLE and BSKY_APP_PASSWORD (setx, then open a new terminal).")

    from atproto import Client, client_utils

    client = Client()
    client.login(handle, password)
    text = client_utils.TextBuilder().text(body).link("ledger", LEDGER_URL)
    resp = client.send_post(text)
    print(f"posted: {resp.uri}")


if __name__ == "__main__":
    main()
