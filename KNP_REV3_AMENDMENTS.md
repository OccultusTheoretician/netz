# KNP-26 REVISION 3 — AMENDMENTS
**Drafted 2026-07-29 UTC · against HEAD e5e4e0f · PROVENANCE: DRAFT** (Claude-drafted under direction; his only after rework. Every external citation below was verified against the source on 2026-07-29 by live retrieval; the C2PA paper is cited to the version its authors analyzed.)

Six amendments to KNP-26, two to KNM-26, one finding drafted for printing, and the sweep-seven register entries. The controlling defect: the canonical preimage binds `id | timestamp | statement | resolution_basis | salt` and excludes `probability` and `deadline` — the two inputs to every Brier figure. A sealed Kall proves the committer said a thing; it proves nothing about the confidence or the horizon being scored. Restating 85% as 55% after sealing leaves every commitment verifying, and today the third-party verifier does not even compare those fields across snapshots. Revision 3 binds them going forward, guards the cheap cheat retroactively at the verifier, replaces two enforcement mechanisms that tested vocabulary instead of structure, and corrects a false sentence about split-view detection before it prints.

External instance of the defect class, for the record and the letter: the UMBC formal-methods analysis of C2PA v2.2 (Golaszewski, Krawetz, Sherman, Zieglar, et al., Cryptology ePrint 2026/804) found that nothing in C2PA's signed data references the trusted timestamp, so timestamps can be removed or replaced without detection — data the validator displays, outside the material the signature covers. The Kall construction has the same shape: the hashlog displays probability and deadline; the commitment does not cover them. The defect class has a named external instance in a major deployed system, found by independent adversarial analysis. That is what the finding below cites.

---

## AMENDMENT 1 — KNP 2.01b: Construction v2 (normative, must for Kalls sealed after this revision)

Insert after 2.01:

> **2.01b Construction v2 (`knp-2`).** For Kalls sealed under revision 3 or later, the canonical preimage is formed by joining exactly these fields with the ASCII pipe `|` in exactly this order:
>
> ```
> id | timestamp | statement | resolution_basis | probability | deadline | salt
> ```
>
> - `probability` — the integer percent, rendered as a decimal ASCII integer with no sign, no leading zeros, no decimal point, no percent sign (`35`, never `35.0`, `035`, or `35%`). The sealer coerces to this form before hashing and stores the same integer in the vault and the hashlog. Values ≤ 0 or ≥ 100 are certainty claims, not forecasts, and must be refused at sealing.
> - `deadline` — the ISO 8601 calendar date exactly as stored, `YYYY-MM-DD`.
> - All other fields as in 2.01. The pipe-escape rule applies to `statement` and `resolution_basis` only; `id`, `timestamp`, `probability`, `deadline`, and `salt` are constrained grammars that cannot contain the separator, so escaping them is a defined no-op in every conformant implementation.
>
> Every record in the hashlog and the vault carries a `construction` field naming its version (`knp-1`, `knp-2`). **A record without a `construction` field is a `knp-1` record** — this default exists so the ten Kalls sealed before this revision remain verifiable without alteration. A commitment is verified under the construction it names, always; the published commitment governs (4.01b). Sealing new Kalls under `knp-1` after this revision is nonconformant.
>
> Rationale, printed rather than implied: under `knp-1`, the two inputs to every Brier score sit outside the commitment. The construction that binds them was in fact the method's stated intent — KNM-26 revision 1's paragraph 3.01 described a commitment over statement, basis, probability, and deadline, and was reconciled *downward* to match the deployed construction in revision 2. This paragraph restores the original intent going forward without breaking a single existing seal.

