# SYNERGY Live Branch Audit — Legacy MT5 Research Systems II

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three MT5/FX research repositories.  
**Method:** read-only GitHub REST; purpose checked against current main README; exact branch SHA and PR associations fetched live.  
**Limit:** no broker terminal, external market feed, live arbitrage or independent backtest was executed.

## Summary

| Repository | Main purpose / implementation boundary | Branches | Open PRs | Latest workflow | Main CI | Decision |
|---|---|---:|---:|---|---|---|
| [`Shtenco/cross_forex_arbitrage_trading_metatrader_5`](https://github.com/Shtenco/cross_forex_arbitrage_trading_metatrader_5) | Cross FX synthetic pricing research: current source uses MT5 OHLC, synthetic bid=close/ask=close+constant, route comparisons and single-leg TP/SL simulation; no three-leg atomic arbitrage or historical executable bid/ask proof. | 2 | 0 | none observed | CI_NOT_VERIFIED absent exact-main checks | Research-only; retain independent until data and execution semantics are corrected. |
| [`Shtenco/global_liquidity_dataminer`](https://github.com/Shtenco/global_liquidity_dataminer) | Macro/FX research combining FRED, Yahoo Finance, MT5, a mixed z-score index and RandomForest; README flags mislabeled central-bank balance proxies, leakage and incomplete forecast uncertainty. | 2 | 0 | none observed | CI_NOT_VERIFIED absent exact-main checks | Research-only; retain independent until data and execution semantics are corrected. |
| [`Shtenco/3D_bars_market_structure`](https://github.com/Shtenco/3D_bars_market_structure) | MT5 M15 multi-factor/3D visualization and CSV research; README explicitly says not true Renko and not a validated ML/trading signal; whole-sample normalization and synthetic OHLC naming need care. | 9 | 1 | MOEX Unified CatBoost Research: success @ moex-catboost-unified-20260904/6b90eb9846f3 | CI_NOT_VERIFIED absent exact-main checks | Research-only; retain independent until data and execution semantics are corrected. |

## cross_forex_arbitrage_trading_metatrader_5

**Purpose:** Cross FX synthetic pricing research: current source uses MT5 OHLC, synthetic bid=close/ask=close+constant, route comparisons and single-leg TP/SL simulation; no three-leg atomic arbitrage or historical executable bid/ask proof.  
**Current main:** `09fb17a3e70a21ee5bb10815b70d6fc3c41105a7`.  
**Open PRs:** 0.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/editorial-readme-v1` | `e6b7f9519a53ba65eedef75759da81a15058cfa1` | Inferred from branch name: docs editorial readme v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Synthetic quote construction is not executable bid/ask; timestamp synchronization, route leg depth, atomicity and three-leg fill modeling are missing. Retain pending lifecycle review. |
| `main` | `09fb17a3e70a21ee5bb10815b70d6fc3c41105a7` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Synthetic quote construction is not executable bid/ask; timestamp synchronization, route leg depth, atomicity and three-leg fill modeling are missing. Retain canonical; research-only. |

## global_liquidity_dataminer

**Purpose:** Macro/FX research combining FRED, Yahoo Finance, MT5, a mixed z-score index and RandomForest; README flags mislabeled central-bank balance proxies, leakage and incomplete forecast uncertainty.  
**Current main:** `728b6af3e53fc0d8beafe060d6f1ee209395b3f5`.  
**Open PRs:** 0.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/editorial-readme-v1` | `31a688e9c4c71a4465780de318514d46ec408d1a` | Inferred from branch name: docs editorial readme v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct source semantics, release-time lags, vintage data, leakage controls and out-of-sample calibration before use. Retain pending lifecycle review. |
| `main` | `728b6af3e53fc0d8beafe060d6f1ee209395b3f5` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct source semantics, release-time lags, vintage data, leakage controls and out-of-sample calibration before use. Retain canonical; research-only. |

## 3D_bars_market_structure

**Purpose:** MT5 M15 multi-factor/3D visualization and CSV research; README explicitly says not true Renko and not a validated ML/trading signal; whole-sample normalization and synthetic OHLC naming need care.  
**Current main:** `5bcf5a95e54d454116d89fa23d1337500091accd`.  
**Open PRs:** 1.  
**Latest workflow observations:** MOEX Unified CatBoost Research=success @ moex-catboost-unified-20260904/6b90eb9846f3 (2026-09-04T16:08:21Z); MOEX Unified CatBoost Research=success @ moex-catboost-unified-20260904/768befe18b92 (2026-09-04T16:03:06Z); MOEX Unified CatBoost Research=success @ moex-catboost-unified-20260904/493f8adb4ef7 (2026-09-04T16:02:47Z); TURBO Stage-1I XPU Device Runtime=success @ turbo-stage1i-xpu-v14/e27486656bd8 (2026-07-31T12:52:59Z); TURBO Stage-1F Canonical Idle Runtime=success @ turbo-stage1i-xpu-v14/e27486656bd8 (2026-07-31T12:52:59Z); TURBO Stage-1H EML Dataflow Runtime=success @ turbo-stage1i-xpu-v14/e27486656bd8 (2026-07-31T12:52:59Z); TURBO Stage-1F Canonical Idle Runtime=success @ turbo-stage1i-xpu-v14/91583a19b0c7 (2026-07-31T12:51:10Z); TURBO Stage-1H EML Dataflow Runtime=success @ turbo-stage1i-xpu-v14/91583a19b0c7 (2026-07-31T12:51:10Z); TURBO Stage-1I XPU Device Runtime=failure @ turbo-stage1i-xpu-v14/91583a19b0c7 (2026-07-31T12:51:10Z); TURBO Stage-1H EML Dataflow Runtime=success @ turbo-stage1i-xpu-v14/2c24ad15cabe (2026-07-31T12:46:30Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/visual-dossier-batch02` | `3beb9c4ee29a24378138cebfd8475d0c0218ea6f` | Inferred from branch name: docs visual dossier batch02 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |
| `main` | `5bcf5a95e54d454116d89fa23d1337500091accd` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain canonical; research-only. |
| `moex-catboost-unified-20260904` | `4e535017bfeeac04f06c6540c4161f91c8151e2f` | Inferred from branch name: moex catboost unified 20260904 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |
| `turbo-stage1f-asset-test` | `51cb6c41ba4ddfd70d67ac99ea9537ce586843f1` | Inferred from branch name: turbo stage1f asset test | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |
| `turbo-stage1f-integrated-v10` | `ee0245e7abd99fb1700e07d3da527a46812e0c64` | Inferred from branch name: turbo stage1f integrated v10 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |
| `turbo-stage1f-runtime` | `f3dd90e9fc3f675c8f0d93b55a21a1b0fe186540` | Temporary TURBO Stage-1F public QEMU runner | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and independent review required. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain candidate; no promotion without causal and OOS validation. |
| `turbo-stage1g-topology-v12` | `a63e6dfcff217a0361ede2e676681996697a3fe5` | Inferred from branch name: turbo stage1g topology v12 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |
| `turbo-stage1h-eml-v13` | `45ba82cf0f0eecf829bdbbf52c89d0b96192de38` | Inferred from branch name: turbo stage1h eml v13 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |
| `turbo-stage1i-xpu-v14` | `e27486656bd8366820a49954e515c742a33bb92c` | Inferred from branch name: turbo stage1i xpu v14 | NO_OPEN_PR | success (TURBO Stage-1I XPU Device Runtime, 2026-07-31T12:52:59Z) | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Correct whole-sample normalization and OHLC semantics; test against causal baselines and preserve raw input mapping. Retain pending lifecycle review. |

## Shared legacy-trading decision

These three repositories contain potentially reusable research assets, but not one interchangeable trading strategy:

- Cross FX is a synthetic-price consistency prototype, not an executable multi-leg arbitrage system.
- Global Liquidity Data Miner is a macro/FX forecasting prototype; source labels and temporal causality need correction before its index is trusted.
- 3D Bars is a visualization/feature experiment; the current naming and normalization can mislead downstream models if interpreted as raw OHLC.

**Recommended disposition:** preserve all three histories; extract reusable, corrected data adapters and research features only after tests; send any future signals through shared RiskGuard and TradeMux interfaces. Do not grant order authority to these research repositories.

**No branches, PRs, MT5 terminals, accounts or source files were modified.**
