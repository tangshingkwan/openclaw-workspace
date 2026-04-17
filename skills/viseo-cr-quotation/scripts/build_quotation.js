/**
 * Viseo CR Quotation Builder
 * Usage: node build_quotation.js <config.json> <output.docx> <skill_base_dir>
 *
 * Produces a complete, filled Viseo Change Request Quotation .docx
 * following the exact format of the reference document.
 */

const path = require('path');
const fs   = require('fs');

// ── Resolve docx module from multiple possible install locations ─────────────
let docxModule;
const candidates = [
  path.join(__dirname, '../../node_modules/docx'),
  path.join(process.cwd(), 'node_modules/docx'),
  'docx',
];
for (const c of candidates) {
  try { docxModule = require(c); break; } catch (_) {}
}
if (!docxModule) {
  console.error('❌  docx module not found. Run: npm install docx');
  process.exit(1);
}

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, Footer, AlignmentType, BorderStyle, WidthType,
  ShadingType, VerticalAlign, HeadingLevel, LevelFormat,
} = docxModule;

// ── Args ─────────────────────────────────────────────────────────────────────
const [,, configPath, outputPath, skillBaseDir] = process.argv;
if (!configPath || !outputPath || !skillBaseDir) {
  console.error('Usage: node build_quotation.js <config.json> <output.docx> <skill_base_dir>');
  process.exit(1);
}

const cfg = JSON.parse(fs.readFileSync(configPath, 'utf8'));
const LOGO_IMG   = fs.readFileSync(path.join(skillBaseDir, 'assets', 'viseo_logo.png'));
const FOOTER_IMG = fs.readFileSync(path.join(skillBaseDir, 'assets', 'viseo_footer.png'));

// ── Brand / layout constants ──────────────────────────────────────────────────
const NAVY  = "13294B";
const WHITE = "FFFFFF";
const BLACK = "000000";
const GREY  = "A6A6A6";

// Table 1 (info): cols [657, 7086, 2111]
const T1 = { C1: 657, C2: 7086, C3: 2111 };
// Table 2 (body): cols [1908, 5812, 1276, 1285]
const T2 = {
  C1: 1908, C2: 5812, C3: 1276, C4: 1285,
  get W()     { return this.C1+this.C2+this.C3+this.C4; },   // 10281
  get C1C2()  { return this.C1+this.C2; },                   // 7720
  get C2C3C4(){ return this.C2+this.C3+this.C4; },           // 8373
  get C1C2C3(){ return this.C1+this.C2+this.C3; },           // 8996
};
// Table 3 (signatures): cols proportionally scaled to match T2 width (10281) at indent 497
const T3 = { C1: 4844, C2: 5437 };

// ── Border helpers ────────────────────────────────────────────────────────────
const bk   = () => ({ style: BorderStyle.SINGLE, size: 4, color: BLACK });
const none = () => ({ style: BorderStyle.NONE,   size: 0, color: BLACK });
const allB = { top: bk(), bottom: bk(), left: bk(), right: bk() };
const noB  = { top: none(), bottom: none(), left: none(), right: none() };

// ── Run / paragraph factories ─────────────────────────────────────────────────
function r(text, o = {}) {
  return new TextRun({
    text,
    font:    o.font    || 'Calibri',
    size:    o.size    || 22,
    color:   o.color   || BLACK,
    bold:    !!o.bold,
    italics: !!o.italics,
    underline: o.underline ? { type: 'single' } : undefined,
  });
}

function p(runsOrText, o = {}) {
  const children = typeof runsOrText === 'string'
    ? [r(runsOrText, o)]
    : Array.isArray(runsOrText) ? runsOrText : [runsOrText];
  return new Paragraph({
    children,
    alignment: o.align || AlignmentType.LEFT,
    spacing: { before: o.before || 0, after: o.after || 0 },
    indent: o.indent ? { left: o.indent } : undefined,
  });
}

function blank(size = 22) {
  return new Paragraph({ children: [r('', { size })], spacing: { after: 0 } });
}

