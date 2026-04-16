# Follow-up Notes Y2Plugin Company V26

*Source: Follow-up_Notes_Y2Plugin_Company_V26.pdf | Extracted: 2026-02-27*

---


## Company Plugin V04


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Company Plugin

2


## Preamble

This plugin is a set of web services associated with one or more versions of Cegid Retail Y2.

This document describes its scope of implementation, as well as the changes and corrections made.

Please note: All plugin methods and services can be cited in this document.  Only public methods for

which the contract is published can be used by applications not designed by Cegid.

Legal notices

Permission is granted under this Agreement to download documents held by Cegid and to use the

information contained in the documents only internally, provided that:  (a) the copyright notice on the

documents remains on all copies of the document; material; (b) the use of these documents for personal

and non-commercial use unless it has been clearly defined by Cegid that certain specifications may be

used for commercial purposes; (c) documents will not be copied to networked computers or published on

any type of media unless expressly authorized by Cegid; and (d) no changes are made to these

documents.


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 – Company Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   STORES  .......................................................................................................................................................................................... 6

GetDetail

6

GetListDetail

7

3.   WAREHOUSES  ............................................................................................................................................................................ 9

GetDetail

9

GetListDetail

10

4.   TRIGGERS  .................................................................................................................................................................................. 11

GetListDetail

11

GetDetail

11

Create

12

Update

13

Evaluate

14

5.   STORESLISTS  .......................................................................................................................................................................... 15

Create

15

GetListDetail

15

GetDetail

16

Delete

16

6.   SUBSIDIARIES  .......................................................................................................................................................................... 17

GetListDetail

17

GetDetail

17

7.   STORES - USERDEFINEDTABLES  ................................................................................................................................ 19

GetValue

19

8.   OTHER  .......................................................................................................................................................................................... 20

Net Framework 4.8

20

Deployment

20


Cegid Retail Y2 – Company Plugin

4


### 1.   O BJECTIVES

The objective of the  Company  plugin is to provide services relating to the management of stores and

warehouses in a network of stores.

This service will be gradually enriched.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download

page:

"Documentation" is a link that provides access to the documentation list:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Company Plugin

5

➔   Exceptions

This part provides access to exceptions, classified by type, and according to the plugin.

➔   Installation

This page allows you to download Web Services installation and consumption documentation.


## Y2 versions

This plugin is compatible with the following versions of Cegid Retail Y2:

➔   Version 26

Note:

The # sign at the beginning of the plugin build number corresponds to the major version of Cegid Retail

Y2.


Cegid Retail Y2 – Company Plugin

6


### 2.   S TORES

Store are managed by Cegid Retail Y2 with a lot of information. A store record is populated through tabs:

➔   Contact information

➔   Information

➔   Additions

➔   Third-party

➔   Linked warehouses

➔   Accounting

➔   Store staff

➔   Miscellaneous

➔   User fields

➔   E-Commerce

➔   Replenishment

➔   Delivered/picked up

Or displays another entry form when you use the available option buttons:

➔   List of contacts

➔   Management of counters linked to the store

➔   Bank accounts

➔   Store settings store for portable inventory input terminals

All this information allows you to define the input environment for a user linked to the store by their user

record, or by the store specified in the header of the document being created.


## GetDetail


### ➔   Objectives

This method returns the detail of a store called by its unique identifier.

A part of the store data is returned by this method, with more or less information depending on the tags

present in the “Fields” property. This method will be progressively enriched.

The following business rules are applied:

➔   The "Id" property is mandatory. The search is performed on the exact value transmitted. In case of

unknown code, the reply contains empty information.

➔   The user provides the filtering through the user restrictions of their user record. If the store is not

authorized for the user,  the system returns “Store prohibited” reply.


### ➔   Improvements

Addition of the 4th address line

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

12/19/2022

A2351

144987

#3.15


Cegid Retail Y2 – Company Plugin

7

Checking the length of the internal identifiers provided.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

5/15/2023

165484

#3.142

Added Airport store

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EBU

1/16/2024

217887

#3.251

Further optimization of the search for linked stores and warehouses. The management of data collections

is reviewed in order to force the assessment of collections as soon as they are read in the database.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/6/2024

256820

#3.299

The service no longer raises an exception and now returns the value "Other" for the store type if it is not

initialized in the database.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

7/18/2024

279905

#3.315

Added the 2D-barcode template used in the store.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

8/26/2024

292067

#3.334

Added value “None” to the scope of the user restriction, which allows the user to obtain information about

the requested store even if it is forbidden to the user.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

9/2/2024

294321

#3.337

The WarehouseId property changes to Obsolete status, before disappearing in future releases.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

5/20/2025

1789036

392199

#3.445


