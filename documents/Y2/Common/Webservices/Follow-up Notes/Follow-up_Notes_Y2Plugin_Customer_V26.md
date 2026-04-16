# Follow-up Notes Y2Plugin Customer V26

*Source: Follow-up_Notes_Y2Plugin_Customer_V26.pdf | Extracted: 2026-02-27*

---


## Customer Plugin V06


## Cegid Retail Y2 –  Version 26


## Follow-up Notes


## Make more


## possible

Registration date:   20 February 2026


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid Retail Y2 – Customer Plugin

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


Cegid Retail Y2 – Customer Plugin

3


## Contents

Preamble  ........................................................................................................................................................................................... 2

1.   OBJECTIVES  ................................................................................................................................................................................ 4

Documentation  ............................................................................................................................................................................... 4

Y2 versions  ...................................................................................................................................................................................... 5

2.   OFFICIAL DOCUMENTS  ......................................................................................................................................................... 6

GetList  ................................................................................................................................................................................................ 6

3.   TRIGGERS  ..................................................................................................................................................................................... 7

Evaluate  ............................................................................................................................................................................................. 7

4.   MANAGEMENT  ............................................................................................................................................................................ 8

GetDetail  ........................................................................................................................................................................................... 8

GetListDetail  ..................................................................................................................................................................................10

Create  ...............................................................................................................................................................................................11

Update  ..............................................................................................................................................................................................14

5.   ANONYMIZATION  .................................................................................................................................................................... 17

Anonymize  ......................................................................................................................................................................................17

BatchAnonymize  ..........................................................................................................................................................................17

6.   ADDRESSES  .............................................................................................................................................................................. 19

GetListDetail  ..................................................................................................................................................................................19

GetDetail  .........................................................................................................................................................................................19

Create  ...............................................................................................................................................................................................20

Update  ..............................................................................................................................................................................................21

Delete  ...............................................................................................................................................................................................23

7.   OFFICIAL DOCUMENTS 2  .................................................................................................................................................. 24

GetDetail  .........................................................................................................................................................................................24

GetListDetail  ..................................................................................................................................................................................24

CreateOrUpdate  ...........................................................................................................................................................................25

Delete  ...............................................................................................................................................................................................26

8.   OTHER  .......................................................................................................................................................................................... 27

Net Framework 4.8  .....................................................................................................................................................................27


Cegid Retail Y2 – Customer Plugin

4


### 1.   O BJECTIVES

The objective of the  Customer  plugin is to offer services relating to customer management.

This version enables you to manage services for retrieving a customer's official documents and addresses,

as well as certain setup elements (user-defined tables, triggers, etc.)

The Management service offers methods designed to gradually replace the Core Customer and

CustomerWcf services written in older technologies.

Just remind: Only public methods for which the contract is published can be used by applications not

designed by Cegid. Cegid reserves the right to modify private services without ensuring backward

compatibility, and without informing users.


## Documentation

The service contract documentation is visible on the IIS server(s) from the software package download

page:

"Documentation" is a link that provides access to the list of documentation:

➔   Web Services

The screen displayed provides access to the Web Services contracts and their properties


![Figure 4](./images/img_0004.png)


![Figure 5](./images/img_0005.png)


Cegid Retail Y2 – Customer Plugin

5

Please note: the absence of a contract in the Web Services documentation screen means that the

service is not installed or is not public.

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


Cegid Retail Y2 – Customer Plugin

6


### 2.   O FFICIAL  D OCUMENTS


## GetList


### ➔   Objectives

This method recovers the list of all official documents of a customer, including those that are closed.


Cegid Retail Y2 – Customer Plugin

7


### 3.   T RIGGERS


## Evaluate


### ➔   Objectives

This method evaluates whether a customer meets the conditions of the trigger.


### ➔   Improvements

Implementation of the method.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PCH

12/3/2021

A2278

95174

#3:26 AM


Cegid Retail Y2 – Customer Plugin