// ── Cell factory ──────────────────────────────────────────────────────────────
function cell(children, width, o = {}) {
  return new TableCell({
    width:        { size: width, type: WidthType.DXA },
    columnSpan:   o.span   || 1,
    borders:      o.borders || allB,
    shading:      { fill: o.fill || WHITE, type: ShadingType.CLEAR },
    margins:      o.margins || { top: 40, bottom: 40, left: 80, right: 80 },
    verticalAlign: o.vAlign || VerticalAlign.CENTER,
    children:     Array.isArray(children) ? children : [children],
  });
}

function navyCell(children, width, o = {}) {
  return cell(children, width, { ...o, fill: NAVY });
}

// ── Bullet list helper ────────────────────────────────────────────────────────
function bulletP(runsOrText, ref, indent = 440) {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    children: typeof runsOrText === 'string' ? [r(runsOrText)] : runsOrText,
    spacing: { before: 0, after: 0 },
    indent: { left: indent, hanging: 220 },
  });
}

// ── Context bullets with optional sub-bullets ─────────────────────────────────
function buildContextParagraphs(bullets, subBullets) {
  const paras = [p([r('Context:', { bold: true })]), blank()];
  bullets.forEach((text, i) => {
    paras.push(bulletP(text, 'contextBullets'));
    const subs = subBullets && subBullets[String(i)];
    if (subs) {
      subs.forEach(sub => paras.push(bulletP(sub, 'contextBullets', 720)));
    }
  });
  return paras;
}

// ── Pricing rows ──────────────────────────────────────────────────────────────
function headerRow(currency) {
  return new TableRow({ children: [
    navyCell([p([r('Description', { bold: true, color: WHITE })])],           T2.C1C2, { span: 2 }),
    navyCell([p([r('Man-days',    { bold: true, color: WHITE })], { align: AlignmentType.CENTER })], T2.C3),
    navyCell([p([r(`Total (${currency})`, { bold: true, color: WHITE })])],  T2.C4),
  ]});
}

function dataRow(item) {
  const descParas = (item.description_lines || [item.description]).map((line, i) =>
    p([r(line, { bold: true, italics: true })], { after: 0 })
  );
  return new TableRow({ children: [
    cell(descParas, T2.C1C2, { span: 2, vAlign: VerticalAlign.TOP }),
    cell([p([r(String(item.mandays))], { align: AlignmentType.CENTER })], T2.C3),
    cell([p([r(item.total)])], T2.C4),
  ]});
}

function totalRow(cfg) {
  return new TableRow({ children: [
    navyCell([p([r(`TOTAL in ${cfg.currency}`, { bold: true, color: WHITE })])],
      T2.C1C2C3, { span: 3 }),
    cell([p([r(`${cfg.total_mandays} man-days / ${cfg.currency} ${cfg.total_amount}`, { bold: true })])],
      T2.C4),
  ]});
}

// ── Invoicing row ─────────────────────────────────────────────────────────────
function invoicingRow(cfg) {
  return new TableRow({
    children: [
      cell([p([r('Invoicing & Payment Schedule', { bold: true })])],
        T2.C1, { vAlign: VerticalAlign.TOP }),
      cell([
        p([r(`Billing will be issued by VISEO to ${cfg.customer.short || cfg.customer.company}`)]),
        blank(),
        bulletP([r('Billing & payment are in '), r(cfg.currency, { bold: true })], 'invoicingBullets'),
        bulletP(cfg.invoicing.timing || 'Invoicing after UAT', 'invoicingBullets'),
        bulletP('Above pricing excludes any taxes that might be applicable. All taxes are borne by the customer.', 'invoicingBullets'),
      ], T2.C2C3C4, { span: 3, vAlign: VerticalAlign.TOP }),
    ],
  });
}

