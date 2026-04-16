# Follow-up Notes Y2Plugin Settings V26

*Source: Follow-up_Notes_Y2Plugin_Settings_V26.pdf | Extracted: 2026-02-27*

---


## Settings Plugin V06


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   20 February 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Settings Plugin

2


## Preamble

This plugin is a set of web services associated with one or more versions of Cegid Retail Y2.

This document describes its scope of implementation, as well as the changes and corrections made.

Please note: All plugin methods and services can be cited in this document. Only public methods for

which the contract is published can be used by applications not designed by Cegid.

Legal notices

Permission is granted under this Agreement to download documents held by Cegid and to use the

information contained in the documents only internally, provided that: (a) the copyright notice on the

documents remains on all copies of the document material; (b) these documents are used for personal

and non-commercial purposes, unless it has been clearly defined by Cegid that certain specifications may

be used for commercial purposes; (c) documents will not be copied to networked computers or published

on any type of media unless expressly authorized by Cegid; and (d) no changes are made to these

documents.


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 – Settings Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 6

Documentation

6

Y2 versions

7

2.   BUSINESSAREAS  ...................................................................................................................................................................... 8

CreateOrUpdate

8

GetDetail

8

GetListDetail

9

3.   CIVILITIES  ................................................................................................................................................................................... 10

Create

10

Delete

10

GetDetail

10

GetListDetail

11

Update

11

4.   COUNTRY  ................................................................................................................................................................................... 12

GetDetail

12

GetListDetail

12

5.   CURRENCIES  ............................................................................................................................................................................ 13

GetDetail

13

GetListDetail

13

GetConversionRates

13

6.   DOCUMENTUSERDEFINEDTABLES  ............................................................................................................................. 15

GetListDetail

15

7.   DOCUMENTUSERFIELDS  .................................................................................................................................................. 16

GetListDetail

16

GetDetail

16

8.   INCOTERMS ............................................................................................................................................................................... 18

CreateOrUpdate

18

Delete

18

GetDetail

19

GetListDetail

19

9.   LEGALFORMS  ........................................................................................................................................................................... 20


Cegid Retail Y2 – Settings Plugin

4

Create

20

Delete

20

GetDetail

20

GetListDetail

21

Update

21

10.   MARKDOWNREASONS  ........................................................................................................................................................ 22

Create

22

Delete

23

GetDetail

23

GetListDetail

24

Update

24

11.   MOVEMENTREASONS  ......................................................................................................................................................... 25

Create

25

Delete

25

GetDetail

25

GetListDetail

26

Update

26

12.   MOVEMENTREASONS2  ...................................................................................................................................................... 28

Create

28

Delete

28

GetDetail

29

GetListDetail

29

Update

30

13.   OFFICIALDOCUMENTTYPES ............................................................................................................................................ 32

CreateOrUpdate

32

Delete

32

GetDetail

33

GetListDetail

33

14.   OPENINGDRAWERREASONS  .......................................................................................................................................... 34

GetDetail

34

GetListDetail

34

15.   PAYMENTMETHODS  ............................................................................................................................................................. 36

GetDetail

36

GetListDetail

37

16.   PERIODICITIES  ........................................................................................................................................................................ 38

Evaluate

38


Cegid Retail Y2 – Settings Plugin

5

GetDetail

38

GetListDetail

39

CreateOrUpdate

39

Delete

40

17.   PRICELISTCATEGORIES  .................................................................................................................................................... 41

CreateOrUpdate

41

GetDetail

41

GetListDetail

42

18.   ROUNDINGRULES  .................................................................................................................................................................. 43

Evaluate

43

GetDetail

43

GetListDetail

44

19.   SHIPPINGMETHODS  ............................................................................................................................................................. 45

CreateOrUpdate

45

Delete

45

GetDetail

46

GetListDetail

46

20.   ZIPCODES  ................................................................................................................................................................................... 48

GetListDetail

48

21.   OTHER  .......................................................................................................................................................................................... 49

Net Framework 4.8

49

Deployment

49


Cegid Retail Y2 – Settings Plugin

6


### 1.   O BJECTIVES

The objective of the  Settings  plugin is to provide services relating to the management of settings

common to several other plugins.

This service will be gradually enriched.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download

page:

"Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.


![Figure 4](./images/img_0004.png)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Settings Plugin

7

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


Cegid Retail Y2 – Settings Plugin

8


### 2.   B USINESS A REAS


## CreateOrUpdate


### ➔   Objectives

This method is used either to new, or to modify a Business area in  Cegid Retail Y2 .

The following business rules are applied:

➔   The short description is mandatory.

➔   If there is an existing value it will be modified.

➔   The update  does not take into account the translation, the wording must be in the original

language of the folder. If the wording changes, the user will have to modify the translations.

➔   The creation and modification of a business area are traced in the event log.


### ➔   Improvements

