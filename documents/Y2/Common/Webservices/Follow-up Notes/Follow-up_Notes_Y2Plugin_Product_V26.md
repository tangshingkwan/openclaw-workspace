# Follow-up Notes Y2Plugin Product V26

*Source: Follow-up_Notes_Y2Plugin_Product_V26.pdf | Extracted: 2026-02-27*

---


## Product Plugin V06


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Product Plugin

2


## Preamble

This plugin is a set of web services associated with one or more versions of Cegid Retail Y2.

This document describes its scope of implementation, as well as the changes and corrections made.

Please note: All plugin methods and services can be cited in this document. Only public methods for

which the contract is published can be used by applications not designed by Cegid.

Legal notices

Permission is granted under this Agreement to download documents held by Cegid and to use the

information contained in the documents only internally, provided that: a) the copyright notice on the

documents remains on all copies of the document; material; (b) the use of these documents for personal

and non-commercial use unless it has been clearly defined by Cegid that certain specifications may be

used for commercial purposes; (c) documents will not be copied to networked computers or published on

any type of media unless expressly authorized by Cegid; and (d) no changes are made to these

documents.


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 – Product Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 5

Documentation

5

Y2 versions

6

2.   ASSEMBLYBILLSOFMATERIALS  ....................................................................................................................................... 7

GetListDetail

7

GetDetail

8

3.   BARCODE2DENGINE  ............................................................................................................................................................... 9

Compute

9

4.   BARCODE2DMANAGEMENT  ............................................................................................................................................ 10

GetDetail

10

GetListDetail

11

5.   CATEGORIES  ............................................................................................................................................................................ 12

CreateOrUpdateValue

12

GetValues

12

GetValue

12

6.   COLLECTIONS  .......................................................................................................................................................................... 13

CreateOrUpdateValue

13

GetValues

13

GetValue

13

7.   FINANCIALITEMS  .................................................................................................................................................................... 14

GetListDetail

14

GetDetail

16

8.   IMAGE  ........................................................................................................................................................................................... 18

Get

18

9.   LINKEDITEMS  ........................................................................................................................................................................... 19

GetListDetail

19

GetDetail

20

10.   LIST ................................................................................................................................................................................................. 21

Create

21

GetList

22

Delete

22


Cegid Retail Y2 – Product Plugin

4

CloseAllItems

22

11.   MACROBILLSOFMATERIALS  ............................................................................................................................................ 23

GetListDetail

23

GetDetail

24

12.   MERCHANDISEITEMS  .......................................................................................................................................................... 25

GetListDetail

25

GetDetail

26

13.   REPORT  ....................................................................................................................................................................................... 27

Download

27

EndGenerateLabels

27

GenerateLabels

28

GenerateScansListLabels

28

14.   SCANSLISTS  ............................................................................................................................................................................. 30

Create

30

Delete

30

GetDetail

30

15.   SEARCH  ....................................................................................................................................................................................... 32

GetListDetail

32

16.   STATISTICS ................................................................................................................................................................................ 34

CreateOrUpdateValue

34

GetValues

34

GetValue

34

17.   TRIGGERS  .................................................................................................................................................................................. 35

Create

35

GetListDetail

35

GetDetail

36

Update

36

Evaluate

36

EvaluateLists

36

18.   OTHER  .......................................................................................................................................................................................... 37

Net Framework 4.8

37

Deployment

37


Cegid Retail Y2 – Product Plugin

5


### 1.   O BJECTIVES

The objective of the  Product  plugin is to provide services relating to the management of items.

This service will be gradually enriched. This first version is used to manage the services allowing:

➔   Retrieving images from an item record.

➔   Management of item lists.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download

page:

"Documentation" is a link that provides access to a documentation list:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Product Plugin

6

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


Cegid Retail Y2 – Product Plugin

7


### 2.   A SSEMBLY B ILLS O F M ATERIALS


## GetListDetail


### ➔   Objectives

This service allows you to search for Assembly-type BoM lists, based on the following search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Lines : Returns BOM detail

o

