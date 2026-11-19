# STM V11 — Economic and GitHub Evidence Audit

**Date:** 2026-11-20  
**Repository:** [Shtenco/synergy_triangle_money_system](https://github.com/Shtenco/synergy_triangle_money_system)  
**Main SHA:** `8fb8a604a225a1ceaa9ee9272bf502d4603f9c39`  
**Candidate V11 SHA:** `d7886b85b839f75d379d41ccb01b7e2b31b02d9e`  
**Scope:** source-level audit of the current main, V9 adaptive market maker, V10 graph arbitrage and V11 integrated revenue candidate. Read-only review; no child-repository code or deployment changed.

## Executive decision

**V11: DEVELOP / BLOCKED for merge and production.** Preserve the experiment; do not merge or deploy until CI, accounting and external settlement evidence are corrected.

## Economic objective

Optimize realized percentage growth of combined dollar NAV per block:

`g_block = (NAV_combined_after - NAV_combined_before) / NAV_combined_before`

Combined NAV must include LP/pool assets, Treasury, protocol-owned inventory, trader balances and liabilities at consistent external prices. Internal transfers, mint/burn, pool-to-treasury movements, gross turnover and mark-to-market TVL multipliers are not new wealth.

A 5% per-block result is a research target, not a sustainable baseline or guaranteed return. At five blocks per second, compounding 5% each block would imply `1.05^5 - 1 = 27.63%` per second. Execution must remain positive-net-PnL and revert/skip otherwise.

## 20% reserve withdrawal and burn hypothesis

The V11 scheduler currently treats 20% of HardNAV as a reserve budget for competing atomic opportunities; it does not define a 20% pool-reserve burn.

- Proportional withdrawal of 20% from both sides of each CPMM leaves the spot price unchanged: `(0.8*y)/(0.8*x)=y/x`. It creates no new triangular price gap.
- It reduces pool depth and invariant `k` to `0.64k`; a fixed trade becomes 25% larger relative to reserves, increasing price impact.
- If withdrawn assets move to Treasury, consolidated NAV is unchanged and capital is merely reallocated.
- If hard assets are burned, consolidated NAV falls by the burned amount.
- One-sided/unequal withdrawal creates a price gap, but external arbitrage closes it by transferring value from the pool/LP to searchers, net of fees and gas. This is not free profit.

**Decision:** do not implement a blanket 20% hard-reserve withdrawal or burn. Test bounded, reversible reserve reallocation only where measured expected net external PnL is positive and minimum per-pool depth/health constraints remain satisfied.

## V9 AdaptiveMM findings

Source: `v9/src/AdaptiveMM.sol`; tests: `v9/test/V9.t.sol`.

- Emission policy ranges from 58% to 74.8%; buyback policy ranges from 2% to 60%, subject to state feedback.
- The V9 test asserts a gross-TVL multiple above 3.77x. Its denominator is net external flow and numerator is gross TVL growth; this is a liquidity/valuation multiple, not realized profit or NAV growth.
- The test explicitly checks `hardNav_after = 1 USDC + external_net_flow`. This means the internal MINT/SELL/BUY/BURN policy does not itself create HardNAV.
- `hardNav()` is USDC pool reserves plus controller USDC balance. It is not a complete combined NAV ledger for token holders, liabilities and external counterparties.

**Decision:** KEEP as an experimental price/inventory controller; DEVELOP accounting and out-of-sample tests. Do not promote its 3.77x TVL multiple as yield.

## V10/V11 graph settlement findings

Source: `v10/src/GraphArbHardNavEngine.sol`, `v10/src/MockExternalSettlement.sol`, `v10/test/V10GraphArb.t.sol`, `unified_revenue/allocator.py`, `block_revenue/scheduler.py`.

- V11 correctly rejects closed internal cycles as HardNAV-producing opportunities.
- The V10 demonstration uses a mock settlement venue with fixed $1 prices and pre-funded USDC. The mock can pay out USDC but does not model a live RFQ, finite executable depth beyond its prefund, price impact, venue fees, gas, MEV, stale quotes or counterparty risk.
- The test counts external USDC received as HardNAV gain, but does not value the RUBX/RUBZ inventory transferred to the mock counterparty in a combined NAV calculation. This proves a funded mock settlement path, not free or net economic profit.
- A production graph route must calculate: external USDC received minus fair value of tokens transferred, gas, funding premium, venue fees, slippage, MEV/tip and execution risk; only the realized positive residual increases combined NAV.
- V11 allocator ranks candidates by net-profit/capital ROI and greedily packs a budget. It does not maximize expected dollar NAV gain globally; it does not multiply profit by calibrated execution probability, and it lacks a multi-asset inventory-conflict model. Its `confidence` is only a threshold.
- The allocator uses float amounts and a fixed/default HardNAV budget; production requires integer token units, live balance snapshots, stale-state rejection, per-asset capital reservation and independent settlement receipts.

**Decision:** DEVELOP graph route with real RFQ/aggregator quotes and strict net-profit accounting. BLOCKED for production until external settlement is independently evidenced and the full portfolio NAV reconciles.

## V11 branch / PR evidence

PR #7: [V11 integrated block revenue + graph HardNAV engine](https://github.com/Shtenco/synergy_triangle_money_system/pull/7).

- 74 commits ahead of main; 5 commits behind; diverged; 56 changed files.
- All eight V5–V11/R&D PRs remain open drafts. Branch comparisons against main:

| PR | Branch | Ahead | Behind | Mergeable flag |
|---:|---|---:|---:|---|
| 1 | `experiment/hardnav-multiplier-v5` | 6 | 5 | false |
| 2 | `experiment/autonomous-borrower-hunter-v6` | 22 | 5 | false |
| 3 | `experiment/block-revenue-engine-v7` | 33 | 5 | false |
| 4 | `experiment/three-pool-market-maker-v8` | 13 | 5 | true |
| 5 | `experiment/adaptive-market-maker-v9` | 23 | 5 | true |
| 6 | `experiment/graph-arb-hardnav-v10` | 34 | 5 | true |
| 7 | `experiment/integrated-revenue-engine-v11` | 74 | 5 | false |
| 8 | `research/recursive-amm-v6-oracle-band` | 4 | 5 | true |

- V11's five observed PR-triggered workflow runs all concluded `failure`.
- Current main's latest observed EVM V3 push run also concluded `failure`.
- Downloading the latest main job log returned `BlobNotFound`; therefore the exact failure step is not independently inspectable in this pass.
- Earlier main runs succeeded on older SHAs; they do not certify current main or V11.

## Prioritized actions

1. **P0 — accounting:** build a single reconciled NAV ledger including all assets, liabilities, LP shares, trader inventory and external counterparties. Distinguish HardNAV, gross TVL and combined NAV.
2. **P0 — external settlement:** replace mock venue with live, bounded RFQ/aggregator quotes; verify actual token transfer and USDC receipt; calculate net PnL after fair value and all costs.
3. **P0 — CI:** repair V11 workflows, rerun on exact current head, preserve inspectable logs/artifacts; no merge while red.
4. **P1 — allocator:** optimize expected dollar NAV gain under multi-asset capital constraints; use calibrated execution probabilities and integer amounts; reject stale quotes and conflicting inventory.
5. **P1 — reserve experiment:** test 0%, 5%, 10%, 20% reversible reserve relocation with no burn first; only compare burn as a separate explicit loss scenario. Measure per-block NAV, pool depth, LVR, trader PnL and drawdown.
6. **P1 — safety:** enforce min reserves per pool, price bands, max price impact, max exposure, oracle freshness, per-block loss caps and emergency pause.

## Final classification

| Component | Decision | Reason |
|---|---|---|
| Main V5 collateral model | KEEP / REFERENCE | Explicit HardNAV vs productive-liquidity boundary; simulation/EVM lab only |
| V7 block revenue infrastructure | DEVELOP | Useful capital-allocation scaffold; not yet independently production-verified |
| V9 AdaptiveMM | DEVELOP | Controller test exists; TVL multiple is not yield |
| V10 graph engine | DEVELOP / BLOCKED | Mock external settlement does not prove real economic edge |
| V11 integrated allocator | DEVELOP / BLOCKED | Five failed CI runs; greedy ROI is not global expected-NAV optimizer |
| Blanket 20% reserve burn | REJECT | Destroys NAV; proportional removal creates no price gap |
| 5% every block | RESEARCH TARGET ONLY | Not supported by current evidence; cannot be promised or hard-coded |



## Cross-repository overlap — first-pass ownership decision

The current owner inventory contains several repositories implementing adjacent AMM, graph-arbitrage, HardNAV, flash-liquidity and market-execution functions. Do not merge repositories wholesale; consolidate by authority and versioned interfaces.

| Repository | Observed mainline / role | Overlap | Decision |
|---|---|---|---|
| synergy_graph_print_money | V7.4 graph economy; token-closed Base surrogate; exact pinned fork still not executable | Graph arbitrage, flash funding, external HardNAV settlement | **KEEP / DEVELOP as canonical graph-arbitrage research engine**; do not duplicate its token-level closure and settlement core in STM |
| synergy_triangle_money_system | V5 collateral core on main; V11 integrated candidate in draft PR #7 | Adaptive AMM, block allocator, graph HardNAV, borrower/flash revenue | **DEVELOP as block-level orchestrator and collateral/MM lab**; consume graph execution through an adapter after evidence gates |
| synergy_ai_financial_system | Research implementation of integer CPMM graph, USDT settlement, anti-MEV/orderflow and flash executor | Graph policy, flash execution, LP growth, orderflow auction, treasury | **KEEP / DEVELOP as contract/security research**; select audited primitives, avoid a second competing production revenue engine |
| synergy_agentic_ai_economy | Closed multi-market / DQN historical research; README reports strict OOS HardNAV result, with some synthetic-flow caveats | Economic simulation and NAV accounting, not identical on-chain execution | **KEEP as independent economic benchmark**; do not count internal GDP/turnover as HardNAV |
| synergy_2chain_qe | Cross-chain QE / arbitrage research and fork-oriented branches | Arbitrage, AMM, synthetic assets, bridge solvency | **DEVELOP / BLOCKED pending current fork and solvency evidence**; preserve research lineage |
| synergy_market_graph | Market graph and route signals | Graph path discovery and executable route planning | **DEVELOP as discovery/quote layer**; capacity and latency must be enforced in executable route valuation |
| synergy_market_maker / synergy_adaptive_engine | Strategy and adaptive-control candidates | Market-making and policy feedback | **KEEP as strategy modules**, but no duplicate authority over pool reserves or settlement |
| synergy_riskguard | Independent pre-trade/portfolio veto | Risk controls | **KEEP as independent risk authority** |
| synergy_trademux | Multi-venue execution planning | Route slicing and venue execution | **KEEP as execution adapter**, paper fills are not real fills |
| synergy_relative_value | Relative-value signal research | Signal generation | **KEEP as non-authorizing research producer** |

### Recommended authority map

    synergy_market_graph          -> route discovery / capacity-aware quote candidates
    synergy_relative_value        -> research signals (no execution authority)
    synergy_graph_print_money     -> token-closed graph-arbitrage + external settlement
    synergy_triangle_money_system -> per-block opportunity allocator + adaptive AMM / collateral
    synergy_riskguard             -> independent ALLOW / RESIZE / DENY / KILL
    synergy_trademux              -> bounded execution plan and fill evidence
    synergy_ai_financial_system   -> audited contract primitives / anti-MEV research
    synergy_agentic_ai_economy    -> independent economic simulation benchmark

### Highest-value integration gate

Before merging or deploying any overlapping engine, define one versioned Opportunity / ExecutionReceipt / SettlementReceipt contract with:
- exact source and head SHA;
- chain ID, block number and block hash;
- token-by-token input/output and repayment;
- pre/post pool reserves and trader inventory;
- independent fair-value source and quote age;
- gas, funding premium, MEV/tip, fees and slippage;
- realized net PnL and consolidated NAV delta;
- unique transaction hash and replay protection.

Only one module may own execution and settlement authority for a given route. Other repositories provide candidates, risk decisions or evidence—not parallel execution rights.
