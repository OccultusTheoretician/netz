# THE SELECTIVE-DISCLOSURE COMMITMENT METHOD
## First Edition · 2026 · Revision 3
**KNM-26 · Issued by the Retro-Prescient Audit™ Desk**
*Companion to the protocol specification KNP-26. This document formalizes the method; KNP-26 specifies the wire format an implementer builds to.*

**PROVENANCE: DRAFT** (Claude-drafted under direction, revision 2 of 2026-07-25. His only after rework pass. The novel-combination claim at 3.03 and the prior-art boundary at Chapter 7 are stated conservatively and are his to verify before any ownership assertion is made in public. Every professional-standards citation in this document is named at concept level and requires paragraph-level verification against the current authoritative text before it is printed as a citation.)

**MARK:** *Krähe's Nest™* and *Krähe's Kalls™* are coined marks pending; first use seals by the desk's standing three-clock mechanics and this header carries it. "KNM" is the citation prefix, not the mark.

**WHAT CHANGED IN REVISION 2.** Three substantive additions and one correction. Added: a two-level conformance structure separating discretionary reveal from scheduled reveal (Chapter 5); a custody and key-management chapter, absent from revision 1 and the method's largest unaddressed control weakness (Chapter 4); and an independence chapter stating the discretions that survive the mechanism, as a disclosed scope limitation rather than an implied absence (Chapter 6). Corrected: revision 1's paragraph 3.01 described a commitment over statement, resolution basis, probability, and deadline, while KNP-26 revision 1 specified a preimage excluding probability and deadline. The two documents contradicted each other and the reference clutch could not have satisfied both. The construction actually used by the demonstration clutch governs; 3.01 and KNP 2.01 are reconciled to it, and the discrepancy is printed in the revision history rather than silently repaired.

---

## LETTER OF ISSUANCE

There is a standard problem in any scheme where a person commits to predictions and later reveals a record of them: the person who reveals the record is the person who benefits from the telling.

Two known instruments each solve half of it and break the other half. A **whole-set commitment** — hash the entire batch, reveal all or nothing — makes cherry-picking impossible, because the seal breaks if any entry is removed; but it forbids selective disclosure, so a committer who wishes to hold most of his record dark cannot use it. **Per-item commitments** restore selective disclosure and reintroduce cherry-picking, because the committer can seal fifty, reveal the six that hit, and stay silent about the forty-four that missed. Every revealed hash verifies perfectly and the record is a lie.

The method formalized here resolves the two against each other. It permits per-item selective disclosure while making cherry-picking detectable, because the *count* of sealed items is itself committed on an append-only external record. Contents stay dark; cardinality does not.

Stated in the register a practitioner will recognize: **selective disclosure is a completeness problem.** A revealed subset chosen by the party being examined is a management-selected sample, and a management-selected sample is not evidence of anything about the population it came from. The count commitment is a completeness control over the population of forecasts — it fixes the denominator without exposing the numerator's contents. Every other control in this standard is subordinate to that one.

What revision 1 did not say, and this revision does: the mechanism does not make the committer independent. In the demonstration deployment the committer is also the custodian, the revealer, and the adjudicator. No cryptography changes that. What the mechanism can do is *narrow* discretion until only nameable amounts remain — the count commitment removes population choice; a pre-registered resolution basis naming an external source removes adjudication choice; scheduled reveal removes reveal choice — and what survives is then disclosed on the record's own face as a scope limitation. A record stating plainly which discretions remain is stronger than one implying it has none. That is what a professional standard does with an impairment it cannot eliminate, and it is what this one does.

The method was demonstrated before it was formalized, in a clutch of nine predictions sealed to a public append-only log the same day revision 1 was written. That demonstration establishes that the method is implementable and that its integrity properties hold. It establishes nothing about whether the predictions are good. The mechanism guarantees you cannot cheat the seal; it does not guarantee foresight. Those are different claims and this standard keeps them apart.

— The Retro-Prescient Audit Desk, 2026

---

## CHAPTER 1 — FOUNDATION