SystemFields : Returns the system fields of the item record

The following rules are applied:

➔   Items are returned sorted by ID

➔   Searches are performed either by the internal code or by the barcode. It is not allowed to use

both lists.

➔   The search is performed on the exact value transmitted

➔   User restrictions (via the sales divisions) are taken into account.


### ➔   Improvements

Code refactoring (Model), no impact on functionality

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2024

1309475

217582

#4.343

Added an input check for at least one and only one of the Ids and Barcodes criteria.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/19/2024

1281588

218899

#4.350

The method is now set to status Beta

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

The method is now set to status Released

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

8


## GetDetail


### ➔   Objectives

This service allows you to search for a bill of materials of type “Assembly” based on search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Lines : Returns BOM detail

o

SystemFields : Returns the system fields of the item record

Particularity: the identifier entered in the criteria can be the internal code or the barcode of the financial

item.

In the case of a barcode, the value entered must be prefixed by "EXT-".

Example with the - barcode "3000000436240": "EXT-3000000436240"

Apart from this particularity, all the rules of the GetListDetail method are applied.


### ➔   Improvements

Code refactoring (Model), no impact on functionality

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2024

1309475

217582

#4.343

The  method is now set to status Beta

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

The method is now set to status Released

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

9


### 3.   B ARCODE 2DE NGINE


## Compute


### ➔   Objectives

This service calculates the 2D barcode for an item list based on a 2D barcode type The search criteria for

items are based on their identifier or barcode. You can indicate a serial number per item (useful if it is

contained in the 2D barcode)

The following rules are applied:

➔   An exception is raised if the barcode type identifier does not exist.

➔   An item identifier must be specified: Its identifier or barcode

➔   In the case of an item that does not exist or does not belong to the user's sales divisions (query),

no exception is raised, the item is simply not returned in the reply.

➔   The barcode is calculated by concatenating each of the information pieces available in the

barcode definition:

o

Fields left-framed and formatted to the length specified in the settings with special

characters, quotation marks and double quotes removed

o

Application of the specific format if specified; otherwise, the decimal separator is a

comma, and  the date format is the default culture of the server

o

The serial number is the one indicated in the request

o

The prefix is added in 1st position if it is specified

➔   The information returned contains the 2D barcode, the item identifier (ID and barcode) and the

serial number. All this is sorted by item ID and serial number.


### ➔   Improvements

Implementation of the method

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/26/2024

A2496

302744

#4.526

The method is now set to status Beta

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

10


### 4.   B ARCODE 2DM ANAGEMENT


## GetDetail


### ➔   Objectives

This service allows you to search for the settings of 2D-barcode type based on the following search

criteria:

➔   Identifier 2D-barcode type

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

BarcodeElements  Returns the components of the 2D-barcode type


**o   SystemFields  Returns the system fields of the item record**

The following rules are applied:

➔   An exception is raised if the barcode type identifier does not exist.

➔   The “SystemFields” and “BarcodeElements” sections are present in the reply only if they have been

requested in the Fields field.

➔   The properties defining the content are returned sorted in order of priority.

➔   The SpecificFormat section is present in the reply only if the M2L_FMTSPECIAL field of the

database is checked. In this case, optional properties are populated according to field type:

Boolean

Date

Double

Other

DecimalSeparator

X

DecimalNumber

X

DateFormat

X

BooleanFormat

X

➔   The ConstantValue property is only present in the reply for a constant-type field.

➔   The names of the fields defining the 2D-barcode structure are not directly displayed in the reply,

but only the name of the property corresponding to the field.


### ➔   Improvements

Implementation of the method

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/9/2024

A2496

296170

#4.499

The method is now set to status Beta

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

11


## GetListDetail


### ➔   Objectives

This service allows you to search for the settings of 2D-barcode types based on the following search

criteria:

➔   List of Identifiers of 2D-barcode types

➔   Its description: A 2D-barcode type is returned if its label contains the requested description.

➔   Its prefix: A 2D-barcode type is returned if its prefix contains the requested prefix.

➔   Its length

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

