# Data Acquisition Repository

Welcome to the Data Acquisition Repository! This repository contains Jupyter Notebooks for web scraping data from various sources including FINRA, Edgar, Legal databases, and the US Patent Office. The results of these scrapes are shared via AWS S3.

## Repository Structure

The repository is organized into the following folders:

	1.	FINRA
	2.	Edgar
	3.	Legal
	4.	US Patent

Each folder contains specific notebooks for scraping data from the respective sources.

## Folder Details

1. FINRA

This folder contains notebooks to scrape data from the Financial Industry Regulatory Authority (FINRA) website. The data includes information about brokers, firms, and regulatory actions.

2. Edgar

This folder contains notebooks for scraping data from the SEC’s Edgar database. The data includes company filings, financial statements, and other regulatory documents.

3. Legal

This folder contains notebooks for scraping data from various legal databases. The data includes court cases, legal precedents, and other legal documents.

4. US Patent

This folder contains notebooks for scraping data from the United States Patent and Trademark Office (USPTO). The data includes patents, patent applications, and other intellectual property documents.

## Data Sharing

Some of the results from these notebooks are shared via AWS S3. You can access the shared data through the following S3 bucket:

	•	AWS S3 Bucket: s3://datahubforall/

## Usage

To use the notebooks in this repository:

	1.	Clone the repository to your local machine.
	2.	Navigate to the folder of interest.
	3.	Open the notebook using Jupyter Notebook or JupyterLab.
	4.	Follow the instructions in the notebook to scrape the data.
