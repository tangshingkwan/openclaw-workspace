# Follow-up Notes Y2Plugin SalesConditions V26

*Source: Follow-up_Notes_Y2Plugin_SalesConditions_V26.pdf | Extracted: 2026-02-27*

---


## Plugin Sales Conditions V06


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   20 February 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – SalesConditions Plugin

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


Cegid Retail Y2 – SalesConditions Plugin

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

Create

6

GetDetail

7

Update

7

Delete

7

GetListDetail

7

3.   ENGINE ............................................................................................................................................................................................ 9

Evaluate

9

4.   OTHER  .......................................................................................................................................................................................... 12

Net Framework 4.8

12


Cegid Retail Y2 – SalesConditions Plugin

4


### 1.   O BJECTIVES

The objective of the  SalesConditions  plugin is to offer services relating to the management of sales

conditions. It allows:

➔   Their management: consultation, creation, modification and deletion.

➔   Running the engine for a list of items to return those that are applied, or applicable.

Just remind: Only public methods for which the contract is published can be used by applications not

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


Cegid Retail Y2 – SalesConditions Plugin

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


Cegid Retail Y2 – SalesConditions Plugin

6


### 2.   M ANAGEMENT


## Create


### ➔   Objectives

The contract to create the sales conditions allows you to specify numerous properties that may be

incompatible.

In interactive creation in Cegid Retail Y2, some options affect the display and options.

For example, in managing sales conditions:

   The unchecked "condition on items" option does not allow you to specify a trigger or a grouping

of items.

   If the "" option is checked, it is possible to enter a trigger and also to select the grouping

management option. If this last option is specified, other options may be entered.

The choice of a sales condition benefit is also closely linked to the properties to be specified.

Before creating a new sales condition by Web Service, we recommend that you check that the properties

specified in the contract are compatible with an interactive entry.

This method will avoid many setbacks.

Check

This method starts with a checking phase that verifies the integrity of the information. In the event of a

problem, an error code is sent to the user, otherwise the sales condition is created, subject to having the

rights for it under the user restrictions.

Constraints

The creation of a sales condition sometimes requires you to specify information present in the database:

   Item, customer, store triggers

   Item list

   Markdown reasons

   etc.

This information should be known by the Web Service.

If a sales condition is created with a new trigger (the code of which is a GUID), the external system must

send an existing code. The trigger must therefore be created in Cegid Retail Y2 before the Web Service is

called to create the sales condition.


### ➔   Improvements

Disabled the "In the receipt sequence" option in the case of grouping or  "X for Y” benefit.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

11/15/2023

1313761


Cegid Retail Y2 – SalesConditions Plugin

7


## GetDetail


### ➔   Objectives

The objective of this method is to retrieve the configuration details of a business operation, subject to

having the rights (user restrictions).


## Update


### ➔   Objectives

The objective of this method is to change an existing sales condition, subject to having the rights (user

restrictions).

The checking phase verifies the integrity of the information transmitted with that of the sales condition. In

particular, "Close" can be used as information to close a sales condition.

This update can be carried out in two ways:

   Return all information on the sales condition, which ensures better consistency of data across the

information.

   Only return amended information, with the risk of generating an inconsistent sales condition if it

has been changed in the meantime in Cegid Retail Y2.

Note: this partial change remains relevant in the event of "closure", change in the period, etc.


### ➔   Improvements


## Delete


### ➔   Objectives

The objective of this method is to remove an existing sales condition subject to having the rights (user

restrictions).


## GetListDetail


### ➔   Objectives

This method has the following objectives:

   To be able to detect if a store does not manage any sales condition, in order to avoid calling the

service in a checkout software.

   To be able to detect if a keyword corresponds to a sales condition available in the store, which

makes it possible to inform the user (and the customer) in the event of rejection (expired date,

unauthorized store, etc.)

   Be able to list the sales conditions in a given environment, to inform the user (and the customer).


Cegid Retail Y2 – SalesConditions Plugin

8

Examples:

o

List of the week’s new promotions

o

