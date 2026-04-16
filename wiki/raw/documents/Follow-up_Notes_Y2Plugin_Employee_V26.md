# Follow-up Notes Y2Plugin Employee V26

*Source: Follow-up_Notes_Y2Plugin_Employee_V26.pdf | Extracted: 2026-02-27*

---


## Employee Plugin V04


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Employee Plugin

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


Cegid Retail Y2 – Employee Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   EMPLOYEE  .................................................................................................................................................................................... 6

SetPassword

6

3.   SALESPERSONS  ........................................................................................................................................................................ 7

GetDetail

7

GetListDetail

8

4.   SALESPERSONS2  .................................................................................................................................................................. 10

SetPassword

10

GetDetail

11

GetListDetail

12

Create

13

Update

14

5.   OTHER  .......................................................................................................................................................................................... 16

Net Framework 4.8

16


Cegid Retail Y2 – Employee Plugin

4


### 1.   O BJECTIVES

The objective of the  Employee  plugin is to provide services relating to the management of employees in a

network of stores such as salespeople, cashiers, representatives, storekeepers.

Login users are managed in another plugin: Identity

This service will be gradually enriched.

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


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Employee Plugin

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


Cegid Retail Y2 – Employee Plugin

6


### 2.   E MPLOYEE

Employees are managed by Cegid Retail Y2 with a lot of information.


## SetPassword


### ➔   Objectives

This method is used to define a new password for the employee. They will have to change it the next time

they log in.


### ➔   Improvements

The method is now set to the Released status.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

07/2024

A2490

283567

#3.287


Cegid Retail Y2 – Employee Plugin

7


### 3.   S ALES P ERSONS

Salespeople and Cashiers are managed by Cegid Retail Y2 with a lot of information. A Salesperson/Cashier

record is populated through tabs:

➔   Contact information

➔   User-defined information

➔   Contract data

➔   Notepads


### ➔   Improvements

The service is now set to the Obsolete status.

Method replaced by Salespersons2. It has the status Obsolete and will be removed from versions

generated after 2/1/2028.


## GetDetail


### ➔   Objectives

This method returns the detail of a salesperson/cashier called by their unique identifier.

A part of the salesperson/cashier data is returned by this method, with more or less information depending

on the tags present in the “Fields” property. This method will be gradually enriched.

The following business rules are applied:

➔   The "Id" property is mandatory. The search is performed on the exact value transmitted. In case of

unknown code, the reply contains empty information.


### ➔   Improvements

The method has been enriched to return a grouping of salesperson/cashier information according to the

tags indicated in the Fields property. You can select none or several elements  (SystemFields, Communication,

Detail, UserDefinedFields .)

-

If the Fields property is set to  SystemFields  the following information is returned:

Creation date, Last modification date, Last modification user and Creation user.

-

If the Fields property is set to  Communication , the following information is returned:

Email Address, Phone, and Main Address banner of the salesperson/cashier

-

If the Fields property is set to  Detail , the following information is returned:

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

PR 151370

#3.103


Cegid Retail Y2 – Employee Plugin

8

Additional information of the salesperson/cashier (Nickname, Commission percentage, Business

area, etc.)

-

If the Fields property is set to  UserDefinedFields , the following information is returned:

Collection (1 to 3) of user-defined amounts

Collection (1 to 3) of user-defined dates

Collection (1 to 10) of user-defined tables

Collection (1 to 3) of user-defined texts

Collection (1 to 3) of user-defined decisions.

The method has been enriched to return the attendance period of the salesperson/cashier in the store

(Contract start date and Contract end date).

The presence of this information is conditioned by the presence of the "Detail" property in the Fields

property.

Addition of the 4th address line


## GetListDetail


### ➔   Objectives

This method recovers the list of salespeople/cashiers of the folder based on the defined criteria.

The following business rules are applied:

➔   The "Roles" property allows you to set a filter. If this information is left blank, all salespeople and

cashiers are returned.

➔   If the "StoreId" information is filled in, the salespeople who work in this store or who are not

assigned to any store are returned (empty string). The reply will allow you to refine the information:

o

Store code in the reply: the employee is associated with this store by default.