## GetListDetail


### ➔   Objectives

This method recovers the store list of the folder based on the defined criteria.

The business rules are recovered from the  GetDetail  method.


Cegid Retail Y2 – Company Plugin

8


### ➔   Improvements

Addition of the 4th address line

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

12/19/2022

A2351

144987

#3.15

Increased the limit on the number of internal and external identifiers for stores from 200 to 1,000 and

improved the performance of warehouse searches.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EBU

1/15/2024

217391

#3.247

Added Airport store

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EBU

1/16/2024

217887

#3.251

Optimization of the search for stores, the query on linked warehouses (METABDEPOT table) is subject to

the presence of the "warehouses" value in the Fields field.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

4/26/2024

252660

#3.296

Further optimization of the search for linked stores and warehouses. The management of data collections

is reviewed in order to force the assessment of collections as soon as they are read in the database.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/6/2024

256820

#3.299

The service no longer raises an exception and now returns the value "Other" for the store type if it is not

initialized in the database.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

7/18/2024

279905

#3.315

Added the 2D-barcode template used in the store.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

8/26/2024

292067

#3.334

Added value “None” to the user restriction scope, enabling the user's default restriction to be applied.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

9/2/2024

294321

#3.337


Cegid Retail Y2 – Company Plugin

9


### 3.   W AREHOUSES

Cegid Retail Y2 always uses two entities:

➔   The store as a price management entity.

➔   The warehouse as an inventory management entity.

In case of a single warehouse folder, the creation of the store automatically the creation of the warehouse

that retrieves the store data. The warehouse will not be requested when making entries, even if it exists,

but it is systematically specified.

In this case, it is advisable to specify in the services the warehouse with the store code.

In a  multi-warehouse  folder context, warehouses are managed in Cegid Retail Y2 with a lot of

information. A warehouse record is populated through tabs:

➔   Contact information

➔   Information

The list of contacts of the warehouse in the repository can be filled in after calling an option with the

buttons.


## GetDetail


### ➔   Objectives

This method returns the detail of a warehouse called by its unique identifier.

A part of warehouse data is returned by this method, with more or less information depending on the

tags present in the “Fields” property. This method will be progressively enriched.

The following business rules are applied:

➔   The "Id" property is mandatory. The search is performed on the exact value transmitted. If the

code is unknown, the system returns a “Store unknown” reply.

➔   The user provides the filtering through the user restrictions of their user record (Inventory query.)

If warehouse is not authorized for the user,  the system returns a “warehouse prohibited” reply.

➔   If the “Closed” property is missing, all warehouses are returned.

➔   If the "CountryId" information is filled in, the search is performed on the exact value transmitted.

➔   The "TransferNoticesManagement" (GDE_SURSITEDISTANT) property can only be true (checked) if

the ET_SURSITEDISTANT field of the affiliated store is checked.

➔   The "GeographicalSite" (GDE_SITEGEO) property can only be filled in if the "RemoteSite"

(GDE_DEPOTDEPORTE) field of the warehouse is checked.

The Fields field is completed by a new tag  UserDefinedFields  used to return user-defined warehouse

information:

Collection (1 to 3) of user-defined amounts

Collection (1 to 3) of user-defined dates

Collection (1 to 20) of user-defined tables

Collection (1 to 3) of user-defined texts

Collection (1 to 3) of user-defined decisions.

Update of the method to search for the details of a warehouse using the external reference:


Cegid Retail Y2 – Company Plugin

10


### ➔   Improvements

Addition of the 4th address line

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

12/19/2022

A2351

144987

#3.15

Checking the length of the internal identifiers provided.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

5/15/2023

165484

#3.142


## GetListDetail


### ➔   Objectives

This method recovers the warehouse list of the folder based on the defined criteria.

The business rules are recovered from the  GetDetail  method. The Fields field is completed by a new tag

UserDefinedFields  used to return user-defined warehouse information:

Collection (1 to 3) of user-defined amounts

Collection (1 to 3) of user-defined dates

Collection (1 to 20) of user-defined tables

Collection (1 to 3) of user-defined texts

Collection (1 to 3) of user-defined decisions.

It is not possible to search simultaneously using both internal and external references. In this case, a

response "It is not possible to perform a search with both an internal identifier and an external identifier

of the warehouse is returned.


### ➔   Improvements

Addition of the 4th address line

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

12/19/2022

A2351

144987

#3.15

Increased the limit on the number of internal and external identifiers for warehouses from 200 to 1,000

and improved the performance.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EBU

1/15/2024

217391

#3.247


Cegid Retail Y2 – Company Plugin

11


### 4.   T RIGGERS

Modules such as loyalty, sales conditions, entry of user-defined tables, and payment methods

