# Follow-up Notes Y2Plugin Sourcing V26

*Source: Follow-up_Notes_Y2Plugin_Sourcing_V26.pdf | Extracted: 2026-02-27*

---


## Sourcing Plugin V07


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Sourcing Plugin

2


## Preamble

This plugin is a set of web services associated with one or more versions of Cegid Retail Y2.

This document describes its scope of implementation, as well as the changes and corrections made.

Please note: All plugin methods and services can be cited in this document. Only public methods for which

the contract is published can be used by applications not designed by Cegid.

Legal notices

Permission is granted under this Agreement to download documents held by Cegid and to use the

information contained in the documents only internally, provided that: (a) the copyright notice on the

documents remains on all copies of the document; material; (b) the use of these documents for personal

and non-commercial use unless it has been clearly defined by Cegid that certain specifications may be used

for commercial purposes; (c) documents will not be copied to networked computers or published on any

type of media unless expressly authorized by Cegid; and (d) no changes are made to these documents.


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 – Sourcing Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   MANAGEMENT  ............................................................................................................................................................................ 6

GetList

6

GetDetail

7

GetListDetail

7

CreateFrom

9

Close

10

Create

10

Create2

12

CreateFrom2

13

3.   REPORT  ....................................................................................................................................................................................... 15

GenerateDocument

15

Poll

15

Download

16

4.   REPORT2  .................................................................................................................................................................................... 17

GenerateLabels

17

EndGenerateLabels

18

Download

18

5.   OTHER  .......................................................................................................................................................................................... 20

Net Framework 4.8

20


Cegid Retail Y2 – Sourcing Plugin

4


### 1.   O BJECTIVES

The  Sourcing  plugin is used to manage the flow of supplier orders. Transformation services for delivery

notices are currently available. This service will be gradually enriched.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

"Documentation" is a link that provides access to the documentation list:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties.

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

➔   Exceptions

This part provides access to exceptions, classified by type, and according to the plugin.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Sourcing Plugin

5

➔   Installation

This page allows you to download Web Services installation and consumption documentation.


## Y2 versions

This plugin is compatible with the following version of Cegid Retail Y2:

➔   Version 26

Note:

The # sign at the beginning of the plugin build number corresponds to the major version of Cegid Retail

Y2.


Cegid Retail Y2 – Sourcing Plugin

6


### 2.   M ANAGEMENT


## GetList


### ➔   Objectives

This service returns the list of supplier delivery notices that meet the contract criteria:

➔   List of stores in which to search delivery notices in compliance with the user restrictions specified

in the contract.

➔   Document dates period.

The "Paging" property provides protection against timeouts due to a significant number of documents. We

recommend that it be used with a setting of a few hundred lines, supplemented by tests for dimensioning

this value according to the communication line.

Please note: the speed of data loading varies according to the device and its location.

The Web Service caller should check that not all information is returned in the first page. It can then call the

next page, until all headers are recovered.

The ExtractByOldest property decides on the order for document recovery:

➔   False: default value, recovering the documents starting with the most recent.

➔   True: recovery of documents starting with the oldest.


### ➔   Improvements

Optimizing the search for delivery notices.

The remaining quantities to deliver for customer orders and reservation requests are no longer calculated

systematically, but only if the Y2 company setting "Calculation of customer expectations in GETs of

transfer/delivery notices" in the "Commercial Management/Web Services" tab is checked.

Added user fields in GetList operation.

Using the UserRestrictions service of the Identity plugin to control the provided stores.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/2/2022

A2320

107261

#4.68

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/10/2022

A2299

108471

#4.97

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

3/22/2023

698738

161149

#5.36


Cegid Retail Y2 – Sourcing Plugin

7


## GetDetail


### ➔   Objectives

The GetDetail service sends the lines of a document, the identifier of which is specified in the contract.

Please note: Managing an item with a serial number requires a unit quantity for the line.


### ➔   Improvements

Added new properties, external reference, catalog reference, package reference and complementary

description at line level to the reply.

Optimizing the search for delivery notices.

The remaining quantities to deliver for customer orders and reservation requests are no longer calculated

systematically, but only if the Y2 company setting "Calculation of customer expectations in GETs of

transfer/delivery notices" in the "Commercial Management/Web Services" tab is checked.

Correction in viewing a supplier return including a serial number.

The XML flow returned by the GetDetail method was incomplete when the line in the supplier return

contained a serial number.


## GetListDetail


### ➔   Objectives

This service returns the list of supplier delivery notices that meet the contract criteria, with details by line,

as with the GetList and GetDetail services.

This service should only be used if a limited number of documents are returned, with few lines.

