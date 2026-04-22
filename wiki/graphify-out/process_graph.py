#!/usr/bin/env python3
"""
Semantic Knowledge Graph Builder for Y2 Wiki
Processes 114 wiki files and extracts entities/relationships to build graph.json
"""

import json
import re
import os
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path("/root/.openclaw/workspace/wiki")
GRAPH_OUT = WIKI_ROOT / "graphify-out"
GRAPH_FILE = GRAPH_OUT / "graph.json"

# ── Stopwords for entity filtering ──────────────────────────────────────────
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "is", "was", "are", "were", "been",
    "be", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "must", "shall", "can", "need",
    "this", "that", "these", "those", "it", "its", "they", "them", "their",
    "we", "us", "our", "you", "your", "he", "she", "him", "her", "his",
    "i", "me", "my", "not", "no", "yes", "so", "if", "then", "than",
    "when", "where", "which", "who", "whom", "whose", "why", "how",
    "all", "each", "every", "both", "few", "more", "most", "other",
    "some", "any", "such", "only", "own", "same", "very", "just",
    "also", "about", "above", "after", "again", "against", "among",
    "before", "between", "during", "into", "through", "until", "while",
}

# ── Semantic type keywords ───────────────────────────────────────────────────
TYPE_KEYWORDS = {
    "plugin":     ["plugin", "y2plugin"],
    "module":     ["module", "management", "management"],
    "connector":  ["connector", "integration"],
    "procedure":  ["procedure", "workflow", "process"],
    "api":        ["web service", "soap", "rest", "api", "endpoint"],
    "data":       ["data", "record", "entity", "master data"],
    "tax":        ["tax", "vat", "avatax", "vertex", "avalara"],
    "payment":    ["payment", "adyen", "pos", "point of sale", "register"],
    "inventory":  ["inventory", "stock", "warehouse", "product"],
    "finance":    ["finance", "accounting", "budget", "forecast", "controlling"],
    "crm":        ["crm", "customer", "loyalty", "clienteling"],
    "hr":         ["employee", "staff", "workforce", "hr"],
    "omni":       ["omni-channel", "omni channel", "ecommerce", "e-commerce"],
    "rfe":        ["rfe", "azure blob", "file exchange"],
    "tool":       ["tool", "utility", "admin", "configuration"],
}

def slugify(name):
    """Convert a phrase to a safe graph node ID."""
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

def extract_entities(content, filename):
    """Extract semantic entities from file content."""
    entities = []
    content_lower = content.lower()

    # Extract headers as concepts
    header_pattern = re.compile(r'^#{1,3}\s+(.+)$', re.MULTILINE)
    for m in header_pattern.finditer(content):
        phrase = m.group(1).strip()
        words = phrase.split()
        if len(words) >= 2 and words[0].lower() not in STOPWORDS:
            # Determine entity type from content context
            ent_type = "concept"
            for t, kw in TYPE_KEYWORDS.items():
                if any(k in content_lower for k in kw):
                    ent_type = t
                    break
            entities.append({
                "id": slugify(phrase),
                "label": phrase.title(),
                "type": ent_type,
                "source": filename,
                "context": "header"
            })

    # Extract bold terms (key concepts)
    bold_pattern = re.compile(r'\*\*(.+?)\*\*')
    for m in bold_pattern.finditer(content):
        term = m.group(1).strip()
        if len(term) > 3 and term.lower() not in STOPWORDS:
            entities.append({
                "id": slugify(term),
                "label": term.title(),
                "type": "concept",
                "source": filename,
                "context": "bold"
            })

    # Extract code/method names
    code_pattern = re.compile(r'`([^`\n]+)`')
    for m in code_pattern.finditer(content):
        code = m.group(1).strip()
        if len(code) > 2 and not code.startswith('http'):
            entities.append({
                "id": slugify(code),
                "label": code,
                "type": "api",
                "source": filename,
                "context": "code"
            })

    # Extract table-like row content (first column as entity)
    table_pattern = re.compile(r'^\|.+\|', re.MULTILINE)
    for m in table_pattern.finditer(content):
        row = m.group(0)
        cols = [c.strip().strip('*_') for c in row.split('|')[1:-1]]
        if cols:
            first = cols[0]
            if len(first) > 2 and first.lower() not in STOPWORDS:
                entities.append({
                    "id": slugify(first),
                    "label": first.title(),
                    "type": "data",
                    "source": filename,
                    "context": "table"
                })

    return entities