BarcodeElements  Returns the components of the 2D-barcode type


**o   SystemFields  Returns the system fields of the item record**

The following rules are applied:

➔   2D-barcode types are returned sorted by Id

➔   No exception is raised if one or more non-existent Ids are called. Non-existent Ids passed in the

request are not present in the reply.

➔   An empty list is returned if no barcode type matches the criteria.

➔   The rules for formatting the reply are defined in the GetDetail method (see above), and are

applied to each barcode type returned.

➔   A paging mechanism is implemented. If no information is provided, only the first 20 barcode

types matching the criteria are returned.


### ➔   Improvements

Implementation of the method

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/9/2024

A2496

296170

#4.499

The method is now set to status Beta

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

12


### 5.   C ATEGORIES

The CATEGORIES service allows the creation, modification and query of item categories.  Deletion is

authorized from the Cegid Retail Y2 menu provided that the category is not used.


## CreateOrUpdateValue


### ➔   Objectives

This method is used either to add a new category, or to modify an existing category in Cegid Retail Y2.

The following business rules are applied:

➔   The number of the category in which you create or modify a value must be a number between 1

and 8.

➔   The name of the category is mandatory.

➔   The short name of the category is mandatory.

➔   The update does not take into account the translation, the wording must be in the original language

of the folder. If the wording changes, the user will have to modify the translations.

The creation or modification of an item category is traced in the event log.


## GetValues


### ➔   Objectives

This method is used to view the different values of an item category.


### ➔   Improvements

Use of PGI_LOOKUP rather than a direct Select on CHOIXCOD to benefit from on-the-fly translation of level

category descriptions.


## GetValue


### ➔   Objectives

This method returns the description and the short description for a value of an item category.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

4/29/2024

1452607

253728

#4.429


Cegid Retail Y2 – Product Plugin

13


### 6.   C OLLECTIONS

The COLLECTIONS service allows the creation, modification and query of item collections. Deletion is

authorized from the Cegid Retail Y2 menu provided that the collection is not used.


## CreateOrUpdateValue


### ➔   Objectives

This method is used either to add a new collection, or to modify an existing collection in  Cegid Retail Y2 .

The following business rules are applied:

➔   The description of the collection is mandatory.

➔   The short description of the collection is mandatory.

➔   The update does not take into account the translation, the wording must be in the original language

of the folder. If the wording changes, the user will have to modify the translations.

The creation or modification of an item collection is traced in the event log.


## GetValues


### ➔   Objectives

This method is used to view the different values of an item collection.


## GetValue


### ➔   Objectives

This method returns the description and the short description for a value of an item collection.


Cegid Retail Y2 – Product Plugin

14


### 7.   F INANCIAL I TEMS


## GetListDetail


### ➔   Objectives

This service allows you to search for lists of financial items, according to the following search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Informations : Returns information from item record

o

SystemFields : Returns the system fields of the item record

o

UserDefinedFields : Returns the system fields of the item record

The following business rules are applied:

➔   Items are returned sorted by ID

➔   Searches are performed either by the internal code or by the barcode. It is not allowed to use

both lists.

➔   The search is performed on the exact value transmitted

➔   User restrictions (via the sales divisions) are taken into account.

Note: Recovery of the item properties used in the sales conditions, to study their presence according to

the type of the item.

The provision of the various properties of the "Informations" tag depends on the financial item type (if no

property is defined for the item type, the tag is not present).

Here is a table specifying, based on the type of the financial item processed, the properties that are

present:

Financial item type

Amount sent

to the EPT

Discount

reason

Maximum

discount

percentage

Store trigger

Item trigger

Combinable

Acquisition of gift certificate

X

X

X

X

Acquisition of gift card

X

X

Acquisition loyalty gift

certificate

X

X

X

X

Acquisition of sales condition

gift certificate

X

X

X

X

X

Deposit reimbursement

X

Credit note reimbursement

X

Gift certificate reimbursement

X

Gift card reimbursement

X

Deposit payment

X


Cegid Retail Y2 – Product Plugin

15


### ➔   Improvements

