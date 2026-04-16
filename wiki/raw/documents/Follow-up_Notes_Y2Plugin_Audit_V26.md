# Follow-up Notes Y2Plugin Audit V26

*Source: Follow-up_Notes_Y2Plugin_Audit_V26.pdf | Extracted: 2026-02-27*

---


## Audit Plugin V04


## Cegid Retail Y2 –  Versions 26


## Follow-up Notes

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Audit Plugin

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


Cegid Retail Y2 – Audit Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   USAGE  ............................................................................................................................................................................................. 6

GetStores

6

GetUsers

6

GetPosFrontOffice

7

GetInventoryTracking

7

GetMpos

8

GetCountryPackages

8

GetCustomOrders

9

3.   TIMEMEASUREMENTS  ........................................................................................................................................................ 10

GenerateFiles

10

4.   OTHER  .......................................................................................................................................................................................... 11

Net Framework 4.8

11


Cegid Retail Y2 – Audit Plugin

4


### 1.   O BJECTIVES

The objective of the Audit plugin is to provide services relating to the management of settings common to

several other plugins.

This service will be gradually enriched.

Just remind: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

“Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties.

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Audit Plugin

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


Cegid Retail Y2 – Audit Plugin

6


### 2.   USAGE


## GetStores


### ➔   Objectives

This method returns the audit of use for the concerned stores during the analysis period.

At least 2 sections are returned:

-

Counters: General counters specifying the stores in the database as well as those active within the

period

-

Countries: Counters of stores by country, with the notion of Country Package

Using the Detail property allows you to get details per store

The following business rules are applied:

➔   The stores are filtered according to the default user restrictions.

➔   The analysis period must not exceed 3 years.


### ➔   Improvements


## GetUsers


### ➔   Objectives

This method returns the audit of use during the analysis period.

The Counters section is systematically returned. It contains the general counters specifying the users in the

database as well as those connected within the period.

A license is counted for any user who connects to a  Back Office or a Front Office that does not collect

during the period.

Using the Detail property allows you to get details per user.

The following business rules are applied:

➔   The analysis period must not exceed 3 years.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135


Cegid Retail Y2 – Audit Plugin

7


### ➔   Improvements

Fixed crashes when executing the query to retrieve cash registers with open days, when the number of

cash registers exceeds 2,100.


## GetPosFrontOffice


### ➔   Objectives

This method returns the audit of Inventory Front Office POS during the analysis period.

At least 2 sections are returned:

-

Counters: General counters specifying the Front Office POS in the database as well as those active

within the period

-

Countries: Counters of active Front Office POS per country

Using the Detail property allows you to get details per Front Office POS.

The following business rules are applied:

➔   The analysis period must not exceed 3 years.


### ➔   Improvements

Fixed to take into account only POS-type registers or those that do not exist in the PARCAISSE table (in the

case of deleted registers) when counting active POS registers.


## GetInventoryTracking


### ➔   Objectives

This method returns the audit of Inventory Tracking devices during the analysis period.

At least 2 sections are returned:

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/12/2024

Bug 1568130

298446

#3.187

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

6/11/2024

Bug 1523243

266229

#3.167


Cegid Retail Y2 – Audit Plugin

8

-

Counters: General counters specifying the Inventory Tracking devices in the database as well as

those active within the period

-

Countries: Counters of Inventory Tracking devices per country.

The following business rules are applied:

➔   The analysis period must not exceed 3 years.


### ➔   Improvements


## GetMpos


### ➔   Objectives

This method returns the audit of Inventory Tracking devices during the analysis period.

At least 2 sections are returned:

-

Counters: General counters specifying the Mpos devices in the database as well as those active

within the period

-

Countries: Counters of Mpos devices per country.

The following business rules are applied:

➔   The analysis period must not exceed 3 years.


### ➔   Improvements


## GetCountryPackages


### ➔   Objectives

This method returns the audit of Country Packages.


### ➔   Improvements

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135


Cegid Retail Y2 – Audit Plugin

9


## GetCustomOrders


### ➔   Objectives

This method returns the counters of e-commerce orders and non-e-commerce store orders/reservations

grouped by month/year, during an analysis period.

The following business rules are applied:

➔   The stores are filtered according to the default user restrictions.

➔   The analysis period must not exceed 3 years.


### ➔   Improvements

In the E-commerce module detail, the store count was incorrect. Reservations from an e-commerce order

were mistakenly matched.

The e-commerce order counter is not affected by the anomaly and was correct.

In the E-commerce module detail, the store count was incorrect. Store orders resulting from e-commerce

orders delivered to the customer's premises used to be erroneously accounted for.

From now on, only e-commerce orders with an “e-commerce” store will be considered.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

March 2022

A2135

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

1/20/2025

1686911

346139

#3.218

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull Request

Plugin Build no.

Quality Ctrl

LDE

3/17/2025

1735694

372135

#3.289


Cegid Retail Y2 – Audit Plugin

10


### 3.   TIMEMEASUREMENTS


## GenerateFiles


### ➔   Objectives

This methods enables the generation of export files for time measurements.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RFO

June 2023

A

172357


### ➔   Improvements

The  method is now set to Released

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

July 2027

A2490

1565857

283516

3.177


Cegid Retail Y2 – Audit Plugin

11


### 4.   O THER


## Net Framework 4.8

Following Microsoft‘s announcement about the “end of support for .NET Framework 4.5.2, 4.6 and 4.6.1 as

soon as April 26, 2022" the plugin now requires the installation of the .Net Framework 4.8 (runtime) on

server components.


## Deployment

Added installation kit for TaskSchedulerService.

Dev

Date

CEGID’s Ref.   Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

10/10/2023

1167931

194211

#3.79


## Swagger

Rest/Restful APIs grouped by plugin, with the option of selecting them by plugin name.

Dev

Date

CEGID’s Ref.   Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/10/2025

1543349

341709

#3.214


