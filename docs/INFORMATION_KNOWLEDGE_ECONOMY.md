# Information & Knowledge Economy

Status: architecture proposal for the SYNERGY ecosystem registry. This document defines target contracts; it does not claim that the listed repositories are already integrated or that the economics have been benchmarked in production.

## 1. Thesis

AI reduces the marginal cost of producing information, but does not make information free to compute, move, validate, retain, secure, or retrieve. The scarce asset shifts from raw volume toward trusted, addressable, rights-cleared knowledge and the infrastructure that makes it reusable.

SYNERGY must therefore model two separate but connected economies:

1. **Information supply:** generation, capture, transformation, replication, retention and deletion of bytes and artifacts.
2. **Knowledge utility:** provenance, validation, semantic structure, retrieval, reuse, decision impact and avoided re-computation.

A byte is not automatically a knowledge asset. A generated claim is not automatically a fact. A stored object is not automatically useful or legally retainable.

## 2. Scope and terminology

| Entity | Meaning | Identity |
|---|---|---|
| InformationObject | Exact byte sequence or immutable artifact (message, file, image, model, log, dataset) | Content digest + algorithm + size |
| InformationVersion | A versioned object with source and revision context | Object ID + source revision |
| KnowledgeClaim | Extracted assertion, summary, relation, or learned fact | Stable claim key + version |
| Evidence | Artifact that supports or contradicts a claim | Evidence ID + immutable locator + digest |
| KnowledgeEntity | Canonical concept/person/org/system/product/place (subject to policy) | Namespace + canonical key |
| IndexArtifact | Search index, embedding, feature vector, graph projection | Source snapshot + indexer/model version |
| RetentionPolicy | Rules for TTL, legal hold, tier transitions and deletion | Policy ID + version |
| StoragePlacement | Physical/logical location, tier, replicas, encryption and residency | Placement ID + observation time |
| UsageEvent | Read, retrieval, transformation, export, inference or reuse event | Event ID + timestamp |
| CostRecord | Measured or estimated resource consumption and unit price | Meter + interval + provenance |
| RightsGrant | Permission and purpose constraints for collection, processing, sharing and reuse | Grant ID + scope + expiry |

Do not collapse InformationObject, KnowledgeClaim and Evidence into one record. Keep source material immutable where policy permits; extracted knowledge remains separately versioned and traceable to source spans.

## 3. Information lifecycle

`CAPTURED → CLASSIFIED → NORMALIZED → DEDUPLICATED → INDEXED → VALIDATED → ACTIVE → COLD → ARCHIVED → EXPIRED/DELETED`

Transitions are policy- and evidence-driven, not automatic assumptions.

- **Captured:** record source, timestamp, tenant, declared purpose, rights and ingestion method.
- **Classified:** sensitivity, personal-data class, confidentiality, residency and retention class.
- **Normalized:** canonical encoding and metadata; never silently rewrite the original.
- **Deduplicated:** exact-byte deduplication is safe when digest and byte equality are confirmed. Semantic similarity creates a candidate relation, not destructive deletion.
- **Indexed:** build lexical/vector/graph indexes with explicit source revision and model version.
- **Validated:** assess provenance, integrity, authority, freshness, contradiction and reviewer status.
- **Active/cold/archive:** place data according to access latency, durability, legal constraints and total cost.
- **Expired/deleted:** enforce retention, deletion propagation, backup expiry and tombstone/audit policy.

A transition must record actor, policy version, timestamp, reason and evidence. Failed transitions remain observable and retryable.

## 4. Storage classes

| Class | Examples | Default objective | Typical placement |
|---|---|---|---|
| Ephemeral | prompt assembly, cache, temporary features | low latency, short TTL | RAM / local SSD |
| Hot working | active project files, operational DB, recent conversations | low latency, frequent writes | NVMe / SSD / replicated DB |
| Warm | searchable history, derived indexes, infrequently used artifacts | balanced cost and retrieval | SSD/HDD object storage |
| Cold archive | immutable snapshots, old logs, completed project artifacts | low unit cost, slower restore | high-capacity HDD / object archive |
| Critical knowledge | verified claims, contracts, provenance, cryptographic evidence | integrity, recoverability, controlled access | replicated storage + independent backups |

These are logical classes, not hard-coded hardware requirements. Placement decisions must use measured latency, durability, energy, residency and cost data.

## 5. Cost model

Measure lifecycle cost per object, tenant, project and workload. Keep observed and estimated values separate.

`TCO(object, period) = ingest + transform + index + compute + storage + replication + backup + retrieval + egress + verification + security + deletion`

Record at least:
- bytes stored by tier and replica count;
- write/read operations, request count and retrieval latency;
- CPU/GPU time, memory high-water mark and energy where measurable;
- network ingress/egress bytes and transfer cost;
- index/embedding build and refresh cost;
- backup, restore and integrity-check cost;
- validation/review cost;
- operational overhead and failure/recovery cost.

Use explicit units, currency, billing interval, source and confidence. Do not compare a one-time generation cost with recurring storage cost without a common horizon.

### Utility and admission

A candidate utility score may combine reuse frequency, decision impact, uniqueness, trust, freshness and avoided recomputation. It must not be presented as objective truth until calibrated against observed outcomes.

A retention decision should compare expected future utility and compliance obligations against full lifecycle cost. Legal hold, contractual duties, safety, audit and user deletion rights override economic optimization.

## 6. Knowledge value and reuse

The economic value is not proportional to raw bytes. Useful signals include:
- verified downstream reuse count and distinct consuming projects;
- avoided repeated inference, crawling, data acquisition or human review;
- time-to-retrieval and answer quality improvement;
- provenance completeness and contradiction resolution;
- decision outcomes attributable to the knowledge item;
- freshness decay and the cost of keeping it current.