The  method is now set to the Released status

The method no longer returns the markdown reason for a financial item that can be used as a payment

method.

Added the following information:

In Informations: Type of credit request, Authorization request from a payment service provider, Use with

other items and Associated payment method.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

3/11/2024

1390441

236127

#4.403

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Added the following properties to the reply in the Information tag:

Condition on amounts (ConditionsOnAmounts):

Minimum amount (MinAmount)

Maximum amount (MaxAmount)

Maximum discount (%) when purchasing a gift certificate or gift card (MaxDiscount)

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

12/17/2024

1646232

332496

#5.99

Added the 'Allocation of voucher number method' property to the Informations tag, in the event of

acquisition for financial item types:

-

Acquisition of a gift card

-

Acquisition of a gift certificate

-

Acquisition of a sales condition gift certificate

-

Acquisition of a loyalty gift certificate

-

Deposit payment

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

3/7/2025

1692862

366167

#5.135

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

1/2/2024

1354137

213852

#4.335


Cegid Retail Y2 – Product Plugin

16


## GetDetail


### ➔   Objectives

This service allows you to search one financial items according to the following search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Informations : Returns information from item record

o

SystemFields : Returns the system fields of the item record

o

UserDefinedFields : Returns the system fields of the item record

Particularity: the identifier entered in the criteria can be the internal code or the barcode of the financial

item.

In the case of a barcode, the value entered must be prefixed by "EXT-".

Example with the - barcode "3000000436240": "EXT-3000000436240"

Apart from this particularity, all the rules of the GetListDetail method are applied.


### ➔   Improvements

The  method is now set to the Released status

The method no longer returns the markdown reason for a financial item that can be used as a payment

method.

Added the following information:

In “Informations”: Type of credit request, Authorization request from a payment service provider, Use with

other items and Associated payment method.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

3/11/2024

1390441

236127

#4.403

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Added the following properties to the reply in the “Informations” tag:

Condition on amounts (ConditionsOnAmounts):

Minimum amount (MinAmount)

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

1/2/2024

1354137

213852

#4.335


Cegid Retail Y2 – Product Plugin

17

Maximum amount (MaxAmount)

Maximum discount (%) when purchasing a gift certificate or gift card (MaxDiscount)

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

12/17/2024

1646232

332496

#5.99

Added the 'Allocation of voucher number method' property to the “Informations” tag, in the event of

acquisition for financial item types:

-

Acquisition of a gift card

-

Acquisition of a gift certificate

-

Acquisition of a sales condition gift certificate

-

Acquisition of a loyalty gift certificate

-

Deposit payment

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

3/7/2025

1692862

366167

#5.135


Cegid Retail Y2 – Product Plugin

18


### 8.   I MAGE


## Get


### ➔   Objectives

This method allows you to retrieve the image of an item stored in Cegid Retail Y2.

An item can have several images, the UseType property allows you to specify the "use of the image":

➔   The first image for this use is sent in the case where several images are present for the same use

(lowest rank).

If there is no image for the requested use, no image is returned.

➔   If no use is specified, the first image of the item is sent.

If the item has dimensions, the image of the dimensioned item is returned. If missing, it is up to the caller

to call back the service with the generic item.


Cegid Retail Y2 – Product Plugin

19


### 9.   L INKED I TEMS


## GetListDetail


### ➔   Objectives

This service allows you to search for the list of linked items in a collection of merchandise or bill of

materials items, along with their usage criteria.

The search is based on the following search criteria:

➔   Item identifier

➔   Item barcode

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

ApplicationCriteria  : Returns application criteria.

o

SystemFields : Returns system fields.

The following rules are applied:

➔   Items are returned sorted by ID

➔   Searches are performed either by the internal code or by the barcode. It is not allowed to use

both lists.

➔   The search is performed on the exact value transmitted

➔   User restrictions (via the sales divisions) are taken into account.

➔   If an item exists but has no linked items, it is not included in the reply.

➔   List of usage stores: only one of the "Identifiers" or "Grouping" properties is returned in the reply.


