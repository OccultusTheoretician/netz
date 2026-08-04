# NETZ — OPERATING MANUAL

**Built 2026-08-04 from `C:\netz` at remote HEAD `3d14128`, the machine map (745 files), and the batch files and workflow crons read as source rather than remembered.**

The 2026-08-01 file map answers *what exists*. This answers *what do I do, in what order, and when*. Where the two disagree, the batch file wins — it is what actually runs.

Three kinds of work, and only three:

| | | |
|---|---|---|
| **A** | runs on a clock you don't hold | GitHub Actions. Nothing to do. |
| **B** | runs when you type one word | `go`, then `publish` |
| **C** | needs your judgment | 0–3 items a day, named for you by `whatnow.py` |

Everything below is one of those three. If a thing is not in this document, it is not part of the daily loop.

---

## 1 · THE MORNING — the whole thing

```
cd C:\netz
go
```

That is the command. It runs five stages and then tells you what needs you.

| stage | what runs | what it does |
|---|---|---|
| **1/5** | `daily.bat` | `lms server start` → `tg_fetch` → `tg_translate --latest` → `tg_cluster --latest` → `tg_grade --latest` → `netz.py` → `kkr.py`. War desk ingests, translates, clusters cross-bias, grades. `netz.py` pulls RSS and writes `reports/battle_report_*.md`. `kkr.py` reads the newest report, elicits from `lmstudio/auto`, gates, seals, renders. |
| **2/5** | `fc_pass.py --draft` | Drafts failure conditions for rows that lack them. **Stops here by default.** |
| **3/5** | `conformance.bat` | Skips if `ledger.json` is unchanged. Otherwise `rpas_audit` → `REPORT_conformance.md`, `rpas_verify` → `docs/rpas_verdict.json`, `knp_verify` → `docs/knp_verdict.json`, syncs the standards texts into `docs/`. |
| **4/5** | `site_audit.py --section all` | Surface audit of the served site. |
| **5/5** | `whatnow.py` | Three tiers: **NEEDS YOU TODAY** (blocking, with the exact command), **STANDING** (real backlog, reported not nagged), **CLEAR** (done — so an absent line means handled, not forgotten). |

**Why stage 2 stops.** On 2026-08-01 a new arm shape produced 19 failure-condition proposals that named a *venue* where a *condition* belongs. They would have sealed non-empty and unfalsifiable — invisible on the published face. The stop is thirty seconds of reading `FC_REVIEW.md` and it is the thing that caught it.

```
python fc_pass.py --apply all
```

`go seal` skips that stop. Use it only on days nothing new ingested.

**If LM Studio was off** during the daily and the report exists but no forecast:

```
qwen_only.bat
```

Re-runs `kkr.py` against the existing latest report. No refetch.

---

## 2 · PUBLISHING — the second and last command

```
publish.bat
```

Opens both reports in the browser and **pauses**. Ctrl+C aborts; any key publishes. Then it copies `reports/latest.html` → `docs/report.html`, `forecasts/ledger.html` → `docs/ledger.html`, `forecasts/KKR_latest.html` → `docs/kkr.html`, `ledger.json` → `docs/`, commits, pushes, and **confirms from `git ls-remote` rather than the console** — failing loudly if remote HEAD doesn't match local.

`publish.bat` already copies the ledger face into `docs/`. Do not duplicate that by hand.

---

## 3 · WHAT RUNS WITHOUT YOU

| workflow | cron (UTC) | what it does |
|---|---|---|
| **SPION** | `17 */6 * * *` — every 6h at :17 | Page watch. Commits `docs/spion_state.json`, `docs/spion_log.json`, `spion_pending.json` under `spion[bot]`. Off the top of the hour on purpose: that slot is the most congested on GitHub's shared scheduler and the most likely to be deferred. |
| **AUDIT** | `41 5 * * *` — daily | *(new 2026-08-04)* `cite_integrity.py` + `ident_audit.py` → `*_latest.md/.json`, synced to `docs/`, committed under `audit[bot]`. Commit message carries the defect rate. |
| **OTS ANCHOR** | manual dispatch | Bitcoin anchoring of the eight anchored files. |
| **GUEST KALL** | issue-triggered | External sealed commitments through the guest gate. |
| **KALLS TOKEN** | manual dispatch | RFC 3161 token pass. |

**Cron here is best-effort.** GitHub delays and occasionally drops scheduled runs under load, which is why every record SPION writes says *observed at*, never *checked at exactly*. The published face says so.

