#!/usr/bin/env python3
"""
decc_conformance.py — the DECC-26 conformance test suite.
Version 0.1.0 · standard library only.

WHY THIS FILE IS THE ASSET
A specification without a test suite is a PDF. A specification WITH one is a
thing others can be measured against — which is what makes "DECC-26 conformant"
a claim with content, and what makes the standard licensable rather than merely
published. This suite tests any implementation, not just the reference one.

IMPLEMENTATION-AGNOSTIC BY DESIGN
The suite drives a vendor through an ADAPTER: a small JSON file naming the
commands for init / seal / anchor / disclose / verify, with {placeholders}. The
built-in adapter drives denom.py. A vendor writes ten lines of JSON and is
measured by exactly the same battery.

WHAT IT TESTS — mapped clause by clause to DECC-26 rev.1
  §3.02  digest width               §5.02  no duplicate-leaf malleability
  §3.03  salt width and uniqueness  §6.01  bundle completeness
  §3.04  canonical determinism      §6.02  denominator travels
  §4.01  append-only chain          §6.03  verification without the operator
  §4.03  tamper detection           §6.05  rejection of 7 forgery classes
  §5.01  anchor field completeness  §8.01  discretions printed on the face

WHAT IT CANNOT TEST, AND SAYS SO
  §5.03/§5.04 anchor venue independence — a fact about the world, not the code.
  §8.01(a) capture completeness — a deployment control, not an artifact property.
  Both are reported as DECLARED, never as PASS, and both are required for
  Level 4. No implementation can test its way to an unqualified completeness
  assertion, which is the point.

    python decc_conformance.py                      # test denom.py
    python decc_conformance.py --adapter vendor.json
    python decc_conformance.py --emit-adapter       # print the adapter schema
"""

import argparse
import base64
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1.0"
STANDARD = "DECC-26 rev.1"

BUILTIN_ADAPTER = {
    "name": "denom.py (reference implementation)",
    "cwd": ".",
    "init": ["{py}", "denom.py", "--vault", "{vault}", "init"],
    "seal": ["{py}", "denom.py", "--vault", "{vault}", "seal",
             "--text", "{text}", "--meta", "k={k}"],
    "anchor": ["{py}", "denom.py", "--vault", "{vault}", "anchor"],
    "anchor_glob": "{vault}/ANCHOR_*.json",
    "chain_path": "{vault}/chain.json",
    "disclose": ["{py}", "denom.py", "--vault", "{vault}", "disclose",
                 "--seq", "{seqs}", "--out", "{out}"],
    "verify": ["{py}", "denom.py", "--vault", "{vault}", "verify-bundle",
               "{bundle}"],
    "audit": ["{py}", "denom.py", "--vault", "{vault}", "audit"],
    "report": ["{py}", "denom.py", "--vault", "{vault}", "report"],
    "verify_fail_markers": ["VERIFICATION FAILED", "FAIL"],
    "audit_fail_markers": ["AUDIT FAILED", "CHAIN BREAK"],
}


class R:
    def __init__(self):
        self.rows = []

    def add(self, clause, desc, status, note=""):
        self.rows.append({"clause": clause, "test": desc,
                          "status": status, "note": note})

    def count(self, s):
        return sum(1 for r in self.rows if r["status"] == s)


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True,
                          timeout=120)


def fill(tpl, **kw):
    out = []
    for part in tpl:
        s = part
        for k, v in kw.items():
            s = s.replace("{" + k + "}", str(v))
        out.append(s)
    return out


def fillstr(s, **kw):
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def naive_dup_root(commits):
    """The construction DECC-26 §5.02 forbids: duplicate the last odd leaf."""
    lv = [hashlib.sha256(bytes.fromhex(c)).digest() for c in commits]
    if not lv:
        return None
    while len(lv) > 1:
        if len(lv) % 2:
            lv.append(lv[-1])
        lv = [hashlib.sha256(lv[i] + lv[i + 1]).digest()
              for i in range(0, len(lv), 2)]
    return lv[0].hex()


