# Viseo — Change Request Quotation Template Guide

> Reference document: `010_VISEO - SKR - CR - Customized report - Product Analysis 3_v1.0.docx`
> Template file: `CR_Quotation_Template.docx`

---

## Document Format (FIXED — never change)

| Property | Value |
|---|---|
| Page size | A4 (8.27 × 11.69 in) |
| Margins | top: 640 DXA (0.44"), right: 600 DXA, bottom: 900 DXA, left: 340 DXA |
| Default font | **Calibri**, 11 pt |
| Body text colour | `#000000` (black) |
| Label/address colour | `#A6A6A6` (grey) — Viseo address in header |
| Table header / TOTAL fill | `#13294B` (Viseo dark navy) |
| Table header text | `#FFFFFF` (white), bold |
| Main table borders | Black single, size 4 |
| Info-table borders | None (borderless) |
| Footer | Viseo banner image (full-width) + "VISEO HONG KONG Limited – Business Registration No.59325360" |

---

## Document Structure (FIXED — maintain this exact order)

```
1.  Header area        Viseo logo + "VISEO Hong Kong Limited" + address (grey, 8pt)
2.  Info table         Date | Version | To (customer) | Attn (contact) — borderless
3.  Title              "QUOTATION FOR CEGID CHANGE REQUEST – {{CR_NAME}}"
4.  Main body table    One single table with 4 columns [1908, 5812, 1276, 1285] DXA
      ├─ Row: Client
      ├─ Row: Vendor (always "VISEO Hong Kong Ltd, referred as VISEO")
      ├─ Row: "Scope of Work & Pricing" (section heading, full-width, bold)
      ├─ Row: "Context:" + bullet list (full-width)
      ├─ Row: "Proposal:" + rate intro text (full-width)
      ├─ Row: Pricing table HEADER (navy, white bold: Description | Man-days | Total)
      ├─ Rows: Pricing line items (bold-italic description | man-days | total)
      ├─ Row: TOTAL (navy, white bold) | grand total amount
      └─ Row: "Invoicing & Payment Schedule" | billing details + bullets
5.  Confidentiality notice  (small 6pt italic text)
6.  TERMS & CONDITIONS      (Heading 1 + bullet list)
7.  PROPOSAL ACCEPTANCE     (Heading 1 + acceptance text + signature table)
8.  APPENDIX / -End-
```

---

## All Variable Fields (`{{…}}` tokens)

### Document-level

| Token | What to replace with | Example |
|---|---|---|
| `{{DATE}}` | Quotation date | `Feb 25, 2026` |
| `{{VERSION}}` | Document version | `1.0` |
| `{{CURRENCY}}` | Currency symbol/code used throughout | `EUR` |
| `{{RATE_DEVELOPER}}` | Day-rate for consultant/developer | `700` |
| `{{RATE_PM}}` | Day-rate for Project Manager | `800` |
| `{{CR_NAME}}` | Change Request name (in main title) | `Customized report - Product Analysis 3` |

### Customer information

| Token | What to replace with | Example |
|---|---|---|
| `{{CUSTOMER_COMPANY}}` | Full legal company name | `SHISEIDO KOREA CO., LTD.` |
| `{{CUSTOMER_ADDRESS}}` | Full postal address | `3F, MDM TOWER 42, TEHERAN-RO 108-GIL, GANNAM-GU SEOUL 06176, KOREA` |
| `{{CUSTOMER_CONTACT}}` | Contact person full name | `Seong Joon Kim` |
| `{{CUSTOMER_SHORT}}` | Short customer name used in body text | `SHISEIDO` |
| `{{CUSTOMER_SIGNATORY_NAME}}` | Full name on signature block | `Seong Joon KIM` |
| `{{CUSTOMER_SIGNATORY_TITLE}}` | Job title on signature block | `CFO` |
| `{{PO_NUMBER}}` | Purchase Order number (leave blank if not yet known) | `PO-2026-001` |

### Context bullets (Row 4 of main table)

Add or remove bullet tokens as needed. Use `{{CONTEXT_BULLET_1}}` through `{{CONTEXT_BULLET_N}}`.
For sub-bullets (indented), use `{{CONTEXT_SUB_BULLET_1}}`, etc.

| Token | Example |
|---|---|
| `{{CONTEXT_BULLET_1}}` | `Shiseido is looking for a CR to have Product Analysis 3 in Cegid report…` |
| `{{CONTEXT_BULLET_2}}` | `The new customized report will be created in the report module.` |
| `{{CONTEXT_SUB_BULLET_1}}` | `The report detail will be collected further / recollected after CR kick-off` |

### Pricing line items

Each line item occupies one row. Add rows as needed; always keep the TOTAL row last.
Description text is **bold italic** in the original.

| Token | What it is | Example |
|---|---|---|
| `{{ITEM_N_DESCRIPTION}}` | Row description text (bold italic) | `Development of customized report - Product Analysis 3 – ref: Appendix` |
| `{{ITEM_N_MANDAYS}}` | Number of man-days (centred) | `3` |
| `{{ITEM_N_TOTAL}}` | Total cost for this row | `2,100.00` |
| `{{TOTAL_MANDAYS}}` | Grand total man-days | `4.5` |
| `{{TOTAL_AMOUNT}}` | Grand total amount | `3,250.00` |

**Fixed line items** (always present, only values change):
- **Misc** (PM / Requirement study and design) → `{{ITEM_1_MANDAYS}}`, `{{ITEM_1_TOTAL}}`
- **Development** → `{{ITEM_2_DESCRIPTION}}`, `{{ITEM_2_MANDAYS}}`, `{{ITEM_2_TOTAL}}`
- **UAT support and deployment** → `{{ITEM_3_MANDAYS}}`, `{{ITEM_3_TOTAL}}`

### Invoicing section

| Token | Example |
|---|---|
| `{{INVOICING_TIMING}}` | `Invoicing after UAT` |

---

## Formatting Rules (do NOT deviate)

- **Viseo address header**: Calibri 8pt, grey `#A6A6A6`, indented 380 DXA from left.
- **Info table**: borderless; `To:` / `Attn:` / `Date:` / `Version:` labels are bold.
- **Main title**: Calibri, large (Title style), bold, no underline.
- **Main body table borders**: black single, size 4, on all four sides of every cell.
- **Section headers inside table** ("Client", "Vendor", "Scope of Work & Pricing", "Context:", "Proposal:", "Invoicing & Payment Schedule"): bold, black, white fill.
- **Pricing header row + TOTAL row**: fill `#13294B`, text white bold.
- **Line item descriptions**: bold italic, Calibri 11pt.
- **Man-days column**: centred text.
- **Confidentiality notice**: Calibri 6pt (sz=12), normal weight.
- **Terms & Conditions + Proposal Acceptance**: Heading 1 style.
- **Signature table**: black single borders size 4, 2-column [4962 + 5572 DXA].
- **Footer**: Viseo banner image full-width + grey 7pt registration text.
- **Do not alter column widths, colour codes, or margin values.**

---

## Fixed Content (never changes per customer)

| Section | Fixed text |
|---|---|
| Vendor row | "VISEO Hong Kong Ltd, referred as VISEO" |
| Confidentiality notice | Full boilerplate text (see template) |
| T&C — validity | "This proposal is only **valid for 15 days**." |
| T&C — tax | "The rates are exclusive of any taxes applicable." |
| T&C — confidentiality | "The Vendor understands that Client's information…" |
| T&C — amendments | "This proposal may only be amended with the prior agreement of VISEO" |
| Bank transfer | Account # 801-137837-838 / HSBC / Swift: HSBCHKHHHKH |
| Viseo signatory | Guillaume Lassignardie, Managing Director |
| Viseo address | Unit 1102, Lee Garden One, 33 Hysan Avenue, Causeway Bay, Hong Kong |
| Footer registration | VISEO HONG KONG Limited – Business Registration No.59325360 |

---

## How to Generate a New CR Quotation

1. **Copy** `CR_Quotation_Template.docx` — do not edit the original.
2. **Replace** every `{{…}}` token with the correct value (see tables above).
3. **Pricing rows**: The template shows 3 line items (Misc, Development, UAT). Add or remove rows to match the actual CR scope, keeping the format.
4. **Context bullets**: Delete unused placeholders; add more if needed. Match the same indentation/bullet style.
5. **Appendix**: Insert supporting diagrams or specifications if available.
6. **Save as**: `Quotation of {{CUSTOMER_SHORT}} {{CR_NAME}} - Draft.docx`

---

## Quick Reference — Colours

| Use | Hex |
|---|---|
| Table header / TOTAL row background | `#13294B` |
| Header text / document background | `#FFFFFF` |
| Body text | `#000000` |
| Viseo address / footer text | `#A6A6A6` |
| Placeholder text (template only) | `#888888` |

---

## File Reference

| File | Purpose |
|---|---|
| `CR_Quotation_Template.docx` | Master template — copy for each new CR |
| `CR_QUOTATION_TEMPLATE_GUIDE.md` | This skill reference guide |
| `build_cr_template_v2.js` | Node.js script that regenerates the template from scratch |
