# SYNERGY Live Branch Audit — Crypto Pump, Graph Money and Print-Money Chain

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three monetary/trading repositories.  
**Method:** read-only GitHub REST; exact branch SHA and PR association. CI credited only to observed exact SHA.  
**Limit:** no market manipulation, live trading, token issuance, wallet signing or production money transfer was executed.

## Summary

| Repository | Role | Branches | Open PRs | Latest workflow | Main CI | Disposition |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_crypto_pump`](https://github.com/Shtenco/synergy_crypto_pump) | Crypto market pump/dump signal research and trading strategy candidates | 3 | 1 | CI: failure @ main/5232f83f3051 | CI_NOT_VERIFIED absent exact-main checks | Keep research separate from authorized economic execution. |
| [`Shtenco/synergy_graph_print_money`](https://github.com/Shtenco/synergy_graph_print_money) | Graph-based monetary flows, print-money mechanisms and capital network experiments | 6 | 5 | V7 live Base snapshot: failure @ main/bf5733de1a1e | CI_NOT_VERIFIED absent exact-main checks | Keep research separate from authorized economic execution. |
| [`Shtenco/print_money_synergychain`](https://github.com/Shtenco/print_money_synergychain) | Alternative money issuance, tokenized credit and SynergyChain monetary concepts | 9 | 3 | AICB EVM Tests: success @ aicb-v2-mainnet-fork/24f15b0548b3 | CI_NOT_VERIFIED absent exact-main checks | Keep research separate from authorized economic execution. |

## synergy_crypto_pump

**Role:** Crypto market pump/dump signal research and trading strategy candidates.  
**Current main:** `5232f83f3051721c491aaf739c4a20c2382be9ee`.  
**Open PRs:** 1.  
**Latest 10 workflow observations:** CI=failure @ main/5232f83f3051 (2026-11-08T23:47:37Z); CI=failure @ main/a1cefdad8c72 (2026-10-24T00:44:56Z); CI=failure @ main/63fe0aa92710 (2026-10-24T00:44:54Z); CI=failure @ main/940bb749f3ad (2026-10-24T00:44:52Z); CI=failure @ main/b26d6a6d1518 (2026-10-23T20:06:45Z); CI=failure @ main/8875c0de2399 (2026-10-19T18:53:58Z); HISTORICAL LATOKEN 90D CHUNKED RECOVERY=failure @ v3-profitability-audit-hardening/d2f94ea16f36 (2026-10-05T22:10:17Z); CI=failure @ v3-profitability-audit-hardening/d2f94ea16f36 (2026-10-05T22:10:17Z); HISTORICAL LATOKEN 90D CHUNKED RECOVERY=failure @ v3-profitability-audit-hardening/ad32f63c3223 (2026-10-05T21:55:09Z); CI=failure @ v3-profitability-audit-hardening/ad32f63c3223 (2026-10-05T21:55:09Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `main` | `5232f83f3051721c491aaf739c4a20c2382be9ee` | Canonical default branch | MAIN | failure (CI, 2026-11-08T23:47:37Z) | No open PR; purpose inferred; verify ancestry and downstream references. Need manipulation-resistant data, exchange rules, fees, risk limits and independent out-of-sample evidence. Retain canonical; no live execution until controls pass. |
| `v3-execution-risk-shadow` | `17ec77e89df4007d5a6eeba239cf0510f5ad1666` | V3: 95% architecture — historical Solana data, first-passage ML, execution, risk and shadow/canary gates | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require strategy and security review. Need manipulation-resistant data, exchange rules, fees, risk limits and independent out-of-sample evidence. Retain candidate; test in isolated environment before promotion. |
| `v3-profitability-audit-hardening` | `d2f94ea16f367c6426f187bb0e4fba8b1a8132c0` | Inferred from branch name: v3 profitability audit hardening | NO_OPEN_PR | failure (HISTORICAL LATOKEN 90D CHUNKED RECOVERY, 2026-10-05T22:10:17Z) | No open PR; purpose inferred; verify ancestry and downstream references. Need manipulation-resistant data, exchange rules, fees, risk limits and independent out-of-sample evidence. Retain pending lineage audit; do not delete automatically. |

## synergy_graph_print_money

**Role:** Graph-based monetary flows, print-money mechanisms and capital network experiments.  
**Current main:** `bf5733de1a1e1b31cbb0b91b91a2742536b68cad`.  
**Open PRs:** 5.  
**Latest 10 workflow observations:** V7 live Base snapshot=failure @ main/bf5733de1a1e (2026-11-08T23:47:40Z); V7 live Base snapshot=cancelled @ main/14ea7f84c6ab (2026-10-24T00:46:21Z); V7 live Base snapshot=cancelled @ main/c18f302ae29e (2026-10-24T00:46:19Z); V7 live Base snapshot=cancelled @ main/7b7276dc19d0 (2026-10-24T00:46:16Z); V7 live Base snapshot=cancelled @ main/a106b9f3c4e7 (2026-10-23T20:06:51Z); V7 live Base snapshot=failure @ main/e915de385929 (2026-10-19T18:54:10Z); V7 live Base snapshot=failure @ v7-4-triangle-mev-audit/fa982e3bac90 (2026-10-11T21:03:23Z); V7 live Base snapshot=failure @ main/3bcac56deaaf (2026-09-28T22:50:27Z); V7 live Base snapshot=failure @ main/6a68d8e164ab (2026-09-28T22:49:25Z); V7 live Base snapshot=failure @ main/ac0f8ba438d9 (2026-09-28T17:25:21Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `main` | `bf5733de1a1e1b31cbb0b91b91a2742536b68cad` | Canonical default branch | MAIN | failure (V7 live Base snapshot, 2026-11-08T23:47:40Z) | No open PR; purpose inferred; verify ancestry and downstream references. Modelled issuance/flow is not external capital; require liability accounting, authorization, redemption and settlement proofs. Retain canonical; no live execution until controls pass. |
| `migration/synergy-723-2026-09` | `103d6e5c6c21bf260ba69c12faa868e9566cc03b` | chore: stage SYNERGY 723-file migration provenance | #4 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require strategy and security review. Modelled issuance/flow is not external capital; require liability accounting, authorization, redemption and settlement proofs. Retain candidate; test in isolated environment before promotion. |
| `v7-4-triangle-mev-audit` | `fa982e3bac902ec516bf6a6c0b464c8dc4502995` | V7.4: reconcile fork packet and add triangle/MEV accounting gates | #5 draft | failure (V7 live Base snapshot, 2026-10-11T21:03:23Z) | PR base=main; draft gate. Require strategy and security review. Modelled issuance/flow is not external capital; require liability accounting, authorization, redemption and settlement proofs. Retain candidate; test in isolated environment before promotion. |
| `v7-live-validation` | `b9d0c604f318316fdd9840eeb1ef810320b0c561` | V7 live Base validation run | #1 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require strategy and security review. Modelled issuance/flow is not external capital; require liability accounting, authorization, redemption and settlement proofs. Retain candidate; test in isolated environment before promotion. |
| `v8-profit-engine` | `e6f533d792217a49195a8bc380e3330fcdacb9d5` | V8 profit engine | #3 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require strategy and security review. Modelled issuance/flow is not external capital; require liability accounting, authorization, redemption and settlement proofs. Retain candidate; test in isolated environment before promotion. |
| `v8-single-contract-flash-proof` | `537c30d7cc87de50edee8eba5dd916ad6a6ac31b` | V8 single contract flash proof | #2 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require strategy and security review. Modelled issuance/flow is not external capital; require liability accounting, authorization, redemption and settlement proofs. Retain candidate; test in isolated environment before promotion. |

## print_money_synergychain

**Role:** Alternative money issuance, tokenized credit and SynergyChain monetary concepts.  
**Current main:** `7dd01e7da992d2efedb957e83a48218b86d0083f`.  
**Open PRs:** 3.  
**Latest 10 workflow observations:** AICB EVM Tests=success @ aicb-v2-mainnet-fork/24f15b0548b3 (2026-09-07T22:01:31Z); AICB EVM Tests=success @ aicb-v2-mainnet-fork/bd689c89fcfd (2026-09-07T21:59:09Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/418872c00ec2 (2026-09-07T21:57:30Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/b3fd76b86c33 (2026-09-07T21:53:41Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/3f61b88ea08a (2026-09-07T21:52:26Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/94b0f53ad960 (2026-09-07T21:51:38Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/972f3d7da0b4 (2026-09-07T21:50:21Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/5c7682a7be23 (2026-09-07T21:49:24Z); AICB EVM Tests=failure @ aicb-v2-mainnet-fork/c608545959a1 (2026-09-07T21:49:13Z); AICB EVM Tests=success @ aicb-v2-mainnet-fork/63e937fe77f9 (2026-09-07T21:28:32Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `aicb-v1-exact-reset` | `edd7a1eb6b9782b0c859beb0bddc5adc14e651fa` | V1 exact-reset AICB baseline | #3 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require strategy and security review. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain candidate; test in isolated environment before promotion. |
| `aicb-v2-mainnet-fork` | `24f15b0548b3c4b3e514b52a9c742db52db81e8c` | Inferred from branch name: aicb v2 mainnet fork | NO_OPEN_PR | success (AICB EVM Tests, 2026-09-07T22:01:31Z) | No open PR; purpose inferred; verify ancestry and downstream references. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain pending lineage audit; do not delete automatically. |
| `feat/hybrid-external-profit-model-v1-20260905` | `0b0fc5b8a63ac411006dbfdc6f9c899a16285672` | Add falsifiable hybrid print-machine external-profit model v1 | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; draft gate. Require strategy and security review. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain candidate; test in isolated environment before promotion. |
| `federation-v3-domain-expansion` | `2f9325814e4bb9e9b4b2e5c8d1bc9a7049d3d729` | Federation V3: formalize monetary/liquidity falsification firewall | #2 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; Require strategy and security review. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain candidate; test in isolated environment before promotion. |
| `main` | `7dd01e7da992d2efedb957e83a48218b86d0083f` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain canonical; no live execution until controls pass. |
| `print_money_synergychain` | `e7b30474bed17d1e2e7de20f1b537cf03812aa76` | Inferred from branch name: print money synergychain | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain pending lineage audit; do not delete automatically. |
| `research/omega-v3-base-fork-hardnav` | `9fc3343648297faf8a9b91230964cfec33cfef76` | Inferred from branch name: research omega v3 base fork hardnav | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain pending lineage audit; do not delete automatically. |
| `research/omega-v4-inflation-bounded-graph` | `4ac67bee187ef2c04b8c92520c9e1f640b97230a` | Inferred from branch name: research omega v4 inflation bounded graph | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain pending lineage audit; do not delete automatically. |
| `research/omega-v5-real-flow-fork` | `dd956f05186790ff27a3443e17dd914e90c7154a` | Inferred from branch name: research omega v5 real flow fork | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and downstream references. Issuance must be policy-bounded, collateral/liability reconciled, and controlled by separated keys and governance. Retain pending lineage audit; do not delete automatically. |

## Decision gates

- Distinguish strategy research from order execution and external settlement.
- Model monetary issuance as a liability/claim with explicit redemption, collateral, loss allocation and authorization—not as free cash creation.
- Require auditable market data, non-manipulable signal generation, adversarial testing, risk caps and a kill switch.
- No autonomous issuer or trading agent may acquire signing authority from branch presence or a successful local unit test.

**No branches, PRs, credentials, wallets, trades or on-chain state were modified.**
