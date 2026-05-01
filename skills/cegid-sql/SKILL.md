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
| `MCHPSUTILISATDATA` | Custom user fields (contract type, carry sales, BP codes, etc.) |
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
- `MUD_VALCHAMP` — Value field in `MCHPSUTILISATDATA`; used for contract type (K1/K2/K3), carry sales date, BP codes, etc.
- `MUD_IDCHAMP = 26` — Contract type field ID in `MCHPSUTILISATDATA` (standard)
- `MUD_IDCHAMP = 35` — Contract type field ID in `MCHPSUTILISATDATA` (Company Store / KR export)
- `MUD_IDCHAMP = 1` — Carry sales delivery date field ID
- `MUD_IDCHAMP = 1-6` — BP codes per brand in ETA user fields (see Domain-Aware BP Joins below)
- `GL_LIBREART6` — Article type code (e.g. `Z001`, `Z002`, `Z003`)
- `GA_CHARLIBRE1` — SAP material number on article
- `GA_DOMAINE` — Brand/sales division code on article (`SHI`, `CPB`, `NAR`, `DRE`, `FRA`, `CPC`)
- `GA_LIBREART6` — Article type filter on `ARTICLEDIM_MODE`

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

### Domain-Aware BP Joins (Company Store / KR Export)

> **⚠️ Critical: use `GP_ETABLISSEMENT` for `MUD_CLEENTITE` in ETA BP joins — not `ET_ETABLISSEMENT`.**
>
> Even though `GP_ETABLISSEMENT = ET_ETABLISSEMENT` after the ETABLISS join, Cegid resolves the outer alias differently at runtime. Using `ET_ETABLISSEMENT` causes query failures or empty SHIP_TO results. Always use `GP_ETABLISSEMENT`.

> **⚠️ Cegid compatibility: do NOT use CASE in JOIN ON clauses.** Use scalar subqueries instead.

The establishment (ETA) record stores BP codes for all 6 brands in user fields 1–6:

| MUD_IDCHAMP | Brand | BP Alias |
|---|---|---|
| 1 | SHI (Shiseido) | SHIBP |
| 2 | CPB | CPBBP |
| 3 | NAR (Nars) | NARBP |
| 4 | DRE (Dior) | DREBP |
| 5 | FRA (Fragrance) | FRABP |
| 6 | CPC | CPCBP |

**ETA BP join + ARTICLEDIM_MODE (correct join order):**
```sql
/* Join ARTICLEDIM_MODE BEFORE BP joins — required for domain-aware routing */
LEFT JOIN ARTICLEDIM_MODE ON GA_ARTICLE = GL_ARTICLE

LEFT JOIN MCHPSUTILISATDATA SHIBP ON SHIBP.MUD_ENTITEMCD = 'ETA'
    AND SHIBP.MUD_CLEENTITE = GP_ETABLISSEMENT
    AND SHIBP.MUD_IDCHAMP = 1
LEFT JOIN MCHPSUTILISATDATA CPBBP ON CPBBP.MUD_ENTITEMCD = 'ETA'
    AND CPBBP.MUD_CLEENTITE = GP_ETABLISSEMENT
    AND CPBBP.MUD_IDCHAMP = 2
LEFT JOIN MCHPSUTILISATDATA NARBP ON NARBP.MUD_ENTITEMCD = 'ETA'
    AND NARBP.MUD_CLEENTITE = GP_ETABLISSEMENT
    AND NARBP.MUD_IDCHAMP = 3
LEFT JOIN MCHPSUTILISATDATA DREBP ON DREBP.MUD_ENTITEMCD = 'ETA'
    AND DREBP.MUD_CLEENTITE = GP_ETABLISSEMENT
    AND DREBP.MUD_IDCHAMP = 4
LEFT JOIN MCHPSUTILISATDATA FRABP ON FRABP.MUD_ENTITEMCD = 'ETA'
    AND FRABP.MUD_CLEENTITE = GP_ETABLISSEMENT
    AND FRABP.MUD_IDCHAMP = 5
LEFT JOIN MCHPSUTILISATDATA CPCBP ON CPCBP.MUD_ENTITEMCD = 'ETA'
    AND CPCBP.MUD_CLEENTITE = GP_ETABLISSEMENT
    AND CPCBP.MUD_IDCHAMP = 6
```

**SHIP_TO — CASE using outer BP aliases (Cegid-compatible):**
```sql
,CASE
    WHEN ARTICLEDIM_MODE.GA_DOMAINE = 'SHI' THEN SHIBP.MUD_VALCHAMP
    WHEN ARTICLEDIM_MODE.GA_DOMAINE = 'CPB' THEN CPBBP.MUD_VALCHAMP
    WHEN ARTICLEDIM_MODE.GA_DOMAINE = 'NAR' THEN NARBP.MUD_VALCHAMP
    WHEN ARTICLEDIM_MODE.GA_DOMAINE = 'DRE' THEN DREBP.MUD_VALCHAMP
    WHEN ARTICLEDIM_MODE.GA_DOMAINE = 'FRA' THEN FRABP.MUD_VALCHAMP
    WHEN ARTICLEDIM_MODE.GA_DOMAINE = 'CPC' THEN CPCBP.MUD_VALCHAMP
    ELSE ''
END AS SHIP_TO
```