**1.01** This standard defines the *selective-disclosure commitment method*: a scheme by which a committer seals predictive statements individually, reveals a subset under a declared reveal regime, and cannot cheat the record because the count of sealed items is committed on an externally-anchored append-only log.

**1.02** The method is the intellectual substance. KNP-26 defines the concrete wire format — hash construction, log structure, custody artifacts, reveal handshake, aggregator conformance. A conformant implementation follows KNP-26; a claim of *the method* refers to this document.

**1.03** Terms.
a. **Committer.** The party who seals predictions and holds the opening material.
b. **Kall.** A single sealed predictive statement with its commitment.
c. **Opening material.** Everything required to reproduce a commitment: the statement, its resolution basis, any bound metadata, and the salt. Formerly "vault contents"; renamed because custody, not storage, is the control (Chapter 4).
d. **Commitment.** The public hash of a Kall. Reveals nothing about the content; binds the content against later edit.
e. **Hashlog.** The committer's append-only public record of commitments. Its length is the committed count.
f. **Reveal.** Publication of one Kall's opening material, permitting any party to recompute and verify.
g. **Abyssal.** The default state of a sealed-but-unrevealed Kall: existence and commitment public, content not.
h. **Aggregator (the Nest).** A read-only surface that ingests published hashlogs and renders the collation. Holds no opening material, receives no submissions, can alter no commitment.
i. **Reveal regime.** The declared rule by which a committer's Kalls open: discretionary or scheduled (Chapter 5).

**1.04 The two-property law.** The method must simultaneously satisfy:
a. **Selective disclosure** — the committer may hold any subset sealed indefinitely.
b. **Cherry-pick detectability** — the count of sealed Kalls is public and monotone, so the proportion revealed is always visible and the sealed population cannot be silently reduced.
A scheme satisfying only (a) is per-item commitment and is gameable. A scheme satisfying only (b) with all-or-nothing reveal is whole-set commitment and forbids the abyssal default. The method requires both.

**1.05 The trustlessness law.** No party other than the committer holds his opening material in usable form, and no central party is capable of altering a commitment. The aggregator reads public hashlogs; it does not receive predictions. A scheme in which a server receives, stores, or could edit predictions is **not** an implementation of this method, because it reintroduces the very party whose absence gives the seal its meaning (7.06). Threshold custody under Chapter 4 does not violate this law: a share below the reconstruction threshold conveys no information about the secret, so a shareholder is not a party holding the material.

**1.06 The assertion mapping.** The method's controls address these assertions, in the sense the term carries in professional risk-assessment literature (AICPA AU-C 315 and its GAGAS overlay; verify paragraph references before citation):
a. **Completeness** — the sealed population is whole and monotone. Addressed by the count commitment (3.02). This is the method's central assertion and its reason to exist.
b. **Existence and occurrence** — the commitment proves the Kall existed at its sealed timestamp. Addressed by the external anchor (3.02) and the hash itself.
c. **Accuracy** — the revealed content is exactly what was sealed. Addressed by binding (3.05).
d. **Cutoff** — the seal precedes the outcome. Addressed by the external anchor's dated third-party record; a self-hosted timestamp does not satisfy it.

**1.07 The validity clause (unconditional).** Conformance certifies that commitment integrity holds — that sealed contents are bound and the count is honest. It certifies nothing about the quality of the predictions committed. No party may present conformance as evidence that its predictions are good. The mechanism keeps the record honest; only the resolved, misfire-inclusive record itself can establish a forecaster.

---

## CHAPTER 2 — REQUIREMENTS FORMAT AND CONFORMANCE

