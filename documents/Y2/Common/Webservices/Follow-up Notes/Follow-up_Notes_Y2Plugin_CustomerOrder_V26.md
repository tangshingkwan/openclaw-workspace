# Follow-up Notes Y2Plugin CustomerOrder V26

*Source: Follow-up_Notes_Y2Plugin_CustomerOrder_V26.pdf | Extracted: 2026-02-27*

---


## CustomerOrder Plugin V07


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – CustomerOrder Plugin

2


## Preamble

This plugin is a set of web services associated with one or more versions of Cegid Retail Y2.

This document describes its scope of implementation, as well as the changes and corrections made.

Please note: All plugin methods and services can be cited in this document.  Only public methods for which

the contract is published can be used by applications not designed by Cegid.

Legal notices

Permission is granted under this Agreement to download documents held by Cegid and to use the

information contained in the documents only internally, provided that:  (a) the copyright notice on the

documents remains on all copies of the document; material; (b) the use of these documents for personal

and non-commercial use unless it has been clearly defined by Cegid that certain specifications may be used

for commercial purposes; (c) documents will not be copied to networked computers or published on any

type of media unless expressly authorized by Cegid; and (d) no changes are made to these documents.


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 – CustomerOrder Plugin

3


## Contents

Preamble

2

1

OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2

DOCUMENTSSETTINGS  ........................................................................................................................................................ 6

GetStoreDetail

6

GetStoreListDetail

6

3

MANAGEMENT  ............................................................................................................................................................................ 8

CreateFrom

8

CreateFrom2

10

GetListDetail

12

GetDetail

14

Refuse

14

Close

15

Create

15

Update

16

Replace

19

4

PICKUPPOINT  ........................................................................................................................................................................... 20

UpdateStatus

20

5

REPORT  ....................................................................................................................................................................................... 22

GenerateDocument

22

Poll

22

Download

23

6

REPORT2  .................................................................................................................................................................................... 24

Download

24

EndGenerateLabels

24

GenerateLabels

25

7

OTHER  .......................................................................................................................................................................................... 26

Net Framework 4.8

26


Cegid Retail Y2 – CustomerOrder Plugin

4


### 1   O BJECTIVES

The  CustomerOrder  plugin is used to manage the flow of customer orders. A document transformation

service is currently available for two flows. This service will be gradually enriched.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

"Documentation" is a link that provides access to the documentation list:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

➔   Exceptions

This part provides access to exceptions, classified by type, and according to the plugin.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – CustomerOrder Plugin

5

➔   Installation

This page allows you to download Web Services installation and consumption documentation.


## Y2 versions

This plugin is compatible with the following version of Cegid Retail Y2:

➔   Version 26

Note:

The # sign at the beginning of the plugin build number corresponds to the major version of Cegid Retail

Y2.


Cegid Retail Y2 – CustomerOrder Plugin

6


### 2   D OCUMENTS S ETTINGS


## GetStoreDetail


### ➔   Objectives

The purpose of this service is to retrieve the settings for one of the following document types:

-

AvailableOrder

-

CustomerDelivery

-

CurstomerOrder

-

DeliveryPreparation

-

ReturnNotice

Business rules

The store must exist and not be included in the user's restrictions.


### ➔   Improvements

Implementation of the method

The method is now set to the Beta status.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

07/2024

A2490

283551

#5.414

The list of user fields available for a document type is now returned in the reply, provided it is  requested

in the request (specifying the Fields property with the new value UserFields.)

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

12/13/2024

A2507

332622

#5.451

The method is now set to the Released status

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352499

#5.470


## GetStoreListDetail


### ➔   Objectives

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/10/2023

A2473

199863

#5.316


Cegid Retail Y2 – CustomerOrder Plugin

7

The purpose of this service is to retrieve the settings for one of the following document types:

-

AvailableOrder

-

CustomerDelivery

-

CurstomerOrder

-

DeliveryPreparation

-

ReturnNotice

Business rules

The store must exist and not be included in the user's restrictions.

If no document type is specified, then all possible document types are concerned.


### ➔   Improvements

Implementation of the method