// ── Main document builder ─────────────────────────────────────────────────────
const doc = new Document({
  numbering: {
    config: [
      { reference: 'contextBullets',   levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 440, hanging: 220 } } } }] },
      { reference: 'invoicingBullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 440, hanging: 220 } } } }] },
      { reference: 'termsBullets',     levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 440, hanging: 220 } } } }] },
    ],
  },

  sections: [{
    properties: {
      page: {
        size:   { width: 11900, height: 16840 },
        margin: { top: 640, right: 600, bottom: 900, left: 340, header: 0, footer: 713 },
      },
    },

    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            spacing: { after: 0 },
            alignment: AlignmentType.LEFT,
            indent: { left: -340 },
            children: [new ImageRun({
              type: 'png', data: FOOTER_IMG,
              transformation: { width: 794, height: 39 },
              altText: { title: 'Footer', description: 'Footer', name: 'Footer' },
            })],
          }),
          new Paragraph({
            spacing: { after: 0 },
            alignment: AlignmentType.LEFT,
            children: [r('VISEO HONG KONG Limited \u2013 Business Registration No.59325360',
              { size: 14, color: GREY })],
          }),
        ],
      }),
    },

    children: [

      // ── Logo + address ────────────────────────────────────────────────────
      new Paragraph({
        spacing: { before: 0, after: 0 }, indent: { left: 497 },
        children: [new ImageRun({
          type: 'png', data: LOGO_IMG,
          transformation: { width: 136, height: 42 },
          altText: { title: 'Viseo Logo', description: 'Viseo Logo', name: 'Viseo Logo' },
        })],
      }),
      blank(24),
      new Paragraph({ spacing: { before: 95, after: 0 }, indent: { left: 497 },
        children: [r('VISEO Hong Kong Limited', { size: 16, bold: true, color: GREY })] }),
      new Paragraph({ spacing: { before: 1, after: 0 }, indent: { left: 497 },
        children: [r('Unit 1102, Lee Garden One,', { size: 16, color: GREY })] }),
      new Paragraph({ spacing: { before: 1, after: 0 }, indent: { left: 497 },
        children: [r('33 Hysan Avenue, Causeway Bay, Hong Kong', { size: 16, color: GREY })] }),
      blank(12),

      // ── Info table (borderless) ───────────────────────────────────────────
      new Table({
        width: { size: T1.C1+T1.C2+T1.C3, type: WidthType.DXA },
        columnWidths: [T1.C1, T1.C2, T1.C3],
        indent: { size: 522, type: WidthType.DXA },
        rows: [
          new TableRow({ children: [
            cell([blank()],                             T1.C1, { borders: noB }),
            cell([p([r('Date:', { bold: true })], { align: AlignmentType.RIGHT })],     T1.C2, { borders: noB }),
            cell([p(cfg.date || '')],                   T1.C3, { borders: noB }),
          ]}),
          new TableRow({ children: [
            cell([blank()],                             T1.C1, { borders: noB }),
            cell([p([r('Version:', { bold: true })], { align: AlignmentType.RIGHT })],  T1.C2, { borders: noB }),
            cell([p(cfg.version || '1.0')],             T1.C3, { borders: noB }),
          ]}),
          new TableRow({ children: [
            cell([p([r('To:', { bold: true })])],       T1.C1, { borders: noB }),
            cell([
              p([r(cfg.customer.company, { bold: true })]),
              p(cfg.customer.address || ''),
            ], T1.C2, { borders: noB, vAlign: VerticalAlign.TOP }),
            cell([blank()], T1.C3, { borders: noB }),
          ]}),
          new TableRow({ children: [
            cell([p([r('Attn:', { bold: true })])],     T1.C1, { borders: noB }),
            cell([p(cfg.customer.contact || '')],       T1.C2, { borders: noB }),
            cell([blank()],                             T1.C3, { borders: noB }),
          ]}),
        ],
      }),

      blank(21),

      // ── Title ─────────────────────────────────────────────────────────────
      new Paragraph({
        heading: HeadingLevel.TITLE,
        alignment: AlignmentType.CENTER,
        children: [
          r('QUOTATION FOR CEGID CHANGE REQUEST \u2013 ', { bold: true, size: 26 }),
          r(cfg.cr_name || '', { bold: true, size: 26 }),
        ],
        spacing: { after: 0 },
      }),
      blank(12),

      // ── Main body table ───────────────────────────────────────────────────
      new Table({
        width: { size: T2.W, type: WidthType.DXA },
        columnWidths: [T2.C1, T2.C2, T2.C3, T2.C4],
        indent: { size: 497, type: WidthType.DXA },
        rows: [

          // Client
          new TableRow({ children: [
            cell([p([r('Client', { bold: true })])], T2.C1),
            cell([
              p([r(cfg.customer.company, { bold: true }),
                 r(', referred as ', {}),
                 r(cfg.customer.short || cfg.customer.company, { bold: true })]),
            ], T2.C2C3C4, { span: 3 }),
          ]}),

          // Vendor
          new TableRow({ children: [
            cell([p([r('Vendor', { bold: true })])], T2.C1),
            cell([p([r('VISEO Hong Kong Ltd', { bold: true }),
                     r(', referred as ', {}),
                     r('VISEO', { bold: true })])],
              T2.C2C3C4, { span: 3 }),
          ]}),

          // Scope of Work heading
          new TableRow({ children: [
            cell([p([r('Scope of Work & Pricing', { bold: true })])],
              T2.W, { span: 4 }),
          ]}),

          // Context
          new TableRow({ children: [
            cell(
              buildContextParagraphs(cfg.context_bullets || [], cfg.context_sub_bullets || {}),
              T2.W, { span: 4, vAlign: VerticalAlign.TOP, margins: { top: 50, bottom: 50, left: 100, right: 100 } }
            ),
          ]}),

          // Proposal + rate intro
          new TableRow({ children: [
            cell([
              p([r('Proposal:', { bold: true })]),
              p([r(`The rate of ${cfg.currency}${cfg.rate_developer} for consultant/developer, and ${cfg.currency}${cfg.rate_pm} for PM per man-day will be used. Calculation will be as below:`)]),
            ], T2.W, { span: 4, vAlign: VerticalAlign.TOP }),
          ]}),

          // Pricing header
          headerRow(cfg.currency),

          // Pricing data rows
          ...(cfg.line_items || []).map(item => dataRow(item)),

          // Total
          totalRow(cfg),

          // Invoicing
          invoicingRow(cfg),
        ],
      }),

      blank(12),

      // ── Confidentiality notice ────────────────────────────────────────────
      new Paragraph({
        spacing: { after: 0 },
        indent: { left: 497 },
        children: [r(
          'This document and the information it contains are strictly private and confidential and are ' +
          'intended only for people who need to know about it in the context of the project, negotiations ' +
          'or services entrusted to VISEO. This document and the information it contains cannot be used by, ' +
          'reproduced or communicated to anyone who is not the recipient and/or outside its context, without ' +
          'VISEO\u2019s prior permission and in breach of the laws and rules of business secrecy',
          { size: 12 }
        )],
      }),
      blank(12),

      // ── Terms & Conditions ────────────────────────────────────────────────
      new Paragraph({ heading: HeadingLevel.HEADING_1,
        children: [r('TERMS & CONDITIONS', { bold: true })], spacing: { after: 0 }, indent: { left: 497 } }),
      blank(),
      bulletP([r('This proposal is only '), r('valid for 15 days', { bold: true }), r('.')], 'termsBullets', 717),
      bulletP('The rates are exclusive of any taxes applicable.', 'termsBullets', 717),
      bulletP('The Vendor understands that Client\u2019s information on its business and the agreed scope of work is confidential and will not disclose to any other parties beside those involved in the engagement.', 'termsBullets', 717),
      bulletP('This proposal may only be amended with the prior agreement of VISEO', 'termsBullets', 717),
      bulletP([r('Payment by Bank Transfer at:', { bold: true })], 'termsBullets', 717),
      p('Account # 801-137837-838', { indent: 937 }),
      p('The Hongkong and Shanghai Banking Corporation Limited 1 Queen\u2019s Road, Central, HKG', { indent: 937 }),
      p('Swift: HSBCHKHHHKH', { indent: 937 }),
      blank(26),

      // ── Proposal Acceptance ───────────────────────────────────────────────
      new Paragraph({ heading: HeadingLevel.HEADING_1,
        children: [r('PROPOSAL ACCEPTANCE', { bold: true })], spacing: { after: 0 }, indent: { left: 497 } }),
      blank(21),
      new Paragraph({
        spacing: { after: 0 },
        indent: { left: 497 },
        children: [
          r('Signature below indicates customer\u2019s acceptance of this quotation subject to the above-mentioned '),
          r('Terms and Conditions', { italics: true, bold: true }),
          r('. This constitutes an authorization for VISEO to begin delivery and to issue invoices per the above payment schedule.'),
        ],
      }),
      blank(),

      // Signature table
      new Table({
        width: { size: T3.C1+T3.C2, type: WidthType.DXA },
        columnWidths: [T3.C1, T3.C2],
        indent: { size: 497, type: WidthType.DXA },
        rows: [
          new TableRow({ children: [
            cell([
              p([r('VISEO Hong Kong Limited', { bold: true })]),
              p('Unit 1102, Lee Garden One,'),
              p('33 Hysan Avenue, Causeway Bay, Hong Kong'),
            ], T3.C1, { vAlign: VerticalAlign.TOP }),
            cell([
              p([r(cfg.customer.company, { bold: true })]),
              p(cfg.customer.address || ''),
            ], T3.C2, { vAlign: VerticalAlign.TOP }),
          ]}),
          new TableRow({ children: [
            cell([
              blank(28),
              blank(28),
              blank(28),
              p([r('Guillaume Lassignardie', { bold: true })]),
              p('Managing Director'),
            ], T3.C1, { vAlign: VerticalAlign.TOP }),
            cell([
              blank(28),
              blank(28),
              blank(28),
              p([r(cfg.customer.signatory_name || cfg.customer.contact || '', { bold: true })]),
              p(cfg.customer.signatory_title || ''),
            ], T3.C2, { vAlign: VerticalAlign.TOP }),
          ]}),
          new TableRow({ children: [
            cell([blank()], T3.C1),
            cell([
              p('Purchase Order Number (if needed):'),
              blank(),
              p(cfg.customer.po_number || ''),
            ], T3.C2, { vAlign: VerticalAlign.TOP }),
          ]}),
          new TableRow({ children: [
            cell([
              p('Return signed copies to:'),
              p([r('VISEO Hong Kong Limited', { bold: true })]),
              p('Unit 1102, Lee Garden One,'),
              p('33 Hysan Avenue, Causeway Bay, Hong Kong'),
            ], T3.C1, { vAlign: VerticalAlign.TOP }),
            cell([
              p('Invoice Name & Address:'),
              p([r(cfg.customer.company, { bold: true })]),
              p(cfg.customer.address || ''),
            ], T3.C2, { vAlign: VerticalAlign.TOP }),
          ]}),
        ],
      }),
      blank(),
      p('Please sign two copies of this document and return to VISEO with your Purchase Order. Viseo will sign and return one copy for your record.', { indent: 497 }),
      blank(),

      // ── Appendix (only if cfg.appendix is provided) ───────────────────────
      ...(cfg.appendix
        ? [
            new Paragraph({ children: [r('APPENDIX:', { bold: true })] }),
            blank(),
            new Paragraph({ children: [r(cfg.appendix, {})] }),
            blank(),
            // Append images if provided
            ...(cfg.appendix_images || []).map(imgPath => {
              try {
                const imgData = fs.readFileSync(imgPath);
                return new Paragraph({
                  spacing: { before: 100, after: 100 },
                  alignment: AlignmentType.CENTER,
                  children: [new ImageRun({
                    type: 'png',
                    data: imgData,
                    transformation: { width: 500, height: 300 },
                    altText: { title: 'Appendix Image', description: 'Appendix Image', name: 'AppendixImage' },
                  })],
                });
              } catch (e) {
                return new Paragraph({ children: [r(`[Image not found: ${imgPath}]`)] });
              }
            }),
            new Paragraph({ children: [r('-End-', { bold: true })] }),
          ]
        : [
            new Paragraph({ children: [r('-End-', { bold: true })], alignment: AlignmentType.CENTER }),
          ]
      ),
    ],
  }],
});

// ── Write output ──────────────────────────────────────────────────────────────
Packer.toBuffer(doc).then(buf => {
  const dir = path.dirname(outputPath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(outputPath, buf);
  console.log(`✅  Quotation created: ${outputPath}`);
}).catch(err => {
  console.error('❌  Build failed:', err.message);
  process.exit(1);
});
