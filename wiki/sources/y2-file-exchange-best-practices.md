---
title: "Y2 File Exchange Best Practices"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, rfe, file-exchange, best-practices, limitations]
summary: "RFE file exchange limitations and best practices: naming, timestamping, file sizes, retention, rate limits."
---

# Y2 File Exchange Best Practices

## Overview

Best practices for RFE file exchange, including limitations and task scheduling.

**Source:** Extracted 2026-02-27

## Key Limitations

| Type | Limit |
|------|-------|
| File naming | Lowercase, no special chars: `\ / : * ? " < > | %` |
| File size | Max 1GB |
| Files per minute (SaaS Dedicated) | 100 |
| Files per minute (SaaS Advanced) | 3 |
| Pending jobs | 10,000 max (returns 429 error beyond) |
| Maintenance window | 01:00-03:00 AM POD local time |
| Retention | Minimum 7 days |

## Best Practices

1. **Naming:** Include timestamp in filenames
2. **Replacement:** Delete old file before uploading same name
3. **Batch:** Group records into single files (avoid 1 record = 1 file)
4. **Directory:** Place files only in `/in` folder (lowercase)

## Related Procedure

- P300 Task Scheduler

## See Also

- [[y2-rfe-operation|RFE Operation]]
- [[y2-rfe-implementation|RFE Implementation]]
