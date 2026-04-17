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
| `GD_TAILLEMODE` | Size mode |

### MCHPSUTILISATDATA (Custom Fields)
| Field | Description |
|---|---|
| `MUD_ENTITEMCD` | Entity type ('CLI' = customer) |
| `MUD_CLEENTITE` | Entity key (customer code) |
| `MUD_IDCHAMP` | Field ID (26 = contract type, 1 = carry sales date) |
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