def extract_relationships(content, filename):
    """Extract semantic relationships between entities."""
    relationships = []
    content_lower = content.lower()

    # Patterns that indicate relationships
    rel_patterns = [
        # uses
        (r'(\w+(?:plugin|connector|module)) uses (\w+)', 'uses'),
        (r'call(?:s|ing)? (\w+(?:plugin|service|api))', 'calls'),
        (r'via (\w+(?:plugin|connector|service))', 'via'),
        # implements / part_of
        (r'(\w+) is part of (\w+)', 'part_of'),
        (r'part of (\w+)', 'part_of'),
        (r'implement(?:s|ed|ation)? by (\w+)', 'implements'),
        # related_to
        (r'relat(?:s|ed|ion) to (\w+)', 'related_to'),
        (r'similar to (\w+)', 'related_to'),
        # configures / manages
        (r'(\w+) (?:manages?|configures?|handles?) (\w+)', 'manages'),
        # depends_on
        (r'depend(?:s|ent)? on (\w+)', 'depends_on'),
        (r'requires? (\w+)', 'requires'),
    ]

    for pattern, rel_type in rel_patterns:
        for m in re.finditer(pattern, content_lower):
            source = m.group(1).strip() if m.lastindex >= 1 else ""
            target = m.group(2).strip() if m.lastindex >= 2 else m.group(1).strip()
            if source and target and source != target:
                relationships.append({
                    "source": slugify(source),
                    "target": slugify(target),
                    "relation": rel_type,
                    "weight": 0.8,
                    "source_file": filename
                })

    # Cross-reference between known Y2 components
    known_components = [
        "y2plugin_customerorder", "y2plugin_customer", "y2plugin_product",
        "y2plugin_inventory", "y2plugin_voucher", "y2plugin_audit",
        "y2plugin_salesconditions", "y2plugin_taxengine", "y2plugin_adyen",
        "y2plugin_avalara", "y2plugin_vertex", "y2plugin_reservation",
        "y2plugin_transfer", "y2plugin_inventorymovement", "y2plugin_inventorycount",
        "y2plugin_inventorytracking", "y2plugin_supplier", "y2plugin_sourcing",
        "y2plugin_salesexternal", "y2plugin_employee", "y2plugin_settings",
        "y2plugin_taskscheduler", "y2plugin_company", "rfe", "pos",
        "azure_blob", "cgft", "soap", "web_service",
    ]

    for comp in known_components:
        if comp in content_lower:
            # Link to filename source
            fname_base = slugify(os.path.basename(filename).replace('.md', ''))
            if comp != fname_base:
                relationships.append({
                    "source": comp,
                    "target": fname_base,
                    "relation": "related_to",
                    "weight": 0.7,
                    "source_file": filename
                })

    return relationships

