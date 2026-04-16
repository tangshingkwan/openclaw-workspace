---
title: "Y2 RFE - Introduction to Retail File Exchange"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, rfe, file-exchange, azure, blob-storage, integration, migration]
summary: "RFE (Retail File Exchange) — new Azure Blob Storage-based file exchange replacing CGFT. Critical for SynagieAPI integration. MUST READ."
---

# Y2 RFE - Introduction to Retail File Exchange

## Overview

**RFE (Retail File Exchange)** is the new file exchange solution for Cegid Retail Y2, replacing the legacy CGFT (Cegid File Transfer). Based on Microsoft Azure Blob Storage.

⚠️ **CRITICAL:** CGFT decommissioned end of 2024 — all integrations must migrate to RFE!

## Key Takeaways

### Architecture
- **Based on:** Microsoft Azure Blob Storage
- **Storage:** Tenant workspace → Containers → IN/OUT/ARCHIVES folders
- **Protocol:** REST API over HTTP/HTTPS

### RFE vs CGFT
| Feature | CGFT (Old) | RFE (New) |
|---------|-------------|------------|
| Storage | Local/SFTP | Azure Blob Storage |
| Scalability | Limited | High |
| File size | Limited | Large files supported |
| Security | Basic | Secure protocols |
| Retention | Variable | Minimum 7 days |
| Supervision | Basic | High |

### Prerequisites
- **Minimum Y2 version:** v21.00.0.1444
- **SaaS only** (Dedicated or Advance)
- **Access to RFE configuration webapp**
- **Azure Storage client library** (.NET, Java, NodeJS, Python, Go, PHP, Ruby)

### Workflow
1. Drop file in container's **IN** folder
2. Y2 processes the file
3. Output placed in **OUT** folder
4. Processed files archived in **ARCHIVES**

## Related Concepts
- [[y2-webservices-guide]] — SOAP/Web Services (complementary to RFE)
- [[y2-rfe-implementation]] — RFE setup and configuration
- [[y2-rfe-best-practices]] — File exchange best practices
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/RFE/Functional Documentation/Implementation Guide/00_Introduction_to_RFE.md`