use filters based on entities such as stores, customers, items, suppliers or payment methods.

Example: Apply a sales condition to stores of type “Branches”. Triggers have been created for this purpose,

allowing to define filters that depend on the value of certain fields.

This service provides the GetListDetail, GetDetail, Create, Update, and Evaluate methods with SOAP and

RestFul compatibility.


## GetListDetail


### ➔   Objectives

Use this method to search for available store triggers based on the following search criteria:

•

Description of the trigger(s) to be returned

Optional (to recover, if necessary, all the triggers present in the database)

The search on this criterion uses the LIKE wildcard

•

Scope of use of the trigger

•

Fields: Filtering the requested information

•

Paging

With SOAP and RestFull compatibility

Dev

Date

CEGID’s

Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

11/14/2022

A2375

138100

#2.310


### ➔   Improvements

The method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352490

#3.387


## GetDetail


### ➔   Objectives

This method allows you to view settings of a store trigger, according to the following search  criteria:

•

Id: Identifier of the store trigger (required).

•

Fields: Filtering returned information

- System fields of the store list

- Details of the settings of the store trigger


Cegid Retail Y2 – Company Plugin

12

Dev

Date

CEGID’s

Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

11/14/2022

A2375

138100

#2.310


### ➔   Improvements

The  method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352490

#3.387


## Create


### ➔   Objectives

•

This method is used to create a new store trigger of type "Fields", "List of stores", or "Grouping":

•

You must provide a description, the scope(s) of use and the detail of the trigger, the content of

which depends on the type of trigger you want to create:

•

Creation of a trigger of type "List of stores"

➔ Comment on the trigger (Optional)

➔   Identifier of the user restriction category (Optional)

➔   Code of the store list (the store list must exist and a blocking check is performed)

•

Creation of a trigger of type "Fields"

➔ Comment on the trigger (Optional)

➔   Identifier of the user restriction category (Optional)

➔   Details about the fields:

Lines must be filled in progressively: a line can only be filled in if it is the first line or if the previous line is

filled in.

o

Exception in the case of line 4 which can only be filled in if the first line is filled in (and not line 3.)

o

A line is either empty or filled with the 3 pieces of information: Field / Field operator / Value.

o

If line 2, 3, 5 or 6 is filled in, the operator of the previous line must be specified.

--1-- --FIELD-- --OPE-- --VALUE-- --LINE OPE

--2-- --FIELD-- --OPE-- --VALUE-- --LINE OPE

--3-- --FIELD-- --OPE-- --VALUE-- --

-- LINE OPE

--4-- --FIELD-- --OPE-- --VALUE-- --LINE OPE

--5-- --FIELD-- --OPE-- --VALUE-- --LINE OPE

--6-- --FIELD-- --OPE-- --VALUE-- --


Cegid Retail Y2 – Company Plugin

13

OPE  (List of authorized operators):

Less  LessOrEqual Different Equal Greater GreaterOrEqual StartWith DontStartWith

IsBetween FinishesWith DoesnotFinishWith IsNotBetween IsIn IsNotIn Contains

DoesnotContain IsEmpty IsNotEmpty

Line OPE  (Authorized operators):

And Or

FIELD : Field existing in the store table (such as  ET_ABREGE, ET_VILLE …)

VALUE : Value of the store field (no control is performed on the values)

•

Creation of a trigger of type “Grouping”

➔ Comment on the trigger (Optional)

➔   Identifier of the user restriction category (Optional)

➔   Details about the groupings (inclusion and/or exclusion):

o

The selection and exclusion lines must be filled in progressively: a line can only be filled in, if it is

the first line or if the previous line is filled in.

o

The first line must be filled in.

o

If a grouping field is filled in, the value is mandatory.

o

The consistency of the values is not checked.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

12/14/2022

A2375

141520

# 3.23


### ➔   Improvements

The method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352490

#3.387


## Update


### ➔   Objectives

•

This method is used to update an existing store trigger of type "Fields", "List of stores", or

"Grouping":

•

You must fill in an existing Identifier for the trigger to be updated

•

The following information can be updated.

➔ Change of trigger description

➔ Change of the scope of use


Cegid Retail Y2 – Company Plugin

14

➔   Change the trigger setting details (change of the type and trigger settings)

•

Change of the trigger settings

➔ Update of trigger comment

➔   Update of the user restriction category identifier (Optional)

➔   Depending on the type of trigger type (List / Fields / Grouping) you want to update:

-

Update with a List of stores:

=>the store list must exist and a blocking check is performed

-

Update with Fields (proceeds by canceling/replacing the entire field block):

=> The lines must be filled in progressively: a line can only be filled in if the first line or

the previous line is filled in.

o

