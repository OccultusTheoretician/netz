# THE SELECTIVE-DISCLOSURE COMMITMENT METHOD
## First Edition · 2026
**KNM-26 · Issued by the Retro-Prescient Audit Desk**
*Companion to the protocol specification KNP-26. This document formalizes the method; KNP-26 specifies the wire format an implementer builds to.*

**PROVENANCE: DRAFT** (Claude-drafted under direction, 2026-07-25, formalizing the commitment mechanism demonstrated the same day in the first sealed clutch of Krähe's Kalls. His only after rework pass. The novel-mechanism claim at 3.03 is the operator's; the prior-art boundary at Chapter 4 is stated conservatively and is his to verify before any ownership assertion is made in public.)

**MARK:** *Krähe's Nest* and *Krähe's Kalls* are coined marks pending; on naming, first use seals by the desk's standing three-clock mechanics and this header carries it. "KNM" is the citation prefix, not the mark.

---

## LETTER OF ISSUANCE

There is a standard problem in any scheme where a person commits to predictions and later reveals a record of them: the person who reveals the record is the person who benefits from the telling. Two known instruments each solve half of it and break the other half.

A **whole-set commitment** — hash the entire batch, reveal all or nothing — makes cherry-picking impossible, because the seal breaks if any entry is removed. But it also makes *selective disclosure* impossible: to prove one call, you must expose them all. The forecaster who wishes to hold most of his record dark cannot use it.

**Per-item commitments** — hash each prediction separately — restore selective disclosure: reveal one, keep the rest sealed. But they reintroduce cherry-picking, because the forecaster can seal fifty, reveal the six that hit, and stay silent about the forty-four that missed. Every revealed hash verifies perfectly and the record is a lie.

The method formalized here resolves the two against each other. It permits **per-item selective disclosure** — the committer reveals any subset he chooses, on his own clock, forever — while making cherry-picking **detectable**, because the *count* of sealed items is itself committed on an append-only public record. Contents stay dark; cardinality does not. A watcher sees how many were sealed and how many were revealed, so withholding is legible and the denominator cannot shrink. The committer holds every prediction abyssal and reveals only what he wishes, and the instrument still cannot be gamed, because the number of sealed-but-unrevealed items is public.

That is the whole method. It was demonstrated before it was formalized — in a sealed clutch of nine predictions committed to a public append-only log the same day this document was written, each hash published, each content held in a private vault, the count standing on the record. This standard is the delayed derivation of a mechanism already running. That is its genesis claim and the only one it makes.

What the demonstration establishes is bound as a requirement at 1.06: it establishes that the method is *implementable* and that its integrity properties *hold*. It establishes nothing about whether any predictions committed under it are good. The mechanism guarantees you cannot cheat the seal. It does not guarantee foresight. Those are different claims and this standard keeps them apart.

— The Retro-Prescient Audit Desk, 2026

---

## CHAPTER 1 — FOUNDATION

**1.01** This standard (KNM) defines the *selective-disclosure commitment method*: a scheme by which a committer seals predictive statements individually, reveals any subset at his sole discretion, and cannot cheat the record because the count of sealed items is committed on an append-only public log.

**1.02** The method is the intellectual substance. The protocol specification KNP-26 defines the concrete wire format — hash construction, log structure, reveal handshake, aggregator conformance — that an implementer builds. A conformant implementation follows KNP-26; a claim of *the method* refers to this document.

**1.03** Terms:
a. **Committer.** The party who seals predictions. Holds his own private vault; no other party holds his contents.
b. **Kall.** A single sealed predictive statement with its commitment.
c. **Vault.** The committer's private store: the plaintext statement, its resolution basis, and its salt, for each Kall. Never transmitted; never held by any other party.
d. **Commitment.** The public hash of a Kall (4.02). Reveals nothing about the content; binds the content against later edit.
e. **Hashlog.** The committer's append-only public record of commitments. Its length is the committed count.
f. **Reveal.** The committer's voluntary publication of one Kall's plaintext and salt, permitting any party to recompute and verify its commitment.
g. **Abyssal.** The default state of a sealed-but-unrevealed Kall: its existence and commitment are public; its content is not.
h. **Aggregator (the Nest).** A read-only surface that ingests published hashlogs from one or more committers and renders the collation. Holds no vaults, receives no submissions, and can alter no commitment.

**1.04** The two-property law. The method must simultaneously satisfy:
a. **Selective disclosure** — the committer may reveal any subset of his Kalls, in any order, at any time, and keep the remainder sealed indefinitely.
b. **Cherry-pick detectability** — the count of sealed Kalls is public and monotone, so the proportion revealed is always visible and the sealed population cannot be silently reduced.
A scheme satisfying only (a) is per-item commitment and is gameable. A scheme satisfying only (b) with all-or-nothing reveal is whole-set commitment and forbids the abyssal default. The method requires both.

