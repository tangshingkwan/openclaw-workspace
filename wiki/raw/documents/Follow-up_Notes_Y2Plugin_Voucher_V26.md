# Follow-up Notes Y2Plugin Voucher V26

*Source: Follow-up_Notes_Y2Plugin_Voucher_V26.pdf | Extracted: 2026-02-27*

---


## Voucher Plugin V02


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date: January 9, 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Plugin Voucher

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


Cegid Retail Y2 – Plugin Voucher

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

CancelCreate

7

Redeem

8

CancelRedeem

9

Update

9

Cashout

10

Close

11

GetDetail

11

GetListDetail

11

3.   REPORT  ....................................................................................................................................................................................... 13

Print

13

4.   VALIDITYPERIODS  ................................................................................................................................................................. 15

Compute

15

5.   OTHER  .......................................................................................................................................................................................... 16


Cegid Retail Y2 – Plugin Voucher

4


### 1.   O BJECTIVES

The objective of the Voucher plugin is to provide services relating to the creation, viewing, and use of

“vouchers”, also called “outstanding payments”.

These are the following payments managed in Cegid Retail Y2:

•

Credit note

•

Gift card

•

Gift certificate

•

Deposit payment

Just remind: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download page:

"Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties


![Figure 4](./images/img_0004.png)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Plugin Voucher

5

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


Cegid Retail Y2 – Plugin Voucher

6


### 2.   M ANAGEMENT

The voucher management service presented in this document can only be used if the " New management

of vouchers " option is activated in the company settings, "Front Office > Link for Payments" tab.

This read-only option is activated by a legacy update utility, available in the Back Office menu

"Administration > Maintenance" menu, named " New management of vouchers ".

The execution of this utility allows the following rules to be adopted when calling the service:

•

A voucher is expressed in a single currency, that of the sales receipt.

•

A voucher can be used in any currency, the conversion being the responsibility of the calling

software, and not of the services.

•

The consumption of a voucher will only be expressed in its storage currency.

•

The service communicates the amounts only in the currency of the voucher

The details of how the vouchers work in the 2022 version are described in the Release Notes.

No business notification is managed in the voucher management.


## Create


### ➔   Objectives

This method thus allows you to:

•

Record the payment of a deposit for an order or a customer reservation.

•

Record a gift certificate or a gift card in a sales transaction for later use by the beneficiary.

•

Record a credit note following a returned sale.

The following business rules are applied:

•

The " Id " property corresponds to the voucher number which must be unique in the database. It is

regularly printed on the receipts for scanning when used.

•

The item in the " RegisterOperationIdentifier " property must exist in the database with the

following characteristics:

o

Financial item of type “Gift certificate / Loyalty gift certificate / Sales condition gift

certificate / Gift card / Deposit payment.

o

Option “Send to EPT” not checked.

o

Not closed

•

The payment method present in the " PaymentMethodId " property must exist in the database

with the following characteristics:

o

Financial item of type "Credit note."

o

Option “Send to EPT” not checked.

•

The " SalesConditionId " property is provided only if the “ RegisterOperationIdentifier " property

is of type "Sales condition gift certificate". The existence of the sales condition is not checked.

•

The voucher type of the " VoucherType " property is provided as input, and must be consistent

with the " RegisterOperationIdentifier " financial item type or the "PaymentMethodId" payment

method type.

•

The " CustomerIdentifier " property must be filled in with a customer, which can be a fictitious

customer.


Cegid Retail Y2 – Plugin Voucher

7

•

The store of the " StoreIdentifier " property:

o

Must exist in the database and not be closed.

o

Must be in the list of stores allowed by the restriction on "Outstanding payments" for the

user calling the service.

•

The amount in the " Amount " property must be strictly greater than zero.

The exactness of the amount must be consistent with the number of decimal places in the

currency.

•

The " DocumentKey " property is optional and will avoid a compatibility break when the FIC type

will be associated to the voucher in case of missing information.

•

If the document is specified (" DocumentKey " property), one of the " LineId ", " LineNumber " or

" PaymentId " properties must be specified, excluding the other.

•

If the " LineId " and " LineNumber " properties are specified, the " RegisterOperationId " property

must also be specified.

•

If the " PaymentId " property is specified, the " PaymentMethodId " property must also be

specified.

•

There is no control over the number of taxes sent compared to the number of taxes of the store.

•

The end date must be superior to the start date when specifying the validity period.

•

Idempotency is ensured by the " OperationUid " property which must be specified in a unique way

for each transaction. The presence of this property avoids the creation of two records in the event

of a network issue and the same information being returned again.

The " Created " property of the Reply informs the caller of this case.


