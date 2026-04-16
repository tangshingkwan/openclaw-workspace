# Follow-up Notes Y2Plugin Supplier V26

*Source: Follow-up_Notes_Y2Plugin_Supplier_V26.pdf | Extracted: 2026-02-27*

---


## Supplier Plugin V04


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date: January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Supplier Plugin

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


Cegid Retail Y2 – Supplier Plugin

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

GetDetail

6

GetListDetail

7

3.   OTHER  ............................................................................................................................................................................................. 9

Net Framework 4.8

9

Scope management

9


Cegid Retail Y2 – Supplier Plugin

4


### 1.   O BJECTIVES

The objective of the  Supplier  plugin is to provide services relating to the management of suppliers.

This service will be gradually enriched.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download

page:

"Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties.

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

➔   Exceptions


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Supplier Plugin

5

This part provides access to exceptions, classified by type, and according to the plugin.

➔   Installation

This page allows you to download Web Services installation and consumption documentation.


## Y2 versions

This plugin is compatible with the following version of Cegid Retail Y2:

➔   Version 26

Note:

The # sign at the beginning of the plugin build number corresponds to the major version of Cegid Retail

Y2.


Cegid Retail Y2 – Supplier Plugin

6


### 2.   M ANAGEMENT

Suppliers are managed by Cegid Retail Y2 with a lot of information. A supplier record is populated

through tabs:

➔   General

➔   Additions

➔   Payments

➔   Information

➔   User fields

The toolbar allows you to enter additional information:

➔   [Zoom Menu] button: Gives access to the commands Current documents, Ordered items,

Category price lists, Pricing, Website, Documents summary.

➔   [Complementary data] button: Gives access to exceptions, address management, referencing and

additional identifiers.

➔   [Contacts] button: Allows the registration of contacts with the supplier.

➔   [BAID] button: Allows the registration of the supplier's bank account details.

➔   [Memos] button: Allows you to associate photos or memos with the supplier's file.

➔   [Barcode] button : Allows you to enter specific barcode settings. This button is only visible if the

Distinct barcode per supplier option is activated in Administration > Company > Company

settings > Commercial management > Items.


## GetDetail


### ➔   Objectives

This method returns the detail of a supplier called by their identifier.

A part of supplier data is returned by this method, with more or less information depending on the tags

present in the “Fields” property. This method will be gradually enriched.

The following business rules are applied:

➔   The "Id" property is mandatory. The search is performed on the exact value transmitted. In case of

unknown code, the reply contains empty information

➔ The method has been enriched to return a grouping of supplier information according to the tags

indicated in the Fields property. You can select none or several elements  (SystemFields, Communication,

Detail, UserDefinedFields .)

-

If the Fields property is set to  SystemFields  the following information is returned:

Creation date, Last modification date, Last modification user and Creation user.

-

If the Fields property is set to  Communication , the following information is returned:

Collection of phone numbers, phone type, Website, etc.

-

If the Fields property is set to  Detail , the following information is returned:

Additional information about the supplier (short description, identification, characteristics, etc.)


Cegid Retail Y2 – Supplier Plugin

7

-

If the Fields property is set to  UserDefinedFields , the following information is returned:

Collection (1 to 3) of user-defined amounts

Collection (1 to 3) of user-defined dates

Collection (1 to 3) of user-defined tables


### ➔   Improvements

Addition of the 4th address line


## GetListDetail


### ➔   Objectives

This method recovers the supplier list of the folder based on the defined criteria.

The following business rules are applied:

➔   The description is not mandatory. If it is present, a “LIKE” is performed on this property.

➔   If the “Closed” property is missing, all suppliers meeting the other criteria are returned.

➔ The method has been enriched to return a grouping of supplier information according to the tags

indicated in the Fields property. You can select none or several elements  (SystemFields, Communication,

Detail, UserDefinedFields .)

-

If the Fields property is set to  SystemFields  the following information is returned:

Creation date, Last modification date, Last modification user and Creation user.

-

If the Fields property is set to  Communication , the following information is returned:

Collection of phone numbers, phone type, Website, etc.

-

If the Fields property is set to  Detail , the following information is returned:

Additional information about the supplier (short description, identification, characteristics, etc.)

-

If the Fields property is set to  UserDefinedFields , the following information is returned:

Collection (1 to 3) of user-defined amounts

Collection (1 to 3) of user-defined dates

Collection (1 to 3) of user-defined tables

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

AMO

3/30/2022

A2324

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/3/2022

A2351

138388

#3.5


Cegid Retail Y2 – Supplier Plugin

8


### ➔   Improvements

➔   Addition of the 4th address line

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

AMO

3/30/2022

A2324

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/3/2022

A2351

138388

#3.5


Cegid Retail Y2 – Supplier Plugin

9


### 3.   O THER


## Net Framework 4.8

Following Microsoft ‘s announcement about the “end of support for .NET Framework 4.5.2, 4.6 and 4.6.1 as

soon as April 26, 2022" the plugin now requires the installation of the .Net Framework 4.8 (runtime) on

server components.


## Scope management

From version 22.0.3.39, for any service call made with an authentication by ApiKey, the plugin now requires

the consumer of the service to position in the ApiKey the scope corresponding to the called method.

Service

Method

Scope

Management

GetDetail, GetListdDetail

suppliers:read

UserDefinedTables

GetLabels, GetValues, GetValue

suppliers-user-defined-tables:read

UpdateLabel, CreateOrUpdateValue

suppliers-user-defined-tables:write


## Swagger

Rest/Restful APIs grouped by plugin, with the option of selecting them by plugin name.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2025

1543349

345136

#3.222