**Canonicalization ruling encoded (was flagged in the prior session for the operator's ruling):** integer percent, as specified above. This matches what `cmd_seal` already coerces and stores (`int(round(p))`, refusing ≤0 and ≥100), so the spec describes deployed behavior rather than legislating new behavior. The `solve` subcommand's forensic render variants (`int`/`pct`/`frac`/`frac2`) remain a recovery tool and are not conformant constructions.

## AMENDMENT 2 — KNP 4.01c: The construction history (must where more than one construction exists)

Insert after 4.01b:

> **4.01c The construction history.** A hashlog containing records sealed under more than one construction must publish a `construction_history` array carrying every construction ever used, each entry bearing a `version` string, the full recipe in the 4.01b shape, and an `effective` date. The singular `construction` block of 4.01b remains and **must state the recipe of the log's earliest records** (`knp-1` for the reference deployment), so that a verifier written against revision 2 — which applies the singular block to every reveal — continues to return correct verdicts on every record sealed before this revision. A version bump without a preserved history destroys the verifiability of the rows it did not touch, which is a worse defect than the one it repairs.
>
> Failure direction, stated: a revision-2 verifier handed a `knp-2` reveal will recompute under `knp-1` and report a mismatch — a false alarm on a valid record, never a false pass. That is the conservative direction, and this paragraph chooses it deliberately. Verification of `knp-2` records requires a revision-3 verifier.

## AMENDMENT 3 — KNP 4.02, extended: published metadata is frozen at sealing (must)

Amend 4.02 by appending:

> A reveal or resolution updates the `status` field (and, at reveal, may add nothing else); it must never remove a record or alter its `commitment`, `timestamp`, `probability`, or `deadline`. For `knp-2` records the last two are bound by the hash; for `knp-1` records they are not, and this sentence is therefore load-bearing: **restating a sealed probability or deadline is the cheap cheat** — it leaves the count undisturbed, the denominator unchanged, and the standing line identical while reducing the Brier cost of an approaching miss. 5.05 guards the expensive cheat (deletion); this sentence guards the efficient one. A conformant verifier comparing two snapshots of the same hashlog treats any change to a sealed record's `probability` or `deadline` as a MUST failure, identical in class to an altered commitment.

*(Implementation note: the revision-2 verifier's append-only check compared `commitment` and `timestamp` only. The revision-3 verifier compares `probability` and `deadline` as well. This closes finding III.1 of the 2026-07-29 enumeration at the only place it can be closed for the ten existing seals — across externally-anchored snapshots — while Amendment 1 closes it cryptographically for everything sealed from now on.)*

## AMENDMENT 4 — KNP 4.03b/4.03c: the anchor resolves, and the head is externally timestamped

Replace the enforcement of 4.03 (currently a word-match: a hashlog containing the token "anchor" passes) and insert:

> **4.03b The anchor object (must).** The hashlog carries a structured `anchor` object declaring the append-only mechanism: at minimum a `mechanism` string and, per mechanism, the pointer fields a stranger needs to walk it (`repository` and `history` URLs for public version control; token path and digest fields for a timestamping authority; witness key and cosignature fields for a cosigned checkpoint). A conformance verifier must test that the object exists, is structured, and that its pointers are well-formed and internally consistent; prose containing the word "anchor" satisfies nothing. Where the verifier can resolve a pointer without credentials, it should; where it cannot, it prints the exact command a reader would run.
>
> **4.03c External timestamp anchoring (must for hashlogs published after this revision).** On each append, the committer obtains a timestamp token from an external authority over the SHA-256 digest of the hashlog file as published — an RFC 3161 timestamping authority, an OpenTimestamps attestation, or a transparency-log witness cosignature per c2sp.org/tlog-witness — and publishes the token beside the hashlog with its covered digest declared in the anchor object. Version-control history (4.03a) remains required; it is the *sequence* anchor. The timestamp token is the *existence* anchor: a dated third-party artifact the committer cannot amend or un-issue, which a repository host's history — however unlikely the rewrite — does not by itself provide against its own operator, and which a deletable social post does not provide against the committer.
>
> **Split-view, stated honestly (replaces any statement that split-view detection is unavailable to a single-operator log).** Serving different views to different readers is the transparency-log attack class. Gossip — readers comparing signed tree heads among themselves — was Certificate Transparency's 2013 answer and was never widely deployed even there. The operational answer since 2016 is proactive **witness cosigning** (Syta et al., IEEE S&P 2016; standardized in the C2SP tlog-checkpoint / tlog-cosignature / tlog-witness specifications; deployed by Sigsum and by the public witness network operated under transparency.dev): independent third parties verify append-only consistency and cosign each head, and a head lacking the cosignatures a reader's policy requires is rejected. Witnesses are not conformers; a federation of one can obtain them. Accordingly: a single-operator log **must** anchor per 4.03c, **should** obtain witness cosignatures where a witness will serve it, and cross-conformer view comparison activates at N ≥ 2 as an additional layer, not as the first available one. The operator-side mirror invariant (canonical-versus-served comparison before publish) is a required control of the sealer and an insufficient one — it compares two copies the operator holds and the operator can disable it; paired with 4.03c it becomes evidentiary, because a served view diverging from an externally-timestamped canonical digest is provable after the fact by any reader holding both.

## AMENDMENT 5 — KNP 4.04: the standing line, must and externally computable

Replace 4.04:

> **4.04 The standing line (must).** The hashlog's rendered surfaces carry the standing summary `N sealed · M revealed · K resolved`. Each figure must be computable by a third party from the published hashlog alone — `N` is the record count, `M` and `K` are counts over the `status` field — and a conformance verifier recomputes them and treats any published standing line that disagrees with its own recomputation as a MUST failure. A standing line computed only by the committer over his own log is a self-report; this paragraph makes it a derivation.

## AMENDMENT 6 — KNP 7.00: the conformance taxonomy, stated before a stranger states it

Insert at the head of Chapter 7:

> **7.00 What this chapter is, in the standards-body sense.** Chapter 7 is a **conformance clause**, and `knp_verify.py` is a **conformance test suite**: pass/fail against numbered requirements, runnable by anyone. It is **not a conformance program** — a program, in the sense the standards literature (NIST's conformity-assessment vocabulary) gives the term, includes an administrative apparatus with a dispute-resolution body of impartial experts, and no such body exists here or is claimed. The distinction is load-bearing, not pedantic: the independent security analysis of C2PA (ePrint 2026/804) found a conformance program that certified products without technical review or defined requirements, and the inflated word was part of what the analysis indicted. This specification takes the smaller, true word.

---

## KNM-26 AMENDMENTS

**KNM 3.01, appended sentence:** "KNP-26 revision 3 defines a successor construction binding probability and deadline for Kalls sealed thereafter, restoring this standard's revision-1 intent going forward; records sealed under the earlier construction remain governed by their published commitments and by the disclosure duty of this paragraph."

**KNM 7.02, appended occupancies (sweep seven, 2026-07-29, executed on the Fable model with live retrieval):**

> Productized prediction pre-commitment is established: **Forecastr** (forecastr.dev, operating since April 2026) binds input, model, and output into a hash chain sealed by RFC 3161 timestamp and on-chain anchor before outcomes exist, marketed as the cryptographic evidence layer for EU AI Act Annex IV obligations. Per-item commitment with external anchoring, productized for regulatory evidence, is therefore occupied. Forecastr implements full-transparency logging of every prediction; it does not implement the abyssal default — selective disclosure bound by a count commitment — so the 3.03 combination claim survives this sweep with its scope tightened, in the falsifiable form 7.03 requires. **Witness-cosigned transparency logs** are established (CoSi, Syta et al. 2016; C2SP tlog-witness; Sigsum; the transparency.dev public witness network) and are the mechanism 4.03c of the protocol now points at rather than claims. **Scientific forecast sealing by published hash table** is practiced (the Axial Seamount Eruption Forecasting Experiment publishes SHA-256 digests of each sealed forecast document).

**KNM revision history, new entry:** "Rev. 3 companion note · 2026-07-29. Sweep seven executed against the prior-art boundary; results printed in 7.02. The combination claim of 3.03 stands, narrowed: the nearest commercial instance (Forecastr) anchors and binds but does not hold contents abyssal under a count commitment. RPAS 7.04's keyed/keyless claim was not touched by any finding of this sweep."

---

## THE FINDING, DRAFTED FOR PRINTING

*For the hashlog `disclosure` field, the public table's face, and the revision history. Print-don't-repair, in the 4.06 form.*

> **FINDING, 2026-07-29 (construction, revision 3).** The ten Kalls sealed 2026-07-25 and 2026-07-29 (KK-20260725-01 through -09, KK-20260729-01) were committed under construction `knp-1`, whose preimage excludes `probability` and `deadline`. For those records, the stated probabilities, deadlines, and every score computed from them are supported by the externally-anchored repository history of this file (KNP 4.03) — a dated, third-party-visible sequence of states — and not by the commitment hash. This is a disclosure of what the seal covers, not a defect in any seal: the statements and resolution bases of all ten are bound and remain so. The same defect class — displayed data outside the signed material — was independently identified in C2PA v2.2 by external formal-methods analysis (Cryptology ePrint 2026/804) in the same season this finding prints. Kalls sealed after this date bind both fields (KNP 2.01b). No sealed record is altered by this revision; the standard forbids retro-binding (4.01c, 4.02). The committer **may**, at his discretion, seal a `knp-2` attestation Kall binding the `(id, probability, deadline)` tuples of the ten prior rows — dated today, cross-referenced, and explicitly not substituting for the originals.

---

## OUT OF SCOPE, VERIFIED RATHER THAN ASSUMED

The RPAS ledger's per-row seal (`candidate_desk.py`) already binds probability and deadline — its payload is a sorted-JSON digest over statement, resolution, deadline, probability, failure condition, and the keyed/keyless declaration. The unbound-input defect is confined to the Kall construction. No RPAS amendment is required by this revision.

---

## APPLY SEQUENCE (single-line PowerShell, one per line, in order)

```
cd C:\netz
python kalls.py selftest
python kalls.py verify
copy KNP_REV3_AMENDMENTS.md .
```
Then replace `kalls.py` and `knp_verify.py` with the revision-3 implementations delivered with this document, and:
```
python kalls.py selftest
python knp_verify.py --selftest
python kalls.py verify
python knp_verify.py docs/kalls_hashlog.json
git add kalls.py knp_verify.py KNP_REV3_AMENDMENTS.md
git commit -m "KNP-26 rev3: bind probability and deadline (knp-2), construction history, metadata frozen across snapshots, anchor resolves structurally, standing line externally computable, conformance taxonomy stated"
git push
```
The first `verify` runs the ten under `knp-1` on the machine that holds the vault, **before** anything is replaced; the revision-3 `cmd_seal` additionally refuses to extend any log whose existing records fail verification, so the guard becomes standing rather than one-time. Spec-file edits to `KRAEHE_NEST_PROTOCOL.md` and `KRAEHE_NEST_METHOD.md` are the operator's paste from this document — the amendments are drop-in paragraphs by design. The first post-revision append is the moment 4.03c activates: run the openssl request line the new `beacon` prints, commit the `.tsr` beside the hashlog.