8


### 4.   M ANAGEMENT

Customers and prospects are managed by Cegid Retail Y2 with a lot of information. A customer record is

populated through tabs:

-

General

-

Additions

-

Conditions

-

Payments

-

Information

-

User fields

The toolbar allows you to enter additional information:

➔   The [Zoom menu] button gives access to Outstanding amounts, Transaction history, Loyalty cards,

List of items, Pricing, and Document summary.

➔   The [Complementary data] button gives access to Classifications Exceptions, Address

management, Referencing, Additional identifiers, etc.

➔   The [Contacts] button allows you to register contacts with the customer.

➔   The [BAID] button allows you to register the customer's bank account details.

➔   The [Memos] button allows you to associate photos or memos with the customer's file.


## GetDetail


### ➔   Objectives

This method returns the detail of a customer, or of a prospect called by their external reference identifier.

A part of customer data is returned by this method, with more or less information depending on the tags

present in the “Fields” property.

The following tags are available:

-

Addres s: Returns the customer’s main address

-

Communication : Returns the fields concerning the communication, except the address, with the

confidentiality of this information

-

Identification : Returns the various codes or identifications of the customer

-

Informations : Returns the general data from the customer record

-

SystemFields : Returns the system fields of the customer record

-

UserDefinedFields : Returns the user-defined fields of the customer record

-

UserFields : Returns the user fields of the customer record

This method will be gradually enriched.

The following business rules are applied:

➔   The "Id" property is mandatory. In case of external identifier, Id must be prefixed with "EXT-"

The search is performed on the exact value transmitted. If the code is unknown, an exception is

raised.

➔   If the 'Individual' tag is present in the reply, the returned customer is of type Individual. If the tag

'Company' is present, it is a customer of type Company.


Cegid Retail Y2 – Customer Plugin

9

➔   The customer searched for must respect the user's restrictions on the customer file, otherwise an

exception is thrown.

➔   Loyalty cards are not returned in this method. They are taken into account by the

LoyaltyEngineLoyaltyEngine service, GetCardInfo method.

➔   Similarly, official documents are not returned by this method. The CustomerOfficialDocuments

service will be upgraded to take them into account


### ➔   Improvements

Implementation of the method

Increased the maximum size of the city and address lines to 70 characters

Addition of the 4th address line

The method is now set to the Beta status

Checking the length of the internal identifier provided.

The  method is now set to the Released status

Added the Closing date to the reply

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/12/2024

PBI: 1317597

216523

#4.391

Replacement of 'VAT liability': property VatPayability (Alphanumeric) replaced by VatLiability (List of

values)

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/27/2024

PBI: 1393010

231775

#4.442

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

7/26/2022

A2357

126317

#3.110

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/27/2021

A2351

137815

#4.4

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

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

151073

#4.102

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

4/27/2023

166811

#4.181

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

10


## GetListDetail


### ➔   Objectives

This method returns the details of a list of customers or prospects meeting the request criteria.

A part of customer data is returned by this method, with more or less information depending on the tags

present in the “Fields” property.

The following tags are available:

-

Addres s: Returns the customer’s main address

-

Communication : Returns the fields concerning the communication, except the address, with the

confidentiality of this information

-

Identification : Returns the various codes or identifications of the customer

-

Informations : Returns the general data from the customer record

-

SystemFields : Returns the system fields of the customer record

-

UserDefinedFields : Returns the user-defined fields of the customer record

-

UserFields : Returns the user fields of the customer record

This method will be gradually enriched.

The following business rules are applied:

-

PhoneNumber: Corresponds to the phone presence in the request through one of the following

three fields T_TELEPHONE / T_FAX / T_TELEX (or).

-

Email: Corresponds to the email presence in the request through one of the following fields

T_EMAIL / T_EMAIL2 (or).

-

Name: Corresponds to the presence of the name or company name in the request through one of

the following fields  T_LIBELLE / T_NOM2 (or).

-

