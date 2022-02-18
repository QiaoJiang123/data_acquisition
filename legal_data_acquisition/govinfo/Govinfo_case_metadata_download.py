import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import glob
import time
import multiprocessing as mp
from multiprocessing import get_context

# Created by Qiao Jiang

# You probably need to run this script multiple times due to the request limit

# Add the file_location for the govinfo_sitemap_all_url.csv. You can downlaod it from my github
# Add the output_folder to store your downloaded metadata

file_location = your_file_location
output_folder = your_output_folder


print("Reading the main dataframe")

govinfo_sitemap_df = pd.read_csv(file_location)

print("Getting the metadata urls")

govinfo_sitemap_df["metadata_url"] = [
    x.replace("app/details", "metadata/pkg") + "/mods.xml"
    for x in govinfo_sitemap_df["case_url"]
]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Reading existing files of metadata")

existing_file = glob.glob(output_folder + "/*.xml")

print("Getting remaining metadata urls")

all_file = govinfo_sitemap_df["metadata_url"].tolist()

existing_file = [
    "https://www.govinfo.gov/metadata/pkg/"
    + x.split("/")[-1].replace(".xml", "/mods.xml")
    for x in existing_file
]

remaining_file = list(set(all_file) - set(existing_file))

print("The number of remaining metadata to download is ", len(remaining_file))


def download_metadata(url):
    try:
        response = requests.get(url)
        file_name = output_folder + "/" + url.split("pkg/")[-1].replace("/mods", "")
        with open(file_name, "wb") as file:
            file.write(response.content)
    except:
        print(url)


print("Downloading...")

p = get_context("fork").Pool(8)
result = p.map(download_metadata, remaining_file)
p.close()
