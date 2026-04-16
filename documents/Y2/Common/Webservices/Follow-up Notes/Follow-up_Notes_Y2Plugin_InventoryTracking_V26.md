# Follow-up Notes Y2Plugin InventoryTracking V26

*Source: Follow-up_Notes_Y2Plugin_InventoryTracking_V26.pdf | Extracted: 2026-02-27*

---


## InventoryTracking Plugin V07


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   January 21, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – InventoryTracking Plugin

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


Cegid Retail Y2 – InventoryTracking Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 5

Documentation

5

Y2 versions

6

2.   INVENTORYTRACKINGDASHBOARD  ............................................................................................................................. 7

GetDetail

7

GetDetailV2

7

3.   INVENTORYTRACKINGDEVICE  ......................................................................................................................................... 9

Connect

9

Create

13

Reassign

17

GetDetail

20

Disconnect

20

4.   INVENTORYTRACKINGITEMSEARCHCACHE  ......................................................................................................... 21

GetItemsReferential

21

GetListByReference

21

GetModifiedItemsSinceDate

22

5.   INVENTORYTRACKINGGLOBALSETTINGS  .............................................................................................................. 23

CreateOrUpdate

23

Delete

23

GetDetail

23

6.   INVENTORYTRACKINGMOBILESETTINGS  ............................................................................................................... 25

CreateDevice, UpdateDevice, UpdateDeviceOnConnect, GetDetailDevice

25

GetListDisplayProperties

26

CreateModel, UpdateModel, GetDetailModel

26

GetListDevice

27

7.   INVENTORYTRACKINGUSERLOG  ................................................................................................................................. 28

UserLoginNotification

28

UserLogoutNotification

28

8.   INVENTORYTRACKINGUSERRIGHTS  ......................................................................................................................... 29

GetList

29

9.   OTHER  .......................................................................................................................................................................................... 30


Cegid Retail Y2 – InventoryTracking Plugin

4

Net Framework 4.8

30


Cegid Retail Y2 – InventoryTracking Plugin

5


### 1.   O BJECTIVES

The  InventoryTracking  plugin contains private (non-public) services for the operation of the Cegid Retail

Inventory Tracking mobile application, available for Android and IOS.

It includes the necessary services:

➔   For connecting and creating devices.

➔   For the display of the dashboard.

➔   For loading the various caches that will be used in online and standalone mode

Reminder: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

"Documentation" is a link that provides access to the documentation list:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties


![Figure 4](./images/img_0004.jpeg)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – InventoryTracking Plugin

6

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

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


Cegid Retail Y2 – InventoryTracking Plugin

7


### 2.   I NVENTORY T RACKING D ASH B OARD


## GetDetail

Filtering of transfer notices and delivery notices awaiting approval.

It has the status Deprecated and will be removed from versions generated after 2/1/2028.

It is replaced by GetDetailV2

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/22/2025

1689722

347327

#6.72


## GetDetailV2

New method for changing the dashboard of the mobile application to show the indicators associated with

the new flows managed. The indicators that can be consulted to find out if there are actions to be

performed:

o

Inventory lists to be processed

o

Reservation requests to be validated

o

Delivery or transfer notices to be received

o

Transfer requests to be validated

o

Customer orders to be prepared

o

Customer orders managed at pick-up point to be received or handed over to the customer

Filtering of transfer notices and delivery notices awaiting approval.

Fixed the counter calculation for Web orders to be delivered by the stores, as the counter was always set to

0.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/15/2021

612463

78337

#3.312

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

5/3/2021

559031

69636

#3.139

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/15/2021

612463

78337

#3.312

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

10/6/2021

623776

87497

#3.377


Cegid Retail Y2 – InventoryTracking Plugin

8

Fixed the counter calculation for Web orders to be delivered by the stores, as the counter was counting the

store orders that were not to be delivered.

The counter for Web orders to be delivered only takes into account the orders in status “Requested in store”

or “Shipped” so that orders partially prepared in Front office are not processed in Inventory Tracking.

Added the counter of the preparations to be delivered.

Orders in preparation are taken into account in the calculation of the CustomerOrdersToBeDeliveredByStore

indicator.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

10/21/2021

660498

89599

#3.388

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/15/2021

671660

92256

#3.422

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

137938

139035

#4.140

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

2/15/2023

1102487

