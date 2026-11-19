# SYNERGY Live Branch Audit — Relative Value, Market Maker and Adaptive Engine

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three strategy repositories.  
**Method:** read-only GitHub REST; exact branch SHA and PR head/base associations. CI credited only to exact SHA observations.  
**Limit:** no live orders, venue connectivity, market making or profitability were executed or independently validated.

## Summary

| Repository | Role | Branches | Open PRs | Latest workflow | Main CI | Disposition |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_relative_value`](https://github.com/Shtenco/synergy_relative_value) | Relative-value and statistical-arbitrage strategy research | 3 | 0 | ci: failure @ main/0f37ef55ac98 | CI_NOT_VERIFIED absent exact-main checks | Research candidates; execution requires independent cost/risk and venue tests. |
| [`Shtenco/synergy_market_maker`](https://github.com/Shtenco/synergy_market_maker) | Market-making, inventory control, spread and liquidity provision strategies | 3 | 0 | ci: failure @ main/3edcea187c45 | CI_NOT_VERIFIED absent exact-main checks | Research candidates; execution requires independent cost/risk and venue tests. |
| [`Shtenco/synergy_adaptive_engine`](https://github.com/Shtenco/synergy_adaptive_engine) | Adaptive execution/strategy engine and dynamic parameter control | 3 | 0 | ci: failure @ main/c4af6194eedf | CI_NOT_VERIFIED absent exact-main checks | Research candidates; execution requires independent cost/risk and venue tests. |

## synergy_relative_value

**Role:** Relative-value and statistical-arbitrage strategy research.  
**Current main:** `0f37ef55ac989933acd63a0954b5cf521eec4449`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/0f37ef55ac98 (2026-10-24T00:57:29Z); ci=failure @ main/ea6e01693c7e (2026-10-24T00:57:26Z); ci=failure @ main/3fb022aad3ce (2026-10-24T00:57:24Z); ci=failure @ main/ddb065db2330 (2026-10-23T20:07:45Z); ci=failure @ main/dc1e7d124209 (2026-10-19T19:17:18Z); ci=failure @ main/f3750336e727 (2026-09-29T01:39:10Z); ci=failure @ main/2bc098f5b4d7 (2026-09-29T01:25:36Z); ci=failure @ main/2e1f358157f7 (2026-09-28T22:41:49Z); ci=failure @ main/2228da905a71 (2026-09-28T22:40:38Z); ci=failure @ main/043687c2de4c (2026-09-28T17:01:04Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `31f99549dd7806648ccd42f99b1af7ce4c16b282` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers. Pair stability, borrow/funding, execution latency, hedge slippage and regime shift must be modeled. Retain pending branch lifecycle review. |
| `main` | `0f37ef55ac989933acd63a0954b5cf521eec4449` | Canonical default branch | MAIN | failure (ci, 2026-10-24T00:57:29Z) | No open PR; purpose inferred; verify ancestry and consumers. Pair stability, borrow/funding, execution latency, hedge slippage and regime shift must be modeled. Retain canonical; do not authorize live trading from repository maturity alone. |
| `production/v3.0.0` | `6a8f955ff0b7a95deacf203e380b3502e15a4e87` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers. Pair stability, borrow/funding, execution latency, hedge slippage and regime shift must be modeled. Retain pending branch lifecycle review. |

## synergy_market_maker

**Role:** Market-making, inventory control, spread and liquidity provision strategies.  
**Current main:** `3edcea187c45866d55a65b74dc707b7b1009a69b`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/3edcea187c45 (2026-11-08T23:47:57Z); ci=failure @ main/7d0988ad0f62 (2026-10-24T00:57:58Z); ci=failure @ main/75781b1d1e28 (2026-10-24T00:57:56Z); ci=failure @ main/7697d45c94b7 (2026-10-24T00:57:54Z); ci=failure @ main/23ba9df530e8 (2026-10-23T20:08:04Z); ci=failure @ main/675d57a0fcd8 (2026-10-19T19:01:59Z); ci=failure @ main/b2da8e62b70c (2026-09-29T01:38:53Z); ci=failure @ main/8c4fd2395502 (2026-09-29T01:23:10Z); ci=failure @ main/4f558bcf765b (2026-09-28T20:44:06Z); ci=failure @ main/33665afdd47b (2026-09-28T20:42:42Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `ee36217fb2721826d21e7f0bc22de1965d95a90c` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers. Inventory skew, adverse selection, toxic flow, cancel/replace limits, venue rules and liquidation stress must be tested. Retain pending branch lifecycle review. |
| `main` | `3edcea187c45866d55a65b74dc707b7b1009a69b` | Canonical default branch | MAIN | failure (ci, 2026-11-08T23:47:57Z) | No open PR; purpose inferred; verify ancestry and consumers. Inventory skew, adverse selection, toxic flow, cancel/replace limits, venue rules and liquidation stress must be tested. Retain canonical; do not authorize live trading from repository maturity alone. |
| `production/v3.0.0` | `c764552393441b313e83524f35ee4094c8bda8ae` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers. Inventory skew, adverse selection, toxic flow, cancel/replace limits, venue rules and liquidation stress must be tested. Retain pending branch lifecycle review. |

## synergy_adaptive_engine

**Role:** Adaptive execution/strategy engine and dynamic parameter control.  
**Current main:** `c4af6194eedfbf9b9c0824822abe42306ba9f6b8`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/c4af6194eedf (2026-10-24T00:58:06Z); ci=failure @ main/21e4d488406a (2026-10-24T00:58:04Z); ci=failure @ main/0f3c6b23d04c (2026-10-24T00:58:02Z); ci=failure @ main/5d8cdba26128 (2026-10-23T20:08:01Z); ci=failure @ main/ae8acd91cc57 (2026-10-19T19:01:13Z); ci=failure @ main/02fc2d7c5267 (2026-09-28T20:44:00Z); ci=failure @ main/8e130d9f75a6 (2026-09-28T20:42:36Z); ci=failure @ main/211cebb33444 (2026-09-28T17:01:40Z); ci=failure @ main/23e299ecd9a2 (2026-09-28T16:26:11Z); ci=failure @ main/61d460046575 (2026-09-28T16:25:25Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `78d6696dff443079218b2087209c527f0fe94240` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers. Adaptive parameter changes need bounded policy ranges, deterministic audit logs and rollback/kill-switch tests. Retain pending branch lifecycle review. |
| `main` | `c4af6194eedfbf9b9c0824822abe42306ba9f6b8` | Canonical default branch | MAIN | failure (ci, 2026-10-24T00:58:06Z) | No open PR; purpose inferred; verify ancestry and consumers. Adaptive parameter changes need bounded policy ranges, deterministic audit logs and rollback/kill-switch tests. Retain canonical; do not authorize live trading from repository maturity alone. |
| `production/v3.0.0` | `856252eb8400546d3e7c359068f96c0d7dda7c99` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers. Adaptive parameter changes need bounded policy ranges, deterministic audit logs and rollback/kill-switch tests. Retain pending branch lifecycle review. |

## Decision gates

- Strategy code remains isolated from order authority.
- RiskGuard must enforce exposure and loss limits independently of these strategy services.
- Backtests require locked data, no-lookahead, walk-forward and net-of-cost metrics.
- Live market making requires venue sandbox and then limited canary with measured fills, inventory and adverse selection.
- Adaptive engines must log every parameter mutation, bound it by policy and support deterministic rollback.

**No branches, PRs, trading accounts or venue settings were modified.**
