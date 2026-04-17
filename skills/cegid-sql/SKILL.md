---
name: cegid-sql
description: >
  Expert guidance for writing, reviewing, fixing, formatting, and explaining SQL queries
  in the Cegid retail/POS environment. Use this skill whenever the user mentions Cegid,
  asks about SQL involving Cegid tables (PIECE, LIGNE, ETABLISS, MCHPSUTILISATDATA, TIERS,
  ARTICLEDIM_MODE, GCTARFCONMODEART, TARIFMODE, etc.), references Cegid document types
  (CF, TEM, FFO, BFA, TRE, CC, AVC, FAC, BLC, DDI, DE, and 40+ others), export states
  (ATT, AT1, AT2, AT3), or asks for help with any query that will run inside the Cegid
  SQL editor. Also trigger when the user pastes a SQL snippet and asks to fix, reorganize,
  or explain it — even if they don't say "Cegid" explicitly, as long as the context is
  a Cegid implementation.
---

# Cegid SQL Skill

This skill covers writing, reviewing, fixing, formatting, and explaining SQL queries
for the Cegid retail/POS platform. Always apply all rules below — they reflect both
Cegid's non-standard SQL dialect and project-specific conventions.

---

## 1. Cegid SQL Dialect Rules

Cegid uses a custom SQL engine. It is **NOT** standard T-SQL or ANSI SQL. Apply these rules strictly.

### Comments
- **ALWAYS use block comments `/* */`** — line comments `--` are NOT supported in Cegid.
- For section headers use the full banner style:
  ```sql
  /* =============================================
     Section Title
     ============================================= */
  ```
- For inline or sub-section comments: `/* K1 / ATT */`

### String Literals
- **ALWAYS use single quotes** for string values: `'K1'`, `'ATT'`, `'Z002'`
- **NEVER use double quotes** for string literals — double quotes are for identifiers only
- This is a common source of errors when porting queries from other environments

### Date & Time Functions
Cegid uses its own function names — do NOT replace these with standard SQL Server equivalents:

| Cegid Function | Meaning | Do NOT use |
|---|---|---|
| `NOW()` | Current datetime | `GETDATE()` |
| `ADDHOURS(date, n)` | Add n hours to date | `DATEADD(HOUR, n, date)` |

### Other Syntax Notes
- `TRIM()`, `LTRIM()`, `RTRIM()` are all supported
- `IIF()` is supported
- `TOP 1` in subqueries is supported
- `REPLICATE()`, `CONVERT()`, `ISNULL()`, `STR()` behave as in T-SQL
- `CONVERT(VARCHAR(8), date, 112)` for YYYYMMDD date formatting

---

## 2. Key Tables & Field Conventions

See `references/cegid_full_db_reference.md` for the **complete 893-table, 21,155-field DB reference** (auto-generated from SQL export). The legacy `references/tables.md` contains curated notes for the most common query patterns. Core tables:

| Table | Purpose |
|---|---|
| `PIECE` (alias `A`) | Document/order header |
| `LIGNE` | Document line items |
| `ETABLISS` | Stores / establishments |
| `TIERS` | Customer master |
| `TIERSCOMPL` | Customer complement data |
| `MCHPSUTILISATDATA` | Custom user fields (contract type, carry sales, etc.) |
| `ARTICLEDIM_MODE` | Article/product with dimensions |
| `GCTARFCONMODEART` | Price tariff by article |
| `TARIFMODE` | Tariff mode periods |
| `CHOIXEXT` | External choice/reference table |
| `DIMENSION` | Product dimension grid |
| `ARTICLE` | Product master |
| `COMMERCIAL` | Sales rep master |

See `references/document_types.md` for the **full 44-code `GP_NATUREPIECEG` reference**.