### ➔   Improvements

The  method is now set to the Released status

Added an input check for at least one and only one of the Ids and Barcodes criteria.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/19/2024

1281588

218899

#4.350

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

20


## GetDetail


### ➔   Objectives

This service allows you to search for the list of linked items for merchandise or bill of materials item, along

with their usage criteria.

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

ApplicationCriteria  : Returns application criteria.

o

SystemFields : Returns the system fields of the item record

Particularity: the identifier entered in the criteria can be the internal code or the barcode of the item.

In the case of a barcode, the value entered must be prefixed by "EXT-".

Example with the - barcode "3000000436240": "EXT-3000000436240"

Apart from this particularity, all the rules of the GetListDetail method are applied.


### ➔   Improvements

The  method is now set to the Released status

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

21


### 10.   L IST


## Create


### ➔   Objectives

Item lists can be used in several Cegid Retail Y2 features: gift lists for sales conditions, triggers,

inventories, etc.

This service allows you to create a new list, with the following characteristics:

➔   The integrated items are not closed, and do not have duplicates.

➔   The list must not exceed 100 hits:

o

Lists are loaded into memory and should not be large.

o

The selection of items in a list is not intended to handle hundreds of items.

➔   The following items can be integrated:

o

Service item

o

Bills of materials of type assortment or assembly

o

Single item

o

Dimensioned item (SKU)

o

Generic item, allowing to take into account all dimensions

o

Generic item with one dimension filled in, allowing all other dimensions to be taken into

account.

➔   At the end of the recording, the counters are calculated and returned: number of lines and

number of SKUs in the list.

➔   The Scopes property lists the features that can use it.

➔   The restriction category limits the users who use it.

➔   The creation of the list is recorded in the event log.

➔   Options in sales conditions must be specified, if the “Sales conditions” scope is defined. These

options must not be filled in, if this scope is missing.

➔   The line values are between 0, then 0.0001 up to 999,999,999.99

The creation of the list is recorded in the event log.


### ➔   Improvements

The maximum number of items in a list is increased from 100 to 1,000.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

7/10/2024

1553926

277309

4.455


Cegid Retail Y2 – Product Plugin

22


## GetList


### ➔   Objectives

This service allows you to search for lists, based on search criteria:

➔   List description

➔   Restriction category

➔   Scope of the list


## Delete


### ➔   Objectives

This service is used to delete a list physically from the database.

The removal of the list is recorded in the event log.

Please note:

➔   There is no control over the use of the list. You should make sure before deleting the list that it

will not be used.

➔   This list can only be deleted by a user authorized by the restrictions.


## CloseAllItems


### ➔   Objectives

This service allows you to close all the items in the list.

This action on the list is recorded in the event log.


Cegid Retail Y2 – Product Plugin

23


### 11.   M ACRO B ILLS O F M ATERIALS


## GetListDetail


### ➔   Objectives

This service allows you to search for Macro-type BoM lists, based on the following search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Lines : Returns BOM detail

o

SystemFields : Returns the system fields of the item record

The following rules are applied:

➔   Items are returned sorted by ID

➔   Searches are performed either by the internal code or by the barcode. It is not allowed to use

both lists.

➔   The search is performed on the exact value transmitted

➔   User restrictions (via the sales divisions) are taken into account


### ➔   Improvements

Optimization of the BoM search request.

The  method is now set to the Beta status

Code refactoring (Model), no impact on functionality

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2024

1309475

217582

#4.343

Added an input check for at least one and only one of the Ids and Barcodes criteria.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/19/2024

1281588

218899

#4.350

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

9/18/2023

1237299

189647

#4.283

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

24

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529


## GetDetail


### ➔   Objectives

This service allows you to search for a bill of materials of type “Macro” based on search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Lines : Returns BOM detail

o

SystemFields : Returns the system fields of the item record

Particularity: the identifier entered in the criteria can be the internal code or the barcode of the financial

item.

In the case of a barcode, the value entered must be prefixed by "EXT-".

Example with the - barcode "3000000436240": "EXT-3000000436240"

