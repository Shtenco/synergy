#!/usr/bin/env python3
"""Rebuild registry/repos.json from GitHub repositories visible to gh CLI."""

import json
import subprocess
from pathlib import Path

OWNER = "Shtenco"
OUT = Path("registry/repos.json")
MATCH = ("synergy", "sinergy", "synegy")

def domain(name: str) -> str:
    n = name.lower()
    if any(x in n for x in ("agi","nexus","agent","company","coder","olga")):
        return "agi-agentic"
    if any(x in n for x in ("midas","trade","trader","quant","risk","market","relative","pump","algotrading")):
        return "trading-quant"
    if any(x in n for x in ("financial","finance","pay","usds","qe","money","budget","cashero","economy")):
        return "finance-economy"
    if any(x in n for x in ("chain","blockchain","blochain","metachain","post_quantum","radio")):
        return "blockchain-protocol"
    if any(x in n for x in ("compress","linux","meta_os","motherboard","xpu","computing","matrix")):
        return "compute-os"
    if any(x in n for x in ("app","messenger","terminal")):
        return "apps-interface"
    if any(x in n for x in ("search","lead")):
        return "search-growth"
    return "research-other"

cmd = [
    "gh","repo","list",OWNER,
    "--limit","1000",
    "--json","name,nameWithOwner,visibility,isArchived,url"
]
repos = json.loads(subprocess.check_output(cmd, text=True))
all_count = len(repos)
synergy = [r for r in repos if any(k in r["name"].lower() for k in MATCH)]

payload = {
    "schema_version":"1.0.0",
    "generated_from":f"GitHub account {OWNER}",
    "umbrella_repository":f"{OWNER}/synergy",
    "discovery_rule":"repository name contains synergy, sinergy, or synegy",
    "total_account_repositories":all_count,
    "synergy_repository_count":len(synergy),
    "repositories":[
        {
            "name":r["name"],
            "full_name":r["nameWithOwner"],
            "visibility":r["visibility"].lower(),
            "archived":r["isArchived"],
            "url":r["url"],
            "category":domain(r["name"]),
        }
        for r in sorted(synergy, key=lambda x: x["name"].lower())
    ],
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
print(f"Wrote {len(synergy)} SYNERGY repositories to {OUT}")
