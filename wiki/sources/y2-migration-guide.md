---
title: "Y2 RFE Migration Guide"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, rfe, migration, cgft, guide]
summary: "RFE migration guide: migrating from CGFT to RFE. Steps for new and existing SaaS customers."
---

# Y2 RFE Migration Guide

## Overview

Migration guide for transitioning from CGFT (Cegid File Transfer) to RFE (Retail File Exchange).

**Source:** Extracted 2026-02-27 | **Original:** 10/13/2023

## When to Migrate

| Customer Type | Migration Path |
|--------------|---------------|
| New SaaS (since 01/05/2023) | Standard RFE provisioning |
| Existing SaaS (before 01/05/2023) | CGFT → RFE migration |
| On-premises | RFE available |

## CGFT → RFE Timeline

- **CGFT Decommission:** End of 2024
- **Action Required:** All CGFT users must migrate to RFE

## Migration Steps

1. Analyze existing CGFT data flows
2. Provision RFE tenant (via Cegid SaaS teams)
3. Configure Y2 settings for RFE
4. Set up containers (IN/OUT/ARCHIVES)
5. Update client applications
6. Test file exchange
7. Cut over to RFE

## Key Resources

- [[y2-rfe-introduction|RFE Introduction]]
- [[y2-rfe-operation|RFE Operation]]
- [[y2-rfe-implementation|RFE Implementation]]
- [[y2-data-flows-analysis|Data Flows Analysis]]

## See Also

- [[y2-annex-files-rfe|RFE Annex Files]] — SQL queries for analysis
