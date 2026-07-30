#!/usr/bin/env python3
"""
denom.py — evidentiary completeness for AI-generated records.
Version 0.1.0 · single file · Python 3.10+ · standard library only.

THE PROBLEM THIS SOLVES
An AI deployer who shows an auditor "the outputs we chose to disclose" has
shown a management-selected sample, and a management-selected sample is not
evidence about the population it came from. Per-record hashes don't fix this:
you can seal fifty records, reveal the six that look good, and every revealed
hash verifies perfectly while the record is a lie.

denom fixes the DENOMINATOR. Every record is sealed at creation into an
append-only, hash-chained vault. Periodically the vault emits an ANCHOR — the
record COUNT, a Merkle root over all commitments, and the chain head — which
the operator publishes somewhere they do not control (a git commit, an RFC 3161
token, a transparency log). Contents stay private. Later, any subset can be
disclosed with inclusion proofs, and a verifier — run by the auditor, without
trusting the operator — confirms each disclosed record was sealed before the
anchor AND that the disclosed subset comes from a population of exactly the
committed size. Cherry-picking stays possible; UNDETECTABLE cherry-picking
does not, because the denominator is on the record.

WHAT THIS DOES NOT PROVE (printed here because an evidence tool that
overclaims is worse than none):
  1. It proves the sealed population's size, not that every output your
     system produced was sealed. Binding "sealed set == all outputs" is a
     deployment control: enforce sealing in the serving path and reconcile
     vault counts against inference/billing logs. denom report prints this
     residual discretion on its face.
  2. The anchor's TIME is only as strong as where you publish it. Publish
     where you do not control the clock.
  3. Sealing proves existence and integrity, not quality, legality, or
     truthfulness of the record.

COMMANDS
  denom.py init  [--vault DIR]
  denom.py seal  (--file F | --text S | --stdin) [--meta k=v ...]
  denom.py anchor
  denom.py disclose --seq N [N ...] [--anchor FILE] [--out FILE]
  denom.py verify-bundle BUNDLE [--anchor FILE]
  denom.py audit
  denom.py report

CRYPTOGRAPHY
  SHA-256 throughout, with domain separation. Merkle tree per RFC 6962
  (Certificate Transparency): leaf = H(0x00 || data), node = H(0x01 || L || R),
  unbalanced split at the largest power of two — no leaf duplication, so the
  known duplicate-leaf malleability (CVE-2012-2459 class) does not apply.
  Commitment = H(TAG || salt(32B urandom) || H(content) || H(canonical-meta)).
  Chain: h_i = H(TAG || h_{i-1} || canonical-entry-core), genesis prev = 0^64.
"""

import argparse
import base64
import hashlib
import json
import os
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1.0"
PROTO = "DENOM1"

TAG_COMMIT = f"{PROTO}|commit|".encode()
TAG_CHAIN = f"{PROTO}|chain|".encode()
TAG_LEAF = b"\x00"
TAG_NODE = b"\x01"

GENESIS = "0" * 64


# ---------------------------------------------------------------- utilities
def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def write_json(p: Path, obj):
    p.write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n",
                 encoding="utf-8")


# ------------------------------------------------------- commitment scheme
def commitment(salt_hex: str, content: bytes, meta: dict) -> str:
    return sha256(TAG_COMMIT + bytes.fromhex(salt_hex)
                  + bytes.fromhex(sha256(content))
                  + bytes.fromhex(sha256(canon(meta))))


def chain_hash(prev_hex: str, entry_core: dict) -> str:
    return sha256(TAG_CHAIN + bytes.fromhex(prev_hex) + canon(entry_core))


# ----------------------------------------------------- RFC 6962-style tree
def _leaf(commit_hex: str) -> bytes:
    return hashlib.sha256(TAG_LEAF + bytes.fromhex(commit_hex)).digest()


def _node(l: bytes, r: bytes) -> bytes:
    return hashlib.sha256(TAG_NODE + l + r).digest()


def _mth(leaves):
    n = len(leaves)
    if n == 0:
        return hashlib.sha256(b"").digest()
    if n == 1:
        return leaves[0]
    k = 1
    while k * 2 < n:
        k *= 2
    return _node(_mth(leaves[:k]), _mth(leaves[k:]))