def main():
    ap = argparse.ArgumentParser(prog="decc_conformance.py")
    ap.add_argument("--adapter", help="vendor adapter JSON")
    ap.add_argument("--emit-adapter", action="store_true")
    ap.add_argument("--out", default="DECC_CONFORMANCE_REPORT.json")
    ap.add_argument("--keep", action="store_true", help="keep the scratch vault")
    a = ap.parse_args()

    if a.emit_adapter:
        print(json.dumps(BUILTIN_ADAPTER, indent=2))
        return 0

    ad = json.loads(Path(a.adapter).read_text(encoding="utf-8")) if a.adapter \
        else BUILTIN_ADAPTER
    cwd = Path(ad.get("cwd", ".")).resolve()
    r = R()
    tmp = Path(tempfile.mkdtemp())
    vault = tmp / "conf_vault"
    py = sys.executable
    N = 9

    try:
        # ---------------------------------------------------------- setup
        run(fill(ad["init"], py=py, vault=vault), cwd)
        for i in range(N):
            run(fill(ad["seal"], py=py, vault=vault,
                     text=f"conformance record {i}", k=f"v{i}"), cwd)
        run(fill(ad["anchor"], py=py, vault=vault), cwd)

        anchors = sorted(Path(fillstr(ad["anchor_glob"], vault=vault)
                              ).parent.glob(
            Path(fillstr(ad["anchor_glob"], vault=vault)).name))
        if not anchors:
            r.add("5.01", "anchor artifact produced", "FAIL",
                  "no anchor file found")
            raise SystemExit(emit(r, ad, a.out))
        anchor = json.loads(anchors[-1].read_text(encoding="utf-8"))

        bundle_p = tmp / "b.json"
        seqs = ["0", "3", "8"]
        cmd = fill(ad["disclose"], py=py, vault=vault, out=bundle_p,
                   seqs=" ".join(seqs))
        # expand a single {seqs} token into multiple argv entries
        expanded = []
        for tok in cmd:
            expanded.extend(tok.split()) if tok == " ".join(seqs) else \
                expanded.append(tok)
        run(expanded, cwd)
        if not bundle_p.exists():
            r.add("6.01", "disclosure bundle produced", "FAIL",
                  "no bundle written")
            raise SystemExit(emit(r, ad, a.out))
        bundle = json.loads(bundle_p.read_text(encoding="utf-8"))

        # ------------------------------------------------ §5.01 anchor fields
        need = {"count": None, "merkle_root": None, "chain_head": None}
        missing = [k for k in need if k not in anchor]
        r.add("5.01", "anchor carries count, root, chain head",
              "PASS" if not missing else "FAIL",
              "" if not missing else f"missing {missing}")
        r.add("5.01", "anchor carries a generation timestamp",
              "PASS" if any("gener" in k or "time" in k or "at" in k
                            for k in anchor) else "FAIL")

        # -------------------------------------------- §6.01/§6.02 bundle shape
        disc = bundle.get("disclosed") or bundle.get("records") or []
        r.add("6.01", "bundle carries openings and inclusion proofs",
              "PASS" if disc and all(
                  ("salt" in d and "path" in d and "commit" in d)
                  for d in disc) else "FAIL")
        emb = bundle.get("anchor", {})
        r.add("6.02", "denominator travels with the disclosure",
              "PASS" if int(emb.get("count", 0)) == N else "FAIL",
              f"expected {N}, found {emb.get('count')}")

        # ------------------------------------------------- §3.02 digest width
        widths = {len(d["commit"]) for d in disc}
        r.add("3.02", "commitment digest at least 256 bits",
              "PASS" if widths and min(widths) >= 64 else "FAIL",
              f"hex widths {sorted(widths)}")

        # ------------------------------- §3.03 salt width and per-record unique
        salts = [d["salt"] for d in disc]
        wide = all(len(s) >= 64 for s in salts)
        uniq = len(set(salts)) == len(salts)
        r.add("3.03", "salt at least 32 bytes",
              "PASS" if wide else "FAIL",
              f"min hex len {min((len(s) for s in salts), default=0)}")
        r.add("3.03", "salt unique per record",
              "PASS" if uniq else "FAIL")
        # crude entropy floor: salts must not share long prefixes
        pref = len({s[:16] for s in salts}) == len(salts)
        r.add("3.03", "salts show no structural prefix collision",
              "PASS" if pref else "FAIL")

        # --------------------------------------- §6.03 verification standalone
        v = run(fill(ad["verify"], py=py, vault=vault, bundle=bundle_p), cwd)
        clean = v.returncode == 0 and not any(
            m in v.stdout for m in ad["verify_fail_markers"])
        r.add("6.03", "honest bundle verifies", "PASS" if clean else "FAIL")
        # verify from a directory with no vault present
        iso = tmp / "iso"
        iso.mkdir(exist_ok=True)
        shutil.copy2(bundle_p, iso / "b.json")
        for f in Path(cwd).glob("denom*.py"):
            shutil.copy2(f, iso / f.name)
        v2 = run(fill(ad["verify"], py=py, vault=iso / "nonexistent_vault",
                      bundle=iso / "b.json"), iso)
        ok_iso = v2.returncode == 0 and "VERIFIED" in v2.stdout
        r.add("6.03", "verifies with no vault and no operator service",
              "PASS" if ok_iso else "FAIL",
              "relying party needs only bundle + verifier")

        # ------------------------------------------ §5.02 duplicate-leaf class
        commits = [json.loads((Path(fillstr(ad["chain_path"], vault=vault))
                               ).read_text(encoding="utf-8"))["entries"][i]
                   ["commit"] for i in range(N)]
        r.add("5.02", "root differs from duplicate-last-leaf construction",
              "PASS" if anchor["merkle_root"] != naive_dup_root(commits)
              else "FAIL", "odd leaf count exercised (N=9)")

        # ------------------------------------------ §6.05 adversarial battery
        forgeries = []

        def forge(label, mut):
            b = copy.deepcopy(bundle)
            mut(b)
            p = tmp / "f.json"
            p.write_text(json.dumps(b), encoding="utf-8")
            res = run(fill(ad["verify"], py=py, vault=vault, bundle=p), cwd)
            rejected = res.returncode != 0 or any(
                m in res.stdout for m in ad["verify_fail_markers"])
            forgeries.append((label, rejected))

        def _content(b, s):
            b["disclosed"][0]["content_b64"] = base64.b64encode(s).decode()

        forge("content altered", lambda b: _content(b, b"FORGED"))

        def _content_and_hash(b):
            s = b"FORGED WITH MATCHING HASH"
            b["disclosed"][0]["content_b64"] = base64.b64encode(s).decode()
            b["disclosed"][0]["content_sha256"] = hashlib.sha256(s).hexdigest()
        forge("content and its hash altered", _content_and_hash)
        forge("salt altered",
              lambda b: b["disclosed"][1].__setitem__("salt", "ab" * 32))
        forge("committed metadata altered",
              lambda b: b["disclosed"][1]["meta"].__setitem__(
                  list(b["disclosed"][1]["meta"])[0], "TAMPERED")
              if b["disclosed"][1].get("meta") else None)
        forge("foreign commitment substituted",
              lambda b: b["disclosed"][2].__setitem__("commit", "e3" * 32))
        forge("sequence index relabelled",
              lambda b: b["disclosed"][0].__setitem__("seq", 5))
        forge("anchor count reduced",
              lambda b: b["anchor"].__setitem__("count", 3))
        forge("anchor root replaced",
              lambda b: b["anchor"].__setitem__("merkle_root", "00" * 32))

        for label, rejected in forgeries:
            r.add("6.05", f"rejects: {label}",
                  "PASS" if rejected else "FAIL",
                  "" if rejected else "*** FORGERY ACCEPTED ***")

        # ------------------------------------- §4.01/§4.03 append-only + audit
        if "audit" in ad:
            au = run(fill(ad["audit"], py=py, vault=vault), cwd)
            r.add("4.01", "clean vault passes audit",
                  "PASS" if au.returncode == 0 else "FAIL")
            cp = Path(fillstr(ad["chain_path"], vault=vault))
            backup = cp.read_text(encoding="utf-8")
            ch = json.loads(backup)
            ch["entries"][4]["commit"] = "aa" * 32
            cp.write_text(json.dumps(ch), encoding="utf-8")
            au2 = run(fill(ad["audit"], py=py, vault=vault), cwd)
            caught = au2.returncode != 0 or any(
                m in au2.stdout for m in ad["audit_fail_markers"])
            r.add("4.03", "retroactive chain edit detected",
                  "PASS" if caught else "FAIL")
            cp.write_text(backup, encoding="utf-8")
        else:
            r.add("4.01", "audit command", "N/A", "adapter declares none")

        # --------------------------------------- §8.01 discretions on the face
        if "report" in ad:
            rep = run(fill(ad["report"], py=py, vault=vault), cwd)
            txt = rep.stdout.lower()
            for key, label in (("captur", "capture completeness"),
                               ("anchor", "anchor independence"),
                               ("sampl", "sampling")):
                r.add("8.01", f"discretion printed: {label}",
                      "PASS" if key in txt else "FAIL")
        else:
            r.add("8.01", "report command", "N/A", "adapter declares none")

        # ------------------------------- untestable-by-construction clauses
        r.add("5.03", "anchor published to an independent venue", "DECLARED",
              "a fact about the world; the operator must name the venue")
        r.add("5.04", "venue independence assessed", "DECLARED",
              "evidentiary weight equals venue independence")
        r.add("8.01a", "capture completeness reconciliation", "DECLARED",
              "deployment control; see denom_capture reconciliation grade")

        return emit(r, ad, a.out)
    finally:
        if not a.keep:
            shutil.rmtree(tmp, ignore_errors=True)