154326

#4.220


Cegid Retail Y2 – InventoryTracking Plugin

9


### 3.   I NVENTORY T RACKING D EVICE


## Connect

New access rights: at "TagID" level, addition of possible returned values:

•

120306: Inputs - Creation of an exceptional input

•

120404: Outputs - Creation of a supplier return

•

120405: Outputs - Creation of a special output

•

120601: Web orders- Web order management

•

120701: Pick-up points - Management of pick-up points

Addition of the store's currency and the number of decimal places of the currency in the reply (Currency

section.)

Addition of information related to the following properties in the reply:

•

Reason for movement,

•

User-defined document tables.

Addition of a new display property for the flow of orders to be delivered in order to view on the mobile

device the customer’s delivery address.

The setup of the user-defined tables for orders delivered to pick-up points is now the one defined at the

level of customer orders and not at customer delivery level.

The default value of the user-defined tables was incorrect in the settings sent to the mobile device

(concatenation of table identifier and its value.) Problem fixed. Only the value is sent now.

Correction made to be able to manage user restrictions when they are defined at the level of store user-

defined fields higher than 10.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2021

4/12/2021

A2180

67049

67429

?

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/12/2021

A2180

67381

#3.84

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

4/29/2021

A2180

69552

#3.132

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/6/2021

A2239

83470

#3.355

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

10/19/2021

655873

89067

#3.386

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/16/2021

673849

92530

#3.432

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

1/6/2022

696375

99054

#4.36


Cegid Retail Y2 – InventoryTracking Plugin

10

Addition of the Scandit key (ScanditLicenceKey property) for the Pilot version.

New access right at "TagID" level, addition of the following value:

•

120107: Generic > Manage scan lists

New access right at "TagID" level, addition of the following values:

•

120108: Generic > Modify internal references upon generation

•

120109: Generic > Modify external references upon generation

•

120110: Generic > Modify follow-up references upon generation

Addition of the delivery preparation management

New access right at "TagID" level, addition of the following value:

•

120801: Transfer request - Create a transfer request

+ addition of the flow of transfer request creation taking into account user restrictions on stores issuing

transfer requests

Increase in the number of days for searching documents (365 instead of a maximum of 30, with a minimum

of 1 day.)

Added the DatabaseManagement property, indicating the recovery mode of the item database.

Add the DisplayPicture property, indicating the display or not of the item pictures when entering

documents.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

3/8/2022

A2328

107853

#4.40

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2022

A2306

112745

#4.???

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

10/10/2022

A2334

134923

#4.107

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

137082

137826

137305

#4.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/22/2022

A2336

139872

140466

141008

#4.167

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

2/24/2023

A2428

155952

#4.230

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2429

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2430

159600

#4.281


Cegid Retail Y2 – InventoryTracking Plugin

11

Added the ScanLibrary section, indicating the scan libraries used in released and  pilot versions for mobile

devices under iOS.

Updated

the

ScanditLicenceKey

and

ScanditLicenceKeyPilote

properties

in

the

MobileUseSetting/MobileSettingDevice/Properties section of the reply, with the values returned by the

GetDetail method of the GlobalSettings service .

The DatabaseManagement, DisplayPicture and ScanLibrary properties are made optional to resolve

compatibility issues with older versions of the service.

Addition of the following properties to the GlobalSettings sub-section of the reply:

•

ScansList

•

MultipleOfQuantityManagement (for each document type)

The WorkerProcessVersion property becomes obsolete and is now an empty string.

Added configuration for software extensions

New access right 1202026: Conduct inventory - Custom inventory:  Zero quantity allowed

Addition of the following properties to the GlobalSettings sub-section of the reply:

-

BillOfMaterials/Assembly: Indicates that BOMs are managed in the local cache

-

ItemTypes (for each document type): Indicates the types of items managed in the cache and allowed

for each flow when scanning or entering items on the mobile device.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2431

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

5/23/2023

1169114

170306

#5.37

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

5/24/2023

1170194

170514

#5.42

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/16/2023

A2456

1170194

174790

174846

#5.66

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/11/2023

1199190

178829

#5.89

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

1/4/2024

A2479

209801

211308

211501

214322

#5.194

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

2/8/2024

A2475

225465

#5.205

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/11/2024

A2492

1447515

248021

#5.241