Apart from this particularity, all the rules of the GetListDetail method are applied.


### ➔   Improvements

The method is now set to the Beta status

Code refactoring (Model), no impact on functionality

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2024

1309475

217582

#4.343

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

25


### 12.   M ERCHANDISE I TEMS


## GetListDetail


### ➔   Objectives

This service allows you to search for merchandise lists, based on the following search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Characteristics : Returns information from item record

o

SystemFields : Returns the system fields of the item record

o

UserDefinedFields : Returns the system fields of the item record

o

UserFields : Returns user fields

The following business rules are applied:

➔   Items are returned sorted by ID

➔   Searches are performed either by the internal code or by the barcode. It is not allowed to use

both lists.

➔   The search is performed on the exact value transmitted

➔   User restrictions (via the sales divisions) are taken into account.

➔   Dimension management:

o   Section “Dimensions”  is missing for single items.

o   Dimension mask is present for generic and dimensioned items.

o   Dimension details are present only for dimensioned items.

➔   User-defined information: all user-defined tables are systematically returned in the reply (empty

or filled in) as soon as they have been requested.

➔   User fields:

o   Only user fields defined for the item are returned.

o   An empty list is returned, if no user fields have been defined for the item.

o   User fields are defined at the single or generic article level.

o   The "UserFields" tag is missing for a dimensioned item.


### ➔   Improvements

The  method is now set to the Beta status

Added an input check for at least one and only one of the Ids and Barcodes criteria.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

26

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/19/2024

1281588

218899

#4.350

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529


## GetDetail


### ➔   Objectives

This service allows you to search one financial items according to the following search criteria:

➔   Item identifier

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Informations : Returns information from item record

o

SystemFields : Returns the system fields of the item record

o

UserDefinedFields : Returns the system fields of the item record

Particularity: the identifier entered in the criteria can be the internal code or the barcode of the financial

item.

In the case of a barcode, the value entered must be prefixed by "EXT-".

Example with the - barcode "3000000436240": "EXT-3000000436240"

Apart from this particularity, all the rules of the GetListDetail method are applied.


### ➔   Improvements

The  method is now set to the Released status

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

27


### 13.   R EPORT

The REPORT service allows the management of reports related to items.


## Download


### ➔   Objectives

This method downloads the PDF file that was generated by one of the Generate methods below.

The following business rules are applied:

➔   The identifier of the file to be downloaded must exist.

In response, a link will allow you to download the PDF document to your computer.


### ➔   Improvements

The method is now set to status Beta

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

352551

#5.122


## EndGenerateLabels


### ➔   Objectives

This method allows you to check the progress of a label printing request in  Cegid Retail Y2.

The following business rules are applied:

➔   The process ID must exist

If the EventLog section is populated, the event log identifier will update it to indicate that printing is

complete if it is.

In response, the Report section is populated only if the PDF was successfully generated. The identifier of

the generated file allows you to download it via the Download method


### ➔   Improvements

The method is now set to status Beta

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

28


## GenerateLabels


### ➔   Objectives

This method is used to initiate a request to generate PDF file for labels of an item list in  Cegid Retail Y2.

The following business rules are applied:

➔   At least one item must be provided in the Items list

➔   If the reprint request is requested and the reprint reason is entered, it must exist

➔   The reason for reprint must only be entered when reprinting.

➔   The printing template, language, and the store must exist.

In reply, the information indicates the progress of the PDF generation request.

➔   The JobId is returned only if the generation could not be finalized within the requested time

(WaitTimeOut in request). This JobId is used to call the EndGenerateLabels method, which indicates

the status of the generation.

➔   The Report section is populated only if PDF generation was successful. The identifier of the

generated file allows you to download it via the Download method

➔   The EventLog section is populated if the event log is updated, i.e., if a reprint is made.


### ➔   Improvements

Corrected the exception that occurred if the price search date was not passed in.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

1/14/2025

A2497 -

1687624

344461

#5.115

The method is now set to status Beta

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

352551

#5.122


## GenerateScansListLabels