def determine_entity_type(entity_id, content_lower, filename):
    """Determine the semantic type of an entity based on keywords."""
    eid_lower = entity_id.lower()
    combined = eid_lower + " " + content_lower

    if any(k in combined for k in ["plugin"]):
        return "plugin"
    if any(k in combined for k in ["connector", "integration"]):
        return "connector"
    if any(k in combined for k in ["soap", "web service", "rest", "api", "endpoint"]):
        return "api"
    if any(k in combined for k in ["tax", "vat", "avatax", "vertex"]):
        return "tax"
    if any(k in combined for k in ["payment", "adyen", "pos", "register"]):
        return "payment"
    if any(k in combined for k in ["inventory", "stock", "warehouse", "product"]):
        return "inventory"
    if any(k in combined for k in ["finance", "accounting", "budget", "forecast"]):
        return "finance"
    if any(k in combined for k in ["customer", "crm", "loyalty", "clienteling"]):
        return "crm"
    if any(k in combined for k in ["employee", "staff", "workforce"]):
        return "hr"
    if any(k in combined for k in ["omni", "ecommerce"]):
        return "omni"
    if any(k in combined for k in ["rfe", "azure blob", "file exchange"]):
        return "rfe"
    if any(k in combined for k in ["procedure", "workflow", "process"]):
        return "procedure"
    if any(k in combined for k in ["tool", "utility", "admin"]):
        return "tool"
    return "concept"

def main():
    # Load existing graph if present
    existing_nodes = {}
    existing_edges = []

    if GRAPH_FILE.exists():
        try:
            existing = json.loads(GRAPH_FILE.read_text())
            for n in existing.get("nodes", []):
                existing_nodes[n["id"]] = n
            existing_edges = existing.get("edges", [])
            print(f"Loaded {len(existing_nodes)} existing nodes, {len(existing_edges)} edges")
        except Exception as e:
            print(f"Could not load existing graph: {e}")

    # Read uncached file list
    uncached_file = GRAPH_OUT / ".graphify_uncached.txt"
    if not uncached_file.exists():
        print("ERROR: .graphify_uncached.txt not found")
        return

    files = [f.strip() for f in uncached_file.read_text().splitlines() if f.strip()]
    print(f"Processing {len(files)} files...")

    all_nodes = dict(existing_nodes)
    all_edges = list(existing_edges)
    seen_edge_keys = {(e["source"], e["target"], e["relation"]) for e in all_edges}

    processed = 0
    for fpath in files:
        full_path = Path(fpath)
        filename = full_path.name

        if not full_path.exists():
            print(f"  [SKIP] {filename} — not found")
            continue

        try:
            content = full_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  [ERR] {filename}: {e}")
            continue

        if len(content) < 50:
            print(f"  [SKIP] {filename} — too short ({len(content)} chars)")
            continue

        processed += 1

        # Extract entities
        entities = extract_entities(content, filename)
        content_lower = content.lower()

        for ent in entities:
            eid = ent["id"]
            if eid not in all_nodes:
                # Refine type
                ent["type"] = determine_entity_type(eid, content_lower, filename)
                all_nodes[eid] = ent
            else:
                # Update source if this is a different file
                if filename not in all_nodes[eid].get("source", ""):
                    all_nodes[eid]["source"] += f", {filename}"

        # Extract relationships
        relationships = extract_relationships(content, filename)
        for rel in relationships:
            key = (rel["source"], rel["target"], rel["relation"])
            if key not in seen_edge_keys:
                seen_edge_keys.add(key)
                all_edges.append(rel)

        if processed % 10 == 0:
            print(f"  ... processed {processed}/{len(files)} files, {len(all_nodes)} nodes, {len(all_edges)} edges")

    print(f"\nFinal: {len(all_nodes)} nodes, {len(all_edges)} edges")

    # Write graph.json
    graph = {
        "nodes": list(all_nodes.values()),
        "edges": all_edges,
        "meta": {
            "total_nodes": len(all_nodes),
            "total_edges": len(all_edges),
            "files_processed": processed,
        }
    }

    GRAPH_FILE.write_text(json.dumps(graph, indent=2, ensure_ascii=False))
    print(f"Written: {GRAPH_FILE}")

    # Write clustering summary
    types_count = defaultdict(int)
    for n in all_nodes.values():
        types_count[n.get("type", "unknown")] += 1

    print("\nNode types:")
    for t, c in sorted(types_count.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    return graph

if __name__ == "__main__":
    main()
