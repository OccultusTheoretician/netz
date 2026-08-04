# RPAS-26 — AMENDMENT, 2026-08-04

**Amends the Retro-Prescient Audit Standards, First Edition 2026 v1, at 5.07, 6.04, 7.03, 7.04 and 7.06.**

Issued as a dated amendment, not an edit. The first edition is externally anchored (`RPAS_FIRST_EDITION_2026_v1.md.ots`); altering its bytes would drift the published digest from its receipt, which is the defect this desk found in its own anchoring on 2026-08-02 and fixed on 2026-08-03. **7.05** already governs: *these standards revise by dated edition, and revisions never alter the sealed record.* Entries remain scored under the edition in force at their sealing.

Nothing here relaxes a requirement. Every amendment below either concedes prior art the desk did not previously acknowledge, or reports a nonconformance in the desk's own record. That direction is not incidental — **6.04** binds the issuer publicly, and a standard whose issuer only ever reports outward is not a standard, it is marketing.

---

## PART I — NONCONFORMANCE IN THE DESK'S OWN RECORD (6.04, 5.07)

Five defects found in the desk's own instrument between 2026-08-02 and 2026-08-04. Each is reported here with the same ceremony the desk would use for a finding about anyone else. None is repaired retroactively: sealed rows are never edited, and the affected entries are marked, never removed.

### A · The declared priors had no unique referent (4.02f, 1.04)

The desk's daily report numbered its record items **per section, each section restarting at 1**. One report carried 111 numbered items across 25 distinct numbers; a citation such as `[4]` resolved to as many as twelve different stories. Every citation-support check the desk had ever run — including the gate shipped 2026-08-01 — silently resolved that ambiguity by taking whichever line came last in the file.

**Consequence under 1.04.** The keyed/keyless determination asks whether a hit was deducible from the declared priors. Where a citation does not identify a unique item, the priors are not weak — they are unaddressable, and the determination was made against nothing readable.

**Scope.** **286 sealed rows** carry at least one citation number that does not uniquely identify an item; the maximum number of candidate items behind a single citation is 8. Numbering is monotonic across the whole report from 2026-08-04 forward. Historical reports retain their numbering and their defect; they are dated artifacts and are not rewritten.

### B · The citation gate never ran on the manual arms (4.02f)

The ingest path resolved a row's `source_report` **three lines after** the validation gate ran. The citation-support check opens by returning pass when that field is empty — deliberately, since an unavailable report is not evidence of a bad citation — and on that path it was always empty. **Every entry that ever entered through manual ingest was ungated on citations.** The local-model path set the field before validating and was therefore checked; no other arm was.

**Consequence for published comparisons.** Any per-arm defect rate computed over entries sealed before 2026-08-04 compares one gated arm against arms that were never gated. It is not evidence that gating does or does not work. This limitation is printed in the by-arm table of every citation-integrity report the desk publishes.

### C · Measured citation defect rate, and its effect on the keyless count

Audited 2026-08-04 across 302 entries with a resolvable source report:

| finding | entries |
|---|---:|
| defective | **47 (15.6%)** |
| — no substantive overlap with the cited item | 35 |
| — no citations | 16 |
| — majority of cited items contributing nothing | 10 |
| — citing 8 or more items, or half the record | 7 |
| citation number not uniquely resolving | 286 |

**Of 36 entries determined KEYLESS, 8 (22.2%) rest on citations that do not support them.** The novelty claim at 7.04 is scoped to the keyed/keyless split alone. The desk therefore states the keyless count with its defect rate attached rather than as a clean integer, and will do so in every publication of that figure.

Thresholds are judgment calls and are printed in every report: rare-token cut at document frequency ≤ 25% of a report's items; shotgun at ≥ 8 cited items or ≥ 50% of the record; deadweight at > 50% of cited items contributing nothing with a minimum of 3 citations. Changing one changes the finding.

### D · Machine-drafted synthesis asserted identifiers its own record did not carry

