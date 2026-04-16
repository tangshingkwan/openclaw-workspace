# Follow-up Notes Y2Plugin SalesExternal V26

*Source: Follow-up_Notes_Y2Plugin_SalesExternal_V26.pdf | Extracted: 2026-02-27*

---


## SalesExternal Plugin V06


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   20 February 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – SalesExternal Plugin

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


Cegid Retail Y2 – SalesExternal Plugin

3


## Contents

Preamble

2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation

4

Y2 versions

5

2.   ENGINE ............................................................................................................................................................................................ 6

Service deprecated, replaced by Engine2.

6

3.   ENGINE2  ......................................................................................................................................................................................... 7

GetTotalWithTaxes

7

RegisterSale

7

Calculate

16

GetReceipt

16

GetChainedDocumentLines

19

Update

19

SanityCheck

20

UpdateCustomer

21

GetListDetail

22

4.   REPORT  ....................................................................................................................................................................................... 24

GenerateDocument

24

Poll

24

Download

25

5.   REPORT2  .................................................................................................................................................................................... 26

SalesReceipt

26

SalesReceipt2

26

SalesReceipt2Get

28

SalesReceipt2FromKey

28

SalesReceiptDuplicate

29

GiftReceipt

30

CashFloatReceipt

30

ZReceipt

31

6.   OTHER  .......................................................................................................................................................................................... 32


Cegid Retail Y2 – SalesExternal Plugin

4


### 1.   O BJECTIVES

This document describes the changes and corrections made to Cegid Retail  SalesExternal  Plugin. The

SalesExternal plugin is a set of web services associated with the corresponding version of Cegid Retail Y2

to create sales captured in a third-party system.

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


Cegid Retail Y2 – SalesExternal Plugin

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


Cegid Retail Y2 – SalesExternal Plugin

6


### 2.   E NGINE


## Service deprecated, replaced by Engine2.


Cegid Retail Y2 – SalesExternal Plugin

7


### 3.   E NGINE 2


## GetTotalWithTaxes


### ➔   Objectives

The objective of this method is to calculate taxes for a tax-exclusive or tax-inclusive basket based on

transmitted information.

Please note: the tax engine of this service is different from that used by the original Cegid Retail Y2

engine. This difference may cause different results to be obtained when calculating rounding.

Details of properties

   CountryId : This property should match the internal country code of Cegid Retail Y2. No matching

is performed if other codes are sent (ISO2, ISO3, INSEE).


### ➔   Improvements

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Increase in the maximum size of the TransactionNumber field, from 35 to 70 characters

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/13/2026

2032732

447463

#5.604


## RegisterSale


### ➔   Operation

The objective of this method is to perform the following operations:

   Check information transmitted on the store, cash register, customer, items, etc.

   Recalculate the receipt to fill in the Cegid Retail Y2 data model. Taxes should be sent in the

contract.

   Record the receipt to feed into the Cegid Retail Y2 tables and be able to view it, change it (subject

to constraints), or print it as if it comes from a Shopping, Front or Back Office entry.

Affiliation of the sale

Sales made through external cash registers should be contained within a regulatory and managed

framework. An external device should not be able to include a sale on any date, without choosing the

store or without any tax system.

The inclusion of a sale is conditional on the presence of:


Cegid Retail Y2 – SalesExternal Plugin

8

   A non-closed store with a non-closed sales warehouse (use the same code as the store in the case

of a single-warehouse folder).

   This store should be authorized for the user (application of user restrictions).

   An external non-closed cash register allocated to the store.

   An open session, at the initiative of the store. If this operation is currently carried out in the Front

Office of Cegid Retail Y2, the objective in a later version is for it to be managed from a Web

Application.

Customer management

The presence of a non-closed customer is mandatory in the contract, whether a named or passing

customer. Only the customer code is specified, which allows its presence to be checked in Cegid Retail Y2.

The customer's information on the database is used by default, overwritten by that sent in the contract to

be recorded in the sale. However, the data sent does not update the customer record (the document type

setting is ignored).

In the event of a customer not existing in Y2, the customer should be created before calling the WS.

Customers should not have the status of "prospect" and should be visible to the user (application of

restrictions).

The country of the customer's address (CountryId) should match the internal country code of Cegid Retail

Y2. No matching is performed if other codes are sent (ISO2, ISO3, INSEE).

The following customer information is not taken into account in this version:

   Concept of closed customer, with document settings taken into account.

   The e-mails and telephone numbers transmitted are not corrected, regardless of the company

settings configuration.

Management of lines

