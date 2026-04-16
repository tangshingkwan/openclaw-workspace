# Follow-up Notes Y2Plugin Reservation V26

*Source: Follow-up_Notes_Y2Plugin_Reservation_V26.pdf | Extracted: 2026-02-27*

---


## Reservation Plugin V07


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Reservation Plugin

2


## Preamble

This plugin is a set of web services associated with one or more versions of Cegid Retail Y2.

This document describes its scope of implementation, as well as the changes and corrections made.

Please note: All plugin methods and services can be cited in this document. Only public methods for

which the contract is published can be used by applications not designed by Cegid.

Legal notices

Permission is granted under this Agreement to download documents held by Cegid and to use the

information contained in the documents only internally, provided that: (a) the copyright notice on the

documents remains on all copies of the document; material; (b) the use of these documents for personal

and non-commercial use unless it has been clearly defined by Cegid that certain specifications may be

used for commercial purposes; (c) documents will not be copied to networked computers or published on

any type of media unless expressly authorized by Cegid; and (d) no changes are made to these

documents.


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 – Reservation Plugin

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

8

CreateFrom

9

Refuse

10

Update

11

Close

12

3.   REPORT  ....................................................................................................................................................................................... 14

GenerateDocument

14

Poll

14

Download

15

4.   REPORT2  .................................................................................................................................................................................... 16

GenerateLabels

16

EndGenerateLabels

17

Download

17

5.   OTHER  .......................................................................................................................................................................................... 19

Net Framework 4.8

19


Cegid Retail Y2 – Reservation Plugin

4


### 1.   O BJECTIVES

The  Reservation  plugin is used to manage the flow of customer reservations.

➔   Reservation requests

➔   Available reservations

This service will be gradually enriched.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download

page:

"Documentation" is a link that provides access to the documentation list:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties.

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Reservation Plugin

5

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


Cegid Retail Y2 – Reservation Plugin

6


### 2.   M ANAGEMENT


## GetList


### ➔   Objectives

This service returns the list of customer reservation requests that meet the contract criteria:

➔   Customer and/or reference of the document searched.

➔   List of stores in which to search for reservation requests, in compliance with the user restrictions

specified in the contract.

➔   Document creation period.

➔   Option to return all documents, or only the active ones.

Please note: Reservation requests awaiting approval or associated with blocked orders are not returned.

The "Paging" property provides protection against timeouts due to a significant number of documents.

We recommend that it be used with a setting of a few hundred lines, supplemented by tests for

dimensioning this value according to the communication line.

Please note: the speed of data loading varies according to the device and its location.

The Web Service caller should check that not all information is returned in the first page. It can then call

the next page, until all headers are recovered.

The ExtractByOldest property decides on the order for document recovery:

➔   False: default value, recovering the documents starting with the most recent.

➔   True: recovery of documents starting with the oldest.


### ➔   Improvements

Added user fields in Getlist, Getlistdetail and CreateFrom operations. .

Using the UserRestrictions service of the Identity plugin to control the provided stores.

Added the ClearedQuantity property (field Y2 GL_QTESOLDE) to the reply, allowing you to see the reserved

quantities that have been canceled on reservation requests.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/24/2022

A2299

106901

#4.21

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/22/2023

698738

161253

#5.25

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

11/5/2025

1955393

431375

#6.92


Cegid Retail Y2 – Reservation Plugin

7


## GetDetail


### ➔   Objectives

The GetList service returns a list of reservation requests; the GetDetail service allows you to load the lines

of a document, the identifier of which is specified in the contract.

Please note: Managing an item with a serial number requires a unit quantity for the line.


### ➔   Improvements

Added new properties, external reference, catalog reference, package reference and complementary

description at line level to the reply.

Added the original document

The application of the "Sales query" user restrictions have been revised to:

-

No longer raise the exception CBR_106_0003 in the case of a non-e-commerce order

-

Systematically apply the restrictions on the establishment of the order. In the case of an e-