FirstName: Corresponds to the presence of the first name or addition to the company name in the

request through one of the following fields T_PRENOM, T_PRENOM2 (or).

-

Individual:  If true, you'll get the Individual tag and not the Company one. If false you'll get the

Company tag and not Individual one. Moreover, if the property is not present in the request,

either one or the other tag will be returned depending on the Third Party.

-

User restriction: The user's customer restrictions are applied to the affiliated store. Customers

whose affiliated store is not allowed for the user are not returned.


### ➔   Improvements

Implementation of the method

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

8/4/2023

A2357

183128

#4.302

The method is now set to the Beta status

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

203085

#4.368


Cegid Retail Y2 – Customer Plugin

11

The error “you must provide a maximum of 1 piece(s) of information from among: ExternalReferences, Ids.”

occurred systematically when searching for customers in the case of a REST call. Problem fixed.

Added the Closing date to the reply

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/12/2024

PBI: 1317597

216523

#4.391

Replacement of 'VAT liability': property VatPayability (Alphanumeric) replaced by VatLiability (List of

values)

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/27/2024

PBI: 1393010

231775

#4.442

The  method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

ADU

2/4/2025

A2508

352496

#4.654


## Create


### ➔   Objectives

This method is used to create a customer or a prospect.

Some data is updated during this creation. This data can be found in different sections in the contract

-

Individual: Information about a customer of type Individual

-

Company: Information about a customer of type Company

-

Address: Customer’s main address

-

Identification: Various codes or identifications of the customer

-

Informations: General data from the customer record

-

UserDefinedFields: User-defined fields from the customer record

This method will be gradually enriched.

The following business rules are applied:

➔   Identifiers

o

If no identifier is specified in the contract, it is assigned automatically. An exception is raised

if the store does not manage the automatic assignment of the customer code.

o

If an identifier is specified and corresponds to an existing customer, the following

information is checked:  Last name - First name - Store of creation and use - zip code - City

- 3 E-mails - 3 phones - External reference

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

EPL

11/29/2023

1326289

205494

#4.371


Cegid Retail Y2 – Customer Plugin

12

▪

If at least one piece of information is different, it is not possible to create 2 different

customers with the same Identifier, an exception is raised.

▪

If all pieces of information are identical, the service considers that there is a case

of idempotency (double call of the creation service of the same customer). No

exception is raised, the customer is not updated, and the value false is returned in

the "CustomerCreated" property.

➔   Store of creation/affiliation

o

The customer’s stores of creation and affiliation must be identified by their code or their

external reference, and must respect the user’s restriction on customers.

No existence control is performed, and it is up to the caller to provide the correct

information.

➔   Identification

o

The EANCode must not already exist for another customer.

o

The municipal registration number, regional registration number and CPF/CNPJ codes must

not already exist for another customer.

➔   Information

o

The paying customers, customers to be delivered, and customers to be invoiced must be

identified by their code or their external reference, and must exist in the database.

➔   Individual/Company customer

o

One and only one of these 2 tags is mandatory and allows you to indicate whether it is an

individual or a company

o

Individual:

▪

LastName is mandatory

▪

BirthDayDate:

-

The day (Day) must be between 1 and 31.

-

The month (Month) must be between 1 and 12

-

The year (Year) must be greater than 1900

-

If all 3 fields are filled in, the date must be consistent.

-

If only the day and month are filled in, the year will automatically be 1900.

o

Company:

o

Name is mandatory

➔   E-mail

o

Each e-mail must be in format  xxx@yyy.zzz

o

Privacy and validity information must be specified for every e-mail sent.

o

Emailing and EmailRecovery must only be specified in the contract if at least one e-mail is

specified

➔   Address

o

The zip code (ZipCode), the city (City), and the country (CountryId) must be consistent with

each other.

➔   Confidentiality

o

Values should be specified for each piece of information; they are not optional.

o

The management level of privacy is defined in Y2 according to a company setting (global,

per channel or for each piece of information.) The values transmitted in the contract  must