If there are documents with more than a few dozen lines, this service should not be used, GetList and

GetDetail being preferred.


### ➔   Improvements

Added new properties, external reference, catalog reference, package reference and complementary

description at line level to the reply.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/1/2022

A2302

107087

#4.60

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/2/2022

A2320

107261

#4.68

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PLA

10/2/2024

1606270

305599

#5.227


Cegid Retail Y2 – Sourcing Plugin

8

Optimizing the search for delivery notices.

The remaining quantities to deliver for customer orders and reservation requests are no longer calculated

systematically, but only if the Y2 company setting "Calculation of customer expectations in GETs of

transfer/delivery notices" in the "Commercial Management/Web Services" tab is checked.

Added user fields in GetListDetail operation.

Added the internal reference, external reference, and the follow-up reference to the request.

Using the UserRestrictions service of the Identity plugin to control the provided stores.

The StoreIds property is made optional.

The method now returns supplier return lines with negative quantities.

The GetListDetail operation of the SourcingManagement WS now returns the positive RemainingQuantity

field in the line section.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

FDE

2/7/2025

16897873

INC0209865

354710

#6.51

The GetListDetail operation of the SourcingManagement WS now returns the TotalQuantity field without

being multiplied by the number of serial numbers in the line.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/1/2022

A2302

107087

#4.60

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/2/2022

A2320

107261

#4.68

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/10/2022

A2299

108471

#4.97

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

3/17/2023

A2424

160436

#5.23

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

3/22/2023

698738

161149

#5.36

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

6/21/2023

A2455

175501

#5.81

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

9/18/2023

1205917

189554

#5.116


Cegid Retail Y2 – Sourcing Plugin

9

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

FDE

2/10/2025

1704359

INC0210668

355867

#6.55


## CreateFrom


### ➔   Objectives

The objective of this service is to be able to validate a delivery notice to convert it into a supplier receipt

and feed into the store's inventory.

Please note: Delivery notices awaiting approval are not returned.

Scope

The generation of delivery notices as delivery slips addresses the following functions:

•

Overall generation of a document without passing lines in the contract.

•

Line-by-line generation to take account of any remaining information in the document, according

to its options

•

Possibility to close the delivery notice according to the RemainderManagement property

•

Management of lines in quantity, with no concept of valuation, with recovery of the original

document valuation and calculation of the document pro-rata to the quantities prepared/delivered.

•

Integration of a warehouse in the header (for all lines) or a line-specific warehouse according to the

generation type.

•

Recognition of the converted document by its Y2 number.

•

Integration of serial numbers with a mandatory unit quantity and the DisableMergeLines property

set to True.

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

Good practice is to specify the OperationUid property in the contract, allowing Cegid Retail Y2 to record

this information, in order not to repeat the processing. This number should therefore be unique.

Example:

•

Software calls the CreateFrom service to generate a document in Cegid Retail Y2.

•

Y2 performs the processing but cannot communicate this information with the caller, who makes

a fresh attempt:

o

If the OperationUid property is transmitted, Y2 knows that the processing was successful

and informs the caller.

o

With no OperationUid property specified, Y2 attempts to repeat the same processing,

risking the creation of a new document.

We undertake to provide this information; it will soon become mandatory.

Recognition of the item

This service allows the item on each line to be found in two ways:

•

Lines.ItemIdentifier.Reference: This property should not be used; it is not reliable.


Cegid Retail Y2 – Sourcing Plugin

10

In the case of a reference with the same level of priority for several items, nothing can predict

which item will be used.

This property will soon be rendered obsolete.

•

Lines.ItemIdentifier.Id: This property identifies an item in a unique way in Cegid Retail Y2 and should

be used.


### ➔   Improvements

Added user fields in CreateFrom operation.

Added properties FollowUpReference and ExternalReference at header level and ExternalReference,

CatalogReference, AdditionalDescription, and PackageReference at line level.

The method is now set to the Released status.

Method replaced by CreateFrom2. It has the status Obsolete and will be removed from versions

generated after 2/1/2028


## Close


### ➔   Objectives

The objective of this service is to close a delivery notice.

Please note: Please note delivery notices awaiting approval cannot be closed.


### ➔   Improvements


## Create


### ➔   Objectives

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

2/24/2022

A2299

106233

#4.31

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

3/9/2022

A2302

108073

#4.91

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

15157

#4.217


Cegid Retail Y2 – Sourcing Plugin

11

The objective of this service is to be able to create a supplier return.

Scope

Please note: You must take into account the option in the company setting which allows you to specify that

the items are provided by single supplier.  If you manage single supplier items, you must check that the

items in the lines are associated with the supplier in the return header.

