# Introduction

This folder extracted brokers' information from FINRA via BrokerCheck report. Note some broker only has IAPD report. I will deal with it later

The source for this BrokerCheck report is https://brokercheck.finra.org/

# Code

The code is uplaoded. The results are obtained via the code, which are not uploaded here but to AWS s3 bucket. It's in the Request Pays s3 bucket that is available to public.

# Brokers' Information (Last Update 04/15/2020)

There are 9 elements for brokers' information:

1. Name
2. CRD
3. Branch Office Information
4. Disclosed Event Count
5. Registration History
6. Employment History
7. Exam
8. Misconduct
9. Other Business Activities

## Raw PDF files

The raw pdf files for brokers and firms are in the Requester Pays s3 bucket:
1. s3://datahubforall/broker/broker.zip
2. s3://datahubforall/broker/firm.zip


## Brokers' Information Files

The information are extracted and contained in the following files:

1. broker_name_CRD.csv
2. broker_branch_office_info.csv
3. broker_disclosed_event_count.csv
4. broker_registration_history.csv
5. broker_employment_history.csv
6. broker_exam.csv
7. broker_misconduct.csv
8. broker_other_business_activities.csv

### broker_name_CRD.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_name_CRD.csv

Columns:
* file_loc
* Broker Name
* CRD Number

### broker_branch_office_info.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_branch_office_info.csv

Columns:
* CRD Number
* Register Status
* Branch Office Name
* Branch Office ADDRESS
* Branch Office CRD
* Branch Office Start Date

### broker_disclosed_event_count.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_disclosed_event_count.csv

Columns:
* CRD Number
* Disclose Check
* Disclose Check Type
* Disclose Num

### broker_registration_history.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_registration_history.csv

Columns:
* CRD Number
* Start Date
* End Date
* Company Name
* Company CRD Number
* Branch Location

### broker_employment_history.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_employment_history.csv

Columns:
* CRD Number
* Start Date
* End Date
* Company Name
* Company CRD Number

### broker_exam.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_exam.csv

Columns:
* Exam Class
* Exam Name
* Category
* Date
* CRD Number

### broker_misconduct.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_misconduct.csv

Columns:
* CRD Number
* Disclosure Check
* Disclose Type
* Disclose Num

### broker_other_business_activities.csv

Requester Pays s3 bucket: s3://datahubforall/broker/broker_other_business_activities.csv

Columns:
* CRD Number
* Activity Detail


