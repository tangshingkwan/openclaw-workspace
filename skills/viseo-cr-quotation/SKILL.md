---
name: viseo-cr-quotation
description: >
  Generate a complete, professional Viseo Change Request (CR) Quotation .docx document for Cegid POS
  implementation projects. Use this skill whenever the user wants to create a quotation, draft a CR quote,
  prepare a change request proposal, or produce a customer-facing pricing document for any Cegid implementation
  work. Trigger on: "create quotation", "new quotation", "quotation for [customer]", "CR quote", "change request
  quote", "prepare a quote", "draft a quotation", "make a quotation", "write a CR", "pricing document for
  customer". Also trigger when the user provides customer details, a scope/context description, or line items
  with man-days and wants a formal Word document output. Do not use for informal estimates, internal notes, or
  non-Viseo quotation formats.
---

# Viseo CR Quotation Generator

This skill produces a complete, ready-to-send Viseo Change Request Quotation as a `.docx` file, following
the exact Viseo brand format used in Cegid implementation projects.

## Document overview

The output is a single-page (typically) A4 Word document with:
1. Viseo logo + address header
2. Info block: Date, Version, customer To/Attn
3. Title: "QUOTATION FOR CEGID CHANGE REQUEST – [CR Name]"
4. Main table: Client/Vendor → Scope → Context bullets → Proposal/pricing → Invoicing
5. Confidentiality notice
6. Terms & Conditions (fixed boilerplate)
7. Proposal Acceptance + signature table
8. Appendix placeholder

See `references/template_guide.md` for the full formatting rules and all `{{VARIABLE}}` tokens.

---

## Step 1 — Collect required information

Before generating, gather these details from the user's message or ask for what's missing.
**Do not generate a document with unknown placeholders** — ask first if any required field is absent.

### Required fields

| Field | What to ask if missing |
|---|---|
| `cr_name` | "What is the name / title of this Change Request?" |
| `customer.company` | "What is the customer's full legal company name?" |
| `customer.address` | "What is the customer's full address?" |
| `customer.contact` | "Who is the primary contact / Attn person?" |
| `customer.short` | Derive from company name if obvious (e.g., "SHISEIDO") |
| `context_bullets` | "Can you describe the scope/context of this CR? (bullet points)" |
| `line_items` | "What are the work items, man-days, and costs?" |
| `total_amount` | "What is the grand total (in currency)?" |

### Optional fields (use defaults if not provided)

| Field | Default |
|---|---|
| `date` | Today's date (formatted e.g. "Apr 5, 2026") |
| `version` | `"1.0"` |
| `currency` | `"EUR"` |
| `rate_developer` | `700` |
| `rate_pm` | `800` |
| `customer.signatory_name` | Same as `customer.contact` |
| `customer.signatory_title` | `""` (leave blank) |
| `customer.po_number` | `""` (leave blank) |
| `invoicing.timing` | `"Invoicing after UAT"` |

---

## Step 2 — Build the config JSON

Once you have all information, create a file at `/tmp/cr_quotation_config.json` with this structure:

```json
{
  "date": "Apr 5, 2026",
  "version": "1.0",
  "currency": "EUR",
  "rate_developer": 700,
  "rate_pm": 800,
  "cr_name": "Customized report - Product Analysis 3",
  "customer": {
    "company": "SHISEIDO KOREA CO., LTD.",
    "address": "3F, MDM TOWER 42, TEHERAN-RO 108-GIL, GANNAM-GU SEOUL 06176, KOREA",
    "contact": "Seong Joon Kim",
    "short": "SHISEIDO",
    "signatory_name": "Seong Joon KIM",
    "signatory_title": "CFO",
    "po_number": ""
  },
  "context_bullets": [
    "Shiseido is looking for a Change Request (CR) to have Product Analysis 3 in Cegid report turned in Customized reports",
    "The new customized report - Product Analysis 3 - will be created in the report module.",
    "Pop-up to another set of report or data won't be available for this customized report.",
    "The scope of this CR includes Requirement Study, Design, Project Management, Development, UAT Support and Deployment",
    "Any work not explicitly described herein will be considered out of scope and require a separate statement of work and agreement."
  ],
  "context_sub_bullets": {
    "1": [
      "The report detail will be collected further / recollected after CR kick-off",
      "It will be following the SKPOS layout to create the comparison period"
    ]
  },
  "line_items": [
    {
      "description_lines": ["Misc", "- PM", "- Requirement study and design"],
      "mandays": 1,
      "total": "800.00"
    },
    {
      "description_lines": ["Development of customized report - Product Analysis 3 \u2013 ref: Appendix"],
      "mandays": 3,
      "total": "2,100.00"
    },
    {
      "description_lines": ["UAT support and deployment"],
      "mandays": 0.5,
      "total": "350.00"
    }
  ],
  "total_mandays": "4.5",
  "total_amount": "3,250.00",
  "invoicing": {
    "timing": "Invoicing after UAT"
  },
  "output_filename": "Quotation of SHISEIDO CR - Draft.docx"
}
```

**Notes on `context_sub_bullets`:** keys are the 0-based index of the parent bullet after which sub-bullets should appear. If no sub-bullets are needed, use `{}`.

**Notes on `line_items`:** `description_lines` is an array. First element is the main bold-italic label. Additional elements (starting with `-`) are bold-italic sub-labels.

---

## Step 3 — Run the build script

```bash
node <SKILL_BASE_DIR>/scripts/build_quotation.js \
  /tmp/cr_quotation_config.json \
  "<OUTPUT_PATH>" \
  "<SKILL_BASE_DIR>"
```

- Replace `<SKILL_BASE_DIR>` with the base directory shown at the top of this skill (e.g. `/sessions/.../viseo-cr-quotation`)
- Replace `<OUTPUT_PATH>` with the full path where the .docx should be saved (typically the user's workspace folder)
- The script outputs the .docx and prints `✅ Quotation created: <path>` on success

**Example:**
```bash
node /sessions/fervent-magical-einstein/mnt/.claude/skills/viseo-cr-quotation/scripts/build_quotation.js \
  /tmp/cr_quotation_config.json \
  "/sessions/fervent-magical-einstein/mnt/template/Quotation of SHISEIDO CR - Draft.docx" \
  /sessions/fervent-magical-einstein/mnt/.claude/skills/viseo-cr-quotation
```

---

## Step 4 — Validate and share

After the script succeeds:

```bash
python /sessions/fervent-magical-einstein/mnt/.claude/skills/docx/scripts/office/validate.py "<OUTPUT_PATH>"
```

Then provide the user with a `computer://` link to the file.

---

## Important formatting rules (do not deviate)

- Font: **Calibri**, 11pt throughout
- Page: **A4**, margins top=640 right=600 bottom=900 left=340 DXA
- Line item descriptions: **bold italic**
- Table header & TOTAL row: navy `#13294B` fill, white bold text
- All main table borders: black single, size 4
- Info table (Date/Version/To/Attn): **no borders**
- Footer: Viseo banner image + grey registration text

Full formatting reference: `references/template_guide.md`
