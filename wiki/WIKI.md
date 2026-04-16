# Wiki Schema — Travis's LLM Wiki

> Configuration file for maintaining Franky's personal wiki. This tells me how to ingest sources, structure pages, and keep everything consistent.

## Purpose

A persistent, compounding knowledge base for Franky Tang. The wiki sits between raw sources and answers — knowledge is compiled once and kept current, not re-derived on every query.

**Core principle:** The wiki is a living artifact. Every ingest, query, and lint pass makes it richer.

## Wiki Focus

**Primary domains:** Tech, Business

- **Tech:** Cegid POS implementation, SynagieAPI integration, coding patterns, APIs
- **Business:** Project management, client work, processes, procedures

---

## Directory Structure

```
wiki/
├── WIKI.md          # This schema (how I maintain the wiki)
├── INDEX.md         # Content catalog (all pages, one-line summaries)
├── LOG.md           # Chronological record of all wiki activity
├── raw/             # Immutable source documents (never modified)
│   ├── articles/     # Web articles, blog posts
│   ├── documents/   # PDFs, longer reports
│   ├── notes/       # Franky's notes, meeting summaries
│   └── images/      # Downloaded images from sources
└── wiki/            # LLM-generated markdown pages
    ├── entities/    # People, companies, products
    ├── concepts/    # Topics, ideas, frameworks
    ├── sources/     # Summary pages for each ingested source
    ├── analyses/    #合成 analyses, comparisons, explorations
    └── meta/        # Project tracking, trip planning, etc.
```

---

## Page Types

### 1. Source Pages (`wiki/sources/`)
Single page per ingested source.

**Frontmatter:**
```yaml
---
title: "[Source Title]"
type: source
source-type: [article|paper|podcast|video|document|note]
source-url: [URL if applicable]
date-added: [YYYY-MM-DD]
tags: [relevant tags]
summary: "[2-3 sentence summary]"
---
```

**Body:** Key takeaways, notable quotes, data points. Always link to related entities/concepts.

---

### 2. Entity Pages (`wiki/entities/`)
People, companies, products, places.

**Frontmatter:**
```yaml
---
title: "[Entity Name]"
type: entity
entity-type: [person|company|product|place|project]
tags: [relevant tags]
created: [YYYY-MM-DD]
last-updated: [YYYY-MM-DD]
---
```

**Body:** Key facts, history, relevance to Franky's interests. Cross-reference related entities and concepts.

**Detail level:** Standard — Summary paragraph + 3-5 key points. Balanced for reference speed and completeness.

---

### 3. Concept Pages (`wiki/concepts/`)
Topics, ideas, frameworks, methodologies.

**Frontmatter:**
```yaml
---
title: "[Concept Name]"
type: concept
tags: [relevant tags]
created: [YYYY-MM-DD]
last-updated: [YYYY-MM-DD]
related-sources: [count]
---
```

**Body:** Definition, key principles, examples, how it connects to other concepts.

---

### 4. Analysis Pages (`wiki/analyses/`)
Syntheses, comparisons, deep dives.

**Frontmatter:**
```yaml
---
title: "[Analysis Title]"
type: analysis
date: [YYYY-MM-DD]
tags: [relevant tags]
sources-used: [list of source pages]
---
```

**Body:** The analysis itself. These are valuable — file them back into the wiki.

---

### 5. Meta Pages (`wiki/meta/`)
Projects, trips, ongoing work.

**Frontmatter:**
```yaml
---
title: "[Project/Trip Name]"
type: meta
category: [project|trip|research|learning]
status: [active|completed|paused]
tags: [relevant tags]
---
```

---

## Source Intake

**Mode:** One-at-a-time with discussion (Option A)

- You drop a source → I read it → we discuss key takeaways → I create pages
- Best quality, more interactive, wiki builds up properly from day one

## Ingest Workflow

When you drop a new source and ask me to process it:

1. **Read the source** — full content
2. **Discuss with you** — key takeaways, what to emphasize
3. **Write source page** — summary in `wiki/sources/`
4. **Update INDEX.md** — add new page to catalog
5. **Update relevant pages** — entity pages, concept pages that the source touches
6. **Log it** — append to `LOG.md`
7. **Flag contradictions** — if source contradicts existing claims, note it

A single source might touch 5-15 wiki pages. I do it all in one pass.

---

## Query Workflow

When you ask a question against the wiki:

1. **Read INDEX.md** — find relevant pages
2. **Read relevant pages** — full content
3. **Synthesize answer** — with citations to wiki pages
4. **File valuable output** — if the answer is a useful analysis, create a page for it

Good answers become new wiki pages. Your explorations compound.

---

## Auto-Lint

**Schedule:** Weekly cron
**Review checkpoint:** Scheduled ~1 month from now (mid-May 2026) — reassess after running the workflow

## Lint Workflow

Periodically (or on request), I health-check the wiki:

- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps that could be filled with a web search

---

## Index Format

`INDEX.md` structure:

```markdown
# Wiki Index

## Sources ([count] total)
| Page | Summary | Date |
|------|---------|------|
| [Page](wiki/sources/page.md) | One-line summary | YYYY-MM-DD |

## Entities ([count] total)
| Page | Type | Summary |
|------|------|---------|
| [Entity](wiki/entities/page.md) | person | One-line summary |

## Concepts ([count] total)
...

## Analyses ([count] total)
...

## Meta ([count] total)
...
```

---

## Log Format

`LOG.md` — append-only, each entry starts with `## [YYYY-MM-DD]`.

```markdown
## [2026-04-15] ingest | Article Title
- Source: [link]
- Key takeaways: [2-3 bullet points]
- Pages touched: [list of created/updated pages]

## [2026-04-15] query | "Your question"
- Pages consulted: [list]
- Answer summary: [brief]
- Filed as: [new page if created]
```

---

## Graph View (Obsidian)

**Enabled:** Yes — optimize for Obsidian graph view

- Add cross-links liberally between related entities, concepts, and sources
- Use YAML frontmatter tags consistently for graph clustering
- Maintain `related-links` field in frontmatter for key relationships
- Consider Dataview queries for dynamic views once wiki grows

---

## Conventions

## Output Formats

**Enabled:** Markdown + Comparisons
**On-demand:** Marp slides, Charts — can be added later as needed

**Comparisons:** I can generate side-by-side tables, matrices, and structured comparisons from wiki content. File valuable comparisons back into `wiki/analyses/`.

---

- **Filenames:** kebab-case, descriptive (`llm-wiki-pattern.md` not `page1.md`)
- **Links:** Use relative markdown links (`[Text](entities/person.md)`)
- **Dates:** ISO format (`2026-04-15`)
- **Frontmatter:** Always include, always update `last-updated`
- **Cross-references:** Link liberally — connections are the value
- **Images:** Store in `wiki/raw/images/`, reference with `![Alt](wiki/raw/images/file.jpg)`

---

## What I Own

- All writing in `wiki/` directory
- Maintaining `INDEX.md` and `LOG.md`
- Cross-referencing and consistency
- Flagging contradictions and gaps

## What You Own

- Curating sources in `raw/`
- Directing analysis and emphasis
- Asking good questions
- Reviewing and browsing the wiki

---

*This schema evolves with the wiki. As we figure out what works, we update this file.*