o

Empty store information in the reply: the salesperson can work in all stores.

➔   If a "Date" property is present, the date must be prior (strict) to the deletion date of the salesperson.

➔   In the case where several criteria are present, they are combined.

Example: Role=Salesperson, StoreId=101 and Date=1/1/2021 – Request for the employee list of

type Salesperson assigned to store 101 by default and not deleted on 1/1/2021.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

3/9/2022

A2321

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

6/23/2022

A2367

823353

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138365

#3.7


Cegid Retail Y2 – Employee Plugin

9

If the code transmitted in the "Request" does not respect the other criteria, it is returned in the

reply with empty information.


### ➔   Improvements

➔   The method has been enriched to return a grouping of salesperson/cashier information according

to the tags indicated in the Fields property. You can select none or several elements  (SystemFields,

Communication, Detail, UserDefinedFields .)

-

If the Fields property is set to  SystemFields  the following information is returned:

Creation date, Last modification date, Last modification user and Creation user.

-

If the Fields property is set to  Communication , the following information is returned:

Email Address, Phone, and Main Address banner of the salesperson/cashier

-

If the Fields property is set to  Detail , the following information is returned:

Additional information of the salesperson/cashier (Nickname, Commission percentage, Business

area, etc.)

-

If the Fields property is set to  UserDefinedFields , the following information is returned:

Collection (1 to 3) of user-defined amounts

Collection (1 to 3) of user-defined dates

Collection (1 to 10) of user-defined tables

Collection (1 to 3) of user-defined texts

Collection (1 to 3) of user-defined decisions.

The method has been enriched to return the attendance period of the salesperson/cashier in the store

(Contract start date and Contract end date).

The presence of this information is conditioned by the presence of the "Detail" property in the Fields

property.

Addition of the 4th address line

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

3/9/2022

A2321

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

AMO

6/23/2022

A2367

823353

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138365

#3.7


Cegid Retail Y2 – Employee Plugin

10


### 4.   S ALESPERSONS 2

Salespeople and Cashiers are managed by Cegid Retail Y2 with a lot of information. A Salesperson/Cashier

record is populated through tabs:

➔   Contact information

➔   User-defined information

➔   Contract data

➔   Notepads


## SetPassword


### ➔   Objectives

This method initializes the password of a salesperson/cashier, who will have to change it the next time you

log in.

The following business rules are applied:

➔   The login user must be an administrator to use this method.

➔   The "Id" property is mandatory and must match an existing salesperson/cashier in the database.

➔   The "NewPassword" property is required and must follow the vendor password policy.


### ➔   Improvements

Added control over the access right “Initialization of passwords” (Tag 26780 – Concepts \ Commercial

management \ Management of the store staff)

The method is now set to the Released status

Fixed the connection saturation problem that occurred if the method was called many times.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/12/2025

1764975

390461

#3.421

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

LDE

12/12/2022

A2382

143525

#3.31

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

LDE

12/23/2022

A2382

145851

#3.59

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

PR 151370

#3.103


Cegid Retail Y2 – Employee Plugin

11


## GetDetail


### ➔   Objectives

This method returns the detail of a salesperson/cashier called by their unique identifier.

A part of the salesperson/cashier data is returned by this method, with more or less information depending

on the tags present in the “Fields” property. This method will be gradually enriched.

The following business rules are applied:

➔   The "Id" property is mandatory. The search is performed on the exact value transmitted. In case of

unknown code, the reply contains empty information.

➔   The operation is identical to that of the Salespersons service. The StoreId and CustomerID fields

have been replaced by Identifier sections where you can enter either the internal reference or the

external reference of the entity.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

PCH

12/8/2022

A2381

143205

#3.31


### ➔   Improvements

The method is now set to the Released status

No longer raise an exception when a sales representative has no customer assigned to them (GCL_TIERS

empty).

No longer raise an exception when a sales representative has no store assigned to them

(GCL_ETABLISSEMENT empty).

No longer raise an exception when a sales representative  has no calculation base document in section

Commission.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

6/20/2024

1523609

269188

#3.274

External references from the salesperson's secondary stores are returned.

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

151370

#3.103

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