Each category synthesis in the desk's report publishes under the printed claim that *every sentence cites the record below*. That claim was true at the sentence level and false at the identifier level. Audited across 45 reports with the elicitation packets supplied: **22 distinct identifiers appearing in synthesis prose and in neither the numbered record nor the packet the forecaster arm read.** Three were malformed and refer to nothing — `CVE-2026-6` (twice) and `CVE-2026-63`.

**Five sealed entries carry a flagged identifier.** One of them, `KKR-20260721-07`, carried `CVE-2026-6` as the operative term of its resolution basis. The vulnerability it described is real and is `CVE-2026-6875`; the identifier the entry depended on is not a valid identifier of any kind. That entry was resolved MISS on 2026-08-04 on its substance, with the defect recorded in its resolution note. A VOID would have been defensible on the ground that the entry could not be resolved on its own stated terms; MISS was taken because voiding on a malformed identifier would let an entry escape a miss it had earned.

An identifier is not a citation. A citation points at a numbered item and can be followed; an unsourced identifier points at nothing in the document and reads as *more* precise than the prose around it, which is why a reader checks it least. Identifier grounding is checked at generation from 2026-08-04 forward and flagged into the same audit channel that already flags uncited sentences.

### E · The elicitation input is not on the record (4.04, and a limitation on 1.04)

**206 sealed entries name a `source_packet` that is excluded from the desk's public repository** by ignore rule, across 10 distinct packets. Nineteen of those entries are determined keyless.

A stranger can recompute the seal, retrieve the report, read the entry, and check the outcome. **A stranger cannot retrieve the exact text the forecaster was shown.** Since the keyed/keyless determination turns on deducibility from the declared priors, and the priors' full text is unpublished, that determination is not independently checkable for those entries. The desk states this as a limitation on its own primary claim rather than leaving it to be discovered.

The same limitation applies to 65 war-desk chain files that constitute the evidence trail behind every cross-bias grading render.

Publishing hash commitments to the packets, rather than the packet bodies, would close the limitation without republishing the underlying feed content. That is the mechanism DECC-26 already specifies. It is named here as the remedy and is not yet implemented.

---

## PART II — PRIOR ART, PRINTED UNDER THE 7.04 COMMITMENT (amends 7.03)

7.04 commits the desk to printing prior art in 7.06 upon discovery. Two sweeps, 2026-08-02 and 2026-08-04. **Every claim swept came back occupied.** Added to the 7.03 acknowledgment list:

**Cryptographic commitment of an evaluation rubric.** arXiv 2607.00276 locks an evaluation specification under a version tag, writes the file's SHA-256 into its own header, and enforces recomputation by pre-commit hook and continuous integration, with separate locks per arm. bioRxiv 10.1101/213439 performs cryptographic pre-registration of a study protocol under SHA-256, self-timelocked and explicitly designed to require no third-party inspector. The desk concedes rubric commitment entirely. What was not located is any occupant that commits a rubric **and then refuses to report a trend across a rubric change**; that refusal, not the commitment, is the unheld part.

**Retrofit detection.** Occupied by a mature clinical-trial meta-research literature: a 1,746-trial cohort study finding 23% with a primary-outcome change between trial start and latest registry version (8% major); a German cohort finding 41% discrepancy between latest registry entry and publication; follow-up-publication outcome switching with 70% of prior deviators deviating again; Dwan et al., Cochrane MR000031 beneath all of it. The desk concedes detection. The surviving distinction is one inch wide and is stated as such: every one of those methods detects retrofit by trusting the registry's own version history, a log the registrar controls, whereas a hash chain with an external timestamp does not require trusting the registrar. **Claim the trust model, not the detection.**

