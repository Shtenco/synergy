# Integration Contract

## Goal

Every SYNERGY repository should be discoverable and operable as a module of the wider ecosystem without copying its source into the umbrella repository.

## Minimum module metadata

Each child repository should eventually expose:

- module name and purpose;
- owner / responsible agent or department;
- runtime type: service, library, app, model, protocol, research;
- inputs / outputs;
- dependencies;
- API or event contracts;
- health / CI status;
- release/version;
- security classification;
- current maturity stage.

## Preferred coupling order

1. API or message/event contract.
2. Versioned package.
3. Versioned build/model artifact.
4. Git submodule only when source pinning is unavoidable.

## NEXUS / Autopilot use

`registry/repos.json` is the canonical discovery seed. NEXUS can enrich this into a capability graph with:

`repository -> capabilities -> interfaces -> dependencies -> runtime nodes -> agents -> tasks`.

## Security

Never centralize secrets in this umbrella. Secrets remain in each repository/runtime secret store.
