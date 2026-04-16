---
title: "Y2Plugin CustomerOrder V26"
type: source
source-type: document
date-added: 2026-04-16
tags: [cegid, y2, plugin, customerorder, ecommerce, soap, api]
summary: "Y2Plugin for managing customer order flows — create, update, transform orders, handle deliveries, pickup points. Key for SynagieAPI e-commerce integration."
---

# Y2Plugin CustomerOrder V26

## Overview

Plugin for managing customer order flows in Cegid Retail Y2 v26. Handles e-commerce orders, delivery preparations, pickup point management, and document generation. Critical for SynagieAPI integration.

**Registration:** January 21, 2026 | **Plugin Build:** #6.96

## Key Takeaways

### Core Methods

| Method | Purpose | Status |
|--------|---------|--------|
| `CreateFrom2` | Generate delivery prep/delivery/available order from customer order | **Released** |
| `Create` | Create new customer order | Beta |
| `Update` | Modify non-e-commerce customer order header | Released |
| `Replace` | Cancel and replace non-e-commerce order or return notice | Released |
| `GetListDetail` | List orders with paging (20/page default) | Released |
| `GetDetail` | Get single order details | Released |
| `Refuse` | Refuse e-commerce order at pickup point | Released |
| `Close` | Close customer order or available order | Released |

### Important Business Rules

- **Item Identification:** Use `Lines.ItemIdentifier.Id` (GA_ARTICLE) or `Barcode` — NOT `Reference` (unreliable, deprecated)
- **Internal Reference:** Must be unique per document type + third-party
- **Idempotency:** `OperationUid` property is **mandatory** in CreateFrom2 to prevent duplicate processing
- **E-commerce flows:** Order → Delivery Preparation → Delivery → FFO (invoicing on delivery)

### Document Types
- `AvailableOrder` — Available order
- `CustomerDelivery` — Customer delivery
- `CustomerOrder` — Customer order
- `DeliveryPreparation` — Delivery preparation
- `ReturnNotice` — Return notice

### ⚠️ Critical: CreateFrom Deprecated
- `CreateFrom` method is **Obsolete** — replaced by `CreateFrom2`
- `CreateFrom` will be removed after **2/1/2028**

### Pickup Point Management
- `UpdateStatus` method for pickup parcel flows:
  - Mark as received at store (status "016")
  - Mark as delivered to customer (status "020")

### Report Generation
- `GenerateDocument` / `Poll` / `Download` — PDF generation
- `GenerateLabels` / `EndGenerateLabels` / `Download` — Label printing (supports serial numbers)

### Technical Requirements
- **.NET Framework 4.8** required on server components
- **Swagger/REST APIs** now available, grouped by plugin name

## Related Concepts
- [[y2-webservices-guide]] — General SOAP/Web Services guide
- [[synagie-api]] — Franky's SynagieAPI project
- [[y2-connectors]] — Y2 connector documentation

## Source
`documents/Y2/Common/Webservices/Follow-up Notes/Y2Plugin CustomerOrder V26`
