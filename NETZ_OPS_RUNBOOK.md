# NETZ OPS RUNBOOK — v1 (2026-07-25)

*Operational procedure for the desk's repository and publishing chain. Not canon, not theory — the sequence of commands and the error classes that produced them. Every rule below was paid for.*

\---

## 0\. THE THREE WORDS

Everything routine is three commands:

|word|what it does|
|-|-|
|`daily`|`daily.bat` — netz.py + kkr.py collection run|
|`seal`|`seal.bat` — veiled entry → conformance regen → commit → push → prompts external clock|
|`publish`|`publish.bat` — review gate → conformance regen + standards sync → targeted add → timestamped commit → push|

If a task isn't one of those three, it's below.

\---

## 1\. THE SHELL — know which one you're in before pasting

**The prompt tells you.** `PS C:\\netz>` is PowerShell. `C:\\netz>` is cmd.exe. Every procedure in this runbook is PowerShell. Pasting PowerShell into cmd fails on `$vars`, `\[Type]::Method()`, and semicolon chaining.

Recovery: type `powershell` and press enter. Prompt changes to `PS`.

**Never paste a command containing angle-bracket placeholders.** `cd <netz>` — PowerShell reads `<` as a reserved operator and the whole line dies. Literal paths only: `cd C:\\netz`.