The method is now set to the Beta status.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

07/2024

A2490

283551

#5.414

The list of user fields available for a document type is now returned in the reply, provided it is  requested

in the request (specifying the Fields property with the new value UserFields.)

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

12/13/2024

A2507

332622

#5.451

The method is now set to the Released status

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352499

#5.470

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/10/2023

A2473

199863

#5.316


Cegid Retail Y2 – CustomerOrder Plugin

8


### 3   M ANAGEMENT


## CreateFrom


### ➔   Objectives

The objective of this service is to be able to manage the delivery of merchandise, in the case of e-commerce

orders, or orders entered directly on the cash register.

The following flows are available:

•

Generation of a delivery preparation from a customer order.

•

Generation of a delivery from a customer order.

•

Generation of a delivery from a delivery preparation

Note: depending on the Y2 invoicing on delivery configuration of the e-commerce order management

process, generation of a delivery creates the receipt, subject to French law.

Business rules

The generation of orders and preparations as delivery slips addresses the following functions:

•

Overall generation of a document without passing lines in the contract.

•

Line-by-line generation to take account any remaining information in the document, according to

its options.

•

Management of lines in quantity, with no concept of valuation, with recovery of the original

document valuation and calculation of the document pro-rata to the quantities prepared/delivered.

•

No concept of movement reason.

•

Integration of a warehouse in the header (for all lines) or a line-specific warehouse.

•

Recognition of the document converted by the Y2 number or the internal reference.

•

Integration of serial numbers with a mandatory unit quantity.

Internal reference

The internal reference is the key to identifying a document to be converted. Any document converted by

this service should have a unique internal reference.

Similarly, the documents generated will also have a unique reference:

•

If the internal reference of the converted document is sent within the contract, it is used and must

be unique for the type and third-party of the document.

•

If the reference is not transmitted, it is:

o

Recovered from the previous document for e-commerce documents, with the internal

reference transmitted in the event of partial conversion.

o

Automatically assigned based on the configuration of the type of documents or recovered

from the previous document for non-e-commerce documents.

Please note: in the event of multiple generation of a document, the internal reference as a document key

should be unique.

Example: Existence of an internal reference customer order, "REF01".


Cegid Retail Y2 – CustomerOrder Plugin

9

•

The service requests the generation of a delivery preparation for part of the merchandise and may

indicate a new internal reference. If the internal reference is not communicated, that of the order

will be recovered: REF01.

•

The delivery preparation can then be converted into a delivery by calling its unique internal

reference, REF01.

•

The customer order is prepared for the second part and generates a new delivery preparation. Only

one solution is possible: the service should indicate a unique internal reference, e.g. REF01_1.

•

The delivery preparation can be converted into a delivery by calling its unique internal reference,

REF01_1.

Generation of an FFO

Invoicing of the delivery is automatic according to the "Invoicing on delivery" configuration.

To remain consistent with Y2, the service does not plan to do so on request.

Closure of original document

The CloseDocument property allows the original document to be closed, based on the folder settings.

Payments

The Payment.Amount property corresponds to the amount of the payment in the document currency.

This part should only exist in the event of an e-commerce order with payment on delivery.

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

Good practice is to specify the OperationUid property in the contract, allowing Cegid Retail Y2 to record

this information, in order not to repeat the processing. This number should therefore be unique.

Example:

•

Software calls the CreateFrom service to generate a document in Cegid Retail Y2.

•

Y2 performs the processing but cannot communicate this information to the caller making then a

fresh attempt:

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

The method is now set to the Obsolete status.


Cegid Retail Y2 – CustomerOrder Plugin

10

Method replaced by CreateFrom2. It has the status Obsolete and will be removed from versions

generated after 2/1/2028.

CivilityId is now managed as optional, to comply with the contract.

(Amendment also made to legalformId)

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

FDE

4/15/2024

1454286

249390

#5.396


## CreateFrom2


### ➔   Objectives

This method cancels and replaces the CreateFrom method above which will be deprecated soon.

This method differs from the previous one in the following ways:

-

The possibility to generate an available order from a customer order

-