The method is now set to the Released status


## GetDetail


### ➔   Objectives

This method is used to view the descriptions of a business area.

The following business rules are applied:

➔   The business area identifier in the query is mandatory.


### ➔   Improvements

The method is now set to the Released status

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

July 2022

A2345

125185

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

179177

#4.298

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

July 2022

A2345

124013

#3.110

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

9


## GetListDetail


### ➔   Objectives

This method is used to view a business areas list.

The following business rules are applied:

➔   Business areas are returned in alphabetical order of their identifier.

➔   If the information is specified, the search is performed on the exact value transmitted. In case of

unknown code, no answer is returned


### ➔   Improvements

The method is now set to the Released status

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

July 2022

A2345

123499

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

10


### 3.   C IVILITIES

Civility titles are used to give customers their title as a mark of respect and courtesy:

➔   Mrs., Miss, Mr.

➔   Doctor, Professor, General, Sister

➔   HRN

They can be declined by country

➔   Sir, Lord, Lady


## Create


### ➔   Objectives

The following business rules are applied:

➔   If the abbreviated title is not specified in the query, the first characters of the title are used.

➔   An error is returned if the title already exists.

➔   The restriction category of the title must exist and have the scope "Titles - Legal forms".

➔   The title restriction category must be part of the user's “Titles - Legal-forms” restrictions.


## Delete


### ➔   Objectives

The following business rules are applied:

➔   The title identifier in the query is mandatory.

➔   No information is returned if the title does not exist.

➔   Title management complies to the restriction rules of the login user.


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔   The title identifier in the query is mandatory.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2146

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2146


Cegid Retail Y2 – Settings Plugin

11

➔   Title management complies to the restriction rules of the login user.


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The titles are returned classified by restriction, then by rank, and in alphabetical order of their

identifier.

➔   The user brings the filtering of the user restriction which is to be compared with the title

restriction.

➔   Restrictions of type " ... " (no restriction) are returned in the contract with an empty string.

➔   The number of titles in a folder should not exceed 100 in the vast majority of cases. We do not

implement a paging mechanism, but a 1,000 (thousand) limit on the number of records returned.

A higher number of titles will be considered abnormal, without generating an exception.

It is up to the caller receiving 1,000 records to detect that this is a partial reply, and that a more

precise filter should be added.


## Update


### ➔   Objectives

The following business rules are applied:

➔   The title identifier in the query is mandatory. An error is returned if the title  does not exist.

➔   Title management complies to the restriction rules of the login user.

➔   The restriction category of the title must exist and have the scope "Titles - Legal forms".

➔   The title restriction category must be part of the user's “Titles - Legal-forms” restrictions.

➔   An error is returned if the description, short form, restriction and rank are not filled in.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2146

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2146

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2146


Cegid Retail Y2 – Settings Plugin

12


### 4.   C OUNTRY

Countries are available in Cegid Retail Y2, Back Office > Settings > General > Countries.

They include standardized identification information, and environment management.


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔   The Cegid Retail Y2 country identifier (Id) is mandatory in the query


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.

➔   If the following information is filled in, the search is performed on the exact value transmitted. If

the code is unknown, it is returned in the reply with empty:

o

Ids

o

ISO3AlphaNumCode

o

ISO2AlphaNumCode

o

ISO3NumCode


### ➔   Improvements

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

JPM

Sept. 2021

A2205

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

JPM

Sept. 2021

A2205


Cegid Retail Y2 – Settings Plugin

13


### 5.   C URRENCIES

Creating a currency allows you to specify information such as the currency, its symbol, its ISO codes, and

the terminology used to write numbers in letters.


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔   The currency identifier in the query is mandatory. It is not possible to call this method with an ISO

code because it is not unique in the database.


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   If the "CountryId" information is filled in, the search is performed on the exact value transmitted.

This information is not returned if the code is unknown.

➔   If  Closed  property is missing, all currencies matching the other criteria are returned.


### ➔   Improvements

Search for currencies with a collection of alphanumerical ISO codes or with a collection of numerical ISO

codes.


## GetConversionRates


### ➔   Objectives

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

June 2021

A2203

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

June 2021

A2203

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

12/6/2022

207190

#4.353


Cegid Retail Y2 – Settings Plugin

14

A service operation that returns the exchange rates of a reference currency in one or more conversion

currencies.

➔   A maximum of 10 conversion currencies is allowed.

➔   The Stock Exchange and rate type are mandatory and must be provided by the application using

this service.

➔   A rate of 1 is systematically returned if the reference currency and the conversion currency are

identical.


### ➔   Improvements

Slightly optimized control of currencies transmitted in the contract to limit the number of database

queries.

Dev

Date

CEGID’s

Ref.

Pb Ref.

PR

Plugin Build

no.

Quality Ctrl

ALE

1/27/2022

A2307

101881

#3:41 AM

Dev

