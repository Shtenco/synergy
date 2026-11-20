# Pay System and AI Financial System — PR / CI audit (2026-11-20)

## Inventory

| Repository | Total PRs | Open | Closed | Draft | Merged |
|---|---:|---:|---:|---:|---:|
| `synergy_pay_system` | 24 | 20 | 4 | 17 | 3 |
| `synergy_ai_financial_system` | 24 | 17 | 7 | 14 | 6 |
| **Total** | **48** | **37** | **11** | **31** | **9** |

Eighteen direct branch-stack dependency edges were found by matching PR `base.ref` to another PR's `head.ref`. The payment/settlement chain is parent-dependent and must be integrated in order; the AI Financial System contains several distinct historical product/research lines, not one single release stack.

## Branch ancestry — 20 current-main comparisons

### SYNERGY Pay System

| PR / branch | Ahead | Behind | Status |
|---|---:|---:|---|
| #24 settlement audit | 32 | 0 | ahead |
| #23 Meta Exchange hybrid pricing | 20 | 1 | diverged |
| #20 Federation V3 domain expansion | 10 | 20 | diverged, refreshed after lint fixes |
| #19 global long-cycle graph | 97 | 20 | diverged |
| #18 hybrid arbitrage external-profit gate | 87 | 20 | diverged |
| #17 capped-canary external requirements | 72 | 20 | diverged |
| #16 distribution settlement reversal v2 | 70 | 20 | diverged |
| #8 MetaPay global settlement | 20 | 20 | diverged |
| #7 PQ migration adapters | 3 | 20 | diverged |
| #1 final financial system | 1 | 79 | diverged |

PR #24's 32-ahead-only audit branch is a good review candidate but remains Draft and its CI startup failed before steps. It is not a product release or a merge-ready implementation.

### SYNERGY AI Financial System

| PR / branch | Ahead | Behind | Status |
|---|---:|---:|---|
| #22 real-asset emission escrow V1 | 123 | 15 | diverged |
| #21 Federation V3 domain expansion | 1 | 15 | diverged |
| #20 MetaPay external-profit evidence | 4 | 15 | diverged |
| #17 Financial OS V4 | 65 | 15 | diverged |
| #16 V15 math over V13.1 | 224 | 15 | diverged |
| #15 SynthL1 recursive QE/MEV | 109 | 15 | diverged |
| #13 Bullish CB refill-safe deploy | 94 | 15 | diverged |
| #11 RL secure runtime | 18 | 15 | diverged |
| #9 V11 atomic QE/QT fork | 125 | 15 | diverged |
| #7 V7 six-pool permissioned core | 135 | 15 | diverged |

## CI root causes and exact-head evidence

### Pay System

**PR #20 — Federation V3 domain expansion**
- The specialized Solidity check succeeded on the pre-fix exact SHA.
- Generic CI reached a runner, installed dependencies, then Ruff reported exactly **3 fixable errors**:
  - UP035: import `Iterator` from `collections.abc` in `src/synergy_pay/federation_outbox.py`.
  - UP017: use `datetime.UTC` in `tests/test_federation_contracts.py`.
  - I001: sort imports in `tests/test_federation_outbox.py`.