**1.05** The trustlessness law. No party other than the committer holds his contents, and no central party is capable of altering a commitment. The aggregator reads public hashlogs; it does not receive predictions. A scheme in which a server receives, stores, or could edit predictions is **not** an implementation of this method, because it reintroduces the very party whose absence gives the seal its meaning (4.06).

**1.06** The validity clause (unconditional). Conformance certifies that the *commitment integrity* holds — that sealed contents are bound and the count is honest. It certifies nothing about the quality of the predictions committed. Demonstration establishes implementability and integrity, never foresight. No party may present conformance with this method as evidence that its committed predictions are good. The mechanism keeps the record honest; only the resolved, misfire-inclusive record itself can establish a forecaster.

---

## CHAPTER 2 — REQUIREMENTS FORMAT AND CONFORMANCE

**2.01** Requirements are of two categories:
a. **Must** — unconditional; complied with in all relevant cases.
b. **Should** — presumptively mandatory; departures documented with justification and the alternative that met the requirement's intent.

**2.02** An **unmodified conformance statement** ("implements the Selective-Disclosure Commitment Method") may be made only where all applicable *must* requirements are met.

**2.03** A **modified conformance statement** must name the requirements not followed and the effect on the integrity properties. A scheme that violates the trustlessness law (1.05) or the count-commitment law (3.02) may not claim conformance under any modifier; it is a different scheme.

**2.04** Citation is by paragraph ("KNM 3.03"). Citation is not endorsement of any citing party's record.

---

## CHAPTER 3 — THE MECHANISM

**3.01** Per-item commitment (must). Each Kall is committed by a salted cryptographic hash over its identifier, timestamp, statement, and resolution basis, plus a per-Kall secret salt, at the moment it is sealed, before any outcome exists. The canonical preimage and field order are normative in KNP 2.01 and are not restated here. The hash is published to the hashlog; the plaintext and salt are retained in the committer's vault. The salt provides the hiding property: without it, a low-entropy statement could be confirmed by brute-force guessing against the published hash.

> **CORRECTION — 2026-07-25, printed not silently substituted.** The first draft of 3.01 stated that probability and deadline are inside the commitment hash. They are not. The first clutch of nine Kalls, sealed 2026-07-25T18:30:00Z, used the five-field preimage `id|timestamp|statement|resolution_basis|salt` — exactly as KNP 2.01 specifies. KNM 3.01 was the erroneous paragraph and is amended here to match the commitment. **The spec is corrected to the seal; the seal is never adjusted to fit the spec.** Probability and deadline are therefore *anchored-not-hashed*: they are published in the hashlog record and their integrity rests on the append-only external anchoring of 3.02, not on the per-item hash. An implementer who hashes them produces commitments incompatible with the reference clutch.

**3.02** Count commitment (must). Commitments are recorded on an **append-only** hashlog whose length is the committed count. The append-only property must be enforced by a mechanism the committer does not solely control — a public version-control history, a third-party timestamping service, or an external beacon — so that the count is monotone and a silent reduction of the sealed population is detectable by any watcher. This is the requirement that makes cherry-picking detectable while preserving selective disclosure: the numerator (revealed) and denominator (sealed) are both public even when contents are not.