Cegid Retail Y2 – InventoryTracking Plugin

12

Addition, in reply, of the InventoryCount section and the SerialNumberManagement property, indicating

whether serial numbers are managed in inventory counts.

In SaaS environments, the URL of the extension access service transmitted through Connect was not directly

usable by the mobile device, as the SaaS configuration files gave the URL of the azure function and not the

URL of the access service. Problem fixed.

New access right 120111: “Inventory query - Other stores"

Added settings for printing labels on request, from a scan list and from a document:

-

Added the following properties to the GlobalSettings sub-section of the reply:

o

LabelTemplates: List of Y2 item label printing templates

o

LabelsManagement: Indicates the printing mode and the label template to be used for

printing labels from the scan lists (data from the company settings “Label printing mode”

and “Label printing template” in Commercial Management > Documents – entry)

-

Added the PriceListTypeId property in the Prices sub-section of the reply, indicating the price list

type

-

Added the LabelPrintingMode property to the DocumentSetting sub-section of each flow (except

PickUpPointsSetting), indicating how labels are printed

-

Added the LabelTemplateId property to the Document sub-section of each flow, indicating the

template to be used

New access right 120112: "Managing comments in documents"

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/4/2025

1947110

416594

#6.131

New access right 120113: "Duplicating a list of scans from history"

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/8/2025

1947744

416723

#6.133

In the section listing the sender stores for transfer requests, the  <Warehouses>   collection is now published,

even in the case of a single warehouse when its identifier is different from the store code.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

9/22/2025

1959709

INC0255854

420116/ 420488

#6.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/30/2024

A2494

261269

#5.301

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

6/18/2024

A2479

268788

#5.319

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/12/2024

A2503

298279

#5.336

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/5/2024

A2500

310967

313528

312315

318262

#6.38


Cegid Retail Y2 – InventoryTracking Plugin

13

The access rights for duplicating a scan list and managing comments in documents are now only available

in versions 6.0 and above of InventoryTracking.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

1/9/2026

1947744

1947110

446291

#7.13


## Create

New access rights: at "TagID" level, addition of possible returned values:

•

120306: Inputs – Create a special input

•

120404: Outputs – Create a supplier return

•

120405: Outputs – Create a special output

•

120601: Web orders – Manage Web orders

•

120701: Pick-up points – Manage pick-up points

Addition of the store's currency and the number of decimal places of the currency in the reply (Currency

section.)

Addition of information related to the following properties in the reply:

•

Reason for movement,

•

User-defined document tables.

Addition of a new display property for the flow of orders to be delivered in order to view on the mobile

device the customer’s delivery address.

The setup of the user-defined tables for orders delivered to pick-up points is now the one defined at the

level of customer orders and not at customer delivery level.

The default value of the user-defined tables was incorrect in the settings sent to the mobile device

(concatenation of table identifier and its value.) Problem fixed. Only the value is sent now.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2021

4/12/2021

A2180

67049

67429

?

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/12/2021

A2180

67381

#3.84

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

4/29/2021

A2180

69552

#3.132

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HAD

9/6/2021

A2239

83470

#3.355

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

10/19/2021

655873

89067

#3.386

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

11/16/2021

673849

92530

#3.432


Cegid Retail Y2 – InventoryTracking Plugin

14

Correction made to be able to manage user restrictions when they are defined at the level of store user-

defined fields higher than 10.

Addition of the Scandit key (ScanditLicenceKey property) for the Pilot version.

New access right at "TagID" level, addition of the following value:

•

120107: Generic > Manage scan lists

New access right at "TagID" level, addition of the following values:

•

120108: Generic > Modify internal references upon generation

•

120109: Generic > Modify external references upon generation

•

120110: Generic > Modify follow-up references upon generation

Addition of the delivery preparation management

New access right at "TagID" level, addition of the following value:

•

120801: Transfer request - Create a transfer request

+ addition of the flow of transfer request creation taking into account user restrictions on stores issuing

transfer requests

Increase in the number of days for searching documents (365 instead of a maximum of 30, with a minimum

of 1 day.)

Added the DatabaseManagement property, indicating the recovery mode of the item database.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

1/6/2022

696375

99054

#4.36

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

3/8/2022

A2328

107853

#4.40

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2022

A2306

112745

#4.???

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

10/10/2022

A2334

134923

#4.107

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

