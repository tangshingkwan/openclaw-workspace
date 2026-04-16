# Follow-up Notes Y2Plugin TaxEngine V26

*Source: Follow-up_Notes_Y2Plugin_TaxEngine_V26.pdf | Extracted: 2026-02-27*

---


## TaxEngine Plugin V08


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date: January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – TaxEngine Plugin

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


Cegid Retail Y2 – TaxEngine Plugin

3


## Contents

Preamble  ........................................................................................................................................................................................... 2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation  ............................................................................................................................................................................... 4

Y2 versions  ...................................................................................................................................................................................... 5

2.   TAXENGINE ................................................................................................................................................................................... 6

GetTax  ............................................................................................................................................................................................... 6

CheckTaxes  ...................................................................................................................................................................................10

3.   TAXTYPES  .................................................................................................................................................................................. 11

GetDetail  .........................................................................................................................................................................................11

GetListDetail  ..................................................................................................................................................................................11

CreateOrUpdate  ...........................................................................................................................................................................11

4.   TAXSYSTEMS  ........................................................................................................................................................................... 13

GetDetail  .........................................................................................................................................................................................13

GetListDetail  ..................................................................................................................................................................................13

CreateOrUpdate  ...........................................................................................................................................................................14

Delete  ...............................................................................................................................................................................................14

5.   TAXCATEGORIES  ................................................................................................................................................................... 15

GetDetail  .........................................................................................................................................................................................15

GetListDetail  ..................................................................................................................................................................................15

CreateOrUpdate  ...........................................................................................................................................................................16

Delete  ...............................................................................................................................................................................................16

6.   OTHER  .......................................................................................................................................................................................... 17

Net Framework 4.8  .....................................................................................................................................................................17


Cegid Retail Y2 – TaxEngine Plugin

4


### 1.   O BJECTIVES

The  TaxEngine  plugin is used to manage the taxation of a receipt.

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

"Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties.

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

➔   Exceptions

This part provides access to exceptions, classified by type, and according to the plugin.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – TaxEngine Plugin

5

➔   Installation

This page allows you to download Web Services installation and consumption documentation.


## Y2 versions

This plugin is compatible with the following version of Cegid Retail Y2:

➔   Version 26

Note:

The # sign at the beginning of the plugin build number corresponds to the major version of Cegid Retail

Y2.


Cegid Retail Y2 – TaxEngine Plugin

6


### 2.   T AX E NGINE


## GetTax


### ➔   Objectives

Please note: this service uses internal services from Y2. It is heavily dependent on Core versions.


### ➔   Improvements


**Non-taxable items**

From now on, the GetTax method of the Tax service always returns a tax line with the tax information in

case the item is not taxable.


**External tax calculation connector**

The "TaxDetails[].Rank" and "TaxDetails[].SkuTaxSystem" properties in the query lines are used to indicate

which tax types of the item will be passed to the external tax calculation connector. If these types are not

present in the request, they are added by the service before calling the external connector.

Please note that these properties are not taken into account by the internal calculation of the GetTax

operation.


**Tax exception**

The "TaxExceptionId" property of the query lines is used to indicate the tax exception code that applies to

a line and causes the item tax types to be replaced with those defined for the tax exception.


**Taxation region and country**

The ISO codes for the taxation country and the Y2 code for the taxation region are now returned in the

details of the taxes applied to the document lines. The values returned depend on the settings of the tax

model and whether the goods are delivered or not.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

12/13/2021

688881

#5:15

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/29/2022

752915

A2343

#5.50

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/29/2022

752915

A2343

#5.50


Cegid Retail Y2 – TaxEngine Plugin

7

The following table shows how these fields are affected in the case of a sale.

Search for taxes in

the model

Over-the-counter sale

Sale for delivery

Taxation country

Taxation region

Taxation country

Taxation region

No regionalization

Country of the store

Not specified

Country of the

delivery address

