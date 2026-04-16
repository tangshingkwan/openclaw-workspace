---
title: "Y2 RFE - Implementation Guide"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, rfe, file-exchange, azure, implementation, setup, configuration]
summary: "RFE implementation steps — tenant provisioning, container creation, Y2 configuration, web service setup."
---

# Y2 RFE - Implementation Guide

## Overview

Step-by-step guide for implementing RFE (Retail File Exchange) on a Y2 customer environment.

## Key Takeaways

### Provisioning (SaaS Teams)

**New SaaS customers** (since 01/05/2023):
- Automatic provisioning
- ADM user = default RFE administrator

**Existing SaaS customers** (before 01/05/2023):
- Manual provisioning via Cegid consultant
- Request to SaaS teams required

### Container Creation
- **Max containers:** 50 per workspace
- **Naming rules:** 20 chars max, no spaces, A-Z, a-z, "-"
- Use RFE Web App or RFE webservices

### Container Structure
Each container has 3 virtual folders:
- **IN/** — Input files (to Y2)
- **OUT/** — Output files (from Y2)
- **ARCHIVES/** — Processed files

### Key Configuration Steps
1. Create container in RFE Web App
2. Add contributors (users who can access)
3. Generate SAS key for authentication
4. Configure Y2 settings for the flow
5. Test with sample file

## Related Concepts
- [[y2-rfe-introduction]] — RFE overview and architecture
- [[y2-rfe-best-practices]] — File exchange best practices
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/RFE/Functional Documentation/Implementation Guide/03_RFE_Implementation.md`
