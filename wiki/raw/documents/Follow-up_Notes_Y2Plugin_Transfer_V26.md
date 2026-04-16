# Follow-up Notes Y2Plugin Transfer V26

*Source: Follow-up_Notes_Y2Plugin_Transfer_V26.pdf | Extracted: 2026-02-27*

---


## Transfer Plugin V07


## Cegid Retail Y2 –  Version  26


## Follow-up Notes


## Make more


## possible

Registration date: January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Transfer Plugin

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


Cegid Retail Y2 – Transfer Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   ITEMSDELIVERYMANAGEMENT  ....................................................................................................................................... 6

Create

6

CreateFrom

7

CreateFromDocuments

9

GetDetail

9

GetList

10

GetListDetail

11

Refuse

12

3.   ITEMSRECEPTIONMANAGEMENT  ................................................................................................................................ 14

Close

14

Create

14

CreateFrom

16

GetDetail

17

GetList

18

GetListDetail

19

4.   REPORT2  .................................................................................................................................................................................... 22

GenerateLabels

22

EndGenerateLabels

23

Download

23

5.   TRANSFERREPORT  .............................................................................................................................................................. 25

GenerateDocument

25

Poll

26

Download

26

6.   OTHER  .......................................................................................................................................................................................... 27

Net Framework 4.8

27


Cegid Retail Y2 – Transfer Plugin

4


### 1.   O BJECTIVES

The  Transfer  plugin is used to manage the flow of goods transfers between the brand's various warehouses.

Several services are currently available:

➔   Issue of a transfer to another warehouse

➔   Issue of a transfer by validation of a transfer request from another warehouse.

➔   Receipt of a transfer by validating a transfer notice from another warehouse

Ce plugin will be enriched gradually.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

"Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Transfer Plugin

5

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

➔   Exceptions

This part provides access to exceptions, classified by type, and according to the plugin.

➔   Installation

This page allows you to download Web Services installation and consumption documentation.


## Y2 versions

This plugin is compatible with the following version of Cegid Retail Y2:

➔   Version 26

Note:

The # sign at the beginning of the plugin build number corresponds to the major version of Cegid Retail

Y2.


Cegid Retail Y2 – Transfer Plugin

6


### 2.   I TEMS D ELIVERY M ANAGEMENT


## Create


### ➔   Objectives

This service allows you to create a transfer issued from a store and a store warehouse.

Note: in the case of a folder not managing warehouses (single warehouse), the store code (StoreId) should

be copied into the warehouse code (WarehouseId).

Depending on the settings used in Cegid Retail Y2, the creation of a transfer generates:

➔   A transfer notice, allowing the stock to be placed in a "Transit" status

➔   A received transfer, which directly feeds the stock.

Scope

The creation of a transfer addresses the following functions:

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

Y2 performs the processing but cannot communicate this information to the caller making a fresh

attempt:

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

In the case of a reference with the same level of priority for several items, nothing can predict which

item will be used.

This property will soon be rendered obsolete.

•

Lines.ItemIdentifier.Id: This property identifies an item in a unique way in Cegid Retail Y2 and should

be used.


### ➔   Improvements


Cegid Retail Y2 – Transfer Plugin

7

Added properties ExternalReference, CatalogReference, AdditionalDescription, and PackageReference at

line level.

Revised the principle of the automatic assignment of the internal reference for non-e-commerce documents

relating to an e-commerce store in order to avoid the error "DOC00002 - the internal reference of the

document is not specified”. This fix requires installing a Core Y2 release later than 5/9/2022.

Added the CustomerIdentifier section, in order to force the creation customer of the document to be

created.

The minimum value of the quantity provided to the method is 0.0001.

Increased the size of the TransactionBumber property from 35 to 70 characters.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

1/19/2026

1967994

447180

#6.56


## CreateFrom


### ➔   Objectives

The objective of this service is to be able to validate a transfer request, in the case of e-commerce orders,

or transfer requests entered directly at checkout. A sent transfer is then created.

Please note: Transfer requests awaiting approval are not returned.

Scope

The generation of transfer requests into sent transfers meets the following functional criteria:

•

Overall generation of a document without passing lines in the contract.

•

Line-by-line generation to take account of any remaining information in the document, according

to its options.

•

Possibility to close the transfer request according to the RemainderManagement property.

•

Management of lines in quantity, with no concept of valuation, with recovery of the original

document valuation and calculation of the document pro-rata to the quantities prepared/delivered.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

RLO

3/9/2022

A2302

PR 108085

#4.79

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