commerce order, the e-commerce store must belong to the user's restriction.

Correction to take into account the GLS_SOLDERRELIQUAT column in the calculation of the remaining

quantity for lines of items managed by serial number, to exclude closed lines.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

10/30/2025

1984267

INC0264298

430741

#6.90

Added the ClearedQuantity property (field Y2 GL_QTESOLDE) to the reply, allowing you to see the reserved

quantities that have been canceled on reservation requests.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

JMO

3/3/2022

A2302

107416

#4.39

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

4/5/2022

A2340

112352

#4.71

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

4/21/2022

786141

114350

#4.123

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

11/5/2025

1955393

431375

#6.92


Cegid Retail Y2 – Reservation Plugin

8


## GetListDetail


### ➔   Objectives

This service returns the list of customer reservation requests that meet the contract criteria, with details by

line, as with the GetList and GetDetail services.

This service should only be used if a limited number of documents are returned, with few lines.

If there are documents with more than a few dozen lines, this service should not be used, GetList and

GetDetail being preferred.


### ➔   Improvements

Added user fields in Getlist, Getlistdetail and CreateFrom operations. .

Added new properties, external reference, catalog reference, package reference and complementary

description at line level to the reply.

Added the original document

RestFul exposure

Added the follow-up reference to the request.

Using the UserRestrictions service of the Identity plugin to control the provided stores.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/24/2022

A2299

106901

#4.21

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

JMO

3/3/2022

A2302

107416

#4.39

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

4/5/2022

A2340

112352

#4.71

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

4/11/2022

A2275

114463

#4.98

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/17/2023

A2424

160343

#5.17

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/22/2023

698738

161253

#5.25


Cegid Retail Y2 – Reservation Plugin

9

Added the ClearedQuantity property (field Y2 GL_QTESOLDE) to the reply, allowing you to see the reserved

quantities that have been canceled on reservation requests.


## CreateFrom


### ➔   Objectives

The objective of this service is to be able to validate a  reservation request, in the case of e-commerce

orders, or orders entered directly at checkout. An available reservation is then created.

Scope

The generation of orders and preparations as delivery slips addresses the following functions:

•

Overall generation of a document without passing lines in the contract.

•

Line-by-line generation to take account of any remaining information in the document, according

to its options.

•

Possibility to close the reservation request according to the RemainderManagement property.

•

Management of lines in quantity, with no concept of valuation, with recovery of the original

document valuation and calculation of the document pro-rata to the quantities

prepared/delivered.

•

Integration of a warehouse in the header (for all lines) or a line-specific warehouse according to

the generation type.

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

Y2 performs the processing, but cannot communicate this information with the caller, who makes

a fresh attempt:

o

If the OperationUid property is transmitted, Y2 knows that the processing was successful

and informs the caller.

o

With no OperationUid property specified, Y2 attempts to repeat the same processing,

risking the creation of a new document.

We undertake to provide this information; it will soon become mandatory.

Recognition of the item

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

11/5/2025

1955393

431375

#6.92


Cegid Retail Y2 – Reservation Plugin

10

This service allows the item on each line to be found in two ways:

•

Lines.ItemIdentifier.Reference: This property should not be used; it is not reliable.

In the case of a reference with the same level of priority for several items, nothing can predict

which item will be used.

This property will soon be rendered obsolete.

•

Lines.ItemIdentifier.Id: This property identifies an item in a unique way in Cegid Retail Y2 and

should be used.


### ➔   Improvements

Added user fields in Getlist, Getlistdetail and CreateFrom operations. .

Added to new properties ExternalReference, FollowUpReference to the document header, and

ExternalReference, CatalogReference, AdditionalDescription, PackageReference at line level.

Added a new InternalReference property at the document header level, this reference is taken into

account at the e-commerce document level if it is filled in.

This change requires a Core version later than February 2023.


## Refuse


### ➔   Objectives

The objective of this service is to refuse a reservation request, by closing it.

