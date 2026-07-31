# SITE AUDIT — retroprescientaudit.com
## 2026-07-30 · 20 pages · run against local clone at HEAD

**PROVENANCE: DRAFT.** Findings are mechanical (counted, not sampled).
`site_audit.py` — the desk's own enumerating auditor — supplies the
infrastructure layer; this report adds the SEO/discoverability layer it does
not check, and root-causes both together.

---

## WHAT PASSED (his auditor, by enumeration)

813 href/src references resolved against disk — **zero broken, zero
case mismatches**. Zero third-party stylesheets or scripts: the "nothing
phones home" claim holds and is now checked, not asserted. Every page declares
lang, title, viewport. Every img carries alt. Every form control has a name.
Script-filled slots degrade correctly with JS blocked. Animating pages honour
`prefers-reduced-motion`. No BOMs. No credential-shaped values across 351
tracked text files. No vault-tier or backup file tracked. This is a clean
infrastructure baseline — the gaps below are discoverability and consistency,
not breakage.

---

## FINDINGS — 9, all mechanical

### The root cause behind most of them
Seven of the nine trace to **one thing: served renders lag their generators.**
`desk.py ship` regenerates the script-emitted pages; the fixes that already
landed in generator sources (Nebelkrähe casing, the TM marks) have simply not
been re-emitted yet. Regenerate first, then hand-patch only the genuinely
hand-authored remainder. Do not fix these page-by-page before regenerating —
that duplicates work the render will redo.

### 1 — Casing on 10 served pages (HIGH, cosmetic-but-visible)
`NebelKr&auml;he` (capital K) renders on KriegForeKaster, fogsim, index, kkr,
konsole, kraehes_kalls, okk, register, report, ledger. Generator sources were
corrected last pass. Script-emitted pages (ledger, kkr, report, konsole) heal
on next ship. Hand-authored pages (index, register, kraehes_kalls, fogsim,
okk, KriegForeKaster) need the in-place fix in the patch.

### 2 — Marks lag on 2 served pages (HIGH per IP work)
`kraehes_kalls.html`: 6 unmarked "Krähe's Kalls". `standards.html`: 2 unmarked
"Krähe's Nest". The mark pass hit sources; these renders lag. First-use-per-page
marking, in the patch.

### 3 — decc.html has no social metadata (MEDIUM)
No og:image (his auditor caught this), and also no twitter:card, no og:url, no
og:title. Shared links preview as a bare URL. This is the flagship standard
page — it is the one most likely to be shared. Full social block, in the patch.

### 4 — decc.html absent from sitemap (MEDIUM, his auditor)
Tracked and indexable but unlisted. A crawler is told the site's map does not
include its most important standalone page. Add the `<url>` block.

### 5 — konsole.html has no social metadata (LOW)
Same shape as decc but a lesser page (cabinet tool). Add a minimal block or
accept — operator's call.

### 6 — Canonicals missing on 19 of 20 pages (LOW)
Only index.html self-references. Single-domain site so duplicate-content risk
is low, but a self-referencing canonical is one line and closes the question.
Best added in the generators' shared `<head>` template so it applies on every
emit rather than per-page forever.

### 7 — Four pages have zero H1 (LOW, structural)
kkr, konsole, ledger, report — the script-heavy dashboard pages. One H1 each
is correct for structure and accessibility even where a masthead visually
substitutes. Fix in the generators that emit them.

### 8 — Runnable command not translation-shielded (LOW, his auditor)
kkr.html carries `python kkr.py...` outside `translate="no"`. Machine
translation would rewrite the command and it would verify nothing. Wrap the
element. Fix in the generator.

### 9 — patch_site_marks_fix.py untracked, sweepable (HOUSEKEEPING)
Not a site issue — last turn's patch file sitting where `git add -A` (inside
`desk.py ship`) would grab it. Stage it deliberately or delete it.

---

## REMEDIATION ORDER

1. **Regenerate first.** `desk.py ship` (or the render step) re-emits the
   script-built pages, clearing casing on ledger/kkr/report/konsole and any
   marks the generators now carry. Confirm with a re-run of `site_audit.py`.
2. **Then hand-patch the remainder** — the accompanying patch fixes the
   genuinely hand-authored pages: casing on index/register/kraehes_kalls/
   fogsim/okk/KriegForeKaster, marks on kraehes_kalls/standards, decc.html's
   social block and sitemap entry.
3. **Generator-level fixes** (canonicals #6, missing H1s #7, translate-shield
   #8) go into the `<head>`/body templates in netz.py so they apply on every
   future emit — one edit each, permanent. Lowest priority; the site is
   discoverable without them.
4. **Re-run `site_audit.py`** — target state is the SUMMARY showing only
   findings the operator has consciously accepted (e.g. konsole social).
5. Stage named files, `desk.py ship`, verify from the remote.
