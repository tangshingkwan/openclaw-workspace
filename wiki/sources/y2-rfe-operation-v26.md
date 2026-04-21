---
title: "Y2 RFE Operation Guide V26"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, rfe, operation, azure-blob, file-exchange, webservices]
summary: "RFE client-side and Y2-side operation: SAS key auth, file transfer via /in and /out directories, Azure Storage Explorer."
---

# Y2 RFE Operation Guide V26

## Overview

Detailed RFE (Retail File Exchange) operation guide covering client-side file exchange and Y2-side processing.

**Source:** Extracted 2026-02-27

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `/in` | Files sent TO Y2 |
| `/out` | Files sent FROM Y2 |

## Client Authentication Flow

1. Call Authentication Server with user/password/domain
2. Receive Bearer token
3. Call RFE to generate SAS key using Bearer token
4. Connect to RFE via Azure Storage Explorer or AzCopy
5. Exchange files while SAS key valid

## Key Notes

- SAS key validity period controls session duration
- For large volumes, cache SAS key securely client-side
- Webservice swagger docs available for RFE TEST environment

## See Also

- [[y2-rfe-introduction|RFE Introduction]]
- [[y2-rfe-implementation|RFE Implementation]]