Please note: Only reservation requests visible to the user may be refused.


### ➔   Improvements

RestFul exposure

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/24/2022

A2299

106901

#4.21

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

3/7/2022

A2302

107788

#4.44

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

2/16/2023

A2432

154224

#4.173

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

4/11/2022

A2275

114463

#4.98


Cegid Retail Y2 – Reservation Plugin

11


## Update


### ➔   Objectives

The objective of this service is to modify data in the header of a reservation.

Business rules

•

If there is an optional tag in the query and its value is null, the corresponding column in the

database is reset; but if the tag is not present in the query, the corresponding column is not

modified.

•

The reservation whose key is given in the query must exist.

•

The reservation must not be deleted.

•

The reservation must be alive.

•

The reservation must be counted.

•

The “Non modifiable document” indicator for the reservation must be false.

•

The store of the reservation must not be closed.

•

The store of the reservation must be authorized by the default store restrictions of the connection

user.

•

The salesperson identifier given in the query must exist in the salespeople table.

•

The salesperson's deletion date must not have been reached.

•

The salesperson's contract end date must not have been reached.

•

The salesperson must be attached to the store of the reservation either through the main store or

through the secondary ones.

•

The salesperson identifier given in the query is recovered in column GP_REPRESENTANT of the

header and in column GL_REPRESENTANT of the lines.

•

The expiry date given in the query is included in the GP_DATEEXPIRATION report of the header

and in the GL_DATEEXPIRATION column of the lines except for the comment or subtotal lines.

•

The external reference given in the query is included as it is in the GP_REFEXTERNE column.

The uniqueness of the external reference is not checked, even if this check is activated for

document type, because Cegid Retail Y2 checks that the code entered is not the external

reference of one of the documents relating to the customer of the reservation. This verification is

not adapted to in-store reservations but rather to  purchase or B2B flows.

•

The same operation is applied to the follow-up reference.

•

The date of the external reference given in the query is taken as it is in the GP_DATEREFEXTERNE

column.

•

The user dates given in the query are included as they are in the GP_DATELIBREPIECE1 to 3

column, depending on the given identifier.

•

The value of the user (customer) tables given in the query must exist in the associated subtable

defined the document type settings.

•

The value of the user tables given in the query is copied into the GP_LIBREPIECE1 to 3 column

according to the given identifier.

•

The value of the user (customer) tables given in the query must exist in the associated subtable.

•

The value of the user (customer) tables given in the query is copied into the GP_LIBRETIERS1 to A

column according to the given identifier.

•

The User fields module must be activated if at least one user field is given in the query.

•

The user field whose identifier is given in the query must exist.


Cegid Retail Y2 – Reservation Plugin

12

•

The value of the user field given in the request must correspond to the type defined in the user

field settings.

•

If the type of the user field is set to "string", the given text value must contain at least the number

of characters set in the minimum size and must not exceed the maximum size.

•

If the user field type is set to "numerical", the integer part of the given numerical value must not

exceed the number of digits set in the integer part and the decimal part of this value must not

exceed the number of digits set in the decimal part.

•

If the type of the user field set is "selection list", each value of the given value list must exist in the

associated subtable or in the set value list.

•

Each user field given for the reservation is either inserted into the table of user fields if it does not

exist, or the value of the user field in this table is modified with the given value, and the

modification date and the user are updated if the user field already exists for the reservation.

•

If the modified reservation has already been exported its export status is changed to "Changed to

be re-exported".

•

The modification date is updated with the date and time of the server (not from the calling

application).

•

The modification user is updated with the code of the connection user.

•

A notification is sent through the Y2 notification system when the reservation is actually updated..

Exclusions

•

The modification of the notepad is not proposed because of format compatibility issues.

•

No business case of modification of e-Commerce data for reservations has been identified.

•

The modification of addresses does not seem relevant for reservations.

•

The “Non modifiable document” and “Non duplicable document” indicators are not changed.