### ➔   Improvements

The  method is now set to the Released status

For loyalty vouchers, the  GOC_TYPEBENEFITFID  column  was not filled in correctly.


## CancelCreate


### ➔   Objectives

This method allows you to cancel the created voucher, if for example, the receipt that created the voucher

is canceled.

The following business rules are applied:

•

One of the 2 properties " DocumentKey " or " CreateOperationUid " of the request is mandatory.

•

The document key defined in the " DocumentKey " or " CreateOperationUid " property must

correspond to an existing voucher.

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

179263

#1.447

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build

no.

Quality Ctrl

PLA

9/22/2025

1960150

INC0256233

420535

#1.722


Cegid Retail Y2 – Plugin Voucher

8

•

The store of the voucher must be in the list of the stores allowed by the user’s restriction

“Outstanding payments.”

•

The voucher must not have any consumption.

•

The voucher is logically deleted from the database, and its available amount is set to 0.

•

If the voucher is already deleted, the method has no impact.

•

If the voucher amount is already 0, the method has no impact.

•

Idempotency is ensured by the " OperationUid " property which must be specified in a unique way

for each transaction.


### ➔   Improvements

The  method is now set to the Released status


## Redeem


### ➔   Objectives

This method allows you to use a voucher to pay for a sale, trigger a delivery or validate a reservation.

The following business rules are applied:

•

It is not possible to consume a deleted or inactive voucher.

•

The voucher identifier must correspond to an existing voucher with an amount to consume.

•

The store of the voucher must be in the list of the stores allowed by the user’s restriction

“Outstanding payments.”

•

The reference of the issuing document given in the request must be identical to the reference of

the document that issued the voucher.

•

Either the line number of the issuing document or its payment number is given in the request.

•

The consumer store must exist and not be closed.

•

The consumer customer must exist.

•

The amount to be consumed must be strictly greater than zero.

•

The currency of the amount consumed must be equal to the currency of the voucher.

•

Either the register operation or the payment method is given, and must not be closed.

•

The consumption must be consistent with the type of the issued voucher.

Examples:

o

Register operation "Deposit payment" -> Payment method "Already paid deposit".

o

Register operation  "Deposit payment" -> Register operation "Deposit reimbursement”.

o

etc.

•

If the register operation is given, the line number of the consuming document must be given in

the request, otherwise if the payment method is given, the payment number of the consuming

document must be given.

•

The amount consumed must be less than or equal to the remaining amount of the voucher.

•

For each tax, the amount consumed of the tax must be less than or equal to the remaining

amount of the tax for the voucher.

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

179263

#1.447


Cegid Retail Y2 – Plugin Voucher

9

•

Idempotency is ensured by the " OperationUid " property which must be specified in a unique way

for each transaction.


### ➔   Improvements

The  method is now set to the Released status


## CancelRedeem


### ➔   Objectives

This method allows you to cancel the voucher consumption, if for example, the receipt that used the

voucher is canceled.

The following business rules are applied:

•

One of the 2 properties " DocumentKey " or " CreateOperationUid " of the request is mandatory.

•

The document key defined in the " DocumentKey " or " CreateOperationUid " property must

correspond to an existing voucher.

•

The store of the voucher must be in the list of the stores allowed by the user’s restriction

“Outstanding payments.”

•

The voucher is deleted logically from the database.

•

The available amount of the issued voucher is then increased by the amount of the consumption.

•

Idempotency is ensured by the " OperationUid " property which must be specified in a unique way

for each transaction.


### ➔   Improvements

The  method is now set to the Released status


## Update


### ➔   Objectives

This method allows you to update information about a voucher.

The following business rules are applied:

•

The end date must be superior to the start date of the period.

•

The voucher identifier must correspond to an existing voucher.

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

179263

#1.447

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

179263

#1.447


Cegid Retail Y2 – Plugin Voucher

10

•

The store of the voucher must be in the list of the stores allowed by the user’s restriction

“Outstanding payments.”

•

No changes are made if the period requested is already the same as the voucher period.

•

The access right of the Front Office is not taken into account.

•

The event log is fed with value "ER4" in level 3.


### ➔   Improvements

The  method is now set to the Released status


## Cashout


### ➔   Objectives

This method is used to redeem a non-splittable voucher.

The following business rules are applied:

•

The business rules for the "Redeem" voucher operation apply, except those concerning the register

operation and the payment method.

•

If taxes are supplied, then the type of use for the voucher must be "payment method", otherwise

an error will be returned.

•

If the voucher is fully used, the available amount is set to zero, even if the amount of the query is

less than the remaining amount of the voucher. The consumed amount registered is then the

remaining voucher amount.