**2.01** Requirements are of two categories: **must** (unconditional) and **should** (presumptively mandatory; departures documented with justification and the alternative that met the requirement's intent).

**2.02** An **unmodified conformance statement** may be made only where all applicable *must* requirements are met, and must name the conformance level (Chapter 5) and the vault architecture (Chapter 4) in the same sentence. "Implements the Selective-Disclosure Commitment Method" without those two facts is incomplete and non-conformant, because the two materially change what the record supports.

**2.03** A **modified conformance statement** must name the requirements not followed and the effect on the integrity properties.

**2.04** A scheme violating the trustlessness law (1.05) or the count-commitment law (3.02) may not claim conformance under any modifier. It is a different scheme.

**2.05** Citation is by paragraph ("KNM 3.03"). Citation is not endorsement of any citing party's record.

---

## CHAPTER 3 — THE MECHANISM

**3.01 Per-item commitment (must).** Each Kall is committed by a salted cryptographic hash over a canonical preimage, at the moment it is sealed, before any outcome exists. The exact field set and ordering are normative in KNP 2.01 and are not restated here; revision 1 restated them and the two documents diverged. **The fields inside the preimage are bound; fields published outside it are not.** A committer publishing probability or deadline outside the preimage must disclose that those values are anchored by the external record only, and are not protected by the hash. The salt provides the hiding property: without it, a low-entropy statement could be confirmed by brute-force guessing against the published hash. "KNP-26 revision 3 defines a successor construction binding probability and deadline for Kalls sealed thereafter, restoring this standard's revision-1 intent going forward; records sealed under the earlier construction remain governed by their published commitments and by the disclosure duty of this paragraph."

**3.02 Count commitment (must).** Commitments are recorded on an append-only hashlog whose length is the committed count. The append-only property must be enforced by a mechanism the committer does not solely control — a public version-control history, a third-party timestamping service, or an external beacon. This is the requirement that makes cherry-picking detectable while preserving selective disclosure: numerator and denominator are both public even when contents are not. A hash chain computed by the committer over his own log does **not** satisfy this paragraph; a chain the committer can recompute end to end is not evidence against the committer, and is only load-bearing to the extent its head is externally anchored.

**3.03 The novel combination (the method's substance).** The distinctive contribution is the *simultaneous* satisfaction of selective disclosure and cherry-pick detectability via count commitment over per-item seals. Neither property alone is novel; commitment schemes, threshold secret sharing, timelock encryption, and prediction ledgers are all long-established (Chapter 7). The combination — per-item salted commitment for selective reveal, plus an externally-anchored append-only count commitment that binds the denominator without exposing contents — is the mechanism this standard names.

**3.04 Selective reveal (must).** Reveal is the publication of one Kall's opening material under the committer's declared reveal regime (Chapter 5). On reveal, any party recomputes the hash and matches it against the sealed commitment; a match proves the Kall existed, unedited, at its sealed timestamp. There must be no mechanism by which any party other than the committer, or the committer's declared schedule, can force a reveal.

**3.05 Binding.** Collision resistance of the hash function provides binding: the committer cannot find different content producing the same commitment. Binding is unaffected by loss or theft of opening material. This matters for control design: theft is a confidentiality failure and loss is an availability failure, but neither is an integrity failure, and controls should be sized accordingly (4.01).

**3.06 Resolution and the keyed/keyless split (should, incorporated from RPAS).** A revealed-and-resolved Kall is adjudicated against its stated basis. Where a Kall bears on a faculty claim, its hit is classified keyed (deducible from priors already held) or keyless (not so deducible; the only class bearing on foresight), per RPAS 1.04. A committer may run bare commitments with no faculty claim at all. A committer who *asserts* foresight from his revealed record is bound by RPAS.

**3.07 The misses-stay-bound law (must).** Contents may stay abyssal; existence may not be shed. A committer who deletes or alters a sealed commitment breaks the append-only record, and the break is detectable against any prior-published state. Deletion of a sealed Kall is the method's one integrity-fatal act. This is the method's management-override control, and management override is the pervasive risk in any self-maintained record (AU-C 240, concept-level).

---

## CHAPTER 4 — CUSTODY AND KEY MANAGEMENT

*Absent from revision 1. The largest control weakness in the demonstration deployment was not the cryptography but the custody of the opening material: a single file, in a single location, under a single person, protecting Kalls with horizons up to ten years.*

**4.01 The custody problem, correctly framed (must be understood before the controls read).** Three properties come apart. **Binding** is guaranteed by the hash and survives both loss and theft. **Confidentiality** until reveal is threatened by theft. **Availability of the opening** is threatened by loss. Only the last two trade against each other. Loss is the severe one, because it is unrecoverable: a Kall whose salt is gone can be proven to have been made and can never be opened. Controls that reduce copies to protect confidentiality therefore increase the probability of the more severe failure, and are misdesigned.

**4.02 Vault architectures (must declare one).**
a. **Architecture A — private opening material.** The opening material is held privately by the committer and is never published until reveal. Simplest; the availability risk sits entirely on the committer's backup discipline.
b. **Architecture B — published ciphertext.** The opening material is encrypted under a per-Kall key and the ciphertext is published alongside the commitment. The ciphertext leaks nothing, so it may be replicated without limit — every copy of the public log is a backup. Reveal is publication of the key rather than the text. Custody collapses from *n* secrets to one master key, with per-Kall keys derived from it so that revealing one does not open the rest.
Architecture B is the **higher-assurance option** and is *should* for any committer holding Kalls with a horizon exceeding three years, because it removes the unrecoverable-loss failure mode entirely. Architecture A remains conformant. The declared architecture is published (2.02).

**4.03 Key custody (must).** The committer must document, and be able to demonstrate, where the key material lives, in how many locations, and under what protection. A key in one location is not a control. Minimum: **three independent locations, at least one offline and one geographically separate.**

**4.04 Split knowledge and dual control (should; must where any Kall's horizon exceeds five years).** Key material should be divided by threshold secret sharing — Shamir's scheme, *k*-of-*n* — such that no single holder can reconstruct and no single loss is fatal. A share below the reconstruction threshold conveys no information about the secret, which is why shareholders are not trusted parties under 1.05. This is the split-knowledge and dual-control pattern established in key-management practice (NIST SP 800-57 and the payment-card lineage; verify paragraph references before citation). The horizon trigger is not arbitrary: a single custodian is a single point of failure against his own unavailability, and any commitment outliving that risk window is uncontrolled without threshold custody.

**4.05 The recovery drill (must).** A recovery path that has never been executed is not a control. The committer must, at least annually and after any change to custody arrangements, reconstruct the key from backup or from threshold shares, open one sealed Kall, verify the commitment reproduces, and **record the date of the drill on the public log**. An untested recovery path must be disclosed as such.

**4.06 Custody failure disclosure (must).** Where opening material is lost, the affected Kalls are marked permanently unopenable on the hashlog and remain in the count. They are not removed, and the loss is stated. An unopenable Kall is a scope limitation on the record, not an absence from it.

**4.07 Separation of custody from adjudication (should).** Where practicable, the party holding key material at reveal should not be the party ruling on resolution. In a one-person deployment this is not practicable, and the impairment is disclosed under Chapter 6 rather than pretended away.

---

## CHAPTER 5 — REVEAL REGIMES AND CONFORMANCE LEVELS

*The single decision that most changes what a record can support is who decides when a Kall opens. Revision 1 permitted only the committer. This revision defines two levels and requires the level to be declared.*

**5.01 Level 1 — Discretionary Reveal.** The committer reveals any subset, in any order, at any time, and may hold the remainder sealed permanently. Integrity rests entirely on the count commitment: the record cannot be cherry-picked *undetectably*, because the withheld proportion is public, but the revealed sample remains committer-selected. A Level 1 record supports statements about the committer's *published* calls and about how much he is withholding. It does not support a calibration claim over his forecasting generally, and a Level 1 committer must not present one.

**5.02 Level 2 — Scheduled Reveal.** Each Kall carries, at sealing, a reveal date at which its opening material becomes available irrespective of the committer's wishes — by publication of a key held in escrow-free form (timelock encryption to a public beacon), or by an equivalent mechanism the committer cannot suppress. Reveal discretion is removed mechanically. A Level 2 record over a completed period supports calibration claims about that period, because the revealed set is the whole set.

**5.03 Period-anchored operation (the professional lane).** Level 2's natural configuration in an assurance context sets reveal dates to a reporting cycle: forecasts sealed at the close of one period open at the close of the next, and the resulting comparison of sealed forecast to realized outcome is a **variance analysis over a pre-committed baseline.** The distinguishing property against ordinary forecast-to-actual reporting is that the baseline could not have been revised after the fact — the failure that makes most published variance analysis unfalsifiable. Forecast-versus-actual comparison is already mandated in some reporting regimes without any commitment mechanism wiring the forecast to a tamper-evident record; this paragraph is that wiring.

**5.04 Mixed operation (should).** A committer may run both levels concurrently provided each Kall's level is declared at sealing and displayed on the hashlog, and provided scores are segregated. Level 1 and Level 2 Kalls must never be scored in a single pooled figure, because the selection properties differ and pooling launders the weaker into the stronger.

**5.05 Beacon dependence, disclosed (must).** Level 2 by timelock introduces a dependence on an external beacon network. That is a third party, distributed but real, and its failure or discontinuation is a risk to the reveal schedule. A Level 2 committer must name the beacon and state a fallback: at minimum, the committer's own retained key material, which restores Level 1 properties if the beacon fails and must be disclosed as doing so.

**5.06 Declaration (must).** The conformance level is published on the hashlog's face and cannot be changed retroactively for a sealed Kall.

---

## CHAPTER 6 — INDEPENDENCE, DISCRETION, AND THE SCOPE LIMITATION

*The chapter revision 1 lacked, and the reason a practitioner would have dismissed it.*

**6.01 The impairment, stated (must).** In a single-operator deployment the committer is also the custodian, the revealer, and the adjudicator. This is a self-audit. No mechanism in this standard makes it independent, and no conformance statement may imply otherwise.

**6.02 What the mechanism does instead.** It narrows discretion to a nameable list. The count commitment removes discretion over the population. A resolution basis pre-registered at sealing and naming an external source removes discretion over adjudication, to the extent the source is genuinely external and genuinely determinate. Scheduled reveal (5.02) removes discretion over disclosure. Each control converts an unbounded judgment into a bounded one.

**6.03 The residual-discretion statement (must).** Every conformant record publishes, in its own words, the discretions that survive its configuration. A Level 1, Architecture A, single-custodian deployment publishes at minimum: that reveal is at the committer's sole discretion; that resolution is adjudicated by the committer; that the committer holds sole custody of opening material; and that no independent party has examined either the population or any resolution. That statement is not a weakness printed against the record — it is the record's most credible sentence, because it is the one an adversary would otherwise write for it.

**6.04 Blind adjudication where practicable (should).** Where a Kall's resolution basis admits it, resolution should be performed by a party who sees neither the committer's identity nor the stated probability, must cite evidence, and may return ambiguous. Where the committer adjudicates his own entries, the resolution basis must be mechanical — adjudicable by any third party from public inputs without judgment calls (RPAS 3.01). Where not practicable, 6.03 governs.

**6.05 The sufficiency floor (must).** Under thirty resolved Kalls, no calibration figure is presented as evidence of skill, and the record states this on its own face. This is a sufficiency-of-evidence requirement, not a modesty convention: below that count the sampling error exceeds the effect being claimed.

**6.06 No self-certification of foresight (must).** A committer may certify conformance with this method. A committer may not certify his own foresight, at any level, under any architecture. Conformance is about the instrument; foresight is a claim about the world that only a resolved, misfire-inclusive record examined by someone else can support.

---

## CHAPTER 7 — THE PRIOR-ART BOUNDARY

**7.01** This chapter states what the method does and does not claim as original, so that any ownership or novelty assertion rests on furnished ground. It is stated conservatively; the operator verifies each boundary before asserting novelty in public.

**7.02 Occupied — claim no originality.** Cryptographic commitment schemes (hash-then-reveal, salted commitments) are decades-old primitives. Merkle trees and append-only authenticated logs are established, as are transparency-log designs built on them. **Shamir's threshold secret sharing (1979) is established**, as are split-knowledge and dual-control key custody practices. **Timelock encryption, verifiable delay functions, and public randomness beacons are established** and are not this standard's invention; Chapter 5's contribution is the governance framing, not the primitive. **Publishing ciphertext and revealing the key later is standard commitment practice**, not a novelty of Architecture B. Public prediction ledgers, calibration scoring, and forecasting tournaments are prior art for the ledger and the scoring. Whole-set commitment as an anti-cherry-pick device is a known move. None of these is claimed here.

Productized prediction pre-commitment is established: **Forecastr** (forecastr.dev, operating since April 2026) binds input, model, and output into a hash chain sealed by RFC 3161 timestamp and on-chain anchor before outcomes exist, marketed as the cryptographic evidence layer for EU AI Act Annex IV obligations. Per-item commitment with external anchoring, productized for regulatory evidence, is therefore occupied. Forecastr implements full-transparency logging of every prediction; it does not implement the abyssal default — selective disclosure bound by a count commitment — so the 3.03 combination claim survives this sweep with its scope tightened, in the falsifiable form 7.03 requires. **Witness-cosigned transparency logs** are established (CoSi, Syta et al. 2016; C2SP tlog-witness; Sigsum; the transparency.dev public witness network) and are the mechanism 4.03c of the protocol now points at rather than claims. **Scientific forecast sealing by published hash table** is practiced (the Axial Seamount Eruption Forecasting Experiment publishes SHA-256 digests of each sealed forecast document).

On-chain forecasting benchmarks are established: Foresight Arena (arXiv 2605.00420) binds AI agents' full probability vectors under salted commit-reveal before outcomes exist, scored against market resolution — per-item probability binding, productized for benchmarking; it reveals all commitments and implements no abyssal default, so the 3.03 combination claim survives sweep eight with its scope unchanged from sweep seven. Resolution infrastructure is established at industrial scale: optimistic oracles with bonded propose–dispute cycles (UMA/Polymarket), outcome review committees (Kalshi), and automated feed resolution; this method's contribution to adjudication is the evidentiary wrapper only — dated, hashed evidence snapshots under propose-never-resolve — not the function. Propagation-prediction methods are established (community-structure predictors, meme-burst models, cross-platform narrative-emergence research); the committed, misfire-scored public record of such calls is not, and is claimed at 7.03.

**7.03 The open, ownable vector.** What remains unoccupied — and what 3.03 names — is the specific combination: per-item salted commitment permitting selective disclosure, bound against cherry-picking by an externally-anchored count commitment, run as a federated protocol in which no central party holds contents. The count-commitment-preserves-selective-disclosure mechanism is the load-bearing novelty. The operator has not located this combination formalized elsewhere; that absence is a search result, not a proof, and is stated as such.

**Conformant-as-disclosed (claimed at sweep eight, 2026-07-30).** No located conformance test suite mechanizes qualified-opinion logic: a verifier that downgrades a defect from failure to note when, and only when, the audited artifact's own machine-readable disclosure prints that defect on its face. Nearest prior art, named: the qualified audit opinion — human judgment, which RPAS 2.03 deliberately mirrors — and modified conformance statements in standards practice. Deployed in rpas_verify.py; falsified by a named suite carrying the mechanical disclosure-reading loop. The full claim trajectory, including reversals, is kept in SWEEP_REGISTER.md at the repository root.

**7.04 What ownership is available (the honest boundary).** The method is a mathematical and analytical procedure and is therefore **not patentable**, and the operator's prior public artifacts have already begun a prior-art clock. No patent is sought and none is available. What *is* ownable: copyright in this specification and in any reference implementation; the coined marks under the header's sealing mechanics; and authorship-of-standard. Monetization follows the open-protocol pattern — the protocol is free; the convenience layer, consulting, and standard-authorship carry the value.

**7.05 The mark-and-standard strategy.** First use of the marks seals by the desk's three-clock mechanics exactly as the sibling standards seal. The standard is citable by paragraph and issued under the desk's name, establishing authorship-of-record without asserting a legal monopoly the subject matter cannot bear.

**7.06 Why no server (the design law, not a limitation).** The trustlessness law forbids a central party that receives or could alter predictions — not for want of capability but because such a party is the exact entity whose absence gives the commitment its meaning. A hosted submission backend would reintroduce "did the operator peek, edit, or cherry-pick," now asked by other people of the operator. The federated design is what keeps the method trustless at scale.

---

## CHAPTER 8 — CONTENT AND CLAIM DISCIPLINE (FEDERATED ADOPTION)

**8.01** The aggregator is a reader, not a publisher (must). It does not vouch for, endorse, or assert the truth of any committer's revealed content, and says so on its face.

**8.02** Sealed contents are opaque and carry no content risk. **Revealed** contents are the committer's published text and are the committer's responsibility. An aggregator rendering others' revealed Kalls must attribute each to its source hashlog, state that it is an aggregator of commitments and not a publisher vouching for content, and carry a revealed-content policy for material that is unlawful or that targets a private individual.

**8.03** No faculty claim by aggregation (must). The Nest may display counts, reveal rates, declared level and architecture, and — for committers past the sufficiency floor — calibration. It may not rank committers as prescient. Level 1 and Level 2 records are displayed as distinct classes and are never pooled (5.04).

**8.04** The committer owns the gate (must). Reveal, resolution, and any public claim from a record are the committer's acts alone. No aggregator and no other committer may reveal, resolve, or characterize another's record.

---

## APPENDIX A — DEMONSTRATION ENGAGEMENT (implementability evidence only; 1.07 governs)

**A.01** Nine Kalls, sealed 2026-07-25, published to an append-only log with commitments, probabilities, deadlines, and statuses public and contents held privately. Configuration as sealed: **Level 1 (discretionary reveal), Architecture A (private opening material), single custodian.** Horizons range from 2026 to 2036.

**A.02 Findings against this standard, printed rather than repaired.** The demonstration is non-conformant with revision 2 in three respects, each of which drove a requirement above. Custody was single-location and single-custodian against a ten-year horizon (4.03, 4.04). No recovery drill had been executed at the time of sealing (4.05). No residual-discretion statement was published with the clutch (6.03). The clutch remains valid as a commitment — binding is unaffected — and the gaps are control weaknesses in the deployment, not defects in the seals.

**A.03** The demonstration establishes implementability and integrity. It establishes nothing about the quality of the nine predictions, none of which had resolved at issuance.

---

## REVISION HISTORY

**Sweep-eight note · 2026-07-30 UTC.** Foresight Arena and industrial resolution infrastructure entered 7.02; two of the desk's own framings narrowed or died and are recorded, with every reversal since sweep one, in SWEEP_REGISTER.md. Conformant-as-disclosed and the committed propagation record entered 7.03 as open claims.

**Rev. 3 companion note · 2026-07-29.** Sweep seven executed against the prior-art boundary; results printed in 7.02. The combination claim of 3.03 stands, narrowed: the nearest commercial instance (Forecastr) anchors and binds but does not hold contents abyssal under a count commitment. RPAS 7.04's keyed/keyless claim was not touched by any finding of this sweep.

**Rev. 2 · 2026-07-25.** Added Chapters 4 (custody), 5 (reveal regimes and levels), and 6 (independence and residual discretion). Reframed the method's central property as a completeness assertion (1.06). Corrected the revision-1 contradiction between KNM 3.01 and KNP 2.01 over which fields enter the preimage: the two documents specified different constructions, and the demonstration clutch could not have satisfied both. The construction used by the clutch governs; 3.01 no longer restates the field set, which is normative in KNP alone, and adds the requirement that unbound published metadata be disclosed as unbound. Added to the prior-art boundary the primitives revision 2 relies on and does not claim: Shamir threshold sharing, timelock encryption and randomness beacons, and commitment-with-published-ciphertext (7.02). Stated the chain-is-not-an-anchor finding at 3.02.

**Rev. 1 · 2026-07-25.** First formalization, drafted the day the demonstration clutch was sealed.

---

*End of KNM-26 rev. 2. The wire format an implementer builds is specified in KNP-26. This document is the method; that document is the protocol.*