Not specified

Zip code

Country of the store

Store zip code

Country of the

delivery address

Zip code of the

delivery address

Region

Country of the store

Region of the store

Country of the

delivery address

Region of the delivery

address

Tax system

Not specified

Tax system of the

store

Not specified

Tax system of the

store (*)

Store

Not specified

Store

Not specified

Store

(*) The behavior differs from the tax calculation of the Y2 Front Office and  Back-Office applications that

return the customer's tax system in the case of a delivery.


**Additional information for the external connector**

The "CustomerTaxExemptionReference" field is added to the query to pass the tax exemption reference

provided by the customer to the external tax calculation connector which may require this information for

legal reasons.

The "CustomsCode" field is added to the query lines to pass the customs code of the items to the

connector, which can use them to determine taxation rules for the items. If this field is missing or empty in

the query, the customs code available in the item record is passed to the external connector.

The "MovementReasonId" and "OriginalDocumentDate" fields are added to the query lines to pass the

return reason and the date of the original sale of the returned items to the external tax calculation

connector, which can use them to determine the tax rules to apply.

These fields are passed as is to the external tax calculation engine set up for the store of the document to

be taxed, but they are simply ignored if no external connector is set up.

If the customer’s tax system given by the "CustomerTaxSystem" field is missing or empty in the query, the

tax system used by the internal calculation is passed to the external connector.


**Administrative entity address**

The "AdministrativeCode" field is added to the query lines to transmit the address of the administrative

entity of a return line to the external tax calculation connector that may require this information for legal

reasons. This address can be the address of the store where the sale was made or the store where the

order was taken.

This field is passed as is to the external tax calculation engine set up for the store to which the document

to be taxed belongs, but it is simply ignored if no external connector is set up.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

5/9/2022

439676

#.5.67

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

5/11/2022

723975

A2348

#.5.73

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

6/24/2022

830035

A2348

#.5.86


Cegid Retail Y2 – TaxEngine Plugin

8


**External reference of the original sale**

The "OriginalDocumentExternalReference" field is added to the query lines to transmit the external

reference of the sales document header of a return line to the external tax calculation connector that may

require this information for legal reasons.

This field is passed as is to the external tax calculation engine set up for the store to which the document

to be taxed belongs, but it is simply ignored if no external connector is set up.


**Generating and sending a Setting:access apikey to authorized URLs**

If the URL specified in the taxConnector configuration starts with an allowed URL, an apikey of scope

settings:access is generated and cached, or retrieved from the cache for subsequent passes. Authorized

URLs are listed in the .cegidconfig file of the plugin.

The apikey is then sent to the taxConnector in the request header along with the tenantId and callback

URL.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

DLE

11/28/2022

800679

#5.140


**Additional amounts**

Taxes on the additional amounts of a document line given with the "ExtraAmounts" property are

calculated even if the net amount of the line is zero, for example for an item with 100% discount. In

addition, the tax rates applicable to the line are returned.


**Tax rates applicable to all tax systems**

If the tax rate search criterion set in the tax model is "tax system", you can create a tax rate that applies to

all tax systems with the code "...".

The tax calculation operation now searches for the rates defined for the tax system of the document. If no

rate exists, it searches for the rates defined for all tax systems.


**Subsidiary**

Corrected the error concerning the length of the SubsidiaryId field, which occurred when calculating taxes

for a sale to be delivered to a store in the USA that was not part of a subsidiary.


**Recording the transaction**

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

8/30/2022

862249

A2388

#5.105

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

11/27/2023

1250083

A2464

204824

#6.124

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

11/27/2023

1250083

A2464

204824

#6.124

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

12/15/2023

1250083

A2464

209724

#6.130


Cegid Retail Y2 – TaxEngine Plugin

9

The reply of the “GetTax” operation indicates whether the transaction should be recorded in the tax

system. This information is given by the external tax calculation connector.


**External tax calculation connector**

