# LEARNINGS.md

> Corrections, best practices, and knowledge gaps captured for continuous improvement.

---

## Categories
- `correction` — User corrected something I said/did
- `best_practice` — Discovered a better approach
- `knowledge_gap` — Found my knowledge was outdated or missing
- `pattern` — Recurring situation handled well

---

## 2026-04

### 2026-04-14 | pattern: simplify-and-harden
**Situation:** Multiple iterations on PDF generation for dryer manual
**What happened:** Font issues (Traditional vs Simplified Chinese) caused repeated rework
**Pattern-Key:** `pdf-font-charset-match`
**See Also:** TOOLS.md - PDF generation notes
**Lessons:**
- Always identify character set before selecting fonts (SC vs TC vs Japanese)
- Noto Sans SC = Simplified Chinese, Noto Sans TC = Traditional Chinese
- Test Chinese text rendering early, not after multiple iterations
**Promote to:** ✅ PROMOTED → TOOLS.md (2026-04-15 bi-weekly review)

### 2026-04-11 | correction
**Situation:** Fig. 1 in dryer manual PDF was cropped incorrectly
**User said:** "The fig. 1 is not having the full picture"
**Correction:** Used wrong crop coordinates from image analysis
**Lesson:** Always ask user to resend reference image when crop quality is uncertain
**Promote to:** ✅ PROMOTED → AGENTS.md (2026-04-15 bi-weekly review)

---

## 2026-04 | knowledge_gap
**Topic:** Discord PDF/file sharing via openclaw message send
**Gap:** Not aware of openclaw message send --media CLI approach initially
**Discovered:** `openclaw message send --channel discord --target channel:XXX --media /path/to/file`
**Promote to:** ✅ PROMOTED → TOOLS.md (2026-04-15 bi-weekly review)

---

*Last updated: 2026-04-14*

### 2026-04-14 | best_practice
**Situation:** Installing skills for dev team agents
**Pattern-Key:** skills-install-symlink
**Lesson:** Skills from ~/.agents/skills/ (skills.sh) need to be symlinked to ~/.openclaw/workspace/skills/ for OpenClaw to discover them. The skills.sh CLI said "symlinked: OpenClaw" but the symlinks were NOT created automatically.
**Action:** Manually run: ln -sf ~/.agents/skills/<skill-name> ~/.openclaw/workspace/skills/<skill-name>
**Promote to:** ✅ PROMOTED → TOOLS.md (2026-04-15 bi-weekly review)