The supplier return is systematically revalued (same operation as in the import with the $$_RECALCULPIECE

variable.)

At least one quantity must be returned in the document.

If the delivery date is not filled in, the document date is copied to this date.

The effective date of the document is updated by the import according to the date of the document.

Management of sales representatives/salespeople:

•

If there is a representative at line level, he/her will be recovered in the line.

•

If there is a representative in the header, but not at line level, the header representative will be

recovered in the line.

•

If there is a representative in the line, but not in in the header, the representative of the first line

will be recovered in the header.

Management of movement reasons:

•

The reason provided in the header of the contract is applied by default to all document

•

If the document supports movement reasons, an exception is raised if:

o

The reason is not provided in in the contract header.

o

The reason provided in the header does not exist in Y2

o

The scope of the reason does not match the type of the processed document

•

If the document type does not support movement reasons, an exception is raised if a reason is

provided in the contract header.

If there is line with a serial number:

•

The quantity of the line must be 1

•

The DisableMergeLines property must be set to True.

•

The document type must accept serial numbers (and management exceptions to the

store/warehouse)

External reference:

•

If the reference is provided in the contract header, it will be recovered in the document header, but

it will not be applied to the document lines.

•

If the external reference is provided at line level, it will be recovered in the document lines.

Valuation:

•

The document will be systematically revalued (set $$_RECALCULPIECE = 'X')

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

It is necessary to specify the OperationUid property in the contract, allowing Cegid Retail Y2 to record this

information, in order not to repeat the processing. This number should therefore be unique.

Example:


Cegid Retail Y2 – Sourcing Plugin

12

•

Software calls the Create service to generate a document in Cegid Retail Y2.

•

Y2 performs the processing but cannot communicate this information with the caller, who makes

a fresh attempt:

o

If the OperationUid property is transmitted, Y2 knows that processing was successful and

informs the caller.


### ➔   Improvements

Added user fields in Create operation.

Added properties CatalogReference, AdditionalDescription, and PackageReference at line level.

The method is now set to the Obsolete status.

Method replaced by Create2. It has the status Obsolete and will be removed from versions generated

after 2/1/2028.

The minimum value of the quantity provided to the method is 0.0001.


## Create2


### ➔   Objectives

This operation corresponds to version 2 of the Create operation. It allows you to create a supplier return

with the same scope. The difference occurs at item level. Indeed, there is an ItemId field in the Create

operation. In Create2, we now use an ItemIdentifier section which contains the Id/Barcode combination to

identify the item either from its identifier, or its barcode.


### ➔   Improvements

New operation

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

2/24/2022

A2299

106233

#4.31

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

3/9/2022

A2302

108073

#4.91

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

15157

#4.217

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

8/3/2023

1210660

182906

#5.99


Cegid Retail Y2 – Sourcing Plugin

13

Added properties CatalogReference, AdditionalDescription, and PackageReference at line level.

The minimum value of the quantity provided to the method is 0.0001.

A new "Comment" property is added to headers and lines, allowing the comment entered on the mobile

device to be integrated.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

9/5/2025

1947111

415969

416650

#6.616


## CreateFrom2


### ➔   Objectives

This operation corresponds to version 2 of the CreateFrom2 operation with the same scope . The difference

occurs at item level. Indeed, in the CreateFrom operation, there is an ItemIdentifier field with the

Id/Reference combination. In CreateFrom2, the ItemIdentifier section but with the Id/Barcode combination

to identify the item indifferently from its identifier or its barcode. You can also validate a purchase order (in

addition to the delivery notice) to transform it into a supplier receipt and supply the store's stock.


### ➔   Improvements

Addition of the CreateFrom2 operation.

A new "Comment" property is added to headers and lines, allowing the comment entered on the mobile

device to be integrated.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

9/5/2025

1947111

415969

#6.616

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

3/3/2022

A2311

106233

#4.31

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

RLO

3/9/2022

A2302

108073

#4.91

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

8/1/2023

1210660

182384

#5.95

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

6/2/2022

A2301

PR    119567

#4.98


Cegid Retail Y2 – Sourcing Plugin

14

RLO

416650


Cegid Retail Y2 – Sourcing Plugin

15


### 3.   R EPORT

This service manages transmission of the PDF of a supplier receipt, once delivery notice been validated, with

the following steps:

➔   Cegid Retail Y2 server request to generate the PDF document on the server, by using the printing

templates configured in the Back Office.

➔   Loading of the PDF to the service caller as soon as available on server.

➔   Sending the PDF to the service caller, for printing managed by this caller.

Please note: this service does not allow the document to be marked as printed (GP_EDITEE field not

updated). The change in value of this field is reserved for interactive publishing, which links the creation of

