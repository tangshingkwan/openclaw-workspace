---
title: "Y2 Foundation Techniques & Tools V26"
type: source
source-type: document
date-added: 2026-04-20
tags: [cegid, y2, foundation, license, secure-key, installation]
summary: "Y2 license management: Secure Key/token activation, license generation, IIS server configuration."
---

# Y2 Foundation Techniques & Tools V26

## Overview

Foundation-level technical content for Y2 v26: license management, Secure Key activation, and installation prerequisites.

**Source:** Extracted 2026-02-27 | **Version:** Y2 v26

## Secure Key / License Management

### Overview

Control of Cegid Retail Y2 requires a valid license (key/token). License signs the Y2 environment declaration to Cegid.

### License Flow

1. Generate file extracted from Y2 environment
2. Send to Cegid contact
3. Receive XML token in return
4. Integrate token with environment

### Prerequisites

- One key per database AND environment
- Separate keys for multiple databases (BASE01, BASE02)
- One key per IIS server setup
- Time zone consideration — don't wait until expiry

**Important:** Changing company name requires new key generation.

### License Manager Access

- Via Internet Services Manager (IIS)
- Or: `http://XXXXX/CBR_YY.YY/License`

### Key Generation Steps

1. Connect to License page on IIS server
2. Select database
3. Click Generate to save info file
4. Send file to Cegid contact
5. Receive token — don't change filename

## See Also

- [[y2-transverse-features-v26|Transverse Features]] (Getting Started)
- [[y2-webservices-guide|Web Services Guide]]
