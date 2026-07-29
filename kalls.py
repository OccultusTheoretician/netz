#!/usr/bin/env python3
"""
kalls.py — KNP-26 reference implementation: sealer, hashlog, verifier.

Conformant to KRÄHE'S NEST PROTOCOL, First Edition (KNP-26), which specifies the
wire format for the Selective-Disclosure Commitment Method (KNM-26). This is the
committer's local sealer (KNP 1.01a) plus the third-party verification procedure
(KNP 5.02). It is not an aggregator; the Nest is a separate read-only artifact
(KNP Ch. 6) and this tool holds no other committer's anything.

Field names, preimage construction, and record shapes below are NORMATIVE per
KNP 2.01, 3.01, and 4.01. They are not stylistic choices — an implementation that
renames them stops interoperating, which is the one thing the protocol exists to
prevent.

CANONICAL PREIMAGES (rev. 3: per-record construction, KNP 2.01/2.01b)
    knp-1 (records sealed before rev. 3; a record without a `construction`
           field is knp-1 — the 2026-07 clutch verifies unchanged)
        id | timestamp | statement | resolution_basis | salt
    knp-2 (everything sealed from rev. 3 on — binds the scored inputs)
        id | timestamp | statement | resolution_basis | probability | deadline | salt
joined with the ASCII pipe, no padding, UTF-8, SHA-256, lowercase hex.
Pipes inside statement or resolution_basis are escaped to \\u007C before joining
and unescaped on reveal (KNP 2.01). probability renders as the integer percent —
decimal ASCII, no sign, no point, no percent sign (KNP 2.01b). deadline is the
stored YYYY-MM-DD, verbatim. The other preimage fields are constrained grammars
that cannot contain the separator.

NOT BOUND BY THE HASH under knp-1: probability, deadline — the two inputs to
every Brier score; anchored only through KNP 4.03 history, which the rev. 3
finding prints on the log's face. status and domain are unbound under both
constructions and are frozen-at-sealing per KNP 4.02 as amended (a restated
probability is the cheap cheat; the verifier now compares it across snapshots).

SUBCOMMANDS
    selftest  reproduce a known published commitment — run this before trusting anything
    seal      seal a clutch: vault written, hashlog appended, markdown rows emitted
    verify    vault vs hashlog, every commitment recomputed, chain checked if present
    reveal    emit a KNP 5.01 reveal block for one Kall; sets status REVEALED
    check     KNP 5.02 third-party verification — needs only a reveal block + hashlog
    solve     find the preimage construction the published commitments actually used
    probe     forensics on one Kall: field shapes + targeted construction search
    matrix    cross-pairing sweep: every statement/basis/salt against every commitment
    adopt     convert a markdown vault export into the KNP 3.01 JSON vault
    import    seed the hashlog from the already-published markdown table
    count     the standing line (KNP 4.04): N sealed · M revealed · K resolved
    beacon    print the external-anchor line for syndicate.py to post (KNP 4.03b)
    anchor    compute a chain anchor over an already-published clutch (non-normative)

PATHS (netz repo layout)
    vault   : vault/kalls_vault.json      gitignored by vault/ ; never pushed (KNP 3.03)
    hashlog : docs/kalls_hashlog.json     public
    table   : docs/kraehes_kalls.md       public, human-readable
"""
from __future__ import annotations
import argparse, hashlib, json, re, secrets, sys
import datetime as dt
from pathlib import Path

SEP = "|"
PIPE_ESC = "\\u007C"
CHAIN_LABEL = "KRAEHES-KALLS-CHAIN-v1"
STATUSES = ("SEALED", "REVEALED", "RESOLVED_HIT", "RESOLVED_MISS", "VOID")
CONSTRUCTION: dict | None = None          # set by solve, honoured by every hash op

# KNP 2.01/2.01b — the versioned constructions (rev. 3). A record names its
# construction; absence means knp-1 so the pre-rev.3 clutch verifies untouched.
CONSTRUCTIONS: dict[str, dict] = {
    "knp-1": {"order": ["id", "timestamp", "statement", "resolution_basis", "salt"],
              "separator": SEP, "effective": "2026-07-25"},
    "knp-2": {"order": ["id", "timestamp", "statement", "resolution_basis",
                        "probability", "deadline", "salt"],
              "separator": SEP, "effective": "2026-07-29"},
}
SEAL_CONSTRUCTION = "knp-2"               # KNP 2.01b: new seals bind probability+deadline
VAULT = Path("vault/kalls_vault.json")
HASHLOG = Path("docs/kalls_hashlog.json")
TABLE = Path("docs/kraehes_kalls.md")

ROW_RE = re.compile(
    r"\|\s*([A-Za-z0-9\-]*KK-\d{8}-\d+)\s*\|\s*([0-9TZ:\-]+)\s*\|\s*`?([0-9a-f]{64})`?\s*\|"
    r"\s*(\d+)%\s*\|\s*([0-9\-]+)\s*\|\s*(\w+)\s*\|")


def esc(s: str) -> str:
    return s.replace(SEP, PIPE_ESC)


def unesc(s: str) -> str:
    return s.replace(PIPE_ESC, SEP)


def canon_prob(v) -> str:
    """KNP 2.01b: the integer percent — decimal ASCII, no sign, no point, no %."""
    return str(int(round(float(v))))


def preimage(e: dict, sep: str = SEP) -> str:
    if CONSTRUCTION:                      # forensic override from `solve` — recovery only
        c = CONSTRUCTION
        parts = []
        for f in c["order"]:
            v = str(e.get(f, ""))
            if f == "probability" and v not in ("", "None"):
                n = float(v)
                r = c.get("probability_render", "int")
                v = {"int": str(int(n)), "pct": f"{int(n)}%",
                     "frac": str(n / 100), "frac2": f"{n/100:.2f}"}.get(r, str(int(n)))
            if c.get("escape") and f in ("statement", "resolution_basis"):
                v = esc(v)
            parts.append(v)
        return c["separator"].join(parts)
    ver = e.get("construction", "knp-1")  # KNP 2.01b: absent = knp-1, always
    c = CONSTRUCTIONS.get(ver)
    if c is None:
        die(f"{e.get('id', '?')} names unknown construction {ver!r} — refusing to "
            f"hash under a guess; the published commitment governs (KNP 4.01b)")
    parts = []
    for f in c["order"]:
        if f == "probability":
            parts.append(canon_prob(e[f]))
        elif f in ("statement", "resolution_basis"):
            parts.append(esc(e[f]))
        else:
            parts.append(str(e[f]))
    # sep stays honoured for knp-1 so `selftest`/`solve` can still hunt legacy
    # separators; knp-2 is pinned to its own declared separator by definition.
    return (sep if ver == "knp-1" else c["separator"]).join(parts)


