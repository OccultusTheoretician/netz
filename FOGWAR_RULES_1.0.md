# FOGWAR - RULES 1.0 (P1: the engine)
**rules_version `fogwar/1.0` - 2026-09-04 - DRAFT until the operator's rework. The engine is `fogwar.py`; its twin is `fogwar_core.js`; the differential test is `test_fogwar_parity.py`.**

## 0. What this is, in the desk's own terms
A wargame you can audit. A game is a pure function of four things - the scenario's bytes, the rules version, the seed, and blue's move log - so anyone re-executes it and obtains the same final state hash, byte for byte, in Python or in the browser. Red's dispositions, the fog, are committed before blue's first move and opened in the receipt at the end. The commitment binds the RECORD: a published receipt lets a third party check that the fog held what the game says it held and that no disposition moved behind it. It does not hide anything from a player who reads their own browser's memory, and no page will claim that it does.

The combat model is a socket, lifted from fogsim: stochastic Lanchester square-law attrition with seeded per-tick shocks. It is not a claim about war. What is claimed is the machinery - determinism, commitment, receipt, re-execution - and the machinery is what the tests prove.

## 1. Map
An abstract region graph. Each region has an id, a name, an adjacency list, a defense multiplier (1.0 or more) and a value. No real theatre is represented; the default scenario is TWO CAPITALS: ten regions, two capitals, a contested centre. The scenario's identity is the SHA-256 of its file bytes (LF-normalised, BOM ignored), so an edited scenario is a different scenario.

## 2. Sides and forces
Blue is the player. Red is a rule AI. Each side has a capital and starting strengths in integer points on named regions. All strengths are integers throughout; there is no fractional force anywhere in the game.

## 3. Turn
Blue issues up to `max_orders` orders, then red does. Three order types:
- `hold` - nothing.
- `move(from, to, n)` - move n points from an own region to an adjacent region, leaving at least 1 behind. Into an own or empty region this reinforces or occupies; into an enemy region it attacks.
- `scout(target)` - reveal the strength of a region adjacent to one you own, for `scout_reveals_turns` turns.
Illegal orders are rejected with a stated reason and take no effect; the rejection is logged outside the game record so it cannot alter the game id. Legal orders are recorded exactly as accepted.

## 4. Resolution, in this order
1. Scouts take effect.
2. Movements leave their origins; arrivals pool by destination and side, origin order kept.
3. Each destination resolves in id order. One side arriving into its own or empty ground reinforces or occupies. Where both sides stand, combat: the occupant defends; on empty ground the larger arriving force defends and ties defend red. The defender's force is what stands there plus its own arrivals. Combat runs `combat_ticks` ticks of Lanchester attrition with shocks drawn from the game's seed; the defender's effectiveness is multiplied by the region's defense. Losses each tick are the floor of a double product evaluated in one fixed order. Whoever falls to `break_fraction` of their starting force breaks. Attacker breaks the defender: the attacker takes the region with what it has left. Defender holds or nothing is decided within the ticks: the attacker withdraws its remainder to the first contributing origin. Both break: the ground stays with whatever the defender has left, or empties.
4. Reinforcements: each side receives floor(controlled value x `reinforce_rate`) points at its capital, or at its strongest region if the capital is lost.
5. End: a side holding no region is eliminated and loses. After `turns` turns the side controlling more value wins; equal value is a draw.

## 5. Fog
A side sees the owner and strength of its own regions; the owner of any region adjacent to one it owns; the strength of an adjacent region only if it scouted it this turn or fought there this turn. Everything else is fog. Red sees under the same rule; the AI is not omniscient.

## 6. The rule AI (red)
A fixed policy over regions in id order, with no randomness of its own: scout the highest-value adjacent enemy region whose strength it does not know; attack where its own force less one is at least 1.5 times its estimate of the target (unknown strengths are estimated as the mean of what it has seen, or 30), taking empty ground whenever it can; move half of its strongest interior region to its weakest adjacent frontier region. Up to `max_orders` orders, padded with holds. Because the policy is fixed and the fog rule is shared, red's play is a function of the game so far and nothing else.

## 7. Commitment and receipt
`hidden` = red's starting strengths. `salt` = SHA-256("FOGWAR1|salt|" + seed). `commitment` = SHA-256("FOGWAR1|commit|" + scenario_hash + "|" + rules_version + "|" + seed + "|" + canon(hidden) + "|" + salt), published before blue's first move. The receipt carries rules_version, scenario_hash, seed, commitment, salt, the opened hidden, blue's accepted moves per turn, red's accepted moves per turn, turns played, outcome, the eliminated side, the final state hash and the final regions; `game_id` = SHA-256 of the canonical receipt. Canonical JSON is sorted keys, no spaces, ASCII, and no floats ever enter a hashed structure.

## 8. Determinism contract
The PRNG is fogsim's 64-bit LCG, seeded once per game, drawn only for combat shocks. Every iteration over regions is in id order. The AI uses no randomness. Losses are floors of double products with identical operand order in both engines. Strengths are integers. Scenario floats never enter a hashed structure (the scenario is hashed as bytes). Any change to any of this is a new rules version.

## 9. What P1 proves and what it does not
Proven by `test_fogwar_parity.py` on 2026-09-04: 60 games with random legal blue move logs (including deliberately illegal orders), executed in Python and in node from the same inputs - 0 divergent final state hashes, outcomes, turn counts, commitments or game ids; 328 combats across those games exercising attacker-wins, defender-holds and undecided paths; the receipt of a game verifies by re-execution and its opened fog reproduces the commitment; a receipt with one opened-fog value altered fails verification; the pure-JS SHA-256 the browser will use agrees with node's crypto on every case tried, including non-ASCII text.

Not yet done, and P2's first job: the game is not tuned. Against a passive blue the AI takes the empty centre and never assaults a defended region, because its attack threshold is 1.5x an estimate of 30 and blue's held regions are stronger than that; random blue loses 58 of 60 on controlled value with no eliminations in ten turns. Turns, reinforce rate, attack threshold and starting strengths are knobs to be set by play, in the board, not guessed in the engine. Any tuning that changes rule text is `fogwar/1.1`.

## 10. Phases
P1 engine + twin + differential test (this). Shell: the shared instrument frame every tool page uses (operator ruling: shell before the board). P2 board: phone-first, inside the shell, single player against the rule AI, hot-seat two-player free. P3 receipt and verifier page: download the receipt, verify any receipt by re-execution in the browser, the same way decc.html verifies a disclosure. P4 sealed campaign sets: fogsim's hashlog machinery over fogwar scenarios and seeds, the count committed before play.