Each line should use the internal item code (GA_ARTICLE), which identifies it in a unique and

unambiguous manner. Only the following types of items are accepted in lines with the following

characteristics:

   Integration of comment lines

   Integration of services (see "improvements" below for the minimum version).

   Integration of items of a unique or dimensioned merchandise type.

o

Positive amount or zero with integration of decimals of quantities and unit prices defined

in the company settings.

o

All lines are expressed as tax-exclusive or tax-inclusive.

   In the event of discount,

o

The reason should follow the markdown reason restrictions.

o

Only certain discounts can be used as described in the contract. The others should be

dispatched on each line.

o

The "discountable" characteristics of the item are monitored.

o

A "sales condition" discount should refer to an existing sales condition.

Other types of items are rejected:

   Generic items

   Subtotal

   Bills of materials

   Financial items


Cegid Retail Y2 – SalesExternal Plugin

9

   Items managed with serial numbers are included in the sale but the serial numbers are ignored.

Sales are included as if the item was not managed by serial number.

The following information in the item is not taken into account in this version:

   Concept of item closed or suspended from sale.

   Units of items and items by batch.

   "Sold in multiples of" characteristic.

   Accounting for stock outages.

   Constraints related to sales divisions.

   Base price of the item not searched; the gross price is copied into the base price.

Payment management

The receipt should be paid in full by payment line, with the following characteristics:

   The internal code of the payment method is used.

   The payment method should be authorized for the user (application of user restrictions).

   The payment amount should be expressed in both the currency of the payment method and the

currency of the store.

   The payment method should have the "Usable at register" property specified.

   A payment line should not have a zero value.

   Payment methods should be of the following type:

o

Bank card

o

Cash and checks (see the "improvements" below for the minimum version).

o

Other

   The characteristics of payment methods are not checked (triggers, amounts, direction, additional

information, access rights, etc.).

Receipt information

The mandatory nature of user-defined document tables (with exception by store) is taken into account.

The seller in the header is recovered and copied by default onto the lines.

The internal reference is automatically generated according to the operation of the Front Office, with

systematic zeroing for each day’s opening.

External and follow-up references are incorporated (see "improvements" below for the minimum version).

It is possible to manage the "sales to be delivered" (see "improvements" below for the minimum version),

with the following characteristics;

   Cegid Retail Y2 is used to manage a delivery address and an invoicing address. The contract will

only manage two situations:

o

The sale is "taken away"; the customer's invoicing address has been provided

o

The sale is "delivered"; the address provided acts as the customer's delivery and invoicing

address.

   In the case of a delivered/picked up/activated module, a sale with the SaleToDeliver property

checked is rejected.

   The post code and country of the customer's address are becoming mandatory.

The following information is not taken into account in this version:

   Tax information (fiscal counter, etc.)

   User fields for documents

   Sales return


Cegid Retail Y2 – SalesExternal Plugin

10

   Tax refund

   Airport sales

   Clock-in/clock-out of salespeople

   Loyalty (joining, counting, benefits)

Receipt image:  At the end of processing, the image of the receipt is generated and stored in the

database. If the image is not generated (technical error, non-existent Stimulsoft template), the data used

to regenerate it later is nevertheless stored in the database.

Idempotency

Idempotency guarantees that an action gives the same result, regardless of its number of applications.

Good practice is to specify the OperationUid property in the contract, allowing Cegid Retail Y2 to record

this information, in order not to repeat the processing. This number should therefore be unique and have

the structure of a GUID.

Example:

•

Software calls the CreateFrom service to generate a document in Cegid Retail Y2.

•

Y2 performs the processing but cannot communicate this information with the caller, who makes

a fresh attempt:

o

If the OperationUid property is transmitted, Y2 knows that the processing was successful

and informs the caller.

o

With no OperationUid property specified, Y2 attempts to repeat the same processing,

risking the creation of a new document.

We undertake to provide this information; it will soon become mandatory.

Complementary data

The following properties are added to the cart lines:

•

References.Catalog: Catalog reference. No control is performed on this data.

•

References.Package: Package reference. No control is performed on this data.

•

AdditionalDescription: Complementary description. No control is performed on this data.

•

TaxExceptionId: Identifier of the tax exception that must exist for the line tax model.

The following properties are added to the cart payments:

•

PSPReference.TerminalPrivateData: Private data of the payment terminal. No control is performed

on this data.

User fields

The user fields of the shopping cart provided by the "Header.UserFields" property are taken into account

and saved when the receipt registered after the following items have been checked:

•

The user fields module must be enabled .

•

The user field identifier must exist in the user field settings.