**Unscored-remainder disclosure ("shadow mass").** arXiv 2106.11248 proves formally that a forecaster minimising mean Brier should forecast only questions outside a probability band set by their own score, and that under relative Brier the optimal move is submitting the community forecast rather than abstaining. IJF (2017) models question selection as signal rather than assuming missing-at-random. Both treat the unscored remainder as a scoring-model correction. **2106.11248 is cited here in support of the desk's disclosure requirement, not swept around: it is the formal proof that the disclosure is needed.**

**Identifier-level attribution failure.** arXiv 2607.09349, *Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation*, names and benchmarks the failure described in Part I·D: a response passing every automated check — zero hallucinations, near-perfect faithfulness, real and correctly formatted citations — while attributing evidence to the wrong entity, with rates of 8–87% across thirteen models at peak adversarial conditions. The desk's identifier-grounding finding is an instance of a documented failure class, not a discovery. Acknowledged.

**Publication of elicitation input as an audit artifact.** arXiv 2605.03762 constructs an information-boundary mechanism and states the governing question in nearly the desk's own words — *on what information did it base this judgment* — answered by a run record and information-boundary audit. arXiv 2605.11599 preserves prompts as reviewable audit artifacts under an audited prompt key with identifier-level rerun provenance. Publishing the elicitation input is not an unoccupied idea, and the desk does not claim it. The distinction the desk does maintain is narrow and stated: both occupants locate the input record inside the harness that produced it, and neither commits the input cryptographically before the outcome exists.

---

## PART III — 7.04, RESTATED WITH ITS LIMITATIONS ATTACHED

The novelty claim is unchanged in substance. **The keyed/keyless split as a mandatory, pre-registered, per-entry classification with segregated scoring** survived both sweeps; no implementation of it was located.

It is restated here with three limitations that were not attached to it at issuance and are now:

1. **The keyless figure carries a measured defect rate.** 8 of 36 keyless determinations rest on citations that do not support the claim. The figure is published with that rate attached.
2. **For 19 keyless entries the determination is not independently checkable**, because the elicitation input naming their declared priors is not on the public record.
3. **The classification was enforced unevenly.** Entries entering through manual ingest were never citation-gated before 2026-08-04, so the determinations behind them were made against priors nothing verified.

None of these falsifies the claim. All three weaken the desk's own instance of it, which is a different thing and is the thing 6.04 exists to make sayable.

---

## PART IV — 7.06, NEW ENTRIES

**— 2026-08-02.** Second and third adversarial sweeps. Three adjacent claims tested — cryptographic rubric commitment, retrofit detection, unscored-remainder disclosure. All three returned occupied; occupants named in Part II above and added to 7.03. No component of the desk survived as novel. The composition — a forecasting record treated as an audit engagement, governed by a published conformance standard, whose issuer reports its own nonconformance under the same rules — was not located in any occupant. Every occupant identified is a benchmark, a platform, or a product; none is an audit.

**— 2026-08-04.** Fourth sweep, run against two findings the desk had produced from auditing itself. Both returned occupied: identifier-level attribution failure (arXiv 2607.09349, published four weeks prior) and publication of elicitation input as an audit artifact (arXiv 2605.03762, 2605.11599). Neither is claimed. Recorded on the same day: five nonconformances in the desk's own record, printed in Part I above under 6.04 and 5.07, including a defect rate on the keyless figure that the 7.04 claim is scoped to.

**The sweep count now stands at four, and no sweep has yet returned a new claim.** That is printed rather than omitted. The desk's position is that a record which concedes accurately is believed when it does not concede, and the concession list is therefore the asset.

---

## PART V — WHAT THIS AMENDMENT DOES NOT DO

It does not rescore a resolved entry. It does not edit a sealed row. It does not alter the anchored first edition. It does not repair the 286 entries whose citations do not uniquely resolve, the 5 entries carrying a flagged identifier, or the 206 entries whose elicitation input is unpublished. Those are marked, not removed, per 5.07.

It records them where a stranger will find them without being told where to look.

---

*Issued under RPAS-26 §7.05. Supersedes no prior text. The first edition remains as anchored.*