Date

CEGID’s

Ref.

Pb Ref.

PR

Plugin Build

no.

Quality Ctrl

HDA

6/10/2024

265825

#4.416


Cegid Retail Y2 – Settings Plugin

15


### 6.   D OCUMENT U SER D EFINED T ABLES

If the information available in the header of a document is not sufficient to characterize it completely, you

can add additional information configured in Cegid Retail Y2, for each type of document in the form of

user-defined tables.

The management of user-defined tables is configured for all document types in the User-defined tables

tab.


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   An exception is returned in the case of a call with a non-existent ID of a document user-defined

table.

➔   In the case of a user-defined table with the use of a subtable, the “values” section contains data

from the table associated with the subtable.

➔   An empty collection is returned if no value is associated with the subtable.

➔   The values of the user-defined table are returned sorted by Id.

➔   The number of values in a user-defined table should not exceed a few hundred. We do not

implement a paging mechanism but a limit of 1,000 (thousand) on the number of records

returned to avoid any risk of server saturation.

A higher number of user-defined table values will be considered as abnormal.

In SOAP exposure, it is up to the caller receiving 1,000 records to detect that this is a partial reply,

and that a more precise filter should be added.

In RESTFULL exposure, an http 206 code "Partial Content" is returned if the list exceeds 1,000

elements.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

NAC

March 2021

A2170


Cegid Retail Y2 – Settings Plugin

16


### 7.   D OCUMENT U SER F IELDS

In addition to user-defined tables, Y2 offers the possibility to manage user fields to fill in additional

information about documents.


## GetListDetail


### ➔   Objectives

This service operation allows you to retrieve the settings of the document user fields defined in Y2.

The following business rules are applied:

➔   User fields and values are returned sorted by rank.

➔   An empty list is returned if the use of user fields is disabled in the folder.

➔   An empty list is returned if no field matches the criteria.

➔   The MinLength and MaxLength properties are only present in the reply for fields of type character

strings.

➔   The DecimalNumber et IntegerPart properties are only present in the reply for numerical fields.

➔   The “SystemFields” and “Values” sections are present in the reply only if they have been requested

in the Fields field.

➔   User restrictions are applied to document-type user fields.

➔   A paging mechanism is implemented for this method. If no information is entered, only the

characteristics of the first 20 user fields are returned.

➔   Values In the case of a user field pointing to a subtable, the “Values” section contains the values of

the subtable.


### ➔   Improvements

The method is now set to the Beta status


## GetDetail


### ➔   Objectives

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build

no.

Quality Ctrl

HDA

1/6/2025

A2507

340758

#5:16 AM

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


Cegid Retail Y2 – Settings Plugin

17

This service operation allows you to retrieve the settings of a particular document user field.

The following business rules are applied:

➔   An exception is raised if the user field identifier does not exist.

➔   An error is raised if the user field is not allowed.

➔   The rules of the GetListDetail method for returning and formatting characteristics are applied.


### ➔   Improvements

The method is now set to the Beta status

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build

no.

Quality Ctrl

HDA

1/6/2025

A2507

340758

#5:16 AM

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


Cegid Retail Y2 – Settings Plugin

18


### 8.   I NCOTERMS


## CreateOrUpdate


### ➔   Objectives

This method is used either to create, or to modify Incoterms in  Cegid Retail Y2 .

The following business rules are applied:

➔   The short description is mandatory.

➔   If there is an existing value it will be modified.

➔   The update does not take into account the translation, the wording must be in the original

language of the folder. If the wording changes, the user will have to modify the translations.

➔   The creation and modification of Incoterms are traced in the event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

January

2023

A2390

148320

#4.80


### ➔   Improvements

The method is now set to the Released status


## Delete


### ➔   Objectives

The following business rules are applied:

➔   The Incoterm identifier in the query is mandatory.

➔   No information is returned if the Incoterm does not exist.

➔   The removal of Incoterms is recorded in the event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

January

2023

A2390

148055


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

179177

#4.298

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

19


## GetDetail


### ➔   Objectives

This method is used to view the descriptions of Incoterms.

The following business rules are applied:

➔   The Incoterm identifier in the query is mandatory.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

December

2022

A2390

144355

#4:58 AM


### ➔   Improvements

The method is now set to the Released status


## GetListDetail


### ➔   Objectives

This method is used to view a list of Incoterms.

The following business rules are applied:

➔   Incoterms are returned in alphabetical order of their identifier.

➔   If the information is specified, the search is performed on the exact value transmitted. In case of

unknown code, no answer is returned

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

November

2022

A2390

138091


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

179177

#4.298

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

20


### 9.   L EGAL F ORMS

Legal forms are used to categorize companies and to prefix their names when creating postal addresses

➔   Examples for France: EI, EURL, SARL, SNC, SAS, SA, GIE, SCI, SCOP, SCIC, etc.