### Common Field Patterns
- `GP_NATUREPIECEG` — Document type code (see Section 3 and `references/document_types.md`)
- `GP_ETATEXPORT` — Export state (see Section 4)
- `GP_SOUCHE` / `GP_NUMERO` / `GP_INDICEG` — Document key (series / number / index)
- `ET_CHARLIBRE1/2/3` — Free fields on establishment: SAP Sold-to / Ship-to / Storage Location
- `MUD_VALCHAMP` — Value field in `MCHPSUTILISATDATA`; used for contract type (K1/K2/K3), carry sales date, etc.
- `MUD_IDCHAMP = 26` — Contract type field ID in `MCHPSUTILISATDATA`
- `MUD_IDCHAMP = 1` — Carry sales delivery date field ID
- `GL_LIBREART6` — Article type code (e.g. `Z001`, `Z002`, `Z003`)
- `GA_CHARLIBRE1` — SAP material number on article

### Standard MCHPSUTILISATDATA Join Patterns
**Contract type from customer:**
```sql
LEFT JOIN MCHPSUTILISATDATA CONTRACTTYPE
    ON CONTRACTTYPE.MUD_ENTITEMCD = 'CLI'
    AND CONTRACTTYPE.MUD_CLEENTITE = T_TIERS
    AND CONTRACTTYPE.MUD_IDCHAMP = 26
```

**Contract type from destination establishment (used in TEM AT1):**
```sql
SELECT TOP 1 MUD_VALCHAMP
FROM MCHPSUTILISATDATA
JOIN ETABLISS ON ET_CHARLIBRE2 = MUD_CLEENTITE
WHERE MUD_ENTITEMCD = 'CLI'
  AND MUD_IDCHAMP = 26
  AND ET_ETABLISSEMENT = A.GP_ETABLISSDEST
```

---

## 3. Document Type Codes (GP_NATUREPIECEG)

> Full 44-code reference: `references/document_types.md`
> The table below lists only the common SKR interface codes.

| Code | Meaning |
|---|---|
| `CF` | Customer order (Commande Ferme) |
| `TEM` | Sent transfer |
| `TRE` | Received transfer |
| `FFO` | Receipt |
| `BFA` | Supplier return |
| `CC` | Customer order |
| `AVC` | Customer credit note |
| `FAC` | Customer invoice |
| `BLC` | Customer delivery |
| `DDI` | Customer reservation requests |
| `DE` | Customer quotation |

---

## 4. Export State Codes (GP_ETATEXPORT)

States progress in sequence: `ATT` → `AT1` → `AT2` → `AT3` → `AT4`

| Code | Meaning |
|---|---|
| `ATT` | Pending / waiting (not yet exported) |
| `AT1` | First export done |
| `AT2` | Second export done |
| `AT3` | Third export done |
| `AT4` | Final / closed |

The `EXPSTATUS` computed column advances the state by one for next-export logic:
```sql
CASE
    WHEN A.GP_ETATEXPORT = 'ATT' THEN 'AT1'
    WHEN A.GP_ETATEXPORT = 'AT1' THEN 'AT2'
    WHEN A.GP_ETATEXPORT = 'AT2' THEN 'AT3'
    ELSE 'AT4'
END AS EXPSTATUS
```

---

## 5. Contract Types (CONTRACTTYPE.MUD_VALCHAMP)

| Value | Meaning |
|---|---|
| `K1` | Standard retail contract |
| `K2` | Concession / franchise contract |
| `K3` | Special/wholesale contract |

Contract type determines SAP document type mappings (SALES_ORDER_TYPE, ITEM_CAT, CUSTREF suffixes).

---

## 6. CASE Statement Formatting Rules

Large `CASE` blocks must follow these conventions for readability and maintainability:

### Group by GP_NATUREPIECEG
Always organize WHEN clauses by document type, with a block comment header per group:
```sql
CASE
    /* =============================================
       CC / AVC: Simple direct mappings
       ============================================= */
    WHEN A.GP_NATUREPIECEG = 'CC' THEN '...'
    WHEN A.GP_NATUREPIECEG = 'AVC' THEN '...'

    /* =============================================
       CF: Based on CONTRACTTYPE + GP_ETATEXPORT
       ============================================= */
    /* K1 / ATT */
    WHEN A.GP_NATUREPIECEG = 'CF' AND CONTRACTTYPE.MUD_VALCHAMP = 'K1' AND GP_ETATEXPORT = 'ATT'
        THEN '...'
    ...
    /* =============================================
       Default
       ============================================= */
    ELSE ''
END AS COLUMN_NAME
```

