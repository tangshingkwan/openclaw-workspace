# Introduction to RFE

*Source: Cegid Retail Y2 RFE - Implementation Guide | Extracted: 2026-02-27*

---


# Introduction to RFE

Introduction to Retail File Exchange (RFE)

RFE is a new file exchange solution integrated to Cegid Retail Y2 based on the Microsoft Azure Blob Storage tool. This solution will gradually replace the historical CGFT component.

The present documentation, intended mainly for our clients, aims at the following:

- Describing how RFE works when integrating with Y2
- Describing the procedure for analyzing existing flows as part of a CGFT/RFE migration
- Detailing the procedure to set up flows between Y2 and RFE
- Describing best practices for exchanging files between an external system and Y2

Context

The historical CGFT solution for file exchange on Y2 SaaS environment will be gradually replaced by a new component, RFE (Retail File Exchange), based on Azure Blob Storage tool.

RFE will be connected to Y2 via the application architecture defined in the following chapters. Y2 core will allow for CGFT and RFE to co-exist. In fact the deployment of flows on RFE can be gradual and will require settings to be defined within Y2.

This new product allows for the following:

- Better processing of large-size files
- Better scalability
- Higher level of security for file exchanges via secure protocols.
- Better supervision and resilience
- A retention of files for a minimum of 7 days.

Deploying RFE in a customer environment must meet several prerequisites detailed below. These prerequisites may change depending on developments made to integration of RFE into Y2.

PLEASE NOTE !

The decommissioning of the CGFT component is scheduled for the end of 2024. Cegid Retail Y2 customers using CGFT will need to migrate to the new RFE solution.

Prerequisites

Implementing the Retail File Exchange component on a Y2 environment must meet the following requirements:

- Dedicated or Advance SaaS customer environment for all PODs.
- Minimum Cegid Retail Y2 version: v21.00.0.1444.
- Access to the RFE configuration webapp:

The Retail File Exchange component is based on the Microsoft Azure Blob Storage tool, the official documentation of which is available at the following address:

https://docs.microsoft.com/fr-fr/azure/storage/blobs/

The documentation above specifies the various prerequisites for using Azure Blob Storage client-side.

However, there are some important prerequisites for using client-side Azure Blob Storage:

- Access to objects stored in Blob Storage only via http/https protocol
- Stored blobs can only be accessed through the API REST Stockage Azure , Azure PowerShell , Azure CLI , or an Azure Storage client library (existing libraries on the following programming languages: .NET, Java, NodeJS, Python, Go, PHP, Ruby). In manual, access to Blob objects is done via Microsoft Azure Storage Explorer available for Windows, MacOS, Linux distributions. Below is the download link: https://azure.microsoft.com/fr-fr/features/storage-explorer/

Glossary

Below is a glossary of the various acronyms used in this document:

- RFE - Retail File Exchange : New file exchange solution integrated with Cegid Retail Y2 based on the Microsoft Azure Blob Storage tool.
- CGFT - Cegid File Transfer : Historical file exchange solution integrated with Cegid Retail Y2.
- Workspace : a storage area dedicated to a tenant and consisting of containers.
- Container : a sub-folder within a workspace consisting, in its own right, of 3 virtual folders (IN, OUT, ARCHIVES)

