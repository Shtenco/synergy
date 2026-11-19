# SYNERGY Repository Audit Delta — 2026-11-20

**Scope:** eight repositories from the agent, trading-interface and science-infrastructure audit package.  
**Method:** read-only inspection of current `main` source files where listed below, plus the supplied exact-SHA CI findings for the investment committee and market graph. No source, branch, PR, workflow or deployment was changed by this audit.  
**Interpretation:** a source-level finding is not a claim that an incident was exploited. A contract, hash or passing test is not by itself proof of trusted identity, independent reproduction, deployment or economic realization.

## Executive register

| Repository | Domain / role | Finding | Status / gate |
|---|---|---|---|
| [`synergy_ai_trade_terminal`](https://github.com/Shtenco/synergy_ai_trade_terminal) | Trading UI / broker execution | Literal credential material is present in `cassandra_v6_FIXED.py`; the same file contains authentication and live order-placement paths. `MAIN.py` falls back to an infinite heartbeat loop when collector/tester startup fails. | **P0 security**; rotate/revoke credentials externally, inspect Git history and access logs. Runtime readiness must fail closed. |
| [`synergy_agi_olga`](https://github.com/Shtenco/synergy_agi_olga) | NEXUS collective intelligence | Ed25519 verification uses the public key supplied by the message; there is no demonstrated binding of that key to an admitted `node_id`. Quorum uses `len(verified_p)`, while answers are keyed by `node_id`; duplicate identities can inflate proposal count while collapsing the answer map. | **High identity / Sybil risk**; require registry-backed key-to-node binding, unique admitted identities and quorum over distinct authorized nodes. |
| [`synergy_agi_autopilot`](https://github.com/Shtenco/synergy_agi_autopilot) | Agent orchestration | Current README explicitly classifies main as `STUB / architecture node`; full autonomous runtime is not confirmed. | **Architecture-only**; exclude from deployed/operational agent counts. |
| [`synergy_ai_investment_committee`](https://github.com/Shtenco/synergy_ai_investment_committee) | Investment decision support | Supplied exact-SHA CI record: 19 tests passed, 2 failed on `7dbec0202badf1afce60ada83b5402f8d8ed9f14`. Failures: unsupported `r.path` access on FastAPI internal `_IncludedRouter`; README version-string assertion not satisfied. | **CI red on recorded SHA**; re-run against current main SHA before treating as current CI state. |
| [`synergy_market_graph`](https://github.com/Shtenco/synergy_market_graph) | Executable market / arbitrage graph | In `src/synergy_market_graph/core.py`, `Edge` stores capacity and latency, but `executable_rate()` applies only rate, fee and slippage; path valuation does not enforce capacity or latency. Latest recorded CI failed; logs were unavailable. | **High execution-validity gap**; route profitability is not proof of executable volume/time feasibility. |
| [`synergy_nexus_science_agent`](https://github.com/Shtenco/synergy_nexus_science_agent) | Scientific evidence and reproduction | Contract requires a reproduction command for `REPRODUCED` and marks independent reproduction as required, but schema-level declaration does not prove that an independent executor actually ran it. SHA-256 binds bytes, not source authenticity or conclusion validity. | **Evidence contract, not reproduction attestation**; require signed independent-run receipt and environment/result binding. |
| [`synergy_ai_coder`](https://github.com/Shtenco/synergy_ai_coder) | Engineering provenance / change approval | `APPROVED` is accepted when supplied check records all say `PASS`; commit SHA format and optional artifact digest are validated, but the contract does not independently authenticate reviewer identity, CI origin, commit existence or artifact-to-commit provenance. | **Provenance hardening required**; verify CI attestations, reviewer signatures and artifact subject/source relationships. |
| [`synergy_agi_trader`](https://github.com/Shtenco/synergy_agi_trader) | Sovereign Trader lineage | The reviewed baseline is an archive/import scaffold with 15 archive parts, a migration manifest and SHA-256 extraction checks; this does not establish a complete trading runtime. | **Migration/archive substrate**; runtime readiness remains unproven until build, tests, integrations and controlled execution are evidenced. |

## Source fingerprints inspected on main

| Repository / path | Blob SHA |
|---|---|
| `synergy_ai_trade_terminal/cassandra_v6_FIXED.py` | `61d2b4a094150ed6b3086ccf3e2904067ee9d44a` |
| `synergy_ai_trade_terminal/MAIN.py` | `9145e627d8f3f44549cb49999f6dda4b3e8d730b` |
| `synergy_agi_olga/nexus_collective/protocol.py` | `12a618ca87fd4823850faa69bac83f151497b2b3` |
| `synergy_agi_olga/nexus_collective/consensus.py` | `bd6f48241bfa67d566a334c90cf328b8644cf811` |
| `synergy_agi_autopilot/README.md` | `5a50b9d90bc106294fb488523fe2caef6d3867d9` |
| `synergy_market_graph/src/synergy_market_graph/core.py` | `ad2b4d3d81f4f54ae85ad4b4be187534497a067f` |
| `synergy_nexus_science_agent/contracts/science_contracts.py` | `4eb798b8921b65304552d3556f7deacc608b232a` |
| `synergy_ai_coder/runtime/contracts.py` | `a192a19e115a946f96377066f4ba78162359a9c3` |

Credential values are intentionally omitted. The presence of a hard-coded password/credential field is sufficient to trigger the security gate; no secret is copied into this report.

## SDU asymmetric AMM — economic evidence boundary

The reviewed 30-day simulation reported the following outcomes:

| Scenario | Day-30 AMM reference price | USDC reserve |
|---|---:|---:|
| Base | 1.8561 | 920,081.91 |
| Bull | 2.2992 | 948,873.54 |
| Stress | 1.4940 | 850,291.28 |

All three modeled prices rose from 1.00 while the USDC reserve fell from 1,000,000. Therefore reference-price appreciation or mark-to-market TVL must not be reported as growth in external cash liquidity. The referenced simulator and CSV inputs were absent from the inspected `synergy_market_graph/main` tree in the supplied audit snapshot; independent reproduction remains pending.

## Cross-ecosystem consequences

1. **Identity & trust:** signatures must resolve to enrolled identities and authorization scopes; message-supplied public keys are not an identity registry.
2. **Runtime truth:** heartbeat, process liveness and functional readiness are separate states. Startup fallback must not masquerade as a healthy service.
3. **Execution safety:** graph paths need capacity, latency, freshness, venue constraints and settlement feasibility before becoming executable intents.
4. **Evidence provenance:** `PASS`, a SHA-256 digest, a commit-shaped string or a reproduction command is not independent proof without authenticated origin and subject binding.
5. **Economic truth:** price marks, reserves, cash, liabilities, settlement and realized external P&L remain separate measures.
6. **Maturity accounting:** STUB, archive/import scaffold, R&D, adapter-integrated, E2E-tested and deployed are distinct states.

## Required follow-up gates

- Revoke/rotate the exposed broker credential outside GitHub; scan all refs/history and inspect provider access logs. Do not publish the credential value.
- Add an identity registry and unique-node quorum enforcement to NEXUS collective consensus.
- Keep AGI Autopilot and AGI Trader out of operational runtime inventory until their execution paths are demonstrated.
- Re-run investment-committee CI on the current main SHA and preserve exact run/job evidence.
- Extend market-graph route feasibility to capacity/latency constraints; restore the missing simulator inputs and reproduce the AMM result.
- Require independently signed reproduction receipts in the science evidence contract.
- Require signed review/CI attestations and artifact-to-commit provenance in AI Coder.

## Canonical ecosystem registries

- [91-repository owner inventory](https://github.com/Shtenco/synergy/blob/main/registry/repos.json)
- [91-repository architecture atlas](https://github.com/Shtenco/synergy_system/blob/main/docs/SYNERGY_REPOSITORY_ATLAS.md)
- [Full branch census report](https://github.com/Shtenco/synergy/blob/main/docs/BRANCH_INVENTORY_2026-11-20.md)
- [Branch names and HEAD SHAs — CSV](https://github.com/Shtenco/synergy/blob/main/registry/BRANCH_INVENTORY_2026-11-20.csv)
- [Branch inventory — JSON](https://github.com/Shtenco/synergy/blob/main/registry/BRANCH_INVENTORY_2026-11-20.json)
- [High-branch repository / BQG audit](https://github.com/Shtenco/synergy/blob/main/docs/HIGH_BRANCH_REPOSITORY_AUDIT_2026-11-20.md)

**Audit posture:** read-only source review. No child-repository code, branches, PRs, CI settings, secrets or deployments were modified. The branch census linked above is a dated 2026-11-20 snapshot and must be refreshed before any branch deletion or merge decision.