**CONTRACTTYPE — scalar subquery (avoids CASE in JOIN ON):**
```sql
/* =============================================
   CONTRACTTYPE: Domain-aware BP code from ETA user fields
   Scalar subquery avoids CASE in JOIN ON (Cegid compatibility)
   ============================================= */
LEFT JOIN MCHPSUTILISATDATA CONTRACTTYPE ON CONTRACTTYPE.MUD_ENTITEMCD = 'CLI'
    AND CONTRACTTYPE.MUD_CLEENTITE = (
        SELECT CASE ARTICLEDIM_MODE.GA_DOMAINE
            WHEN 'SHI' THEN SHIBP.MUD_VALCHAMP
            WHEN 'CPB' THEN CPBBP.MUD_VALCHAMP
            WHEN 'NAR' THEN NARBP.MUD_VALCHAMP
            WHEN 'DRE' THEN DREBP.MUD_VALCHAMP
            WHEN 'FRA' THEN FRABP.MUD_VALCHAMP
            WHEN 'CPC' THEN CPCBP.MUD_VALCHAMP
            ELSE ''
        END
        FROM ARTICLEDIM_MODE
        JOIN MCHPSUTILISATDATA SHIBP ON SHIBP.MUD_ENTITEMCD = 'ETA' AND SHIBP.MUD_CLEENTITE = ET_ETABLISSEMENT AND SHIBP.MUD_IDCHAMP = 1
        JOIN MCHPSUTILISATDATA CPBBP ON CPBBP.MUD_ENTITEMCD = 'ETA' AND CPBBP.MUD_CLEENTITE = ET_ETABLISSEMENT AND CPBBP.MUD_IDCHAMP = 2
        JOIN MCHPSUTILISATDATA NARBP ON NARBP.MUD_ENTITEMCD = 'ETA' AND NARBP.MUD_CLEENTITE = ET_ETABLISSEMENT AND NARBP.MUD_IDCHAMP = 3
        JOIN MCHPSUTILISATDATA DREBP ON DREBP.MUD_ENTITEMCD = 'ETA' AND DREBP.MUD_CLEENTITE = ET_ETABLISSEMENT AND DREBP.MUD_IDCHAMP = 4
        JOIN MCHPSUTILISATDATA FRABP ON FRABP.MUD_ENTITEMCD = 'ETA' AND FRABP.MUD_CLEENTITE = ET_ETABLISSEMENT AND FRABP.MUD_IDCHAMP = 5
        JOIN MCHPSUTILISATDATA CPCBP ON CPCBP.MUD_ENTITEMCD = 'ETA' AND CPCBP.MUD_CLEENTITE = ET_ETABLISSEMENT AND CPCBP.MUD_IDCHAMP = 6
        WHERE ARTICLEDIM_MODE.GA_ARTICLE = LIGNE.GL_ARTICLE
    )
    AND CONTRACTTYPE.MUD_IDCHAMP = 26
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

## 7. ⚠️ CASE in JOIN ON — Cegid Compatibility

**Cegid may not support CASE expressions inside JOIN ON clauses.**
If you need conditional join logic based on a field value, use a **scalar subquery** instead of CASE in the ON clause.

**Wrong (may fail in Cegid):**
```sql
JOIN TIERS ON TIERS.T_TIERS = CASE ARTICLEDIM_MODE.GA_DOMAINE
    WHEN 'SHI' THEN SHIBP.MUD_VALCHAMP
    WHEN 'DRE' THEN DREBP.MUD_VALCHAMP
    ELSE ''
END
```

**Correct (scalar subquery):**
```sql
JOIN TIERS ON TIERS.T_TIERS = (
    SELECT CASE ARTICLEDIM_MODE.GA_DOMAINE
        WHEN 'SHI' THEN SHIBP.MUD_VALCHAMP
        WHEN 'DRE' THEN DREBP.MUD_VALCHAMP
        ELSE ''
    END
    FROM ARTICLEDIM_MODE
    JOIN MCHPSUTILISATDATA SHIBP ON ...
    WHERE ARTICLEDIM_MODE.GA_ARTICLE = LIGNE.GL_ARTICLE
)
```

See Section 2 for the full 6-brand domain-aware patterns.

---

## 8. Review Checklist

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
- [ ] ETA BP joins use `GP_ETABLISSEMENT` (not `ET_ETABLISSEMENT`) for `MUD_CLEENTITE`
- [ ] `ARTICLEDIM_MODE` is joined before BP joins

---

## 9. Writing Queries from Scratch

When writing a new Cegid query:

1. **Start with the standard join chain** for document queries:
   `PIECE A → LIGNE → ETABLISS → COMMERCIAL → ARTICLEDIM_MODE → ETA BP joins (SHIBP...CPCBP)`
   Add `CONTRACTTYPE` and `CARRYSALES` as LEFT JOINs from `MCHPSUTILISATDATA` when needed.

2. **Apply all dialect rules** from Section 1 from the start — don't write standard T-SQL and fix later.

3. **Structure CASE blocks** per Section 6 from the beginning.

4. **For Company Store / KR export** — use the domain-aware BP joins from Section 2. Join `ARTICLEDIM_MODE` before BP joins so `GA_DOMAINE` is available for routing. Always use `GP_ETABLISSEMENT` for ETA BP `MUD_CLEENTITE`.

5. **Standard ORDER BY** for document export queries:
   ```sql
   ORDER BY A.GP_NATUREPIECEG, A.GP_SOUCHE, A.GP_NUMERO, A.GP_ETATEXPORT, GL_CODEARTICLE
   ```

6. Refer to `references/cegid_full_db_reference.md` for full field listings when needed (893 tables, 21,155 fields). Use `references/tables.md` for curated join patterns and common field notes. Use `references/document_types.md` for the full list of GP_NATUREPIECEG codes.