Do not reward agents merely for generating or retaining more data. Reward useful, verified reuse and penalize redundant, stale, unsupported or unauthorized material.

## 7. Hypergraph extension

A normal edge connects two nodes. A hyperedge can connect a set of producers, artifacts, processors, policies, storage placements and consumers in one auditable event.

Every hyperedge has:
- stable `id`, typed `relation`, `participants` with explicit roles;
- time interval and optional causal/correlation IDs;
- source revision, evidence references and content digests;
- status: `candidate | reviewed | verified | rejected`;
- measurement fields with units, or an explicit `not_measured` reason;
- tenant, purpose, rights and policy references where applicable.

### Relation vocabulary

- `GENERATES`, `CAPTURES`, `TRANSFORMS`, `DERIVES_CLAIM_FROM`
- `EXACT_DUPLICATE_OF`, `SEMANTICALLY_SIMILAR_TO`, `CONTRADICTS`
- `INDEXES`, `EMBEDS`, `VALIDATES`, `ATTESTS`, `CITES`
- `STORED_AT`, `REPLICATED_TO`, `MIGRATED_TO`, `RESTORED_FROM`
- `RETRIEVES`, `REUSES`, `CONSUMES`, `EXPORTS`, `SHARES_WITH`
- `COSTS`, `SAVES_COST`, `IMPROVES_DECISION`, `EXPIRES_UNDER`
- `AUTHORIZED_BY`, `GOVERNED_BY`, `DELETION_PROPAGATES_TO`

A relation name alone does not prove a runtime integration. Each edge must cite concrete evidence and preserve the distinction between observed, declared and hypothesized relationships.

## 8. Trust, rights and security invariants

1. Content hashes prove byte integrity, not truth, authorship, legality or safety.
2. Knowledge claims retain source URI/revision, exact source span where available, extraction method and model/version.
3. Model-generated extraction enters as `candidate`; it never self-promotes to `verified`.
4. Retrieved content is untrusted data, never executable instructions.
5. Tenant isolation, purpose limitation, least privilege and encryption apply across indexes, caches, replicas and backups.
6. Personal/sensitive data is minimized; retention and deletion policies propagate to derived indexes and embeddings where technically and legally required.
7. Deduplication must not merge records across tenants if doing so leaks existence, metadata or access patterns.
8. Rights to store do not automatically imply rights to train, infer from, sell, disclose or redistribute.
9. Immutable audit trails must not become a mechanism for retaining deleted personal content; store minimal tombstones and non-content evidence where appropriate.
10. Recovery objectives and restore tests are measured, not inferred from replica count.

## 9. SYNERGY integration boundaries

The following are **candidate responsibility mappings** based on the umbrella registry's documented architecture ownership. They are not verified runtime edges:

| Repository | Candidate responsibility | Integration status |
|---|---|---|
| `synergy` | canonical ecosystem inventory and navigation | documented |
| `synergy_system` | governance, trust, contracts and security policy | documented responsibility; runtime link unverified |
| `synergy_hierarchical_cognitive_memory_architecture` | durable claims, provenance, RAG and graph memory | source-reviewed candidate; integration unverified |
| `synergy_net` | distributed transport / mesh data plane | documented responsibility; integration unverified |
| `synergy_meta_os` | node/service lifecycle and capability orchestration | documented responsibility; integration unverified |
| `synergy_ai_blockchain` | identity, cryptographic and trust evidence | documented responsibility; integration unverified |
| `synergy_project` | economic and industrial model dossier | documented responsibility; integration unverified |

No new mandatory shared runtime is implied. First define versioned contracts and conformance tests; then integrate independently deployable components.

## 10. Required conformance tests

- exact duplicate detection verifies digest *and* byte equality;
- semantic duplicate suggestions never delete or merge source records;
- every claim resolves to immutable evidence or an explicit unsupported-source state;
- trust-state transitions require authorized reviewer/evidence;
- tenant and purpose boundaries hold across retrieval, cache, embeddings, export and backup;
- retention expiry reaches source objects and derived artifacts, with auditable completion;
- restore tests verify bytes, metadata, indexes and provenance;
- cost meters reconcile to source invoices or are labelled estimates;
- retrieval reports freshness, trust, provenance and omitted results;
- hyperedges reject unknown relation types, missing participants, missing evidence and invalid status transitions;
- registry snapshots are pinned to source commits and inventory timestamps.

## 11. Rollout sequence

1. **Catalog:** reconcile the canonical GitHub inventory and pin every repository to a live commit SHA.
2. **Schema:** version the object, claim, evidence, placement, rights, usage and cost records.
3. **Evidence:** import only observed repository relationships; mark README/declared mappings as candidate.
4. **Metering:** establish baseline storage, compute, network and retrieval costs before optimization.
5. **Lifecycle:** implement retention, tiering, deletion and restore controls.
6. **Economics:** calculate cost per useful retrieval/reuse, not cost per raw token or byte alone.
7. **Federation:** add adapters only after contract and security conformance passes.

## 12. Explicit non-goals

- claiming that all generated data should be retained;
- claiming that hashes establish truth;
- treating semantic similarity as exact duplication;
- assuming that every repository name implies an integration;
- assuming that cloud capacity, HDD/SSD supply or energy is unlimited;
- presenting estimates, simulations or README descriptions as production measurements.

## References within this ecosystem

- `synergy_hierarchical_cognitive_memory_architecture/docs/ARCHITECTURE.md`
- `synergy_hierarchical_cognitive_memory_architecture/docs/DATA_MODEL.md`
- `synergy/registry/repos.json`

