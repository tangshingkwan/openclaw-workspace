---
title: "Consuming Y2 Web Services"
type: source
source-type: document
source-url: 
date-added: 2026-04-15
tags: [cegid, y2, webservices, soap, api, integration]
summary: "Official Cegid guide for consuming Y2 retail web services via SOAP. Covers authentication (Basic, NTLM, Cookie), WSDL configuration, and code samples in PHP, C#, Python, Ruby, Java, and JavaScript."
---

# Consuming Y2 Web Services

## Overview

Official Cegid documentation (extracted from PDF, dated 2026-02-27) providing illustrative examples of how to consume Y2 Web Services via SOAP. Target version: Cegid Retail Y2 Version 26.

## Key Takeaways

### Authentication Methods
- **Basic Auth (CBR)** — Username/password sent in SOAP header
- **NTLM Auth** — Supported but deprecated
- **Cookie-based Auth** — Optimizes WS/HTTP flow by caching auth cookie

### Core Concepts
- `DatabaseId` = FolderId of the database to target
- `RetailContext` object required for all requests
- WSDL cache should be **enabled in production** (`soap.wsdl_cache_enabled=1`)
- All requests use SOAP over HTTP/HTTPS

### Supported Languages
1. **PHP** (>= 5.6.25) — SoapClient class
2. **C#** — Visual Studio Service Reference + WCF
3. **Python 2.7** — suds library
4. **Ruby** — savon gem
5. **Java** — Eclipse + Apache Axis2
6. **JavaScript** — Browser-based (custom soapclient.js)

### Common Data Types
- **Arrays** — Create cell objects, then aggregate into array
- **Dates** — ISO 8601 format (`YYYY-MM-DDTHH:MM:SS`)
- **Enum** — Use constant string values directly (no enum type in PHP/Python/Ruby)
- **Non-ASCII** — UTF-8 encoding required for all languages

### Troubleshooting
- Enable trace logging to capture XML request/response
- PHP: Use `soapDebug.php` to log SOAP traffic
- C#: Use `System.ServiceModel.MessageLogging` in app.config
- Python: Use `logging.getLogger('suds.client')`
- JavaScript: Browser console + Fiddler

## Related Concepts
- [[y2-connectors]] — Y2 connector documentation (Adyen, Avalara, Vertex)
- [[synagie-api]] — Franky's SynagieAPI interface project

## Source
`documents/Y2/Common/Webservices/Consuming Y2 Web Services/`
