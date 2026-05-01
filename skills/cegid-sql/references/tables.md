# Cegid SQL — Curated Table Reference

> Curated notes for the most common query patterns. For the full 893-table, 21,155-field reference, see `cegid_full_db_reference.md`.

---

## Core Tables

| Table | Alias | Purpose |
|---|---|---|
| `PIECE` | `A` | Document/order header |
| `LIGNE` | — | Document line items |
| `ETABLISS` | — | Stores / establishments |
| `TIERS` | `T_TIERS` (field ref) | Customer master |
| `TIERSCOMPL` | — | Customer complement data |
| `MCHPSUTILISATDATA` | `CONTRACTTYPE`, `CARRYSALES` | Custom user fields |
| `ARTICLEDIM_MODE` | — | Article/product with dimensions |
| `GCTARFCONMODEART` | — | Price tariff by article |
| `TARIFMODE` | — | Tariff mode periods |
| `CHOIXEXT` | — | External choice/reference table |
| `DIMENSION` | — | Product dimension grid |
| `ARTICLE` | — | Product master |
| `COMMERCIAL` | — | Sales rep master |

---

## Standard Join Chain (Document Queries)

```sql
FROM PIECE A
JOIN LIGNE         ON GL_SOUCHE   = A.GP_SOUCHE
                  AND GL_NUMERO   = A.GP_NUMERO
                  AND GL_INDICEG  = A.GP_INDICEG
JOIN ETABLISS      ON ET_ETABLISSEMENT = A.GP_ETABLISSEMENT
JOIN TIERS         ON T_TIERS     = A.GP_TIERS
LEFT JOIN TIERSCOMPL ON TC_TIERS  = A.GP_TIERS
LEFT JOIN ARTICLEDIM_MODE ON GA_CODEARTICLE = GL_CODEARTICLE
                          AND GD_TAILLEMODE = GL_TAILLEMODE
```

---

## MCHPSUTILISATDATA Join Patterns

### Contract Type from Customer
```sql
LEFT JOIN MCHPSUTILISATDATA CONTRACTTYPE
    ON CONTRACTTYPE.MUD_ENTITEMCD = 'CLI'
    AND CONTRACTTYPE.MUD_CLEENTITE = T_TIERS
    AND CONTRACTTYPE.MUD_IDCHAMP = 26
```

### Contract Type from Destination Establishment (TEM AT1)
```sql
SELECT TOP 1 MUD_VALCHAMP
FROM MCHPSUTILISATDATA
JOIN ETABLISS ON ET_CHARLIBRE2 = MUD_CLEENTITE
WHERE MUD_ENTITEMCD = 'CLI'
  AND MUD_IDCHAMP = 26
  AND ET_ETABLISSEMENT = A.GP_ETABLISSDEST
```

### Carry Sales Delivery Date
```sql
LEFT JOIN MCHPSUTILISATDATA CARRYSALES
    ON CARRYSALES.MUD_ENTITEMCD = 'CLI'
    AND CARRYSALES.MUD_CLEENTITE = T_TIERS
    AND CARRYSALES.MUD_IDCHAMP = 1
```

---

## Company Store / KR Export — Domain-Aware BP Patterns

> **⚠️ Critical: use `GP_ETABLISSEMENT` for `MUD_CLEENTITE` in ETA BP joins — not `ET_ETABLISSEMENT`.**
> Even though `GP_ETABLISSEMENT = ET_ETABLISSEMENT` after the ETABLISS join, Cegid resolves outer aliases differently. Using `ET_ETABLISSEMENT` causes query failures or empty results.

> **⚠️ Cegid does not support CASE in JOIN ON clauses.** Use scalar subqueries instead.

### ETA BP User Fields (MUD_IDCHAMP 1–6)
Establishment records store BP codes for all 6 brands in user fields:

| MUD_IDCHAMP | Brand | Alias |
|---|---|---|
| 1 | SHI (Shiseido) | SHIBP |
| 2 | CPB | CPBBP |
| 3 | NAR (Nars) | NARBP |
| 4 | DRE (Dior) | DREBP |
| 5 | FRA (Fragrance) | FRABP |
| 6 | CPC | CPCBP |

### ETA BP Join (all 6 brands)
```sql
/* Join ARTICLEDIM_MODE before BP joins — required for domain-aware routing */
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

### SHIP_TO — CASE using outer BP aliases (Cegid-compatible)
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

### CONTRACTTYPE — Domain-aware scalar subquery (avoids CASE in JOIN ON)
Company Store uses `MUD_IDCHAMP = 26` (standard field ID for FFO):

```sql
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

## Common Fields

### PIECE (Header)
| Field | Description |
|---|---|
| `GP_NATUREPIECEG` | Document type (CF, TEM, FFO, BFA, TRE, CC, AVC) |
| `GP_ETATEXPORT` | Export state (ATT, AT1, AT2, AT3, AT4) |
| `GP_SOUCHE` | Document series |
| `GP_NUMERO` | Document number |
| `GP_INDICEG` | Document index |
| `GP_TIERS` | Customer code |
| `GP_ETABLISSEMENT` | Source establishment |
| `GP_ETABLISSDEST` | Destination establishment |
| `GP_DATEPIECE` | Document date |
| `GP_COMMERCIAL` | Sales rep code |

### LIGNE (Lines)
| Field | Description |
|---|---|
| `GL_CODEARTICLE` | Article/product code |
| `GL_TAILLEMODE` | Size/dimension mode |
| `GL_QTEFACT` | Invoiced quantity |
| `GL_PRIXUNET` | Unit net price |
| `GL_LIBREART6` | Article type code (Z001, Z002, Z003) |

### ETABLISS (Stores)
| Field | Description |
|---|---|
| `ET_ETABLISSEMENT` | Store code |
| `ET_CHARLIBRE1` | SAP Sold-to party |
| `ET_CHARLIBRE2` | SAP Ship-to party |
| `ET_CHARLIBRE3` | SAP Storage Location |

### ARTICLEDIM_MODE (Articles)
| Field | Description |
|---|---|
| `GA_CODEARTICLE` | Article code |
| `GA_CHARLIBRE1` | SAP material number |
| `GA_DOMAINE` | Brand/sales division (`SHI`, `CPB`, `NAR`, `DRE`, `FRA`, `CPC`) |
| `GA_LIBREART6` | Article type filter (`Z001` = standard) |
| `GD_TAILLEMODE` | Size mode |

### MCHPSUTILISATDATA (Custom Fields)
| Field | Description |
|---|---|
| `MUD_ENTITEMCD` | Entity type ('CLI' = customer, 'ETA' = establishment, 'DOC' = document) |
| `MUD_CLEENTITE` | Entity key (customer code, establishment code, or doc key) |
| `MUD_IDCHAMP` | Field ID (26 = contract type, 35 = Company Store contract type, 1 = carry sales date, 1-6 = BP codes per brand) |
| `MUD_VALCHAMP` | Field value |

---

## Article Type Codes (GL_LIBREART6)

| Code | Meaning |
|---|---|
| `Z001` | Standard retail article |
| `Z002` | Special/consignment article |
| `Z003` | Service article |

---

## Contract Types (CONTRACTTYPE.MUD_VALCHAMP)

| Value | Meaning |
|---|---|
| `K1` | Standard retail contract |
| `K2` | Concession / franchise contract |
| `K3` | Special/wholesale contract |

---

## Standard ORDER BY (Document Export Queries)

```sql
ORDER BY A.GP_NATUREPIECEG, A.GP_SOUCHE, A.GP_NUMERO, A.GP_ETATEXPORT, GL_CODEARTICLE
```