These terms are specific to each country.

➔   Examples for the UAE: Sole Proprietorship, Civil Company, Limited Liability Company, Partnership

Company, Private Shareholding company, Public Shareholding company, etc.


## Create


### ➔   Objectives

The following business rules are applied:

➔   If the abbreviated title is not specified in the query, the first characters of the title are used.

➔   An error is returned if the Legal form already exists.

➔   The restriction category of Legal form must exist and have the scope "Titles - Legal forms".

➔   The legal form restriction category must be part of the user's “Titles - Legal-forms” restrictions.


## Delete


### ➔   Objectives

The following business rules are applied:

➔   The legal form identifier in the query is mandatory.

➔   No information is returned if the Legal form does not exist.

➔   Legal form management complies to the restriction rules of the login user.


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔   The legal form identifier in the query is mandatory.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2147

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2147


Cegid Retail Y2 – Settings Plugin

21

➔   Legal form management complies to the restriction rules of the login user.


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The user brings the filtering of the user restriction which is to be compared with the legal form

restriction.

➔   The Legal forms returned are sorted by restriction, then by rank, and in alphabetical order of their

identifier.

➔   Restrictions of type " ... " (no restriction) are returned in the contract with an empty string.

➔   The number of legal forms in a folder should not exceed 100 in the vast majority of cases. We do

not implement a paging mechanism, but a 1,000 (thousand) limit on the number of records

returned. A higher number of legal forms will be considered abnormal, without generating an

exception.

It is up to the caller receiving 1,000 records to detect that this is a partial reply, and that a more

precise filter should be added.


## Update


### ➔   Objectives

The following business rules are applied:

➔   The legal form identifier in the query is mandatory. An error is returned if the legal form does not

exist.

➔   Legal form management complies to the restriction rules of the login user.

➔   The restriction category of Legal form must exist and have the scope "Titles - Legal forms".

➔   The legal form restriction category must be part of the user's “Titles - Legal-forms” restrictions.

➔   An error is returned if the description, short form, restriction and rank are not filled in.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2147

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2147

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

March 2021

A2147


Cegid Retail Y2 – Settings Plugin

22


### 10.   M ARKDOWN R EASONS

Markdown reasons allow you to justify a discount. They can be used by various functional modules in

Cegid Retail Y2.

Examples:

➔   10% off at checkout through a salesperson’s action, “VIP customer” reason .

➔   20% off of a group of items granted by a sales condition,  “Promotion” reason.

➔   Preferential rate for an item, "Winter Sale" reason.

The discounts and their reasons are then analyzed by the retailer.

The creations, modifications and deletions of markdown reasons generate a record in the event log

(depending on the access rights of the action follow-up.)


## Create


### ➔   Objectives

The following business rules are applied:

➔   The code of the markdown reason must be alphanumerical (digits and/or letters in upper/lower

case.)

➔   At least one markdown type is mandatory.

➔   Some markdown types are exclusive and cannot be combined with others:

o

Loyalty

o

Sales conditions

o

Allocations

o

Software extension

➔   Some markdown types can be combined with each other exclusively:

o

Line discount

o

Price list discount

o

Final selling price

➔   Each “group” of markdown types has its own constraints for the fields that can be filled in (and

therefore used):

Configured fields

Loyalty

Sales

cond.

Allocation

s

Ext.

Soft.

Line

disco

unt

Price

list

discou

nt

FSP

discou

nt

Rounding

No

No

No

No

Yes

No

No

Minimum %

No

No

No

No

Yes

No

No

Maximum %

No

No

No

No

Yes

No

No

Printable at register

No

No

No

No

Yes

No

No

Customer required

Yes

Yes

Yes

No

Yes

Yes

Yes

Operating period

No

No

No

No

Yes

No

Yes

Periodicity

No

No

No

No

Yes

No

Yes

Exclusion period

No

No

No

No

Yes

No

Yes

Store trigger

No

No

No

No

Yes

No

Yes


Cegid Retail Y2 – Settings Plugin

23

Item trigger

No

No

No

No

Yes

No

Yes

➔   For operating and exclusion periods:

o

The period must be consistent: start date less than or equal to end date.

o

If it is filled in, the exclusion period must be included in the operating period.

➔   The user provides the filtering through the user restriction.

➔   The restriction category used should include the "Markdown reasons” scope.

Note: the above table may not reflect the current input behavior of older versions of Cegid Retail

Y2.

➔   In the management of the 3 combinable types, the constraints of the most permissive are applied.

Example: If "Line discount" and "Price list discount" are checked, then it is possible to include the

trigger fields in the query (applicable in the case of "Line discount" and only in this case.) It is up

to the caller using the plugin in read mode (GetDetail) to target the usable information according

to the context.


## Delete


### ➔   Objectives

The following business rules are applied:

➔    The code of the markdown reason (Id) is mandatory.

