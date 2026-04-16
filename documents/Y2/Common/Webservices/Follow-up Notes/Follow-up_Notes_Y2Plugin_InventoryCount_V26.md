# Follow-up Notes Y2Plugin InventoryCount V26

*Source: Follow-up_Notes_Y2Plugin_InventoryCount_V26.pdf | Extracted: 2026-02-27*

---

Cegid Retail Y2 –  InventoryCount Plugin

1


## Follow-up Notes


## Make more


## possible


## InventoryCount Plugin V07


## Cegid Retail Y2 –  Version 26

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.png)


![Figure 2](./images/img_0002.jpeg)


![Figure 3](./images/img_0003.png)


Cegid Retail Y2 –  InventoryCount Plugin

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


Cegid Retail Y2 –  InventoryCount Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   COUNTINGMANAGEMENT  ................................................................................................................................................... 6

Create

6

3.   LISTMANAGEMENT  .................................................................................................................................................................. 8

GetList

8

GetDetail

8

4.   OTHER  ............................................................................................................................................................................................. 9

Net Framework 4.8

9


Cegid Retail Y2 –  InventoryCount Plugin

4


### 1.   O BJECTIVES

The  InventoryCount  plugin contains public and private services intended to manage the inventories.

Public services are described in the following chapters. Private services are intended for the operation of

the Cegid Retail Inventory Tracking mobile application, available on Android and IOS.

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


Cegid Retail Y2 –  InventoryCount Plugin

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


Cegid Retail Y2 –  InventoryCount Plugin

6


### 2.   C OUNTING M ANAGEMENT


## Create


### ➔   Objectives

The objective of this service is to create an inventory transmission following the counting of items in the

store. It is used for:

➔   Inventories of the store associated with an inventory list in Y2.

The list identifier is to be specified in the service.

➔   Inventories conducted in list.

The list identifier will be assigned by the service reply.

Note: this type of inventory cannot manage areas, as these are generated in Cegid Retail Y2.

If a list containing thousands of items is transmitted, the transmission can be returned as several calls:

•

Creation of a transmission with the first few thousand items and an indicator showing that the

transmission is partial.

•

Reminder from the service with the following thousands of items to be added to the existing

transmission.

•

The last call is indicated by specifying the "IsLastTransmissionData" property.

In the case of a single-warehouse folder, the store code (StoreId) should be copied into the warehouse

code (WarehouseId).

Recognition of the item

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

Added notification management after creating an inventory validation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/27/2023

A2419

150147

The Create method no longer throws an exception when the warehouse is closed.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

4/28/2023

736662

167017

#6.48


Cegid Retail Y2 –  InventoryCount Plugin

7

In the case of a search using a serial number specified in the "Reference" property (and only in this case),

this serial number is now stored in the GIN_CODEBARRE field of the TRANSINVLIG table, as it is in Y2

Core.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

8/3/2023

1206424

182891

#6.75

The size of the GIN_CODEBARRE column has been extended to 35 characters in 2021. The input in this

column was always limited to 18 characters, and has been revised to take account of this new size.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

8/24/2023

185581

#6.80

Added serial number to the Lines section of the method request.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

9/1/2023

1206427

186595

#6.85

Idempotency management to secure the integration of an inventory transmission.

To ensure this idempotency, the service consumer must now set the OperationUid property with a unique

GUID for each call of this operation.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RFO

11/9/2023

A2474

197732

#6.110

Warehouses sent by the InventoryCount plugin are now listed in priority order instead of alphabetical

order.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

FDE

4/19/2024

1462972

251151

#6.151


Cegid Retail Y2 –  InventoryCount Plugin

8


### 3.   L IST M ANAGEMENT


## GetList


### ➔   Objectives

The objective of this service is to return the active inventory lists not yet pre-validated in the store.

The properties of each list are transmitted, allowing you to know, for example:

➔   The date of conducting the inventory.

➔   If the inventory is complete. In this case, it is not necessary to retrieve the inventory lines that will

not be sent, since all the items in the store and in the warehouse are to be inventoried.

➔   If the inventory is partial, calling the GetDetail service allows you to load the items to be counted.

➔   The obligation to manage the inventory with areas.

Please note: in the case of an inventory managed with areas, only private services allow you to

retrieve the inventory areas and then reserve them for counting.

Note: incomplete inventory lists for which the counting has started are not returned. A partial inventory

should be managed as a single transmission.

It is possible to indicate the identifier of a list to retrieve the properties of this list.


### ➔   Improvements


## GetDetail


### ➔   Objectives

The GetList service returns the list(s) of items to be inventoried. If the inventory is partial (incomplete), this

GetDetail service allows you to load the list of items to be counted.

The "Paging" property provides protection against timeouts due to bulky inventories. We recommend that

it be used with a setting of a few hundred lines, supplemented by tests for dimensioning this value

according to the communication line.

Please note: the speed of data loading varies according to the device and its location.

The Web Service caller should check that not all information is returned in the first page. It should then

call the next page, until all lines are retrieved.


### ➔   Improvements


Cegid Retail Y2 –  InventoryCount Plugin

9


### 4.   O THER


## Net Framework 4.8

Following Microsoft‘s announcement about the “end of support for .NET Framework 4.5.2, 4.6 and 4.6.1 as

soon as April 26, 2022" the plugin now requires the installation of the .Net Framework 4.8 (runtime) on

server components.


