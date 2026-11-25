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

    def test_proposals_are_not_counted_as_repositories(self):
        actual_ids = {node["node_id"] for node in self.nodes_doc["nodes"]}
        proposal_ids = {proposal["proposal_id"] for proposal in self.proposals["proposals"]}
        self.assertEqual(len(proposal_ids), 39)
        self.assertFalse(actual_ids.intersection(proposal_ids))
        self.assertEqual(
            len(self.overlap["assessments"]) + len(self.overlap["remaining_proposals"]),
            39,
        )

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

    def test_critical_security_gaps_are_recorded_without_secret_values(self):
        critical = [gap for gap in self.gaps["gaps"] if gap["severity"] == "critical"]
        self.assertGreaterEqual(len(critical), 5)
        serialized = json.dumps(self.gaps, ensure_ascii=False)
        self.assertNotRegex(serialized, r"(?i)(-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----)")
        self.assertNotRegex(serialized, r"(?i)(api[_-]?key|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_\-/+=]{16,}")

if __name__ == "__main__":
    unittest.main()
