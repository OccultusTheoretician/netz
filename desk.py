#!/usr/bin/env python3
"""
desk.py — one entry point for the Prescient Desk.

Written because establishing what was true cost more than changing it. Every
working session opened with the same archaeology: which arm has how many rows,
what is past deadline, whether the served copies match the canonical ones,
when Spion last ran, whether the last push actually landed. None of that was
one command. Now it is.

    python desk.py status      what is true right now
    python desk.py verify      assert the invariants; non-zero exit on failure
    python desk.py due         what needs resolving
    python desk.py ship        verify, commit, rebase, push, confirm from remote

`verify` is the one that earns its keep. Three separate mirrors drifted in a
single night — the protocol document, the ledger JSON, the report face — and
each was found by hand, late, after the public copy had already been wrong for
hours. They are assertions now, and `ship` refuses to run if they fail.

Standard library only. Nothing here writes to the ledger.
"""

import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone, date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
FC = ROOT / "forecasts"

C_OK, C_WARN, C_BAD, C_DIM, C_OFF = "\033[32m", "\033[33m", "\033[31m", "\033[90m", "\033[0m"
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        C_OK = C_WARN = C_BAD = C_DIM = C_OFF = ""

HALF_LIFE = {"existence": 365, "composition": 180, "commander": 60,
             "posture": 21, "location": 14}


def ok(s):   return f"{C_OK}{s}{C_OFF}"
def warn(s): return f"{C_WARN}{s}{C_OFF}"
def bad(s):  return f"{C_BAD}{s}{C_OFF}"
def dim(s):  return f"{C_DIM}{s}{C_OFF}"


def head(t):
    print(f"\n{t}")
    print(dim("-" * max(28, len(t))))


def md5(p: Path):
    return hashlib.md5(p.read_bytes()).hexdigest() if p.exists() else None


def md5lf(p: Path):
    """MIRROREOL-2026-09-06: md5 over LF-normalised bytes."""
    return hashlib.md5(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest() if p.exists() else None


def load_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def git(*args, cwd=ROOT):
    try:
        r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True,
                           text=True, timeout=45)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:
        return 1, "", str(e)


# ----------------------------------------------------------------------
def arm_table(projs):
    arms = {}
    for p in projs:
        arms.setdefault(p.get("model") or "unattributed", []).append(p)
    rows = []
    for tag, rs in sorted(arms.items()):
        res = [x for x in rs if x["status"] in ("hit", "miss")]
        rec = {"arm": tag, "issued": len(rs),
               "open": sum(1 for x in rs if x["status"] == "open"),
               "void": sum(1 for x in rs if x["status"] == "void"),
               "n": len(res),
               "hits": sum(1 for x in res if x["status"] == "hit")}
        rec["misses"] = rec["n"] - rec["hits"]
        if rec["n"]:
            b = sum((x["probability"]/100 - (1.0 if x["status"] == "hit" else 0.0))**2
                    for x in res) / rec["n"]
            base = rec["hits"] / rec["n"]
            clim = base * (1 - base)
            rec.update({"brier": b, "base": base, "clim": clim,
                        "skill": (1 - b/clim) if clim else None})
        rows.append(rec)
    return rows


def due_rows(projs, horizon=7):
    today = date.today()
    overdue, soon = [], []
    for p in projs:
        if p["status"] != "open":
            continue
        try:
            d = datetime.strptime(p["deadline"], "%Y-%m-%d").date()
        except (ValueError, KeyError, TypeError):
            continue
        if d < today:
            overdue.append((d, p))
        elif (d - today).days <= horizon:
            soon.append((d, p))
    key = lambda t: (t[0], t[1].get('id', ''))
    return sorted(overdue, key=key), sorted(soon, key=key)


