# SYNERGY Live Branch Audit — Evidence, Coder and Trading Terminal Tranche

**Audit date:** 2026-11-20  
**Scope:** live GitHub branches, open PRs and latest 10 workflow runs for three repositories.  
**Method:** read-only GitHub REST. Exact branch HEAD SHA and PR head/base association are live values. CI is attached only to exact SHA evidence visible in the returned run window.  
**Limit:** this is not a broker account audit, external credential rotation verification, full historical workflow census or proof of production trading.

## Summary

| Repository | Role | Branches | Open PRs | Latest workflow | Main CI | Disposition |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_nexus_science_agent`](https://github.com/Shtenco/synergy_nexus_science_agent) | Scientific evidence contracts, source provenance, experiment execution and reproducibility | 8 | 7 | NEXUS R8.3 Research Cortex: failure @ r83-research-cortex/363e27e6f064 | CI_NOT_VERIFIED absent exact-main check | Science/coder stay evidence-gated; trading terminal remains P0-blocked. |
| [`Shtenco/synergy_ai_coder`](https://github.com/Shtenco/synergy_ai_coder) | Requirement-to-code traceability, change planning, CI evidence and artifact provenance | 8 | 6 | engineering-foundation: failure @ feat/recursive-context-archive-integration-20261118/ef6b09113376 | CI_NOT_VERIFIED absent exact-main check | Science/coder stay evidence-gated; trading terminal remains P0-blocked. |
| [`Shtenco/synergy_ai_trade_terminal`](https://github.com/Shtenco/synergy_ai_trade_terminal) | Trading terminal, broker connectivity, execution UI and order lifecycle | 5 | 0 | none observed | CI_NOT_VERIFIED absent exact-main check | Science/coder stay evidence-gated; trading terminal remains P0-blocked. |

## synergy_nexus_science_agent

**Role:** Scientific evidence contracts, source provenance, experiment execution and reproducibility.  
**Current main:** `5ccad4e6d2bc82f147e6955b811720df2542ea23`.  
**Open PRs:** 7.  
**Latest 10 workflow observations:** NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/363e27e6f064 (2026-09-11T04:49:03Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/363e27e6f064 (2026-09-11T04:49:00Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/a68fa5919045 (2026-09-11T04:47:18Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/a68fa5919045 (2026-09-11T04:47:15Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/54287ffb1ffa (2026-09-11T04:45:07Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/54287ffb1ffa (2026-09-11T04:45:04Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/bc8750b4b56f (2026-09-11T04:44:57Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/bc8750b4b56f (2026-09-11T04:44:50Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/a541fc9e440f (2026-09-11T04:44:43Z); NEXUS R8.3 Research Cortex=failure @ r83-research-cortex/a541fc9e440f (2026-09-11T04:44:41Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `feat/local-science-service-build-recipe-v1-20260821` | `2e4e86484d842f1283204fa87d86927603278e5b` | Add deterministic local Science Agent service build recipe v1 | #5 draft | NOT_OBSERVED in latest-10 workflow window | PR base=feat/science-service-protocol-v4-20260821; draft gate. Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |
| `feat/science-service-protocol-v4-20260821` | `0607690c3036d2fdce2ac3e044094a8e4da0311b` | Add bounded local Science Agent service protocol v4 | #4 draft | NOT_OBSERVED in latest-10 workflow window | PR base=feat/source-quality-identity-v3-20260821; draft gate. Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |
| `feat/search-evidence-graph-core-v1-20260821` | `90135b758799f1bf931c1e3e14e937d826ef8dae` | Add deterministic search index and evidence graph research core v1 | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |
| `feat/source-quality-identity-v3-20260821` | `c9872e48a55d38fdfc26b209d2df1027e97fa6ad` | Add canonical source identity and transparent quality gate v3 | #3 draft | NOT_OBSERVED in latest-10 workflow window | PR base=feat/web-retrieval-snapshot-v2-20260821; draft gate. Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |
| `feat/web-retrieval-snapshot-v2-20260821` | `2c1a2e9e19ab0c1498f5fee759d25d20d62d429a` | Add provenance-preserving web retrieval and network safety boundary v2 | #2 draft | NOT_OBSERVED in latest-10 workflow window | PR base=feat/search-evidence-graph-core-v1-20260821; draft gate. Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |
| `federation-v3-domain-expansion` | `82545d735a6cb90de890fda164f1868ef1d435a6` | Federation V3: add science→falsification→commercialization pipeline | #6 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |
| `main` | `5ccad4e6d2bc82f147e6955b811720df2542ea23` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain canonical; enforce exact-SHA checks. |
| `r83-research-cortex` | `363e27e6f0649809bf01cf1ca12b6f9ab2f7fd04` | R8.3 Research Cortex — autonomous web research, evidence graph, falsification and memory | #7 draft | failure (NEXUS R8.3 Research Cortex, 2026-09-11T04:49:03Z) | PR base=main; draft gate. Require exact-head CI and independent review. REPRODUCED requires independent execution receipt, not only a reproduction command/hash. Retain; review diff and evidence before promotion. |

## synergy_ai_coder

**Role:** Requirement-to-code traceability, change planning, CI evidence and artifact provenance.  
**Current main:** `4ccdae38ff831d7b3f2e4e4872b593a5f58609e7`.  
**Open PRs:** 6.  
**Latest 10 workflow observations:** engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/ef6b09113376 (2026-11-19T03:36:06Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/5e483a6e1944 (2026-11-19T03:35:58Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/936a552bcdbb (2026-11-19T03:30:36Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/6342afa4c407 (2026-11-19T03:30:30Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/3ff34f8b7790 (2026-11-19T03:30:17Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/df820d6107dc (2026-11-19T03:30:13Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/1fcb88c43213 (2026-11-19T03:30:05Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/49fe95853536 (2026-11-19T03:28:53Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/3f83653a17ba (2026-11-19T03:28:43Z); engineering-foundation=failure @ feat/recursive-context-archive-integration-20261118/f35392f46f83 (2026-11-19T03:27:56Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/editorial-batch03` | `8d3c42e0561bb0632fc9307889173e62b6540ec2` | Inferred from branch name: docs editorial batch03 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain pending lifecycle audit; no deletion by default. |
| `feat/autonomous-engineering-foundation-20261114` | `3fb7d85c86c15f8d181cec872866696a2fd7fb9b` | Add autonomous engineering foundation: context archive and DAG planner | #6 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head CI and independent review. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain; review diff and evidence before promotion. |
| `feat/change-set-review-protocol-20260818` | `337941f2b2da327da9c9addf6f616836ccc86168` | Add deterministic engineering change-set review protocol without autonomous merge authority | #2 draft | NOT_OBSERVED in latest-10 workflow window | PR base=feat/sinergy-engineering-orchestration-20260817; draft gate. Require exact-head CI and independent review. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain; review diff and evidence before promotion. |
| `feat/recursive-context-archive-integration-20261118` | `ef6b0911337610773d3915ed93431ed98c897e6e` | feat: integrate recursive context archive codecs | #7 draft | failure (engineering-foundation, 2026-11-19T03:36:06Z) | PR base=feat/autonomous-engineering-foundation-20261114; draft gate. Require exact-head CI and independent review. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain; review diff and evidence before promotion. |
| `feat/sinergy-engineering-orchestration-20260817` | `af59705399ee55c048997f831a2dffeb7fb66aeb` | Bootstrap SINERGY autonomous engineering orchestration layer | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head CI and independent review. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain; review diff and evidence before promotion. |
| `federation-v3-domain-expansion` | `93653d59882a27cc2253a97da0f089b4c432cc67` | Federation V3: expand AI Coder into evidence-backed change orchestration | #3 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require exact-head CI and independent review. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain; review diff and evidence before promotion. |
| `main` | `4ccdae38ff831d7b3f2e4e4872b593a5f58609e7` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain canonical; enforce exact-SHA checks. |
| `migration/synergy-723-2026-09` | `d14a10936557b85f92fbec50aa4a558d2ac2ab7c` | chore: stage SYNERGY 723-file migration artifacts | #4 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head CI and independent review. APPROVED requires authenticated reviewer/CI provenance and artifact-to-commit binding. Retain; review diff and evidence before promotion. |