def merkle_root(commits) -> str:
    return _mth([_leaf(c) for c in commits]).hex()


def merkle_path(commits, index):
    """RFC 6962 audit path for leaf `index` (0-based). Returns list of
    {"hash": hex, "side": "L"|"R"} from leaf level upward."""
    leaves = [_leaf(c) for c in commits]

    def path(lv, i):
        n = len(lv)
        if n == 1:
            return []
        k = 1
        while k * 2 < n:
            k *= 2
        if i < k:
            return path(lv[:k], i) + [{"hash": _mth(lv[k:]).hex(), "side": "R"}]
        return path(lv[k:], i - k) + [{"hash": _mth(lv[:k]).hex(), "side": "L"}]

    return path(leaves, index)


def merkle_verify(commit_hex, index, count, path, root_hex) -> bool:
    if not (0 <= index < count):
        return False
    h = _leaf(commit_hex)
    # replay the RFC6962 shape for (index, count) to check path length/sides
    i, n, expect = index, count, []
    while n > 1:
        k = 1
        while k * 2 < n:
            k *= 2
        if i < k:
            expect.append("R")
            n = k
        else:
            expect.append("L")
            i -= k
            n -= k
    expect.reverse()
    if [p["side"] for p in path] != expect:
        return False
    for p in path:
        sib = bytes.fromhex(p["hash"])
        h = _node(h, sib) if p["side"] == "R" else _node(sib, h)
    return h.hex() == root_hex


# ---------------------------------------------------------------- the vault
def vault_dir(args) -> Path:
    return Path(getattr(args, "vault", None) or "denom_vault")


def load_vault(args):
    v = vault_dir(args)
    cp = v / "chain.json"
    if not cp.exists():
        die(f"no vault at {v} — run: denom.py init")
    return v, read_json(cp)


def die(msg, code=1):
    print(f"denom: {msg}", file=sys.stderr)
    sys.exit(code)


# ---------------------------------------------------------------- commands
def cmd_init(args):
    v = vault_dir(args)
    if (v / "chain.json").exists():
        die(f"vault already exists at {v}")
    (v / "openings").mkdir(parents=True, exist_ok=True)
    write_json(v / "chain.json", {
        "denom": VERSION, "protocol": PROTO,
        "vault_id": secrets.token_hex(8),
        "created": now_utc(), "entries": []})
    (v / "PRIVATE_DO_NOT_PUBLISH.txt").write_text(
        "This vault's openings/ directory contains salts and record contents.\n"
        "It must NEVER reach a public repository or shared storage.\n"
        "Only ANCHOR files and DISCLOSURE bundles you deliberately export are\n"
        "shareable. If this directory sits inside a git working tree, add it\n"
        "to .gitignore before anything else.\n", encoding="utf-8")
    print(f"vault created at {v}")
    print("WARNING: openings/ holds private material — keep the vault out of "
          "any public repo.")
    return 0


def cmd_seal(args):
    v, chain = load_vault(args)
    if args.file:
        content = Path(args.file).read_bytes()
        src = os.path.basename(args.file)
    elif args.text is not None:
        content = args.text.encode("utf-8")
        src = "text"
    else:
        content = sys.stdin.buffer.read()
        src = "stdin"
    meta = {}
    for kv in (args.meta or []):
        if "=" not in kv:
            die(f"--meta expects k=v, got {kv!r}")
        k, val = kv.split("=", 1)
        meta[k] = val

    seq = len(chain["entries"])
    salt = secrets.token_hex(32)
    ts = now_utc()
    com = commitment(salt, content, meta)
    prev = chain["entries"][-1]["chain_hash"] if chain["entries"] else GENESIS
    core = {"seq": seq, "ts": ts, "commit": com}
    entry = dict(core)
    entry["prev"] = prev
    entry["chain_hash"] = chain_hash(prev, core)
    chain["entries"].append(entry)
    write_json(v / "chain.json", chain)
    write_json(v / "openings" / f"{seq:08d}.json", {
        "seq": seq, "ts": ts, "salt": salt,
        "content_b64": base64.b64encode(content).decode(),
        "content_sha256": sha256(content),
        "meta": meta, "source": src, "commit": com})
    print(f"sealed  seq={seq}  commit={com[:16]}…  count={seq+1}  "
          f"head={entry['chain_hash'][:16]}…")
    return 0