def emit(r, ad, out_path):
    p, f, d, na = (r.count("PASS"), r.count("FAIL"),
                   r.count("DECLARED"), r.count("N/A"))
    print(f"DECC-26 CONFORMANCE — {ad.get('name','unnamed implementation')}")
    print(f"suite {VERSION} · standard {STANDARD}")
    print("=" * 66)
    last = None
    for row in r.rows:
        if row["clause"] != last:
            print(f"  §{row['clause']}")
            last = row["clause"]
        mark = {"PASS": "PASS", "FAIL": "FAIL",
                "DECLARED": "DECL", "N/A": " n/a"}[row["status"]]
        note = f"  — {row['note']}" if row["note"] else ""
        print(f"    [{mark}] {row['test']}{note}")
    print("=" * 66)
    print(f"  {p} passed · {f} failed · {d} declared · {na} not applicable")
    print()

    if f:
        level, verdict = 0, ("NON-CONFORMANT — a failed normative clause is "
                             "disqualifying, not advisory.")
    else:
        level = 3
        verdict = ("LEVEL 3 (Disclosing) on artifact evidence. Level 4 "
                   "requires the DECLARED clauses to be satisfied in "
                   "deployment: an independent anchor venue (§5.03/5.04) and "
                   "an external-grade capture reconciliation (§8.01a). No "
                   "suite can grant Level 4 — that is the standard working "
                   "as designed.")
    print(f"  VERDICT: {verdict}")

    report = {"suite": VERSION, "standard": STANDARD,
              "implementation": ad.get("name"),
              "generated_at": datetime.now(timezone.utc).strftime(
                  "%Y-%m-%dT%H:%M:%SZ"),
              "passed": p, "failed": f, "declared": d, "not_applicable": na,
              "artifact_level": level, "verdict": verdict, "results": r.rows}
    Path(out_path).write_text(json.dumps(report, indent=1) + "\n",
                              encoding="utf-8")
    print(f"  report -> {out_path}")
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main())