the PDF to its printing.


## GenerateDocument


### ➔   Objectives

This method prompts the print server to stack the printing request of a document, using its unique identifier

in Cegid Retail Y2.

The report is printed by default in the “software language” as defined in the cultural profile of the user using

this service for the following elements:

➔   The mask: Titles and descriptions of the report template

➔   The format of numbers and dates

➔   The data transmitted: item descriptions, markdown reason, etc.

The  LanguageId  property allows you to edit the report mask and the format of numbers and dates

according to this new language.

The  CultureId  property allows you to force the formatting of data numbers and dates:

➔   If the  LanguageId  property is missing.

➔   If the  LanguageId  property is identical to the "software language" in the user’s cultural profile.

The data remains in the user's language.

Only the native Cegid report generator is used to generate the PDF.


### ➔   Improvements


## Poll


### ➔   Objectives

At the end of the PDF generation call, the Poll method is called to find out its availability.

In interactive mode, we advise to make a first call after 5 seconds, then every 2 seconds without time limit,

leaving the user the possibility to interrupt the wait.

In batch mode, a call every 5 seconds is recommended, with a maximum of 10 calls.


Cegid Retail Y2 – Sourcing Plugin

16


### ➔   Improvements


## Download


### ➔   Objectives

When the Poll returns positively, the Download method is used to download the PDF and print on a printer,

store it or send it by e-mail.


### ➔   Improvements


Cegid Retail Y2 – Sourcing Plugin

17


### 4.   R EPORT 2

The Report2 service allows the management of reports related to sourcing documents.

The following steps are to be respected:

➔   Cegid Retail Y2 server request to generate the PDF of the document on the server, by using the

printing templates configured in the Back Office.

➔   Upload the PDF to the service caller as soon as it is available on server.

➔   Send the PDF to the service caller, for printing managed by this caller.


## GenerateLabels


### ➔   Objectives

This method is used to initiate a request to generate the PDF file for labels of a sourcing document in  Cegid

Retail Y2.

The document types processed are :

-

Supplier receipts

-

Supplier returns

The following business rules are applied:

•

A document identifier must be filled in and exist

•

If the reprint request is requested and the reprint reason is entered, it must exist

•

The reason for reprint must only be entered when reprinting.

•

The printing template, language, and the store must exist.

In reply, the information indicates the progress of the PDF generation request.

•

The JobId is returned only if the generation could not be finalized within the requested

time (WaitTimeout in request). This JobId is used to call the EndGenerateLabels method, which

indicates the status of the generation.

•

The Report section is populated only if the PDF generation was successful. The identifier of

the generated file allows you to download it via the Download method

•

The EventLog section is populated if the event log is updated, i.e. if a reprint is made.


### ➔   Improvements

The method is now set to status Beta

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

12/24/2024

A2497

PR 335383

# 6.24


Cegid Retail Y2 – Sourcing Plugin

18

The price list type and pricing system used for label printing are no longer those of the document, but are

now searched for at store level, in order to be able to print labels with their final consumer price inclusive

of tax from a purchase document invoiced exclusive of tax.


## EndGenerateLabels


### ➔   Objectives

This method allows you to check the progress of a label printing request in  Cegid Retail Y2.

The following business rules are applied:

•

The process ID must exist

If the EventLog section is populated, the event log identifier will update it to indicate that printing is

complete if it is.

In response, the Report section is populated only if the PDF was successfully generated. The identifier of

the generated file allows you to download it via the Download method.


### ➔   Improvements

The method is now set to status Beta


## Download


### ➔   Objectives

This method downloads the PDF file that was generated by one of the Generate methods below.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

353155

# 6.50

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/5/2025

1726793

366581

#.6.64

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

12/24/2024

A2497

PR 336877

# 6.32

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

353155

# 6.32


Cegid Retail Y2 – Sourcing Plugin

19

The following business rules are applied:

•

The identifier of the file to be downloaded must exist.

In response, a link will allow you to download the PDF document to your computer.


### ➔   Improvements

The method is now set to status Beta

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

12/24/2024

A2497

PR 336877

# 6.32

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

353155

# 6.32


Cegid Retail Y2 – Sourcing Plugin

20


### 5.   O THER


## Net Framework 4.8

Following Microsoft‘s announcement about the “end of support for .NET Framework 4.5.2, 4.6 and 4.6.1 as

soon as April 26, 2022" the plugin now requires the installation of the .Net Framework 4.8 (runtime) on

server components.


## Swagger

Rest/Restful APIs grouped by plugin, with the option of selecting them by plugin name.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

ADU

1/16/2025

1543349

344817

#6.43


