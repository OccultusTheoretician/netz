#!/usr/bin/env python3
"""
ots_anchor.py — the trustless clock. OpenTimestamps anchoring for the desk.

WHY THIS EXISTS

    The desk's own standing rule: a seal hash must be published somewhere the
    operator does not control the clock. Two mechanisms already serve that, and
    both require trusting somebody.

      · Version-control history (RPAS 4.04) — anchored, public, and checkable,
        but GitHub could in principle be compelled or could err, and the
        operator holds the account.
      · RFC 3161 timestamping (the kalls token) — a trusted third party signs
        the time. Better. Still a party you trust.

    OpenTimestamps removes the trusted party. It aggregates a digest into a
    Merkle tree, commits the tree root into a Bitcoin transaction, and hands
    back a receipt that proves the digest existed before that block. Verifying
    it requires trusting no one — only that Bitcoin's history is what it is.
    That is the exact cryptographic embodiment of what this desk claims, and it
    costs nothing.

WHAT IS ANCHORED, AND WHEN

    Commit-time only. The served pages never call out — site_audit enforces
    "zero external stylesheets or scripts, nothing phones home", and that
    property is an asset, not an inconvenience. This runs from the operator's
    machine, writes a .ots receipt beside the file, and the receipt is committed
    like any other artifact. The READER verifies with their own client against
    their own view of the chain; the desk is not consulted at its own audit.

THE TWO-PHASE SHAPE, WHICH MUST NOT BE MISREPRESENTED

    A fresh receipt is NOT yet a Bitcoin attestation. `ots stamp` returns
    commitments from calendar servers, which promise to include the digest in a
    future block. Aggregation into a block takes hours. Only after
    `ots upgrade` does the receipt carry a real Bitcoin attestation and become
    independently verifiable.

    So a receipt has two honest states, and this tool prints which one it is in:

      PENDING  — calendar commitments only. Proves the calendars saw the digest.
                 Does NOT yet prove a block height. Publishable, but must be
                 labelled pending.
      ANCHORED — upgraded, carries a Bitcoin attestation, verifiable by a
                 stranger with no trust in this desk or in the calendars.

    Claiming a pending receipt is "anchored in Bitcoin" would be exactly the
    stated-versus-operational gap this desk exists to audit. Don't.

USE
    python ots_anchor.py --stamp              stamp ledger + hashlog digests
    python ots_anchor.py --upgrade            try to upgrade pending receipts
    python ots_anchor.py --status             report each receipt's real state
    python ots_anchor.py --stamp --dry-run    show what would be stamped
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"

# The artifacts whose existence-in-time is the load-bearing claim.
TARGETS = [
    "ledger.json",
    "kalls_hashlog.json",
    "plate.json",
    # KK18: the doctrine documents. A novelty claim's precedence cannot rest
    # on git history alone - the operator holds that account (4.05). The
    # claim's own text is what needs a clock the operator does not hold.
    "ABYSS_DOCTRINE_DRAFT_v1.md",
    "RPAS_FIRST_EDITION_2026_v1.md",
    "KRAEHE_NEST_METHOD.md",
    "KRAEHE_NEST_PROTOCOL.md",
    "LIAS_FIRST_EDITION_2026_v1.md",
    # OTSTARGETS-2026-09-01: the pre-registration is the paper; its text gets a clock
    # the operator does not hold, same as the standards.
    "KALIBRIERWARTE_REGISTERED_REPORT_v3.md",
    # 2026-08-18: the PCAOB 2026-005 docket as a committed population -
    # 33 comment letters, count fixed with no gaps, each hashed as served,
    # retrieved complete rather than sampled. This is the construction the
    # desk's own letter 6 asked the Board to require, applied to the docket
    # that contains it. Unlike ledger.json the file is immutable by design,
    # so its pairing should read MATCH permanently; a DRIFT here would mean
    # the population commitment itself was altered and must be investigated.
    "PCAOB_2026-005_DOCKET_MANIFEST.txt",
]

STATE = DOCS / "ots_anchors.json"


# DEFECT, 2026-07-30: this checked shutil.which("ots") only. pip installs the
# console script into a per-user Scripts directory that is frequently NOT on
# PATH — it prints that warning during install — so the tool reported "ots not
# found" on a machine where opentimestamps was correctly installed. The console
# script is a two-line wrapper around otsclient.ots:main, so invoking the module
# with the running interpreter works regardless of PATH and is now the fallback.
def ots_candidates():
    """Every place the console script actually lands, then the module.

    Fix history, both defects measured on live runs:
      1. Checked only shutil.which("ots") — pip installs the script into a
         per-user Scripts directory that is routinely NOT on PATH, and says so
         during install. The binary existed; the tool declared it missing.
      2. Fell back to importing otsclient and SWALLOWED the exception, so a
         failing dependency looked identical to a missing package. The import
         error is now printed, because a hidden reason is the thing that cost
         an hour tonight in a different tool.
    """
    out = []
    w = shutil.which("ots")
    if w:
        out.append(("PATH", [w]))
    # user + platform script directories, where pip actually puts it
    import sysconfig, site
    dirs = []
    for key in ("scripts", "purelib"):
        for scheme in ("nt_user", "posix_user", "nt", "posix_prefix"):
            try:
                d = sysconfig.get_path("scripts", scheme)
            except Exception:
                d = None
            if d:
                dirs.append(Path(d))
        break
    try:
        ub = Path(site.getuserbase())
        dirs += [ub / "Scripts", ub / "bin"]
    except Exception:
        pass
    for d in dirs:
        for name in ("ots.exe", "ots"):
            p = d / name
            if p.exists():
                out.append((str(d), [str(p)]))
    out.append(("module", [sys.executable, "-c",
                "import sys;from otsclient.ots import main;"
                "sys.argv[0]='ots';sys.exit(main())"]))
    return out


def ots_argv(verbose=False):
    for where, argv in ots_candidates():
        if where == "module":
            try:
                import otsclient.ots  # noqa: F401
            except Exception as e:
                if verbose:
                    print(f"  module import failed: {type(e).__name__}: {e}",
                          file=sys.stderr)
                continue
        if verbose:
            print(f"  using ots from: {where}", file=sys.stderr)
        return argv
    return None


def have_ots():
    return ots_argv(verbose=True) is not None


def run(args, timeout=90):
    argv = ots_argv()
    if argv is None:
        return 127, "opentimestamps-client not importable"
    try:
        p = subprocess.run(argv + args, capture_output=True, text=True,
                           timeout=timeout)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "timed out"
    except FileNotFoundError:
        return 127, "ots not installed"


def sha256_file(p: Path):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


_OTS_MAGIC = bytes.fromhex("004f70656e54696d657374616d7073000050726f6f66"
                           "00bf89e2e884e89294")


def receipt_digest(receipt: Path):
    """The digest this receipt actually commits, read from its own bytes.

    Layout: magic, one version byte, one file-hash op byte (0x08 = SHA-256),
    then the 32-byte digest. `ots info` does not print it, so it is parsed
    here rather than inferred from whatever file happens to sit beside the
    receipt. This value is fixed for the life of the receipt.
    """
    try:
        b = receipt.read_bytes()
    except OSError:
        return None
    if not b.startswith(_OTS_MAGIC):
        return None
    off = len(_OTS_MAGIC) + 1
    if len(b) < off + 33 or b[off] != 0x08:
        return None
    return b[off + 1:off + 33].hex()


def _entry(src: Path, rec: Path, state, height=None):
    """One row of the published state file.

    Carries what the receipt commits AND what is being served, because
    publishing only one of the two lets a changed file sit beside an unchanged
    receipt looking like a matched pair. A stranger needs both numbers to
    check anything.
    """
    at_stamp = receipt_digest(rec)
    served = sha256_file(src) if src.exists() else None
    if at_stamp and served:
        pairing = "MATCH" if at_stamp == served else "DRIFT"
    else:
        pairing = "UNKNOWN"
    e = {"receipt": rec.name, "state": state,
         "digest": at_stamp or served,
         "digest_at_stamp": at_stamp,
         "digest_served": served,
         "pairing": pairing}
    if height:
        e["bitcoin_block"] = height
    if pairing == "DRIFT":
        e["pairing_note"] = ("the served file has changed since this receipt "
                             "was created. The receipt still proves the "
                             "ORIGINAL bytes existed before its block and "
                             "proves nothing whatever about the file served "
                             "now.")
    return e


def receipt_state(receipt: Path):
    """Read the receipt's REAL state rather than assuming it succeeded.

    `ots info` prints the attestation set. A Bitcoin attestation names a block
    height; calendar commitments name a URL. That distinction is the whole
    difference between 'pending' and 'anchored', so it is read, not inferred.
    """
    if not receipt.exists():
        return "absent", None, ""
    code, out = run(["info", str(receipt)], timeout=30)
    if code != 0:
        return "unreadable", None, out.strip()[:200]
    low = out.lower()
    if "bitcoin block" in low:
        height = None
        for tok in out.replace(",", " ").split():
            if tok.isdigit() and len(tok) >= 6:
                height = int(tok)
                break
        return "anchored", height, out.strip()[:400]
    if "pendingattestation" in low.replace(" ", "") or "calendar" in low:
        return "pending", None, out.strip()[:400]
    return "unknown", None, out.strip()[:400]


CALENDARS = ["https://a.pool.opentimestamps.org",
             "https://b.pool.opentimestamps.org",
             "https://a.pool.eternitywall.com",
             "https://ots.btc.catallaxy.com"]


def do_probe(timeout=8):
    """Ask each calendar directly. Stamping needs two of these to answer, so
    when a stamp fails this says WHICH ones are the problem rather than leaving
    'unreachable' to cover everything from DNS to a corporate proxy."""
    import urllib.request
    import urllib.error
    print("Calendar reachability (stamping requires 2 to answer):")
    ok = 0
    inconclusive = 0
    for url in CALENDARS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "netz-ots-probe"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                code = r.status
            print(f"  OK    {url}  (HTTP {code})")
            ok += 1
        except urllib.error.HTTPError as e:
            # A 404 or 405 on the root proves the calendar host answered. A 403
            # does NOT: an intercepting proxy returns 403 too, and at this layer
            # the two are indistinguishable. Counting 403 as reachable made this
            # probe print "4 of 4 answered, retry" on a machine where every
            # stamp failed — a probe that falsely reassures is worse than none.
            if e.code in (404, 405, 400):
                print(f"  OK    {url}  (HTTP {e.code} on root — host answered)")
                ok += 1
            elif e.code in (401, 403, 407):
                print(f"  INCONCLUSIVE  {url}  (HTTP {e.code} — this is what an "
                      f"intercepting proxy returns; cannot tell proxy from host)")
                inconclusive += 1
            else:
                print(f"  FAIL  {url}  (HTTP {e.code})")
        except Exception as e:
            print(f"  FAIL  {url}  ({type(e).__name__}: {e})")
    print(f"\n{ok} answered, {inconclusive} inconclusive, "
          f"{len(CALENDARS) - ok - inconclusive} failed.")
    if ok >= 2:
        print("Enough answered for a stamp — retry --stamp.")
    elif inconclusive:
        print("Cannot conclude. An intercepting proxy or captive network is "
              "the usual cause;\nthe calendars may be fine and unreachable "
              "from here anyway. Try another network.")
    else:
        print("Not enough reachable. DNS, firewall, or ISP block — nothing "
              "about this desk.")
    return 0 if ok >= 2 else 1


def do_stamp(dry):
    files = [DOCS / t for t in TARGETS if (DOCS / t).exists()]
    missing = [t for t in TARGETS if not (DOCS / t).exists()]
    if missing:
        print("  not present, skipped: " + ", ".join(missing))
    if not files:
        print("Nothing to stamp.", file=sys.stderr)
        return 1
    print("Digests to be anchored (SHA-256 of the exact bytes served):")
    for f in files:
        print(f"  {f.name:22} {sha256_file(f)}")
    if dry:
        print("\n(dry run — nothing submitted)")
        return 0
    if not have_ots():
        print("\nCould not locate the ots client. Places checked:",
              file=sys.stderr)
        for where, argv in ots_candidates():
            print(f"    {where}: {argv[0]}", file=sys.stderr)
        print("\nopentimestamps-client is neither on PATH nor importable.\n"
              "  pip install opentimestamps-client\n"
              "  (if pip warns its Scripts directory is not on PATH, that is "
              "fine — this tool falls back to the module.)", file=sys.stderr)
        return 2

    results = {}
    for f in files:
        print(f"\nstamping {f.name} …")
        code, out = run(["stamp", str(f)])
        rec = f.with_suffix(f.suffix + ".ots")
        if rec.exists():
            st, h, _ = receipt_state(rec)
            results[f.name] = _entry(f, rec, st, h)
            print(f"  receipt {rec.name} · state {st.upper()}")
            if st == "pending":
                print("  PENDING is correct and expected: calendars have the "
                      "digest, Bitcoin does not yet.")
                print("  Re-run with --upgrade in a few hours, then commit the "
                      "upgraded receipt.")
        else:
            # The exact failure seen when calendars are unreachable:
            #   "Failed to create timestamp: need at least 2 attestations
            #    but received 0 within timeout"
            reason = "calendars unreachable or refused"
            # DEFECT: this label was printed even when the client had CRASHED,
            # which is a different fact and sent the diagnosis down the wrong
            # road — the probe said 4 of 4 calendars answered while this said
            # unreachable. A traceback is not a network condition.
            if "Traceback" in out or "Error:" in out or "LoadLibrary" in out:
                reason = ("the ots client itself failed to start — NOT a "
                          "network problem; read the traceback below")
                if "bitcoin.core.key" in out or "find_library" in out:
                    reason += ("\n  Known cause: python-bitcoinlib cannot "
                               "locate an OpenSSL DLL on this interpreter. "
                               "Run ots under Python 3.12/3.13, or put "
                               "libcrypto/libssl on PATH.")
            elif "need at least" in out:
                reason = ("fewer than two calendars answered — OpenTimestamps "
                          "requires 2 attestations minimum")
            print(f"  NO RECEIPT WRITTEN — {reason}")
            # THIRD swallow of the night in this codebase, so it ends here: the
            # client's own words are the diagnosis and a summary is not. LM
            # Studio's 400 body and the otsclient import exception were the
            # first two; each cost a cycle that printing the output would have
            # saved.
            if out.strip():
                print("  --- ots said, verbatim ---")
                for line in out.strip().splitlines()[-14:]:
                    print("  | " + line)
            else:
                print("  (ots produced no output at all — check that the "
                      "client can reach the network)")
            print("  Nothing was published and nothing is claimed. Retry when "
                  "the network is available.")
            results[f.name] = {"receipt": None, "state": "failed",
                               "reason": reason, "digest": sha256_file(f)}

    write_state(results)
    return 0


def do_upgrade():
    if not have_ots():
        print("`ots` not found.", file=sys.stderr)
        return 2
    recs = sorted(DOCS.glob("*.ots"))
    if not recs:
        print("No receipts to upgrade. Run --stamp first.")
        return 0
    changed = 0
    results = {}
    for rec in recs:
        before, _, _ = receipt_state(rec)
        if before == "anchored":
            print(f"{rec.name}: already ANCHORED — nothing to do")
            continue
        code, out = run(["upgrade", str(rec)], timeout=120)
        after, height, _ = receipt_state(rec)
        src = rec.with_suffix("")
        if src.exists():
            results[src.name] = _entry(src, rec, after, height)
        arrow = f"{before.upper()} -> {after.upper()}"
        extra = f" · Bitcoin block {height}" if height else ""
        print(f"{rec.name}: {arrow}{extra}")
        if after == "anchored":
            changed += 1
        elif "not found" in out.lower() or before == after:
            print("  still pending — the calendar has not aggregated into a "
                  "block yet. Hours, not minutes.")
    if changed:
        print(f"\n{changed} receipt(s) now carry a Bitcoin attestation. Commit "
              f"the upgraded .ots file(s); a stranger can now verify the date "
              f"with no trust in this desk.")
    if results:
        write_state(results)
    return 0


def do_status():
    recs = sorted(DOCS.glob("*.ots"))
    if not recs:
        print("No receipts. Run --stamp.")
        return 0
    print(f"{'receipt':30} {'state':10} {'block':>9}  digest matches served file")
    print("-" * 76)
    for rec in recs:
        st, height, _ = receipt_state(rec)
        src = rec.with_suffix("")
        match = "—"
        if src.exists():
            saved = load_state().get(src.name, {}).get("digest")
            cur = sha256_file(src)
            match = ("yes" if saved == cur else
                     "NO — the file changed since stamping" if saved
                     else "unrecorded")
        print(f"{rec.name:30} {st.upper():10} {str(height or '—'):>9}  {match}")
    print("")
    print("A receipt proves the digest existed before its block. It says")
    print("nothing about whether the contents were true — same as every other")
    print("seal on this desk.")
    return 0


def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8-sig")).get("files", {})
        except Exception:
            return {}
    return {}


def write_state(results):
    payload = {
        "schema": "ots_anchors/v1",
        "generated": datetime.now(timezone.utc).isoformat(),
        "construction": ("SHA-256 over the exact served bytes, submitted to "
                         "OpenTimestamps calendars, aggregated into a Bitcoin "
                         "transaction. Verification requires no trust in this "
                         "desk or in the calendars."),
        "two_phase_note": ("a PENDING receipt carries calendar commitments "
                           "only and does NOT prove a block height; only an "
                           "ANCHORED receipt does. Pending must never be "
                           "described as anchored."),
        "pairing_note": ("digest_at_stamp is read from the receipt and is "
                         "fixed; digest_served is computed live from the "
                         "bytes on this site. pairing=MATCH means the "
                         "receipt covers what you can download. "
                         "pairing=DRIFT means the file has changed since "
                         "it was stamped and the receipt covers the older "
                         "bytes only. DRIFT is disclosed, not corrected: a "
                         "receipt is never re-issued to make a later file "
                         "look anchored."),
        "verify_command": "ots verify docs/<file>.ots",
        "files": {**load_state(), **results},
    }
    STATE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"\nstate → {STATE}")


def main():
    ap = argparse.ArgumentParser(description="OpenTimestamps anchoring")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("--upgrade", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--probe", action="store_true",
                    help="test calendar reachability and name which fail")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.probe:
        return do_probe()
    if not (a.stamp or a.upgrade or a.status or a.probe):
        ap.print_help()
        return 1
    if a.stamp:
        return do_stamp(a.dry_run)
    if a.upgrade:
        return do_upgrade()
    return do_status()


if __name__ == "__main__":
    sys.exit(main())