➔   The user provides the filtering through the user restrictions of GTR_GRPDEMARQUE.


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔   The user provides the filtering through the user restriction.


### ➔   Improvements

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

LDE

March 2021

A2074 - A2156

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

LDE

March 2021

A2074 - A2156

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

LDE

March 2021

A2074

NAC

March 2021

A2169


Cegid Retail Y2 – Settings Plugin

24


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The user provides the filtering through the user restriction.

➔   If the scope of use “Mark-down type” is not specified, no filter will be applied to the markdown

type scope.

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.


## Update


### ➔   Objectives

The business rules of the "Create" method are applied, with the following additions:

➔   The code of the markdown reason (Id) is mandatory.

➔   It is not possible to modify the markdown type when it is not combinable.

➔   Only combinable types allow you to add a new type:

Example: It is possible to add "SalesPriceLists" to a reason that is already of type "SalesLines".

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

LDE

March 2021

A2074

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

LDE

March 2021

A2074 - A2156


Cegid Retail Y2 – Settings Plugin

25


### 11.   M OVEMENT R EASONS

Movement reasons are used to distinguish and justify some specific lines in documents.

Examples:

➔   Justification of an item return.

➔   Explanation of a special entry or withdrawal from stock.


## Create


### ➔   Objectives

The following business rules are applied:

➔   The identifier, the description and the movement types of the movement reason are mandatory in

the query.

➔   If the short description is not specified in the query, the first characters of the description are

used.


## Delete


### ➔   Objectives

The following business rules are applied:

➔   The identifier of the movement reason is mandatory in the query.

➔   No error is returned if the movement reason does not exist.


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔    The identifier of the movement reason is mandatory in the query.

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

NAC

March 2021

A2169

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

NAC

March 2021

A2169

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

NAC

March 2021

A2169


Cegid Retail Y2 – Settings Plugin

26


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔    If no movement type is entered in the query, no filter is applied to the movement type, otherwise

the movement reasons  selected are those with a list of authorized movement types with at least

one of the requested types.

➔   If the description is given in the query, the movement reasons are selected if the label contains

the description given in the query.

➔   An empty collection is returned if no movement reason matches the requested criteria or if no

reason exists


### ➔   Improvements


## Update


### ➔   Objectives

The following business rules are applied:

➔   The identifier of the movement reason is mandatory in the query.

➔   If a field is present in the query, the corresponding data is modified with the value of the field

given in the query.

➔   If a field is not present in the query, the corresponding data is not modified.

➔   The movement types of the movement reason are replaced with those that may be given in the

query (cancel and replace if the property is present).

➔   At least one of the data (the description, the short description or the movement types) must be

specified in the query.


### ➔   Improvements

Three types of use are managed:

-

SpecialInputs: Special movements for inventory input (type I)

-

SpecialOutputs: Special movements for inventory output (type J)

-

Transfers: Transfers (type K).

The existing “InternalMovements” use is kept in the contracts to ensure

backward compatibility of the service and will later become deprecated. With the following operating:

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

NAC

March 2021

A2169

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

NAC

March 2021

A2169


Cegid Retail Y2 – Settings Plugin

27

GetDetail and GetListDetail methods:

-

The “InternalMovements” use in a request returns the reasons of type i, J, and K.

-

The “InternalMovements” use is added to the reply for each reason of type I, J, and K.

➔  Create/Update methods:

-

If “InternalMovements” is present in the request, the reason contains types I, J, and K, regardless

of the values specified in the request for the SpecialInputs, SpecialOutputs and Transfers types.

-

If “InternalMovements” is not present in the request, the reason contains only the types specified

in the request.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AMO

4/26/2023

A2379

166125

#4.231


Cegid Retail Y2 – Settings Plugin

28


### 12.   M OVEMENT R EASONS 2

Movement reasons are used to distinguish and justify some specific lines in documents.

Examples:

➔   Justification of an item return.

➔   Explanation of a special entry or withdrawal from stock.

The MovementReason2 service allows the management of more movement types (usages) for list

lookup, creation and modification compared to MovementReason.


## Create


### ➔   Objectives

The following business rules are applied:

➔   The identifier, the description and the movement types of the movement reason are mandatory in

the query.

➔   If the short description is not specified in the query, the first characters of the description are

used.


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## Delete


### ➔   Objectives

The following business rules are applied:

➔   The identifier of the movement reason is mandatory in the query.

➔   No error is returned if the movement reason does not exist.

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

EPL

June 2023

A2379


Cegid Retail Y2 – Settings Plugin

29


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔    The identifier of the movement reason is mandatory in the query.


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔    If no movement type is entered in the query, no filter is applied to the movement type, otherwise

the movement reasons  selected are those with a list of authorized movement types with at least

one of the requested types.

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

EPL

June 2023

A2379

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

EPL

June 2023

A2379


