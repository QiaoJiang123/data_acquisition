# Leagle Data Acquisition

Data are stored in the Requester Pay S3 bucket in AWS.

## Govinfo

This folder contains information extracted from Govinfo.gov, a service provided by the United States Government Publishing Office (GPO). The GPO is a Federal agency in the legislative branch that provides free public access to official publications from all three branches of the Federal Government. This folder contains notebooks and scripts that retrieves sitemap, case basic information, case details and case pdf files.

Data are stored in AWS s3 and please proceed to Govinfo folder for more information.

## US Judges from Wiki

Wikipedia_US_Judge.py scrapped federal judges from wikipedia.

* US Court of Appeals Current Judge: ***s3://datahubforall/legal/USCA_current_judge.csv***
* US Court of Appeals Former Judge: ***s3://datahubforall/legal/USCA_former_judge.csv***
* US District Court Current Judge: ***s3://datahubforall/legal/USDC_current_judge.csv***
* US District Court Former Judge: ***s3://datahubforall/legal/USDC_former_judge.csv***

## Leagle

This folder contains notebooks to retrieve information from leagle.com website. 

## Note

You can also obtain judicial opinion and judge information from courtlistener via their API or bulk data service.
