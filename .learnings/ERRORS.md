# ERRORS.md

> Failed commands, API errors, and tool failures logged for pattern analysis.

---

## 2026-04

### 2026-04-11 | image_model: MiniMax-VL timeout
**Error:** `All image models failed: minimax-portal/MiniMax-VL-01: The operation was aborted due to timeout`
**Command:** OCR of dryer manual pages (7 images)
**What worked:** Processing images one at a time instead of batch
**Lesson:** MiniMax VL has lower throughput than expected; always do single images with timeout handling
**Promoted to:** ✅ TOOLS.md (2026-04-15 bi-weekly review)

### 2026-04-11 | image_model: MiniMax-VL API 1033
**Error:** `MiniMax VLM API error (1033): system error`
**Command:** Image OCR on batch
**What worked:** Retry with single image, worked on second try
**Integration:** OpenClaw image model
**Promoted to:** ✅ TOOLS.md (2026-04-15 bi-weekly review)

---

## Integration Details

| Service | Error Pattern | Resolution |
|---------|--------------|------------|
| MiniMax VL (image) | Timeout on batch | Single image mode |
| MiniMax VL (image) | API 1033 | Retry |
| Playwright PDF | Relative paths fail | Use file:// URLs |
| Discord upload | API route unknown | Use openclaw CLI |

**Note:** All ERRORS.md patterns → ✅ PROMOTED to TOOLS.md (2026-04-15 bi-weekly review)

---

*Last updated: 2026-04-14*