Cegid Retail Y2 – Settings Plugin

30

➔   If the description is given in the query, the movement reasons are selected if the label contains

the description given in the query.

➔   An empty collection is returned if no movement reason matches the requested criteria or if no

reason exists


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## Update


### ➔   Objectives

The following business rules are applied:

➔   The identifier of the movement reason is mandatory in the query.

➔   If a field is present in the query, the corresponding data is modified with the value of the field

given in the query.

➔   If a field is not present in the query, the corresponding data is not modified.

➔   The movement types of the movement reason are replaced with those that may be given in the

query (cancel and replace if the property is present).

➔   At least one of the data (the description, the short description or the movement types) must be

specified in the query.


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

EPL

June 2023

A2379

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

EPL

June 2023

A2379


Cegid Retail Y2 – Settings Plugin

31

ADU

2/4/2025

A2508

352727

#5:41 AM


Cegid Retail Y2 – Settings Plugin

32


### 13.   O FFICIAL D OCUMENT T YPES


## CreateOrUpdate


### ➔   Objectives

This method allows you to create or modify an official document type in Cegid Retail Y2

The following business rules are applied:

➔   The official document type identifier is mandatory (max. 3 characters)

➔   Description is mandatory.

➔   The short description is mandatory.

➔   If there is an existing value it will be modified.

➔   The creation and modification of an official document type are tracked in the event log.


## Delete


### ➔   Objectives

This method allows you to delete an official document type

The following business rules are applied:

➔   The official document type identifier in the query is mandatory.

➔   Deletion is  prohibited for the P (Passport) identifier .

➔   Deletion is prohibited if the document type is  used in the MDOCOFFICIEL table .

➔   Deletion is tracked in the  event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

SBE

January

2026

2018661

446001

#5.169

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

SBE

January

2026

2018661

446001

#5.169


Cegid Retail Y2 – Settings Plugin

33


## GetDetail


### ➔   Objectives

This method allows you to view an official document type.

The following business rules are applied:

➔   The official document type identifier in the query is mandatory.


## GetListDetail


### ➔   Objectives

This method allows you to view a list of official document types.

The following business rules are applied:

➔   Official document types are returned sorted alphabetically by identifier.

➔   Searches can be performed by identifier and/or part of the description.

➔   Pagination is supported.

➔   When the list of details is empty, the service returns an HTTP  200 (OK)  response with an empty

list, not an error.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ARA

January

2026

2018661

446001

#5.169

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ARA

March 2023

2018661

446001

#5.169


Cegid Retail Y2 – Settings Plugin

34


### 14.   O PENING D RAWER R EASONS

The reasons for opening the drawer are set in the Back Office menu “Settings > Font Office”


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔   The opening reason identifier (Id )for the drawer in Cegid Retail Y2 is mandatory in the query.

➔   The search is performed on the exact value transmitted; if the code is unknown an exception will

be raised.


### ➔   Improvements

The method is now set to the Beta status

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.

➔   Ids: Collection of drawer opening reason identifiers

The search is performed on the exact value transmitted. If the code is unknown, it is returned in

the reply with empty data:

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

AMO

March 2023

A2425

157507

#4.176

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

203321

#4.342

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

AMO

March 2023

A2425

157507

#4.176


Cegid Retail Y2 – Settings Plugin

35


### ➔   Improvements

The method is now set to the Beta status

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

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

203321

#4.342


Cegid Retail Y2 – Settings Plugin

36


### 15.   P AYMENT M ETHODS

Payment methods are used to pay a sales transaction. They include many options depending on the

location of the country of sale, and the rules given by the retailers.

Examples:

➔   Minimum amount of €1 required to use the "Bank Card" payment method.

➔   Maximum cash payment of €1,500 in Greece.

Source:  https://www.europe-consommateurs.eu/en/shopping-internet/cash-payment-limitations.html

➔   Maximum cash refund of €60 by merchants in case of payment by bank card in France.

French government site: https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037852342

➔   Payment method management in the safe

Initially, only the payment methods available in the cash register are taken into account.

The data corresponding to the Characteristics, Front-Office and Cash float tabs are mainly managed by

the services. The Addition tab corresponding to EFT is not taken into account, as EFT is managed

separately.


## GetDetail


### ➔   Objectives

The business rules of the  GetListDetail  method are applied, as well as:

➔    The identifier of the payment mode is mandatory in the query.


### ➔   Improvements

Addition of the "CreditRequestType" property in the detail section, which indicates the type of credit

request sent to the electronic payment system for payment methods such as "Gift cards", "gift

certificates", "Credit notes" and "Already paid deposits" managed by an electronic payment system.

Added

PaymentSupplement section to the details section, which provides additional information about payment

cards:

The following business rules are applied:

➔   PaymentSupplement is not returned unless it is included in the Fields field of the request and

unless it is a payment method of the "credit card" or "payment instruments" category. If it is

