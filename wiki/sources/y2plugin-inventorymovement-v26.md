---
title: "Y2Plugin InventoryMovement V26"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, plugin, inventory, stock, movement, soap, api]
summary: "Y2Plugin for inventory input/output flows — stock movements, item inputs/outputs, inventory tracking."
---

# Y2Plugin InventoryMovement V26

## Overview

Plugin for managing inventory movement flows in Cegid Retail Y2 v26 — item inputs (receiving stock) and item outputs (removing stock).

**Registration:** January 21, 2026 | **Plugin Build:** #6.96

## Key Takeaways

### Core Methods

| Method | Purpose | Status |
|--------|---------|--------|
| `ItemsInput.Create` | Create inventory input (receiving) | Released |
| `ItemsInput.GetDetail` | Get input details | Released |
| `ItemsInput2.Create` | Create inventory input (v2) | Released |
| `ItemsInput2.GetDetail` | Get input v2 details | Released |
| `ItemsOutput.Create` | Create inventory output | Released |
| `ItemsOutput.GetDetail` | Get output details | Released |
| `ItemsOutput2.Create` | Create inventory output (v2) | Released |
| `ItemsOutput2.GetDetail` | Get output v2 details | Released |

### Report Methods
- `GenerateDocument` / `Poll` / `Download` — PDF generation
- `GenerateLabels` / `EndGenerateLabels` / `Download` — Label printing

### Technical Requirements
- **.NET Framework 4.8** required

## Related Concepts
- [[y2-webservices-guide]] — General SOAP/Web Services guide
- [[y2plugin-company-v26]] — Store/warehouse data (for inventory location)
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/Common/Webservices/Follow-up Notes/Y2Plugin InventoryMovement V26`
