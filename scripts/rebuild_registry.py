#!/usr/bin/env python3
"""Rebuild the complete Shtenco portfolio registry for the SYNERGY umbrella.

Important: ecosystem membership is NOT inferred from the repository name.
Every repository owned by Shtenco is inventoried. Classification is enriched
by M0/M1 audit metadata in registry/master_graph.json.
"""

import json
import subprocess
from pathlib import Path

OWNER = "Shtenco"
OUT = Path("registry/repos.json")
GRAPH = Path("registry/master_graph.json")

cmd = [
    "gh", "repo", "list", OWNER,
    "--limit", "1000",
    "--json", "name,nameWithOwner,visibility,isArchived,url,defaultBranchRef"
]
repos = json.loads(subprocess.check_output(cmd, text=True))

graph_by_repo = {}
if GRAPH.exists():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    graph_by_repo = {n["repository"]: n for n in graph.get("nodes", [])}

items = []
for r in sorted(repos, key=lambda x: x["name"].lower()):
    full = r["nameWithOwner"]
    g = graph_by_repo.get(full, {})
    items.append({
        "name": r["name"],
        "full_name": full,
        "visibility": r["visibility"].lower(),
        "archived": r["isArchived"],
        "url": r["url"],
        "default_branch": (r.get("defaultBranchRef") or {}).get("name"),
        "ecosystem_relation": g.get("ecosystem_relation", "unclassified"),
        "category": g.get("domain", "unclassified"),
        "node_type": g.get("node_type", "unclassified"),
        "maturity": g.get("maturity", "UNCLASSIFIED"),
        "capabilities": g.get("capabilities", []),
        "dependencies": g.get("dependencies", []),
        "risks": g.get("risks", []),
    })

payload = {
    "schema_version": "2.0.0",
    "generated_from": "Full GitHub inventory + M0/M1 graph enrichment",
    "umbrella_repository": f"{OWNER}/synergy",
    "discovery_rule": "ALL repositories owned by Shtenco are inventoried; classification is content/graph based.",
    "total_account_repositories": len(items),
    "inventoried_repositories": len(items),
    "repositories": items,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {len(items)} repositories to {OUT}")
