---
title: "Y2Plugin Sourcing V26"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, plugin, sourcing, purchase-order, procurement, soap, api]
summary: "Y2Plugin for sourcing/purchase order management — create, update, close purchase orders, supplier management."
---

# Y2Plugin Sourcing V26

## Overview

Plugin for managing sourcing and purchase orders in Cegid Retail Y2 v26.

**Registration:** January 21, 2026 | **Plugin Build:** #6.96

## Key Takeaways

### Core Methods

| Method | Purpose | Status |
|--------|---------|--------|
| `GetList` | List purchase orders | Released |
| `GetDetail` | Get order details | Released |
| `GetListDetail` | List orders with full details | Released |
| `CreateFrom` | Create from another document | Released |
| `Create` | Create new purchase order | Released |
| `Create2` | Create purchase order (v2) | Released |
| `CreateFrom2` | Create from another document (v2) | Released |
| `Close` | Close a purchase order | Released |

### Report Methods
- `GenerateDocument` / `Poll` / `Download` — PDF generation

### Use Cases
- Supplier order management
- Purchase order creation from sales orders
- Procurement workflow automation

## Related Concepts
- [[y2-webservices-guide]] — General SOAP/Web Services guide
- [[y2plugin-inventorymovement-v26]] — Inventory movements (receiving goods)
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/Common/Webservices/Follow-up Notes/Y2Plugin Sourcing V26`