be consistent with the setup.

▪

Global: All Optins must be the same.

▪

By Distribution channel: The Phones Optins must be the same, and the Email Optins

must be the same.

▪

For each piece of information: Each Optin can be different


Cegid Retail Y2 – Customer Plugin

13


### ➔   Improvements

Implementation of the method

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

ADU

4/7/2023

A2357

132683 to

163916

#4.150

Increased the maximum size of the city and address lines to 70 characters

Addition of the 4th address line

Added notification and event log management when creating a customer or prospect.

The method is now set to the Beta status

City and zip code (City and ZipCode) are now optional

Added 'VAT liability' to  'Informations': VatLiability property (List of values)

Added in Property identification: Municipal Registration no. (MunicipaleRegistration), Regional

Registration no. (RegionaleRegistration) and CPF / CNPJ Code (CpfCnpjCode)

-

Municipal and regional registration numbers can only be entered for  corporate customers.

-

CPF expected on 11 digits for a private customer, with key control.

-

CNPJ expected on 14 digits for a corporate customer, with key control.

Added user fields (UserFields)

Added Salespeople (Salespersons)

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/27/2024

PBI: 1391598,

1393010, 1393575,

1391591

231775

#4.442

The  method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb

Ref.

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

RLO

10/27/2022

A2351

137815

#4.4

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

6/16/2023

A2357

174532

#4.215

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

14

ADU

2/4/2025

A2508

352496

#4.654

Language and Nationality identifiers are now optional.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/7/2025

1708914

354885

#4.656

Fixed the algorithm for assigning the T_AUXILIAIRE counter, when the number of characters for the

auxiliary is smaller than that for the Third Party.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

PLA

6/24/2025

1815990

INC0225160

399597

#4.723


## Update


### ➔   Objectives

This method is used to modify a customer or a prospect.

It must be identified in the Id tag, by its internal identifier or by its external identifier preceded by 'EXT-'.

This data can be found in different sections in the contract:

-

Individual: Information about a customer of type Individual

-

Company: Information about a customer of type Company

-

Address: Customer’s main address

-

Identification: Various codes or identifications of the customer

-

Informations: General data from the customer record

-

UserDefinedFields: User-defined fields from the customer record

This method will be gradually enriched.

General update principle:

-

A property not transmitted in the contract is not modified.

-

A property present in the contract is updated with the transmitted value, after a consistency check

against other data.

-

An empty value on a property indicates that the field is reset to blank in the database.

-

Please note that all data in the updated customer record are checked again before being stored in

the database, including those not transmitted. An error on non-updated data may therefore be

reported during the update.

Example: I am changing my customer’s e-mail address, but the sales representative associated with

this customer has been deleted from the database. An error of type “Sales representative does not

exist” will be raised during the update.

Please note that the customer type cannot be changed using this method (Individual     → Company); the

customer must be deleted and the recreated.

The business rules applied are the same as for creation.


Cegid Retail Y2 – Customer Plugin

15


### ➔   Improvements

Implementation of the method.

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

6/6/2023

A2357

173075

#4.198

Increased the maximum size of the city and address lines to 70 characters

Addition of the 4th address line

Added notification and event log management when updating a customer or prospect.

The method is now set to the Beta status

Fixes error “Exception - Cegid.Retail.Tools.Resources.Biz001Exception: (1) input data not valid. -The Id field

is required. ” that occurred when updating a customer without an associated language.

Dev

Date

CEGID’s Ref.

Pb Ref.

PR

Plugin Build no.

Quality Ctrl

EPL

12/22/2023

1349425

211544

#4.381

Added the update of the Closing date in relation to the ‘Closed’ tag: If 'Closed' becomes true, the closing

date is updated with the current date. If it becomes false, it is set to empty (1900-01-01).

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

1/12/2024

PBI: 1317597

216523

#4.391

City and zip code (City and ZipCode) are now optional

