from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HYPERGRAPH = ROOT / "hypergraph"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


class HypergraphCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodes_doc = load_json(HYPERGRAPH / "nodes.json")
        cls.edges_doc = load_json(HYPERGRAPH / "edges.json")
        cls.coverage = load_json(HYPERGRAPH / "coverage.json")
        cls.gaps = load_json(HYPERGRAPH / "gaps.json")
        cls.proposals = load_json(HYPERGRAPH / "proposals.json")
        cls.target = load_json(HYPERGRAPH / "architecture" / "target-graph.json")
        cls.overlap = load_json(HYPERGRAPH / "architecture" / "overlap-matrix.json")
        cls.audit = load_json(HYPERGRAPH / "evidence" / "repository-audits.json")
        cls.governance = load_json(HYPERGRAPH / "evidence" / "governance-registry-snapshot.json")
        cls.governance_projection = load_json(HYPERGRAPH / "governance-edges.json")
        cls.scope_manifest = load_json(HYPERGRAPH / "evidence" / "governance-scope-manifest.json")
        cls.governance_projection_schema = load_json(HYPERGRAPH / "schemas" / "governance-graph-projection.schema.json")
        cls.registry = load_json(ROOT / "registry" / "repos.json")

    def test_inventory_has_112_unique_provider_ids(self):
        nodes = self.nodes_doc["nodes"]
        ids = [node["github_repository_id"] for node in nodes]
        self.assertEqual(len(nodes), 112)
        self.assertEqual(len(set(ids)), 112)
        self.assertEqual(len(self.registry["repositories"]), 112)
        registry_ids = [row["github_repository_id"] for row in self.registry["repositories"]]
        self.assertEqual(set(ids), set(registry_ids))

    def test_dependency_edges_are_candidate_and_referentially_valid(self):
        nodes = {node["node_id"] for node in self.nodes_doc["nodes"]}
        edges = self.edges_doc["edges"]
        self.assertEqual(len(edges), 109)
        self.assertEqual(self.edges_doc["verified_edge_count"], 0)
        self.assertTrue(all(edge["status"] == "candidate" for edge in edges))
        for edge in edges:
            self.assertGreaterEqual(len(edge["participants"]), 2)
            for participant in edge["participants"]:
                self.assertIn(participant["node_id"], nodes)
            for evidence in edge["provenance"]:
                self.assertRegex(evidence["source_revision"], r"^[0-9a-f]{40}$")
                self.assertRegex(evidence["evidence_digest"]["value"], r"^[0-9a-f]{40}$")

    def test_audit_provenance_is_pinned_and_consistent(self):
        node_by_name = {node["name"]: node for node in self.nodes_doc["nodes"]}
        records = self.audit["records"]
        self.assertEqual(len(records), self.audit["audit_record_count"])
        self.assertEqual(len({record["name"] for record in records}), self.audit["audited_repository_count"])
        self.assertEqual(self.audit["source_code_reviewed_count"], self.coverage["audit"]["source_code_reviewed_total"])
        latest_by_name = {record["name"]: record for record in records}
        for record in records:
            self.assertRegex(record["commit"], r"^[0-9a-f]{40}$")
            self.assertIn(record["name"], node_by_name)
            for file_record in record.get("files", []):
                if "blob_sha" in file_record:
                    self.assertRegex(file_record["blob_sha"], r"^[0-9a-f]{40}$")
                if "gitlink_commit" in file_record:
                    self.assertRegex(file_record["gitlink_commit"], r"^[0-9a-f]{40}$")
        for name, record in latest_by_name.items():
            self.assertEqual(node_by_name[name]["source_audit"]["commit"], record["commit"])

    def test_coverage_matches_review_ledger(self):
        reviewed = sum(
            1 for node in self.nodes_doc["nodes"]
            if node["audit_status"] in {"source_reviewed_limited", "branch_only_prototype"}
        )
        self.assertEqual(reviewed, self.coverage["audit"]["source_code_reviewed_total"])
        self.assertEqual(self.coverage["audit"]["source_code_audited_total"], reviewed)
        self.assertEqual(reviewed, len(self.coverage["audit"]["source_code_reviewed_repository_names"]))
        self.assertAlmostEqual(
            self.coverage["completion_percentages"]["repository_source_audit"],
            round(reviewed / 112 * 100, 2),
        )
        self.assertEqual(self.coverage["audit"]["readme_reviewed_total"], self.audit["audited_repository_count"])
        self.assertAlmostEqual(
            self.coverage["completion_percentages"]["readme_review"],
            round(self.audit["audited_repository_count"] / 112 * 100, 2),
        )

    def test_every_inventory_node_has_commit_pinned_content_audit(self):
        node_names = {node["name"] for node in self.nodes_doc["nodes"]}
        audit_names = {record["name"] for record in self.audit["records"]}
        self.assertEqual(node_names, audit_names)
        self.assertEqual(self.audit["audited_repository_count"], 112)
        self.assertEqual(self.audit["content_reviewed_repository_count"], 112)
        self.assertEqual(self.audit["audit_record_count"], len(self.audit["records"]))
        latest = {record["name"]: record for record in self.audit["records"]}
        for node in self.nodes_doc["nodes"]:
            record = latest[node["name"]]
            self.assertEqual(node["source_audit"]["commit"], record["commit"])
            self.assertEqual(node["source_audit"]["status"], record["status"])

    def test_documentation_dossiers_are_not_counted_as_executable_source(self):
        executable = sum(
            1 for node in self.nodes_doc["nodes"]
            if node["audit_status"] in {"source_reviewed_limited", "branch_only_prototype"}
        )
        self.assertEqual(executable, 106)
        self.assertEqual(self.coverage["audit"]["executable_source_reviewed_total"], 106)
        self.assertEqual(self.coverage["audit"]["content_reviewed_repository_total"], 112)
        self.assertEqual(self.coverage["audit"]["non_code_content_reviewed_in_this_pass"], 6)
        self.assertAlmostEqual(
            self.coverage["completion_percentages"]["repository_source_audit"],
            round(106 / 112 * 100, 2),
        )
        self.assertEqual(
            self.coverage["completion_percentages"]["repository_content_audit"], 100
        )

    def test_governance_registry_subset_is_explicit_and_counts_are_not_conflated(self):
        snapshot = self.governance
        counts = snapshot["counts"]
        reconcile = snapshot["reconciliation"]
        inventory = {node["full_name"] for node in self.nodes_doc["nodes"]}
        self.assertEqual(counts["authority_registry_entries"], 42)
        self.assertEqual(counts["contract_registry_entries"], 39)
        self.assertEqual(counts["dependency_graph_nodes"], 75)
        self.assertEqual(counts["dependency_graph_edges"], 136)
        self.assertEqual(counts["repository_interface_records"], 77)
        self.assertEqual(reconcile["hypergraph_inventory_repositories"], 112)
        self.assertEqual(len(reconcile["hypergraph_names_missing_from_interface_registry"]), 35)
        self.assertEqual(len(reconcile["hypergraph_names_missing_from_dependency_graph"]), 37)
        self.assertEqual(reconcile["interface_only_names_not_in_dependency_graph"], [
            "Shtenco/synergy_hierarchical_cognitive_memory_architecture",
            "Shtenco/synergy_long_term_harness",
        ])
        self.assertEqual(counts["dependency_graph_edge_type_counts"], {
            "ARCHITECTURAL_PARENT": 70,
            "CONTRACT_FLOW": 22,
            "RUNTIME_DEPENDENCY": 22,
            "RUNTIME_CONTRACT": 22,
        })
        self.assertEqual(counts["dependency_graph_summary"]["adapter_implemented_runtime_edges"], 22)
        self.assertEqual(counts["m5_required_runtime_edges"], 44)
        self.assertEqual(counts["m5_observed_execution"]["status"], "BLOCKED_BY_RUNNER")
        self.assertEqual(counts["m5_observed_execution"]["verified_runtime_edges"], 0)
        self.assertEqual(counts["dependency_graph_summary"]["e2e_tested_runtime_edges"], 0)
        self.assertEqual(counts["dependency_graph_summary"]["deployed_runtime_edges"], 0)
        self.assertTrue(set(reconcile["interface_registry_repository_names"]).issubset(inventory))
        self.assertTrue(set(reconcile["dependency_graph_repository_names"]).issubset(inventory))

    def test_governance_graph_projection_preserves_canonical_edges(self):
        projection = self.governance_projection
        counts = projection["counts"]
        nodes = {node["node_id"] for node in self.nodes_doc["nodes"]}
        projected_nodes = {node["node_id"] for node in projection["nodes"]}
        self.assertEqual(counts["nodes"], 75)
        self.assertEqual(counts["edges"], 136)
        self.assertEqual(len(projected_nodes), 75)
        self.assertTrue(projected_nodes.issubset(nodes))
        self.assertEqual(counts["unique_contract_ids"], 38)
        self.assertEqual(counts["m5_required_edges"], 44)
        self.assertEqual(counts["e2e_tested_edges"], 0)
        self.assertEqual(counts["deployed_runtime_edges"], 0)
        self.assertEqual(counts["edge_type_counts"], {
            "ARCHITECTURAL_PARENT": 70,
            "CONTRACT_FLOW": 22,
            "RUNTIME_DEPENDENCY": 22,
            "RUNTIME_CONTRACT": 22,
        })
        self.assertEqual(counts["edge_status_counts"], {
            "DOCUMENTED": 70, "ADAPTER_IMPLEMENTED": 66
        })
        self.assertEqual(counts["m5_edge_type_counts"], {
            "RUNTIME_DEPENDENCY": 22, "RUNTIME_CONTRACT": 22
        })
        self.assertEqual(sum(edge["in_m5_required_scope"] for edge in projection["edges"]), 44)
        for edge in projection["edges"]:
            self.assertIn(edge["source_node_id"], projected_nodes)
            self.assertIn(edge["target_node_id"], projected_nodes)
            self.assertIn(edge["source_node_id"], nodes)
            self.assertIn(edge["target_node_id"], nodes)
        self.assertEqual(projection["source"]["commit"], "f1183d54121c3bbc558e4a171ddbba20973f8520")
        projection_schema = self.governance_projection_schema
        self.assertEqual(
            projection_schema["properties"]["projection_type"]["const"],
            "read_only_governance_graph_projection",
        )
        self.assertEqual(set(projection), set(projection_schema["properties"]))
        edge_schema_properties = projection_schema["properties"]["edges"]["items"]["properties"]
        for edge in projection["edges"]:
            self.assertTrue(set(edge).issubset(edge_schema_properties))

    def test_governance_scope_manifest_partitions_all_112_repositories(self):
        manifest = self.scope_manifest
        records = manifest["repositories"]
        nodes = {node["full_name"]: node for node in self.nodes_doc["nodes"]}
        self.assertEqual(len(records), 112)
        self.assertEqual({item["repository"] for item in records}, set(nodes))
        self.assertEqual(manifest["counts"], {
            "inventory_repositories": 112,
            "dependency_graph_and_interface": 75,
            "interface_only": 2,
            "absent_from_both": 35,
            "requiring_owner_scope_decision": 35,
        })
        for item in records:
            self.assertEqual(item["node_id"], nodes[item["repository"]]["node_id"])
            self.assertEqual(
                item["scope_review"],
                "present_in_canonical_registry"
                if item["in_dependency_graph"] or item["in_interface_registry"]
                else "needs_owner_scope_decision",
            )

    def test_m5_scope_aliases_and_contract_counts_reconcile(self):
        snapshot = self.governance
        counts = snapshot["counts"]
        contract = snapshot["contract_reconciliation"]
        m5 = snapshot["m5_scope_reconciliation"]
        self.assertEqual(counts["unique_contract_ids_in_dependency_graph"], 38)
        self.assertEqual(contract["registry_contract_count"], 39)
        self.assertEqual(contract["intra_repository_contracts_not_in_graph"], [
            "synergy.trading.execution-plan/v1"
        ])
        self.assertEqual(contract["stale_summary_value"]["reported"], 17)
        self.assertEqual(m5["required_edges"], 44)
        self.assertEqual(m5["exact_name_matches_to_dependency_graph"], 42)
        self.assertEqual(m5["legacy_alias_matches"], 2)
        self.assertEqual(m5["normalized_matches_to_dependency_graph"], 44)
        self.assertEqual(m5["unmatched_after_alias_normalization"], 0)
        self.assertEqual(m5["matched_edge_type_counts"], {
            "RUNTIME_DEPENDENCY": 22, "RUNTIME_CONTRACT": 22
        })
        self.assertEqual(m5["matched_status_counts"], {"ADAPTER_IMPLEMENTED": 44})

    def test_proposals_are_not_counted_as_repositories(self):
        actual_ids = {node["node_id"] for node in self.nodes_doc["nodes"]}
        proposal_ids = {proposal["proposal_id"] for proposal in self.proposals["proposals"]}
        self.assertEqual(len(proposal_ids), 39)
        self.assertFalse(actual_ids.intersection(proposal_ids))
        self.assertEqual(
            len(self.overlap["assessments"]) + len(self.overlap["remaining_proposals"]),
            39,
        )

    def test_all_proposals_have_overlap_assessments(self):
        proposal_names = {item["name"] for item in self.proposals["proposals"]}
        assessed_names = {item["proposal"] for item in self.overlap["assessments"]}
        self.assertEqual(proposal_names, assessed_names)
        self.assertEqual(len(self.overlap["assessments"]), len(proposal_names))
        self.assertEqual(self.overlap["remaining_proposals"], [])
        for assessment in self.overlap["assessments"]:
            self.assertTrue(assessment["decision"])
            for evidence in assessment.get("evidence", []):
                self.assertRegex(evidence["commit"], r"^[0-9a-f]{40}$")
                self.assertTrue(evidence["files"])

    def test_target_graph_links_resolve(self):
        target_ids = {node["node_id"] for node in self.target["nodes"]}
        for edge in self.target["edges"]:
            self.assertEqual(edge["status"], "candidate")
            for participant in edge["participants"]:
                self.assertIn(participant["node_id"], target_ids)

    def test_node_audit_statuses_are_schema_allowed(self):
        schema = load_json(HYPERGRAPH / "schemas" / "node.schema.json")
        allowed = set(schema["properties"]["audit_status"]["enum"])
        for node in self.nodes_doc["nodes"]:
            self.assertIn(node["audit_status"], allowed)

    def test_memory_api_auth_and_security_blocker_registry_freshness(self):
        by_id = {gap["id"]: gap for gap in self.gaps["gaps"]}
        memory = by_id["GAP-096"]
        self.assertEqual(memory["severity"], "high")
        self.assertIn("api.py is unchanged", memory["description"])
        self.assertIn("45475196929", memory["validation"])
        stale = by_id["GAP-097"]
        self.assertEqual(stale["severity"], "high")
        self.assertIn("CLOSED and unmerged", stale["description"])
        related = self.governance["related_branch_audits"][-1]
        self.assertEqual(related["pull_request"], 56)
        self.assertEqual(related["portfolio"]["live_repository_count"], 112)
        self.assertFalse(related["portfolio"]["full_source_review_complete"])
        self.assertEqual(related["registry"]["interface_records"], 77)
        self.assertEqual(related["registry"]["backlog_repository_count"], 77)

    def test_canonical_financial_integration_risks_are_explicit(self):
        by_id = {gap["id"]: gap for gap in self.gaps["gaps"]}
        self.assertEqual(
            by_id["GAP-093"]["severity"], "critical"
        )
        self.assertEqual(
            by_id["GAP-094"]["evidence"][0]["ref"],
            "federation-v3-domain-expansion",
        )
        self.assertIn("open/draft/unmerged", by_id["GAP-094"]["validation"])
        self.assertEqual(
            by_id["GAP-095"]["evidence"][1]["ref"],
            "fix/v4-exclude-modeled-fees-from-hardnav-20261116",
        )
        self.assertIn("13,000-block corrected replay remains pending", by_id["GAP-095"]["description"])
        self.assertIn(
            "GAP-095",
            {risk["hypergraph_gap"] for risk in self.governance["counts"]["observed_contract_risk_details"]},
        )
        self.assertIn("43754510440", by_id["GAP-094"]["validation"])
        self.assertIn("43864234518", by_id["GAP-095"]["validation"])

    def test_critical_security_gaps_are_recorded_without_secret_values(self):
        critical = [gap for gap in self.gaps["gaps"] if gap["severity"] == "critical"]
        self.assertGreaterEqual(len(critical), 5)
        serialized = json.dumps(self.gaps, ensure_ascii=False)
        self.assertNotRegex(serialized, r"(?i)(-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----)")
        self.assertNotRegex(serialized, r"(?i)(api[_-]?key|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_\-/+=]{16,}")

if __name__ == "__main__":
    unittest.main()