The result of the internal tax calculation is passed into the "InternalResult" property of the request sent to

the TaxConnector.


**Effective rate**

Change in the calculation algorithm of the reply.Lines[I].TaxRate property, for items with tax amount equal

to 0, the effective rate becomes the sum of the tax rates applying to the line.


**Setting ‘Calculating taxes by line’ or ‘by grouping’ is now taken into account**

TaxEngine now takes advantage of the Cegid Retail Y2 tax model setting, which allows tax to be calculated

by grouping or by line ('Tax model' record, 'Properties' tab, 'Calculating taxes by line'.) Depending on

'IsTaxIncluded', the 'Calculating taxes by line’ checkbox 'For tax excl. document' or 'For tax incl. document'

is taken into account. If 'by line' is ticked, taxes are calculated line by line. If not ticked, taxes are calculated

on the total of all lines, and any difference is distributed over the 2 lines with the highest amount.

Please note: If the tax model properties are not checked, the results may be different with this new version.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

7/4/2024

1266264

273828

#7.25


**Setting ‘Activation of US fiscal representations’ is now taken into account**

TaxEngine now takes advantage of the Cegid Retail Y2 tax model setting, which allows sales to be tax-

exempt if they are to be delivered to a US state in which the retailer does not have a fiscal representation,

i.e., a branch or subsidiary (Tax model record, Properties tab, ‘Activation of US fiscal representations’.)

Please note: If the tax model property is not checked, the results may be different with this new version.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

7/9/2024

1391824

276444

#7.28


**Tax system options taken into account when invoicing inclusive of tax**

TaxEngine now always takes into account the tax system setting of the document to determine whether

taxes apply. Previously, this setting only applied to documents invoiced exclusive of tax. Now it also applies

to documents invoiced inclusive of tax.

Please note: Unlike the old versions, if the tax systems are incorrectly set, so  that the taxes do not

apply , the result of the tax calculation can now be zero or different,  according to this setup .

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

4/22/2024

1465732

251872

#6.155

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

4/30/2024

1465732

254912

#6.158

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

5/6/2024

1470963

255109

#6.164


Cegid Retail Y2 – TaxEngine Plugin

10

It is now necessary to make the setup consistent so that the taxes must apply.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

10/9/2024

1579921

308624

#7.56


**External tax calculation connector**

Implementation of a RETY mechanism when the TaxEngine plugin calls an external tax engine, via a REST

http call, with 3 attempts made before raising an exception.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

10/21/2025

1970980

INC0261310

427344

#7.233


## CheckTaxes


### ➔   Objectives

Unexposed method, used to control the taxes of a cart of lines.

Added dependency on the Company plugin.


### ➔   Improvements

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

4/11/2022

706595

#.5.60


Cegid Retail Y2 – TaxEngine Plugin

11


### 3.   T AX T YPES


## GetDetail


### ➔   Objectives

This method returns a tax category from a tax model.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

8/11/2025

411746

#5.413


### ➔   Improvements


## GetListDetail


### ➔   Objectives

This method returns a list of tax categories classified by identifier for a tax model.

Paging is implemented.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

8/19/2025

412111

#7.158


### ➔   Improvements


## CreateOrUpdate


### ➔   Objectives

The aim of this method is to create or modify the tax categories of a tax model.

The tax model must exist.

The number of tax categories must correspond to the number of taxes in the tax model (1 or 2).

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

8/19/2025

412111

#7.158


Cegid Retail Y2 – TaxEngine Plugin

12


### ➔   Improvements


Cegid Retail Y2 – TaxEngine Plugin

13


### 4.   T AX S YSTEMS


## GetDetail


### ➔   Objectives

This operation displays the details of a tax system identified by its code ( TaxSystemId ).

It provides all the descriptive information associated with the tax system, including:

•

TaxModelId : Model identifier

•

TaxSystemId : Unique identifier for the tax system.