Added 'VAT liability' to  'Informations': VatLiability property (List of values)

Added in Property identification: Municipal Registration no. (MunicipaleRegistration), Regional

Registration no. (RegionaleRegistration) and CPF / CNPJ Code (CpfCnpjCode)

-

Municipal and regional registration numbers can only be entered for  corporate customers.

-

CPF expected on 11 digits for a private customer, with key control.

-

CNPJ expected on 14 digits for a corporate customer, with key control.

Added user fields (UserFields)

Added Salespeople (Salespersons)

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/27/2021

A2351

137815

#4.4

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

6/16/2023

A2357

174532

#4.215

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

203085

#4.368


Cegid Retail Y2 – Customer Plugin

16

For all these new properties: the tag can be assigned an empty value to clear the information in the

customer record.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/27/2024

PBI: 1391598,

1393010, 1393575,

1391591

231775

#4.442

The  method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/4/2025

A2508

352496

#4.654

Language and Nationality identifiers are now optional.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

2/7/2025

1708914

354885

#4.656

UserDefinedTables could not be reset to empty. It is now possible to put the table rank in the Id, and

enter “” in Value to reset the table value to empty.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

ADU

11/20/2025

2004264

435918

#5:26 AM


Cegid Retail Y2 – Customer Plugin

17


### 5.   A NONYMIZATION

This service anonymizes customer data.


## Anonymize


### ➔   Objectives

This method is used to anonymize customer data.

It is not possible to anonymize customer data in the following cases:

➔   Clothing allowances were granted to one of the customers

➔   There are outstanding payments for one of the customers

Anonymization is subject to the user right “Anonymization” (menu 26).


### ➔   Improvements

Implementation of the  method .


## BatchAnonymize


### ➔   Objectives

This method anonymizes data for a list of customers.

It is not possible to anonymize customer data in the following cases:

➔   Clothing allowances  were granted to this customer

➔   There are outstanding payments for this customer

➔   One of the customers does not exist in the database

Anonymization is subject to the user right “Anonymization” (menu 26).


### ➔   Improvements

Implementation of the method.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

SBU

4/12/2024

248093

#4.521

Dev

Date

CEGID’s Ref.

Pb Ref. Pull request

Plugin Build no.

Quality Ctrl

SBU

4/12/2024

248093

#4.521


Cegid Retail Y2 – Customer Plugin

18


Cegid Retail Y2 – Customer Plugin

19


### 6.   ADDRESSES

This service is used to manage customers’ additional addresses.


## GetListDetail


### ➔   Objectives

This method returns the details of a customer’s additional addresses, called by their external reference

identifier.

The following business rules are applied:

➔   The "Id" property is mandatory.

It allows the customer to be found from their internal code or external reference.

In case of an external identifier, the latter must be prefixed with "EXT-"

The search is performed on the exact value transmitted.

➔   In the reply, only one of the two tags "Individual" and "Company" is present, to show whether the

address is that of an individual customer or of a company.


### ➔   Improvements

Implementation of the  method .

Addition of the 4th address line

The  method is now set to the Released status


## GetDetail


### ➔   Objectives

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

JMO

10/11/2022

A2346

134740

#3.182

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

20

This method returns the details of a customer’s additional addresses, called by their external reference

identifier.

The following business rules are applied:

➔   The "CustomerID" and "AddressNumber" properties are mandatory.

➔   The “CustomerID” property allows the customer to be found from their internal code or external

reference.

In case of an external identifier, The "Id" property is be prefixed with "EXT-"

The search is performed on the exact value transmitted.

➔   An exception is also raised, if the transmitted address number does not exist for the customer.

➔   In the reply, only one of the two tags "Individual" and "Company" is present, to show whether the

address is that of an individual customer or of a company.


### ➔   Improvements

Implementation of the method.

Addition of the 4th address line

The  method is now set to the Released status


## Create


### ➔   Objectives

This method is used to create an additional address for a customer.

