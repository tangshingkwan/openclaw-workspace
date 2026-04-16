# Wiki Log

> Append-only chronological record of all wiki activity.
> Format: `## [YYYY-MM-DD] type | Title`

---

## [2026-04-16] ingest | Batch: All remaining Y2Plugins + v26 modules
- 13 Y2Plugins: Customer, Employee, Inventory, Product, Reservation, SalesConditions, Settings, Supplier, TaxEngine, Transfer, SalesExternal, InventoryCount, InventoryTracking
- 6 v26 modules: Procurement, Workforce, Budgeting, Localization, Finance, Foundation
- Total sources now: 35
- Pages touched: `wiki/sources/y2plugin-*.md`, `wiki/sources/y2-v26-*.md`

## [2026-04-16] ingest | Batch: 4 RFE documents
- RFE Introduction, Implementation, Best Practices, Migration Guide
- CRITICAL for SynagieAPI — RFE is the file exchange layer
- Pages touched: `wiki/sources/y2-rfe-*.md`

## [2026-04-16] ingest | Batch: 5 Front Office Back Office v26 modules
- POS Management, Product/Inventory, CRM/Clienteling, Omni-Channel, Transverse Features
- Pages touched: `wiki/sources/y2-v26-*.md`

## [2026-04-16] ingest | Batch: 6 Y2Plugins + 3 Connectors
- Plugins: InventoryMovement, Voucher, TaskScheduler, Sourcing, Audit
- Connectors: Adyen, Avalara, Vertex
- Pages touched: `wiki/sources/y2plugin-*.md`, `wiki/sources/y2-connector-*.md`

## [2026-04-16] ingest | Y2Plugin CustomerOrder V26
- Source: `documents/Y2/Common/Webservices/Follow-up Notes/Y2Plugin CustomerOrder V26/`
- Key takeaways: Customer order flows (CreateFrom2/Update/Replace/GetList), e-commerce pickup points, idempotency via OperationUid, CreateFrom deprecated (deadline 2/1/2028)
- Pages touched: `wiki/sources/y2plugin-customerorder-v26.md`

## [2026-04-16] ingest | Y2Plugin Company V26
- Source: `documents/Y2/Common/Webservices/Follow-up Notes/Y2Plugin Company V26/`
- Key takeaways: Store/warehouse retrieval, store settings for document types, POS configurations
- Pages touched: `wiki/sources/y2plugin-company-v26.md`

## [2026-04-15] ingest | Consuming Y2 Web Services
- Source: `documents/Y2/Common/Webservices/Consuming Y2 Web Services/`
- Key takeaways: SOAP integration guide, 6 languages supported (PHP/C#/Python/Ruby/Java/JS), Basic/NTLM/Cookie auth, WSDL caching, data types (arrays/dates/enum)
- Pages touched: `wiki/sources/y2-webservices-guide.md`

## [2026-04-15] setup | LLM Wiki Initialized
- Wiki schema created: `wiki/WIKI.md`
- Directories set up: `raw/`, `wiki/`, `assets/`
- Index and log initialized
- Next: Start ingesting sources!

---

*Add new entries above, never delete old ones.*