# ----------------------------------------------------------------------
MIRRORS = [("ledger.json", ROOT/"ledger.json", DOCS/"ledger.json"),
           ("ledger.html", FC/"ledger.html", DOCS/"ledger.html"),
           ("ledger_full.html", FC/"ledger_full.html", DOCS/"ledger_full.html"),   # LEDGERVIEW-2026-09-02
           ("ledger_index.json", FC/"ledger_index.json", DOCS/"ledger_index.json"),
           ("fogwar_core.js", ROOT/"fogwar_core.js", DOCS/"fogwar_core.js"),   # FOGWARBOARD-2026-09-04
           ("fogwar_scenario_two_capitals.json", ROOT/"fogwar_scenario_two_capitals.json", DOCS/"fogwar_scenario_two_capitals.json"),
           ("kkr.html", FC/"KKR_latest.html", DOCS/"kkr.html"),
           ("KriegForeKaster.json", ROOT/"KriegForeKaster.json",
            DOCS/"KriegForeKaster.json")]

# Anything holding opening material for something not yet revealed.
VAULT_PATTERNS = ["kalls_vault", "kalls_rescue", "_VAULT.md", "vault/",
                  "fogsim_campaign", "_campaign.json"]


def check_mirrors():
    out = []
    for name, src, dst in MIRRORS:
        if not src.exists():
            out.append((name, "skip", f"canonical missing: {src.name}")); continue
        if not dst.exists():
            out.append((name, "fail", "served copy missing")); continue
        # MIRROREOL-2026-09-06: content judged LF-normalised, as every digest on the
        # desk is (OTSNORM); the --autostash pull re-checks out staged copies through
        # autocrlf and a byte compare read one byte per line as drift.
        same = md5lf(src) == md5lf(dst)
        out.append((name, "pass" if same else "fail",
                    "identical" if same else
                    f"DRIFT — canonical {src.stat().st_size:,}B vs served {dst.stat().st_size:,}B"))
    return out


def check_envelope():
    d = load_json(ROOT/"ledger.json")
    if d is None:
        return "fail", "ledger.json unreadable"
    missing = [k for k in ("schema", "generator", "as_of") if k not in d]
    return ("fail", "missing " + ", ".join(missing)) if missing else \
           ("pass", f"{d['schema']} · as_of {d['as_of']}")


def check_vault_leak():
    rc, out, _ = git("ls-files")
    if rc:
        return "skip", "git not available"
    hits = [f for f in out.splitlines() if any(v in f for v in VAULT_PATTERNS)]
    return ("fail", f"{len(hits)} vault-tier file(s) TRACKED: " + ", ".join(hits[:4])) \
        if hits else ("pass", "no vault-tier file tracked")


PREFLIGHT = False   # True only while ship() is checking itself


def check_remote():
    rc, local, _ = git("rev-parse", "HEAD")
    rc2, ls, _ = git("ls-remote", "origin", "main")
    if rc or rc2 or not ls:
        return "skip", "remote unreachable"
    remote = ls.split()[0]
    if local == remote:
        return "pass", f"in sync at {local[:7]}"
    # ahead is the normal pre-ship state; behind is not
    rc3, cnt, _ = git("rev-list", "--count", f"{remote}..{local}")
    ahead = cnt.isdigit() and int(cnt) > 0
    if PREFLIGHT and ahead:
        return "info", f"local {local[:7]} is ahead of origin — which is what shipping is for"
    return "warn", f"local {local[:7]} != remote {remote[:7]} — unpushed or behind"


def check_dirty():
    rc, out, _ = git("status", "--porcelain")
    if rc:
        return "skip", "git not available"
    n = len([l for l in out.splitlines() if l.strip()])
    if n == 0:
        return "pass", "clean"
    if PREFLIGHT:
        return "info", f"{n} change(s) staged for this ship"
    return "warn", f"{n} uncommitted change(s)"


def check_identity():
    """A name on a published surface cannot be recalled. The guard holds only
    hashes, so this check discloses nothing about what it is looking for."""
    g = ROOT / "identity_guard.py"
    if not g.exists():
        return "skip", "identity_guard.py not present"
    try:
        r = subprocess.run([sys.executable, str(g), "scan"], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=120)
    except Exception as e:
        # KK30-GUARDPERF fail-closed: a safety guard that could not run is not
        # a pass and not a skip. A name on a published surface cannot be
        # recalled, so the uncertain case BLOCKS the publish (desk verify gates
        # on "fail"). Two 2026-08-08 publishes shipped unscanned under the old
        # "skip"; that path is closed.
        return "fail", (f"guard did not run ({e}) - publish BLOCKED fail-closed; "
                        f"run `python identity_guard.py scan` by hand to clear")
    if r.returncode == 0:
        return "pass", "no configured term in any tracked file"
    n = sum(1 for l in r.stdout.splitlines() if ":" in l and l.strip().startswith(("d", "b", "s", "k", "m", "i", "f", "a", "c", "p", "r", "t", "w", "n", "o", "l", "e", "g", "h", "j", "q", "u", "v", "x", "y", "z", ".")))
    return "fail", (f"a configured identity term appears in tracked files — run "
                    f"`python identity_guard.py scan` for locations")


