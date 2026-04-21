---
title: "Y2 Deprecated Methods"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, deprecated, migration, api, methods]
summary: "Y2 deprecated service methods with scheduled deletion dates. Key: CustomerOrder/CreateFrom deprecated, use CreateFrom2."
---

# Y2 Deprecated Methods

## Overview

List of deprecated service methods for Y2 plugins. These methods are no longer supported and scheduled for removal.

**Source:** Extracted 2026-02-27 | **Last Updated:** 2/20/2025 (package 25.0.1)

## ⚠️ Critical Deprecation

| Plugin/Service | Deprecated Method | Use Instead | Deletion Date |
|---------------|-------------------|-------------|---------------|
| CustomerOrder/Management | `CreateFrom` | `CreateFrom2` | 2/1/2028 |

## Known Deprecated Methods

### CustomerOrder

| Old Method | New Method | Status |
|-----------|------------|--------|
| `CreateFrom` | `CreateFrom2` | **Deprecated** — use immediately |

## Action Required

- [ ] Identify any use of deprecated methods in your integration
- [ ] Replace with new method equivalents
- [ ] Test thoroughly before deletion date
- [ ] Monitor Cegid release notes for additional deprecations

## References

- [[y2plugin-customerorder-v26|CustomerOrder Plugin]] — uses `CreateFrom2`
- [[y2-rfe-introduction|RFE Introduction]] — for file-based integrations

## See Also

- [[y2-webservices-guide|Web Services Guide]]
- [[y2-rfe-migration-guide|RFE Migration Guide]]