### Sub-group CF by export state
Within `CF`, group conditions by export state (ATT → AT1 → AT2 → AT3) with sub-comments.

### FFO fallback placement
The generic `FFO` fallback (`WHEN A.GP_NATUREPIECEG = 'FFO' THEN '...'`) must always appear **immediately after** all specific `FFO` conditions, before any other document type group. Placing it after other groups makes it unreachable dead code.

### Collapse redundant branches
If two consecutive WHEN conditions for the same document type produce the same THEN result but differ only on a single field, collapse using `IN (...)`:
```sql
/* WRONG - redundant */
WHEN A.GP_NATUREPIECEG = 'FFO' AND GL_QTEFACT >= 0 AND GL_LIBREART6 = 'Z002'  THEN 'Z4KE'
WHEN A.GP_NATUREPIECEG = 'FFO' AND GL_QTEFACT >= 0 AND GL_LIBREART6 <> 'Z002' THEN 'Z4KE'

/* CORRECT - collapsed */
WHEN A.GP_NATUREPIECEG = 'FFO' AND GL_QTEFACT >= 0 THEN 'Z4KE'
```

### Align operators vertically
Within a group, align `=`, `<>`, `IN` operators for quick scanning:
```sql
WHEN A.GP_NATUREPIECEG = 'CF' AND CONTRACTTYPE.MUD_VALCHAMP = 'K1' AND GL_LIBREART6 <> 'Z002' AND GP_ETATEXPORT = 'ATT'
    THEN 'TAN'
WHEN A.GP_NATUREPIECEG = 'CF' AND CONTRACTTYPE.MUD_VALCHAMP = 'K1' AND GL_LIBREART6 =  'Z002' AND GP_ETATEXPORT = 'ATT'
    THEN 'TANN'
```

---

## 7. Review Checklist

When reviewing or fixing a Cegid SQL query, always check:

- [ ] No `--` line comments anywhere → replace with `/* */`
- [ ] No double-quoted string literals (`"K1"`) → replace with single quotes (`'K1'`)
- [ ] No `GETDATE()` → use `NOW()`
- [ ] No `DATEADD(HOUR, ...)` → use `ADDHOURS(date, n)`
- [ ] All commas present before each column in SELECT list
- [ ] FFO fallback is placed immediately after other FFO conditions
- [ ] No redundant WHEN branches returning the same value
- [ ] CASE blocks grouped by GP_NATUREPIECEG with block comment headers
- [ ] CF conditions sub-grouped by export state (ATT → AT1 → AT2 → AT3)

---

## 8. Writing Queries from Scratch

When writing a new Cegid query:

1. **Start with the standard join chain** for document queries:
   `PIECE A → LIGNE → ETABLISS → TIERS → TIERSCOMPL → ARTICLEDIM_MODE`
   Add `CONTRACTTYPE` and `CARRYSALES` as LEFT JOINs from `MCHPSUTILISATDATA` when needed.

2. **Apply all dialect rules** from Section 1 from the start — don't write standard T-SQL and fix later.

3. **Structure CASE blocks** per Section 6 from the beginning.

4. **Standard ORDER BY** for document export queries:
   ```sql
   ORDER BY A.GP_NATUREPIECEG, A.GP_SOUCHE, A.GP_NUMERO, A.GP_ETATEXPORT, GL_CODEARTICLE
   ```

5. Refer to `references/cegid_full_db_reference.md` for full field listings when needed (893 tables, 21,155 fields). Use `references/tables.md` for curated join patterns and common field notes. Use `references/document_types.md` for the full list of GP_NATUREPIECEG codes.
