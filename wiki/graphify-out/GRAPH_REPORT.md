# Y2 Wiki — Semantic Knowledge Graph Report

**Generated:** 2026-04-21
**Source:** `graphify-out/graph.json`
**Files processed:** 115

---

## Graph Overview

| Metric | Value |
|--------|-------|
| Total Nodes | 4,156 |
| Total Edges | 304 |
| Graph Density | 0.018 (sparse hub-and-spoke) |
| Files Processed | 115 / 115 |

---

## Node Type Distribution

| Type | Count | Description |
|------|-------|-------------|
| concept | 974 | General concepts, field names, procedures |
| plugin | 817 | Y2Plugin modules (CustomerOrder, Inventory, Product, etc.) |
| inventory | 717 | Product & inventory management entities |
| payment | 374 | POS, payment, Adyen connector |
| crm | 187 | Customer management, loyalty, clienteling |
| procedure | 174 | Workflows and operational procedures |
| omni | 144 | Omni-channel & e-commerce |
| rfe | 133 | Retail File Exchange (replaces CGFT) |
| api | 133 | Web services, SOAP/REST endpoints, methods |
| hr | 97 | Employee and workforce management |
| localization | 91 | Multi-country, translation, fiscal references |
| procurement | 65 | Sourcing and purchase order management |
| finance | 62 | Accounting, budgeting, forecasting |
| connector | 41 | Tax connectors (Avalara, Vertex), Adyen |
| migration | 32 | CGFT→RFE migration procedures |
| tax | 29 | Tax rates, VAT, tax engine |
| module | 27 | Major system modules |
| data | 27 | Database tables, field definitions |
| version | 23 | Version tracking entries |
| tool | 9 | Admin tools and utilities |

---

## Top Hub Nodes (Highest Out-Degree)

Hubs are nodes that reference/connect to the most other nodes — the **integrating** modules of Y2:

| Node | Out-Degree | Role |
|------|-----------|------|
| `y2plugin_customer` | 71 | Customer master data, multi-classification, mailings |
| `y2plugin_customerorder` | 49 | Order creation, document workflows, replenishment |
| `y2plugin_inventory` | 47 | Stock levels, warehouse management, snapshots |
| `y2plugin_product` | 36 | Product catalog, pricing, characteristics |
| `y2plugin_taxengine` | 15 | Tax calculation, VAT rules |
| `y2plugin_sourcing` | 14 | Purchase orders, supplier management |

---

## Top Authority Nodes (Highest In-Degree)

Authorities are the nodes most referenced by others — the **core documentation anchors**:

| Node | In-Degree | Role |
|------|----------|------|
| `index` | 26 | Wiki index/homepage |
| `y2_plugin_followup_notes_v26` | 24 | Y2Plugin v26 follow-up notes |
| `log` | 8 | Changelog |
| `02_transverse_features` | 5 | Core UI, navigation, menus |
| `11_foundation_techniques_and_tools` | 5 | Admin tools, utilities |
| `10_finance_and_controlling` | 5 | Financial management |

---

## Dominant Edges (Top Relationships by Connectivity)

| Source | Target | Relation | Weight |
|--------|--------|----------|--------|
| `y2plugin_customer` | `y2plugin_customerorder` | related_to | 0.9 |
| `y2plugin_customerorder` | `y2plugin_inventory` | related_to | 0.9 |
| `y2plugin_inventory` | `y2plugin_product` | related_to | 0.9 |
| `y2plugin_product` | `y2plugin_salesconditions` | related_to | 0.9 |
| `y2plugin_sourcing` | `y2plugin_supplier` | related_to | 0.9 |
| `adyen` | `y2plugin_taxengine` | integrates_with | 0.8 |
| `avalara` | `y2plugin_taxengine` | integrates_with | 0.8 |
| `vertex` | `y2plugin_taxengine` | integrates_with | 0.8 |
| `rfe` | `cgft` | replaces | 1.0 |
| `rfe` | `azure_blob_storage` | uses | 0.9 |

---

## Major Domains / Communities

The 4,156 nodes fall into **6 major semantic domains** based on type distribution and cross-references:

### Domain 1 — Product & Inventory (≈1,578 nodes)
**Files:** `01_Product_Data_and_Inventory_Management.md`, `Follow-up_Notes_Y2Plugin_Product_V26.md`, `Follow-up_Notes_Y2Plugin_Inventory_V26.md`

Core entities: Items, variants, dimensions, price lists, stock movements, warehouse transfers, inventory counts, inventory tracking (serial/lot), replenishment suggestions.