Exception in the case of line 4 which can only be filled in if the first line is filled in (and not

line 3.)

o

A line is either empty or filled with the 3 pieces of information: Field / Field operator /

Value.

o

If line 2, 3, 5 or 6 is filled in, the operator of the previous line must be specified.

-

Update with “Grouping” with inclusion and/or exclusion (proceeds by

canceling/replacing the entire field block):

-

=>The selection and exclusion lines must be filled in progressively:

A line

can only be filled in if it is the first line or if the previous line is filled in.

o

The first line must be filled in.

o

If a grouping field is filled in, the value is mandatory.

o

The consistency of the values is not checked.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

12/14/2022

A2375

141520

# 3.23


### ➔   Improvements

The method is now set to status Beta

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352490

#3.387


## Evaluate


### ➔   Objectives

This method evaluates whether a customer meets the conditions of the trigger.

Dev

Date

CEGID’s

Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

PCH

11/30/2021

A2277

94604

#2.87


Cegid Retail Y2 – Company Plugin

15


### 5.   S TORES L ISTS


### ➔   Improvements

The service is now set to the Released status


## Create


### ➔   Objectives

Store lists can be used in several features of Cegid Retail Y2. Thus, sales conditions can be based on

triggers using lists of stores.

This service is used to create a new list:

➔   Stores in the list can be entered by internal or external identifier of the store (external reference)

➔   The list must not exceed 100 occurrences.

(Lists are loaded into memory and should not be large)

A consistency and duplicate check in the list are performed.

➔   At the end of the registration, the number of stores in the list is returned.

➔   The Scopes property allows you to list the features that will be able to use it: Currently only the

“Triggers” scope is available

➔   The restriction category limits the users who use it.

➔   The creation of the list is logged to the event log.


### ➔   Improvements

The maximum number of stores in a list is increased from 100 to 1,000.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

7/9/2024

1550987

276515

3.312


## GetListDetail


### ➔   Objectives

This method allows you to search for lists of available stores, according to the following search criteria:

➔   Ids: Collection of store lists to return

➔   Description: Description of the list

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

151315

#3.53


Cegid Retail Y2 – Company Plugin

16

➔   Scope: Scope of use

➔   Restrictions: Identifier of the restriction category

➔   Fields: Filtering the requested information

➔   Scope of use

➔   Paging


## GetDetail


### ➔   Objectives

This method allows you to view the details of a store list, according to the following search criteria:

➔   Id: Identifier of the store list

➔   Fields: Filtering returned information

- System fields of the store list

- Detailed content of the store list


## Delete


### ➔   Objectives

This service is used to delete physically a list of stores  from the database, using its unique identifier.

The removal of the list is recorded in the event log.

Please note:

➔   There is no control over the use of the list. You should make sure before deleting the list that it

will not be used.

➔   This list can only be deleted by a user authorized by the restrictions.


Cegid Retail Y2 – Company Plugin

17


### 6.   S UBSIDIARIES


## GetListDetail


### ➔   Objectives

This method allows you to search for lists of available subsidiaries, according to the following search

criteria:

➔   Ids: Collection of the subsidiaries to return

➔   Fields: Filtering the requested information

-

SystemFields: To return the system fields updated by the server

-

Detail: To return additional information about the subsidiary

➔   Paging


### ➔   Improvements

Availability of this new service operation.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

1/31/2023

A2409

150676

# 3.42

The  method is now set to the Released status

The method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

7/30/2024

A2490

283537

#3.319


## GetDetail


### ➔   Objectives

This method allows you to view the detail of a subsidiary defined by its identifier:

➔   Id: Identifier of the subsidiary to be viewed.

➔   Fields: Filtering returned information

-

SystemFields: To return the system fields updated by the server

-

Detail: To return additional information about the subsidiary

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

202566

#3.227


Cegid Retail Y2 – Company Plugin

18


### ➔   Improvements

Availability of this new service operation.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

1/31/2023

A2409

150676

# 3:42

The method is now set to the Released status

The method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

7/30/2024

A2490

283537

#3.319

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/21/2023

A2478

202566

#3.227


Cegid Retail Y2 – Company Plugin

19


### 7.   S TORES  -   U SER D EFINED T ABLES


## GetValue


### ➔   Objectives

This method allows you to find the label of a code in a store user-defined table (tables from 1 to 20):

➔   Id: The code for which the label is to be returned

➔   TableId: Index of the user-defined table from 1 to 20


### ➔   Improvements

Availability of this new service operation.

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

PLA

12/16/2024

1667505

333848

#3.370


Cegid Retail Y2 – Company Plugin

20


### 8.   O THER


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

1/13/2025

1543349

341742

#3.382

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

190607

#3.209


