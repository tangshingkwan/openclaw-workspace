---
title: "Y2 Product Data & Inventory Management V26"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, product-data, inventory, items, merchandise, services]
summary: "Cegid Retail Y2 item record management, merchandise/service types, inventory valuation, and related procedures."
---

# Y2 Product Data & Inventory Management V26

## Overview

Product Data and Inventory Management in Cegid Retail Y2 v26. Covers item records, merchandise/service types, stock management, and pricing.

**Source:** Extracted 2026-02-27 | **Version:** Y2 v26

## Item Types

| Type | Code | Description |
|------|------|-------------|
| Merchandise | MAR | Standard items, may be single or dimensioned (size/color) |
| Service | PRE | Services, repairs, non-stocked items |
| Financial | FI | Register operations (deposits, reimbursements, cash float) |
| Bill of Materials | NOM | Bundled merchandise items |

## Key Settings

### Item Record Settings (Company)

- Automatic barcode assignment
- Item code assignment
- Distinct barcodes per supplier

### Access Rights

- Menu 26: Item display/create/modify authorization
- Menu 105: Settings tables, item profiles, barcode types
- Menu 110: Basic data access, modification, deletion

## Related Procedures

- P135 Event Log
- P417 Item Margin

## See Also

- [[y2plugin-product-v26|Product Plugin]]
- [[y2plugin-inventory-v26|Inventory Plugin]]