**3.03** The novel combination (the method's substance). The distinctive contribution is the *simultaneous* satisfaction of selective disclosure and cherry-pick detectability via count commitment over per-item seals. Neither property alone is novel; commitment schemes and prediction ledgers are long-established (Chapter 4). The combination — **per-item salted commitment for selective reveal, plus an externally-anchored append-only count commitment that binds the denominator without exposing contents** — is the mechanism this standard names. Its effect: a committer may hold his entire record abyssal and reveal only what he chooses, and still cannot cherry-pick, because the world can always see how much he is withholding.

**3.04** Selective reveal (must). Reveal is the committer's voluntary publication of one Kall's plaintext and salt. On reveal, any party recomputes the hash from the published plaintext-plus-salt and matches it against the sealed commitment; a match proves the Kall existed, unedited, at its sealed timestamp. Unrevealed Kalls remain abyssal indefinitely; there is no mechanism, and must be no mechanism, by which any party other than the committer can force or perform a reveal.

**3.05** Resolution and the keyed/keyless split (should, incorporated from RPAS). A revealed-and-resolved Kall is adjudicated against its stated basis. Where a Kall bears on a faculty claim, its hit is classified keyed (deducible from priors already held — arithmetic) or keyless (not so deducible — the only class that bears on foresight), per RPAS 1.04. The commitment method is agnostic to adjudication; a committer may run bare commitments with no faculty claim at all. But a committer who *asserts* foresight from his revealed record is bound by RPAS.

**3.06** The misses-stay-bound law (must). Contents may stay abyssal; existence may not be shed. Because the count is committed (3.02), a Kall cannot be removed from the sealed population after sealing. A committer who deletes or alters a sealed commitment breaks the append-only record, and the break is detectable against any prior-published state of the log. Deletion of a sealed Kall is the method's one integrity-fatal act.

---

## CHAPTER 4 — THE PRIOR-ART BOUNDARY

**4.01** This chapter states what the method does and does not claim as original, so that any ownership or novelty assertion rests on furnished ground. It is stated conservatively; the operator verifies each boundary before asserting novelty in public.

**4.02 Occupied — claim no originality.** Cryptographic commitment schemes (hash-then-reveal, salted commitments) are decades-old primitives. Merkle trees and append-only authenticated logs are established. Public prediction ledgers, calibration scoring (Brier 1950), and forecasting tournaments (Tetlock; Metaculus; Manifold) are prior art for the *ledger* and the *scoring*. Whole-set commitment as an anti-cherry-pick device is a known move. None of these is claimed here.

**4.03 The open, ownable vector.** What Chapter 4 leaves unoccupied — and what 3.03 names — is the *specific combination*: per-item salted commitment permitting selective disclosure, bound against cherry-picking by an externally-anchored count commitment, run as a **federated** protocol in which no central party holds contents. The count-commitment-preserves-selective-disclosure mechanism is the load-bearing novelty. The operator has not located this combination formalized elsewhere; that absence is a search result, not a proof, and is stated as such.

**4.04 What ownership is available (the honest boundary).** The method is a mathematical/analytical procedure and is therefore **not patentable** (subject-matter ineligibility; and the operator's prior public artifacts — the standing ledger and the Retro-Prescient Audit definition — have already begun a prior-art clock). No patent is sought and none is available. What *is* ownable: copyright in this specification and any reference implementation (automatic on authorship); the coined marks (Krähe's Nest, Krähe's Kalls) under the header's sealing mechanics; and authorship-of-standard — the durable value in an open protocol is being its named origin and reference implementation, as with any published protocol standard. Monetization follows the open-protocol pattern: the protocol is free; the convenience layer (a hosted aggregator others pay to avoid running themselves), consulting, and standard-authorship carry the value. This is stated so that no ownership claim is made that the law will not support.

**4.05 The mark-and-standard strategy.** First use of the marks seals by the desk's three-clock mechanics (public commit, external beacon, dated archive) exactly as the sibling standards seal. The standard is citable by paragraph and is issued under the desk's name, establishing authorship-of-record without asserting any legal monopoly the subject matter cannot bear.

**4.06 Why no server (the design law, not a limitation).** The trustlessness law (1.05) forbids a central party that receives or could alter predictions — not for want of capability but because such a party is the exact entity whose absence gives the commitment its meaning. A hosted submission backend would reintroduce "did the operator peek, edit, or cherry-pick," now asked by *other people* of the operator. The federated design (committers hold their own vaults and publish their own hashlogs; the Nest only reads) is what keeps the method trustless at scale. It is a feature of the method, bound as a requirement, not an implementation shortcut.

---

## CHAPTER 5 — CONTENT AND CLAIM DISCIPLINE (for federated adoption)

**5.01** The aggregator is a reader, not a publisher (must). The Nest ingests published hashlogs and renders the collation. It does not vouch for, endorse, or assert the truth of any committer's revealed content. Its conformance statement says so on its face.

**5.02** Sealed contents are opaque and carry no content risk (they are hashes). **Revealed** contents are the committer's published text and are the committer's responsibility. A federated aggregator that renders others' revealed Kalls must (a) attribute each to its source hashlog, (b) state that it is an aggregator of commitments and not a publisher vouching for content, and (c) carry a revealed-content policy for material that is unlawful or that targets a private individual. This is the scale version of the desk's standing firewall: the instrument may host commitments to anything (opaque), but a surface rendering revealed claims about named living persons inherits the responsibility for those claims.

**5.03** No faculty claim by aggregation (must). The Nest may display counts, reveal rates, and — for committers past a stated resolution floor — calibration. It may not rank committers as "prescient" or present aggregate display as evidence of any committer's foresight. Under thirty resolved, a committer's score is noise and the Nest says so on the committer's own row, per RPAS and 1.06.

**5.04** The committer owns the gate (must). Reveal, resolution, and any public claim from a record are the committer's acts alone. No aggregator, and no other committer, may reveal, resolve, or characterize another's record.

---

*End of KNM-26. The wire format an implementer builds is specified in KNP-26. This document is the method; that document is the protocol.*