The identification of the item which is done without using the search priorities, thus exclusively

through its ID (GA_ARTICLE) or its barcode.

-

The identification of the original document is done exclusively through its key.

The objective of this method is to be able to manage the delivery of merchandise, in the case of e-commerce

orders, or orders entered directly at the cash register.

The following flows are available:

•

Generation of a delivery preparation from a customer order.

•

Generation of a delivery from a customer order.

•

Generation of a delivery from a delivery preparation

•

Generation of an available order from a customer order.

Note: depending on the Y2 invoicing on delivery configuration of the e-commerce order management

process, generation of a delivery creates the receipt, subject to French law.

Business rules

The generation of orders and preparations as delivery slips addresses the following functions:

•

Overall generation of a document without passing lines in the contract.

•

Line-by-line generation to take account any remaining information in the document, according to

its options.

•

Management of lines in quantity, with no concept of valuation, with recovery of the original

document valuation and calculation of the document pro-rata to the quantities prepared/delivered.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

151326

#5.101


Cegid Retail Y2 – CustomerOrder Plugin

11

•

Integration of a warehouse in the header (for all lines) or a line-specific warehouse.

•

Recognition of the transformed document by its Y2 number

•

Integration of serial numbers with a mandatory unit quantity.

Internal reference

Any document converted by this service should have a unique internal reference.

Similarly, the documents generated will also have a unique reference:

•

If the internal reference of the converted document is sent within the contract, it is used and must

be unique for the type and third-party of the document.

•

If the reference is not transmitted, it is:

o

Recovered from the previous document for e-commerce documents, with the internal

reference transmitted in the event of partial conversion.

o

Automatically assigned based on the configuration of the type of documents or recovered

from the previous document for non-e-commerce documents.

Please note: in the event of multiple generations of a document, the internal reference as a document key

should be unique.

Example: Existence of an internal reference customer order, "REF01".

•

The service requests the generation of a delivery preparation for part of the merchandise and may

indicate a new internal reference. If the internal reference is not communicated, that of the order

will be recovered: REF01.

•

The delivery preparation can then be converted into a delivery by calling its unique internal

reference, REF01.

•

The customer order is prepared for the second part and generates a new delivery preparation. Only

one solution is possible: the service should indicate a unique internal reference, e.g. REF01_1.

•

The delivery preparation can be converted into a delivery by calling its unique internal reference,

REF01_1.

Generation of an FFO

Invoicing of the delivery is automatic according to the "Invoicing on delivery" configuration.

To remain consistent with Y2, the service does not plan to do so on request.

Closure of original document

The CloseDocument property allows the original document to be closed, based on the folder settings.

Payments

The Payment.Amount property corresponds to the amount of the payment in the document currency.

This part should only exist in the event of an e-commerce order with payment on delivery.

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

The OperationUid property is mandatory and allows Cegid Retail Y2 to record this information so as not to

repeat the processing. This number should therefore be unique.

Example:

•

Software calls the CreateFrom2 operation service to generate a document in Cegid Retail Y2.


Cegid Retail Y2 – CustomerOrder Plugin

12

•

Y2 performs the processing but cannot communicate this information to the caller making then a

fresh attempt:

•

Thanks to the OperationUid property, which is identical on both calls, Y2 knows that the processing

was successful, and informs the caller.

Recognition of the item

This service allows the item on each line to be found in two ways:

•

Lines.ItemIdentifier.Id: This property uniquely identifies an item using the Cegid Retail Y2 internal

code. This is to be preferred

•

Lines.ItemIdentifier.Barcode: This property allows you to find the item through its unique barcode

in Y2.

If both properties are specified, a consistency check is performed, preventing the registration of a

document with a barcode that does not correspond to that of the item.


### ➔   Improvements

The  method is now set to the Released status

Increased the TransactionNumber property from 35 to 70 characters

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

1/8/2026

2032732

447337

#6.96


## GetListDetail


### ➔   Objectives

The objective of this service is to return a list of customer orders based on defined criteria.

This service can be used by external within the delivery cycle of the goods, especially in case of e-Commerce

orders. This service also takes into account orders entered directly at checkout.

