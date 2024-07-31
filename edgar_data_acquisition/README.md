dgar Data Acquisition

This folder contains scripts and notebooks for web scraping data from the SEC’s Edgar database. The data includes company filings, financial statements, and other regulatory documents.

Main Scripts:

	1.	Edgar Web Scrapping.R
	2.	edgar_data.py

Edgar Web Scrapping.R

This R script uses several libraries to download and process Edgar filings.

Key Libraries:

	•	edgar
	•	downloader
	•	RCurl
	•	XML
	•	httr

Main Function:

	•	edgar_file_download(YEAR, FORM.TYPE): Downloads filings of the specified form type for a given year and saves them to the specified directory.

Usage Example:
```
YEAR <- 2010
FORM.TYPE <- "10-K"
edgar_file_download(YEAR, FORM.TYPE)
```
edgar_data.py

This Python script uses Selenium and requests to download Edgar filings.

Key Classes:

	•	EdgarMasterDownloadSelenium: Downloads master files of Edgar filings using Selenium.
	•	EdgarMasterDownload: Downloads master files using requests with a provided User-Agent.
	•	EdgarRecentFiling: Requests recent filings from SEC for a given CIK.

Usage Example:

from edgar_data import EdgarMasterDownloadSelenium, EdgarMasterDownload, EdgarRecentFiling
```
# Using Selenium to download master files
downloader_selenium = EdgarMasterDownloadSelenium(start_year=1993, end_year='now', output_folder='edgar_master')
downloader_selenium.get_master_file_combined()

# Using requests to download master files
downloader = EdgarMasterDownload(user_agent="Your Name Your Email Address", start_year=1993, end_year='now', output_folder='edgar_master')
downloader.get_master_file_combined()

# Getting recent filings for a single CIK
recent_filing = EdgarRecentFiling(user_agent="Your Name Your Email Address", CIK='0000320193')
company_info, filings = recent_filing.get_recent_filing_single(limit=100)
```