present, a "LIKE" will be performed.

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

RLO

March 2021

A2149– A2202

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

12/5/2023

1250083

PR 206765

#4.348


Cegid Retail Y2 – Settings Plugin

37

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

10/17/2025

PR 1972451

#5.115


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The user provides the filtering through the user restriction.

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.

➔   Only the payment types that are available for the cash register are taken into account (checkbox

"Usable at register" in the "Front Office" tab).

➔   The minimum cash amount, the maximum cash amount and the alert amount are only filled in,

and therefore returned, for the cash payment method.

➔   Exceptions per store are taken into account if they exist for the store entered in the query.


### ➔   Improvements

Addition of the "CreditRequestType" property in the detail section, which indicates the type of credit

request sent to the electronic payment system for payment methods such as "Gift cards", "gift

certificates", "Credit notes" and "Already paid deposits" managed by an electronic payment system.

Added

PaymentSupplement section to the details section, which provides additional information about payment

cards:

The following business rules are applied:

➔   PaymentSupplement is not returned unless it is included in the Fields field of the request and

unless it is a payment method of the "credit card" or "payment instruments" category. If it is

present, a "LIKE" will be performed.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

10/17/2025

PR 1972451

#5.115

Dev

Date

CEGID’s Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

RLO

March 2021

A2149– A2202

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

12/5/2023

1250083

PR 206765

#4.348


Cegid Retail Y2 – Settings Plugin

38


### 16.   P ERIODICITIES

Periodicities are available in Y2, Back Office > Settings > General >Periodicities.

Generic periodicities are created and  usable by different functional modules of Y2.

Example:

➔  Apply a specific sales condition on Fridays from 6 to 8 pm


## Evaluate


### ➔   Objectives

Returns a list of valid periodicities in relation to a submission date (list limited to 1000 periodicities.)

The following business rules are applied:

➔   The periodicity is mandatory and must be filled in accurately.

➔   The date/time of submission is that of the client station.

➔   User restrictions will be applied.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

JMO

January 2023

A2415

150182

#4.103


### ➔   Improvements

The method is now set to the Released status


## GetDetail


### ➔   Objectives

Returns the periodicity settings(periodicity record)

The following business rules are applied:

➔    The identifier of the rounding method is mandatory in the query.

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

179177

#4.298

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

BGI

September

2022

A2073


Cegid Retail Y2 – Settings Plugin

39


### ➔   Improvements

The method is now set to the Released status


## GetListDetail


### ➔   Objectives

Returns a list of periodicities based on defined criteria

The following business rules are applied:

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.


### ➔   Improvements

The method is now set to the Released status


## CreateOrUpdate


### ➔   Objectives

Is used to create or modify a periodicity.

The following business rules are applied:

➔   We work using the cancel and replace method. All periodicity information must therefore be

systematically passed on.

➔   The periodicity type must have a unique value (weekly or monthly).

➔   For a weekly periodicity:

o

At least one day must be entered with a time slot other than the default.

o

Time slots between 00:00 and 23:59 must be consistent (start time < end time).

o

The day of validity within the month, between 1 and 31, must be consistent (start day <

end day).

o

In the event of an existing value, the periodicity is modified.

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

179177

#4.298

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

BGI

September

2022

A2073

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

40

➔   For monthly periodicity :

o

At least one month must be entered

o

The time slot, between 00:00 and 23:59, must be consistent (start time < end time).

➔   The creation and modification of a periodicity are reported to the event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

BGI

March 2023

A2073


### ➔   Improvements

The method is now set to the Released status

Default value assigned to properties absent from the periodicity query to be created.


## Delete


### ➔   Objectives

Is used to delete a periodicity.

The following business rules are applied:

➔   The periodicity identifier in the query is mandatory.

➔   A Boolean is returned confirming whether or not the periodicity has been deleted.

➔   The removal of a periodicity is reported to the event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

BGI

March 2023

A2073


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

179177

#4.298

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

NAC

7/18/2024

1423751

279910

#4.423

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

41


### 17.   P RICE L IST C ATEGORIES


## CreateOrUpdate


### ➔   Objectives

This method is used either to create, or to modify a price list category in  Cegid Retail Y2 .

The following business rules are applied:

➔   The short description is mandatory.

➔   If there is an existing value it will be modified.

➔   The update does not take into account the translation, the wording must be in the original

language of the folder. If the wording changes, the user will have to modify the translations.

➔   The creation and modification of Incoterms are traced in the event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RFO

Dec. 2022

A2344

142010

#4:47 AM


### ➔   Improvements

The method is now set to the Released status


## GetDetail


### ➔   Objectives

This method is used to view the descriptions of a price list category.

The following business rules are applied:

➔   The price list category identifier in the query is mandatory.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RFO

A2344

123667

#3.100


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

179177

#4.298

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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

42


## GetListDetail