\*\*`.NET file calls do not follow `cd`.\*\* `\[IO.File]::ReadAllText('docs\\index.html')`resolves against the process's working directory, not the shell's. Always anchor:`$f="$PWD\\docs\\index.html"`.

\---

## 2\. THE GATE — always first, no exceptions

Nothing gets added, committed, or pushed until the gate is verified. The gate is `.gitignore`.

```powershell
cd C:\\netz; git status --short; git check-ignore -v netz\_wardesk.session netz\_bundle.zip warroom.html
```

`check-ignore` must print a match line for each. `git status --short` must not show any sensitive file as tracked or staged.

**Permanently excluded classes:** `\*.session` (auth keys — a Telegram session file operates the account without a password), bundles/zips, raw scrape output (`forecasts/tg\_\*`), `warroom.html` / `warroom.py`, `state.json`, `\*.bak`, `\*\_backup.py`, test dirs, `.conformance\_last`.

**If a sensitive file is already tracked:** revoke the credential first (terminate the session in the app), *then* deal with git. Revocation kills the exposed key regardless of what history says. History rewriting is second, never first.

\---

## 3\. NEVER `git add -A`

`-A` stages whatever happens to be in the folder — including files the gate doesn't cover yet, working files, and anything a pipeline dropped since the last commit. `publish.bat` has been rewritten to use a targeted add list for this reason.

**Rule:** name every path. If the list is long, that's the cost of knowing what shipped.

\---

## 4\. EDITING FILES — the download path is canonical

**Tonight's most expensive error class.** Long code pasted into notepad picks up line-wraps from chat rendering and produces syntax errors (an f-string split across lines). Then the broken file gets committed, and the fix attempts compound.

**Rule: anything over \~100 lines is downloaded, not pasted.** Chat link → Downloads → `Copy-Item ... -Force`.

**For surgical edits, use Python — not PowerShell string replacement.** The working copy is CRLF. PowerShell `-replace` and `.Replace()` patterns written with `\\n` silently miss every line in a `\\r\\n` file, and the command reports success while changing nothing. Python read in text mode normalizes newlines and matches reliably.

Pattern for a surgical edit:

```powershell
cd C:\\netz
@'
import io
p="target.py"
src=io.open(p,encoding="utf-8").read()
# ... anchor-based edit, with an assert to prove it took ...
assert src.count("expected marker")==1
io.open(p,"w",encoding="utf-8",newline="\\n").write(src)
print("patched OK")
'@ | Set-Content -Encoding UTF8 patch.py
python patch.py
```

**Design surgical patches to be idempotent** — safe to run twice. A patch that duplicates a line on a second run creates a new bug while fixing the old one.

**Prefer anchor-based block rewrites over line matching.** Find a stable start and end marker, replace everything between. Line-level matching breaks on whitespace and newline drift; block rewriting doesn't.

\---

## 5\. THE COMPILE GATE — never push an unrun script

```powershell
python -m py\_compile target.py
if($LASTEXITCODE -eq 0){ <run, add, commit, push> } else {"COMPILE FAILED - stop"}
```

Tonight a crashed script's broken source got committed while the output it should have produced never regenerated. The gate costs one line and catches the entire class.

**Same principle for generated output:** if the generator crashes, the artifact is stale. Check the artifact, not the exit code of the commit.

\---

## 6\. VERIFY FROM THE SERVED BRANCH, NOT THE LOCAL COPY

Local success does not mean published success. Verify what the world sees.

**Caution: `raw.githubusercontent.com` caches.** It served stale content twice tonight and produced two false "still broken" verdicts on a fix that had already landed. Cache-busting query strings help but are not reliable.

**True HEAD, no CDN:**

```
https://codeload.github.com/OccultusTheoretician/netz/tar.gz/refs/heads/main
```

Pull the tarball and read the files out of it. That is ground truth.

**When a check contradicts expectation, suspect the instrument before the artifact.** An empty API response, a rate-limit message, a cached read — these are *non-findings*, not clean results. Distinguish "the check returned clean" from "the check did not run." (LIAS 3.04 exists because of this.)

\---

## 7\. GITHUB PAGES — what actually gets served

**Pages serves `docs/` only.** A file at repo root is in the repository but not on the site. Tonight's 404 on the conformance report was exactly this.

**Root-authored files must be synced.** `conformance.bat` now does this automatically for the standards documents and the report. Anything new that must be public needs adding to that sync list.

**`docs/.nojekyll` is present and must stay.** Without it, Pages runs Jekyll and renders `.md` files with a default white theme. With it, `.md` serves as raw text — which is the better archival form for a standard: exact bytes, no theme in between.

**`docs/CNAME`** carries the custom domain. Don't delete it.

**Canonical vs. archive copies:** for `standards.html`, `docs/` is canonical and root is a stale archive. Never sync root→docs for that file; it regresses fixes.

**Cloudflare sits in front.** After a push, allow a minute or two for Pages to rebuild, then check in incognito. Purge cache from the dashboard if stale.

\---

## 8\. HISTORY PURGE (use sparingly)

When something that shouldn't be public has been committed and pushed, and the content is cosmetic-to-moderate sensitivity:

```powershell
git reset --soft <last-clean-commit>
git add <explicit file list>
git commit -m "<single clean message>"
git push --force
```

This collapses everything since the clean commit into one commit and removes the intermediates from reachable history.

**Limits, stated honestly:** orphaned commits stay fetchable by exact SHA until GitHub garbage-collects. Nobody browses to them, but they exist. A support ticket forces the GC if the belt-and-suspenders is wanted. Anything genuinely secret (credentials, keys) is **revoked, not purged** — purging is for embarrassment, revocation is for security.

\---

## 9\. THE ARCHIVE SEQUENCE (external clock — RPAS 4.05)

After a publication that matters:

1. Verify from the served branch (§6) that content is correct — archive captures what is there, mistakes included.
2. Incognito load of each live URL; confirm the page renders and reads right.
3. archive.ph each URL: site root, the standards page, each standards document, the ledger, the conformance report.
4. Glance at each capture. JS-populated elements (stat bands, live verdicts) may freeze at their loading state — that's an archive-tool limitation, and the underlying JSON carries the numbers anyway. Content errors are not; re-snapshot after fixing.

Snapshots stack. An earlier capture is never undone by a later one — it becomes a timestamped earlier state. **This means: fix before archiving when possible, but never treat an existing snapshot as a reason not to correct.**

\---

## 10\. PRE-PUBLICATION SWEEP (compartment)

Before any push that changes public-facing text, sweep every served surface for identity terms and local paths:

```powershell
Select-String -Path docs\*.html,docs\*.md,*.html,*.md -Pattern (Get-Content identity_sweep.local.txt -Raw).Trim() | Select-Object -First 20
```

The pattern lives in `identity_sweep.local.txt`, which is gitignored: a runbook that prints the descriptors it screens for publishes exactly what it protects. Keep that file local; it is a soft sweep, not the hashed guard, because a place name appears legitimately in feed content and would block every ship if it entered `identity_guard.json`.

Also sweep generated JSON payloads — `notes` and `evidence` fields in pipeline output can carry local paths and names that never appear in source.

**The lesson from tonight:** small-pool descriptors are the risk, not names. Names nobody and identifies one person. Compartment discipline is about *inference chains*, not literal identifiers.

\---

## 11\. WHEN A COMMAND CHAIN FAILS

Order of suspicion, in order:

1. **Wrong shell** (§1) — check the prompt.
2. **Placeholder pasted literally** (§1) — check for `<`.
3. **Nothing actually changed** — `git commit` with nothing staged aborts and says so; a "successful" push that changes nothing means the edit missed. Read the output, don't assume.
4. **CRLF defeated the match** (§4) — switch to the Python patch pattern.
5. **Stale read** (§6) — verify against the tarball before concluding the fix failed.
6. **Wrong directory** — `.NET` calls and relative paths (§1).

**Stop after two failed surgical attempts.** The third attempt is where compounding damage happens. Fall back to the download path (§4), which is slower and always works.

\---

## APPENDIX — FILE INVENTORY (what lives where, C:\\netz)

**Automation:** `daily.bat` · `publish.bat` (review gate, hardened) · `conformance.bat` · `seal.bat` · `score.bat` · `syndicate.bat` · `run\_netz.bat` · `kkr.bat` · `mine.bat` · `archiv\_\*.bat` · `audit\_\*.bat` · `fable\_\*.bat`

**Instruments:** `rpas\_audit.py` (conformance auditor + migration) · `candidate\_desk.py` (veiled entry creation) · `netz.py` · `kkr.py` · `tg\_\*.py` · `warroom.py` (local only, gitignored) · `syndicate.py` (external clock) · `wardesk\_wire.py`

**Records:** `ledger.json` (canonical) · `ledger.json.pre\_rpas` (pre-migration backup, gitignored-adjacent — leave it) · `REPORT\_conformance.md` · `war\_channels.json` · `audit\_verdicts\*.json` · `forecasts/`

**Standards:** `RPAS\_FIRST\_EDITION\_2026\_v1.md` · `LIAS\_FIRST\_EDITION\_2026\_v1.md` · `STANDARDS\_MAPPING\_RPA\_2026-07-24.md` · `RETRO\_PRESCIENT\_AUDIT.md` (the sealed definition)

**Served (`docs/`):** `index.html` · `standards.html` · `ledger.html` · `report.html` · `kkr.html` · the three standards + conformance report · `ledger.json` · `war\_desk.json` · `crow.png` · `CNAME` · `.nojekyll`

**Held out deliberately (untracked, not gitignored):** `forecasts/WARDESK\_2026-07-24\_\*.md` — six files, pipeline output, unreviewed. Ruling pending: open one; if clean graded output, publish the set as dated record; if raw-scrape residue, one ignore line classifies the class.