•

Description : Full label of the tax system.

•

ShortDescription : Abbreviated label of the tax system

•

Taxes : List of application indicators for the taxes making up the tax system

o

Rank : Tax number

o

isSubmitted : Indicates whether the tax is applicable.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

415788

#7.187


### ➔   Improvements


## GetListDetail


### ➔   Objectives

This operation allows you to  view the list of tax schemes .

It provides all the descriptive information associated with every tax system, with the option of filtering and

paging, including:

•

TaxModelId : Tax model identifier

•

TaxSystemId : Unique identifier for the tax system.

•

Description : Full name of the tax system.

•

ShortDescription : Abbreviated label of the tax system.

•

Taxes : List of application indicators for the taxes making up the tax system

o

Rank : Tax number

o

isSubmitted : Indicates whether the tax is applicable.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

415788

#7.187


Cegid Retail Y2 – TaxEngine Plugin

14


### ➔   Improvements


## CreateOrUpdate


### ➔   Objectives

This operation is used to create or modify a tax system identified by its code ( TaxSystemId ).

It provides and records all descriptive and structural information associated to the tax system, including:

•

TaxModelId : Tax model identifier

•

TaxSystemId : Unique identifier for the tax system.

•

Description : Full label of the tax system.

•

ShortDescription : Abbreviated label of the tax system.

•

Taxes : Collection of application indicators for the taxes making up the tax system

o

Rank : Tax number (1 or 2 depending on model).

o

isSubmitted : Indicates whether the tax is applicable.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

415788

#7.187


### ➔   Improvements


## Delete


### ➔   Objectives

This operation is used to  delete a tax system  identified by its code ( TaxSystemId ).

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

415788

#7.187


### ➔   Improvements


Cegid Retail Y2 – TaxEngine Plugin

15


### 5.   T AX C ATEGORIES


## GetDetail


### ➔   Objectives

This operation allows you to  view the details of a tax category  for a given tax level ( taxRank ).

It provides all the descriptive information associated to the category, including:

•

TaxRank : Tax number (1 or 2)

•

TaxCategoryId : Unique identifier for the tax category

•

Description : Full label of the tax category.

•

ShortDescription : Abbreviated label of the tax category

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

420024

#7.196


### ➔   Improvements


## GetListDetail


### ➔   Objectives

This operation allows you to  view the list of tax categories  for a given tax level ( taxRank ).

It provides all associated descriptive information for every category, including:

•

TaxRank : Tax number (1 or 2).

•

TaxCategoryId : Unique identifier for the tax category

•

Description : Full name of the tax category

•

ShortDescription : Abbreviated label of the tax category

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

8/19/2025

418488

#7.194


### ➔   Improvements


Cegid Retail Y2 – TaxEngine Plugin

16


## CreateOrUpdate


### ➔   Objectives

This operation allows you to  create or modify a tax category  for a given tax level ( taxRank ).

It provides and records all the descriptive information associated to the category, including:

•

TaxRank : Tax number (1 or 2)

•

TaxCategoryId : Unique identifier for the tax category

•

Description : Full label of the tax category.

•

ShortDescription : Abbreviated label of the tax category

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

420024

#7.196


### ➔   Improvements


## Delete


### ➔   Objectives

This operation allows you to  delete a tax category  for a given tax level ( taxRank ).

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

9/23/2025

420560

#


### ➔   Improvements


Cegid Retail Y2 – TaxEngine Plugin

17


### 6.   O THER


## Net Framework 4.8

Following Microsoft’s announcement about the “end of support for .NET Framework 4.5.2, 4.6 and 4.6.1 as

soon as April 26, 2022" the plugin now requires the installation of the .Net Framework 4.8 (runtime) on

server components.


## Swagger

Rest/Restful APIs grouped by plugin, with the option of selecting them by plugin name.

Dev

Date

CEGID's

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2025

1543349

345242

#7.78