Management of lines

•

This method is part of a new strategy and returns all the lines of the document (generic item line,

comment lines...), these elements being part of the order.

In order to return only the "significant" lines, limit yourself to processing the lines containing an

item code.

Business rules

The search for orders satisfies the following functional requirements:

•

User restrictions on stores are taken into account. In case of pick-up points, restriction on

MEJ_CDEECOMETAB, otherwise restriction on GP_ETABLISSEMENT.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

151326

#5.101


Cegid Retail Y2 – CustomerOrder Plugin

13

•

Are returned only

o

Non-deleted orders GP_SUPPRIME <> ‘X’

o

Orders that are not awaiting approval GP_ETATVISA <> ‘ATT’

•

Blocked e-Commerce orders (GP_STATUTANNUL = ‘001’) or canceled ones (GP_STATUTANNUL =

‘002’) are not returned. If blocked orders are released, the cancellation status GP_STATUTANNUL is

set to ‘003’.

•

If Omni-channel information is not filled in, all orders are returned (E-commerce and non E-

commerce).

Paging

A paging mechanism is set up, with 20 documents per page by default.


### ➔   Improvements

Customer preparations were not returned by the service. Problem fixed.

Fixed the incorrect quantity issue on document lines for items managed with serial numbers (the quantity

returned for each serial number was the overall quantity of the line.)

Serial numbers were not returned in the preparation documents. Problem fixed.

Added missing e-commerce order tracking statuses.

Added the follow-up reference to the request.

The reply from the method now contain decimal quantities.

Fixed the issue that caused serial numbers to be missing in the delivery document response.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/17/2022

1015854

140529

#5.32

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/21/2022

1002582

140702

140804

#5.37

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/22/2022

1032255

141132

#5.40

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/16/2023

A2444

159670

#5.146

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

160371

#5.153

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

8/9/2023

1217991

183754

#5.220


Cegid Retail Y2 – CustomerOrder Plugin

14

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/27/2025

1795759

394708

#6.46


## GetDetail


### ➔   Objectives

The objective of this service is to return the details of a customer order to be delivered, searched by its

identifier.

The management rules of the  GetListDetail  method are applied.


### ➔   Improvements

Customer preparations were not returned by the service. Problem fixed.

Fixed the incorrect quantity issue on document lines for items managed with serial numbers (the quantity

returned for each serial number was the overall quantity of the line.)

Serial numbers were not returned in the preparation documents. Problem fixed.

Fixed the issue that caused serial numbers to be missing in the delivery document response.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/27/2025

1795759

394708

#6.46

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

430750

#6.87


## Refuse


### ➔   Objectives

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/17/2022

1015854

140529

#5.32

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/21/2022

1002582

140702

140804

#5.37

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/

22/2022

1032255

141132

#5.40


Cegid Retail Y2 – CustomerOrder Plugin

15

The objective of this order is to refuse the delivery of a customer order that has been assigned to me by

Headquarters.

Business rules

This method satisfies the following functional requirements:

•

Only an e-commerce order to be delivered to the customer from a store can be processed by this

service.

•

An order that has already been closed, canceled, blocked or awaiting approval cannot be refused.

•

The store of the order must be authorized for the user.

•

The movement reason is mandatory and must be of type "Refusal of goods request".

•

Closing an order causes the following updates:

o

The order associated with the store is closed.

o

The original e-commerce order is reactivated, allowing it to be reassigned to another store.

o

Its tracking status changes to "Refused by the store".

o

The tracking status of the lines is also changed to "Refused" (table MLIGNEECO - field

MEK_LIGECOMSUIVI)

•

A rejected order can be refused again, with the information "UpdateStatus" set to False.

•

The deposits assigned to the e-commerce order are reusable for the next order.


### ➔   Improvements


## Close


### ➔   Objectives

The objective of this service is to close a customer order or an available order in non-e-commerce context.

Please note: Only orders visible to the user may be closed.


### ➔   Improvements

The  method is now set to the Released status


## Create


### ➔   Objectives

This method is used to create a customer order. The implemented business rules are detailed in Analysis

