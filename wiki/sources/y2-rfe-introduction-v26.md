---
title: "Y2 RFE Introduction V26"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, rfe, file-exchange, azure-blob, cgft-migration]
summary: "Retail File Exchange (RFE) introduction — replaces CGFT, based on Azure Blob Storage. CGFT decommission end of 2024."
---

# Y2 RFE Introduction V26

## Overview

RFE (Retail File Exchange) is a new file exchange solution integrated with Cegid Retail Y2 based on Microsoft Azure Blob Storage. Replaces the historical CGFT component.

**Source:** Extracted 2026-02-27 | **CGFT Decommission:** End of 2024

## Key Takeaways

### Why RFE?

| Benefit | Description |
|---------|-------------|
| Large files | Better processing of large-size files |
| Scalability | Higher scalability |
| Security | Better security via HTTPS |
| Supervision | Better supervision and resilience |
| Retention | Minimum 7 days file retention |

### Prerequisites

- Dedicated or Advance SaaS customer environment
- Minimum Y2 version: v21.00.0.1444
- Access to RFE configuration webapp

### Glossary

- **RFE** — Retail File Exchange (new)
- **CGFT** — Cegid File Transfer (historical, being deprecated)
- **Workspace** — Storage area dedicated to a tenant
- **Container** — Sub-folder within workspace (IN/OUT/ARCHIVES)

## See Also

- [[y2-rfe-migration-guide|RFE Migration Guide]]
- [[y2-rfe-implementation|RFE Implementation]]
- [[y2-rfe-best-practices|RFE Best Practices]]
