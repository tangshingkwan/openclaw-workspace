---
title: "Y2 RFE - File Exchange Best Practices"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, rfe, file-exchange, best-practices, azure, performance, limits]
summary: "Critical RFE limits and best practices — file naming, size limits, rate limits, SAS tokens, caching strategy. MUST READ for SynagieAPI."
---

# Y2 RFE - File Exchange Best Practices

## Overview

Critical operational limits and best practices for RFE file exchanges. **Essential reading for SynagieAPI integration.**

## Key Takeaways

### File Naming
- **Case-sensitive!** Use lowercase
- **Avoid characters:** `\ / : * ? " < > | %`
- **IN folder only** — files outside won't be processed
- **Include timestamp** in filenames

### File Replacement
1. Delete existing file first
2. Then upload new file with same name
3. Otherwise rejected if file still present on server

### Rate Limits
| Client Type | Max Files/Minute |
|-------------|------------------|
| SaaS Dedicated | 100 files/min |
| SaaS Advanced | 3 files/min |

### Size Limits
- **Max file size:** 1GB (larger files rejected, stay in IN)
- **Batch records** — group multiple records in one file (don't use 1 file per record)

### Queue Limits
- **Max pending jobs:** 10,000 (both directions)
- Beyond limit → "429 Too Many Requests" error
- Wait until queue drops below 10,000

### Maintenance Window
- **01:00 AM - 03:00 AM** (POD local time)
- Jobs may not run during this window

### SAS Token Strategy
| Key Type | Max Validity |
|----------|--------------|
| Read | 24 hours |
| Read/Write | 10 minutes |

### Connection Strategy
- **Max frequency:** Every 5 minutes recommended
- **Use caching** — cache Token Bearer and SAS keys
- Batch transfer files during SAS key validity

### Correlation ID
- Add `x-correlation-id` header to API calls
- Enables tracking and debugging
- Must be unique per request

## Related Concepts
- [[y2-rfe-introduction]] — RFE overview
- [[y2-rfe-implementation]] — RFE setup
- [[synagie-api]] — Franky's SynagieAPI project

## Source
`documents/Y2/RFE/Functional Documentation/Implementation Guide/04_File_exchange_best_practices.md`