•

The value of the user field the request must match the type defined in the user field settings.

•

If the type of the user field is set to "string", the text value must contain at least the number of

characters set in the minimum size and must not exceed the maximum size.

•

If the user field type is set to "numerical", the integer part of the numerical value must not exceed

the number of digits set in the integer part and the decimal part of this value must not exceed the

number of digits set in the decimal part.


Cegid Retail Y2 – SalesExternal Plugin

11

•

If the type of the user field set is "selection list", the given value must exist in the associated

subtable or in the configured value list.

•

The user field identifier is not checked for its presence in the list of available user fields for the

document type.

•

No user restrictions are checked and the 'mandatory' property of the user field setting is ignored.

Reference of the original sale

•

The "RegisterSale" operation considers the references of the "LinkedDocuments" property with

the link type "OriginalSale" to create a link between the return line and the original line. This is

called a controlled return.

•

Remainders are not supported in the case of a controlled return. All items of the sales line must

be returned.

•

The following rules are applied:

•

The reference of the original sale is given by the element of the "LinkedDocuments" property

having the "OriginalSale” link type.

•

The elements of "LinkedDocuments" with a link type different from "OriginalSale" are ignored.

•

The "LinkedDocuments" property can only contain one element whose link type is "OriginalSale".

An error is raised if several items with this type are found.

•

The reference of the original sale is only available for a return line, i.e., with a negative quantity.

An error is raised if it is given for a line with a positive or zero quantity.

•

The reference of the original sale must correspond to a line of an existing document. An error is

raised if the document line does not exist in Y2.

•

The item of the original sale must be identical to the one of the return line of the shopping cart.

An error is raised if these items are different.

•

The quantity of the original sale must be identical to the one of the cart return line, to the nearest

sign. An error is raised if these quantities are different.

•

The original sales line must not have been returned. An error is raised if a return has already been

recorded for this original line.

•

An error is raised if several lines in the basket reference the same original sales line.

•

The original sales document must be a sales ticket. An error is raised if the linked document is of a

different nature.

Taxation region and country

The maximum length of the taxation region code has been increased to 10 characters in order to take into

account the code returned by the tax calculation service (TaxEngine) which now returns the taxation

region and country in the details of the taxes applied to the document lines.

Additional data for tax calculation

The customer's tax exemption reference provided by the customer, the reason and the original sale date

of the return lines are passed to the tax calculation service (TaxEngine) which can send them to an

external tax calculation connector.


Cegid Retail Y2 – SalesExternal Plugin

12

Item identification

The item of the line can be identified by its id or by its barcode. Consequently, at least one of the two

properties "Lines[].Product.ItemIdentifier.Id" or "Lines[].Product.ItemIdentifier.Barcode" of the line must be

specified.

The search for the item is done with the "Id" property if it is specified, otherwise with the "Barcode"

property.

If both properties are specified, the value of the "Barcode" property must be the barcode of the item with

the identifier given by the "Id" property.

Externally managed financial items

The cart can now contain sales lines rows with a financial item.

The following rules are applied:

•

An item of type "financial item" is accepted in the cart if the type of financial item is among the

following list and if the option "Send amount to EPT" is checked.

o

Acquisition of gift certificate

o

Acquisition of gift card

o

Deposit payment

o

Deposit reimbursement

o

Credit note reimbursement

o

Gift certificate reimbursement

o

Reimbursement of a gift card

•

A financial item is accepted in the cart if it is of type

o

Misc. input

o

Miscellaneous output

•

If a line in the shopping cart contains a financial item that does not meet the above conditions, an

error is raised.

•

If the "AllowDiscountLine" and "AllowDiscountDocument" properties are not given in the query,

they are initialized with the "Line discountable" and "Invoice total discountable" indicators of the

item.

•

The lines with a financial item are subject to neither a line discount, nor an invoice total discount.

The "AllowDiscountLine" and "AllowDiscountDocument" properties, if given, must be false

otherwise an error is raised.

•

If the "Discounts" property is specified for a line with a financial item, it must be empty or an error

will be raised.

•

The quantity of the lines with a financial item must be 1 or -1 (case of a cancellation).

•

The "PSPReference" property can only be specified if the option "Send amount to EPT" of the

financial item is checked. An error is raised if the condition is not met.

•

If the option "Use with other items" of the financial item is not checked, all the merchandise lines

of the cart must be related to the financial item. An error is raised if the cart contains a line with

an item different from the financial item.

•

If the option "Cash transaction" of the financial item is checked, the accounting type of the