137082

137826

137305

#4.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/22/2022

A2336

139872

140466

141008

#4.167

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

2/24/2023

A2428

155952

#4.230

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2429

159600

#4.281


Cegid Retail Y2 – InventoryTracking Plugin

15

Add the DisplayPicture property, indicating the display or not of the item pictures when entering

documents.

Added the ScanLibrary section, indicating the scan libraries used in released and  pilot versions for mobile

devices under iOS.

Addition of the following properties to the GlobalSettings sub-section of the reply:

•

ScansList

•

MultipleOfQuantityManagement (for each document type)

The WorkerProcessVersion property becomes obsolete and is now an empty string.

Added configuration for software extensions

New access right 1202026: Conduct inventory - Custom inventory: Zero quantity allowed

Addition of the following properties to the GlobalSettings sub-section of the reply:

-

BillOfMaterials/Assembly: Indicates that BOMs are managed in the local cache

-

ItemTypes (for each document type): Indicates the types of items managed in the cache and allowed

for each flow when scanning or entering items on the mobile device.

Addition, in reply, of the InventoryCount section and the SerialNumberManagement property, indicating

whether serial numbers are managed in inventory counts.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2430

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2431

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/16/2023

A2456

1170194

174790

174846

#5.66

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/11/2023

1199190

178829

#5.89

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

1/4/2024

A2479

209801

211308

211501

214322

#5.194

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

2/8/2024

A2475

225465

#5.205

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/11/2024

A2492

1447515

248021

#5.241

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/30/2024

A2494

261269

#5.301


Cegid Retail Y2 – InventoryTracking Plugin

16

In SaaS environments, the URL of the extension access service transmitted through Connect was not directly

usable by the mobile device, as the SaaS configuration files gave the URL of the azure function and not the

URL of the access service. Problem fixed.

New access right 120111: “Inventory query - Other stores"

Added settings for printing labels on request, from a scan list and from a document:

-

Added the following properties to the GlobalSettings sub-section of the reply:

o

LabelTemplates: List of Y2 item label printing templates

o

LabelsManagement : Indicates the printing mode and the label template to be used for

printing labels from the scan lists (data from the company settings “Label printing

mode” and “Label printing template” in Commercial Management > Documents – entry)

-

Added the PriceListTypeId property in the Prices sub-section of the reply, indicating the price list

type

-

Added the LabelPrintingMode property to the DocumentSetting sub-section of each flow (except

PickUpPointsSetting), indicating how labels are printed

-

Added the PriceListTypeId property in the Prices sub-section of the reply, indicating the price list

type

New access right 120112: "Managing comments in documents"

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/4/2025

1947110

416594

#6.131

New access right 120113: "Duplicating a list of scans from history"

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/8/2025

1947744

416723

#6.133

In the section listing the sender stores for transfer requests, the  <Warehouses>   collection is now published,

even in the case of a single warehouse when its identifier is different from the store code.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

9/22/2025

1959709

INC0255854

420116/ 420488

#6.140

The access rights for duplicating a scan list, and managing comments in documents are now only available

in versions 6.0 and above of InventoryTracking.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

1/9/2026

1947744

1947110

446291

#7.13

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

6/18/2024

A2479

268788

#5.319

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/12/2024

A2503

298279

#5.336

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/5/2024

A2500

310967

313528

312315

318262

#6.38


Cegid Retail Y2 – InventoryTracking Plugin

17


## Reassign

New method for reallocating a mobile device to an existing device sheet allocated to another piece of

equipment to be replaced.

Reallocations of mobile devices are now systematically stored.

Addition of the Scandit key (ScanditLicenceKey property) for the Pilot version.

New access right at "TagID" level, addition of the following value:

•

120107: Generic > Manage scan lists

New access right at "TagID" level, addition of the following values:

•

120108: Generic > Modify internal references upon generation

•

120109: Generic > Modify external references upon generation

•

120110: Generic > Modify follow-up references upon generation

Addition of the delivery preparation management

New access right at "TagID" level, addition of the following value:

•

120801: Transfer request - Create a transfer request

+ addition of the flow of transfer request creation taking into account user restrictions on stores issuing

transfer requests

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

5/27/2021

A2167

72218

#3.166

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

7/5/2021

A2168

76976

#3.293

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

3/8/2022

A2328

107853

