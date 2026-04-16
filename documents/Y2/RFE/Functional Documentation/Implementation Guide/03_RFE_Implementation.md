# RFE Implementation

*Source: Cegid Retail Y2 RFE - Implementation Guide | Extracted: 2026-02-27*

---


# RFE Implementation


## Introduction

RFE implementation - Introduction

The objective of this section is to know the methodology of implementing RFE on a customer environment as well as to know the settings to be made in Y2 and RFE for a deployment of RFE.

Methodology:


## Provisioning of tenant client

Provisioning of tenant client

The provisioning of customer environments for the use of the RFE component must be carried out by Cegid's SaaS teams.

There are two cases to consider in customer provisioning:

- New SaaS customer: This corresponds to Cegid customers who have subscribed to a Cegid Retail Y2 SaaS offer since 01/05/2023.
- Existing SaaS customer : This corresponds to Cegid customers who subscribed to a Cegid Retail Y2 SaaS offer before 01/05/2023.

In both cases, customer provisioning involves setting up the first administrator user, who will be used to configure RFE.

New SaaS customer.

In this case, the provisioning of the customer's RFE environment, whatever the offer, is automatic. In detail, the ADM user code corresponding to the CEG_ADMIN user created by default in the Y2 template database will also be declared as an administrator user in RFE.

In the case of database migration for certain new SaaS customers (example: OnPremise to SaaS migration), the ADM user code will be created in RFE by default. If this user code does not exist in the migrated Y2 database, it will be necessary to create a user with the ADM code to initiate RFE use via this user.

Existing SaaS customer.

In this case, provisioning must be carried out manually by the Cegid consultant via a request to the SaaS teams.


## Creation of RFE containers

Creation of RFE containers

It is recommended to use the RFE Web App to create containers.

The creation via RFE webservices remains an option. A maximum of up to 50 containers can be created per workspace.

Creating containers via the RFE Web App

The RFE administrator can manage containers with the following characteristics:

- Container ID: To be entered.
- Container name: this name is assigned automatically.
- Contributors: List of containers.
- Key: SAS key generation.
- Pen : Modification (add, delete contributors from container)
- Recycle bin : Delete container

Creation of a container

Container naming rules :

- 20 characters maximum
- No spaces
- Allowed characters : A to Z, a to z, "-".

Procedure

1. From the Containers tab, click on the [Add container] button:
2. Enter the container name in accordance with the naming rules.
3. Contributors can be selected later.
4. Validate.

Modifying a container

1. To modify a container, click on the [Modify] button.
2. Here you can add or remove contributors (see : Managing contributors )

Deleting a container

1. To delete a container, click on the [Delete] button.
2. A message is displayed to confirm (or cancel) deletion of the container:

SAS key generation

This option allows you to generate a temporary key, giving a contributor access to a container.

To generate a SAS key, click the icon that represents a key, and choose one of the 2 options below:

Option 1: Read-only

This option allows for the generation of a SAS key that allows a contributor only to view the files hosted within a container for an alloted period of time.

- Validity period: The validity period must be between 5 minutes and 24 hours.
- Unit: Minutes or hours
- Generate

Please note that the duration of validity is indicated within the SAS key window (top right).

Option 2: Read and write

This option allows for the generation of a SAS key that allows a contributor to view the hosted files and also to upload files onto their designated containers. Please note that the validity period is constant (10 minutes; and this information is indicated in the top right corner of the window).

Creation of containers via Web Services

Run the following web service on the RFE APIs:

See details of the call in swagger documentation.

The client's workspace is required and the permission level is Token Bearer using the token returned by Server Authentication.


## Access rights management

Access rights management

It is recommended to use the RFE Web App to manage access permissions. It is still possible though to manage permissions via RFE web services.

Owner/Admin management

As a reminder, RFE administrators must correspond to Y2 users (preferably Y2 administrators).

Creating administrators via the RFE Web App

The RFE administrator can delegate this role to another Y2 user.

In the Administrators tab, the list of RFE administrators is available.

Click on the [Add an administrator button] to select one.

To delete an RFE administrator, from the list, click on the the [Delete] button, then confirm the deletion of the RFE administrator.

Creation of owners via Web Services

Use the following API:

- The tenantId is the name of the client's tenant.
- The ownerId corresponds to the user code (do not take the user login).
- The authentication method is via the Authentication Server token bearer.

Contributor management

An RFE administrator can assign access rights to one or more containers to a contributor.

It is recommended to create one contributor per RFE Container, in order to secure access to each container,

For greater legibility, it is quite possible to give the same name as the container as a login, which implies creating them beforehand in Y2.

To assign rights to a Container, go to the Containers tab: edit the Container, then add the contributor(s).

Please note that when a Y2 user has no RFE rights (i.e. is neither an RFE administrator nor an RFE contributor), a message informs him/her that access is not authorized.

Creation of contributors via webservices

Use the following API:

- The tenantId is the name of the client's tenant.
- The containerId is the name of the container as created in the previous step.
- The contributorId corresponds to the user code (do not take the user login).
- The authentication method is via the Authentication Server token bearer.


## Y2 settings:

Y2 settings:

Data sources :

Go to the Menu Back-Office > Data exchanges>Data recovery>Settings>Data provenance.

1. Select the data source(s) to modify based on the analysis.
2. In the data source edit the following fields: Input directory: [RetailFileExchangePath]\<Container Id>\in Rejects directory: [RetailFileExchangePath]\<Container Id>\out\Rejets Archive directory: [RetailFileExchangePath]\<Container Id>\in\Archives Log file name: [RETAILFILEEXCHANGEPATH]\<Container Id>\out\LOGS\LOG.TXT

The field Container Id refers to the name of the container set in the chapter on Creating RFE containers.

Please note!

Putting or moving files into the out directory will allow them to be retrieved after processing.

Recommendations:

1. Please set an archive cleaning period of 15 days in data provenances to avoid overload on the task servers:

1. Limit the number of files going through RFE: set folders only as needed (example: Rejects directory).

Reminders

The logs can be viewed in the Y2 event log

Exports

Free exports, Standard exports, Accounting exports:

- The export path must be: [RetailFileExchangePath]\<Container Id>\out\
- The files will be available in the following blob storage directory: - /out