created receipts "cash flow receipt" and the internal reference assigned to this receipt follows the

cash flow receipt chronology of the cash register.

New payment methods are accepted.

The following rules are applied:


Cegid Retail Y2 – SalesExternal Plugin

13

•

The payment methods are accepted if their type is among the following list and if the options

"Send amount to EPT" or "Software extension" are checked

o

Credit note

o

Already paid deposits

o

Gift Certificate

o

Gift card

•

If a payment of the receipt contains a payment method that does not respect the previous

conditions, an error is raised.

•

The "PSPReference" property can only be specified if the "Send amount to EPT" option of the

payment method is checked or if it is of the "bank card" type to ensure compatibility with the

previous functioning. An error is raised if the above conditions are not met.


### ➔   Improvements

Save voucher numbers linked to business discounts provided in the Basket / Lines / Product / Discounts

sections of the query.

Added OffLineMode information to indicate that the receipt was created in offline mode.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/5/2024

1371012

224113

#5:39 AM

Added the following properties to the PSP information for lines and payments.

•

CardExpirationDate: Expiration date of the payment.

•

CardMaskedNumber: Hidden payment card number.

•

CardRemainingAmount: Amount remaining on the payment card.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

2/5/2024

1398291

224410

#5:41 AM

A free item, i.e., one with a net amount of zero, a non-zero tax rate and a tax amount of zero, is now

accepted in a shopping cart.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

4/4/2024

1371123

245835

#5.81

Once the receipt is saved in the database, the GetTax operation of the TaxEngine service is called a second

time with the 'Commit' option to save the transaction in the tax system. This second call is made if the

TaxEngine has indicated in the reply to the first call that the transaction is to be recorded in the tax

system.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

4/23/2024

1371123

252377

#5.96

The company setting specific to the SalesExternal plugin “Y2 method of rounding amounts” allows the

harmonizes rounding calculations between SalesExternal and Y2.

Y2 supports arithmetic rounding: A method that always rounds to the nearest integer farthest from zero.

For example, 2.5 is rounded to 3 and -2.5 is rounded to -3.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

12/13/2023

A2464

209215

#5.4


Cegid Retail Y2 – SalesExternal Plugin

14

If this setting is unchecked (default): The rounding calculation via SalesExternal is a bank rounding: a

method that rounds to the nearest integer and for numbers exactly halfway from an integer to the lower

integer if the previous integer is even  or to the upper integer if the previous integer is odd. With this

method, 2.5 is rounded down to 2 and 3.5 is rounded up to 4. This method minimizes the cumulative

rounding error.

By checking this setting, the rounding calculation performed by SalesExternal will switch to the arithmetic

rounding method like in Y2.

Note that from this revision SalesExternal authorizes an amount difference during integration in Y2: The

rule being that there can be a difference of 1 on the last decimal place (position of the last decimal place

depending on the currency). For example, in Euro, SalesExternal will accept 11.23 or 11.25 while it

calculates 11.24. But it will not accept 11.26.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

5/3/2024

1447320

256063

#5.108

Fixed the NullReferenceException error raised in data preloading when no customer is given in the receipt

creation query.

In the event of an error, a trace is added with the details of the query but excluding customer data.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

5/14/2024

1447325

258665

#5.112

The key of the created receipt is passed to the "DocCode" property on the second call to the GetTax

operation of the TaxEngine service, which is made with the 'Commit' option.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

6/6/2024

1371123

264126

#5.117

For the 2nd call of TaxEngine, the empty customs codes of the lines added by TaxEngine for the

TaxConnector during the 1st call are set to zero.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

6/11/2024

1371123

266256

#5.120

Fixed the calculation of the tax amount of a sales condition discount for a line when the Y2 rounding

method is activated.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

6/12/2024

1447320

266585

#5.124

Fixed the error encountered when issuing a deposit with a tax amount of zero.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

6/13/2024

1447320

267229

#5.131

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227


Cegid Retail Y2 – SalesExternal Plugin

15

The recording of the receipt is no longer blocked by exception CBR_161_0006, in the event that the billed

or paying customer, or delivered customer is not found. The corresponding fields in the receipts are updated

with the third-party code of the receipt.

However, the information remains available in the logs.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

10/24/2024

1614415

314772

#5.229

Add the possibility of using loyalty points as a payment method.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

12/4/2024

1645788

330267

#5.250

A free item, i.e., one with a net amount of zero, a non-zero tax rate and a tax amount of zero, is now

accepted when validating the receipt.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

1/9/2025

1370976

342395

#5.262

Fixed the application of a document discount in amount on the lines of a shopping cart where the last line

