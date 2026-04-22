#!/usr/bin/env python3
"""
Semantic Knowledge Graph Builder for Y2 Wiki — v2
Refined entity type detection and better deduplication.
"""

import json
import re
import os
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path("/root/.openclaw/workspace/wiki")
GRAPH_OUT = WIKI_ROOT / "graphify-out"
GRAPH_FILE = GRAPH_OUT / "graph.json"

# ── Helpers ──────────────────────────────────────────────────────────────────
def slugify(name):
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

STOPWORDS = {
    "the","a","an","and","or","but","in","on","at","to","for","of","with",
    "by","from","as","is","was","are","were","been","be","have","has","had",
    "do","does","did","will","would","could","should","may","might","must",
    "shall","can","need","this","that","these","those","it","its","they",
    "them","their","we","us","our","you","your","he","she","him","her","his",
    "i","me","my","not","no","yes","so","if","then","than","when","where",
    "which","who","whom","whose","why","how","all","each","every","both",
    "few","more","most","other","some","any","such","only","own","same",
    "very","just","also","about","above","after","again","against","among",
    "before","between","during","into","through","until","while","using",
    "see","set","new","get","use","used","using","note","note:","notes",
    "follow","follow-up","follow up","field","fields","value","values",
    "type","based","option","options","allows","allows you","you can",
    "please","refer","section","example","examples","way","ways",
}

# Known Y2 Plugins (authoritative list)
KNOWN_PLUGINS = {
    "customerorder": "CustomerOrder",
    "customer": "Customer",
    "product": "Product",
    "inventory": "Inventory",
    "voucher": "Voucher",
    "audit": "Audit",
    "salesconditions": "SalesConditions",
    "taxengine": "TaxEngine",
    "reservation": "Reservation",
    "transfer": "Transfer",
    "inventorymovement": "InventoryMovement",
    "inventorycount": "InventoryCount",
    "inventorytracking": "InventoryTracking",
    "supplier": "Supplier",
    "sourcing": "Sourcing",
    "salesexternal": "SalesExternal",
    "employee": "Employee",
    "settings": "Settings",
    "taskscheduler": "TaskScheduler",
    "company": "Company",
}

KNOWN_CONNECTORS = {"adyen", "avalara", "vertex"}
KNOWN_SYSTEMS = {"rfe", "cgft", "soap", "pos", "pos_management", "crm", "finance",
                 "inventory", "hr", "workforce", "budgeting", "localization",
                 "omni_channel", "procurement", "sourcing", "foundation"}

def classify_entity(eid, label, content_lower, filename):
    """Classify an entity based on its ID, label, and file context."""
    eid_lower = eid.lower()
    label_lower = label.lower()
    fname_lower = filename.lower()

    # 1. Explicit plugin detection
    if eid_lower.startswith("y2plugin_") or "y2plugin" in eid_lower:
        return "plugin"
    for pkey, _ in KNOWN_PLUGINS.items():
        if pkey in eid_lower or pkey in label_lower:
            return "plugin"

    # 2. Connector detection
    for c in KNOWN_CONNECTORS:
        if c in eid_lower:
            return "connector"
    if "connector" in eid_lower or "connector" in label_lower:
        return "connector"

    # 3. File-context-based detection
    if "y2plugin" in fname_lower:
        return "plugin"
    if "connector" in fname_lower or "adyen" in fname_lower or "avalara" in fname_lower or "vertex" in fname_lower:
        return "connector"
    if "rfe" in fname_lower or "file_exchange" in fname_lower:
        return "rfe"
    if "pos" in fname_lower or "point_of_sale" in fname_lower:
        return "payment"
    if "crm" in fname_lower or "clienteling" in fname_lower:
        return "crm"
    if "inventory" in fname_lower or "product" in fname_lower:
        return "inventory"
    if "finance" in fname_lower or "budget" in fname_lower or "forecast" in fname_lower:
        return "finance"
    if "workforce" in fname_lower or "employee" in fname_lower:
        return "hr"
    if "omni" in fname_lower or "channel" in fname_lower:
        return "omni"
    if "procedure" in fname_lower:
        return "procedure"
    if "tax" in fname_lower or "vat" in fname_lower:
        return "tax"
    if "localization" in fname_lower:
        return "localization"
    if "procurement" in fname_lower or "sourcing" in fname_lower:
        return "procurement"
    if "migration" in fname_lower or "deprecated" in fname_lower:
        return "migration"
    if "web_service" in fname_lower or "webservices" in fname_lower or "rfe" in fname_lower:
        return "api"
    if "version" in fname_lower or "tracking" in fname_lower:
        return "version"

    # 4. Keyword-based detection
    if any(k in eid_lower for k in ["soap", "rest", "api", "endpoint", "web_service", "webservice"]):
        return "api"
    if any(k in eid_lower for k in ["plugin"]):
        return "plugin"
    if any(k in eid_lower for k in ["tax", "vat"]):
        return "tax"
    if any(k in eid_lower for k in ["payment", "adyen"]):
        return "payment"
    if any(k in eid_lower for k in ["inventory", "stock", "warehouse", "product"]):
        return "inventory"
    if any(k in eid_lower for k in ["customer", "loyalty"]):
        return "crm"
    if any(k in eid_lower for k in ["employee", "staff"]):
        return "hr"
    if any(k in eid_lower for k in ["budget", "forecast", "finance"]):
        return "finance"
    if any(k in eid_lower for k in ["omni", "ecommerce", "e_commerce"]):
        return "omni"
    if any(k in eid_lower for k in ["rfe", "azure_blob", "file_exchange"]):
        return "rfe"
    if any(k in eid_lower for k in ["procedure", "workflow", "process"]):
        return "procedure"
    if any(k in eid_lower for k in ["tool", "utility", "admin"]):
        return "tool"
    if any(k in eid_lower for k in ["migration", "upgrade", "install"]):
        return "migration"
    if any(k in eid_lower for k in ["method", "function", "class"]):
        return "api"
    if any(k in eid_lower for k in ["table", "field", "column", "database", "schema"]):
        return "data"

    # 5. Known systems
    for sys in KNOWN_SYSTEMS:
        if sys in eid_lower:
            return "module"

    return "concept"

