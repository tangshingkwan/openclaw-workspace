---
title: "Y2 RFE Implementation Guide V26"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, rfe, implementation, provisioning, saas]
summary: "RFE implementation methodology: tenant provisioning (new vs existing SaaS), Y2 settings, deployment steps."
---

# Y2 RFE Implementation Guide V26

## Overview

Methodology for implementing RFE on customer environment, including provisioning and Y2 settings.

**Source:** Extracted 2026-02-27

## Tenant Provisioning

Two cases for SaaS customer provisioning:

| Customer Type | Definition | Provisioning |
|--------------|-----------|-------------|
| New SaaS | Subscribed since 01/05/2023 | Standard provisioning |
| Existing SaaS | Subscribed before 01/05/2023 | Migration required |

**Note:** Provisioning must be carried out by Cegid's SaaS teams.

## Implementation Steps

1. Tenant provisioning via Cegid SaaS teams
2. Y2 settings configuration
3. RFE configuration
4. Testing and deployment

## See Also

- [[y2-rfe-introduction|RFE Introduction]]
- [[y2-rfe-operation|RFE Operation]]
- [[y2-rfe-migration-guide|RFE Migration Guide]]