is free and has the highest discount amount.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

1/15/2025

1655022

344722

#5.270

The consistency check between receipt salesperson and receipt store has been moved to the Employee

plugin, referenced #3.309. It is no longer possible to pass to the  RegisterSale  method a salesperson who

does not respect the rules controlled by the Employee plugin.

The reference to the Receipt plugin has changed to #5,181

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

1/21/2025

1690668

346861

#5.279

Possibility to sell an item of type " Assembly BOM " by providing the list of component items.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/3/2025

1710613

365468

#5.307

Corrected component quantity check when returning an assembly BOM that should always be strictly

positive.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/13/2025

1710613

370736

#5.317

Corrected LPP, LCP, WAPP, and WACP valuations of component lines in an Assembly BOM that were

incorrect.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

HDA

4/2/2025

1710613

379670

#5.337

Addition of the tax version to the information sent to the Receipt plugin for updating tax information

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl


Cegid Retail Y2 – SalesExternal Plugin

16

OEL

11/21/2025

1710613

436369

#5.525

Increase in the maximum size of the TransactionNumber field, from 35 to 70 characters

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/13/2026

2032732

447463

#5.604


## Calculate


### ➔   Objectives

The objective of this method is to calculate the amount for the limes of the shopping cart, after a range of

discount has been applied.


### ➔   Improvements

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Increase in the maximum size of the TransactionNumber field, from 35 to 70 characters

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/13/2026

2032732

447463

#5.604


## GetReceipt


### ➔   Objectives

The objective of this method is to return the  data of a receipt from its key.


### ➔   Improvements

Return voucher numbers linked to business discounts provided in the Basket / Lines / Product / Discounts

sections of the query.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

12/13/2023

A2464

209215

#5.4


Cegid Retail Y2 – SalesExternal Plugin

17


### Serial number

In a certain scenario, especially after several item deletions from the receipt, the GetReceipt method was

not returning the serial numbers of an item, due to a mismatch between the GL_NUMLIGNE and

GLS_NUMLIGNE columns. Fixed.


### Creation method

Added methods for creating missing receipt lines, whose absence caused an argument exception.


### Revision management

The presence of fields added with revisions 20 and 21 to the reply from GetReceipt is conditional on the

presence of WithRevision20 and WithRevision21 in the Fields property of the request.

If WithRevision20 is present in the Fields property the following information is added:

•

In the receipt header

o

Cancelled: Receipt canceled

o

Origin: Type of origin

o

ExportSales: Receipt processed as export sale.

•

in the receipt lines

o

LineRank: Rank of the line

o

Origin: Type of origin

o

CreationOrigin: Creation method

Links of the following types are returned at cart line level if WithRevision21 is present in the Fields

property:

•

CustomerOrderToReceipt: the line is linked to a customer order

•

ReservationToReceipt: the line is linked to a reservation

•

Ecommerce: the line is linked to an e-Commerce order

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

1/9/2024

1354615

215650

#5:14 AM

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

1/31/2024

1393471

222737

#5:32 AM

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/13/2024

1407019

227281

#5:47 AM


Cegid Retail Y2 – SalesExternal Plugin

18


### Register operation notepad


### To populate the  <PSPReference>  node of the reply, the plugin performs a join between the receipt

line and the line of the MOPERCAISSEOLE table, containing the notepad. Use of the  LineRank  property of

the receipt line instead of  LineNumber .


### Type of line

Fixed the issue of raising an exception when viewing a receipt for which the type of one of the lines is not

specified.

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Possibility to get the components of an item of type "Assembly BOM" sold in a shopping cart with the

"Components” option of the "Fields” property.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/3/2025

1710613

365468

#5.307

Tax tags are now returned even when the tax amount is equal to 0.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

3/21/2025

1740354

374446

#5.320

Return of private data from fiscal device (MBP_BLOCNOTE field in the MPIECEOLE table) in the

Header.FiscalInformations section, provided the FiscalDevicePrivateData value has been set in the Fields

tag in request.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

5/16/2025

1761202

391789

#5.351

Added information relating to tax refunds. A new ‘TaxRefundData’ tag with the information is returned if

‘TaxRefundData’ is selected in ‘Fields’ in Request. The new ‘HasTaxRefunded’ tag indicates in all cases

whether the receipt has benefited from a tax refund.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

8/21/2024

1573576

290616

#5.172

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

9/9/2024

1189133

296939

#5.187


Cegid Retail Y2 – SalesExternal Plugin

19

AAH

11/26/2025

1972509

436454

#5.529

