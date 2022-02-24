import glob
import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.cElementTree as et
import xml.dom.minidom
import os
import requests
import time


def download_pdf(pdf_url):
    path = "Govinfo_pdf"
    if not os.path.exists(path):
        os.makedirs(path)
    if "Not Found" in pdf_url:
        return None
    else:
        response = requests.get(pdf_url, stream=True)
        with open(path + "/" + pdf_url.split("/pdf/")[-1], "wb") as f:
            f.write(response.content)


df = pd.read_csv("govinfo_details.csv")
pdf_urls = df["pdf_url"].tolist()

existing_pdf = glob.glob("Govinfo_pdf/*.pdf")

existing_pdf = [x.split("/")[-1] for x in existing_pdf]

pdf_urls = [x for x in pdf_urls if x != "Not Found"]


existing_pdf_url = [
    "https://www.govinfo.gov/content/pkg/" + "-".join(x.split("-")[:-1]) + "/pdf/" + x
    for x in existing_pdf
]

remaining_pdf = list(set(pdf_urls) - set(existing_pdf_url))

print("The total number of pdf files to download is ", len(pdf_urls))

print("The remaining number of pdf files to download is ", len(remaining_pdf))

for i, pdf_url in enumerate(remaining_pdf):
    try:
        if i % 5000 == 0:
            print(i)
        # time.sleep(0.1)
        download_pdf(pdf_url)
    except:
        print(pdf_url)
        continue