def cmd_anchor(args):
    v, chain = load_vault(args)
    ents = chain["entries"]
    if not ents:
        die("nothing sealed yet")
    commits = [e["commit"] for e in ents]
    anchor = {
        "denom": VERSION, "protocol": PROTO,
        "vault_id": chain["vault_id"],
        "count": len(ents),
        "first_seq": 0, "last_seq": len(ents) - 1,
        "merkle_root": merkle_root(commits),
        "chain_head": ents[-1]["chain_hash"],
        "generated_at": now_utc()}
    out = v / f"ANCHOR_{anchor['count']:08d}.json"
    write_json(out, anchor)
    a_hash = sha256(canon(anchor))
    print(f"anchor written -> {out}")
    print(f"count        {anchor['count']}")
    print(f"merkle_root  {anchor['merkle_root']}")
    print(f"chain_head   {anchor['chain_head']}")
    print(f"anchor sha256({'{'}canonical{'}'})  {a_hash}")
    print()
    print("PUBLISH the anchor (or its sha256) somewhere you do not control the")
    print("clock: a git commit on a public host, an RFC 3161 timestamp, a")
    print("transparency log. The anchor's evidentiary weight equals the")
    print("independence of where it lands.")
    return 0


def cmd_disclose(args):
    v, chain = load_vault(args)
    ents = chain["entries"]
    if args.anchor:
        anchor = read_json(Path(args.anchor))
    else:
        anchors = sorted(v.glob("ANCHOR_*.json"))
        if not anchors:
            die("no anchor found — run: denom.py anchor")
        anchor = read_json(anchors[-1])
    n = anchor["count"]
    commits = [e["commit"] for e in ents[:n]]
    if merkle_root(commits) != anchor["merkle_root"]:
        die("vault does not reproduce the anchor's merkle_root — the chain "
            "changed after anchoring, or the wrong anchor was given. Refusing.")
    bundle = {"denom": VERSION, "protocol": PROTO,
              "anchor": anchor, "disclosed": []}
    for s in args.seq:
        if not (0 <= s < n):
            die(f"seq {s} is outside the anchored population [0, {n-1}]")
        op = read_json(v / "openings" / f"{s:08d}.json")
        bundle["disclosed"].append({
            "seq": s, "ts": ents[s]["ts"], "salt": op["salt"],
            "content_b64": op["content_b64"],
            "content_sha256": op["content_sha256"],
            "meta": op["meta"], "commit": ents[s]["commit"],
            "path": merkle_path(commits, s)})
    out = Path(args.out) if args.out else Path(
        f"DISCLOSURE_{len(args.seq)}of{n}_{now_utc().replace(':','')}.json")
    write_json(out, bundle)
    print(f"disclosure bundle -> {out}")
    print(f"  {len(args.seq)} of {n} sealed records disclosed "
          f"({100*len(args.seq)/n:.1f}%) — the denominator travels with the "
          f"bundle.")
    return 0


def cmd_verify_bundle(args):
    b = read_json(Path(args.bundle))
    anchor = read_json(Path(args.anchor)) if args.anchor else b["anchor"]
    ok = True
    if args.anchor and canon(anchor) != canon(b["anchor"]):
        print("FAIL  bundle's embedded anchor differs from the supplied one")
        ok = False
    n, root = anchor["count"], anchor["merkle_root"]
    print(f"anchor: count={n}  root={root[:16]}…  head="
          f"{anchor['chain_head'][:16]}…  at {anchor['generated_at']}")
    for d in b["disclosed"]:
        content = base64.b64decode(d["content_b64"])
        line = f"  seq {d['seq']:>6}"
        if sha256(content) != d["content_sha256"]:
            print(line + "  FAIL content hash mismatch"); ok = False; continue
        if commitment(d["salt"], content, d["meta"]) != d["commit"]:
            print(line + "  FAIL commitment does not reopen"); ok = False; continue
        if not merkle_verify(d["commit"], d["seq"], n, d["path"], root):
            print(line + "  FAIL inclusion proof invalid"); ok = False; continue
        print(line + f"  OK  sealed {d['ts']}  ({len(content)} bytes)")
    print()
    if ok:
        print(f"VERIFIED — {len(b['disclosed'])} disclosed record(s) reopen "
              f"correctly and prove membership in a sealed population of "
              f"exactly {n}.")
        print("What this proves: each record existed, unmodified, when the "
              "anchor was made, inside a population whose size the operator "
              "committed to in advance.")
        print("What it does not prove: that the population contains every "
              "output the operator's system produced, nor anything about the "
              "records held back. The denominator is honest; the sampling is "
              "still the discloser's choice, made in the open.")
        return 0
    print("VERIFICATION FAILED — do not rely on this bundle.")
    return 1


