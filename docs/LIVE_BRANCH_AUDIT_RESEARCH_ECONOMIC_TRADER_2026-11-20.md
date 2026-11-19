# SYNERGY Live Branch Audit — Research, Economic Master and Trader tranche

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 Actions runs for three previously uncovered repositories.  
**Method:** read-only GitHub REST. Main README was inspected for purpose. PR association is exact head branch + SHA. CI is credited only to the exact observed branch HEAD; older failures on different SHAs are not treated as current-HEAD failures.  
**Limit:** no closed PR history, full CI history, check-runs for every branch, local rebuilds, economic valuation validation or live broker execution was performed.

## Summary

| Repository | Purpose | Branches | Open PRs | CI evidence | Decision |
|---|---|---:|---:|---|---|
| [synergy_project](https://github.com/Shtenco/synergy_project) | Economic master dossier, 89-asset portfolio audit and IP-backed financing | 5 | 3 (all draft) | No Actions runs returned | Keep as master dossier; valuation/financing claims remain research until independently reconciled |
| [dlp_solver](https://github.com/Shtenco/dlp_solver) | REVERSE-EXP cryptographic constraint research; computational crossover not found | 23 | 1 (draft) | V13 Qiskit probe failed on exact PR HEAD; no main run observed | Preserve research lineage; do not claim cryptographic break or computational speedup |
| [synergy_agi_trader](https://github.com/Shtenco/synergy_agi_trader) | LLM-native Sovereign Trader research and foundation archive | 3 | 0 | Runtime probe failed on exact branch HEAD; no main CI observed | Keep experimental; no production/live trading promotion |

## synergy_project

**Main SHA:** `fcfaa292ab97b622ac6292b8179aaa66a4e585a4`  
**Open PRs:** #3, #2 and #1; all draft and target main.  
**CI:** Actions API returned no workflow runs; classify as CI_NOT_VERIFIED, not PASS.

| Branch | HEAD SHA | State / PR | CI | Decision |
|---|---|---|---|---|
| `audit/portfolio-89-repositories-v1` | `9ffa1736783df8f4ff19163d0b9d5716fcba0ca9` | #2 draft | NOT_OBSERVED | Retain; review valuation and IP financing evidence before promotion |
| `grant-dossier-ip-valuation-v1` | `4c6e1c3b4c735c78bab947b7f114d6b59b84231e` | NO_OPEN_PR | NOT_OBSERVED | Retain; review valuation and IP financing evidence before promotion |
| `main` | `fcfaa292ab97b622ac6292b8179aaa66a4e585a4` | MAIN | NOT_OBSERVED | Retain; review valuation and IP financing evidence before promotion |
| `research/ip-financing-readiness-2026-11-14` | `40cd4901df5aae9b63cb51e4f2aa8df25c9c9103` | #3 draft | NOT_OBSERVED | Retain; review valuation and IP financing evidence before promotion |
| `valuation-v3-87-assets-20261114` | `66b5fed8332a65865962cafb22cb41c3701b38f5` | #1 draft | NOT_OBSERVED | Retain; review valuation and IP financing evidence before promotion |

The README declares the project an R&D / pre-production / regulatory-sandbox candidate and identifies the economic operating model as capital → external value → science → industry. The portfolio audit and valuation PRs are not evidence that 89 assets are independently valued, legally transferable or financeable. Require source artefacts, valuation method, owner/IP rights, liabilities, revenue evidence and independent review.

## dlp_solver

**Main SHA:** `f140d3e7f1db141d7ce5497b65663fd4d4f5b305`  
**Open PR:** [#12 V13 Qiskit graph probe](https://github.com/Shtenco/dlp_solver/pull/12), draft, exact head `12118ec87685b0380e8916b92be3d8821ce33470`.  
**Latest observed CI:** run [36622254861](https://github.com/Shtenco/dlp_solver/actions/runs/36622254861) failed on that exact PR head. Main has no run in the returned latest-10 window.

The README explicitly distinguishes information-theoretic candidate reduction from computational work and states that computational crossover has not been found. This is the correct claim boundary. Keep all V13/Qiskit outputs as failed or unresolved experimental evidence until the job log, dependency environment and a deterministic rerun are available. Do not describe REVERSE-EXP as SHA-256 inversion or a cryptographic break.

## synergy_agi_trader

**Main SHA:** `8efe7942ed6c68ac4b081ee44b651ac99fd0ae7c`  
**Open PRs:** none.  
**Latest observed workflows:** [Qwen 3.5 runtime probe](https://github.com/Shtenco/synergy_agi_trader/actions/runs/35353005404) failed on `runtime/qwen35-4b-2026-eval` exact HEAD `eadbf502f069739f9cd492538477f6fefbd5b8a8`. Foundation import failures occurred on older SHAs, not the current import branch HEAD.

The README explicitly separates the approved target architecture from historical research lineage and archive provenance. A verified archive checksum proves byte integrity of the imported payload, not that the target Sovereign Trader runtime exists or is production-ready. Require runtime implementation, unit/integration tests, deterministic Capital Guardian, paper trading, OOS evaluation and execution safety review before any live capital.

## Branch-level disposition

The full machine-readable branch list, exact HEAD SHA, PR association, CI evidence and per-branch decision is appended to the consolidated JSON/CSV registry. All 31 observed branch refs in this tranche are retained; no branch deletion, merge or source-code mutation was performed.