def check_unmerged():
    """PUBGUARD-2026-09-01: publish.bat pulls with --autostash. A conflicted
    pop leaves conflict markers inside tracked files, and on 2026-09-01 one
    such file (docs/ots_anchors.json) was committed and pushed as invalid
    JSON because nothing looked. An unmerged path, or a tracked text file
    carrying both a <<<<<<< line and a >>>>>>> line, is a FAIL, and verify
    gates the ship on fail. The scan runs after add -A on purpose: add
    clears the unmerged state and leaves the markers, which is exactly the
    case that shipped."""
    rc, out, _ = git("diff", "--name-only", "--diff-filter=U")
    if rc:
        return "skip", "git not available"
    unmerged = [l for l in out.splitlines() if l.strip()]
    if unmerged:
        return "fail", (f"{len(unmerged)} unmerged path(s): {', '.join(unmerged[:4])} "
                        f"- resolve, then rerun")
    rc, files, _ = git("ls-files", "--", "*.json", "*.py", "*.md", "*.html", "*.txt", "*.bat", "*.csv", "*.yml")
    if rc:
        return "skip", "git not available"
    hits = []
    for f in files.splitlines():
        try:
            data = (ROOT / f).read_bytes()
        except Exception:
            continue
        if b"\n<<<<<<< " in b"\n" + data and b"\n>>>>>>> " in data:
            hits.append(f)
    if hits:
        return "fail", f"conflict markers in {len(hits)} tracked file(s): {', '.join(hits[:4])}"
    return "pass", "no unmerged paths, no conflict markers"


CHECKS = [("identity guard", check_identity),
          ("ledger envelope", check_envelope),
          ("vault leak", check_vault_leak),
          ("merge state", check_unmerged),  # PUBGUARD-2026-09-01
          ("working tree", check_dirty),
          ("remote", check_remote)]


def run_verify(quiet=False):
    results = []
    for name, state, note in check_mirrors():
        results.append((f"mirror: {name}", state, note))
    for name, fn in CHECKS:
        s, n = fn()
        results.append((name, s, n))
    if not quiet:
        head("VERIFY")
        for name, state, note in results:
            mark = {"pass": ok("PASS"), "fail": bad("FAIL"),
                    "warn": warn("WARN"), "skip": dim("SKIP"),
                    "info": dim("INFO")}[state]
            print(f"  [{mark}] {name:26s} {note}")
    failed = [r for r in results if r[1] == "fail"]
    return failed


