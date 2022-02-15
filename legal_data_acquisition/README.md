# legal-data-acquisition

All data are stored in the Requester Pay S3 bucket in AWS. The location will be updated later.

## US Judges from Wiki (Updated on 02/06/2022)## 
* US Court of Appeals Current Judge: s3://datahubforall/legal/USCA_current_judge.csv
* US Court of Appeals Former Judge: s3://datahubforall/legal/USCA_former_judge.csv
* US District Court Current Judge: s3://datahubforall/legal/USDC_current_judge.csv
* US District Court Former Judge: s3://datahubforall/legal/USDC_former_judge.csv

## Govinfo - US Court Cases

This section contains information extracted from Govinfo.gov

Here is a list of information extracted:
1. Sitemap urls
2. Case urls
3. Case metadata
4. Case PDF files
5. ...

### Sitemap urls

This file is in the Requester Pay S3 bucket: 

It contains the following columns:
1. US court + year url (2,721)
2. Case url

Note for each case, there may be multiple judicial opinions (pdf files) and summaries.