Addition of the tax version linked to French law NF525 to the response in terms of tax information

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

12/10/2025

1710613

441158

#5.556

Increase in the maximum size of the TransactionNumber field, from 35 to 70 characters

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/13/2026

2032732

447463

#5.604


## GetChainedDocumentLines


### ➔   Objectives

This method returns the lines of the previous documents, starting with the most recent (the line of rank 1),

to the oldest (the highest rank).


### ➔   Improvements


## Update


### ➔   Objectives

The objective of this method is to update the external reference, the tracking reference, the user-defined

dates or user fields and the external reference of the lines of a sale already recorded.

The general principle is described as follows. If there is tag in the query and its value is null, the

corresponding column in the database is reset; but if the tag is not present in the query, the

corresponding of receipt is not modified.

Business rules

•

The follow-up reference given in the transaction request is copied into the GP_REFSUIVI column of

the PIECE table without taking into account the document type settings and without checking its

uniqueness.

To be consistent with existing services and with the import of data from Cegid Retail Y2, it is

accepted that the calling application gives a follow-up reference even though the follow-up

reference is not activated for this document type.

The uniqueness of the follow-up reference is not checked, even if this check is activated for

document type, because Cegid Retail Y2 checks that the code entered is not the follow-up reference


Cegid Retail Y2 – SalesExternal Plugin

20

of one of the documents relating to the customer of the sale. This verification is not adapted to in-

store sales rather to  purchase or B2B flows.

•

The current processing of the external reference is kept, and this reference is copied into the

GP_REFSUIVI column of the PIECE table without taking into account the document type settings

and without checking its uniqueness for the same reasons as for the follow-up reference.

•

The external reference for lines is not modified to remain consistent with document entry and data

import in Cegid Retail Y2.

•

The external reference of each line given in the query is copied into the GL_REFEXTERNE column of

the LIGNE table without checking its uniqueness and without any relation with the external

reference in the header.

•

The value of the user-defined document table given in the operation query must exist in the

associated subtable in the document type settings.

•

An error is raised if the value of the user-defined document table is empty in the query and the

user-defined table is declared mandatory in the document type settings.

•

The value of the user-defined customer table given in the operation query must exist in the

associated subtable.

•

The user fields of the document are modified according to the following principle. Each given user

field is inserted into user field table of the document if it does not exist in the database. If the user

field exists in the database and if a value is passed in the query, then the value in the user field table

of the receipt is modified with the given value. If the user field exists and no value is passed in the

query, then the user field is removed from the user field table of the document.

•

The business rules applied to user fields also apply when creating a receipt with the "RegisterSale"

operation .


### ➔   Improvements


## SanityCheck


### ➔   Objectives

The role of the RegisterSale method is to perform all the necessary checks before the receipt is registered.

These verifications take place after the payment, which is too late in the cycle because errors related to

problems of configuration, bug, etc. require payment cancellations, which are always complex to manage.

The objective of this method is to perform checks as early as possible in the lifecycle of the receipt, i.e.,

Before the payments are entered.

The localization rules that apply from the "receipt total" are not checked.

Moreover, the user fields in the header are not checked.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

2/17/2023

154658

#4.175


Cegid Retail Y2 – SalesExternal Plugin

21


### ➔   Improvements

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Add cart payment check

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

12/30/2025

1804432

445975

#5.581

Increase in the maximum size of the TransactionNumber field, from 35 to 70 characters

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

2/13/2026

2032732

447463

#5.604


## UpdateCustomer


### ➔   Objectives

The role of the UpdateCustomer method is to assign a previously registered receipt to a customer.

The following handling rules apply:

•

The key of the document to be modified must correspond to an existing receipt, otherwise an error

will be returned.

•

The store of the receipt must be included in the user’s default restriction, otherwise an error will be

returned.

•

The receipt must not be canceled or deleted, otherwise an error will be returned.

•

The receipt must not have been exported to accounting, otherwise an error will be returned.

•

The receipt must not be assigned to a tax refund (otherwise an error will be returned).

•

The posting type of the receipt must not be cash, otherwise an error will be returned.

•

No line of the receipt to be modified must contain a register operation that  prohibits assignment

to a customer, otherwise an error will be returned.

•

If the customer’s identifier and external reference are not specified, an error will be returned.

•

If the identifier is specified, it must correspond to an existing customer, otherwise an error will be

returned.

•

If the external reference is specified, it must correspond to an existing customer, otherwise an error

will be returned.

•

If both the identifier and the external reference are specified, they must correspond to the same

customer, otherwise an error will be returned.