HDA

5/9/2022

751474

SVN 159518

NC

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

LDE

9/2/2022

A2386

PR 129770

#4.187

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

#5.110


Cegid Retail Y2 – Transfer Plugin

8

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

Y2 performs the processing but cannot communicate this information to the caller making a fresh

attempt:

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

In the case of a reference with the same level of priority for several items, nothing can predict which

item will be used.

This property will soon be rendered obsolete.

•

Lines.ItemIdentifier.Id: This property identifies an item in a unique way in Cegid Retail Y2 and should

be used.


### ➔   Improvements

Added properties ExternalReference, CatalogReference, AdditionalDescription, and PackageReference at

line level.

Revised the principle of the automatic assignment of the internal reference for non-e-commerce documents

relating to an e-commerce store in order to avoid the error "DOC00002 - the internal reference of the

document is not specified”. This fix requires installing a Core Y2 release later than 5/9/2022.

Increased the size of the TransactionBumber property from 35 to 70 characters.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

1/19/2026

1967994

447180

#6.56

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

RLO

3/9/2022

A2302

PR 108085

#4.79

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

HDA

5/9/2022

751474

SVN 159518

NC


Cegid Retail Y2 – Transfer Plugin

9


## CreateFromDocuments


### ➔   Objectives

The objective of this method is to be able to validate a list of transfer requests, in the case of e-commerce

orders, or transfer requests entered directly at checkout. A sent transfer is then created.

Management rules

•

The sender warehouse of the header is retrieved from the first line of the sent document.

•

The sender store of all transfer requests must be unique.

•

The recipient store of all transfer requests must be unique.

•

The recipient warehouse of all transfer request headers must be unique.

•

The third-party of all transfer requests must be unique.

•

The origin of all transfer request must be unique.

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

It is necessary to specify the OperationUid property in the contract, allowing Cegid Retail Y2 to record this

information, in order not to repeat the processing. This number should therefore be unique.


### ➔   Improvements

Added properties ExternalReference, CatalogReference, AdditionalDescription, and PackageReference at

line level.


## GetDetail


### ➔   Objectives

The GetList service returns a list of transfer requests; the GetDetail service allows you to load the lines of a

document, the identifier of which is specified in the contract.

Please note:

•

Managing an item with a serial number requires a unit quantity for the line.

•

Using this method is not authorized for documents awaiting approval.


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

RLO

3/9/2022

A2302

PR 108085

#4.79

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/3/2022

A2302

PR 107333

#4.64


Cegid Retail Y2 – Transfer Plugin

10

Optimizing the search for transfer requests.

The remaining quantities to deliver for customer orders and transfer requests are no longer calculated for

transfer requests.


## GetList


### ➔   Objectives

This service returns the list of transfer requests that meet the contract criteria:

➔   Recipient store for the transfer request, in compliance with the restrictions of the user specified in

the contract.

➔   Document creation period.

Please note: Transfer requests awaiting approval are not returned.

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

Optimizing the search for transfer requests.

The remaining quantities to deliver for customer orders  and transfer requests are no longer calculated for

transfer requests.

Reading user fields in the transfer document.

Fixed an exception “ 500 internal server error ” occurring when viewing a transfer containing some populated user

fields.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/10/2022

A2320

108597

#4.82

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/10/2022

A2320

108597

#4.82


Cegid Retail Y2 – Transfer Plugin

11

Added the CustomerIdentifier section, in order to get in the reply the customer of each document (internal

identifier and external reference.)

Using the UserRestrictions service of the Identity plugin to control the provided stores.

Fixed the conversion error from a local DocumentType to a Common DocumentType.


## GetListDetail


### ➔   Objectives

This service returns the list of transfer requests that meet the contract criteria, with details by line, as with

the GetList and GetDetail services.

This service should only be used if a limited number of documents are returned, with few lines.

If there are documents with more than a few dozen lines, this service should not be used, GetList and

GetDetail being preferred.

Please note: Transfer requests awaiting approval are not returned.


### ➔   Improvements

Added new properties, external reference, catalog reference, package reference and complementary

description at line level to the reply.

Optimizing the search for transfer requests.

The remaining quantities to deliver for customer orders and transfer requests are no longer calculated for

transfer requests.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PLA

6/17/2022

820775

121148

#4.136

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

LDE

9/2/2022

A2386

PR 129770

#4.187

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

161295

#5.32

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

9/5/2023

846036

187137

#5.118

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/3/2022

A2302

PR 107333

#4.64


