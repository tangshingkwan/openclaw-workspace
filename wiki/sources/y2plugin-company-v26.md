---
title: "Y2Plugin Company V26"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, plugin, company, stores, warehouses, soap, api]
summary: "Y2Plugin for company/store/warehouse data — retrieve store details, warehouse info, POS endpoints. Foundation for SynagieAPI integration."
---

# Y2Plugin Company V26

## Overview

Plugin for retrieving company, store, and warehouse information in Cegid Retail Y2 v26. Essential for SynagieAPI to know store configurations and warehouse mappings.

**Registration:** January 21, 2026 | **Plugin Build:** #6.96

## Key Takeaways

### Core Methods

| Method | Purpose | Status |
|--------|---------|--------|
| `GetDetail` (Stores) | Retrieve single store details | Released |
| `GetListDetail` (Stores) | List all stores with filtering | Released |
| `GetDetail` (Warehouses) | Retrieve single warehouse details | Released |
| `GetListDetail` (Warehouses) | List all warehouses | Released |

### Store Information
- Store settings for document types (CustomerOrder, DeliveryPreparation, etc.)
- POS endpoints and configurations
- User restrictions per store
- User fields available per document type

### Warehouse Information
- Warehouse details and configurations
- Stock management linkage

### Business Rules
- User restrictions on stores are respected
- For pickup points: restriction on `MEJ_CDEECOMETAB`
- Otherwise: restriction on `GP_ETABLISSEMENT`

## Related Concepts
- [[y2-webservices-guide]] — General SOAP/Web Services guide
- [[y2plugin-customerorder-v26]] — CustomerOrder plugin (uses store/warehouse data)
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/Common/Webservices/Follow-up Notes/Y2Plugin Company V26`
