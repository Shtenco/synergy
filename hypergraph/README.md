# SYNERGY Hypergraph Core — V3

Machine-readable repository inventory, evidence-aware dependency graph and target architecture for the ecosystem audit.

## Current snapshot
- 112 repository nodes keyed by immutable GitHub repository IDs (100 search results on page 1, 12 on page 2).
- 109 registry-declared `DEPENDS_ON` edges, all `candidate`; zero verified runtime edges.
- Sixty-four README reviews and fifty-three limited source reviews, each pinned to the exact main commit and file blob SHA.
- 39 proposed shared cores and domain routers are kept separate from actual repositories; 27 have first-pass overlap assessments and 12 remain unaudited.
- Six target architecture layers and twenty-eight candidate target relationships are documented separately from observed dependencies.

## Files
- `nodes.json`: 112 repository nodes and per-repository audit status.
- `edges.json`: registry-declared dependency edges; every edge remains `candidate` until source evidence verifies it.
- `architecture/target-graph.json`: six-layer target graph and candidate architecture links.
- `architecture/ownership-map.json`: canonical owners and integration direction; avoids duplicate core repositories.
- `architecture/overlap-matrix.json`: first-pass overlap review for proposed shared cores.
- `coverage.json`: measurable inventory and audit coverage.
- `gaps.json`: unresolved source audit, security, evidence, contract and overlap gaps.
- `proposals.json`: 39 proposed components, not actual repositories.
- `evidence/registry-snapshot.json`: provenance for the original 92-record registry snapshot.
- `evidence/repository-audits.json`: twelve commit-pinned repository reviews.
- `contracts/`: requirements for versioned OpenAPI, JSON Schema, AsyncAPI and contract tests.
- `security/RESPONSE_PLAYBOOK.md`: credential rotation and live-execution containment without secret material.
- `schemas/`: JSON Schema contracts for repository nodes and n-ary hyperedges.

## Current findings
1. `synergy_system` has a stale 92-repository snapshot; its federation authority and contract registry remain canonical. The current main branch of hierarchical cognitive memory contains commit-pinned dependency and cross-repository intelligence, contrary to the older README-only claim.
2. `synergy_ai_browser-`: the Playwright route guard checks top-level document navigation, but continues subresource requests without equivalent host/IP checks. Treat as a high-priority potential SSRF/private-network exposure until fixed and tested.
3. `timeweb_synergy_service_recovery`: inspected recovery scenario is an in-memory simulator, while README describes local HTTP/SQLite restarts. Evidence scope must be reconciled.
4. `timeweb_synergy_cpu_gpu_cost_benchmark`: inspected code is an assumption-based cost calculator; a GPU benchmark harness and paid cloud evidence were not found in the inspected tree.
5. `timeweb_synergy_retry_storm_lab`: the protected policy reached 32.92% median success versus 56.25% for retry-budget plus bulkhead in its fixed localhost fault model. This is a configuration/granularity warning, not a general verdict on circuit breakers.
6. `timeweb_synergy_benchmark_statistics`: archived UCI digits results show binary model accuracy 88.81% versus FP32 95.85% over three paired seeds; uncertainty is exploratory and fixed-test-set limitations apply.

7. `synergy_meta_os`: compatibility runtime uses POSIX resource limits but is not a complete filesystem/network/namespace sandbox.
8. `synergy_meta_api`: V0.1 gateway keeps connector execution disabled by default until authentication is implemented.
9. `synergy_market_graph`: current fair-value graph is advisory and does not apply capacity/latency constraints.

10. `synergy_financial_os` recognition helper has an optional settlement evidence parameter and accepts empty balanced entries; `synergy_pay_system` settlement idempotency is process-local; `synergy_riskguard` treats fewer than five returns as zero VaR/CVaR.