### ➔   Objectives

This method is used to view a list of price list categories

The following business rules are applied:

➔   The price list categories are returned in alphabetical order of their identifier.

➔   If the information is specified, the search is performed on the exact value transmitted. In case of

unknown code, no answer is returned

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RFO

A2344

123667

#3.100


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

179177

#4.298


Cegid Retail Y2 – Settings Plugin

43


### 18.   R OUNDING R ULES

Rounding methods are available in Cegid Retail Y2, Back Office > Settings > Management > Rounding

methods. They are used to round up or down an amount according to the 4 values described in the

documentation: Threshold (positive or negative) / Weight / Method / Constant.

Please note: The weight of the rounding cannot exceed 2 decimals.

Examples:

Test value

Threshold

Weight

Method

Constant

Result

-12.75

0

0.10

Round down

-12.70

-12.75

0

0.10

Round up

-12.80

12.75

99

0.50

Round down

0.05

#12:45 PM

12.75

99

0.50

Adjust to closer value

(0.5 = 0)

0.05

#12:45 PM

12.75

99

0.50

Adjust to closer value

(0.5 = 1)

0.05

12.95

12.75

99

0.50

Round up

0.05

12.95

112.75

999

#1:00 AM

Round up

0.50

112.50

1112.75

999,999

#10:00 AM

Round up

#5:00 AM

1115.00


## Evaluate

This method applies a rounding method to a transmitted amount.


### ➔   Objectives

The following business rules are applied:

➔    The transmitted amount can be negative, null, or positive, without constraint on the number of

its decimals.


### ➔   Improvements


## GetDetail


### ➔   Objectives

The following business rules are applied:

➔    The identifier of the rounding method is mandatory in the query.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

July 2021

A2210


Cegid Retail Y2 – Settings Plugin

44


## GetListDetail


### ➔   Objectives

The following business rules are applied:

➔   The description is not mandatory; if there is one, a “LIKE” will be performed.

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

July 2021

A2210

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

OXY

July 2021

A2210


Cegid Retail Y2 – Settings Plugin

45


### 19.   S HIPPING M ETHODS


## CreateOrUpdate


### ➔   Objectives

This method is used either to create, or to modify Shipping method in  Cegid Retail Y2 .

The following business rules are applied:

➔   The short description is mandatory.

➔   If there is an existing value it will be modified.

➔   The update  does not take into account the translation, the wording must be in the original

language of the folder. If the wording changes, the user will have to modify the translations.

➔   The creation and modification of the Shipping method are traced in the event log.


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## Delete


### ➔   Objectives

The following business rules are applied:

➔   The Shipping method identifier in the request is mandatory.

➔   A Boolean is returned attesting to the effective deletion or not of the shipping method

➔   The removal of a Shipping method is traced in the event log.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

March 2023

A2391

158989

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

April 2023

A2391

163941


Cegid Retail Y2 – Settings Plugin

46


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## GetDetail


### ➔   Objectives

This method is used to view the descriptions of a Shipping method.

The following business rules are applied:

➔   The Shipping method identifier in the request is mandatory.


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM


## GetListDetail


### ➔   Objectives

This method is used to view a list of Shipping methods

The following business rules are applied:

➔   The Shipping methods are returned in alphabetical order of their identifier.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

March 2023

A2391

158703


Cegid Retail Y2 – Settings Plugin

47

➔   If the information is specified, the search is performed on the exact value transmitted. In case of

unknown code, no answer is returned


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

9/19/2024

1565857

300491

#4.440

The method is now set to status Released

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352727

#5:41 AM

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EBU

March 2023

A2391

158200


Cegid Retail Y2 – Settings Plugin

48


### 20.   Z IP C ODES

Zip codes are available for input in Cegid Retail Y2, Back Office > Settings > General> Zip codes.

Note: The uniqueness of a zip code is guaranteed by the "zip code" and the "city", making it possible to

record several municipalities with the same zip code.

Example for France:

Zip code

Municipality

10400

Bouy sur Orvin

10400

St Aubin

10400

La Saulsotte

10400

Nogent sur Seine

Depending on the country, the zip code can be attached to a region or a district.


## GetListDetail

Only the indexed fields of the table can be used for performance reasons.


### ➔   Objectives

The following business rules are applied:

➔   If the "CountryId" information is filled in, the search is performed on the exact value transmitted.

If the code is unknown, it is returned in the reply with empty information.

➔   The city not mandatory; if there the city property is present, a “LIKE” will be performed.


### ➔   Improvements

Dev

Date

CEGID’s

Ref.

Pb Ref.

SVN Rev.

Plugin Build no.

Quality Ctrl

BGI

Sept. 2021

A2208


Cegid Retail Y2 – Settings Plugin

49


### 21.   O THER


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

1/15/2025

1543349

344737

#5:36 AM

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

190647

#4.326


