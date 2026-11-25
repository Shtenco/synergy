# Credential and Live-Execution Response Playbook

This playbook contains no secret values. Treat any credential committed to a repository as compromised, even if the file was later deleted.

## Immediate containment
1. Disable affected deployment workflows and live execution adapters.
2. Revoke/rotate exposed SSH keys, wallet/deployer keys, broker credentials, API passwords, bearer tokens and webhook secrets at the issuing provider.
3. Verify old credentials no longer authenticate; inspect access, deployment and transaction logs for the exposure window.
4. Move replacement secrets to an approved secret manager or protected CI secret store. Never place them in source, sample configs or artifacts.
5. Remove tracked secret files and sanitize Git history only after rotation, with coordinated force-push and downstream clone handling.
6. Enable GitHub secret scanning and push protection; add a repository-wide secret policy and CI scan.
7. Record provider-side revocation evidence, rotation timestamp, affected principal, repository and reviewer in a restricted incident record. Do not commit secret values or private-key fingerprints to this public graph.

## Trading execution containment
- Set live execution to disabled by default.
- Use isolated demo accounts until execution paths, account identity, notional caps, daily loss caps, kill switch and operator approval are tested.
- Treat `accepted`, `submitted` and `filled` as separate states; only broker/provider acknowledgements can establish submission/fill.
- A risk veto must return a non-tradable result and must never invoke an execution adapter.