•

The corresponding record is created by repeating the register operation or payment method used

to issue the voucher and inverting the sign of the amount, as done by the "Close" operation.


### ➔   Improvements

Correction to fully consume a loyalty voucher issued by a Y2 loyalty program that is associated with both

a register operation and a payment method.

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

179263

#1.447

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

10/10/2023

A2464

194120

#1.516

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

NAC

3/8/2024

236087

#1.560


Cegid Retail Y2 – Plugin Voucher

11


## Close


### ➔   Objectives

This method is used to make a voucher unusable.

The following business rules are applied:

•

No action is performed by the method, if the available amount of the voucher is 0.

•

Otherwise, a full consumption of the voucher is made at the closing date. The movement qualifier

of this consumption is “Solde” (Closing).

•

No control is made on the issuance data read from the database during this particular

consumption (because it is assumed that the data in the database is correct.)

•

The access right of the Front Office is not taken into account.

•

The event log is fed with value "ER1" in level 3.


### ➔   Improvements

The  method is now set to the Released status


## GetDetail


### ➔   Objectives

This method retrieves the information about a voucher to be used, or the details of its use.

The following business rules are applied:

•

The store of the voucher must be in the list of the stores allowed by the user’s restriction

“Outstanding payments.”

•

The amounts are always positive, whether for acquisitions or consumptions.


### ➔   Improvements

The  method is now set to the Released status


## GetListDetail


### ➔   Objectives

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

179263

#1.447

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

179263

#1.447


Cegid Retail Y2 – Plugin Voucher

12

This method allows you to retrieve information from a list of vouchers in order to use them or consult the

details of their use.

The following business rules are applied:

•

The rules of the " GetDetail " method are applied

•

At least one of these properties is specified in the request:

o

" Ids ”

o

“ CustomerIdentifier “

o

“ DocumentKey ”

If several properties are specified (not empty):

o

If the "Ids" property is present, a search is performed on these ids, filtered by customer

and/or document.

o

Without Ids, a search is performed on the vouchers of the document, the document must

correspond to the specified customer.


### ➔   Improvements

The  method is now set to the Released status

Added the VoucherTypes property to the request.

Added the Store property to the request to filter the vouchers issued in several stores.

Consider the time difference between the cash register and the server to include vouchers that are

available and acquired from cash registers in advance.

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

179263

#1.447

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

7/24/2023

A2461

180983

#1.452

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

9/8/2023

A2470

187740

#1.476

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build

no.

Quality Ctrl

PLA

12/10/2025

2016005

INC0270178

441981

#1.762


Cegid Retail Y2 – Plugin Voucher

13


### 3.   R EPORT

Printing service for voucher.


## Print


### ➔   Objectives

This method generates a voucher in "Image", "PDF", or "Text" format.

The report template used is the one associated with the store and the type of voucher, i.e.: credit note, gift

certificate or deposit.

The culture provided to the method is used to translate the data captions and format the numbers and

dates.


### ➔   Improvements

Fixed the “The StoreId is required” error that occurred when printing a credit note voucher.

The method is now set to status Beta

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

300515

#1.603

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

353170

#1.644

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/23/2025

1775141

393488

#1.686

Possibility to use a voucher template without using Config Console (via TemplateCode)

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

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

EPL

5/5/2023

1137846

167912

#1.428

Dev

Date

CEGID’s Ref.

Pb

Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

8/11/2023

1218984

184112

#1.462


Cegid Retail Y2 – Plugin Voucher

14

OEL

2/4/2025

420131

#1.724


Cegid Retail Y2 – Plugin Voucher

15


### 4.   V ALIDITY P ERIODS


## Compute


### ➔   Objectives

This method allows you to calculate the validity period of a voucher based on a creation date.

Example: Calculation of the validity period of a voucher issued this day.

This method will be used when a voucher is created, either by the calling application, or by the creation

service, if the information is not present in the contract.

The following business rules are applied:

•

Only one of these properties " RegisterOperationIdentifier " or " PaymentMethodId " must be

specified.

•

The identifier of the register operation or the payment method must exist.

•

The validity period is determined according to the settings defined for the register operation or

payment method.

•

No check is made on the data read from the database (because it is assumed that the data in the

database is correct.) Certain settings can lead to inconsistencies such as a start date greater than

the end date.


### ➔   Improvements

The  method is now set to the Released status

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

179263

#1.447


Cegid Retail Y2 – Plugin Voucher

16


### 5.   O THER


## Swagger

Rest/Restful APIs grouped by plugin, with the option of selecting them by plugin name.

Dev

Date

CEGID’s Ref.     Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/16/2025

1543349

345273

#1.639


