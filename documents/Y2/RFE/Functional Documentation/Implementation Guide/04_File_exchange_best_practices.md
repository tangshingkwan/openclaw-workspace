# File exchange best practices

*Source: Cegid Retail Y2 RFE - Implementation Guide | Extracted: 2026-02-27*

---


# File exchange best practices

File exchange best practices

The objective of this section is to recall the best practices in terms of file exchange and in particular on the management of planned tasks.

Y2 scheduled tasks:

For scheduled tasks, please refer to the P300 Task Scheduler procedure.

Summary of limitations and best practices


| Type | Description |
| --- | --- |
| File/folder naming | Containers are case-sensitive. The files must be loaded in the “in” folder, small letters and avoiding the following characters \ / : * ? " < > | %. The API calls must also observe the small letter case of the “in” folder. Files placed outside the “in” folder cannot be processed by RFE. |
| Time/date stamping of files | In order for your files to be processed correctly, it is strongly recommended to integrate time and date information into the names of the files. |
| File replacement | In case of the need to replace a file that has just been placed into a container, it is recommended to delete this file before placing another one with the same name. This is to ensure that the new file will be properly taken into account. A file with the same name as a file that has already been transferred will be: Processed successfully by RFE if it has already been integrated into the Cegid application, Rejected by RFE if it is still present on the Cegid server, as it will be detected as already existing. |
| Number of files per minute | For transfer times <2 min (files from 10 to 100 MB) for all clients: SaaS Dedicated: max 100 files per minute SaaS Advanced: max 3 files per minute |
| Time range | A maintenance time frame is defined from 01:00 AM to 03:00 AM (POD Local Time). During this period, servers may be unavailable, and no Y2 jobs will be run for 60 minutes. |
| File size | Files larger than 1GB are not processed. In the Client => Cegid direction, files remain in the IN directory. It is recommended to group information in files (avoid, for example, having a file for a single record). |
| Number of pending jobs | The number of files waiting to be transferred (sum of transfers in both directions) is limited to 10,000 files. Beyond 10,000 files, a "429 - Too Many Requests" error is returned by the GetSasToken service, no new SAS key will be assigned to the contributor and he/she won't be able to upload a new file until the number of files drops below 10,000. As soon as the number of waiting files falls below 10,000, it is possible to deposit a new file. |
| Retention time on blob storage | Minimum 7 days This applies to all directories, including archives |
| Token Bearer validity time | 60 min |
| SAS key validity time | Read: max 24h Read/write: max 10 min The choice of SAS "Read" or "Read/Write" key type is made when the key is created. |
| Connection | It is recommended to avoid untimely connections (maximum every 5 minutes). If you need to transfer files beyond this frequency, you need to use a cache system for the TokenBearer and SAS keys generated, in order to transfer the batch of files during the period of validity of the SAS key. This caching system must be managed on the client IS side. |
| API consumption | Users may need to use a correlation identifier, which they can transmit to RFE by adding an http header x-correlation-id. Example: PUT https://urlrfe/mytenant/RFE/V1/owners/anyuser Authorization: Bearer ************************* x-correlation-id : 79534c53-a169-457f-ace1-f498c37ae6df Content-Type: application/json If this identifier is not entered, it is automatically assigned by RFE. If it is, RFE retains the identifier supplied. PLEASE NOTE ! If it is, it must be different for each request. As recommended by Microsoft : https://microsoft.github.io/code-with-engineering-playbook/observability/correlation-id/ |