def extract_entities(content, filename):
    """Extract semantic entities from file content."""
    entities = []
    content_lower = content.lower()

    # H1/H2/H3 headers
    for m in re.finditer(r'^#{1,3}\s+(.+)$', content, re.MULTILINE):
        phrase = m.group(1).strip()
        words = phrase.split()
        if len(words) >= 1 and words[0].lower() not in STOPWORDS and len(phrase) > 2:
            eid = slugify(phrase)
            ent_type = classify_entity(eid, phrase, content_lower, filename)
            entities.append({"id": eid, "label": phrase.title(), "type": ent_type, "source": filename})

    # Bold terms
    for m in re.finditer(r'\*\*(.+?)\*\*', content):
        term = m.group(1).strip().strip('.,;:')
        if len(term) > 3 and term.lower() not in STOPWORDS and not term.startswith('http'):
            eid = slugify(term)
            if eid not in {e["id"] for e in entities}:
                ent_type = classify_entity(eid, term, content_lower, filename)
                entities.append({"id": eid, "label": term.title(), "type": ent_type, "source": filename})

    # Inline code terms
    for m in re.finditer(r'`([^`\n]{2,50})`', content):
        code = m.group(1).strip()
        if not code.startswith('http') and not re.match(r'^\d+$', code):
            eid = slugify(code)
            if eid not in {e["id"] for e in entities}:
                entities.append({"id": eid, "label": code, "type": "api", "source": filename})

    # Table first-columns (parameter/field names)
    for m in re.finditer(r'^\|(.+?)\|', content, re.MULTILINE):
        row = m.group(1)
        cols = [c.strip().strip('*_`') for c in row.split('|')]
        for col in cols[:2]:
            col = re.sub(r'[#*`]', '', col).strip()
            if len(col) > 2 and col.lower() not in STOPWORDS and not col.startswith('http'):
                if not re.match(r'^[\-\–\(]', col) and not re.match(r'^\d+$', col):
                    eid = slugify(col)
                    if eid not in {e["id"] for e in entities}:
                        ent_type = classify_entity(eid, col, content_lower, filename)
                        entities.append({"id": eid, "label": col.title(), "type": ent_type, "source": filename})

    return entities