List of promotions available for a customer

o

List of the store's promotions

Business rules

   The sales conditions respecting the input criteria are returned if you have the appropriate rights

(user restrictions.)

If the information ID (code of the sales condition) is specified, the search is made on the exact

value transmitted. If the code is unknown, it is returned in the reply with empty information.


### ➔   Improvements


Cegid Retail Y2 – SalesConditions Plugin

9


### 3.   E NGINE


## Evaluate


### ➔   Objectives

The objective of this method is to run the sales conditions engine on a list of items in order to return the

conditions that are applied, or applicable.

It allows the generation of sales conditions to be reproduced in entering Cegid Retail Y2 cash collection,

with the same engine being used.


### ➔   Improvements

For quantities with decimals (less than 1), the sales condition with maximization (on net or base price) is

triggered. We avoid considering the prorated price calculation as a discount, so that the maximization

calculation no longer considers the price recalculation as a discount, and the sales condition can be

triggered.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

FDE

11/20/2023

1310351

PRB0134328

202955

#5:11 AM

When recalculating sales conditions after entering the payment method, sales conditions other than gift

certificates are no longer excluded.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

FDE

1/5/2024

1352290

PRB0136342

214824

#5:34 AM

Correction made to take into account in the store trigger the exact value of the user-defined table

(example 25) and of the user-defined store table (example 5). 5 was contained in 25, but that's not what

we want.

Fixed cases: Is in, is not in

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

FDE

2/12/2024

1040574

PRB0137712

226014

#5:55 AM

The receipt discount distribution was not correct for a receipt with 2 lines. The 1st line was made up of

more than a quantity on which part of the quantities were discounted through a same condition. A

second sales condition applies to both lines, but the order of the discounts did not respect the order of

the lines and caused a poor distribution of the receipt discount. Problem fixed.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

FDE

3/5/2024

1419489

INC0129521

234739

#5.63


Cegid Retail Y2 – SalesConditions Plugin

10

Due to a rounding problem when splitting the lines, and recalculating sales conditions, after the deletion

of one of the conditions, the first lines were no longer discounted. Problem fixed.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

3/8/2024

1422759

INC0130393

235972

#5.67

The incentive message is no longer displayed if a sales condition is not triggered.

In a multi-level context, the number of missing items in the incentive message was wrong. Problem fixed.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

5/17/2024

1485931

INC0182836

259301

#5.115

Correction in the case of groupings where the second condition took into account the item discounted by

the 1st condition, instead of the non-discounted item.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

9/13/2024

1552212

INC0189005

298661

295665

298677

#5.158

To sort conditions of the same level, if the priority is the same, conditions are sorted from the discounted

amount of the previous levels and no longer from the discounted amount of the sales condition alone.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

9/20/2024

1552212

INC0189005

300867

#5.168

Correction to take into account all receipt lines meeting the criteria of the business condition for the latter

to apply.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

1/22/2025

1688671

INC0208511

347479

#5.206

In a receipt, for 1 line of 3, the number of items meeting the condition (i.e,the 3) is searched for. As the

condition is defined by range, this number of items is used to find the number of loyalty points to be

applied. With patch 1688671, the number of items meeting the condition was incorrect if there were

several ranges. Problem fixed.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

4/15/2025

1758551

INC0218559

387353

391191

#5.242

In a shopping cart containing items eligible for a sales condition of type XforY, the addition of an item

which, although eligible for the condition, does not belong to the same membership criterion, and no

longer prevents the sales condition from being triggered for the other items meeting this criterion.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl


Cegid Retail Y2 – SalesConditions Plugin

11

FDE

9/24/2025

1961011

INC0256495

421408

#5.276

(ManagementService) – We now use the StoreId passed as a parameter to list the sales conditions

associated with the store passed as a parameter.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.   Quality Ctrl

FDE

12/5/2025

2015196

INC0270534

440777

#5.303


Cegid Retail Y2 – SalesConditions Plugin

12


### 4.   O THER


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

1/15/2025

1543349

344293

#5.203