### ➔   Objectives

This method is used to initiate a request to generate PDF file for labels of a scan list in  Cegid Retail Y2.

The following business rules are applied:

➔   The scan list must exist


Cegid Retail Y2 – Product Plugin

29

➔   The printing template, language, and the store must exist.

In reply, the information indicates the progress of the PDF generation request.

➔   The JobId is returned only if the generation could not be finalized within the requested time

(WaitTimeOut in request). This JobId is used to call the EndGenerateLabels method, which indicates

the status of the generation.

➔   The Report section is populated only if PDF generation was successful. The identifier of the

generated file allows you to download it via the Download method


### ➔   Improvements

Corrected the exception that occurred if the price search date was not passed in.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

1/14/2025

A2497 -

1687624

344461

#5.115

The method is now set to status Beta

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

352551

#5.122


Cegid Retail Y2 – Product Plugin

30


### 14.   S CANS L ISTS

The SCANLISTS service handles the creation, deletion and query of a list of item scans.


## Create


### ➔   Objectives

This method is used to add a new list to scan in  Cegid Retail Y2 .

The following business rules are applied:

➔   The scan list identifier is a Guid.

➔   The description of the scan list is mandatory.

➔   The device that entered the scan list is mandatory.

➔   The store where the scan list was entered is mandatory and must be authorized for the user.

➔   To identify an item in the scan list of scans, you can use its identifier or its barcode. You can enter

both but they must be consistent.


### ➔   Improvements

Added the possibility of entering quantities with decimals.

Note: 4 decimal places maximum (maximum managed by Y2)

Added a check on the quantity that must be 1 for items with a given serial number.


## Delete


### ➔   Objectives

This method is used to delete a list to scan in  Cegid Retail Y2 .

The following business rules are applied:

➔   The scan list identifier is a Guid and mandatory.

➔   The store of the scan list must be authorized for the user.


## GetDetail


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

7/20/2023

1207647

180618

#4.167

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/20/2023

1208585

202536

#4.319


Cegid Retail Y2 – Product Plugin

31

This method is used to view a scan list.

The store of the scan list must be authorized for the user.


### ➔   Improvements

Added the possibility of returning quantities with decimals.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/20/2023

1207647

180618

#4.167


Cegid Retail Y2 – Product Plugin

32


### 15.   S EARCH


## GetListDetail


### ➔   Operation

This service allows you to search for item lists, based on the following search criteria:

➔   Item identifier

➔   Item barcode

➔   Fields tag to filter the information to be returned (Many – Enum – Optional)

o

Informations : Returns information from item record

o

SystemFields : Returns the system fields of the item record

o

UserDefinedFields : Returns the system fields of the item record

o

UserFields : Returns the user fields of the item record

The following business rules are applied:

➔   Items are returned sorted by ID

➔   Searches are performed either by the internal code or by the barcode. It is not allowed to use

both lists.

➔   The search is performed on the exact value transmitted

➔   User restrictions (via the sales divisions) are taken into account.

Note: Recovery of the item properties used in the sales conditions, to study their presence according to

the type of the item.

Note: neutralization of the "Item groups" and "Gross unit price", specific to the shopping cart:

Criteria/Item type

Number    Merchandise    Financial    Service

Macro

BOM

Assembly

BOM

Assortment

BOM

Item code

Yes

Yes

Yes

Yes

Yes

Yes

Categories/Sub-

categories

1..8

Yes

NO

Yes

Yes

Yes

Yes

Collection

Yes

NO

Yes

Yes

Yes

Yes

Statistics

1. 2

Yes

NO

Yes

Yes

Yes

Yes

User-defined tables

1..15

Yes

Yes

Yes

NO

Yes

Yes

User fields

X

Yes

NO

NO

Yes

Yes

Yes

User-defined texts

1..3

Yes

Yes

Yes

NO

Yes

Yes


### ➔   Improvements

The  method is now set to the Beta status


Cegid Retail Y2 – Product Plugin

33

Added an input check for at least one and only one of the Ids and Barcodes criteria.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/19/2024