The following business rules are applied:

➔   The “CustomerID” property allows the customer to be found from their internal code or external

reference.

In case of an external identifier, the latter must be prefixed with "EXT-"

The tag is checked against the exact value transmitted.

➔   The “Individual” tag must be present if the customer of the address is of a Type “Individual”.

Dev

Date

CEGID’s Ref.

Pb Ref. Pull request

Plugin Build no.

Quality Ctrl

JMO

10/11/2022

A2346

134740

#3.182

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

21

➔   The “Company” tag must be present if the customer of the address is of type “Company”.

➔   An error is raised in the following cases:

•

The Customer does not exist

•

The internal reference exceeds 17 characters

•

Unknown carriage conditions

•

Unknown shipping method

•

Unknown place of departure of goods

•

Unknown title (if the "Individual" tag is present)

•

Unknown legal form (if the "Company" tag is present)

•

The country does not exist

•

The region does not exist

•

The zip code does not exist

•

Unknown barcode for the country

•

Inconsistent address line numbering


### ➔   Improvements

Implementation of the method.

Increased the maximum size of the city and address lines to 70 characters

Addition of the 4th address line

The  method is now set to the Released status


## Update


### ➔   Objectives

This method allows you to update an additional address for a customer.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

JMO

10/11/2022

A2346

134740

#3.182

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

10/27/2021

A2351

137815

#4.4

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

22

This method does not work in "CANCEL-REPLACE" context; only the data specified in the contract is

updated.

-

A property not transmitted in the contract is not modified.

-

Properties specified in the contract are  updated with the transmitted value, after a consistency

check against other data.

-

An empty value on a property indicates that the field is reset to blank in the database.

The following business rules are applied:

➔   The "CustomerID" and "AddressNumber" properties are mandatory.

➔   The “CustomerID” property allows the customer to be found from their internal code or external

reference.

In case of an external identifier, The "Id" property is be prefixed with "EXT-"

The tag is checked against the exact value transmitted.

➔   An error is raised in case of a non-existent customer, called by their internal or external

reference.

➔   An exception is also raised if the transmitted address number does not exist for the customer.

➔   The “Individual” tag can be present if the customer of the address is of type “Individual”.

➔   The “Company” tag can be present if the customer of the address is of type “Company”.

The business rules applied are the same as for creation.


### ➔   Improvements

Implementation of the method.

Increased the maximum size of the city and address lines to 70 characters

Addition of the 4th address line

The  method is now set to the Released status

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

JMO

10/24/2022

A2346

136828

#3.200

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

RLO

10/27/2021

A2351

137815

#4.4

Dev

Date

CEGID’s Ref.

Pb Ref.

Pull request

Plugin Build no.

Quality Ctrl

RLO

11/5/2022

A2351

138888

#4:21 AM

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

23


## Delete


### ➔   Objectives

This method allows you to delete a customer’s additional address, called by its identifier or external

reference.

The following business rules are applied:

➔   The "CustomerID" and "AddressNumber" properties are mandatory.

➔   The “CustomerID” property allows the customer to be found from their internal code or external

reference.

In case of an external identifier, The "Id" property is be prefixed with "EXT-"

The tag is checked against the exact value transmitted.

➔   An error is raised in case of a non-existent customer, called by their internal or external

reference.


### ➔   Improvements

Implementation of the method.

The  method is now set to the Released status

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

JMO

10/11/2022

A2346

134740

#3.182

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

LDE

7/12/2023

A2452

179260

#4.275


Cegid Retail Y2 – Customer Plugin

24


### 7.     OFFICIAL   DOCUMENTS   2