•

The chosen customer must be included user’s customer restriction, otherwise an error will be

returned

•

The new customer must not be closed, otherwise an error will be returned.


Cegid Retail Y2 – SalesExternal Plugin

22

•

If the address is specified, address management must have been enabled for the receipt type,

otherwise an error will be returned.

•

The title or the legal form must correspond to an existing code, otherwise an error will be returned.

•

The country must correspond to an existing code, otherwise an error will be returned.

•

The region must correspond to an existing code, otherwise an error will be returned.

•

Address line numbers must be sequential, otherwise an error will be returned.

•

An Individual tag or exclusively a Company tag must be present, otherwise an error will be returned.

•

If addresses are specified, one of these addresses must be a delivery address and the other a billing

address, otherwise an error will be returned.

•

The address must be filled in, if the "Sale for delivery" option of the receipt is set to is true, otherwise

an error is returned.

If the above conditions are met, the following elements are modified:

•

Customer codes in the receipt header are replaced with those of the given customer.

•

The customer codes of the receipt lines are replaced with those of the given customer.

•

The customer code for the  payments of the ticket is replaced with that of the given customer.

•

The customer code of the receipt register operations is replaced with that of the chosen customer,

i.e., Balance due, credit collections and vouchers managed by an electronic payment system or

software extension.

•

The addresses specified in the query are copied to the receipt addresses. If no address is specified,

the receipt addresses are deleted.

•

A line is inserted in the Y2 event log if the user granted access to the "Assign receipt to customer”

line of the Follow up actions menu.


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

300318

#5.194

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

352714

#5.294


## GetListDetail


### ➔   Objectives

This method returns the receipt headers according to selection criteria.

The selection criteria are:

-

A list of store identifiers

-

A list of external references for stores

-

A receipt creation date interval


Cegid Retail Y2 – SalesExternal Plugin

23

-

A list of identifiers for salespeople and identifiers

-

The internal or external reference of the receipt

In the reply, you can choose whether to include system fields and whether to hide customer data.

You can choose to sort the returned receipts: newest to oldest (default), oldest to newest or by number.

Pagination is supported.

In return, you obtain a list of receipt headers.

The "Sales query" restriction for stores is applied.


### ➔   Improvements

Added information relating to tax refunds. A new ‘TaxRefundData’ tag with the information is returned if

‘TaxRefundData’ is selected in ‘Fields’ in Request. The new ‘HasTaxRefunded’ tag indicates in all cases

whether the receipt has benefited from a tax refund.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

AAH

11/26/2025

1972509

436454

#5.529

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

OEL

7/25/2025

408681

#


Cegid Retail Y2 – SalesExternal Plugin

24


### 4.   R EPORT

This service manages the transmission of the PDF of an invoice, with the following steps:

➔   Cegid Retail Y2 server request to generate the PDF document on the server, by using the printing

templates configured in the Back Office.

➔   Loading the PDF to the service caller as soon as available on server.

➔   Sending the PDF to the service caller, for printing managed by this caller.

Please note: this service does not allow the document to be marked as printed (GP_EDITEE field not

updated). The change in value of this field is reserved for interactive publishing, which links the creation of

the PDF to its printing.


## GenerateDocument


### ➔   Objectives

This method prompts the print server to stack the printing request of a document, using its unique identifier

in Cegid Retail Y2.

The report is printed by default in the “software language” as defined in the cultural profile of the user using

this service for the following elements:

➔   The mask: Titles and descriptions of the report template

➔   The format of numbers and dates.

➔   The data transmitted: item descriptions, markdown reason, etc.

The  LanguageId  property allows you to edit the report mask and the format of numbers and dates

according to this new language.

The  CultureId  property allows you to force the formatting of data numbers and dates:

➔   If the LanguageId property is missing.

➔   If the LanguageId property is identical to the "software language" in the user’s cultural profile.

The data remains in the user's language.

Only the native Cegid report generator is used to generate the PDF.


### ➔   Improvements


## Poll


### ➔   Objectives

At the end of the PDF generation call, the Poll method is called to find out its availability.

In interactive mode, we advise to make a first call after 5 seconds, then every 2 seconds without time limit,

leaving the user the possibility to interrupt the wait.


Cegid Retail Y2 – SalesExternal Plugin

25

In batch mode, a call every 5 seconds is recommended, with a maximum of 10 calls.


### ➔   Improvements


## Download


### ➔   Objectives

When the Poll returns positively, the Download method is used to download the PDF and print on a printer,

store it or send it by e-mail.


### ➔   Improvements