1281588

218899

#4.350

Added optimization to search for UserFields only if they are requested in response to the call via the

'Fields' tag.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

7/29/2024

1371504

283280

#4.460

The method is now set to status Released

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

9/27/2024

1565857

303838

#4.529

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

203241

#4.325


Cegid Retail Y2 – Product Plugin

34


### 16.   S TATISTICS

The STATISTICS service allows the creation, modification and query of item statistics 1 and 2.   Deletion is

authorized from the Cegid Retail Y2 menu provided that the statistics are not used.


## CreateOrUpdateValue


### ➔   Objectives

This method is used either to add new statistics, or to modify existing statistics in  Cegid Retail Y2 .

The following business rules are applied:

➔   The description of the statistic is mandatory.

➔   The short description of the statistic is mandatory.

➔   The update does not take into account the translation, the wording must be in the original language

of the folder. If the wording changes, the user will have to modify the translations.

The creation or modification of item statistics is traced in the event log.


## GetValues


### ➔   Objectives

This method is used to view the different values of an item statistic.


### ➔   Improvements

Use of PGI_LOOKUP rather than a direct Select on CHOIXCOD to benefit from on-the-fly translation of the

descriptions for item user-defined statistics.


## GetValue


### ➔   Objectives

This method returns the description and the short description for a value of an item statistics.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

4/29/2024

1452607

253728

#4.429


Cegid Retail Y2 – Product Plugin

35


### 17.   T RIGGERS


## Create


### ➔   Objectives

Modules such as loyalty, sales conditions, entry of user-defined tables, and payment methods use filters

based on items.

For example: Applying a sales condition only on items of category 1 "F01" and user-defined table 3 "T01".

Triggers are created with this objective in mind, making it possible to set filters that depend on the value of

certain fields.

Business rules

The following business rules are applied:

➔   The trigger type includes a single choice among those 3 (mandatory):

o

Fields (TriggerFields = True)

o

Item list (TriggerItemList  = True)

o

Groupings (TriggerGroupingField = True)

➔   For the trigger type “Fields”:

o

Lines must be filled in progressively: a line can only be filled in if it is the first line or if the

previous line is filled in.

o

Exception in the case of line 4 which can only be filled in if the first line is filled in (and not

line 3.)

o

A line is either empty or filled with the 3 pieces of information: Field / Field operator /

Value.

o

If line 2, 3, 5 or 6 is filled in, the operator of the previous line must be specified.

➔   For the trigger type “Item List”:

o

The list of items is mandatory but is not checked. If there is no list, the trigger will not

work.

➔   For the trigger type "Grouping":

o

The selection and exclusion lines must be filled in progressively: a line can only be filled

in, if it is the first line or if the previous line is filled in.

o

The first line must be filled in.

o

If a grouping field is filled in, the value is mandatory.

o

The consistency of the values is not checked.

➔   The user provides the filtering by the user restriction.

➔   The restriction category used must include the "Trigger" scope.


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The user provides the filtering by the user restriction.

➔   If the scope of use is not specified, no filter will be applied to the scope.


Cegid Retail Y2 – Product Plugin

36

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.


## GetDetail


### ➔   Objectives

The  GetListDetail  method are applied.


## Update


### ➔   Objectives

The rules of the  Create  method are applied.


## Evaluate


### ➔   Objectives

This method evaluates whether an item meets the conditions of the trigger.


## EvaluateLists


### ➔   Objectives

This method is meant to assess a list of triggers with a list of items. In return, we get a list of triggers and

the items being part of it.


### ➔   Improvements

The method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179136

#4.159


Cegid Retail Y2 – Product Plugin

37


### 18.   O THER


## Net Framework 4.8

Following Microsoft‘s announcement about the “end of support for .NET Framework 4.5.2, 4.6 and 4.6.1 as

soon as April 26, 2022" the plugin now requires the installation of the .Net Framework 4.8 (runtime) on

server components.


## Deployment

Added installation kit for ReportService.


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

342906

#5.113

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

9/22/2023

1239802

190638

#4.291


