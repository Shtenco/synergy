# SYNERGY Live Branch Audit — QE and Alternative Monetary Systems

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three monetary-system repositories.  
**Method:** read-only GitHub REST; exact branch SHA and PR head/base associations. CI credited only to exact SHA observations.  
**Limit:** no central-bank operation, bank settlement, monetary issuance, custody or live credit obligations were performed or verified.

## Summary

| Repository | Role | Branches | Open PRs | Latest workflow | Main CI | Disposition |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_2chain_qe`](https://github.com/Shtenco/synergy_2chain_qe) | Two-chain quantitative easing and cross-ledger monetary policy experiments | 5 | 3 | Foundry Cycle A Unit Tests: failure @ recovery/base-synergy-l3-arbitrage-20261117/e7477ede9c65 | CI_NOT_VERIFIED absent exact-main checks | Research/simulation only until monetary liabilities and settlement are proven. |
| [`Shtenco/synergy_triangle_money_system`](https://github.com/Shtenco/synergy_triangle_money_system) | Triangle money / mutual-credit / alternative settlement system experiments | 9 | 8 | EVM V3: failure @ main/8fb8a604a225 | CI_NOT_VERIFIED absent exact-main checks | Research/simulation only until monetary liabilities and settlement are proven. |
| [`Shtenco/synergy_qe`](https://github.com/Shtenco/synergy_qe) | Quantitative easing and monetary policy simulation specifications | 3 | 2 | Foundry CI: failure @ impl/qe-engine-v1-m1/b5a6b5006df7 | CI_NOT_VERIFIED absent exact-main checks | Research/simulation only until monetary liabilities and settlement are proven. |

## synergy_2chain_qe

**Role:** Two-chain quantitative easing and cross-ledger monetary policy experiments.  
**Current main:** `79c105dac4c65e125b1ce395e8a493822de6356f`.  
**Open PRs:** 3.  
**Latest 10 workflow observations:** Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/e7477ede9c65 (2026-11-19T07:33:59Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/e7477ede9c65 (2026-11-19T07:33:55Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/69494f8b73f2 (2026-11-19T07:33:29Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/69494f8b73f2 (2026-11-19T07:33:25Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/42396fdab182 (2026-11-19T07:26:50Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/42396fdab182 (2026-11-19T07:26:46Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/399b35bc4670 (2026-11-19T07:26:14Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/399b35bc4670 (2026-11-19T07:26:11Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/60f664ce6a97 (2026-11-19T07:25:59Z); Foundry Cycle A Unit Tests=failure @ recovery/base-synergy-l3-arbitrage-20261117/60f664ce6a97 (2026-11-19T07:25:56Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `hardnav-v2-economic-core` | `3062b0a847bf3dbc27fb9e37ba80b69e6901565e` | HARDNAV V2: canonical accounting, solvent bridge, real V3 execution | #1 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require exact-head tests and accounting/legal review. Cross-chain issuance/settlement needs atomicity, bridge risk analysis, reserve/credit accounting and independent reconciliation. Retain research candidate; require model validation and independent review. |
| `integration/protocol-convergence-v1-20260925` | `0099d40f55ef4a94812d58c8126a88f2611352ff` | Stage SYNERGY Protocol Convergence P5 source-locked adapter | #2 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Cross-chain issuance/settlement needs atomicity, bridge risk analysis, reserve/credit accounting and independent reconciliation. Retain research candidate; require model validation and independent review. |
| `main` | `79c105dac4c65e125b1ce395e8a493822de6356f` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Cross-chain issuance/settlement needs atomicity, bridge risk analysis, reserve/credit accounting and independent reconciliation. Retain canonical; monetary claims remain non-operational until reconciled. |
| `pool-bridge` | `665677f58b6ef391d0c7a31d62b8aa8894a58eae` | Inferred from branch name: pool bridge | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Cross-chain issuance/settlement needs atomicity, bridge risk analysis, reserve/credit accounting and independent reconciliation. Retain pending lifecycle review. |
| `recovery/base-synergy-l3-arbitrage-20261117` | `e7477ede9c65700824502fd48f40f90085e5a166` | WIP: Recover and harden Base Cycle A arbitrage executor | #3 draft | failure (Foundry Cycle A Unit Tests, 2026-11-19T07:33:59Z) | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Cross-chain issuance/settlement needs atomicity, bridge risk analysis, reserve/credit accounting and independent reconciliation. Retain research candidate; require model validation and independent review. |

## synergy_triangle_money_system

**Role:** Triangle money / mutual-credit / alternative settlement system experiments.  
**Current main:** `8fb8a604a225a1ceaa9ee9272bf502d4603f9c39`.  
**Open PRs:** 8.  
**Latest 10 workflow observations:** EVM V3=failure @ main/8fb8a604a225 (2026-11-08T23:47:51Z); EVM V3=success @ main/4829e076745c (2026-10-24T02:37:52Z); EVM V3=success @ main/66a383864605 (2026-10-24T02:37:50Z); EVM V3=success @ main/9c4521c9935e (2026-10-24T02:37:47Z); EVM V3=failure @ main/0b5102d723f0 (2026-10-19T18:55:29Z); EVM V3=failure @ research/recursive-amm-v6-oracle-band/e44639b31ffd (2026-10-15T13:31:28Z); EVM V3=failure @ research/recursive-amm-v6-oracle-band/5f3108a59ece (2026-10-15T12:31:45Z); EVM V3=failure @ experiment/integrated-revenue-engine-v11/d7886b85b839 (2026-10-08T07:58:21Z); V8 isolated EVM=failure @ experiment/integrated-revenue-engine-v11/d7886b85b839 (2026-10-08T07:58:21Z); V10 Graph Arb EVM=failure @ experiment/integrated-revenue-engine-v11/d7886b85b839 (2026-10-08T07:58:21Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `experiment/adaptive-market-maker-v9` | `26ecd61706adc840a681d75ccffcd7fc86222ec3` | V9 adaptive three-pool market maker | #5 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `experiment/autonomous-borrower-hunter-v6` | `a10c25bb1fef4ac2876c632b29b6f2e5a82c3b2d` | V6 autonomous borrower market maker | #2 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `experiment/block-revenue-engine-v7` | `d23ac725dded6dfdcb506df3e753d27305c39f93` | V7 block revenue engine | #3 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `experiment/graph-arb-hardnav-v10` | `a8a49f65d9e5fd3987122aad7feaab799162c1a4` | V10 graph arbitrage HardNAV engine | #6 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `experiment/hardnav-multiplier-v5` | `74dae12833137bedd7bedb5bbb211f777425c2a2` | V5 hardnav multiplier engine | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `experiment/integrated-revenue-engine-v11` | `d7886b85b839f75d379d41ccb01b7e2b31b02d9e` | V11 integrated block revenue + graph HardNAV engine | #7 draft | failure (EVM V3, 2026-10-08T07:58:21Z) | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `experiment/three-pool-market-maker-v8` | `a33e8b4b83cc8a751e20e082efad95b572b0de57` | V8 three-pool asymmetric market maker EVM benchmark | #4 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |
| `main` | `8fb8a604a225a1ceaa9ee9272bf502d4603f9c39` | Canonical default branch | MAIN | failure (EVM V3, 2026-11-08T23:47:51Z) | No open PR; purpose inferred; verify ancestry and downstream references. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain canonical; monetary claims remain non-operational until reconciled. |
| `research/recursive-amm-v6-oracle-band` | `e44639b31ffd6bdecd3f229272e00ae8d642c03c` | R&D V6: independent-oracle band for asymmetric AMM (NOT DEPLOYABLE) | #8 draft | failure (EVM V3, 2026-10-15T13:31:28Z) | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Mutual-credit liabilities, redemption/settlement obligations, default handling and participant consent must be explicit. Retain research candidate; require model validation and independent review. |

## synergy_qe

**Role:** Quantitative easing and monetary policy simulation specifications.  
**Current main:** `c69f19ae77ac244a19e1ead4009ea7dc0fb2afdf`.  
**Open PRs:** 2.  
**Latest 10 workflow observations:** Foundry CI=failure @ impl/qe-engine-v1-m1/b5a6b5006df7 (2026-09-21T23:21:44Z); Foundry CI=failure @ impl/qe-engine-v1-m1/b5a6b5006df7 (2026-09-21T23:21:35Z); Foundry CI=failure @ impl/qe-engine-v1-m1/642e1b0442dc (2026-09-21T23:20:33Z); Foundry CI=failure @ impl/qe-engine-v1-m1/6c1dc8721d72 (2026-09-21T23:20:23Z); Foundry CI=failure @ impl/qe-engine-v1-m1/a239f118b933 (2026-09-21T23:20:21Z); Foundry CI=failure @ impl/qe-engine-v1-m1/e7b70e922b60 (2026-09-21T23:19:58Z); Foundry CI=failure @ impl/qe-engine-v1-m1/000887ecf5f6 (2026-09-21T23:19:49Z); Foundry CI=failure @ impl/qe-engine-v1-m1/b553df1892fe (2026-09-21T23:19:46Z); Foundry CI=failure @ impl/qe-engine-v1-m1/cc330429be50 (2026-09-21T23:19:19Z); Foundry CI=failure @ impl/qe-engine-v1-m1/b428341a697c (2026-09-21T23:19:17Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `impl/qe-engine-v1-m1` | `b5a6b5006df7b9eaa12cae35acaffbac8cd4919a` | M1: implement QE debt core and hard-value accounting | #2 draft | failure (Foundry CI, 2026-09-21T23:21:44Z) | PR base=spec/qe-engine-v1; draft gate. Require exact-head tests and accounting/legal review. Current maturity is spec-only; do not treat policy equations or simulations as executable monetary authority. Retain research candidate; require model validation and independent review. |
| `main` | `c69f19ae77ac244a19e1ead4009ea7dc0fb2afdf` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Current maturity is spec-only; do not treat policy equations or simulations as executable monetary authority. Retain canonical; monetary claims remain non-operational until reconciled. |
| `spec/qe-engine-v1` | `65d8479f47abdb26f37ddd14b2cc1bf2ad671b18` | QE Engine V1 architecture and implementation plan | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require exact-head tests and accounting/legal review. Current maturity is spec-only; do not treat policy equations or simulations as executable monetary authority. Retain research candidate; require model validation and independent review. |

## Monetary-system acceptance gates

1. Separate issued units, claims, liabilities, collateral, reserves, external cash and mark-to-market valuation.
2. Define who can issue, redeem, freeze, transfer, settle and absorb losses; enforce these permissions in deterministic contracts and signer controls.
3. Simulate defaults, liquidity stress, redemption runs, cross-chain failure, oracle unavailability and governance capture.
4. Prove accounting conservation and reconcile every settlement against an authoritative ledger.
5. Label every model result as analytical derivation, simulation, testnet observation or live external settlement.

**No branches, PRs, financial accounts, contracts or monetary state were modified.**