- All three were fixed in three small commits: `fde5d746b775a594caef943124916970d476ba4c`, `a53485da54fc2a3d50d43295deec737062dcaf3b`, `d99f10d622e1ae0cbc2e51ced1ab53037278a3f1`.
- The new exact-head CI and Solidity workflows are queued: [CI 44674460415](https://github.com/Shtenco/synergy_pay_system/actions/runs/44674460415), [Solidity 44674460417](https://github.com/Shtenco/synergy_pay_system/actions/runs/44674460417). No green rerun is claimed.

**PR #19 — Global Long-Cycle Graph**
- Specialized graph validation and Solidity checks succeeded.
- Generic CI reached Ruff and failed with **405 errors**, primarily broad E701/E702/I001 style violations across source and tests. This is not a dependency-install failure and not a runner-startup failure.
- The error volume is too large for a blanket lint suppression; it requires a scoped cleanup plan and review of the touched payment/settlement code.

**PR #18 — Hybrid arbitrage external-profit gate**
- Specialized MetaPay External Profit Bus and Solidity checks succeeded.
- Generic CI reached Ruff and failed with **402 errors**, across multiple maintained distribution/settlement modules and tests (including `distribution_settlement_v2.py`, `distribution_batch_v2.py`, `distribution_settlement_v3.py`, `distribution_reversal_v2.py` and related tests).
- This is genuine lint debt across maintained implementation/test files; do not classify it as a runner outage or suppress all Ruff rules.

**PR #24 — Settlement integrity audit**
- Generic CI and Solidity jobs failed before steps / runner allocation (`runner_id=0` or `startup_failure`). No source/test assertion was observed.

**PR #23 — Meta Exchange hybrid pricing**
- Both generic CI and Solidity jobs failed before runner steps (`runner_id=0`). No compiler or test result was produced.

**PR #17, #8, #7**
- The inspected generic CI runs failed before runner steps (`runner_id=0`); no test outcome is proven.

### AI Financial System

**PR #22 — AICB V5 productive monetary policy + dual-gate emission escrow**
- Three exact-head checks (SYNERGY RL security gate, AICB V5 productive monetary system, Real Asset Emission Escrow V1) failed before runner allocation; all show `runner_id=0`, zero steps.
- This is infrastructure-only evidence. It does not prove a code failure or a successful security/escrow validation.

**PR #20 — MetaPay external-profit evidence adapter**
- The dedicated exact-head workflow succeeded. This is positive scoped evidence, not a complete federation E2E or production settlement proof.

**PR #7 — V7 six-pool permissioned core**
- Twelve exact-head workflows succeeded; one failed at `Materialize V9 test bundle`.
- The corresponding job-log endpoint now returns HTTP 410, so the original failure detail is no longer available. Do not infer whether the missing bundle was a producer, path, or artifact-retention issue without a fresh reproduction.
- The green matrix is useful historical evidence, but the one failed workflow and 135-ahead / 15-behind branch ancestry keep the PR out of merge-ready status.

**PR #21**
- No exact-head workflow run was visible in the inspected Actions run inventory.

**PR #17 and #15**
- Exact-head CI failed before runner steps (`runner_id=0`); no code-level test outcome is proven.

**PR #13**
- Multiple preflight/security/Polygon fork workflows failed; the inspected preflight job had `runner_id=0` and zero steps. No chain/fork assertion is proven from that run.

## Decisions

- **KEEP:** keep Pay System (payment execution/settlement) and AI Financial System (monetary policy / research / financial R&D) as separate authorities.
- **DEVELOP:** Pay System PR #20's three Ruff fixes are committed; await CI. Address PR #18/#19 lint debt with a scoped formatting/review series, not blanket exclusions.
- **BLOCKED:** Pay System PRs #23/#24 and AI Financial PR #22/#13/#17/#15 by runner startup; PR #18/#19 by real Ruff failures; AI Financial PR #7 by one failed workflow with expired logs.
- **MERGE-READY:** none of the reviewed PRs.
- No PR was merged, no branch deleted, and no force-push performed.

## Evidence links

- [Pay System PR #24](https://github.com/Shtenco/synergy_pay_system/pull/24)
- [Pay System PR #20](https://github.com/Shtenco/synergy_pay_system/pull/20)
- [Pay System PR #19](https://github.com/Shtenco/synergy_pay_system/pull/19)
- [Pay System PR #18](https://github.com/Shtenco/synergy_pay_system/pull/18)
- [AI Financial System PR #22](https://github.com/Shtenco/synergy_ai_financial_system/pull/22)
- [AI Financial System PR #20](https://github.com/Shtenco/synergy_ai_financial_system/pull/20)
- [AI Financial System PR #7](https://github.com/Shtenco/synergy_ai_financial_system/pull/7)