def commit_of(e: dict, sep: str = SEP) -> str:
    return hashlib.sha256(preimage(e, sep).encode("utf-8")).hexdigest()


def sha_raw(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def construction_path(vault: str) -> Path:
    return Path(vault).parent / "kalls_construction.json"


def load_construction(vault: str) -> None:
    global CONSTRUCTION
    p = construction_path(vault)
    if p.exists():
        CONSTRUCTION = json.loads(p.read_text(encoding="utf-8"))


def construction_line(ver: str = "knp-1") -> str:
    if CONSTRUCTION:
        return (f"SHA-256( {CONSTRUCTION['separator'].join(CONSTRUCTION['order'])} )"
                if CONSTRUCTION["separator"].strip()
                else f"SHA-256( {' + '.join(CONSTRUCTION['order'])}, no separator )")
    c = CONSTRUCTIONS.get(ver, CONSTRUCTIONS["knp-1"])
    return f"SHA-256( {' | '.join(c['order'])} )"


def die(msg: str, code: int = 2):
    print(f"KALLS · REFUSED · {msg}", file=sys.stderr)
    sys.exit(code)


def load_json(p: Path, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def _con_block(ver: str) -> dict:
    c = CONSTRUCTIONS[ver]
    return {"version": ver, "preimage_order": list(c["order"]), "separator": c["separator"],
            "hash": "SHA-256", "encoding": "UTF-8", "pipe_escape": PIPE_ESC,
            "probability_render": "integer percent, decimal ASCII (KNP 2.01b)"
            if "probability" in c["order"] else None,
            "effective": c["effective"]}


def stamp_log(log: dict) -> dict:
    log["protocol"] = "KNP-26"
    if CONSTRUCTION:
        log["construction"] = {
            "preimage_order": CONSTRUCTION["order"], "separator": CONSTRUCTION["separator"],
            "hash": "SHA-256", "encoding": "UTF-8", "pipe_escape": PIPE_ESC}
        return log
    # KNP 4.01c: the singular block states the log's EARLIEST construction so a
    # rev.2 verifier stays correct on every legacy record (conservative failure:
    # it false-alarms on a knp-2 reveal, it never false-passes). The history
    # carries every construction; a record's own `construction` field selects.
    log.setdefault("construction", {
        "preimage_order": ["id", "timestamp", "statement", "resolution_basis", "salt"],
        "separator": SEP, "hash": "SHA-256", "encoding": "UTF-8",
        "pipe_escape": PIPE_ESC})
    log["construction"].setdefault("version", "knp-1")
    hist = {b["version"]: b for b in log.get("construction_history", [])
            if isinstance(b, dict) and b.get("version")}
    for ver in CONSTRUCTIONS:
        hist.setdefault(ver, {k: v for k, v in _con_block(ver).items() if v is not None})
    log["construction_history"] = [hist[v] for v in sorted(hist)]
    return log


def save_json(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def load_vault(p: Path) -> list[dict]:
    d = load_json(p, [])
    if isinstance(d, dict):
        d = d.get("entries") or d.get("records") or d.get("kalls") or []
    return d


def load_log(p: Path) -> dict:
    d = load_json(p, None)
    if d is None:
        return {"protocol": "KNP-26", "records": []}
    if isinstance(d, list):                       # bare-array hashlog: accept, normalize
        return {"protocol": "KNP-26", "records": d}
    d.setdefault("records", d.pop("entries", []))
    return d


def parse_table(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [{"id": m.group(1), "timestamp": m.group(2), "commitment": m.group(3),
             "probability": int(m.group(4)), "deadline": m.group(5), "status": m.group(6)}
            for m in ROW_RE.finditer(p.read_text(encoding="utf-8"))]


def norm(e: dict) -> dict:
    """Accept legacy field names from a hand-made vault; emit KNP-26 names."""
    out = dict(e)
    for old, new in (("timestamp_utc", "timestamp"), ("seal", "commitment"),
                     ("hash", "commitment"), ("p", "probability"), ("basis", "resolution_basis")):
        if old in out and new not in out:
            out[new] = out.pop(old)
    if isinstance(out.get("probability"), float) and out["probability"] <= 1:
        out["probability"] = int(round(out["probability"] * 100))
    return out


# --------------------------------------------------------------- selftest
def cmd_selftest(a) -> int:
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    e = next((x for x in vault if x["id"] == a.id), None)
    if not e:
        die(f"{a.id} not in the vault at {a.vault}")
    published = None
    for r in parse_table(Path(a.table)) + load_log(Path(a.hashlog))["records"]:
        if r["id"] == a.id:
            published = r["commitment"]
            break
    published = published or e.get("commitment")
    if not published:
        die(f"no published commitment found for {a.id} to test against")
    for sep in (a.sep, "|", "", " | ", "\n", ":"):
        if commit_of(e, sep) == published:
            print(f"PASS  {a.id}  ·  separator {sep!r}  ·  KNP 2.01 construction reproduced")
            if sep != SEP:
                print(f"      NOTE: the clutch used {sep!r}, not the pipe KNP 2.01 mandates.\n"
                      f"      The commitment governs; the spec text is what needs amending.")
            return 0
    print(f"FAIL  {a.id}", file=sys.stderr)
    print(f"  published : {published}", file=sys.stderr)
    print(f"  computed  : {commit_of(e, a.sep)}", file=sys.stderr)
    print("\nThe clutch was sealed with a different field order or separator than KNP 2.01\n"
          "states. Recover the original construction and amend the spec to match it — the\n"
          "published commitment is the binding artifact and is never edited to fit a tool.",
          file=sys.stderr)
    return 1


# ------------------------------------------------------------------- seal
def cmd_seal(a) -> int:
    drafts = load_json(Path(a.draft), None)
    if drafts is None:
        die(f"draft not found: {a.draft}")
    drafts = [drafts] if isinstance(drafts, dict) else drafts
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    log = load_log(Path(a.hashlog))
    # KNP 4.02 standing guard (rev. 3): never extend a log whose past does not
    # verify. Every existing vault record is recomputed under its own declared
    # construction before a single byte is written; one failure aborts the seal.
    dirty = [e["id"] for e in vault
             if e.get("commitment") and commit_of(e, SEP) != e["commitment"]]
    if dirty:
        die(f"{len(dirty)} existing record(s) fail verification under their own "
            f"construction: {', '.join(dirty)} — sealing refused. Run `verify`; "
            f"print the finding; never repair silently (KNP 4.02).")
    known = ({e["id"] for e in vault} | {r["id"] for r in log["records"]}
             | {r["id"] for r in parse_table(Path(a.table))} | set(log.get("anchored_over", [])))

    now = a.timestamp or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    day = now[:10].replace("-", "")
    pre = a.prefix + "-" if a.prefix else ""
    seq = 1 + sum(1 for i in known if i.startswith(f"{pre}KK-{day}-"))
    head = log.get("head")  # NOT anchor: anchor is a prose disclosure object, not a chain hash

    new_v, new_p = [], []
    for d in drafts:
        for req in ("statement", "resolution_basis", "probability", "deadline"):
            if not str(d.get(req, "")).strip():
                die(f"draft missing `{req}` — {str(d)[:60]}")
        p = float(d["probability"])
        p = p * 100 if p <= 1 else p
        if p <= 0 or p >= 100:
            die(f"probability {p} is a certainty claim, not a forecast")
        if len(str(d["resolution_basis"]).split()) < 4:
            die("resolution_basis too thin for a stranger to resolve (KNP 5.02)")
        kid = d.get("id") or f"{pre}KK-{day}-{seq:02d}"
        if kid in known:
            die(f"{kid} already committed — a commitment is never rewritten (KNM 3.06)")
        seq += 1
        known.add(kid)
        e = {"id": kid, "timestamp": now, "statement": d["statement"].strip(),
             "resolution_basis": d["resolution_basis"].strip(),
             "probability": int(round(p)), "deadline": d["deadline"],
             "salt": secrets.token_hex(16),                      # KNP 2.01: 128-bit minimum
             "construction": SEAL_CONSTRUCTION}                  # KNP 2.01b: binds prob+deadline
        e["commitment"] = commit_of(e, SEP)
        rec = {"id": kid, "timestamp": now, "commitment": e["commitment"],
               "probability": e["probability"], "deadline": e["deadline"],
               "construction": SEAL_CONSTRUCTION, "status": "SEALED"}
        for opt in ("domain", "level", "architecture", "reveal_date"):
            if d.get(opt) is not None:
                rec[opt] = e[opt] = d[opt]
        if head:                                    # non-normative chain extension
            head = sha_raw(SEP.join([head, e["commitment"]]))
            rec["chain"] = head
        new_v.append(e); new_p.append(rec)

    if a.dry_run:
        for r in new_p:
            print(f"{r['id']}  {r['commitment']}  {r['probability']}%  {r['deadline']}")
        print("\nDRY RUN — nothing written; salts generated and discarded.")
        return 0

    save_json(Path(a.vault), vault + new_v)
    log["records"].extend(new_p)
    if head:
        log["head"] = head
    save_json(Path(a.hashlog), stamp_log(log))
    print(f"sealed {len(new_p)}  ·  vault {a.vault}  ·  hashlog {a.hashlog}")
    print("\nMarkdown rows — APPEND ONLY, never edit a row above (KNM 3.06):")
    for r in new_p:
        print(f"|{r['id']}|{r['timestamp']}|`{r['commitment']}`|{r['probability']}%|"
              f"{r['deadline']}|SEALED|")
    print("\nKNP 3.04: the vault is the critical secret. A lost salt makes that Kall\n"
          "permanently unrevealable. Back it up privately before you close the session.")
    return 0


# ----------------------------------------------------------------- verify
def cmd_verify(a) -> int:
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    log = load_log(Path(a.hashlog))
    table = {r["id"]: r for r in parse_table(Path(a.table))}
    vids = {e["id"] for e in vault}
    bad = 0

    for e in vault:
        if e.get("commitment") and commit_of(e, a.sep) != e["commitment"]:
            print(f"COMMITMENT MISMATCH  {e['id']} — vault content does not reproduce its "
                  f"own hash", file=sys.stderr); bad += 1
    by_vid = {e["id"]: e for e in vault}
    for r in log["records"]:
        if r["id"] in table and table[r["id"]]["commitment"] != r["commitment"]:
            print(f"LOG/TABLE DIVERGE    {r['id']}", file=sys.stderr); bad += 1
        if r.get("status") and r["status"] not in STATUSES:
            print(f"BAD STATUS           {r['id']} = {r['status']} (KNP 4.01)",
                  file=sys.stderr); bad += 1
        if r["id"] not in vids:
            print(f"UNOPENABLE           {r['id']} — published, no vault record; "
                  f"permanently dark (KNP 3.04)", file=sys.stderr); bad += 1
        v = by_vid.get(r["id"])
        if v is not None:                    # KNP 4.02 (rev. 3): frozen at sealing
            if "probability" in r and "probability" in v and \
                    canon_prob(r["probability"]) != canon_prob(v["probability"]):
                print(f"METADATA DIVERGE     {r['id']} — probability differs between "
                      f"vault and hashlog; a restated probability is the cheap cheat "
                      f"(KNP 4.02)", file=sys.stderr); bad += 1
            if "deadline" in r and "deadline" in v and \
                    str(r["deadline"]) != str(v["deadline"]):
                print(f"METADATA DIVERGE     {r['id']} — deadline differs between "
                      f"vault and hashlog (KNP 4.02)", file=sys.stderr); bad += 1
            if r.get("construction", "knp-1") != v.get("construction", "knp-1"):
                print(f"CONSTRUCTION SPLIT   {r['id']} — vault and hashlog name "
                      f"different constructions (KNP 2.01b)", file=sys.stderr); bad += 1
    head = log.get("head")  # chain seed, not the KNP 4.03 disclosure block
    if head:
        for r in log["records"]:
            head = sha_raw(SEP.join([head, r["commitment"]]))
            if r.get("chain") and r["chain"] != head:
                print(f"CHAIN BREAK          {r['id']} — a record above it changed",
                      file=sys.stderr); bad += 1
    for t in table.values():
        if t["id"] not in vids and t["id"] not in {r["id"] for r in log["records"]}:
            print(f"UNTRACKED            {t['id']} — on the public table, in neither the "
                  f"hashlog nor the vault", file=sys.stderr); bad += 1

    if bad:
        print(f"\nVERIFY FAILED — {bad} finding(s). Print them; never repair silently.",
              file=sys.stderr)
        return 1
    print(f"VERIFY PASS · vault {len(vault)} · hashlog {len(log['records'])} · "
          f"table {len(table)}")
    return 0


# ----------------------------------------------------------------- reveal
def cmd_reveal(a) -> int:
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    e = next((x for x in vault if x["id"] == a.id), None)
    if not e:
        die(f"{a.id} not in the vault — nothing to open")
    c = e.get("commitment") or commit_of(e, a.sep)
    if commit_of(e, a.sep) != c:
        die(f"{a.id} fails its own check — refusing to publish an unverifiable reveal")
    ver = e.get("construction", "knp-1")
    block = (f"## REVEAL — {e['id']}\n\n"
             f"**Sealed:** {e['timestamp']}  ·  **Probability:** {e['probability']}%  ·  "
             f"**Deadline:** {e['deadline']}\n\n"
             f"**Statement:** {unesc(e['statement'])}\n\n"
             f"**Resolution basis:** {unesc(e['resolution_basis'])}\n\n"
             f"**Salt:** `{e['salt']}`\n\n**Commitment:** `{c}`\n\n"
             f"**Construction:** `{ver}`\n\n"
             f"Verify per KNP 5.02: `{construction_line(ver)}`\n")
    if a.out:
        Path(a.out).write_text(block, encoding="utf-8")
        print(f"reveal written: {a.out}")
    else:
        print(block)
    if not a.no_status:
        log = load_log(Path(a.hashlog))
        for r in log["records"]:
            if r["id"] == a.id and r.get("status") == "SEALED":
                r["status"] = "REVEALED"
        save_json(Path(a.hashlog), stamp_log(log))
        print("hashlog status -> REVEALED (in place; the record is never removed, KNP 4.02)")
    return 0


# ------------------------------------------------------------------ check
def cmd_check(a) -> int:
    txt = Path(a.reveal).read_text(encoding="utf-8")
    g = lambda lbl: (re.search(rf"\*\*{lbl}:?\*\*\s*`?([^\n`]+)`?", txt) or [None, None])[1]
    kid = re.search(r"REVEAL\s*[—\-]\s*([A-Za-z0-9\-]*KK-\d{8}-\d+)", txt)
    ts = re.search(r"\*\*Sealed:\*\*\s*([0-9TZ:\-]+)", txt)
    pr = re.search(r"\*\*Probability:\*\*\s*(\d+)\s*%", txt)
    dl = re.search(r"\*\*Deadline:\*\*\s*([0-9\-]+)", txt)
    cn = re.search(r"\*\*Construction:\*\*\s*`?(knp-\d+)`?", txt)
    e = {"id": kid.group(1) if kid else None,
         "timestamp": ts.group(1).strip() if ts else None,
         "statement": (g("Statement") or "").strip(),
         "resolution_basis": (g("Resolution basis") or "").strip(),
         "salt": (g("Salt") or "").strip()}
    if not all(e.values()):
        die("reveal block incomplete — cannot verify")
    log_recs = load_log(Path(a.hashlog))["records"]
    hrec = next((r for r in log_recs if r["id"] == e["id"]), None)
    ver = (cn.group(1) if cn else None) or (hrec or {}).get("construction", "knp-1")
    if ver != "knp-1":
        if not (pr and dl):
            die(f"a {ver} reveal must carry Probability and Deadline — both are "
                f"preimage fields (KNP 2.01b)")
        e["probability"] = int(pr.group(1))
        e["deadline"] = dl.group(1)
        e["construction"] = ver
    computed = commit_of(e, a.sep)
    published = hrec["commitment"] if hrec else None
    if published is None:
        published = next((r["commitment"] for r in parse_table(Path(a.table))
                          if r["id"] == e["id"]), None)
    if published is None:
        die(f"{e['id']} is not in the public hashlog — an unlogged reveal proves nothing")
    ok = computed == published
    print(f"{'PASS' if ok else 'FAIL'}  {e['id']}\n  computed  : {computed}\n"
          f"  published : {published}")
    if not ok:
        print("\nThe revealed text does not reproduce the published commitment: the content\n"
              "was altered after sealing, or the reveal is malformed.")
    return 0 if ok else 1


# ------------------------------------------------------------------ count
def cmd_count(a) -> int:
    log = load_log(Path(a.hashlog))
    recs = log["records"] or parse_table(Path(a.table))
    st = {s: sum(1 for r in recs if r.get("status") == s) for s in STATUSES}
    resolved = st["RESOLVED_HIT"] + st["RESOLVED_MISS"]
    print(f"{len(recs)} sealed · {st['REVEALED'] + resolved} revealed · {resolved} resolved")
    print(f"  abyssal {st['SEALED']} · void {st['VOID']} · vault records "
          f"{len(load_vault(Path(a.vault)))}")
    if resolved < 30:
        print(f"  under thirty resolved the score is noise ({resolved}/30) — RPAS, KNM 5.03")
    return 0


# ----------------------------------------------------------------- beacon
def cmd_beacon(a) -> int:
    p = Path(a.hashlog)
    if not p.exists():
        die(f"no hashlog at {a.hashlog}")
    raw = p.read_bytes()
    log = load_log(p)
    recs = log["records"]
    resolved = sum(1 for r in recs if str(r.get("status", "")).startswith("RESOLVED"))
    revealed = sum(1 for r in recs if r.get("status") == "REVEALED") + resolved
    dig = hashlib.sha256(raw).hexdigest()
    print(f"KRÄHE'S KALLS · {len(recs)} sealed · {revealed} revealed · {resolved} resolved")
    print(f"kalls_hashlog.json sha256: {dig}")
    print("\nKNP 4.03b: post this to a surface you do not control. syndicate.py already does\n"
          "exactly this for ledger.json — extend it rather than writing a second poster.\n"
          "Until the count is externally anchored, the count is not committed.")
    print("\nKNP 4.03c (rev. 3) — external timestamp token over this exact file. A social\n"
          "post is deletable by its author; an RFC 3161 token cannot be un-issued. Run,\n"
          "one line at a time, then commit the .tsr beside the hashlog and declare its\n"
          "covered sha256 in the anchor object:")
    print(f"openssl ts -query -data {a.hashlog} -sha256 -cert -out {a.hashlog}.tsq")
    print(f"curl.exe -s -H \"Content-Type: application/timestamp-query\" "
          f"--data-binary @{a.hashlog}.tsq https://freetsa.org/tsr -o {a.hashlog}.tsr")
    print(f"openssl ts -reply -in {a.hashlog}.tsr -text")
    return 0


# ----------------------------------------------------------------- anchor

# ------------------------------------------------------------------ solve
FIELDS = ("id", "timestamp", "statement", "resolution_basis", "probability", "deadline", "salt")
SEPS = ("|", "", " | ", ":", "\n", "-", "::", " ")


def _variants(e: dict) -> list[dict]:
    """Value-rendering variants that plausibly differed at sealing time."""
    outs = []
    p = e.get("probability")
    pr = []
    if p not in (None, ""):
        n = float(p)
        pr = [str(int(n)), f"{int(n)}%", str(n / 100), f"{n/100:.2f}"]
    else:
        pr = [""]
    for pv in dict.fromkeys(pr):
        for esc_on in (True, False):
            v = dict(e)
            v["probability"] = pv
            v["_esc"] = esc_on
            outs.append(v)
    return outs


def _pre(e: dict, order, sep) -> str:
    parts = []
    for f in order:
        val = str(e.get(f, ""))
        if e.get("_esc") and f in ("statement", "resolution_basis"):
            val = esc(val)
        parts.append(val)
    return sep.join(parts)


def cmd_solve(a) -> int:
    """Search constructions until the published commitments reproduce. Prints the
    winning field order and separator only — never contents."""
    import itertools
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    if a.source:
        import subprocess  # noqa
    tested = [e for e in vault if e.get("commitment")]
    if not tested:
        die("no commitments in the vault to solve against")
    probe = tested[0]
    found = None
    for k in range(2, len(FIELDS) + 1):
        for order in itertools.permutations(FIELDS, k):
            if "salt" not in order or "statement" not in order:
                continue
            for sep in SEPS:
                for v in _variants(probe):
                    if hashlib.sha256(_pre(v, order, sep).encode("utf-8")).hexdigest() \
                            == probe["commitment"]:
                        found = (order, sep, v["probability"], v["_esc"])
                        break
                if found: break
            if found: break
        if found: break
    if not found:
        print("NO CONSTRUCTION FOUND over field orders, separators, and probability "
              "renderings.", file=sys.stderr)
        print("The preimage used something not in the vault as parsed — a field the export\n"
              "omits, different whitespace, or a value normalized before hashing.",
              file=sys.stderr)
        return 1
    order, sep, pv, esc_on = found
    ok = 0
    for e in tested:
        for v in _variants(e):
            if v["_esc"] == esc_on and hashlib.sha256(
                    _pre(v, order, sep).encode("utf-8")).hexdigest() == e["commitment"]:
                ok += 1
                break
    print(f"CONSTRUCTION FOUND · {ok}/{len(tested)} reproduce")
    print(f"  order      : {' | '.join(order)}")
    print(f"  separator  : {sep!r}")
    print(f"  pipe-escape: {'yes' if esc_on else 'no'}")
    if "probability" in order:
        print(f"  probability rendered as: {pv!r}")
        print("\n  NOTE: probability is INSIDE the preimage. KNP 2.01 says it is not.\n"
              "  KNM 3.01 says it is. The clutch followed KNM; KNP 2.01 is the paragraph\n"
              "  that needs amending, not the seal.")
    if ok < len(tested):
        print(f"\n  {len(tested)-ok} entries do not reproduce under it — those need "
              f"individual inspection.")
    render = {"60": "int"}.get(str(pv), None)
    render = ("pct" if str(pv).endswith("%") else
              "frac2" if str(pv).count(".") == 1 and len(str(pv).split(".")[-1]) == 2 else
              "frac" if "." in str(pv) else "int")
    rec = {"order": list(order), "separator": sep, "escape": esc_on,
           "probability_render": render, "solved_at":
               dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "reproduces": f"{ok}/{len(tested)}"}
    cp = construction_path(a.vault)
    cp.parent.mkdir(parents=True, exist_ok=True)
    cp.write_text(json.dumps(rec, indent=2), encoding="utf-8")
    print(f"\nrecorded -> {cp}   every later command now hashes this way")
    return 0



# ------------------------------------------------------------------ probe
def _shape(v) -> str:
    v = str(v)
    hx = bool(re.fullmatch(r"[0-9a-fA-F]+", v))
    return f"len={len(v)}" + (" hex" if hx else "") \
        + (" CRLF" if "\r" in v else "") \
        + (" nbsp" if "\u00a0" in v else "") \
        + (" smartq" if re.search(r"[\u2018\u2019\u201c\u201d]", v) else "") \
        + (" emdash" if "\u2014" in v else "") \
        + (" 2xspace" if "  " in v else "")


def cmd_probe(a) -> int:
    """Forensics on one Kall: field shapes, alternates, and a targeted construction
    search including single-field substitutions. Prints NO content."""
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    e = next((x for x in vault if x["id"] == a.id), None)
    if not e:
        die(f"{a.id} not in the vault")
    print(f"PROBE {e['id']}")
    for f in ("id", "timestamp", "statement", "resolution_basis", "salt",
              "probability", "deadline", "commitment"):
        if f in e:
            print(f"  {f:<18} {_shape(e[f])}")
    for k, v in (e.get("_alt") or {}).items():
        print(f"  ALT {k:<14} {_shape(v)}")
    for k, v in (e.get("_extra") or {}).items():
        print(f"  EXTRA {k!r:<18} {_shape(v)}")

    target = e.get("commitment")
    if not target:
        die("no commitment to probe against")
    import itertools

    def _deword(v: str) -> str:
        # reverse Word/Substack autocorrect wholesale: smart quotes, dashes,
        # ellipsis, nbsp — the classic paste-through-a-word-processor transform
        return (v.replace("\u2018", "'").replace("\u2019", "'")
                 .replace("\u201c", '"').replace("\u201d", '"')
                 .replace("\u2014", "--").replace("\u2013", "-")
                 .replace("\u2026", "...").replace("\u00a0", " "))

    def _reword(v: str) -> str:
        # forward direction: what autocorrect would have MADE the sealed text
        v = re.sub(r"(?<=\w)'(?=\w)", "\u2019", v)
        v = re.sub(r"--", "\u2014", v)
        return v

    def norms(v: str):
        yield "asis", v
        yield "strip", v.strip()
        yield "crlf", v.replace("\r", "")
        yield "ws1", re.sub(r"\s+", " ", v).strip()
        yield "deword", _deword(v)
        yield "deword+ws1", re.sub(r"\s+", " ", _deword(v)).strip()
        yield "reword", _reword(v)
        yield "ascii-q", v.replace("\u2018", "'").replace("\u2019", "'")
        yield "ascii-dq", v.replace("\u201c", '"').replace("\u201d", '"')
        yield "dash", v.replace("\u2014", "--").replace("\u2013", "-")
        yield "nfc", __import__("unicodedata").normalize("NFC", v)
        yield "nfkc", __import__("unicodedata").normalize("NFKC", v)
        yield "lower", v.lower()
        yield "upper", v.upper()

    base = {f: str(e.get(f, "")) for f in
            ("id", "timestamp", "statement", "resolution_basis", "salt",
             "probability", "deadline")}
    orders = [("id", "timestamp", "statement", "resolution_basis", "salt"),
              ("id", "timestamp", "statement", "resolution_basis", "probability",
               "deadline", "salt"),
              ("statement", "resolution_basis", "probability", "deadline", "salt"),
              ("id", "statement", "resolution_basis", "salt"),
              ("statement", "resolution_basis", "salt")]
    seps = ("|", "", " | ", "\n", ":")

    def tryhash(fields: dict, note: str) -> bool:
        for order in orders:
            for sep in seps:
                for esc_on in (True, False):
                    for pv in (str(fields.get("probability", "")),
                               f"{fields.get('probability','')}%"):
                        f2 = dict(fields); f2["probability"] = pv
                        parts = [esc(f2.get(x, "")) if esc_on and x in
                                 ("statement", "resolution_basis") else f2.get(x, "")
                                 for x in order]
                        for labeled in (False, True):
                            pre = sep.join(f"{x}: {v}" for x, v in zip(order, parts)) \
                                if labeled else sep.join(parts)
                            if hashlib.sha256(pre.encode("utf-8")).hexdigest() == target:
                                print(f"\nMATCH · {note}")
                                print(f"  order={' | '.join(order)}  sep={sep!r}  "
                                      f"esc={esc_on}  labeled={labeled}  prob={pv!r}")
                                return True
        return False

    if tryhash(base, "fields as parsed"):
        return 0
    # single-field normalization sweeps
    for f in ("statement", "resolution_basis", "timestamp", "salt"):
        for nname, nv in norms(base[f]):
            if nv == base[f]:
                continue
            b2 = dict(base); b2[f] = nv
            if tryhash(b2, f"{f} normalized [{nname}]"):
                return 0
    # paired sweep: the same transform applied to statement AND basis at once,
    # which is what a word processor actually does to a pasted block
    for (n1, v1), (n2, v2) in __import__("itertools").product(
            list(norms(base["statement"])), list(norms(base["resolution_basis"]))):
        if v1 == base["statement"] and v2 == base["resolution_basis"]:
            continue
        b2 = dict(base); b2["statement"] = v1; b2["resolution_basis"] = v2
        if tryhash(b2, f"statement[{n1}] + basis[{n2}]"):
            return 0
    # substitute alternates and extra hex values into salt / basis / statement
    subs = list((e.get("_alt") or {}).items()) + \
           [(k, v) for k, v in (e.get("_extra") or {}).items()]
    for label, val in subs:
        for f in ("salt", "resolution_basis", "statement", "timestamp"):
            b2 = dict(base); b2[f] = str(val)
            if tryhash(b2, f"{f} <- {label!r}"):
                return 0
    print("\nNO MATCH under targeted probes. The sealed text differs from the export "
          "in more than formatting —\nnext step is diffing one Kall against the "
          "sealing session's own record, not widening the search.")
    return 1



# ------------------------------------------------------------------ matrix
def cmd_matrix(a) -> int:
    """Cross-pairing sweep for a hand-assembled export: for every published
    commitment, try every (statement_i, basis_j, salt_k) triple across ALL Kalls,
    under each candidate construction. Catches shifted lines — a statement filed
    under one id, a salt under another. Prints id-level pairings only, no content."""
    import itertools
    vault = [norm(e) for e in load_vault(Path(a.vault))]
    if len(vault) < 2:
        die("matrix needs the full clutch in the vault")
    ids = [e["id"] for e in vault]
    sts = {e["id"]: str(e.get("statement", "")) for e in vault}
    bas = {e["id"]: str(e.get("resolution_basis", "")) for e in vault}
    sls = {e["id"]: str(e.get("salt", "")) for e in vault}
    tss = {e["id"]: str(e.get("timestamp", "")) for e in vault}
    prs = {e["id"]: str(e.get("probability", "")) for e in vault}
    dls = {e["id"]: str(e.get("deadline", "")) for e in vault}
    targets = {e["id"]: e.get("commitment") for e in vault if e.get("commitment")}

    def ts_variants(ts):
        seen = {ts, ts.replace("Z", ""), ts.replace("T", " "),
                ts.replace("T", " ").replace("Z", ""), ts[:10]}
        return [t for t in seen if t]

    orders = [("id", "timestamp", "statement", "resolution_basis", "salt"),
              ("id", "timestamp", "statement", "resolution_basis", "probability",
               "deadline", "salt"),
              ("statement", "resolution_basis", "probability", "deadline", "salt"),
              ("statement", "resolution_basis", "salt")]
    seps = ("|", "", " | ")
    found, open_ = [], []
    for kid, target in targets.items():
        hit = None
        for si, bi, ki in itertools.product(ids, ids, ids):
            fields = {"id": kid, "statement": sts[si], "resolution_basis": bas[bi],
                      "salt": sls[ki], "probability": prs[kid], "deadline": dls[kid]}
            done = False
            for tsv in ts_variants(tss[kid]):
                fields["timestamp"] = tsv
                for order in orders:
                    for sep in seps:
                        for esc_on in (True, False):
                            parts = [esc(fields.get(x, "")) if esc_on and x in
                                     ("statement", "resolution_basis")
                                     else fields.get(x, "") for x in order]
                            pre = sep.join(parts)
                            if hashlib.sha256(pre.encode("utf-8")).hexdigest() == target:
                                hit = (si, bi, ki, order, sep, esc_on, tsv)
                                done = True
                            if not done and "salt" in order:
                                try:
                                    raw = sep.encode().join(
                                        x.encode("utf-8") if f != "salt"
                                        else bytes.fromhex(fields["salt"])
                                        for f, x in zip(order, parts))
                                    if hashlib.sha256(raw).hexdigest() == target:
                                        hit = (si, bi, ki, order, sep, esc_on,
                                               tsv + " · salt-as-bytes")
                                        done = True
                                except ValueError:
                                    pass
                            if done: break
                        if done: break
                    if done: break
                if done: break
            if done: break
        if hit:
            si, bi, ki, order, sep, esc_on, tsv = hit
            tag = "ALIGNED" if si == bi == ki == kid else "SHIFTED"
            found.append((kid, tag, si, bi, ki, order, sep, esc_on, tsv))
        else:
            open_.append(kid)

    for kid, tag, si, bi, ki, order, sep, esc_on, tsv in found:
        loc = "" if tag == "ALIGNED" else f"  st<-{si} basis<-{bi} salt<-{ki}"
        print(f"{tag:<8} {kid}{loc}")
        print(f"         order={'|'.join(order)}  sep={sep!r}  esc={esc_on}  ts={tsv!r}")
    if open_:
        print(f"UNSOLVED {len(open_)}: {', '.join(open_)}")
    if found and not open_:
        print("\nAll nine reproduce. If any row reads SHIFTED, the export mis-filed "
              "fields across ids;\nre-file per the pairings above, re-run adopt, then "
              "verify goes green.")
    elif not found:
        print("\nNothing reproduces even cross-paired: the sealed TEXT differs from "
              "the export.\nThe session record is the only recovery path left.")
    return 0 if found and not open_ else 1

# ----------------------------------------------------------------- import
FIELD_MAP = {
    "id": "id", "kall": "id", "kall id": "id", "ref": "id",
    "timestamp": "timestamp", "timestamp utc": "timestamp", "time": "timestamp",
    "sealed": "timestamp", "utc": "timestamp", "date": "timestamp",
    "timestamp note": "timestamp", "sealed utc": "timestamp",
    "statement": "statement", "claim": "statement", "call": "statement",
    "prediction": "statement", "text": "statement",
    "resolution basis": "resolution_basis", "basis": "resolution_basis",
    "resolution": "resolution_basis", "resolves": "resolution_basis",
    "resolution criterion": "resolution_basis", "criterion": "resolution_basis",
    "salt": "salt", "nonce": "salt",
    "resolved when": "resolution_basis",
    "commitment": "commitment", "hash": "commitment", "seal": "commitment",
    "sha256": "commitment", "sha 256": "commitment", "hash sha 256": "commitment",
    "p": "probability", "probability": "probability", "prob": "probability",
    "deadline": "deadline", "by": "deadline", "resolve by": "deadline",
    "status": "status", "domain": "domain",
}
KID_RE = re.compile(r"[A-Za-z0-9]*KK-\d{8}-\d+")


def _key(s: str) -> str | None:
    k = re.sub(r"[^a-z0-9 ]", " ", s.strip().lower())
    k = re.sub(r"\s+", " ", k).strip()
    return FIELD_MAP.get(k)


def _clean(v: str) -> str:
    v = v.strip()
    v = re.sub(r"^\*{1,2}\s*", "", v)          # **Label:** puts the closer after the colon
    return v.strip().strip("`").strip().rstrip("%").strip()


def cmd_adopt(a) -> int:
    """Convert a hand-made markdown vault export into the KNP 3.01 JSON vault.
    Prints counts and field coverage only — never contents."""
    src = Path(a.source)
    if not src.exists():
        die(f"source not found: {a.source}")
    text = src.read_text(encoding="utf-8-sig")
    lines = text.split("\n")
    out: list[dict] = []

    rows = [l for l in lines if l.strip().startswith("|")]
    rows = [r for r in rows if not re.fullmatch(r"[\s|:\-]+", r)]
    if len(rows) >= 2 and KID_RE.search("\n".join(rows[1:])):
        hdr = [_key(c) for c in rows[0].strip().strip("|").split("|")]
        for r in rows[1:]:
            cells = [_clean(c) for c in r.strip().strip("|").split("|")]
            if not KID_RE.search(" ".join(cells)):
                continue
            if len(cells) != len(hdr):
                kid = KID_RE.search(" ".join(cells))
                print(f"  ROW SHAPE  {kid.group(0)}: {len(cells)} cells vs {len(hdr)} columns "
                      f"— an unescaped pipe inside a cell breaks the table; fix the export "
                      f"before trusting this row", file=sys.stderr)
            raw = rows[0].strip().strip("|").split("|")
            e = {h: c for h, c in zip(hdr, cells) if h and c}
            e["_extra"] = {raw[j].strip(): cells[j] for j in range(min(len(raw), len(cells)))
                           if not hdr[j] and cells[j]}
            if e.get("id"):
                out.append(e)
    # ALWAYS also parse the section form and merge — a file may carry a public-style
    # table over per-Kall plaintext sections; stopping at the table loses the vault
    sect: list[dict] = []
    if True:                                       # section form
        idx = [i for i, l in enumerate(lines) if l.lstrip().startswith("#") and KID_RE.search(l)]
        for n, i in enumerate(idx):
            block = lines[i:idx[n + 1] if n + 1 < len(idx) else len(lines)]
            e: dict = {"id": KID_RE.search(lines[i]).group(0)}
            last = None
            for l in block[1:]:
                m = re.match(r"\s*[-*]?\s*\*{0,2}([A-Za-z0-9 _\\-]{2,28})\*{0,2}\s*[:：]"
                             r"\s*\*{0,2}\s*(.+)", l)
                if m:
                    k = _key(m.group(1))
                    if k and k not in e:
                        e[k] = _clean(m.group(2)); last = ("f", k)
                    elif not k:
                        lbl = m.group(1).strip()
                        e.setdefault("_extra", {})[lbl] = _clean(m.group(2))
                        last = ("x", lbl)
                    else:
                        last = None
                    continue
                t = l.strip()
                if (not t or t.startswith("#") or t.startswith("|")
                        or re.fullmatch(r"[-=_\\]{3,}", t) or KID_RE.fullmatch(t)):
                    last = None
                    continue
                if last:                            # wrapped continuation of the prior value
                    kind, key = last
                    tgt = e if kind == "f" else e.setdefault("_extra", {})
                    prev, add = tgt.get(key, ""), _clean(t)
                    hexish = lambda x: bool(re.fullmatch(r"[0-9a-fA-F]+", x))
                    tgt[key] = prev + add if (hexish(prev) and hexish(add)) \
                        else (prev + " " + add).strip()
            sect.append(e)
    if out and sect:
        by_id = {e["id"]: e for e in out}
        for e in sect:
            tgt = by_id.get(e["id"])
            if tgt is None:
                out.append(e)
            else:
                for kk, vv in e.items():
                    if kk == "_extra":
                        tgt.setdefault("_extra", {}).update(vv)
                    elif kk not in tgt or not str(tgt.get(kk, "")).strip():
                        tgt[kk] = vv
                    elif str(tgt[kk]).strip() != str(vv).strip():
                        tgt.setdefault("_alt", {})[kk] = str(vv).strip()
                        print(f"  CONFLICT   {e['id']}.{kk}: table and section disagree "
                              f"(table kept; section value retained as alternate)",
                              file=sys.stderr)
    elif sect:
        out = sect
    if not out:
        die("could not parse the export — send me its first structural lines and I'll widen it")

    for e in out:
        if isinstance(e.get("probability"), str) and e["probability"].isdigit():
            e["probability"] = int(e["probability"])
    def reproduces(entries) -> int:
        return sum(1 for e in entries if e.get("commitment")
                   and all(str(e.get(f, "")).strip() for f in
                           ("id", "timestamp", "statement", "resolution_basis", "salt"))
                   and commit_of(e, a.sep) == e["commitment"])

    if reproduces(out) < len(out):
        cands = sorted({k for e in out for k in e.get("_extra", {})})
        best, hits = None, reproduces(out)
        for c in cands:
            for e in out:
                e["_try"] = e.get("resolution_basis")
                e["resolution_basis"] = e.get("_extra", {}).get(c, e.get("resolution_basis", ""))
            n = reproduces(out)
            if n > hits:
                best, hits = c, n
            for e in out:
                e["resolution_basis"] = e.pop("_try")
        if best:
            for e in out:
                e["resolution_basis"] = e.get("_extra", {}).get(best, e.get("resolution_basis", ""))
            print(f"FIELD RESOLVED BY HASH: the label {best!r} is the resolution_basis "
                  f"({hits}/{len(out)} commitments reproduce with it)")
        elif cands:
            print(f"unmapped labels present, none reproduce the commitment: {cands}")
    for e in out:
        e.pop("_extra", None)

    have = lambda f: sum(1 for e in out if str(e.get(f, "")).strip())
    n32 = len(re.findall(r"(?<![0-9a-f])[0-9a-f]{32}(?![0-9a-f])", text))
    n64 = len(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", text))
    print(f"source: {len(text)} bytes · {len(lines)} lines · {len(rows)} table rows · "
          f"{len([l for l in lines if l.lstrip().startswith('#')])} headings · "
          f"{n64} 64-hex · {n32} 32-hex")
    print(f"labels: {sorted(set(re.findall(r'[*]{2}([A-Za-z0-9 :]{2,28})[*]{2}', text)))[:14]}")
    print(f"parsed {len(out)} Kalls")
    for f in ("id", "timestamp", "statement", "resolution_basis", "salt", "commitment",
              "probability", "deadline"):
        n = have(f)
        print(f"  {f:<18} {n}/{len(out)}" + ("" if n == len(out) else "   <-- INCOMPLETE"))

    ok = bad = untestable = 0
    for e in out:
        if not all(str(e.get(f, "")).strip() for f in
                   ("id", "timestamp", "statement", "resolution_basis", "salt")):
            untestable += 1
        elif e.get("commitment") and commit_of(e, a.sep) == e["commitment"]:
            ok += 1
        elif e.get("commitment"):
            bad += 1
        else:
            untestable += 1
    sl = sorted({len(str(e.get("salt", ""))) for e in out if e.get("salt")})
    print(f"  salt hex lengths seen: {sl or '—'}"
          + ("   <-- MIXED: some salts likely truncated by line wrap" if len(sl) > 1 else ""))
    print(f"\ncommitment check: {ok} reproduce · {bad} mismatch · {untestable} untestable")
    if bad:
        print("A mismatch means the export's construction differs from KNP 2.01. The published\n"
              "hash governs; run selftest to find the separator before writing anything.")
    if a.dry_run:
        print("\nDRY RUN — nothing written.")
        return 0
    save_json(Path(a.vault), out)
    print(f"\nwrote {a.vault}")
    return 0


def cmd_import(a) -> int:
    """Seed the machine-readable hashlog from the already-published markdown table.
    The nine of 2026-07-25 were published before a hashlog existed; KNP 6.02 needs
    one for any aggregator to ingest them."""
    rows = parse_table(Path(a.table))
    if not rows:
        die(f"no rows parsed from {a.table}")
    log = load_log(Path(a.hashlog))
    have = {r["id"] for r in log["records"]}
    vault = {e["id"]: e for e in (norm(x) for x in load_vault(Path(a.vault)))}
    added, unopenable = 0, []
    for r in rows:
        if r["id"] in have:
            continue
        if r["id"] not in vault:
            unopenable.append(r["id"])
        log["records"].append({"id": r["id"], "timestamp": r["timestamp"],
                               "commitment": r["commitment"], "probability": r["probability"],
                               "deadline": r["deadline"],
                               "status": r["status"] if r["status"] in STATUSES else "SEALED"})
        added += 1
    log["records"].sort(key=lambda x: (x["timestamp"], x["id"]))
    save_json(Path(a.hashlog), stamp_log(log))
    print(f"imported {added} record(s) -> {a.hashlog}  (total {len(log['records'])})")
    if unopenable:
        print(f"\nNO VAULT RECORD for {len(unopenable)}: {', '.join(unopenable)}")
        print("Published but unopenable — the commitment stands, the content can never be\n"
              "revealed (KNP 3.04). Say so on the log's face rather than leaving it implied.")
    return 0


def cmd_anchor(a) -> int:
    rows = parse_table(Path(a.table))
    if not rows:
        die("no rows parsed from the table")
    anchor = sha_raw(SEP.join([CHAIN_LABEL] + [r["commitment"] for r in rows]))
    log = load_log(Path(a.hashlog))
    log["chain_anchor"] = anchor  # never overwrite anchor: that holds the KNP 4.03 declaration
    log["anchored_over"] = [r["id"] for r in rows]
    log["head"] = log.get("head") or anchor  # seeded from chain_anchor above
    save_json(Path(a.hashlog), stamp_log(log))
    print(f"anchor : {anchor}\nover   : {len(rows)} ({rows[0]['id']} … {rows[-1]['id']})")
    print("\nNon-normative extension. KNP 4.03 is satisfied by git history and the external\n"
          "beacon, NOT by this chain — a chain the committer can recompute end-to-end is\n"
          "not evidence against the committer. It is only worth the head being beaconed.")
    return 0


def main() -> int:
    common = argparse.ArgumentParser(add_help=False)
    for f in ("--vault", "--hashlog", "--table", "--sep", "--prefix"):
        common.add_argument(f, default=None)
    ap = argparse.ArgumentParser(description="KNP-26 reference sealer.", parents=[common])
    sub = ap.add_subparsers(dest="cmd", required=True)
    P = {"parents": [common]}
    s = sub.add_parser("selftest", **P); s.add_argument("--id", required=True); s.set_defaults(fn=cmd_selftest)
    s = sub.add_parser("seal", **P); s.add_argument("--draft", required=True)
    s.add_argument("--timestamp"); s.add_argument("--dry-run", action="store_true"); s.set_defaults(fn=cmd_seal)
    s = sub.add_parser("verify", **P); s.set_defaults(fn=cmd_verify)
    s = sub.add_parser("reveal", **P); s.add_argument("--id", required=True)
    s.add_argument("--out"); s.add_argument("--no-status", action="store_true"); s.set_defaults(fn=cmd_reveal)
    s = sub.add_parser("check", **P); s.add_argument("--reveal", required=True); s.set_defaults(fn=cmd_check)
    s = sub.add_parser("count", **P); s.set_defaults(fn=cmd_count)
    s = sub.add_parser("beacon", **P); s.set_defaults(fn=cmd_beacon)
    s = sub.add_parser("solve", **P); s.add_argument("--source"); s.set_defaults(fn=cmd_solve)
    s = sub.add_parser("probe", **P); s.add_argument("--id", required=True); s.set_defaults(fn=cmd_probe)
    s = sub.add_parser("matrix", **P); s.set_defaults(fn=cmd_matrix)
    s = sub.add_parser("adopt", **P); s.add_argument("--source", required=True)
    s.add_argument("--dry-run", action="store_true"); s.set_defaults(fn=cmd_adopt)
    s = sub.add_parser("import", **P); s.set_defaults(fn=cmd_import)
    s = sub.add_parser("anchor", **P); s.set_defaults(fn=cmd_anchor)

    argv = sys.argv[1:]
    pre, _ = common.parse_known_args(argv)
    a = ap.parse_args(argv)
    a.vault = a.vault or pre.vault or str(VAULT)
    a.hashlog = a.hashlog or pre.hashlog or str(HASHLOG)
    a.table = a.table or pre.table or str(TABLE)
    a.sep = a.sep or pre.sep or SEP
    a.prefix = a.prefix or pre.prefix or ""
    load_construction(a.vault)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
