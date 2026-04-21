---
title: "Y2 Web Services Guide"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, webservices, soap, api, php, csharp, integration]
summary: "How to consume Y2 web services: PHP and C# examples, WSDL, authentication, arrays, dates, enums."
---

# Y2 Web Services Guide

## Overview

Guide for consuming Y2 web services via SOAP API. Includes code examples in PHP and C#.

**Source:** Extracted 2026-02-27

## Supported Languages

| Language | Notes |
|----------|-------|
| PHP | Using suds library or native SOAP |
| C# | .NET with WSDL reference |

## Key Topics

### General
- WSDL Cache configuration
- Basic authentication
- Non-ASCII character handling
- Troubleshooting

### Data Types
- Arrays
- Dates
- Enums

### Common Operations
- AddNewCustomer (complex example)
- Response handling

## Code Example Structure

```php
// PHP SOAP example
$client = new SoapClient('http://y2server/Y2WS.asmx?WSDL');
$client->__setUsernameToken('user', 'pass');
$result = $client->SomeOperation($params);
```

```csharp
// C# WSDL reference example
var client = new Y2ServiceRef.Y2WS();
client.ClientCredentials.UserName.UserName = "user";
client.ClientCredentials.UserName.Password = "pass";
var result = client.SomeOperation(params);
```

## Authentication

- Basic auth via username token
- WSDL endpoint: `http://y2server/Y2WS.asmx?WSDL`

## See Also

- [[y2-connectors|Y2 Connectors Overview]]
- [[y2plugin-customerorder-v26|Customer Order Plugin]] (API integration)