def extract_relationships(content, filename):
    """Extract semantic relationships from file content."""
    relationships = []
    content_lower = content.lower()

    # ── Intra-wiki references ────────────────────────────────────────────────
    # "Y2Plugin X" / "plugin X" mentions
    for m in re.finditer(r'(?:y2plugin|plugin)[_\s]+([a-zA-Z]+)', content_lower):
        mentioned = m.group(1).strip()
        if mentioned in KNOWN_PLUGINS:
            fname_slug = slugify(filename.replace('.md',''))
            key = (f"y2plugin_{mentioned}", fname_slug, "related_to")
            relationships.append({"source": f"y2plugin_{mentioned}", "target": fname_slug,
                                  "relation": "related_to", "weight": 0.9, "source_file": filename})

    # ── Connector ↔ Tax/Payment ─────────────────────────────────────────────
    tax_connectors = {"adyen", "avalara", "vertex"}
    for m in re.finditer(r'(adyen|avalara|vertex).*?(?:tax|payment|vat|invoice)', content_lower):
        rels = [("y2plugin_taxengine", m.group(1), "integrates_with", 0.8),
                (m.group(1), "y2plugin_taxengine", "integrates_with", 0.8)]
        for s, t, r, w in rels:
            relationships.append({"source": s, "target": t, "relation": r, "weight": w, "source_file": filename})

    # ── RFE ↔ File Exchange ─────────────────────────────────────────────────
    if "rfe" in content_lower and any(k in content_lower for k in ["cgft", "azure blob", "file exchange"]):
        relationships.append({"source": "rfe", "target": "cgft", "relation": "replaces", "weight": 1.0, "source_file": filename})
        relationships.append({"source": "rfe", "target": "azure_blob_storage", "relation": "uses", "weight": 0.9, "source_file": filename})

    # ── POS ↔ Payment ────────────────────────────────────────────────────────
    if "pos" in content_lower or "point of sale" in content_lower:
        if "adyen" in content_lower:
            relationships.append({"source": "pos", "target": "adyen", "relation": "integrates_with", "weight": 0.9, "source_file": filename})

    # ── API/Web Service relationships ───────────────────────────────────────
    api_patterns = [
        (r'uses? (?:the )?(soap|rest|web service|api)', 'uses'),
        (r'call(?:s|ed|ing)? (?:the )?(soap|rest|api)', 'calls'),
        (r'(?:via|through) (soap|rest|api)', 'via'),
        (r'(soap|rest|api) (?:request|call|method)', 'is_used_by'),
    ]
    for pattern, rel in api_patterns:
        for m in re.finditer(pattern, content_lower):
            target = m.group(1).strip()
            if target:
                relationships.append({"source": slugify(filename.replace('.md','')),
                                      "target": target, "relation": rel, "weight": 0.7,
                                      "source_file": filename})

    # ── Module ↔ Plugin ──────────────────────────────────────────────────────
    mod_plugin_map = {
        "inventory": "y2plugin_inventory",
        "customer": "y2plugin_customer",
        "product": "y2plugin_product",
        "sales": "y2plugin_customerorder",
        "procurement": "y2plugin_sourcing",
        "finance": "y2plugin_taxengine",
    }
    for mod, plugin in mod_plugin_map.items():
        if mod in content_lower:
            fname_slug = slugify(filename.replace('.md',''))
            relationships.append({"source": plugin, "target": fname_slug,
                                  "relation": "part_of", "weight": 0.8, "source_file": filename})

    return relationships

def main():
    # Load existing graph
    existing_nodes = {}
    existing_edges = []
    seen_edge_keys = set()

    if GRAPH_FILE.exists():
        try:
            existing = json.loads(GRAPH_FILE.read_text())
            for n in existing.get("nodes", []):
                existing_nodes[n["id"]] = n
            for e in existing.get("edges", []):
                key = (e["source"], e["target"], e["relation"])
                seen_edge_keys.add(key)
                existing_edges.append(e)
            print(f"Loaded {len(existing_nodes)} existing nodes, {len(existing_edges)} edges")
        except Exception as e:
            print(f"Could not load existing graph: {e}")

    # Read uncached files
    uncached_file = GRAPH_OUT / ".graphify_uncached.txt"
    files = [f.strip() for f in uncached_file.read_text().splitlines() if f.strip()]
    print(f"Processing {len(files)} files...")

    all_nodes = dict(existing_nodes)
    all_edges = list(existing_edges)
    processed = 0

    for fpath in files:
        full_path = Path(fpath)
        filename = full_path.name

        if not full_path.exists():
            continue

        try:
            content = full_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            continue

        if len(content) < 50:
            continue

        processed += 1

        # Extract & merge entities
        entities = extract_entities(content, filename)
        for ent in entities:
            eid = ent["id"]
            if eid in all_nodes:
                # Merge sources
                existing_src = all_nodes[eid].get("source", "")
                if filename not in existing_src:
                    all_nodes[eid]["source"] = f"{existing_src}, {filename}"
                # Upgrade type if needed
                if all_nodes[eid].get("type") == "concept" and ent.get("type") != "concept":
                    all_nodes[eid]["type"] = ent["type"]
            else:
                all_nodes[eid] = ent

        # Extract & deduplicate relationships
        for rel in extract_relationships(content, filename):
            key = (rel["source"], rel["target"], rel["relation"])
            if key not in seen_edge_keys:
                seen_edge_keys.add(key)
                all_edges.append(rel)

        if processed % 20 == 0:
            print(f"  {processed}/{len(files)}: {len(all_nodes)} nodes, {len(all_edges)} edges")

    print(f"\nDone: {len(all_nodes)} nodes, {len(all_edges)} edges")

    # Build & save graph
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
    print(f"Saved: {GRAPH_FILE}")

    # Summary by type
    type_count = defaultdict(int)
    for n in all_nodes.values():
        type_count[n.get("type","unknown")] += 1
    print("\nNode types:")
    for t, c in sorted(type_count.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    return graph

if __name__ == "__main__":
    main()