## synergy_ai_trade_terminal

**Role:** Trading terminal, broker connectivity, execution UI and order lifecycle.  
**Current main:** `e53064ec6741dce47ee10a5f30b798c0cf4daa2a`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `codex/fix-price-discrepancy-in-dashboard` | `e2f0eb52041862f2a6e2e49271f549e66e52f098` | Inferred from branch name: codex fix price discrepancy in dashboard | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. P0 broker credential exposure is registered; no deployment or live trading until external rotation/revocation and history review are evidenced. Retain pending lifecycle audit; no deletion by default. |
| `codex/revise-cassandra-architecture-for-python` | `8ee6b215eed8c39c0248cdc9b1dadcdddf86e4b9` | Inferred from branch name: codex revise cassandra architecture for python | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. P0 broker credential exposure is registered; no deployment or live trading until external rotation/revocation and history review are evidenced. Retain pending lifecycle audit; no deletion by default. |
| `codex/revise-cassandra-architecture-for-python-tvznjv` | `6c9a141f2ea2211154f7278918cf49cd2e649fd2` | Inferred from branch name: codex revise cassandra architecture for python tvznjv | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. P0 broker credential exposure is registered; no deployment or live trading until external rotation/revocation and history review are evidenced. Retain pending lifecycle audit; no deletion by default. |
| `docs/editorial-batch03` | `fd9a05f425ee836a3534b77f67b8763d87501904` | Inferred from branch name: docs editorial batch03 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. P0 broker credential exposure is registered; no deployment or live trading until external rotation/revocation and history review are evidenced. Retain pending lifecycle audit; no deletion by default. |
| `main` | `e53064ec6741dce47ee10a5f30b798c0cf4daa2a` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry, tags and downstream references before cleanup. P0 broker credential exposure is registered; no deployment or live trading until external rotation/revocation and history review are evidenced. Retain canonical; enforce exact-SHA checks. |