Cegid Retail Y2 – Transfer Plugin

12

Reading user fields in the transfer document.

Fixed an exception “ 500 internal server error ” occurring when viewing a transfer containing some populated user

fields.

Added the CustomerIdentifier section, in order to get in the reply the customer of each document (internal

identifier and external reference.)

Added the internal reference, external reference, and the follow-up reference to the request.

Using the UserRestrictions service of the Identity plugin to control the provided stores.

The StoreIds property is made optional.

Fixed the conversion error from a local DocumentType to a Common DocumentType.


## Refuse


### ➔   Objectives

The objective of this service is to refuse a transfer request, by closing it.

Please note:

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/10/2022

A2320

108597

#4.82

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PLA

6/17/2022

820775

121148

#4.136

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

LDE

9/2/2022

A2386

PR 129770

#4.187

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

160477

#5.21

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

161295

#5.32

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

175500

#5.88

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

9/5/2023

846036

187137

#5.118


Cegid Retail Y2 – Transfer Plugin

13

•

Only transfer requests visible to the user may be refused.

•

Transfer requests awaiting approval cannot be closed.


### ➔   Improvements


Cegid Retail Y2 – Transfer Plugin

14


### 3.   I TEMS R ECEPTION M ANAGEMENT


## Close


### ➔   Objectives

The objective of this service is to close a transfer notice.

Please note: Transfer notices awaiting approval cannot be closed.


### ➔   Improvements


## Create


### ➔   Objectives

This service is used to create a transfer request.

Scope

The creation of a transfer request meets the following functional criteria:

•

Integration of serial numbers with a mandatory unit quantity and the DisableMergeLines property

set to True.

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

The OperationUid property is mandatory, allowing Cegid Retail Y2 to record this information, so as not to

repeat the processing. This number should therefore be unique.

Example:

•

Software calls Create service to generate a document in Cegid Retail Y2.

•

Y2 performs the processing but cannot communicate this information to the caller making a fresh

attempt. With the OperationUid property, Y2 knows that the processing was successful, and informs

the caller.

Recognition of the item

This service allows the item on each line to be found in two ways:

•

Lines.ItemIdentifier.Id: This property identifies an item in a unique way in Cegid Retail Y2.

•

Lines.ItemIdentifier.Barcode: Barcode

When both properties are specified, a consistency check is performed: if the barcode does not match the

item found, an exception is returned.

Document valuation

Either the document is not valued, or it is fully valued.

-

Valuation: The CurrencyId and TaxIncluded properties of the Header section, as well as the

UnitPriceBase property of each item line must be specified.

-

No valuation: None of the above properties must be specified.


Cegid Retail Y2 – Transfer Plugin

15


### ➔   Improvements

Added properties ExternalReference, CatalogReference, AdditionalDescription, and PackageReference at

line level.

Revised the principle of the automatic assignment of the internal reference for non-e-commerce documents

relating to an e-commerce store in order to avoid the error "DOC00002 - the internal reference of the

document is not specified”. This fix requires installing a Core Y2 release later than 5/9/2022.

Added the CustomerIdentifier section, in order to force the creation customer of the document to be

created.