def cmd_audit(args):
    v, chain = load_vault(args)
    ents = chain["entries"]
    prev, bad = GENESIS, 0
    for e in ents:
        core = {"seq": e["seq"], "ts": e["ts"], "commit": e["commit"]}
        if e["prev"] != prev or e["chain_hash"] != chain_hash(prev, core):
            print(f"  CHAIN BREAK at seq {e['seq']}"); bad += 1
        prev = e["chain_hash"]
        op = v / "openings" / f"{e['seq']:08d}.json"
        if not op.exists():
            print(f"  MISSING opening for seq {e['seq']}"); bad += 1
            continue
        o = read_json(op)
        content = base64.b64decode(o["content_b64"])
        if commitment(o["salt"], content, o["meta"]) != e["commit"]:
            print(f"  OPENING MISMATCH at seq {e['seq']}"); bad += 1
    if bad:
        print(f"AUDIT FAILED — {bad} defect(s). The vault has been altered or "
              f"corrupted; anchors made after the damage are unreliable.")
        return 1
    print(f"AUDIT PASS — {len(ents)} entries, chain intact, every opening "
          f"reopens its commitment.")
    return 0


def cmd_report(args):
    v, chain = load_vault(args)
    ents = chain["entries"]
    anchors = sorted(v.glob("ANCHOR_*.json"))
    print("DENOM COMPLETENESS REPORT")
    print("-" * 60)
    print(f"vault {chain['vault_id']} · created {chain['created']}")
    print(f"sealed records: {len(ents)}")
    if ents:
        print(f"first sealed {ents[0]['ts']} · last sealed {ents[-1]['ts']}")
        print(f"chain head   {ents[-1]['chain_hash']}")
    print(f"anchors emitted: {len(anchors)}"
          + (f" (latest covers {read_json(anchors[-1])['count']})" if anchors
             else ""))
    print()
    print("DISCLOSED DISCRETIONS (stated on the face, per the method):")
    print("  1. Capture completeness — this vault proves the size of what was")
    print("     SEALED, not that everything produced was sealed. Close the gap")
    print("     with pipeline enforcement + reconciliation against inference")
    print("     or billing logs, and state the reconciliation in the audit.")
    print("  2. Anchor independence — anchors are only as strong as where")
    print("     they are published. Name the venue in the engagement letter.")
    print("  3. Sampling — which records get disclosed remains the")
    print("     discloser's choice; the mechanism makes the choice visible,")
    print("     not neutral.")
    return 0


def main():
    ap = argparse.ArgumentParser(prog="denom.py",
                                 description="count-committed sealing for "
                                             "AI-generated records")
    ap.add_argument("--vault", default=None, help="vault directory "
                                                 "(default: denom_vault)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    s = sub.add_parser("seal")
    g = s.add_mutually_exclusive_group()
    g.add_argument("--file"); g.add_argument("--text")
    s.add_argument("--meta", action="append")
    sub.add_parser("anchor")
    d = sub.add_parser("disclose")
    d.add_argument("--seq", type=int, nargs="+", required=True)
    d.add_argument("--anchor"); d.add_argument("--out")
    vb = sub.add_parser("verify-bundle")
    vb.add_argument("bundle"); vb.add_argument("--anchor")
    sub.add_parser("audit")
    sub.add_parser("report")
    a = ap.parse_args()
    return {"init": cmd_init, "seal": cmd_seal, "anchor": cmd_anchor,
            "disclose": cmd_disclose, "verify-bundle": cmd_verify_bundle,
            "audit": cmd_audit, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