# ----------------------------------------------------------------------
def cmd_status(args):
    print(f"\n{'THE PRESCIENT DESK':^64}")
    print(f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ'):^64}")

    head("LEDGER")
    d = load_json(ROOT/"ledger.json")
    if not d or "projections" not in d:
        print(bad("  ledger.json missing or unreadable"))
    else:
        projs = d["projections"]
        print(f"  {len(projs)} issued · schema {d.get('schema', bad('ABSENT'))} · "
              f"as_of {d.get('as_of', bad('ABSENT'))}")
        print(f"\n  {'arm':16s} {'iss':>4s} {'open':>5s} {'void':>5s} {'res':>4s} "
              f"{'H/M':>7s} {'Brier':>7s} {'base':>6s} {'clim':>6s} {'skill':>7s}")
        for r in arm_table(projs):
            if r["n"]:
                sk = "—" if r["skill"] is None else f"{r['skill']:+.3f}"
                line = (f"  {r['arm']:16s} {r['issued']:>4d} {r['open']:>5d} {r['void']:>5d} "
                        f"{r['n']:>4d} {r['hits']:>3d}/{r['misses']:<3d} {r['brier']:>7.3f} "
                        f"{r['base']:>5.1%} {r['clim']:>6.3f} {sk:>7s}")
                if r["n"] < 30:
                    line += dim("  noise")
            else:
                line = (f"  {r['arm']:16s} {r['issued']:>4d} {r['open']:>5d} {r['void']:>5d} "
                        f"{0:>4d} {'—':>7s} {'—':>7s} {'—':>6s} {'—':>6s} {'—':>7s}")
            print(line)
        print(dim("  no pooled score — a Brier belongs to one forecaster"))
        overdue, soon = due_rows(projs)
        if overdue:
            print("\n  " + bad(f"{len(overdue)} PAST DEADLINE, unresolved") +
                  f" — oldest {overdue[0][0]}")
        if soon:
            print("  " + warn(f"{len(soon)} due within 7 days"))
        if not overdue and not soon:
            print("\n  " + ok("nothing due"))

    head("KRIEGFOREKASTER")
    k = load_json(ROOT/"KriegForeKaster.json")
    if not k:
        print(dim("  no KriegForeKaster.json"))
    else:
        stale = 0
        for f in k.get("formations", []):
            for b, hl in HALF_LIFE.items():
                blk = f.get(b)
                if not blk or not blk.get("as_of"):
                    continue
                try:
                    age = (date.today() - datetime.strptime(blk["as_of"], "%Y-%m-%d").date()).days
                except ValueError:
                    continue
                if age > hl:
                    stale += 1
        n = len(k.get("formations", []))
        # Mirrors KriegForeKaster.COMMAND_PRECISION. These two literals are the
        # only duplication permitted between the files; change them together.
        _CMD = {"headquarters", "installation centroid"}
        _STATE = {"capital centroid", "approximate"}
        _fs = k.get("formations", [])
        _den = lambda f: (f.get("location") or {}).get("denotes")
        loc = sum(1 for f in _fs if _den(f) in _CMD)
        st = sum(1 for f in _fs if _den(f) in _STATE)
        nolo = len(_fs) - loc - st
        print(f"  {k.get('theater','?')}")
        print(f"  {n} formations · {loc} located to a command, {st} to a capital or approximate only, {nolo} unlocated · "
              + (warn(f"{stale} claims past half-life") if stale else ok("all claims fresh")))

    head("SPION")
    s = load_json(DOCS/"spion_state.json")
    if not s:
        print(dim("  no docs/spion_state.json"))
    else:
        c = s.get("counts", {})
        print(f"  as_of {s.get('as_of','?')} · host {s.get('run_host','?')}")
        line = f"  {c.get('checked','?')} checked · {c.get('moved',0)} moved · {c.get('steady',0)} steady"
        if c.get("unreachable"):
            line += " · " + bad(f"{c['unreachable']} unreachable")
        print(line)
        for src in (s.get("sources") or {}).values() if isinstance(s.get("sources"), dict) else (s.get("sources") or []):
            if isinstance(src, dict) and src.get("error"):
                print(dim(f"    {str(src.get('name', src.get('url','?')))[:44]:46s} {src['error']}"))

    head("REPO")
    rc, br, _ = git("rev-parse", "--abbrev-ref", "HEAD")
    rc2, lh, _ = git("rev-parse", "--short", "HEAD")
    print(f"  branch {br or '?'} at {lh or '?'}")
    st, note = check_dirty();  print(f"  working tree: {note}")
    st, note = check_remote(); print(f"  remote: {note}")
    try:
        t, u, f = shutil.disk_usage(ROOT)
        pct = f/t*100
        line = f"  disk: {f/2**30:.1f} GB free of {t/2**30:.0f} GB ({pct:.1f}%)"
        print(bad(line) if pct < 5 else (warn(line) if pct < 12 else line))
    except Exception:
        pass

    failed = run_verify()
    print()
    if failed:
        print(bad(f"  {len(failed)} invariant(s) FAILING — `python desk.py ship` will refuse"))
    else:
        print(ok("  all invariants hold"))
    print()
    return 0


def cmd_due(args):
    d = load_json(ROOT/"ledger.json")
    if not d:
        print(bad("ledger.json unreadable")); return 1
    overdue, soon = due_rows(d["projections"], horizon=getattr(args, "days", 7))
    head("PAST DEADLINE")
    if not overdue:
        print(ok("  none"))
    for dt, p in overdue:
        print(f"  {bad(str(dt))}  {p['id']}  {p['probability']:>3}%  "
              f"[{p.get('model','?')}]")
        print(dim(f"      {p['statement'][:96]}"))
    head("DUE SOON")
    if not soon:
        print(dim("  none"))
    for dt, p in soon:
        print(f"  {warn(str(dt))}  {p['id']}  {p['probability']:>3}%  "
              f"[{p.get('model','?')}]")
        print(dim(f"      {p['statement'][:96]}"))
    print(f"\n  resolve with: python kkr.py --resolve\n")
    return 0


def cmd_verify(args):
    failed = run_verify()
    print()
    if failed:
        print(bad(f"  {len(failed)} FAILING"))
        return 1
    print(ok("  all invariants hold"))
    return 0


def cmd_ship(args):
    msg = getattr(args, "m", None)
    if not msg:
        print(bad("FAIL — a commit message is required:  python desk.py ship -m \"...\""))
        return 1
    # nav normalization before verify: generators rewrite pages without
    # nav; stamping here means verify checks the post-nav mirrors. WARN,
    # never block - a gate that fails on cosmetics gets disabled.
    _ng = ROOT / "navgen.py"
    if _ng.exists():
        _r = subprocess.run([sys.executable, str(_ng)], cwd=str(ROOT),
                            capture_output=True, text=True, timeout=60)
        if _r.returncode != 0:
            print(warn("  [WARN] navgen failed - shipping without nav "
                       "normalization"))
            print(dim((_r.stdout + _r.stderr).strip()[-300:]))
        else:
            _stamped = [l for l in _r.stdout.splitlines()
                        if l.strip().startswith(("replaced", "inserted"))]
            if _stamped:
                print(dim(f"  nav: {len(_stamped)} page(s) re-stamped"))
    # NOTHING-TO-SHIP GATE (KK17): a ship with no payload prints a
    # message describing work the commit does not contain - the
    # d77e59c class. Clean tree + remote in sync = refuse. Clean but
    # ahead = push-only, which the tolerant sequence below performs.
    _ds, _ = check_dirty()
    _rs, _ = check_remote()
    if _ds == "pass" and _rs == "pass":
        print(bad("\n  NOTHING TO SHIP \u2014 working tree clean, remote in sync."))
        print(dim("  A message without a payload is the d77e59c defect class."))
        print(dim("  Make the change first; FIX prints, or nothing ships."))
        return 1
    globals()["PREFLIGHT"] = True
    failed = run_verify()
    globals()["PREFLIGHT"] = False
    if failed:
        print()
        print(bad("  REFUSING TO SHIP — fix the invariants above first."))
        print(dim("  A served copy that disagrees with the canonical one is the "
                  "defect this instrument exists to detect."))
        return 1
    print(ok("\n  invariants hold — shipping"))
    for step in (["add", "-A"], ["commit", "-m", msg],
                 ["pull", "--rebase", "origin", "main"], ["push"]):
        rc, out, err = git(*step)
        label = " ".join(step[:2])
        if rc and "nothing to commit" not in (out + err):
            print(bad(f"  git {label} FAILED")); print(dim(out or err)); return 1
        print(f"  {ok('ok')}  git {label}")
    rc, ls, _ = git("ls-remote", "origin", "main")
    rc2, lh, _ = git("rev-parse", "HEAD")
    if ls and lh and ls.split()[0] == lh:
        print(ok(f"\n  remote confirms {lh[:7]}"))
        return 0
    print(bad("\n  PUSH DID NOT LAND — remote does not match local HEAD"))
    return 1


def main():
    cmds = {"status": cmd_status, "verify": cmd_verify,
            "due": cmd_due, "ship": cmd_ship}
    argv = sys.argv[1:]
    if not argv or argv[0] not in cmds:
        print(__doc__)
        return 0
    class A: pass
    a = A()
    for i, tok in enumerate(argv[1:]):
        if tok == "-m" and i + 2 <= len(argv[1:]):
            a.m = argv[1:][i+1]
        if tok == "--days" and i + 2 <= len(argv[1:]):
            a.days = int(argv[1:][i+1])
    return cmds[argv[0]](a)


if __name__ == "__main__":
    sys.exit(main())