**AUDIT's scope limitation, recorded because CI can't state it for itself:** it runs `ident_audit` **without** `--packets`, because `forecasts/kkr_packet_*.md` is gitignored and the runner never sees them. Its UNSOURCED findings mean *not present in the published record*, not *invented*. Your local run with `--packets` is the adjudicating one; CI publishes the floor.

Both bots rebase-and-retry three times and fail loudly rather than force anything. They will not fight your push.

---

## 4 · WEEKLY — the manual arms

All Anthropic manual arms run on the **same packet, same week**. Staggering them makes their Briers incomparable: arms forecasting different packets face different questions and different base rates. A missed run is a coverage gap and shows as one; it is never backfilled from a later packet.

**Step 1 — build the blinded packet:**

```
fable_packet.bat
```

Runs `netz.py` then `kkr.py --packet-only`, writes `forecasts/kkr_packet_[stamp].md`, opens the folder.

**Step 2 — upload that packet into a fresh project, no guidance, and say "run the forecast."** That absence of guidance is what makes the arm's access tag honest.

**Step 3 — ingest each arm's JSON:**

```
python kkr.py --ingest forecasts\opus_projections_[date].json --arm manual/opus-5/unattested --report battle_report_[stamp].md --packet kkr_packet_[stamp].md
```

`--report` and `--packet` are **not optional in practice.** Without `--report`, `latest_report()` takes whatever is newest on disk, and the row gets attributed to a record the arm never read — every citation then resolves against the wrong document. Without `--packet`, the same happens one level down.

**Arm tags.** Bare `manual/fable`, `manual/opus-5`, `manual/sonnet-5` are RETIRED. Live tags carry an access axis:

- `/searched` — the sealed text cites a retrieved source
- `/cold` — provably search-off session
- `/unattested` — search was available and the sealed text cites nothing retrieved. **This is the default under the KK18 standing rule**, and it is what a fresh no-guidance project produces.

**Step 4 — pair the control, same run:**

```
python baserate.py --from-ledger manual/opus-5/unattested --date [YYYY-MM-DD]
python kkr.py --ingest control_packet_[date]_[arm-slug].json --arm control/baserate --report battle_report_[stamp].md --packet kkr_packet_[stamp].md
```

The control emits the same probability for every row in a reference class, computed from this ledger's own resolved history, pre-registered before the outcome existed. It is not trying to be right. Its Brier is the floor a forecaster arm must clear; an arm that doesn't beat it has skill zero regardless of raw score.

`--out` composes its own filename from arm and date since KK21e. Do not override it without reason — the fixed default is what cost `KKR-20260803-01` its provenance permanently.

---

## 5 · RESOLUTION

**The only resolution path is `kkr.py --resolve`.** Nothing else writes a verdict to the ledger — not the resolvers, not the adjudicator, not the jury.

```
python kkr.py --resolve
```

**Never `--all`.** That walks all 300+ rows instead of the past-deadline ones. **Ctrl+C mid-run discards everything** — the tool buffers and writes at session end.

### Before you resolve — get the evidence

```
python mechanical_adjudicator.py --due --keep-raw
```

Fetches named public endpoints for due rows and **proposes** a verdict with a SHA-256 hashed evidence record in `evidence/`. It never sees the arm or the probability while judging, which is what makes it blind by construction. It writes nothing to the ledger.

**Current honest coverage: 10 of 265 open rows (4%).** 219 unmapped come back as *"resolution basis is a statement/press-release shape — a search problem, not a feed read."* The resolver is not the bottleneck; the rows are.

### Verifying the parsers

```
python mechanical_adjudicator.py --smoke --keep-raw
```

One row per resolver, forced probe, regardless of deadline. Every record it writes carries `probe: true`, the row's deadline, `verdict_if_resolved_now` instead of `verdict_proposed`, a `_probe` filename suffix, and a line refusing to be cited as resolving evidence.

**First run, 2026-08-04:** treasury10y ok · kev ok · usgs ok · gdacs **YES but false — its own detail line names a Green alert while the predicate asked for red; the matcher is a substring test over flattened item text** · ecb INDETERMINATE (honest refusal: `missing observation`) · fedreg ok. **Four of six trustworthy, one refusing correctly, one false-positive in the dangerous direction.**

### Other resolution support