A2287.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

151326

#5.101


Cegid Retail Y2 – CustomerOrder Plugin

16


### ➔   Improvements

Increased the maximum size of the city and address lines to 70 characters.

Addition of the 4th address line

The method is now set to the Beta status

Formatting user-defined tables before they are inserted into the database.

It is no longer necessary to check that the address zip code exists in Y2 table for zip codes..

The zip code and the city are now optional.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

3/14/2024

1396391

238133

#5.385


## Update


### ➔   Objectives

The objective of this service is to modify some data in the header of a non-e-Commerce customer order.

Business rules

This method satisfies the following functional requirements:

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2022

A2351

137115

#5.14

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/9/2022

A2351

137987

#5.18

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

151326

#5.101

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/2/2023

1115230

156907

#5.138

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

11/6/2023

1272235

199766

#5.306


Cegid Retail Y2 – CustomerOrder Plugin

17

•

If there is an optional tag in the query and its value is null, the corresponding column in the

database is reset; but if the tag is not present in the query, the corresponding column is not

modified.

•

The order with the key is given in the query must exist.

•

The order must not be deleted.

•

The order must be alive.

•

The order must not be accounted for.

•

The “non-modifiable document” indicator must be set to false for the order.

•

The store of the order must not be closed.

•

The store of the order must be authorized by the default store restrictions of the connection

user.

•

The salesperson identifier given in the query must exist in the salespeople table.

•

The salesperson's deletion date must not have been reached.

•

The salesperson's contract end date must not have been reached.

•

The salesperson must be attached to the store of the order either through the main store or

through the secondary ones.

•

The salesperson identifier given in the query is recovered in column GP_REPRESENTANT of

the header and in column GL_REPRESENTANT of the lines.

•

The delivery date given in the query is included as it is in GP_DATELIVRAISON of the header

and in the GL_DATELIVRAISON column of the lines except for the comment or subtotal lines.

•

The expiry date given in the query is included as it is in GP_DATEEXPIRATION of the header

and in the GL_DATEEXPIRATION column of the lines except for the comment or subtotal

lines.

•

The external reference given in the query is included as it is in the GP_REFEXTERNE column.

The uniqueness of the external reference is not checked even if this check is activated for the

document type.

•

The date of the external reference given in the query is taken as it is in the

GP_DATEREFEXTERNE column.

•

The follow-up reference given in the query is included as it is in the GP_REFSUIVI column.

The uniqueness of the follow-up reference is not checked even if this check is activated for

the document type.

•

The user dates given in the query are included as they are in the GP_DATELIBREPIECE1 to 3

column, depending on the given identifier.

•

The value of the user (customer) tables given in the query must exist in the associated

subtable defined the document type settings. It is copied to column GP_LIBREPIECE1 to 3,

depending on the given identifier.

•

The value of the user (customer) tables given in the query must exist in the associated

subtable. It is copied to column  GP_LIBRETIERS1 to A, depending on the given identifier.

•

The User fields module must be activated if at least one user field is given in the query.


Cegid Retail Y2 – CustomerOrder Plugin

18

•

The user field whose identifier is given in the query must exist.

•

The value of the user field given in the query must correspond to the type defined in the

user field settings.

o

If the type of the user field is set to "string", the given text value must contain at

least the number of characters set in the minimum size and must not exceed the

maximum size.

o

If the user field type is set to "numerical", the integer part of the given numerical

value must not exceed the number of digits set in the integer part and the decimal

part of this value must not exceed the number of digits set in the decimal part.

o

If the type of the user field set is "selection list", each value of the given value list

must exist in the associated subtable or in the set value list.

•

Each user field given for the order is:

o

Either inserted into the user field table of the document if it does not exist, with an

update of the date and user for the creation and the modification.

o

Or the value of the user field in this table is modified with the given value, updating

the date and user of this modification.

•

If the modified order has already been exported, its export status is changed to "Changed to

be re-exported".

•

The modification date is updated with the date and time of the server (not from the calling

application).

•

The modification user is updated with the code of the login user.

Exclusions

•

The modification of the notepad is not proposed because of format compatibility issues.