The out-of-stock control is now in place when creating a sent transfer (TEM) (via the  Create  method of the

TransferItemsDeliveryManagementService  Web Service: In case of a shortage, an exception is raised

preventing the creation of the TEM.

The minimum value of the quantity provided to the method is 0.0001.

Increased the size of the TransactionBumber property from 35 to 70 characters.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

1/19/2026

1967994

447180

#6.56

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

3/4/2022

A2303

PR 107424

#4.70

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

RLO

3/9/2022

A2302

PR 108085

#4.79

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

HDA

5/9/2022

751474

SVN 159518

NC

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

LDE

9/2/2022

A2386

PR 129770

#4.187

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

PLA

1/13/2023

1081885

SVN 164986

NC

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

#5.110


Cegid Retail Y2 – Transfer Plugin

16


## CreateFrom


### ➔   Objectives

The objective of this service is to be able to validate a transfer notice to convert it into a Received transfer

and feed the store's inventory.

Please note: Transfer notices awaiting approval are not returned.

Scope

The generation of transfer notices ins Received transfer meets the following functional criteria:

•

Overall generation of a document without passing lines in the contract.

•

Line-by-line generation to take account of any remaining information in the document, according

to its options.

•

Possibility to close the transfer notice according to the RemainderManagement property.

•

Management of lines in quantity, with no concept of valuation, with recovery of the original

document

valuation,

and

calculation

of

the

document

pro-rata

to

the

quantities

prepared/delivered.

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

Y2 performs the processing but cannot communicate this information to the caller making a fresh

attempt:

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

In the case of a reference with the same level of priority for several items, nothing can predict which

item will be used.

This property will soon be rendered obsolete.

•

Lines.ItemIdentifier.Id: This property identifies an item in a unique way in Cegid Retail Y2 and should

be used.


Cegid Retail Y2 – Transfer Plugin

17


### ➔   Improvements

Added properties ExternalReference, CatalogReference, AdditionalDescription, and PackageReference at

line level.

For the folders that do not manage remainders on transfer notices, the idempotency table GUIDDOCUMENT

was not correctly populated during the creation of the received transfer; a malfunction that could be the

cause of errors of type "CBR00074 -This document is already closed" when calling this method. This fix

requires installing a Core Y2 release later than 4/28/2022.

Revised the principle of the automatic assignment of the internal reference for non-e-commerce documents

relating to an e-commerce store in order to avoid the error "DOC00002 - the internal reference of the

document is not specified”. This fix requires installing a Core Y2 release later than 5/9/2022.

The out-of-stock control is in place when creating a sent transfer (TEM) from a transfer request DTR (via the

CreateFrom  method of the  TransferItemsDeliveryManagementService  Web Service: In case of a shortage, an

exception is raised preventing the creation of the TEM.

Increased the size of the TransactionBumber property from 35 to 70 characters.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PCH

1/19/2026

1967994

447180

#6:56 AM


## GetDetail


### ➔   Objectives

The GetDetail service sends the lines of a document, the identifier of which is specified in the contract.

Please note: Managing an item with a serial number requires a unit quantity for the line.


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

RLO

3/9/2022

A2302

PR 108085

#4.79

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

4/27/2022

785919

All

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

HDA

5/9/2022

751474

SVN 159518

NC

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

PLA

1/13/2023

1081885

SVN 164986

NC


Cegid Retail Y2 – Transfer Plugin

18

Added the capability to query transfer requests.

Optimizing the search for transfer notices.

The remaining quantities to deliver for customer orders and reservation requests are no longer calculated

systematically, but only if the Y2 company setting "Calculation of customer expectations in GETs of

transfer/delivery notices" in the "Commercial Management/Web Services" tab is checked.


## GetList


### ➔   Objectives

This service returns the list of transfer notices or transfer requests, or received transfers that meet the

contract criteria:

➔   List of stores in which to search documents in compliance with the user restrictions specified in the

contract.

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

Added the capability to query transfer requests.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/3/2022

A2302

PR 107333

#4.64

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

3/4/2022

A2303

PR 107424

#4.70

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/10/2022

A2320

108597

#4.82


Cegid Retail Y2 – Transfer Plugin

19

Optimizing the search for transfer notices.

The remaining quantities to deliver for customer orders and reservation requests are no longer calculated

systematically, but only if the Y2 company setting "Calculation of customer expectations in GETs of

transfer/delivery notices" in the "Commercial Management/Web Services" tab is checked.

Reading user fields in the transfer document.

Fixed an exception “ 500 internal server error ” occurring when viewing a transfer containing some populated user

fields.

Added the CustomerIdentifier section, in order to get in the reply the customer of each document (internal

identifier and external reference.)

Using the UserRestrictions service of the Identity plugin to control the provided stores.

Fixed the conversion error from a local DocumentType to a Common DocumentType.


## GetListDetail


### ➔   Objectives

This service returns the list of transfer requests, transfer notices, or received transfers that meet the contract

criteria, with details by line, as with the GetList and GetDetail services.

This service should only be used if a limited number of documents are returned, with few lines.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

3/4/2022

A2303

PR 107424

#4.70

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/10/2022

A2320

108597

#4.82

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PLA

6/17/2022

820775

121148

#4.136

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

LDE

9/2/2022

A2386

PR 129770

#4.187

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

161295

#5.32

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

9/5/2023

846036

187137

#5.118


Cegid Retail Y2 – Transfer Plugin

20

If there are documents with more than a few dozen lines, this service should not be used, GetList and

GetDetail being preferred.


### ➔   Improvements

Added new properties, external reference, catalog reference, package reference and complementary

description at line level to the reply.

Added the capability to query transfer requests.

Optimizing the search for transfer notices.

The remaining quantities to deliver for customer orders and reservation requests are no longer calculated

systematically, but only if the Y2 company setting "Calculation of customer expectations in GETs of

transfer/delivery notices" in the "Commercial Management/Web Services" tab is checked.

Reading user fields in the transfer document.

Fixed an exception “ 500 internal server error ” occurring when viewing a transfer containing some populated user

fields.

Added the CustomerIdentifier section, in order to get in the reply the customer of each document (internal

identifier and external reference.)

Using the UserRestrictions service of the Identity plugin to control the provided stores.

The RecipientStoreIds property is made optional.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

JMO

3/3/2022

A2302

PR 107333

#4.64

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

3/4/2022

A2303

PR 107424

#4.70

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

HDA

3/10/2022

A2320

108597

#4.82

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

PLA

6/17/2022

820775

121148

#4.136

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build

no.

Quality Ctrl

LDE

9/2/2022

A2386

PR 129770

#4.187

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

161295

#5.32

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

175500

#5.88


Cegid Retail Y2 – Transfer Plugin

21

Fixed the conversion error from a local DocumentType to a Common DocumentType.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

EPL

9/5/2023

846036

187137

#5.118


Cegid Retail Y2 – Transfer Plugin

22


### 4.   R EPORT 2

The Report2 service allows the management of reports related to transfers.

The following steps are to be respected:

➔   Request the Cegid Retail Y2 server to generate the PDF on the server, by using the printing

templates configured in the Back Office.

➔   Upload the PDF to the service caller as soon as it is available on server.

➔   Send the PDF to the service caller, for printing managed by this caller.


## GenerateLabels


### ➔   Objectives

This method is used to initiate a request to generate the PDF file for labels of a transfer in  Cegid Retail Y2.

The proceeded document types are:

-

Transfer requests

-

Sent transfers

-

Received transfers

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

The EventLog section is populated if the event log is updated, i.e., if a reprint is made.


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

ADU

12/23/2024

A2497

PR 335942

# 6.13


Cegid Retail Y2 – Transfer Plugin

23

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

353166

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

3/7/2025

1726793

367497

# 6.37

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

ADU

12/23/2024

A2497

PR 336867

# 6.15

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

353166

# 6.50


Cegid Retail Y2 – Transfer Plugin

24

This method downloads the PDF file that was generated by one of the Generate methods below.

The following business rules are applied:

•

The identifier of the file to be downloaded must exist.

In response, a link will allow you to download the PDF document to your computer.


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

ADU

12/23/2024

A2497

PR 336867

# 6.15

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

353166

# 6.29


Cegid Retail Y2 – Transfer Plugin

25


### 5.   T RANSFER R EPORT

This service manages the PDF transmission of a sent transfer or a received transfer with the following steps:

➔   Cegid Retail Y2 server request to generate the PDF document on the server, by using the printing

templates configured in the Back Office.

➔   Loading the PDF to the service caller as soon as available on server.

➔   Sending the PDF to the service caller, for printing managed by this caller.

Please note: this service does not allow the document to be marked as printed (GP_EDITEE field not

updated). The change in value of this field is reserved for interactive printing, which links the creation of the

PDF to its printing.


## GenerateDocument


### ➔   Objectives

This method prompts the print server to stack the printing request of a document, using its unique identifier

in Cegid Retail Y2.

The report is printed by default in the “software language” as defined in the cultural profile of the user using

this service for the following elements:

➔   The mask: titles and descriptions of the report model.

➔   The format of numbers and dates.

➔   The data transmitted: item descriptions, markdown reason, etc.

The  LanguageId  property allows you to edit the report mask and the format of numbers and dates

according to this new language.

The  CultureId  property allows you to force the formatting of data numbers and dates:

➔   If the LanguageId property is missing.

➔   If the LanguageId property is identical to the "software language" in the user’s cultural profile.

The data remains in the user's language.

Only the native Cegid report generator is used to generate the PDF.


### ➔   Improvements

Added the capability to generate transfer requests.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

11/15/2022

A2336

PR 139966

#4.226


Cegid Retail Y2 – Transfer Plugin

26


## Poll


### ➔   Objectives

At the end of the PDF generation call, the Poll method is called to find out its availability.

In interactive mode, we advise to make a first call after 5 seconds, then every 2 seconds without time limit,

leaving the user the possibility to interrupt the wait.

In batch mode, a call every 5 seconds is recommended, with a maximum of 10 calls.


## Download


### ➔   Objectives

When the Poll returns positively, the Download method is used to download the PDF and print it on a

printer, store it or send it by e-mail.


Cegid Retail Y2 – Transfer Plugin

27


### 6.   O THER


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

345250

#6:24 AM