| command | does |
|---|---|
| `duecheck.bat [thresh]` | Due queue + three keyless lookups in one pass. Deliberately not an auto-resolver — its header records why: of eight probed endpoints, two returned passing-looking HTML shells, one served the wrong instrument, one sat behind a bot challenge. |
| `lookup.bat` | `desk_lookup.py` — reproducible keyless lookups: `treasury`, `kev`, `quake`. Prints the value and the query a stranger can re-fetch. |
| `python wardesk_evidence.py` | Grade-A war-desk corpus evidence for open rows → `forecasts/EVIDENCE_*.md` |
| `audit_export.bat` | Blinded packet of past-deadline rows. Probabilities and arm tags withheld; prompt SHA-256 printed into the packet. |
| `audit_rule.bat` | Single-auditor verdicts in, **you rule per row**. |
| `python kkr.py --jury A.json B.json --auditors X Y` | Blind jury. Concordance recommends, discord escalates, you rule, kappa → `jury_log.json`. |

**On the jury and on automating adjudication.** `jury_log.json` entry one is the finding that governs this: Qwen returned the correct MISS verdict *by citing outlets it cannot access*. Fabricated evidence landing on a right answer — a failure invisible to any check that only looks at the verdict. Qwen is cold and has no network; anything it "cites" it invented. The only honest architecture is retrieval outside the model: Python fetches and hashes, the model reads only what Python holds, and a proposal whose evidence Python cannot independently re-fetch becomes ABSTAIN rather than a verdict.

---

## 6 · SEALING A KALL

```
seal.bat
```

`candidate_desk.py --new` → `conformance.bat --force` → commit → push. Then, per RPAS 4.05:

```
syndicate.bat
```

Posts the seal hash to Bluesky as a third-party dated commitment.

---

## 7 · THE STATUS COMMANDS

```
python desk.py status     what is true right now
python desk.py due        what needs resolving
python desk.py verify     assert the invariants; non-zero exit on failure
python desk.py ship       verify, commit, rebase, push, confirm from remote
python whatnow.py         what needs YOU, in three tiers
```

`desk.py verify` earns its keep. Three separate mirrors drifted in one night — the protocol document, the ledger JSON, the report face — each found by hand, late, after the public copy had been wrong for hours. They are assertions now, and `ship` refuses to run if they fail.

---

## 8 · THE AUDITS OF THE DESK ITSELF

| command | asks |
|---|---|
| `python cite_integrity.py --report X.md --json X.json` | Do cited items actually support their claims? Per-item, IDF-weighted, shotgun-capped. Cross-tabs against keyed/keyless. |
| `python ident_audit.py --packets forecasts --report X.md --json X.json` | Do identifiers in synthesis prose exist in the record beneath them? **Always pass `--packets`** — without it UNSOURCED is unadjudicable. |
| `python rpas_audit.py --ledger ledger.json --report REPORT_conformance.md` | RPAS conformance. Runs inside `conformance.bat`. |
| `python type3.py --scope E.json` / `--run` / `--report` | Type III third-party engagement against a foreign forecast record. Twelve procedures, each traceable to a named clause. SCOPE is a first-class outcome. |
| `python desk_fragility.py` | The desk auditing its own foundation → `forecasts/FRAGILITY_*.md` |
| `python site_audit.py --section all` | Served-surface audit. Runs in `go` stage 4. |
| `python navgen.py` | Regenerates nav on every served page from `nav_manifest.json`. Run after adding a page. |

---

## 9 · THE RULES THAT COST SOMETHING TO LEARN

**Verification.** Confirm pushes with `git ls-remote origin main` from the remote, not the console. For per-file checks use commit-pinned raw URLs — CDN caching on branch URLs masks fresh content.

**Sealed rows are never edited.** A defect found after sealing is a printed finding, not a substitution. Corrections enter the record as new entries.

**Never `git add -A` from the repo root mid-session** unless you have just read `git status --short`. It swept duplicate packet copies in tonight and they had to be removed in a follow-up commit.