•

Address modification is not part of this study, as the order is not for delivery.

•

The “Non modifiable document” and “Non duplicable document” indicators are not

changed.

•

There is no consistency check between the given user fields and the document type settings

(the user field may not be defined in the document settings, or there may be exceptions per

store.)


### ➔   Improvements

The  method is now set to the Released status

Formatting user-defined tables before they are updated in the database.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

151326

#5.101


Cegid Retail Y2 – CustomerOrder Plugin

19


## Replace


### ➔   Objectives

The objective of this operation is to be able to update in “cancel and replace” mode:

-

A non-e-commence customer order

-

A non-e-commerce return notice

Business rules

This method satisfies the following functional requirements:

•

The document to be updated must not be closed or already transformed.

•

For return notices, it is not possible to change the e-commerce order that originated the return. To

manage this case, you must delete the notice and recreate it.

•

The payments of the document to be replaced are deleted. The payments of the new document are

automatically recalculated as currently done in Y2.

•

This method applies the same data consistency checks as those for document creation.


### ➔   Improvements

Increased the maximum size of the city and address lines to 70 characters.

Addition of the 4th address line

The method is now set to the Released status

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/2/2023

1115230

156907

#5.138

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2022

A2351

137115

#5.14

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/9/2022

A2351

137987

#5.18

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/2/2023

A2427

151326

#5.101


Cegid Retail Y2 – CustomerOrder Plugin

20


### 4   P ICK U P P OINT


## UpdateStatus


### ➔   Objectives

New method for updating the follow-up status of an e-commerce order managed at pick-up point:

•

The order managed as a pick-up parcel has been received in the store.

•

The order managed as a pick-up parcel has been delivered to the customer.

This operation returns:

•

True, if update has been carried out

•

False, if status already updated by a previous call

Business rules

The receipt of the package or the delivery to the customer is refused and an exception is raised if:

•

The document key provided as input does not exist or does not correspond to an e-commerce

order managed in a pick-up point (GP_TYPEPROVENANCE = "ECO", MEJ_CDEECOMENVOI= "004")

•

The order is canceled

•

The order is blocked

•

The store of the order does not correspond to an e-commerce store authorized to the user.

•

The order pick-up store (MEJ_CDEECOMETAB) does not correspond to a store authorized to the

user.

The receipt of packages is managed by the store:

•

The receipt of the package is refused and an exception is raised if the order is not in status "Shipped

by the central office" (MEJ_CDEECOMSUIVI= "008")

•

The receipt is accepted with StatusUpdated set to False and no update is performed in the database

in the following cases:

o

The order has already been received in the store (MEJ_CDEECOMSUIVI="016")

o

The order has already been picked up by the customer (MEJ_CDEECOMSUIVI="020")

•

In all other cases, the receipt is accepted with StatusUpdated set to False and an update is

performed in the database:

o

The order is now available in status “Available in store” (MEJ_CDEECOMSUIVI="016")

o

The receipt date of the package is initialized with the execution date/time of the request

(Field MEJ_DATERECCOLIS)

o

The export status of the order (GP_ETATEXPORT) is repositioned to "Changed  to be re-

exported" if it was already set to "Exported"; the modification date of the document is

updated in case of status change.

Management of package delivery to the customer:

•

The handover to the customer is refused and an exception is raised, if the order is not in the

"Available in store" status (MEJ_CDEECOMSUIVI="016")

•

The delivery to the customer is accepted with the StatusUpdated status set to False and no update

is made in the database, if the order has already been withdrawn by the customer

(MEJ_CDEECOMSUIVI="020")


Cegid Retail Y2 – CustomerOrder Plugin

21

•

In all other cases, the handover to the customer is accepted with the StatusUpdated status set to

True, and the database is updated:

o

The order status is set to "Received by customer" (Field MEJ_CDEECOMSUIVI="020")

o

The pick-up date of the package is initialized with the date/time of the request (Field

MEJ_DATERETCOLIS)

o

The export status of the order (GP_ETATEXPORT) is repositioned to "Changed to be re-

exported" if it was set to "Exported", the modification date of the document is updated in

