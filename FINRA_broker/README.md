# Introduction

This folder extracted brokers' information from FINRA via BrokerCheck report. Note some broker only has IAPD report. I will deal with it later

The source for this BrokerCheck report is https://brokercheck.finra.org/

# Code

The code is still been revised for better quality. The results are obtained using old version of codes, which are not uploaded here.

# Brokers' Information (Last Update 04/15/2020)

There are 9 elements for brokers' information:

1. Name
2. CRD
3. Branch Office Information
4. Disclosed Event
5. Registration History
6. Employment History
7. Exam
8. Misconduct
9. Other Business Activities

## Raw PDF files

The raw pdf files are in the Requester Pays s3 bucket: s3://datahubforall/broker/broker.zip

## Brokers' Information Files

The information are extracted and contained in the following files:

1. broker_name_CRD.csv
