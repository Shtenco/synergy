# SYNERGY — Open PR / Branch Association Audit

**Snapshot:** 2026-11-20  
**Scope:** all 91 repositories; all currently open pull requests returned by GitHub REST API.

## Summary

- Repositories queried: **91/91**
- Open pull requests: **548**
- Draft PRs: **414**
- Ready-for-review PRs: **134**
- PRs targeting main: **268**
- PR head branch refs: **548**
- PR head branch refs found in branch census: **548/548**
- Exact PR head SHA == current branch HEAD SHA: **548/548**
- Duplicate head-branch names with multiple open PRs: **4**

All 548 open PR heads currently resolve to a branch in the branch census, and each PR head SHA matches that branch's HEAD at snapshot time. This validates the branch-to-open-PR mapping, not the PR's code quality, mergeability, CI status, or production readiness.

## Repositories with most open PRs

| Repository | Open PRs | Draft | Ready | Target main |
|---|---:|---:|---:|---:|
| [`Shtenco/synergy_binary_quantum_theory`](https://github.com/Shtenco/synergy_binary_quantum_theory) | 51 | 27 | 24 | 35 |
| [`Shtenco/synergy_system`](https://github.com/Shtenco/synergy_system) | 47 | 43 | 4 | 7 |
| [`Shtenco/synergy_financial_os`](https://github.com/Shtenco/synergy_financial_os) | 39 | 36 | 3 | 4 |
| [`Shtenco/synergy_meta_os`](https://github.com/Shtenco/synergy_meta_os) | 28 | 26 | 2 | 5 |
| [`Shtenco/synergy_ai_language`](https://github.com/Shtenco/synergy_ai_language) | 25 | 13 | 12 | 15 |
| [`Shtenco/synergychain.github.io`](https://github.com/Shtenco/synergychain.github.io) | 25 | 20 | 5 | 20 |
| [`Shtenco/synergy_gllm_nexus`](https://github.com/Shtenco/synergy_gllm_nexus) | 24 | 23 | 1 | 3 |
| [`Shtenco/synergy_ai_blockchain`](https://github.com/Shtenco/synergy_ai_blockchain) | 22 | 21 | 1 | 7 |
| [`Shtenco/synergy_pay_system`](https://github.com/Shtenco/synergy_pay_system) | 20 | 16 | 4 | 11 |
| [`Shtenco/synergy_net`](https://github.com/Shtenco/synergy_net) | 20 | 18 | 2 | 4 |
| [`Shtenco/synergy_chain`](https://github.com/Shtenco/synergy_chain) | 19 | 10 | 9 | 13 |
| [`Shtenco/synergy_agi_nexus`](https://github.com/Shtenco/synergy_agi_nexus) | 19 | 16 | 3 | 5 |
| [`Shtenco/synergy_ai_financial_system`](https://github.com/Shtenco/synergy_ai_financial_system) | 17 | 13 | 4 | 12 |
| [`Shtenco/synergy_agi_autopilot`](https://github.com/Shtenco/synergy_agi_autopilot) | 15 | 13 | 2 | 5 |
| [`Shtenco/synergistic_economics`](https://github.com/Shtenco/synergistic_economics) | 13 | 12 | 1 | 5 |
| [`Shtenco/synergy_agi_olga`](https://github.com/Shtenco/synergy_agi_olga) | 11 | 5 | 6 | 8 |
| [`Shtenco/synergy_eurasian`](https://github.com/Shtenco/synergy_eurasian) | 11 | 6 | 5 | 9 |
| [`Shtenco/synegy_ai_compress`](https://github.com/Shtenco/synegy_ai_compress) | 10 | 4 | 6 | 5 |
| [`Shtenco/synergy_maps`](https://github.com/Shtenco/synergy_maps) | 9 | 9 | 0 | 2 |
| [`Shtenco/synergy_triangle_money_system`](https://github.com/Shtenco/synergy_triangle_money_system) | 8 | 8 | 0 | 8 |
| [`Shtenco/shtencoauantai.github.io`](https://github.com/Shtenco/shtencoauantai.github.io) | 7 | 7 | 0 | 4 |
| [`Shtenco/synergy_nexus_science_agent`](https://github.com/Shtenco/synergy_nexus_science_agent) | 7 | 6 | 1 | 3 |
| [`Shtenco/synergy_gguf_compress`](https://github.com/Shtenco/synergy_gguf_compress) | 7 | 0 | 7 | 1 |
| [`Shtenco/synergy_turbo_linux`](https://github.com/Shtenco/synergy_turbo_linux) | 6 | 2 | 4 | 5 |
| [`Shtenco/synergy_ai_coder`](https://github.com/Shtenco/synergy_ai_coder) | 6 | 5 | 1 | 4 |

## Duplicate branch references

- `Shtenco/synergy_pay_system` · `feat/distribution-settlement-reversal-v2-fee-refund-20260828` · PRs #16, #14
- `Shtenco/synergy_ai_blockchain` · `feat/economic-testnet-persistent-restart-evidence-v1-20260828` · PRs #17, #16
- `Shtenco/synergy_financial_os` · `feat/distribution-available-capacity-v4-refund-restored-20260828` · PRs #33, #32
- `Shtenco/synergy_system` · `feat/economic-os-rc5-canonical-capture-ready-20260828` · PRs #35, #34

## Machine-readable artifacts

- [JSON — per-repository open PR inventory](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.json)
- [CSV — one row per open PR](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.csv)
- [Branch inventory JSON](../registry/BRANCH_INVENTORY_2026-11-20.json)
- [Branch inventory CSV](../registry/BRANCH_INVENTORY_2026-11-20.csv)

## Important limitations

This is an open-PR snapshot only. Closed and merged PR history is not included in this file. A branch with no open PR is not automatically stale or deletable. Before deleting or merging any branch, check closed PRs, workflow history, external references, branch protection and the branch's unique commits relative to main.