#4.40

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2022

A2306

112745

#4.???

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

10/10/2022

A2334

134923

#4.107

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

137082

137826

137305

#4.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/22/2022

A2336

139872

#4.167


Cegid Retail Y2 – InventoryTracking Plugin

18

Increase in the number of days for searching documents (365 instead of a maximum of 30, with a minimum

of 1 day.)

Added the DatabaseManagement property, indicating the recovery mode of the item database.

Add the DisplayPicture property, indicating the display or not of the item pictures when entering

documents.

Added the ScanLibrary section, indicating the scan libraries used in released and  pilot versions for mobile

devices under iOS.

Addition of the following properties to the GlobalSettings sub-section of the reply:

•

ScansList

•

MultipleOfQuantityManagement (for each document type)

The WorkerProcessVersion property becomes obsolete and is now an empty string.

Added configuration for software extensions

New access right 1202026: Conduct inventory - Custom inventory: Zero quantity allowed

Addition of the following properties to the GlobalSettings sub-section of the reply:

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

140466

141008

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

2/24/2023

A2428

155952

#4.230

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2429

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2430

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/15/2023

A2431

159600

#4.281

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/16/2023

A2456

1170194

174790

174846

#5.66

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/11/2023

1199190

178829

#5.89

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

1/4/2024

A2479

209801

211308

211501

214322

#5.194

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

2/8/2024

A2475

225465

#5.205


Cegid Retail Y2 – InventoryTracking Plugin

19

-

BillOfMaterials/Assembly: Indicates that BOMs are managed in the local cache

-

ItemTypes (for each document type): Indicates the types of items managed in the cache and allowed

for each flow when scanning or entering items on the mobile device.

Addition, in reply, of the InventoryCount section and the SerialNumberManagement property, indicating

whether serial numbers are managed in inventory counts.

In SaaS environments, the URL of the extension access service transmitted through Connect was not directly

usable by the mobile device, as the SaaS configuration files gave the URL of the azure function and not the

URL of the access service. Problem fixed.

New access right 120111: “Inventory query - Other stores"

Added settings for printing labels on request, from a scan list and from a document:

-

Added the following properties to the GlobalSettings sub-section of the reply:

o

LabelTemplates: List of Y2 item label printing templates

o

LabelsManagement : Indicates the printing mode and the label template to be used for

printing labels from the scan lists (data from the company settings “Label printing

mode” and “Label printing template” in Commercial Management > Documents – entry)

-

Added the PriceListTypeId property in the Prices sub-section of the reply, indicating the price list

type

-

Added the PriceListTypeId property in the Prices sub-section of the reply, indicating the price list

type

-

Added the PriceListTypeId property in the Prices sub-section of the reply, indicating the price list

type

New access right 120112: "Managing comments in documents"

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/4/2025

1947110

416594

#6.131

New access right 120113: "Duplicating a list of scans from history"

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/11/2024

A2492

1447515

248021

#5.241

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/30/2024

A2494

261269

#5.301

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

6/18/2024

A2479

268788

#5.319

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/12/2024

A2503

298279

#5.336

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/5/2024

A2500

310967

313528

312315

318262

#6.38


Cegid Retail Y2 – InventoryTracking Plugin

20

LDE

9/8/2025

1947744

416723

#6.133

In the section listing the sender stores for transfer requests, the  <Warehouses>   collection is now published,

even in the case of a single warehouse when its identifier is different from the store code.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

9/22/2025

1959709

INC0255854

420116/ 420488

#6.140


## GetDetail

New method of searching for the main properties of a mobile device, by knowing its identifier.

Addition of a new display property for the flow of orders to be delivered in order to view on the mobile

device the customer’s delivery address.


## Disconnect

The ULG_LOGOUTDATE field was no longer updated when the mobile device was disconnected. Problem

fixed.

Checking the default user restriction when logging out as well as when logging in.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

5/31/2021

A2167

72431

#3.182

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/6/2021

A2239

83470

#3.355

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

1/6/2022

685048

PR98896

#4:34

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/3/2023

1117358

157434

#4.241


Cegid Retail Y2 – InventoryTracking Plugin

21


### 4.   I NVENTORY T RACKING I TEM S EARCH C ACHE


## GetItemsReferential

Addition of the "MultipleOfQuantity" property to the ItemCache" section of the reply.