## Cross-repository evidence gates

### Science agent

A declared `REPRODUCED` state must be backed by an independently signed execution receipt: source commit, command, environment lock, executor identity, artifact digest, exit status and captured outputs. A hash alone proves byte identity, not scientific truth; a command string alone proves no execution. Keep hypothesis, simulation, measured and independently reproduced claims distinct.

### AI Coder

An `APPROVED` record must resolve to authenticated reviewer identity, CI run ID and exact commit SHA, trusted artifact subject digest, and proof the artifact was produced from that commit. User-supplied PASS fields or a syntactically valid SHA string are insufficient.

### Trading terminal

A non-placeholder broker username/password literal was confirmed in `cassandra_v6_FIXED.py`; the same file contains authentication and order-placement paths. This is a registered P0 security blocker. Broker-side validity, exploitation and rotation/revocation were not verified. The branch audit does not reproduce credential values. No trading deployment or execution should be enabled until credentials are rotated/revoked externally, access logs reviewed, source/history remediated and dependents moved to fresh secrets.

## Disposition

- Keep science, provenance/coder and broker execution as separate trust domains.
- Do not promote scientific claims from schema state alone.
- Do not promote code changes from self-reported PASS status alone.
- Do not deploy the trading terminal while its P0 credential incident remains unresolved.
- A branch without an open PR is `NO_OPEN_PR`, not automatically obsolete.
- No branches, PRs, source files, workflow settings or broker settings were modified in this audit.
