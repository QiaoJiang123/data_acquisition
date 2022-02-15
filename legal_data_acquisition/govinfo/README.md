# Govinfo - US Court Cases

This section contains information extracted from Govinfo.gov

Here is a list of information extracted:
1. Sitemap urls
2. Case urls
3. Case metadata
4. Case PDF files
5. ...

## Sitemap urls

### Data

This file is in the Requester Pay S3 bucket: s3://datahubforall/legal/govinfo/govinfo_sitemap_all_url.csv

It contains the following columns:
1. US court + year url (2,721)
2. Case url (1,615,328)

Note for each case, there may be multiple judicial opinions (pdf files) and summaries.

### Code

To acquire sitemap urls for all cases (not US court + year), You can either add time.sleep(1) in the loop or run the code more than once (the code will pick up remaining sitemaps to acquire all case urls) since the website imposes maximum limit on requests.

