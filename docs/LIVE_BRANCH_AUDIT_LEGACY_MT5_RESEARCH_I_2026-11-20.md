# SYNERGY Live Branch Audit — Legacy MT5 Research Systems I

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three MT5 research repositories.  
**Method:** read-only GitHub REST; source purpose checked against current main README, branch SHAs and PR associations fetched live.  
**Limit:** no MetaTrader terminal, broker account, live trading, independent backtest or external data provider was operated.

## Summary

| Repository | Main purpose and verified boundary | Branches | Open PRs | Latest workflow | Main CI | Decision |
|---|---|---:|---:|---|---|---|
| [`Shtenco/quantum-trading_metatrader5`](https://github.com/Shtenco/quantum-trading_metatrader5) | Quantum/quantum-circuit MT5 research prototype. README explicitly says price_binary input is not used by the fixed circuit; no market forecast or quantum advantage is established. | 2 | 0 | none observed | CI_NOT_VERIFIED absent exact-main checks | Keep as independent research prototypes; do not combine into a live strategy until OOS and broker execution gates pass. |
| [`Shtenco/computer_vision_trading_metatrader_5`](https://github.com/Shtenco/computer_vision_trading_metatrader_5) | MarketVision RGB/2D image encoding of technical indicators with CNN/attention; research ML prototype, no independently reproduced out-of-sample performance. | 2 | 0 | none observed | CI_NOT_VERIFIED absent exact-main checks | Keep as independent research prototypes; do not combine into a live strategy until OOS and broker execution gates pass. |
| [`Shtenco/swap_arbitrage_metatrader_5`](https://github.com/Shtenco/swap_arbitrage_metatrader_5) | Swap/carry portfolio research using MT5 quotes, current swap_long/swap_short, SLSQP optimization and scenario simulation; no proven arbitrage or positive live return. | 2 | 0 | none observed | CI_NOT_VERIFIED absent exact-main checks | Keep as independent research prototypes; do not combine into a live strategy until OOS and broker execution gates pass. |

## quantum-trading_metatrader5

**Purpose:** Quantum/quantum-circuit MT5 research prototype. README explicitly says price_binary input is not used by the fixed circuit; no market forecast or quantum advantage is established.  
**Current main:** `a0ec14a8f10c2b26668664c0626ab63bce7094eb`.  
**Open PRs:** 0.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/editorial-readme-v1` | `cba6ebfff5a050e485eb8700e1742f28221e81e1` | Inferred from branch name: docs editorial readme v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Input sequence is not connected to the fixed quantum circuit; need causal input encoding, classical baseline and statistically powered out-of-sample test. Retain pending branch lineage review. |
| `main` | `a0ec14a8f10c2b26668664c0626ab63bce7094eb` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Input sequence is not connected to the fixed quantum circuit; need causal input encoding, classical baseline and statistically powered out-of-sample test. Retain canonical; research-only status. |

## computer_vision_trading_metatrader_5

**Purpose:** MarketVision RGB/2D image encoding of technical indicators with CNN/attention; research ML prototype, no independently reproduced out-of-sample performance.  
**Current main:** `0aabf5bf43052a1fb4bc98c07126811a165e911d`.  
**Open PRs:** 0.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/editorial-readme-v1` | `7793889ad8b01c9ec8958ee8da39786962632212` | Inferred from branch name: docs editorial readme v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Need leakage-free chronological splits, locked dataset, baseline parity, artifact hashes and independent OOS replication. Retain pending branch lineage review. |
| `main` | `0aabf5bf43052a1fb4bc98c07126811a165e911d` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Need leakage-free chronological splits, locked dataset, baseline parity, artifact hashes and independent OOS replication. Retain canonical; research-only status. |

## swap_arbitrage_metatrader_5

**Purpose:** Swap/carry portfolio research using MT5 quotes, current swap_long/swap_short, SLSQP optimization and scenario simulation; no proven arbitrage or positive live return.  
**Current main:** `232c704f37156eac5d774f33fb652b7afa3866e0`.  
**Open PRs:** 0.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `docs/editorial-readme-v1` | `10a134bb840b678293c1586b6fec200109e82784` | Inferred from branch name: docs editorial readme v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Current broker swap values cannot stand in for historical swap schedules; include FX P&L, spread, commissions, financing changes and liquidation risk. Retain pending branch lineage review. |
| `main` | `232c704f37156eac5d774f33fb652b7afa3866e0` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and consumers before cleanup. Current broker swap values cannot stand in for historical swap schedules; include FX P&L, spread, commissions, financing changes and liquidation risk. Retain canonical; research-only status. |

## Legacy MT5 portfolio boundary

These three repositories cover different research hypotheses and should not be collapsed into a single execution engine:

- Quantum-trading: quantum circuit experiment; presently not a causal predictor because the input sequence is unused.
- Computer-vision trading: visual representation and CNN/attention experiment; requires rigorous OOS validation.
- Swap arbitrage: carry-aware portfolio model; positive swap is not arbitrage without full FX, funding and execution costs.

A future shared trading platform may consume their **versioned research signals**, but RiskGuard, order authorization, broker credentials, execution and ledger reconciliation must remain separate services. The README evidence is source-level; it is not proof of profitable or live operation.

**No branches, PRs, MT5 terminals, credentials or broker accounts were modified.**