11. `synergy_lead_search_engline` is an offline real-estate lead candidate store with human review, not a deployed multi-tenant crawler; current schema lacks tenant isolation.
12. `synergy_search_engline` is a HardNAV simulation, not a general search service.
13. `synergy_messenger` main branch has a manifest whose scripts reference missing source/test paths; the alpha runtime is not verified on main.
14. `synergy_ai_workspace` implementation exists only on a release branch; main remains README-only.

15. `synergy_algotrading_graph_system` is a README-only architecture specification; executable graph models already exist in `synergy_market_graph` and `synergy_ai_financial_system`.
16. Relative-value and MIDAS institutional outputs are advisory/non-authorizing and must pass canonical RiskGuard validation.

17. `synergy_usds` and `synergy_cashero` contain tracked key/environment artifacts that require credential rotation review; `synergy_turbo_linux` has a documented historical unencrypted SSH private-key incident with revocation not yet evidenced.
18. `synergy_metachain` replay protection is process-local and does not verify chain proofs.
19. `synergy_computing_topology` has archived correctness results, but kernel runtime on the current host was not tested.

20. QuantLab is the validation authority; MIDAS AI is a target canonical advisory-contract layer; Market Maker and MarketVision are non-authorizing signal/feature producers.
21. Market Maker quotes and MIDAS institutional assessments are not broker orders; canonical RiskGuard and Financial OS remain separate authorities.

22. MIDAS AI Trading System main has a broken Risk Veto exception path, unauthenticated log/metrics WebSockets, a VaR/CVaR sign mismatch and non-persistent archive chain state.
23. `midas_lite` contains direct MT5 order submission in a legacy agent; `synergy_ai_trade_terminal` contains embedded credentials. Keep execution disabled and rotate credentials.
24. `synergy_usds`, `synergy_cashero` and `synergy_turbo_linux` have tracked or historical credential exposure findings. The security playbook records containment steps without storing secret material.

25. AI Language's multi-target code generator interpolates unescaped strings for C/Rust/Solidity/Kotlin; command execution is not an OS sandbox and trace output is not secret-redacted.
26. GLLM runtime and RWKV quantization code are branch-only; neither should be described as default-main functionality or production-ready model runtime.
27. Matrix SOTA is a documentation-only debt/credit maturity design, not an executable credit engine.

28. `synergy_qr_compress` is a shared-model temporal dictionary/patch codec; zero residual is only meaningful after amortizing dictionary storage and distribution.
29. `synegy_ai_compress` is a benchmark dossier whose engine source is a gitlink without `.gitmodules`; exact source retrieval is not reproducible from the repository alone.
30. `synergy_gguf_compress` and `synergy_shhts` are documentation-only on main.

## Evidence rules
1. Repository names are not identities; GitHub repository IDs are.
2. A registry dependency is a candidate edge, not proof of an import or runtime call.
3. `candidate`, `reviewed`, `verified`, and `rejected` are distinct states. `verified` requires reproducible source or runtime evidence.
4. Proposed components are not repository inventory entries.
5. Hashes establish byte identity, not truth, authorization or correctness.
6. No tests were executed as part of the current repository review; archived results are not fresh CI runs.
7. Existing implementation boundaries: `synergy_system` owns governance/contracts; hierarchical cognitive memory owns static dependency and cross-repository evidence intelligence; Hypergraph V3 is a projection/read model, not a new competing runtime or repository.

## Coverage
- Inventory: 112/112 unique IDs returned by owner-scoped search.
- README reviewed: 64/112 (57.14%).
- Source reviewed (limited scope): 53/112 (47.32%).
- Dependency edges verified: 0/109.
- Cross-repository contracts verified: 0.

## Next audit sequence
1. Close the browser subresource network-policy finding.
2. Audit the remaining 59 repositories in small batches: manifests, imports, API routes, event schemas, tests and workflows.
3. Replace registry-only candidate edges with source-pinned evidence.
4. Extract contracts and validate compatibility.
5. Run capability-overlap analysis before proposing any new repository.