•

There is no consistency check between the given user fields and the document type settings.

Idempotency

•

This is an idempotent operation, given the updated data.


### ➔   Improvements


## Close


### ➔   Objectives

The objective of this service is to close a customer reservation in non-e-commerce context.

Please note: Only customer reservations visible to the user may be closed.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/28/2022

A2298

111046

#4.70


Cegid Retail Y2 – Reservation Plugin

13


### ➔   Improvements

The method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179143

#5.66


Cegid Retail Y2 – Reservation Plugin

14


### 3.   R EPORT

This service manages transmission of the PDF of an available reservation, once a reservation request has

been validated, with the following steps:

➔   Cegid Retail Y2 server request to generate the PDF document on the server, by using the printing

templates configured in the Back Office.

➔   Loading of the PDF to the service caller as soon as available on server.

➔   Sending the PDF to the service caller, for printing managed by this caller.

Please note: this service does not allow the document to be marked as printed (GP_EDITEE field not

updated). The change in value of this field is reserved for interactive printing, which links the creation of

the PDF to its printing.


## GenerateDocument


### ➔   Objectives

This method prompts the print server to stack the printing request of a document, using its unique

identifier in Cegid Retail Y2.

The report is printed by default in the “software language” as defined in the cultural profile of the user

using this service for the following elements:

➔   The mask: titles and descriptions of the status model.

➔   The format of numbers and dates.

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


Cegid Retail Y2 – Reservation Plugin

15

In interactive mode, we advise to make a first call after 5 seconds, then every 2 seconds without time limit,

leaving the user the possibility to interrupt the wait.

In batch mode, a call every 5 seconds is recommended, with a maximum of 10 calls.


### ➔   Improvements


## Download


### ➔   Objectives

When the Poll returns positively, the Download method is used to download the PDF and print it on a

printer, store it or send it by e-mail.


### ➔   Improvements


Cegid Retail Y2 – Reservation Plugin

16


### 4.   R EPORT 2

The Report2 service allows the management of printout for labels related to reservation documents.

The following steps are to be respected:

➔   Requests the Cegid Retail Y2 server to generate the PDF of the document on the server, by using

the printing templates configured in the Back Office.

➔   Upload the PDF to the service caller as soon as it is available on server.

➔   Send the PDF to the service caller, for printing managed by this caller.


## GenerateLabels


### ➔   Objectives

This method is used to initiate a request to generate the PDF file for labels of a reservation document in

Cegid Retail Y2.

The following document types are processed:

-

Customer reservation

The following business rules are applied:

•

A document identifier must be filled in and exist

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


### ➔   Improvements

The method is now set to the Beta status..

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/19/2025

A2497

392228

#6:35

Fixed issue preventing serial numbers from printing on reservation labels.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2025

A2497

PR 382738

# 6.32


Cegid Retail Y2 – Reservation Plugin

17

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/26/2025

1795759

394382

#6:40


## EndGenerateLabels


### ➔   Objectives

This method allows you to check the progress of a label printing request in  Cegid Retail Y2.

The following business rules are applied:

•

The process ID must exist

In response, the Report section is populated only if the PDF was successfully generated. The identifier of

the generated file allows you to download it via the Download method.


### ➔   Improvements

The method is now set to the Beta status..

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/19/2025

A2497

392228

#6:35


## Download


### ➔   Objectives

This method downloads the PDF file that was generated by one of the Generate methods below.

The following business rules are applied:

•

The identifier of the file to be downloaded must exist.

In response, a link will allow you to download the PDF document to your computer.


### ➔   Improvements

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2025

A2497

PR 383071

# 6.32

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2025

A2497

PR 383071

# 6.32


Cegid Retail Y2 – Reservation Plugin

18

The method is now set to the Beta status..

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/19/2025

A2497

392228

#6:35


Cegid Retail Y2 – Reservation Plugin

19


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

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/14/2025

1543349

342944

#5.206


