#!/usr/bin/env python3
r"""local_arms.py - LOCALARM-1004: fire every registered local arm, one model at a time.

The registry is the authority. Every arm in arms.json with lane "lmstudio" and
status "active" is fired here except lmstudio/auto, which daily.bat fires as part of
the desk run. Arms are grouped by the model the registry names, and each model is
loaded once: the model the morning preflight already loaded goes first, the rest
follow in registry order, and the box ends with that first model loaded again, as
it started. Only one model is ever in memory.

An arm with a "frame" field runs as a frame arm (kkr.py --frame); any other runs by
tag (kkr.py --local-arm). Either way kkr.py sends the registered model by name, so
a model left loaded by mistake cannot answer for an arm it is not.

Fail-open per arm: a failure is printed and logged and the next arm still runs.
Exit 0 when every arm reached the gate, 1 otherwise, so auto.bat's :run records a
miss as a miss. --plan prints what would run and touches nothing.

  python local_arms.py          fire the local arms
  python local_arms.py --plan   show the plan only
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TAG = "LOCAL_ARMS"
HERE = Path(__file__).resolve().parent
SKIP = {"lmstudio/auto"}          # fired by daily.bat
GATE = re.compile(r"gate: (\d+) accepted, (\d+) rejected")


def say(msg):
    print("%s: %s" % (TAG, msg), flush=True)


def lms_cmd():
    p = shutil.which("lms")
    if not p:
        return None
    return ["cmd", "/c", p] if p.lower().endswith((".cmd", ".bat")) else [p]


def lms(base, *args, timeout=900):
    r = subprocess.run(base + list(args), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def loaded(base):
    rc, out = lms(base, "ps", timeout=60)
    return out if rc == 0 else ""


def plan():
    arms = json.loads((HERE / "arms.json").read_text(encoding="utf-8-sig"))["arms"]
    local = [a for a in arms if a.get("lane") == "lmstudio" and a.get("status") == "active"]
    primary = next((a.get("model") for a in local if a.get("tag") == "lmstudio/auto"), None)
    groups, bad = {}, []
    for a in local:
        if a.get("tag") in SKIP:
            continue
        m = str(a.get("model") or "").strip()
        if not m:
            bad.append(a.get("tag"))
            continue
        groups.setdefault(m, []).append(a)
    order = sorted(groups, key=lambda m: (m != primary, list(groups).index(m)))
    return primary, [(m, groups[m]) for m in order], bad


def command(arm):
    # FRAMEROUTE-1004: only the arm named lmstudio/<frame> takes the shared frame path;
    # a frame arm on another model runs under its own tag and kkr reads its frame from
    # arms.json, so it can never seal under lmstudio/<frame> or run that arm's model.
    if arm.get("frame") and arm.get("tag") == "lmstudio/%s" % arm["frame"]:
        return [sys.executable, "kkr.py", "--provider", "lmstudio", "--frame", arm["frame"]]
    return [sys.executable, "kkr.py", "--provider", "lmstudio", "--local-arm", arm["tag"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    a = ap.parse_args()
    primary, groups, bad = plan()
    for t in bad:
        say("%s is registered without a model - not fired" % t)
    if not groups:
        say("no local arm to fire beyond lmstudio/auto")
        return 0 if not bad else 1
    for m, arms in groups:
        say("model %s -> %s" % (m, ", ".join(x["tag"] for x in arms)))
    if a.plan:
        say("PLAN ONLY - nothing loaded, nothing fired")
        return 0
    base = lms_cmd()
    if not base:
        say("lms is not on PATH - no local arm fired")
        return 1
    day = datetime.now().strftime("%Y-%m-%d")
    logdir = HERE / "state" / ("log_%s" % day)
    logdir.mkdir(parents=True, exist_ok=True)
    failed = list(bad)
    for m, arms in groups:
        if m not in loaded(base):
            lms(base, "unload", "--all", timeout=300)
            rc, out = lms(base, "load", m, "-y")
            if rc != 0 or m not in loaded(base):
                say("could not load %s - %s not fired: %s" % (m, ", ".join(x["tag"] for x in arms), out.strip()[-200:]))
                failed += [x["tag"] for x in arms]
                continue
        say("loaded %s" % m)
        for arm in arms:
            slug = re.sub(r"[^A-Za-z0-9._-]+", "-", arm["tag"])
            try:
                r = subprocess.run(command(arm), cwd=str(HERE), capture_output=True, text=True,
                                   encoding="utf-8", errors="replace", timeout=3600)
                out = (r.stdout or "") + (r.stderr or "")
            except subprocess.TimeoutExpired:
                out, r = "timed out after 3600 s", None
            (logdir / ("local_%s.log" % slug)).write_text(out, encoding="utf-8")
            g = GATE.search(out)
            bound = re.search(r"bound to registered model (\S+)", out)
            if g:
                say("%s: %s accepted, %s rejected (model %s)" % (arm["tag"], g.group(1), g.group(2),
                                                                  bound.group(1) if bound else "?"))
            else:
                tail = [ln for ln in out.strip().splitlines() if ln.strip()][-1:] or ["no output"]
                say("%s: no gate line - %s" % (arm["tag"], tail[0][:200]))
                failed.append(arm["tag"])
    if primary and primary not in loaded(base):
        lms(base, "unload", "--all", timeout=300)
        rc, _ = lms(base, "load", primary, "-y")
        say("restored %s" % primary if rc == 0 else "could not restore %s" % primary)
    say("%d arm(s) fired, %d failed%s" % (sum(len(x) for _, x in groups) - len([f for f in failed if f not in bad]),
                                          len(failed), (": " + ", ".join(failed)) if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