Optimization of item search queries.

Removed the "Nullable object must have a value" error that occurred in the GetItemsReferential method

when several methods of the ItemSearchCache service were executed at the same time.

Addition, based on the global BOM management setting, the loading of Assembly BOMs.

Added the ItemType property to the ItemCacheProperties subsection of the reply, indicating the item type

or BOM type for each returned item or BOM.


## GetListByReference

It is now possible to search for an item with its identifier, by entering this identifier in the "Reference"

property.

Addition of the "MultipleOfQuantity" property to the ItemCache" section of the reply.

Fixed the error that occurred if a date prior to 01/01/1900 was transmitted as service input during an item

search on a folder with the "Supplier catalog" search priority activated.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/15/2023

A2456

1180476

174409

#5.57

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/6/2023

1178580

178191

#5.83

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

9/21/2023

1240418

190349

#5.136

LDE

5/2/2024

A2492

1447561

254595

#5.273

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

2/21/2023

1107476

155349

#4.227

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/15/2023

A2456

1180476

174409

#5.57

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

6/22/2023

1179114

175747

175835

#5.73


Cegid Retail Y2 – InventoryTracking Plugin

22

Optimization of item search queries.

Optimization of the item search by keywords

Added the ItemType property to the ItemCacheProperties subsection of the reply, indicating the item type

or BOM type for each returned item or BOM.

RQ: Only the assembly BOM type is returned, otherwise the commodity type for all other cases


## GetModifiedItemsSinceDate

Addition of the "MultipleOfQuantity" property to the ItemCache" section of the reply.

The dates of the latest changes of keywords and supplier references are taken into account to build the

reply.

Optimization of item search queries.

Addition, based on the global BOM management setting, the loading of Assembly BOMs.

Added the ItemType property to the ItemCacheProperties subsection of the reply, indicating the item type

or BOM type for each returned item or BOM.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/6/2023

1178580

178191

#5.83

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/7/2023

1179723

178562

#5.86

LDE

4/19/2024

A2492

1447561

251070

#5.250

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/15/2023

A2456

1180476

174409

#5.57

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/4/2023

1123355

177900

#5.81

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/6/2023

1178580

178191

#5.83

LDE

5/2/2024

A2492

1447561

254595

#5.273


Cegid Retail Y2 – InventoryTracking Plugin

23


### 5.   I NVENTORY T RACKING G LOBAL S ETTINGS


## CreateOrUpdate

Implementation of the method, with Soap and RestFul exposure.

This method allows the creation or the update of the global InventoryTracking settings, i.e.:

•

Recovery ode of the item database,

•

Request for displaying pictures of items when entering documents.

•

Scan library for mobile devices.

Added support for Assembly-type BOMs (BillOfMaterials section with Assembly property in the Items

section).

The method is now set to the Released status.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

8/29/2024

A2490

1565857

293248

#5.331


## Delete

Implementation of the method, with Soap and RestFul exposure.

This method allows the removal of the global InventoryTracking. settings.

The method is now set to the Released status.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

8/29/2024

A2490

1565857

293248

#5.331


## GetDetail

Implementation of the method, with Soap and RestFul exposure.

This method allows the restitution of the global InventoryTracking. settings.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/8/2023

1108246

157698

#4.261

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/9/2024

A2492

1447487

247146

#5.233

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/8/2023

1108246

157698

#4.261


Cegid Retail Y2 – InventoryTracking Plugin

24

Added results of processing Assembly BOMs (BillOfMaterials section with Assembly property in the Items

section).

The method is now set to the Released status.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

8/29/2024

A2490

1565857

293248

#5.331

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

3/8/2023

1108246

157698

#4.261

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/9/2024

A2492

1447487

247146

#5.233


Cegid Retail Y2 – InventoryTracking Plugin

25


### 6.   I NVENTORY T RACKING M OBILE S ETTINGS


## CreateDevice, UpdateDevice, UpdateDeviceOnConnect,


## GetDetailDevice

Addition of a new display property for the flow of orders to be delivered in order to configure on the

Webapp the display of the customer’s delivery address.

Addition of the Scandit key (ScanditLicenceKey property) for the Pilot version.

Addition of the delivery preparation management

Addition of the flow of transfer request creation

Increase in the number of days for searching documents (365 instead of a maximum of 30, with a minimum

of 1 day.)

