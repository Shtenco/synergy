# SYNERGY Live Branch Audit — QuantLab, RiskGuard and Institutional MIDAS

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three trading-control repositories.  
**Method:** read-only GitHub REST; exact branch SHA and PR head/base association. CI credited only to exact SHA observations.  
**Limit:** no live broker, portfolio, market-data subscription or production risk engine was exercised.

## Summary

| Repository | Role | Branches | Open PRs | Latest workflow | Main CI | Disposition |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_quantlab`](https://github.com/Shtenco/synergy_quantlab) | Quantitative research laboratory, backtesting, strategy evaluation and portfolio experiments | 3 | 0 | Pinned Federated Synthetic Benchmark: success @ main/57ee40a6879c | CI_NOT_VERIFIED absent exact-main checks | Keep research, risk controls and institutional execution separate but contract-compatible. |
| [`Shtenco/synergy_riskguard`](https://github.com/Shtenco/synergy_riskguard) | Risk controls, portfolio limits, exposure monitoring and execution guardrails | 3 | 0 | ci: failure @ main/bc3ef1810c5d | CI_NOT_VERIFIED absent exact-main checks | Keep research, risk controls and institutional execution separate but contract-compatible. |
| [`Shtenco/synergy_midas_institutional`](https://github.com/Shtenco/synergy_midas_institutional) | Institutional MIDAS strategy lineage, portfolio allocation and institutional execution controls | 3 | 0 | ci: failure @ main/75f646380cd0 | CI_NOT_VERIFIED absent exact-main checks | Keep research, risk controls and institutional execution separate but contract-compatible. |

## synergy_quantlab

**Role:** Quantitative research laboratory, backtesting, strategy evaluation and portfolio experiments.  
**Current main:** `57ee40a6879c0db6550b573aacadad27347fb2db`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** Pinned Federated Synthetic Benchmark=success @ main/57ee40a6879c (2026-10-24T01:23:47Z); ci=failure @ main/57ee40a6879c (2026-10-24T01:23:47Z); ci=failure @ main/f1730a394b2c (2026-10-24T01:23:44Z); ci=failure @ main/316c2b33d586 (2026-10-24T01:23:34Z); ci=failure @ main/108c6ed0cce6 (2026-10-24T01:23:00Z); ci=failure @ main/df808e3cf666 (2026-10-24T00:56:25Z); ci=failure @ main/74f61d743979 (2026-10-24T00:56:22Z); ci=failure @ main/d6c4fd101066 (2026-10-24T00:56:20Z); ci=failure @ main/df3e054905a7 (2026-10-23T20:07:37Z); ci=failure @ main/81a9737127bb (2026-10-19T19:17:15Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `27b41cb9babdc45d644f4fe95b16156f44baf955` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream references. Backtests need no-lookahead validation, walk-forward splits, costs, slippage, survivorship and reproducibility. Retain pending lifecycle review. |
| `main` | `57ee40a6879c0db6550b573aacadad27347fb2db` | Canonical default branch | MAIN | success (Pinned Federated Synthetic Benchmark, 2026-10-24T01:23:47Z) | No open PR; purpose inferred; inspect ancestry and downstream references. Backtests need no-lookahead validation, walk-forward splits, costs, slippage, survivorship and reproducibility. Retain canonical; operational risk claims require exact-SHA and live control evidence. |
| `production/v3.0.0` | `3727a085a4f805ee77a187e30ab7433bfb17d4c2` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream references. Backtests need no-lookahead validation, walk-forward splits, costs, slippage, survivorship and reproducibility. Retain pending lifecycle review. |

## synergy_riskguard

**Role:** Risk controls, portfolio limits, exposure monitoring and execution guardrails.  
**Current main:** `bc3ef1810c5d77f54b8a9ecf2f1b8adc35231f2b`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/bc3ef1810c5d (2026-10-24T00:57:05Z); ci=failure @ main/95ae5ffbc1a0 (2026-10-24T00:57:03Z); ci=failure @ main/8857df2b2bf0 (2026-10-24T00:57:00Z); ci=failure @ main/55372eb9b081 (2026-10-23T20:07:40Z); ci=failure @ main/f23d03db95ec (2026-10-19T19:02:16Z); ci=failure @ main/ca1174f50670 (2026-09-28T18:04:33Z); ci=failure @ main/d268252679c6 (2026-09-28T18:03:49Z); ci=failure @ main/ccf25d89e3c4 (2026-09-28T18:01:46Z); ci=failure @ main/21afbefa2032 (2026-09-28T18:01:43Z); ci=failure @ main/235a3d4e6960 (2026-09-28T17:00:54Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `b0a5ad16a7adf6368395d8b1b600900685e85b3c` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream references. Risk limits must be enforced outside strategy agents; require fail-closed behavior and kill-switch tests. Retain pending lifecycle review. |
| `main` | `bc3ef1810c5d77f54b8a9ecf2f1b8adc35231f2b` | Canonical default branch | MAIN | failure (ci, 2026-10-24T00:57:05Z) | No open PR; purpose inferred; inspect ancestry and downstream references. Risk limits must be enforced outside strategy agents; require fail-closed behavior and kill-switch tests. Retain canonical; operational risk claims require exact-SHA and live control evidence. |
| `production/v3.0.0` | `c6d20f2c37fdebace002da9af9052ae23ddb1a5a` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream references. Risk limits must be enforced outside strategy agents; require fail-closed behavior and kill-switch tests. Retain pending lifecycle review. |

## synergy_midas_institutional

**Role:** Institutional MIDAS strategy lineage, portfolio allocation and institutional execution controls.  
**Current main:** `75f646380cd0a1478e5093216615b1af8ded1fbf`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/75f646380cd0 (2026-10-24T00:57:21Z); ci=failure @ main/22a8482f5e0e (2026-10-24T00:57:18Z); ci=failure @ main/bc76cfdc3b71 (2026-10-24T00:57:16Z); ci=failure @ main/9ea5cb0310de (2026-10-23T20:07:48Z); ci=failure @ main/1b9708693b23 (2026-10-19T19:17:08Z); ci=failure @ main/fbdcbb693af2 (2026-09-29T01:39:01Z); ci=failure @ main/96c4540afebe (2026-09-29T01:25:29Z); ci=failure @ main/65b6f5d70f2c (2026-09-28T22:06:33Z); ci=failure @ main/b610138a0fec (2026-09-28T22:05:31Z); ci=failure @ main/ed5ee20251c7 (2026-09-28T17:01:04Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `4b6a7b19e53d46ed3baff267fb9221656e33c007` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream references. Institutional readiness requires permissions, execution audit, position reconciliation and capacity/market impact evidence. Retain pending lifecycle review. |
| `main` | `75f646380cd0a1478e5093216615b1af8ded1fbf` | Canonical default branch | MAIN | failure (ci, 2026-10-24T00:57:21Z) | No open PR; purpose inferred; inspect ancestry and downstream references. Institutional readiness requires permissions, execution audit, position reconciliation and capacity/market impact evidence. Retain canonical; operational risk claims require exact-SHA and live control evidence. |
| `production/v3.0.0` | `00ff3fffbb3d90ac81297c55dca1b58b95aa6f2b` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream references. Institutional readiness requires permissions, execution audit, position reconciliation and capacity/market impact evidence. Retain pending lifecycle review. |

## Trading-control acceptance gates

- QuantLab research outputs do not authorize orders.
- RiskGuard should be a separate deterministic enforcement boundary with hard limits, independent monitoring and fail-closed behavior.
- MIDAS institutional execution must reconcile broker positions, fills, cash, fees, funding and internal ledger state.
- All performance metrics must be net of transaction costs and tested out-of-sample with locked datasets/configuration.
- Keep all three repositories separate; integrate through versioned signals, risk-intent and execution-result contracts.

**No branches, PRs, trading accounts or risk settings were modified.**
