---
title: "Y2 RFE Annex Files"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, rfe, annex, sql, postman, api]
summary: "RFE annex files: Postman collection, SQL queries for CGFT data analysis, and RFE deployment scripts."
---

# Y2 RFE Annex Files

## Overview

Technical annex files for RFE implementation: Postman collections, SQL queries, and deployment scripts.

**Source:** Extracted 2026-02-27

## Included Files

### Postman Collection
- **RFE.postman_collection.json** — API collection for RFE TEST/PROD environments
  - Authentication Server (Get Token)
  - Container Management (List, Create, Delete)
  - Rights Management (Add/Delete Owner, Contributor)
  - SAS Key Management (Get SAS Token)

### SQL Analysis Queries
- **Analyse_Provenances_De_Donnees.sql** — Retrieve scheduled data provenances
- **Analyse_Exports_Libres.sql** — Extract free exports via active tasks
- **Analyse_Exports_Standards.sql** — Extract standard exports
- **Analyse_Exports_Comptables.sql** — Extract accounting exports

### Deployment Scripts
- **Maj_Provenance_Exports.sql** — RFE deployment script for Provenance/Export updates

## API Endpoints

| Environment | Swagger URL |
|-------------|-------------|
| TEST | https://rfe.cegid.cloud/t/storage/api/swagger/ui |
| PROD | https://rfe.cegid.cloud/p/storage/api/swagger/ui |

## See Also

- [[y2-rfe-implementation|RFE Implementation]]
- [[y2-rfe-operation|RFE Operation]]