Cegid Retail Y2 – SalesExternal Plugin

26


### 5.   R EPORT 2

This service manages the generation of receipts in image format.


## SalesReceipt


### ➔   Objectives

This method formats the sales receipt with a given culture. The printing template is the one stored in the

database for the cash register.

The contents of the receipt are the same as those sent to Engine.RegisterSale.

The generated image is a monochrome image.


### ➔   Improvements

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


## SalesReceipt2


### ➔   Objectives

This method formats the sales receipt with a given culture. The printing template is the one stored in the

database for the cash register.

The content of the receipt is the same as the one sent to Engine2.RegisterSale.

The generated image is a monochrome image.


### ➔   Improvements

Added the following properties to PSP information for lines and payments.

•

CardExpirationDate: Expiration date of the payment.

•

CardMaskedNumber: Hidden payment card number.

•

CardRemainingAmount: Amount remaining on the payment card.


Cegid Retail Y2 – SalesExternal Plugin

27

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

2/21/2024

1392260

229912

#5:50 AM

Stop blocking the size of the item the description of the line to be printed, at 70? The control has been

changed to 5120 (maximum size already used in this same plugin.)

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

4/11/2024

1456523

248111

#5.85

Added the possibility to enter the code of the template to be used.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

10/9/2024

1607510

308128

#5.202

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


Cegid Retail Y2 – SalesExternal Plugin

28

Added fiscal version number (NF525)

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

12/1/2025

1975953

438824

#5.546


## SalesReceipt2Get


### ➔   Objectives

This method retrieves the image of an already stored sales receipt by using its key. If only the data has been

stored (the generation having failed previously with SalesReceipt2), the method tries to generate the image.

If the generation fails again, an exception is raised.


### ➔   Improvements

Added the possibility to enter the code of the template to be used.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

10/9/2024

1607510

308128

#5.202

Added the possibility to specify the identifier of the cash register that wants to print the receipt, to benefit

from its settings (template, etc.)

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

2/26/2025

1692171

362933

#5.301

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


## SalesReceipt2FromKey


### ➔   Objectives


Cegid Retail Y2 – SalesExternal Plugin

29

This method formats the sales receipt from its key with a given culture. The printing template is the one

stored in the database for the cash register.

The generated image is a monochrome image.


### ➔   Improvements


### Management of the GetReceipt revisions

Added WithRevision20 and WithRevision21 to the Fields property of the GetReceipt request to obtain the

fields added with revisions 20 and 21 of GetReceipt.

Added the possibility to enter the code of the template to be used.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

10/9/2024

1607510

308128

#5.202

Added the possibility to specify the identifier of the cash register that wants to print the receipt, to benefit

from its settings (template, etc.)

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

2/26/2025

1692171

362933

#5.301

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


## SalesReceiptDuplicate


### ➔   Objectives

This method generates a duplicate receipt from its key.

The generated image is a monochrome image or a PDF.


### ➔   Improvements

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

NAC

3/14/2024

1407019

227545

#5:47 AM


Cegid Retail Y2 – SalesExternal Plugin

30


## GiftReceipt


### ➔   Objectives

This method formats a sales receipt without prices that can be used as an exchange voucher.

The generated image is a monochrome image. In format PNG or PDF.


### ➔   Improvements

Increased the maximum size of the payment transaction identifier from 17 to 40 characters.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/24/2024

1593792

314375

#5.227

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


## CashFloatReceipt


### ➔   Objectives

This method formats a cash float receipt for a given cash register, with a given printing template and with

a given culture

The generated image is a monochrome image.


### ➔   Improvements

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355

Added printing template orientation

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

2/27/2024

1392919

231977

#5:53 AM


Cegid Retail Y2 – SalesExternal Plugin

31

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


## ZReceipt


### ➔   Objectives

This method formats receipt X or Z (depending on whether the cash register has been opened or closed)

for a given cash register, with a given printing template and with a given culture.

The generated image is a monochrome image.


### ➔   Improvements

Added the additional information:

•

Added section DETAIL OF REGISTER OPERATIONS (unconditional, because normally conditioned by

a register setting)

•

Added section TAXES unconditional, see above)

•

Added data to section ADDITIONAL INFORMATION: Number of receipts, Number of items, No. of

items / Receipt, SF / receipt, SF / Item

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

12/11/2024

1647138

331283

#5.253

Added printing template orientation

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

MGA

5/20/2025

1775141

392638

#5.355


Cegid Retail Y2 – SalesExternal Plugin

32


### 6.   O THER


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

1/16/2025

1543349

345170

#5.272