case of status change.

Idempotency

Managed by the fact that a call on an order that already has the updated status has no impact and returns

the "StatusUpdated" information as false.


### ➔   Improvements


Cegid Retail Y2 – CustomerOrder Plugin

22


### 5   R EPORT


## GenerateDocument


### ➔   Objectives

This method prompts the print server to stack the printing request of a document, using its unique identifier

in Cegid Retail Y2.

The report is printed by default in the “software language” as defined in the cultural profile of the user using

this service for the following elements:

➔   The mask: Titles and descriptions of the report template

➔   The format of numbers and dates.

➔   The data transmitted: item descriptions, markdown reason, etc.

The  LanguageId  property allows you to edit the report mask and the format of numbers and dates

according to this new language.

The  CultureId  property allows you to force the formatting of data numbers and dates:

➔   If the LanguageId property is missing.

➔   If the LanguageId property is identical to the "software language" in the user’s cultural profile.

The data remains in the user's language.

Only the native Cegid report generator is used to generate the PDF.

This operation returns:

•

The identifier of the generated file if the generation was fast enough,

•

The identifier of the process in charge of the generation, otherwise. In this case, use the Poll method

to check the end of the generation.


### ➔   Improvements


## Poll


### ➔   Objectives

At the end of the PDF generation call, the Poll method is called to find out its availability.

In interactive mode, we advise to make a first call after 5 seconds, then every 2 seconds without time limit,

leaving the user the possibility to interrupt the wait.

In batch mode, a call every 5 seconds is recommended, with a maximum of 10 calls.


### ➔   Improvements


Cegid Retail Y2 – CustomerOrder Plugin

23


## Download


### ➔   Objectives

When the Poll returns positively, the Download method is used to download the PDF and print on a printer,

store it or send it by e-mail.


### ➔   Improvements


Cegid Retail Y2 – CustomerOrder Plugin

24


### 6   R EPORT 2

This service manages the printouts and their follow-up for a customer order or its associated document

(preparation, delivery).

This service manages the PDF transmission of a customer order its related document (preparation,

delivery) with the following steps:

Request the Cegid Retail Y2 server to generate the PDF (GenerateXX method) on the server, by using the

printing templates configured in the Back Office.

Upload  the PDF to the service caller as soon as it is available on server.

Sending the PDF to the service caller, for printing managed by this caller.


## Download


### ➔   Objectives

This method downloads the PDF file that was generated by one of the Generate methods below.

The following business rules are applied:

•

The identifier of the file to be downloaded must exist.

In response, a link will allow you to download the PDF document to your computer.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

4/8/2025

A2497

383114

#6.15


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

392220

#6.40


## EndGenerateLabels


### ➔   Objectives

This method allows you to check the progress of a label printing request in  Cegid Retail Y2.

The following business rules are applied:

•

The process ID must exist

In response, the Report section is populated only if the PDF was successfully generated. The identifier of

the generated file allows you to download it via the Download method


Cegid Retail Y2 – CustomerOrder Plugin

25

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

4/8/2025

A2497

383114

#6.15


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

392220

#6:40


## GenerateLabels


### ➔   Objectives

This method is used to launch a request to generate a PDF of labels for items in a document identifying a

customer order or a related document (preparation, delivery) .

The following business rules are applied:

•

The document must exist

•

The printing template, language, and the store must exist.

If the print contains the 2D barcode, its setup is retrieved at the store level.

In reply, the information indicates the progress of the PDF generation request.

•

The JobId is returned only if the generation could not be finalized within the requested

time (WaitTimeout in request). This JobId is used to call the EndGenerateLabels method, which

indicates the status of the generation.

•

The Report section is populated only if the PDF generation was successful. The identifier of

the generated file allows you to download it via the Download method

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

4/8/2025

A2497

382867

#6:15


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

392220

#6:40

Fixed issue preventing serial numbers from printing on delivery labels.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/27/2025

1795759

394708

#6.46


Cegid Retail Y2 – CustomerOrder Plugin

26


### 7   O THER


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

1/13/2025

1543349

342467

#5.463