**Patches and tools live in `Documents\`, never the repo root.** *(Currently violated — see §11.)*

**Every script written in a session must be saved that same turn.** Container destruction destroys unsaved work.

**PowerShell, not CMD.** `$env:USERPROFILE`, not `%USERPROFILE%`. `Copy-Item -Destination X -Force`, not `copy /Y X .`.

**Run artifacts never overwrite.** Since KK21f/h, `runguard.write_run_artifact` suffixes `_2` and prints rather than discarding a different run. This closed a class that appeared **five times in one day** and defeated two naming-based fixes: a name encodes what its author anticipated, and a run always has one more distinguishing property than that.

**GitHub Pages is case-sensitive; Windows is not.** og:image 404s traced to exactly that.

---

## 10 · WHAT THE MACHINE MAP TURNED UP

745 files: 239 root · 238 `docs/` · 156 `forecasts/` · 91 `reports/` · 12 `evidence/` · 6 `.github/` · 3 `vault/`.

**Local-only, gitignored, lost if the machine is lost:**

- **24 `kkr_packet_*.md`** — the elicitation input for 206 sealed rows. Not on the record. This is the largest single gap on the book and it lands on §7.04's novelty scope: keyed/keyless asks whether a claim could be deduced from declared priors, and the priors' full text is not published.
- **65 war-desk chain files** — `tg_events_*`, `tg_translated_*`, `tg_wardesk_*`. The evidence chain behind every WARDESK render.
- `identity_salt.local.txt`, `identity_sweep.local.txt`, `state.json`, `vault/`
- `FC_REVIEW.md`, `fc_proposals.json`, `DECC_CONFORMANCE_REPORT.json`, `KriegForeKaster_projections.json`, `fogsim_campaign*.json`, `kfk_*_2026-07-29.json`
- `warroom.py` / `warroom.html` — **untracked and unmentioned in any session record.** Worth a look; either it belongs on the record or it should be named as retired.

**Housekeeping the map exposed:**

- **18 `.bak` files and 10 `patch_kk2*.py` sitting in the repo root.** Gitignored, so `git add -A` can't sweep them — but the standing rule puts patches in `Documents\`, where 124 other `.py` files correctly live. Tonight's drift is mine: every command I wrote said `-Destination C:\netz`.
- `forecasts/kkr_packet_latest.md` exists as a pointer alongside the dated packets.

---

## 11 · CLEANUP, WHEN YOU WANT IT

```
cd C:\netz
New-Item -ItemType Directory -Force "$env:USERPROFILE\Documents\netz_patches" | Out-Null
Move-Item patch_kk2*.py "$env:USERPROFILE\Documents\netz_patches\" -Force
Remove-Item *.bak -Force
git status --short
```

Nothing tracked moves. `git status --short` at the end confirms it.

---

## 12 · THE BOARD

| # | open | note |
|---|---|---|
| 1 | **191 rows with no keyed/keyless determination** | 151 unset + 40 literal `unset`, against 75 keyed and 37 keyless. Largest conformance gap, sits directly under §7.04. |
| 2 | **§7.06 revision-history entry unwritten** | 254 ambiguous-reference rows, 8-of-36 keyless defect rate, the ingest path never having been citation-gated, the synthesis-fabricated identifier, and a keyed hit whose condition was already true at issue. All currently live in audit files and commit messages. |
| 3 | **GDACS resolver false positive** | Substring match over flattened item text; returned YES on a Green alert against a red predicate. Fails in the dangerous direction. |
| 4 | **Preconditions: 0 of 303** | `abyss.py` still has nothing to read. |
| 5 | **Packets not on the record** | 206 rows name a `source_packet` no stranger can retrieve. Publishing hashes rather than bodies would close it without republishing ten days of feed content — the move DECC-26 already makes. |
| 6 | **Registry data** | TimesofIsrael zero-yield, `sdf_press`. |
| 7 | **Rows not written to be resolvable** | ~172 of 234 narrative rows are automatable *in principle* — Treasury/FRED/ECB for economics, Federal Register and Congress.gov for political, KEV/NVD for cyber, USGS/GDACS/NIFC for disaster. Military/conflict is 57 rows and has no mechanical source, permanently. The fix is a generation rule preferring a mechanically checkable source of record, not a better resolver. |
| — | **Entity formation** | Not a build. Unblocks the trademark filings, the certification mark, the counsel brief, Phase 4, and Aspen Peaks contracting. Nothing else on the board unblocks four things at once. |

---

## 13 · THE CARD

```
MORNING          cd C:\netz
                 go
                 python fc_pass.py --apply all      (after reading FC_REVIEW.md)
                 publish.bat

DUE ROWS         python mechanical_adjudicator.py --due --keep-raw
                 python kkr.py --resolve            (never --all; never Ctrl+C)

WEEKLY ARMS      fable_packet.bat
                 python kkr.py --ingest F --arm TAG --report R --packet P
                 python baserate.py --from-ledger TAG --date D
                 python kkr.py --ingest control_packet_D_slug.json --arm control/baserate --report R --packet P

STATUS           python whatnow.py
                 python desk.py status | due | verify | ship

SEAL A KALL      seal.bat  →  syndicate.bat

VERIFY A PUSH    git ls-remote origin main
```

Two commands cover a normal day. Everything else is on this page for the day that isn't normal.
