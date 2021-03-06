# Govinfo - US Court Cases

This section contains information extracted from Govinfo.gov.

Govinfo.gov is a service of the United States Government Publishing Office (GPO), which is a Federal agency in the legislative branch.
It provides free public access to official publications from all three branches of the Federal Government.

Here is a list of information extracted from this website and organized into csv files:
1. Sitemap urls
2. Case urls
3. Case metadata
4. Case PDF files

Check the following sections for more details.

## Sitemap urls/ Case urls

Sitmap urls allow us to keep track of cases by US courts and years. Case urls direct us to each case including its summary, details, metadata, judicial opinion (in pdf), etc.

### Data

This file is in the Requester Pay S3 bucket: ***s3://datahubforall/legal/govinfo/govinfo_sitemap_all_url.csv***

It contains the following columns:
1. US court + year url (2,721)
2. Case url (1,615,328)

Note for each case, there may be multiple judicial opinions (pdf files) and summaries.

### Code

The code to download all case urls is in ***Govinfo_Sitemap_Download.ipynb***

To acquire sitemap urls for all cases (not US court + year), You can either add time.sleep(1) in the loop or run the code more than once (the code will pick up remaining sitemaps to acquire all case urls) since the website imposes maximum limit on requests.

## Metadata download

### Data 

This file is in the Requester Pay S3 bucket: ***s3://datahubforall/legal/govinfo/Govinfo_metadata.tar.gz***

### Code

The code to download all metadata for cases is in ***Govinfo_case_metadata_download.py***

You may need to run this code multiple times due to request limits of the website. Also, sometimes, the metadata of some case can be downloaded successfully but is not the desired one. You just need to redownload it.

## Metadata extraction

### Data

Here is the list of information extracted from the metadata files:

1. govinfo_party_name.csv

#### govinfo_party_name.csv

This file is in the Requester Pay S3 bucket: ***s3://datahubforall/legal/govinfo/govinfo_party_name.csv***

There are 9,451,173 rows and 6 columns. The columns include:
* caseIdentifier
* caseURI
* firstName
* fullName
* lastName
* role

#### govinfo_basic_information.csv

This file is in the Requester Pay S3 bucket: ***s3://datahubforall/legal/govinfo/govinfo_basic_information.csv***

There are 1,615,325 rows and 12 columns. The columns include:
* caseIdentifier
* caseURI
* natureSuit
* natureSuitCode
* courtType
* courtCode
* courtCircuit
* courtState
* caseNumber
* caseOffice
* caseType
* cause

#### govinfo_details.csv

This file is in the Requester Pay S3 bucket: ***s3://datahubforall/legal/govinfo/govinfo_details.csv***

There are 3,483,428 rows and 7 columns. The columns include:
* caseIdentifier
* caseURI
* title
* dateIssued
* pdf_url
* content_detail_url
* docket_text

### Code

The code to extract metadata is in ***Govinfo_metadata_extraction.py***

There are a few functions in this script responsible for extracting information from metadata files:

* get_party_name
* get_details
* get_basic_information

Each function takes a location of metadata file as input and save the result to a specified folder. You can find the aggregated result in the Requester Pay S3 buckets given above.

## PDF Download (No Data)

No downaloded pdf files yet. The estimated size of all pdf files is 650GB. If you have use case of the pdf files, you can request for download. 

### Code

The code to download all pdf files is in ***Govinfo_pdf_download.py***
