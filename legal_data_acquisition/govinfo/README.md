# Govinfo - US Court Cases

This section contains information extracted from Govinfo.gov.

Govinfo.gov is a service of the United States Government Publishing Office (GPO), which is a Federal agency in the legislative branch.
It provides free public access to official publications from all three branches of the Federal Government.

Here is a list of information extracted from this website and organized into csv files:
1. Sitemap urls
2. Case urls
3. Case metadata
4. Case PDF files
5. ...

Check the following sections for more details.

## Sitemap urls/ Case urls (downloaded)

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

## Metadata download (downloading)

### Data 

This file is in the Requester Pay S3 bucket: ***s3://datahubforall/legal/govinfo/Govinfo_metadata.tar.gz***



## Metadata extraction
