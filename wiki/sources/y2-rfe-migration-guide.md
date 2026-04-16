---
title: "Y2 RFE - Migration Guide (CGFT to RFE)"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, rfe, migration, cgft, file-exchange, upgrade]
summary: "Migration guide from CGFT (Cegid File Transfer) to RFE (Retail File Exchange). CGFT decommissioned end of 2024."
---

# Y2 RFE - Migration Guide (CGFT to RFE)

## Overview

Official migration guide for transitioning from CGFT (Cegid File Transfer) to RFE (Retail File Exchange).

**CGFT decommissioned end of 2024** — all customers must migrate.

## Key Takeaways

### Why Migrate?
- CGFT designed for older data standards
- RFE handles modern volumes and scalability
- Better security, performance, reliability
- Active development on RFE only

### Migration Steps
1. **Assess current CGFT usage** — inventory all file exchange flows
2. **Provision RFE environment** — contact Cegid SaaS team
3. **Create containers** — one per file flow
4. **Configure Y2** — update settings for RFE
5. **Test flows** — validate file processing
6. **Switch over** — point integration to RFE

### Key Differences

| Aspect | CGFT | RFE |
|--------|------|-----|
| Protocol | SFTP/FTP | Azure Blob REST API |
| Authentication | Basic/Key | SAS tokens |
| Tracking | Limited | Correlation IDs |
| Scalability | Low | High |

## Related Concepts
- [[y2-rfe-introduction]] — RFE overview
- [[y2-rfe-implementation]] — RFE implementation
- [[y2-rfe-best-practices]] — Operational best practices
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/RFE/Migration/Migration_Guide.md`
