# Version Tracking

*Source: Version_Tracking.pdf | Extracted: 2026-02-27*

---


## Cegid Retail File Exchange (RFE)


## Release Note


![Figure 1](./images/img_0001.jpeg)


![Figure 2](./images/img_0002.png)


Cegid

2


## Introduction

This document describes various upgrades to the modules of Retail File Exchange (RFE).

Legal Notice

Permission is hereby granted to download Cegid documents and to use information within for

internal purposes only, providing that: (a) the copyright statement remains on all copies of the

material; (b) the documents are used for personal purposes and not commercial ones, unless

explicitly stated by Cegid that certain specific items may be used for commercial purposes;(c)

the documents shall not be copied to networked computers, nor published on any type of

media unless explicit permission to do so has been granted by Cegid; and (d) no modifications

shall be made to these documents.


![Figure 3](./images/img_0003.png)


Cegid

3


### Contents

Introduction  .................................................................................................................................................................. 2

Version 4.1 – December 2025  ...................................................................................................... 5

RFE Core – Version 4.1.174  ................................................................................................................................ 5

RFE WebApp – Version 4.1.10  ........................................................................................................................... 5

Version 4.0 – November 2025  ...................................................................................................... 5

RFE WebApp – Version 1.0.171  ........................................................................................................................ 5

Version 4.0 – September 2025  ..................................................................................................... 5

RFE Core – Version 4.0.369  ................................................................................................................................ 5

RFE WebApp – Version 1.0.117  ........................................................................................................................ 5

Version 3.1 – July 2025  ................................................................................................................ 5

RFE Core – Version 3.0.430  ................................................................................................................................ 5

RFE WebApp – Version 1.0.113  ........................................................................................................................ 6

Version 3.0 – April 2025  ............................................................................................................... 6

RFE Core – Version 3.0.315  ................................................................................................................................ 6

RFE WebApp – Version 1.0.97  ........................................................................................................................... 6

Version 2.3 – December 2024  ...................................................................................................... 6

RFE WebApp – Version 1.0.88  ........................................................................................................................... 6

Version 2.2 – April 2024  ............................................................................................................... 6

RFE Core – Version 2.1.1421  ............................................................................................................................. 6

RFE WebApp – Version 1.0.59  ........................................................................................................................... 6

Version 2.1 – February 2024  ........................................................................................................ 7

RFE WebApp – Version 1.0.36  ........................................................................................................................... 7


Cegid

4

Version 2.0 – December 2023  ...................................................................................................... 7

RFE WebApp – Version 1.0.25  ........................................................................................................................... 7

Version 2.0 – October 2023  .......................................................................................................... 7

RFE Core – Version 2.1.432  ................................................................................................................................ 7

RFE WebApp – Version 1.0.17  ........................................................................................................................... 7

Version 1.1 – June 2023  ............................................................................................................... 8

RFE WebApp – Version 0.0.139  ........................................................................................................................ 8

Version 1.0 – October 2022  .......................................................................................................... 8

RFE Core – Version 1.0.1162  ............................................................................................................................. 8


Cegid

5


## Version 4.1 – December 2025

•

Technical upgrades and security enhancements

•

Technical upgrades and security enhancements

•

Increased maximum number of containers per workspace to 50


## Version 4.0 – November 2025

•

Security fix


## Version 4.0 – September 2025

•

Change of the webservices documentation URLs

o   For TEST:  https://rfe.cegid.cloud/t/storage/swagger/index.html

o   For PRODUCTION:  https://rfe.cegid.cloud/p/storage/swagger/index.html

•

On the container side, moved rejected files into the folder archive/rejected

•

Technical optimizations and general improvements.

•

Minor Technical upgrades


## Version 3.1 – July 2025

•

Performance optimization

•

Enhanced stability

•

Cegid Ref. : 1774660

o   Enhanced resilience on the GetSasToken API


![Figure 4](./images/img_0004.png)


![Figure 5](./images/img_0005.png)


![Figure 6](./images/img_0006.png)


![Figure 7](./images/img_0007.png)


![Figure 8](./images/img_0008.png)


![Figure 9](./images/img_0009.png)


Cegid

6

•

Cegid Ref. : 1773086

o   User selection based on identity provider type

•

Cegid Ref. : 1760601

o   Support for claim folderId


## Version 3.0 – April 2025

•

Performance optimization

•

Enhanced stability

•

Enriched trace logs to improve monitoring

•

Contents of the files  « .Input folder.txt » and « .Output folder.txt » created upon creating

of a container in French and in English

•

Cegid Ref. : 1688351

o   Migration to .net8

•

Cegid Ref. : 1668630

o   Security issue


## Version 2.3 – December 2024

•

Cegid Ref. : 1584895

o   Enhanced security on HTTP calls


## Version 2.2 – April 2024

•

Performed optimizations needed for proper operation and supervision.

•

Cegid Ref. : 1425903

o   Correction of the validity period of the SAS key


![Figure 10](./images/img_0010.png)


![Figure 11](./images/img_0011.png)


![Figure 12](./images/img_0012.png)


![Figure 13](./images/img_0013.png)


![Figure 14](./images/img_0014.png)


![Figure 15](./images/img_0015.png)


Cegid

7


## Version 2.1 – February 2024

•

Cegid Ref. : 1251050

o   Fallback management for situations where the translation server is down. This

ensures that the application is translated under all circumstances.

•

Cegid Ref. : 1234989

o   Sas keys generation in “Read” or “Read/Write” modes


## Version 2.0 – December 2023

•

Minor Technical upgrades


## Version 2.0 – October 2023

•

Performed optimizations needed for proper operation and supervision.

•

Cegid Ref. : 1176534

o   Help tooltips

•

Cegid Ref. : 1164279

o   Dataprotection v2

•

Cegid Ref. : 1209953

o   Added an error message upon creation if the name of the container is already in

use.

•

Cegid Ref. :  1176251

o   Interface corrections (labels, icons)


![Figure 16](./images/img_0016.png)


![Figure 17](./images/img_0017.png)


![Figure 18](./images/img_0018.png)


![Figure 19](./images/img_0019.png)


Cegid

8


## Version 1.1 – June 2023

•

Cegid Ref. :  1136323

o   List of containers

•

Cegid Ref. :  1136327

o   Management of containers

•

Cegid Ref. :  1136321

o   Management of users


## Version 1.0 – October 2022

•

Deployment of the initial version


![Figure 20](./images/img_0020.png)


![Figure 21](./images/img_0021.png)