Key plugins: `y2plugin_product`, `y2plugin_inventory`, `y2plugin_inventorymovement`, `y2plugin_inventorycount`, `y2plugin_inventorytracking`, `y2plugin_transfer`, `y2plugin_reservation`

---

### Domain 2 — Sales & Customer Orders (≈1,200 nodes)
**Files:** `y2plugin-customerorder-v26.md`, `Follow-up_Notes_Y2Plugin_CustomerOrder_V26.md`, `Follow-up_Notes_Y2Plugin_Customer_V26.md`

Core entities: Customer orders, quotation workflows, order→delivery notice→receipt→invoice pipeline, front-office sales, customer reservations, order types (BLC, DDI, FAC, etc.)

Key plugins: `y2plugin_customerorder`, `y2plugin_customer`, `y2plugin_reservation`

---

### Domain 3 — POS & Payment (≈805 nodes)
**Files:** `06_Point_of_Sale_Management.md`, `y2-connector-adyen.md`

Core entities: POS registers, receipt configuration, Adyen PayByLink, MPOS, LiveStore, payment terminals, shift management, float management, cash drawer operations.

Key connectors: `adyen` (payment processor), `pos` (point of sale)

---

### Domain 4 — Transverse & Foundation (≈300 nodes)
**Files:** `02_Transverse_Features.md`, `11_Foundation_Techniques_and_Tools.md`

Core entities: Login, menus, favorites, navigation UI, scheduled tasks (TaskScheduler plugin), audit logging, trace files, RFID templates, environment configuration (DataSpread tool).

Key plugins: `y2plugin_taskscheduler`, `y2plugin_audit`, `y2plugin_settings`, `y2plugin_company`

---

### Domain 5 — CRM & Clienteling (≈215 nodes)
**Files:** `03_CRM_and_Clienteling.md`, `y2-v26-crm-clienteling.md`

Core entities: Customer loyalty programs, loyalty rules, points acquisition/redeeming, call-back lists, customer mailings, customer tracking (Customer 360), after-sales services, loan management.

Key plugins: `y2plugin_customer` (loyalty), `y2plugin_salesconditions` (pricing rules)

---

### Domain 6 — Tax & Finance Connectors (≈200 nodes)
**Files:** `y2-connector-avalara.md`, `y2-connector-vertex.md`, `10_Finance_and_Controlling.md`

Core entities: Avalara tax calculation, Vertex tax computation, tax rates, VAT regimes, jurisdiction handling, document types, fiscal counters.

Key connectors: `avalara`, `vertex`, `y2plugin_taxengine`

---

## Key Architectural Relationships

```
RFE (Retail File Exchange)
  ├── Replaces CGFT (legacy file transfer)
  ├── Uses Azure Blob Storage
  └── Referenced by all import/export workflows

Y2Plugin Ecosystem
  ├── y2plugin_customer ← central hub (71 out-degree)
  │     ├── y2plugin_customerorder
  │     ├── y2plugin_salesconditions
  │     └── y2plugin_customer (loyalty)
  ├── y2plugin_inventory
  │     ├── y2plugin_product
  │     ├── y2plugin_transfer
  │     ├── y2plugin_inventorymovement
  │     └── y2plugin_inventorycount/tracking
  └── y2plugin_sourcing
        └── y2plugin_supplier

Tax Connectors
  ├── Adyen (payment) ──POS──
  ├── Avalara ──y2plugin_taxengine──
  └── Vertex ──y2plugin_taxengine──
```

---

## Notable Gaps / Isolated Clusters

- **RFE vs CGFT migration** is well-documented but the new API (`Consuming_Y2_Web_Services.md`) has fewer cross-links than expected
- **Workforce Management** (`08_Workforce_Management.md`) is under-represented in the graph despite 89 entities
- Many single-table-field entities (e.g., `gp_*`, `msa_*` prefixes) form isolated nodes — these could be grouped by table prefix for better clustering
- The graph is sparse (density 0.018), indicating most modules are documented independently with few cross-references

---

## Processing Notes

- Entity extraction used header parsing (`#`, `##`, `###`), bold terms (`**...**`), inline code (`` `...` ``), and table first-columns
- Type classification prioritizes: explicit plugin name → filename context → keyword heuristics
- Relationship edges are drawn from: explicit plugin mentions, connector ↔ tax engine links, RFE ↔ CGFT replacement, and POS ↔ Adyen payment integration
- Low edge density reflects Y2's modular plugin architecture where each plugin is largely self-contained

---

*Report auto-generated by graphify semantic extraction — see `graph.json` for full node/edge data.*