The WorkerProcessVersion property becomes obsolete and is now an empty string.

Added configuration for software extensions

The Extensibility.Extensions property is now optional in the contract of the UpdateDevice method.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/6/2021

A2239

83470

#3.355

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

3/8/2022

A2328

107853

#4.40

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

136050

136754

138926

#4.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/22/2022

A2336

140092

#4.167

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

2/24/2023

A2428

155952

#4.230

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

7/11/2023

1199190

178829

#5.89

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

1/4/2024

A2479

209801

211308

211501

214322

#5.194

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

4/25/2024

A2479

253313

#5.258


Cegid Retail Y2 – InventoryTracking Plugin

26

Added settings for how labels are printed from documents.

The DeviceModel and OperatingSystemInformation data entered when creating a device record is no longer

reset to zero when the device record is modified by the WebApp..


## GetListDisplayProperties

Addition of the V3 suffix to the descriptions of the "Movement reason" and "User-defined document tables"

properties.

Addition of the display property “Delivery address” for the flow of orders to be delivered.

Addition of the display property “Delivery preparation”

Addition of the display property “Create transfer requests”

Removed the V3 suffix from the descriptions of the "Movement reason" and "User-defined document

tables" properties.


## CreateModel, UpdateModel, GetDetailModel

Addition of the delivery preparation management

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/5/2024

A2500

316914

#6.38

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

1/6/2025

446539

446563

#7.11

#6.172

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

6/2/2021

A2213

585286

72879

#3.198

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

9/6/2021

A2239

83470

#3.355

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

136050

136754

138926

#4.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/22/2022

A2336

140092

#4.167

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/27/2025

1653057

348519

#6.74


Cegid Retail Y2 – InventoryTracking Plugin

27

Addition of the flow of transfer request creation

Increase in the number of days for searching documents (365 instead of a maximum of 30, with a minimum

of 1 day.)

Added configuration for software extensions

Added settings for how labels are printed from documents.


## GetListDevice

Removed checks on access to InventoryTracking module functions and serialization in the GetListDevice

method, so as to no longer trigger an exception when the method is called from the audit report in the

following cases:

-

InventoryTracking module not serialized to folder

-

Audit report launched by a user with no access to InventoryTracking functions

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/9/2022

A2332

136050

136754

138926

#4.140

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/22/2022

A2336

140092

#4.167

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

2/24/2023

A2428

155952

#4.230

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

1/4/2024

A2479

209801

211308

211501

214322

#5.194

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

11/5/2024

A2500

316914

#6.38

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HAD

3/17/2025

781400

372029

#6.89


Cegid Retail Y2 – InventoryTracking Plugin

28


### 7.   I NVENTORY T RACKING U SER L OG


## UserLoginNotification

Replacement of NULL strings by empty strings in the USERLOG table.


## UserLogoutNotification

Replacement of NULL strings by empty strings in the USERLOG table.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

11/9/2021

658424

91663

#3.406

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

11/9/2021

658424

91663

#3.406


Cegid Retail Y2 – InventoryTracking Plugin

29


### 8.   I NVENTORY T RACKING U SER R IGHTS


## GetList

Addition of the access right to manage scan lists (MenuListeDeScans operation)

Addition of the access right allowing the modification of:

-

Internal references (MenuModificationReferencesInternesEnGeneration operation)

-

External references (MenuModificationReferencesExternesEnGeneration operation)

-

Follow-up references (MenuModificationReferencesSuiviEnGeneration operation)

Documents upon generation

Addition of the access right to create transfer requests (MenuCreationDemandeTransfert operation)

Added access right to record a zero quantity in user-defined inventory transmissions

(MenuAuthorizationQuantiteZero operation)

Added access right to add comments in documents (operation MenuManagementCommentsDocuments)

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/4/2025

1947110

416594

#6.131

Added access right to reuse a scan list by duplicating/regenerating it from a historized scan list.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

9/8/2025

1947744

416723

#6.133

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2022

A2306

112745

#4.???

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

10/10/2022

A2334

134923

#4.107

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

4/8/2022

A2336

139872

#4.167

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

2/8/2024

A2475

225465

#5.205


Cegid Retail Y2 – InventoryTracking Plugin

30


### 9.   O THER


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

194215

#5.143


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

343756

#6.70