09/ 11/2022

1230921

188137

#3.189

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

7/12/2024

1536167

277877

#3.281


Cegid Retail Y2 – Employee Plugin

12


## GetListDetail

This method recovers the list of salespeople/cashiers of the folder based on the defined criteria.

The following business rules are applied:

➔   The "Roles" property allows you to set a filter. If this information is left blank, all salespeople and

cashiers are returned.

➔   If the "StoreId" information is filled in, the salespeople who work in this store or who are not

assigned to any store are returned (empty string). The reply will allow you to refine the information:

o

Store code in the reply: the employee is associated with this store by default.

o

Empty store information in the reply: the salesperson can work in all stores.

➔   If a "Date" property is present, the date must be prior (strict) to the deletion date of the salesperson.

➔   In the case where several criteria are present, they are combined.

Example: Role=Salesperson, StoreId=101 and Date=1/1/2021 – Request for the employee list of

type Salesperson assigned to store 101 by default and not deleted on 1/1/2021.

➔   If the code transmitted in the "Request" does not respect the other criteria, it is returned in the

reply with empty information.

➔   The operation is identical to that of the Salespersons service. The StoreId field has been replaced

by an Identifier section where you can enter either the internal reference or the external reference

of the entity.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

PCH

12/8/2022

A2381

143205

#3.31

The method is now set to the Released status

No longer raise an exception when a sales representative has no store assigned to them

(GCL_ETABLISSEMENT empty).

No longer raise an exception when a sales representative  has no calculation base document in section

Commission.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

6/20/2024

1523609

269188

#3.274

External references from salespeople’s secondary stores are returned.

Taking into account ancillary stores when selecting salespeople/cashiers for a store listed in a request.

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

151370

#3.103

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

7/12/2024

1536167

277877

#3.281


Cegid Retail Y2 – Employee Plugin

13


## Create


### ➔   Objectives

This method is used to create new salesperson;/cashier

The following business rules are applied:

➔   The "Id" and "LastName" properties are mandatory. If code already exists, the response contains a

Boolean set to False.

➔   The stores entered (store and ancillary stores) must be in the list of stores authorized by the user’s

default restriction.

➔   The touchpad identifier must not be associated with another salesperson during the given period

in their usual store.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

PCH

12/14/2022

A2381

144251

#3.31


### ➔   Improvements

Removal of the test on the touchpad identifier

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

PCH

3/9/2023

1120433

PRB0119036

158499

#3.129

The method is now set to the Released status

Initialized the Salesperson and Cashier roles to False, as well as Commission Calculation mode to Sales if

this information is not passed in the query.

Other fields not exposed by the creation service are also initialized to default values.

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

237759

#3.250

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/30/2024

1602437

304582

#3.309

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

LDE

7/11/2023

A2452

179202

#3.171

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

EBU

1/19/2024

1371195

218835

#3.237


Cegid Retail Y2 – Employee Plugin

14

External references from the main store and secondary stores are taken into account to create the

salesperson.


## Update


### ➔   Objectives

This method is used to change an existing salesperson/cashier

The following business rules are applied:

➔   The "Id" and "LastName" properties are mandatory. If code already exists, the response contains a

Boolean set to False.

➔   The stores entered (store and ancillary stores) must be in the list of stores authorized by the user’s

default restriction.

➔   The touchpad identifier must not be associated with another salesperson during the given period

in their usual store.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

PCH

12/19/2022

A2381

144708

#3.93


### ➔   Improvements

The  method is now set to the Released status

No change of the Salesperson and Cashier roles if no information is passed in the query.

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

237759

#3.250

Possibility of updating a salesperson’s main establishment and secondary stores with the external

reference.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

7/12/2024

1536167

277877

#3.281

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

LDE

7/11/2023

A2452

179202

#3.171

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

EBU

1/19/2024

1371195

218835

#3.237


Cegid Retail Y2 – Employee Plugin

15

Possibility of updating a salesperson to blank out one  of the address lines.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

7/12/2024

1536167

277877

#3.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

7/15/2024

1431032

278666

#3.284


Cegid Retail Y2 – Employee Plugin

16


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

342751

#3.341


