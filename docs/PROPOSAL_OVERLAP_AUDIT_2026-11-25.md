# SYNERGY proposal overlap audit — 2026-11-25

## Scope

This audit compares all 39 proposed components against the inspected main-branch implementations and contracts of existing SYNERGY repositories. It does not claim that every listed repository has been fully tested. Each assessment cites exact commits and file blob SHAs in `hypergraph/architecture/overlap-matrix.json`.

## Decisions

| Proposal | Finding | Decision |
|---|---|---|
| `synergy_offer_protocol` | Generic event envelope and economic records exist; no offer-specific contract | Extend canonical contracts in `synergy_system`; no new repository |
| `synergy_ai_pricing_engine` | Market rates/fees and typed money exist; no general commercial pricing policy | Reuse primitives; defer engine extraction |
| `synergy_transaction_orchestrator` | META API has bounded read-only workflows; Pay System handles payment settlement | No competing authority; define durable order saga in the commercial owner |
| `synergy_ai_skills_marketplace` | Tool/MCP discovery exists; commercial skill packages, rights, reviews and royalties do not | Distinct domain; defer until skill manifest and licensing contracts exist |
| `synergy_ai_tutors` | App catalog only; no tutoring runtime | Combine into one education vertical |
| `synergy_ai_courses` | App catalog only; no course delivery/enrolment runtime | Combine with tutoring; no separate repo initially |
| `synergy_ai_video_router` | Generic API discovery only; no video job/provider lifecycle | Distinct vertical; defer pending provider contracts |
| `synergy_ai_advertising_router` | Lead discovery/CRM review exists; ad campaign orchestration does not | Distinct from Lead OS; defer pending platform adapters and attribution |
| `synergy_ai_seo_router` | Existing search projects cover HardNAV simulation and lead discovery, not SEO operations | Distinct vertical; defer pending crawler/rank/SEO contracts |
| `synergy_ai_coupon_router` | Payment routing exists; coupon inventory/redemption does not | Distinct vertical; defer pending merchant and redemption model |
| `synergy_ai_logistics_router` | Maps supplies geospatial context; no carrier/shipment execution | Reuse Maps; defer logistics-specific service |
| `synergy_ai_legal_router` | Lead OS has human review and lawful-contact gates; no lawyer registry or legal case routing | Distinct high-stakes vertical; require jurisdiction and credential contracts |

## Important boundaries

- `synergy_meta_api` OpenAPI registration is an in-memory prototype and is explicitly non-executable; public catalog lookup is read-only.
- `synergy_meta_api.workflow` runs bounded local allowlisted tools. It is not a durable order saga.
- `synergy_pay_system` provides payment quotes, routing and settlement; its provider registry is not a bank/merchant/coupon catalogue.
- `synergy_market_graph` computes indicative graph rates and cycles; it does not prove executable commercial arbitrage or generalized dynamic pricing.
- `synergy_maps` is a geospatial layer, not a carrier marketplace.
- `synergy_lead_search_engline` is a local-first lead discovery/review workflow, not advertising execution, SEO or legal advice.
- `synergy_apps` has an application catalog design and read models, not an education runtime.

## Repository creation decision

No new repository is approved by this audit. Build the missing contracts and vertical scope in existing authoritative domains first. A new repository should be proposed only when it has a unique owner, an executable boundary, a versioned API/event contract, tests, security/compliance gates and a measurable reason not to extend an existing canonical owner.

## Coverage

- Proposed components: 39
- Assessed with pinned evidence: 39
- Remaining unaudited proposals: 0
- Runtime integrations proven by this proposal audit: 0
