# Cegid Document Types Reference

This file lists all known `GP_NATUREPIECEG` codes used in the Cegid Y2 database.

---

## Document Type Codes (GP_NATUREPIECEG)

| Code | Description |
|------|-------------|
| `AAF` | Request for financial credit |
| `AF` | Supplier financial credit note |
| `AFF` | Supplier invoice notice |
| `AFS` | Supplier credit note on inventory |
| `ALF` | Delivery notice |
| `ANR` | Return notice |
| `AVC` | Customer credit note |
| `AVS` | Credit on inventory |
| `BEX` | Special input drafts |
| `BFA` | Supplier return |
| `BLC` | Customer delivery |
| `BLF` | Supplier receipt |
| `BLR` | Return receipt |
| `BRF` | Supplier return draft |
| `BSX` | Special output drafts |
| `BTR` | Transfer worksheet |
| `CC` | Customer order |
| `CDI` | Available order |
| `CF` | Purchase order |
| `DDI` | Customer reservation requests |
| `DE` | Customer quotation |
| `DEF` | Purchase order proposal |
| `DTR` | Transfer request |
| `EEX` | Special inputs |
| `FAC` | Customer invoice |
| `FAF` | Financial customer invoice |
| `FCF` | Replenishment order |
| `FF` | Supplier invoice |
| `FFA` | Receipt on hold |
| `FFE` | Receipt imprint |
| `FFF` | Financial supplier invoice |
| `FFO` | Receipt |
| `FIC` | Fictitious type MODE |
| `INV` | Inventory discrepancies |
| `PRE` | Delivery worksheet |
| `PRO` | Pro-forma invoice |
| `PRT` | Loan |
| `RDI` | Customer reservations |
| `SEX` | Special outputs |
| `TEM` | Sent transfer |
| `TRE` | Received transfer |
| `TRV` | Transfer notice |

---

## Notes

- `GP_NATUREPIECEG` is the primary document type discriminator in the `PIECE` table.
- Use this field in `WHERE` or `CASE` clauses to filter/classify document flows.
- Common codes used in SKR interface exports: `CF`, `TEM`, `FFO`, `BFA`, `TRE`, `CC`, `AVC`, `FAC`.