This service allows you to manage  official documents for customers and prospects  (passports, ID cards,

driver's licenses, etc.).


## GetDetail


### ➔   Objectives

This method returns the  details of an official document  linked to a customer or prospect, identified by

its internal ID or external reference.

The following business rules are applied:

➔   The  CustomerId  and  Id  properties are mandatory.

➔   The  CustomerId  is used to identify the customer:

o

either by internal identifier,

o

or by external reference, prefixed by  EXT -.

➔   The customer must exist.

➔   The official document sought must exist for the customer.

➔   The customer must be authorized.

➔   System fields (SystemFields)  are only returned if explicitly requested via the Fields parameter.

➔   The returned document contains:

o

Document rank,

o

the type and identifier of the document,

o

the issuing institution,

o

the issue and expiration dates,

o

the Closed status,

o

comments,

o

optional system fields.


## GetListDetail


### ➔   Objectives

This method returns a  detailed list of official documents  for a customer or prospect.

The following business rules are applied:

➔   The  CustomerId  property is mandatory.

➔   The customer can be identified by internal ID or external reference.

➔    Documents can be filtered by:

o

document type,

o

Closed  status,

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

SBE

12/3/2025

1990718

437649

#5:38 AM


Cegid Retail Y2 – Customer Plugin

25

o

Validity date.

➔   Documents are returned  sorted in descending order.

➔   System fields  are only returned if requested.

➔   The customer must exist and be authorized.

➔   If there are missing documents matching the criteria, the method returns an  empty list.

➔   No pagination is applied.


## CreateOrUpdate


### ➔   Objectives

This method thus allows you to create or update an official document linked to a customer or prospect.

The following business rules are applied:

➔   The  CustomerId  and  Id  and  DocumentTypeId  properties are mandatory.

➔   The customer must exist and be authorized.

➔   If the document exists:

o

it is updated,

o

The call is idempotent if the data is identical.

➔   If the document does not exist:

o

it is created.

➔   Rank  management:

Insertion case:

-If the Rank field is not filled in:

-The document is inserted with a rank calculated automatically equal to the

maximum existing rank + 1.

-No other documents are modified.

-If the Rank field is filled in:

If the rank provided is not already in use:

The document is inserted with the rank provided, without modifying the other

documents.

If the rank provided is already in use:

The document is inserted at the requested rank.

All existing documents with a rank greater than or equal to this rank

are incremented by +1 in order to preserve the uniqueness and order of the ranks.

Dev

Date

CEGID’s

Ref.

Pb Ref.

Pull request

Plugin Build

no.

Quality Ctrl

SBE

12/3/2025

1990718

437649

#5:38 AM


Cegid Retail Y2 – Customer Plugin

26

Update case:

-If the Rank field is not filled in:

No change is made to the rank.

-If the Rank field is filled in:

If the target rank does not exist:

The rank of the document is updated with the value provided, without impacting

other documents.

If the target rank already exists:

The document is moved to the requested rank.

Other documents with a rank  greater than or equal  to this rank are  incremented

by +1  to ensure consistency in the order.

➔   Default dates are applied if not specified.

➔   The end of validity date must be later than or equal to the beginning date.

➔   The document type must exist.

➔   The  T_PASSEPORT  field in the customer file is kept up to date for Passport-type documents:

o

Creation,

o

Modification,

o

Closing.

➔   The active passport retained is the one  with the highest rank that is not closed.

➔   The existence of the store is not checked.


## Delete


### ➔   Objectives

This method allows you to  delete an official document  linked to a customer or prospect.

The following business rules are applied:

➔   The  CustomerId  and  Id  properties are mandatory.

➔   The customer must exist and be authorized.

➔   If a Passport type document is deleted:

o

if the deleted passport is the one in the customer file,

it is replaced by the highest-ranking passport that has not been closed,

or reset to empty if it no longer exists.

➔   No error is raised if the document no longer exists.

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

SBE

1/16/2026

1990718

446738

#5.69

Dev

Date

CEGID’s Ref.

Pb

Ref.

Pull request

Plugin Build no.

Quality Ctrl

SBE

1/16/2026

1990718

446738

#5.69


Cegid Retail Y2 – Customer Plugin

27


### 8.   O THER


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

1/13/2025

1543349

341752

#3.648


