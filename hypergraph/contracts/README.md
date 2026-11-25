# Hypergraph Contracts

This directory is reserved for versioned, executable cross-repository contracts.

## Accepted artifacts
- OpenAPI 3.x documents for HTTP APIs.
- JSON Schema for event envelopes and payloads.
- AsyncAPI documents for broker topics and delivery semantics.
- Compatibility fixtures and consumer/provider contract tests.

## Promotion rule
A proposed edge such as `CALLS`, `CONSUMES`, `PROVIDES`, `DELIVERY_GUARDED_BY` or `SETTLES_THROUGH` is not verified by a README statement alone. Store the contract artifact, source revision, evidence file/line references, test command and observed result. Mark an edge `verified` only after a reproducible consumer/provider contract test or runtime integration test passes.

No cross-repository API contract is currently claimed as verified by Hypergraph V3.
