# RFE Operation

*Source: Cegid Retail Y2 RFE - Implementation Guide | Extracted: 2026-02-27*

---


# RFE Operation


## General operation

General operation

This chapter aims at drawing the schema for general RFE operation as well as the interactions between the Y2 application and the RFE component.

Below is the RFE/Y2 macro operating diagram:

Figure 1 : RFE enables file transfer between Y2 and a client through Azure Blob storage.

Files sent to Y2 must be dropped in the /in directory

Files intended for Y2 must be placed in the /out directory.

Files exported from Y2 must be retrieved in the /out directory

RFE allows for segmenting the data flows via creation of various containers

Below is a more detailed operating diagram:

Figure 2 : Detailed diagram of RFE operation

The diagram above is divided into three parts:

- An external part: Client or partner applications
- An RFE part: Management of the Core RFE and its operation.
- A Y2 part: Management of the different Y2 components (task server, Core Y2, Server Authentication).

Operation of each of these parts is described in the chapters on Client-side operation et Y2-side operation.


## Client-side operation


### Introduction

Client-side operation

Below is the detailed client-side operation of RFE:

Figure 3 : Client-side RFE operating diagram via Automat (script, ETL, or other)

Figure 4 : Manually exchanging files with Azure Storage Explorer.

File exchanges with RFE can be done manually via Azure Storage Explorer software downloadable at: https://azure.microsoft.com/fr-fr/features/storage-explorer/

The connection to the RFE component as well as the file exchanges must go through authentication via a SAS key. In order to recover this SAS key, it is necessary to follow the steps described in Figures 2 and 3.

Below is the description of the steps to transfer files:

1. Webservice call to Authentication Server via a user/password/domain declared in Y2 (no special rights to assign to this user to retrieve the server authentication token).
2. The return of the call of the webservice of step 1 returns a token Bearer in case of success. This token is to be kept for subsequent webservice calls.
3. Webservice call to RFE to generate the SAS key. (This operaiton can be performed via the RFE Web App). The Bearer token retrieved in the previous step must be used in the call parameters.
4. RFE checks the validity of the token sent as a parameter, if successful, then it returns the SAS key that allows you to connect to RFE.
5. This step consists of connecting to RFE using the previously recovered SAS key. The connection can be made via Azure Storage explorer or via the Microsoft AzCopy client or via a programming language library published by Microsoft (see Microsoft documentation). The connection to RFE remains active as long as the SAS key is valid (see SAS key validity period ).
6. This step involves exchanging files with RFE once the connection is established. Exchanges with RFE remain possible as long as the SAS key is valid (see SAS key validity period ).

Please note!

In the case of volume of too large exchanges, it is possible to cache the SAS key on the client side in a secure way.


### Documentation of webservices

Documentation of webservices

Below are the swagger documentation links of the webservices presented in the chapter Client-side operation.

RFE TEST environment Webservices:

SAS key generation

- Versions prior to: https://rfe.cegid.cloud/t/storage/api/swagger/ui
- Version 4.0 and later: https://rfe.cegid.cloud/t/storage/swagger/index.html

Webservices RFE environment PROD:

SAS key generation

- Versions prior to: https://rfe.cegid.cloud/p/storage/api/swagger/ui
- Version 4.0 and later: https://rfe.cegid.cloud/p/storage/swagger/index.html

Webservices AuthenticationServer environment TEST:

Generation of Token Bearer

Refer to the following OpenID documentation: https://developer.okta.com/docs/reference/api/oidc/#token

The Y2 call URL is: https://retail-services.cegid.cloud/t/as/connect/token

Webservices AuthenticationServer environment PROD:

Generation of Token Bearer

Refer to the following OpenID documentation: https://developer.okta.com/docs/reference/api/oidc/#token

The Y2 call URL is: https://retail-services.cegid.cloud/p/as/connect/token

Please note!

Authentication for all RFE Web Services can be performed systematically via TokenBearer retrieved from the Authentication Server.

Below are examples of webservices calls on the POSTMAN software

File name: RFE.postman_collection.json

=> See available content under Annex files.


### How to connect via Azure Storage Explorer:

How to connect via Azure Storage Explorer:

As a reminder, Azure Storage Explorer software allows you to transfer files manually between a client computer and RFE. The software can be downloaded from the following address:

https://azure.microsoft.com/fr-fr/features/storage-explorer/

The connection to RFE can only be done via a SAS key obtained via the getsastoken function of the RFE storage webservice (or the RFE WebApp).

This webservice returns three fields that should be used to connect to RFE:

- blobServiceUri
- containerName
- sasToken

Below is the step-by-step procedure to connect to RFE via Azure Blob Storage:

Procedure

1. Open Azure Storage Explorer software from the Start menu:

1. Create a new storage account:

1. Choose the Blob container option.

1. Choose the Shared Access Signature (SAS) URL connection method

1. Concatenate the 3 fields that form the container URL in the Blob container SAS URL field.
2. The display name will be replaced automatically with the containerName.
3. Click Next .

1. Click Connect .
2. The container appears in the list of Blob Containers via its containerName:

1. 4.Navigating in Azure Storage Explorer:

- Navigate into virtual directories:

1. Double click on a directory to go there.

- Upload a file:

PLEASE NOTE ! The files must be loaded in the “in” folder (small letters) If they are loaded in another folder, they cannot be processed by RFE

- Download a file:


## Y2-side operation

Y2-side operation

Figure 5 : RFE/Y2 operating diagram

The operation on the Y2 side is to be broken down into 2 parts:

1. Importing files into Y2 : In this case, the files are dropped by the client into the /in directory. The runner on the RFE side runs every minute to transfer any new files in the /in directory of the Blob Storage to the corresponding directory on the Y2 task server (this for each container of a client).
2. Exporting files from Y2 : A FileWatcher Agent scans the task server and detects any new files to send to RFE. If a new file is generated on the task server, the FileWatcher agent sends a message to the RFE queue. This RFE queue manages the message stack of FileWatcher agents and triggers a job for the runner to order him to move the files from the task server to RFE.


## Managing RFE access permissions and containers

Managing RFE access permissions and containers

RFE offers access rights management by container. This is to secure container access to certain users declared in Y2.

This management of access rights involves two user profiles: owners and contributors.

Owner:

- He/she is defined at the tenant level
- He/she can manage the owners of the tenant (creation, deletion)
- He/she can manage containers (creation, deletion, assignment of permissions to contributors)
- He/she can list containers
- He/she can generate a SAS key on any container

Contributor:

- He/she is defined at the level of the container(s)
- He/she can list containers for which he/she is set as contributor.
- He/she can generate a SAS key for containers for which he/she has access in order to view their contents, drop off or retrieve files.

Please note!

When provisioning a tenant with RFE, a first owner must be created. (See Provisioning tenant client)

Below is the schema representation of the concept of “Owner” and “Contirbutor”

RFE offers container management to segment the different customer flows.

This management only allows you to create/delete containers on the RFE side. The corresponding directories on the task server are created automatically by the scheduled tasks when they are first run on the path set up in Y2 (data provenance or export format).

Administrators (owners) and contributors (creation/deletion) are managed either via the RFE web app, or via webservice calls.

Webservices documentation is available here:

- For TEST environments: Versions prior to 4.0: https://rfe.cegid.cloud/t/storage/api/swagger/ui Version 4.0 and later: https://rfe.cegid.cloud/t/storage/swagger/index.html
- For PROD environments: Versions prior to 4.0: https://rfe.cegid.cloud/p/storage/api/swagger/ui Version 4.0 and later: https://rfe.cegid.cloud/p/storage/swagger/index.html

Access rights management is contained in the "Rights management" block:

The following webservices are used to create or delete an owner via the PUT or DELETE methods:

The following webservices are used to create or delete a contributor via the PUT or DELETE methods:

PLEASE NOTE !

Only an RFE administrator can create contributors for a container. The first RFE administrator must therefore be pre-created by Cegid's Cloud teams.

Below is an example of a POSTMAN collection containing calls to these webservices:

File name: RFE.postman_collection.json

=> See available content under Annex files.

Access rights management is contained in the Container management block:

- RFE Webservice PROD environment: https://rfe.cegid.cloud/p/storage/api/swagger/ui https://rfe.cegid.cloud/p/storage/api/swagger/ui

- The containers GET function allows you to list all containers for a Y2 domain GET function
- The POST containers function allows you to create a container for a Y2 domain the POST function
- The DELETE containers function allows you to delete a container for a Y2 domain the POST function

