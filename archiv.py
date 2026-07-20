#!/usr/bin/env python3
"""
ARCHIV — acquisition + integrity ledger for the offline vault.

The vault holds verbatim dumps; ARCHIV fetches them resumably, checksums them,
and keeps the register of what you hold, how big it is, and whether it still
verifies. It never modifies content — preservation, not curation.

Usage:
    python archiv.py add <url> [--name wikipedia_en_nopic]   # register a target
    python archiv.py fetch [name]        # download (resumes .part automatically)
    python archiv.py verify [name]       # recompute sha256 vs. register
    python archiv.py status              # holdings table + total size

Vault location: --vault DIR (default D:\\vault or ./vault). Register lives in
the vault as archiv_register.json.
"""

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, unquote

import requests

CHUNK = 1024 * 1024
UA = {"User-Agent": "ARCHIV/1.0 (offline preservation; personal use)"}


def default_vault() -> Path:
    d = Path("D:/vault")
    return d if d.parent.exists() else Path(__file__).resolve().parent / "vault"


def reg_path(vault: Path) -> Path:
    return vault / "archiv_register.json"


def load_reg(vault: Path) -> dict:
    p = reg_path(vault)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"holdings": []}


def save_reg(vault: Path, reg: dict):
    reg_path(vault).write_text(json.dumps(reg, indent=2, ensure_ascii=False),
                               encoding="utf-8")


def find(reg: dict, name: str):
    for h in reg["holdings"]:
        if h["name"] == name:
            return h
    return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(CHUNK * 8)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def human(n) -> str:
    if n is None:
        return "?"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


# ----------------------------------------------------------------------
# commands
# ----------------------------------------------------------------------

def cmd_add(vault: Path, url: str, name: str | None):
    reg = load_reg(vault)
    if not name:
        name = unquote(Path(urlsplit(url).path).name) or "unnamed"
    if find(reg, name):
        print(f"ARCHIV · '{name}' already registered", file=sys.stderr)
        return
    size = None
    try:
        r = requests.head(url, timeout=20, headers=UA, allow_redirects=True)
        size = int(r.headers.get("Content-Length", 0)) or None
    except Exception:
        pass
    reg["holdings"].append({"name": name, "url": url,
                            "file": unquote(Path(urlsplit(url).path).name) or name,
                            "expected_bytes": size, "bytes": None, "sha256": None,
                            "date_fetched": None, "status": "registered"})
    save_reg(vault, reg)
    print(f"ARCHIV · registered '{name}' ({human(size)} expected)", file=sys.stderr)


def cmd_fetch(vault: Path, name: str | None):
    reg = load_reg(vault)
    targets = [h for h in reg["holdings"]
               if (name is None and h["status"] != "held") or h["name"] == name]
    if not targets:
        print("ARCHIV · nothing to fetch", file=sys.stderr)
        return
    for h in targets:
        dest = vault / h["file"]
        part = vault / (h["file"] + ".part")
        pos = part.stat().st_size if part.exists() else 0
        headers = dict(UA)
        if pos:
            headers["Range"] = f"bytes={pos}-"
            print(f"ARCHIV · resuming '{h['name']}' at {human(pos)}", file=sys.stderr)
        else:
            print(f"ARCHIV · fetching '{h['name']}'", file=sys.stderr)
        try:
            with requests.get(h["url"], stream=True, timeout=60, headers=headers) as r:
                if pos and r.status_code == 200:
                    print("ARCHIV · server ignored resume — restarting from zero",
                          file=sys.stderr)
                    pos = 0
                elif r.status_code not in (200, 206):
                    r.raise_for_status()
                total = h["expected_bytes"]
                mode = "ab" if pos else "wb"
                done = pos
                last = time.monotonic()
                with open(part, mode) as f:
                    for chunk in r.iter_content(CHUNK):
                        f.write(chunk)
                        done += len(chunk)
                        if time.monotonic() - last > 5:
                            pct = f" ({done/total:.0%})" if total else ""
                            print(f"ARCHIV · {h['name']}: {human(done)}{pct}",
                                  file=sys.stderr)
                            last = time.monotonic()
            part.rename(dest)
            h["bytes"] = dest.stat().st_size
            print(f"ARCHIV · hashing {h['name']} …", file=sys.stderr)
            h["sha256"] = sha256_file(dest)
            h["date_fetched"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            h["status"] = "held"
            save_reg(vault, reg)
            print(f"ARCHIV · held: {h['name']} · {human(h['bytes'])} · "
                  f"sha256 {h['sha256'][:16]}…", file=sys.stderr)
        except Exception as exc:
            h["status"] = "partial" if part.exists() else "failed"
            save_reg(vault, reg)
            print(f"ARCHIV · '{h['name']}' interrupted ({str(exc)[:80]}) — "
                  f"rerun fetch to resume", file=sys.stderr)


def cmd_verify(vault: Path, name: str | None):
    reg = load_reg(vault)
    targets = [h for h in reg["holdings"] if h["status"] == "held" and
               (name is None or h["name"] == name)]
    bad = 0
    for h in targets:
        dest = vault / h["file"]
        if not dest.exists():
            print(f"ARCHIV · MISSING  {h['name']} — file gone from vault", file=sys.stderr)
            h["status"] = "missing"
            bad += 1
            continue
        digest = sha256_file(dest)
        if digest == h["sha256"]:
            print(f"ARCHIV · OK       {h['name']}", file=sys.stderr)
        else:
            print(f"ARCHIV · CORRUPT  {h['name']} — hash mismatch, refetch", file=sys.stderr)
            h["status"] = "corrupt"
            bad += 1
    save_reg(vault, reg)
    print(f"ARCHIV · verify complete · {len(targets) - bad} ok / {bad} bad", file=sys.stderr)


def cmd_status(vault: Path):
    reg = load_reg(vault)
    if not reg["holdings"]:
        print("ARCHIV · register empty — `archiv.py add <url>` to begin", file=sys.stderr)
        return
    total = 0
    print(f"{'name':<34}{'status':<12}{'size':<12}fetched")
    print("-" * 70)
    for h in reg["holdings"]:
        total += h["bytes"] or 0
        print(f"{h['name'][:33]:<34}{h['status']:<12}"
              f"{human(h['bytes'] or h['expected_bytes']):<12}{h['date_fetched'] or '—'}")
    print("-" * 70)
    print(f"{'VAULT TOTAL (held)':<46}{human(total)}")


def main():
    ap = argparse.ArgumentParser(description="ARCHIV — offline vault acquisition + ledger")
    ap.add_argument("command", choices=["add", "fetch", "verify", "status"])
    ap.add_argument("target", nargs="?", default=None, help="url (add) or name")
    ap.add_argument("--name", default=None)
    ap.add_argument("--vault", default=None)
    args = ap.parse_args()

    vault = Path(args.vault) if args.vault else default_vault()
    vault.mkdir(parents=True, exist_ok=True)

    if args.command == "add":
        if not args.target:
            print("ARCHIV · add needs a URL", file=sys.stderr)
            sys.exit(1)
        cmd_add(vault, args.target, args.name)
    elif args.command == "fetch":
        cmd_fetch(vault, args.target)
    elif args.command == "verify":
        cmd_verify(vault, args.target)
    else:
        cmd_status(vault)


if __name__ == "__main__":
    main()
