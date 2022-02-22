import glob
import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.cElementTree as et
import xml.dom.minidom
import os
import requests

# Author: Qiao Jiang
# Date: 02/22/2022


def redownload_metadata(file):

    """

    This function is to re-download metadata in case the downloaded one is due to request limit

    """

    ID = file.split("/")[-1].replace(".xml", "")
    url = "https://www.govinfo.gov/metadata/granule/" + ID + "/" + ID + "/mods.xml"
    response = requests.get(url)
    with open(file, "wb") as file:
        file.write(response.content)


def get_party_name(file):

    """

    This function is to extract party names of cases.
    It will create a folder called Govinfo_party_name in your working directory and save the party names in the folder as a csv file.

    Parameter:

    file: the location of the metadata file (The metadata file should be an xml file)

    """

    path = "Govinfo_party_name"
    if not os.path.exists(path):
        os.makedirs(path)
    tree = et.parse(file)
    root = tree.getroot()
    case_identifier = file.split("/")[-1].replace(".xml", "")

    party = [
        x.attrib
        for x in root.findall(
            "{http://www.loc.gov/mods/v3}extension/{http://www.loc.gov/mods/v3}party"
        )
    ]

    caseURI = [
        x.text
        for x in root.findall('{http://www.loc.gov/mods/v3}identifier/[@type="uri"]')
    ][0]

    if len(party) == 0:
        temp = pd.DataFrame(
            {
                "caseIdentifier": [case_identifier],
                "caseURI": [caseURI],
                "firstName": ["Not Found"],
                "fullName": ["Not Found"],
                "lastName": ["Not Found"],
                "role": ["Not Found"],
            }
        )
        temp.to_csv(path + "/" + case_identifier + ".csv", index=False)
        return None

    firstName = [x.get("firstName", "") for x in party]
    fullName = [x.get("fullName", "") for x in party]
    lastName = [x.get("lastName", "") for x in party]
    role = [x.get("role", "") for x in party]

    temp = pd.DataFrame(
        {
            "caseIdentifier": [case_identifier] * len(party),
            "caseURI": [caseURI] * len(party),
            "firstName": firstName,
            "fullName": fullName,
            "lastName": lastName,
            "role": role,
        }
    )
    temp.drop_duplicates(inplace=True)
    temp.to_csv(path + "/" + case_identifier + ".csv", index=False)
    return None


def get_extension_tag(root, tag_name):

    """

    A helper function to extract tags in metadata files

    """

    tag_string = (
        "{http://www.loc.gov/mods/v3}extension/{http://www.loc.gov/mods/v3}" + tag_name
    )
    temp = [x for x in root.findall(tag_string)]
    if len(temp) == 0:
        return "Not Found"
    else:
        return [x.text for x in temp][0]


def get_basic_information(file):

    """

    This function is to extract basic information of cases.
    It will create a folder called Govinfo_basic_information in your working directory and save results in the folder as a csv file.

    Parameter:

    file: the location of the metadata file (The metadata file should be an xml file)

    """

    path = "Govinfo_basic_information"
    if not os.path.exists(path):
        os.makedirs(path)
    tree = et.parse(file)
    root = tree.getroot()
    case_identifier = file.split("/")[-1].replace(".xml", "")
    caseURI = [
        x.text
        for x in root.findall('{http://www.loc.gov/mods/v3}identifier/[@type="uri"]')
    ][0]

    natureSuit = get_extension_tag(root, "natureSuit")
    natureSuitCode = get_extension_tag(root, "natureSuitCode")
    courtType = get_extension_tag(root, "courtType")
    courtCode = get_extension_tag(root, "courtCode")
    courtCircuit = get_extension_tag(root, "courtCircuit")
    courtState = get_extension_tag(root, "courtState")
    caseNumber = get_extension_tag(root, "caseNumber")
    caseOffice = get_extension_tag(root, "caseOffice")
    caseType = get_extension_tag(root, "caseType")
    cause = get_extension_tag(root, "cause")

    temp = pd.DataFrame(
        {
            "caseIdentifier": [case_identifier],
            "caseURI": [caseURI],
            "natureSuit": [natureSuit],
            "natureSuitCode": [natureSuitCode],
            "courtType": [courtType],
            "courtCode": [courtCode],
            "courtCircuit": [courtCircuit],
            "courtState": [courtState],
            "caseNumber": [caseNumber],
            "caseOffice": [caseOffice],
            "caseType": [caseType],
            "cause": [cause],
        }
    )
    temp.drop_duplicates(inplace=True)
    temp.to_csv(path + "/" + case_identifier + ".csv", index=False)
    return None


def get_details(file):

    """

    This function is to extract content details such as docket texts and pdf urls of cases.
    It will create a folder called Govinfo_details in your working directory and save results in the folder as a csv file.

    Parameter:

    file: the location of the metadata file (The metadata file should be an xml file)

    """

    path = "Govinfo_details"
    if not os.path.exists(path):
        os.makedirs(path)
    tree = et.parse(file)
    root = tree.getroot()
    case_identifier = file.split("/")[-1].replace(".xml", "")
    caseURI = [
        x.text
        for x in root.findall('{http://www.loc.gov/mods/v3}identifier/[@type="uri"]')
    ][0]
    title = [
        x.text
        for x in root.findall(
            "{http://www.loc.gov/mods/v3}relatedItem/{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title"
        )
    ]
    dateIssued = [
        x.text
        for x in root.findall(
            "{http://www.loc.gov/mods/v3}relatedItem/{http://www.loc.gov/mods/v3}originInfo/{http://www.loc.gov/mods/v3}dateIssued"
        )
    ]

    content_url = [
        x
        for x in root.findall(
            "{http://www.loc.gov/mods/v3}relatedItem/{http://www.loc.gov/mods/v3}location"
        )
    ]

    pdf_url = [
        x.findall('{http://www.loc.gov/mods/v3}url/[@displayLabel="PDF rendition"]')
        for x in content_url
    ]
    pdf_url = [x[0].text if len(x) != 0 else "Not Found" for x in pdf_url]

    content_detail_url = [
        x.findall('{http://www.loc.gov/mods/v3}url/[@displayLabel="Content Detail"]')
        for x in content_url
    ]
    content_detail_url = [
        x[0].text if len(x) != 0 else "Not Found" for x in content_detail_url
    ]

    docket_text = [
        x.text
        for x in root.findall(
            "{http://www.loc.gov/mods/v3}relatedItem/{http://www.loc.gov/mods/v3}extension/{http://www.loc.gov/mods/v3}docketText"
        )
    ]

    temp = pd.DataFrame(
        {
            "caseIdentifier": [case_identifier] * len(dateIssued),
            "caseURI": [caseURI] * len(dateIssued),
            "title": title,
            "dateIssued": dateIssued,
            "pdf_url": pdf_url,
            "content_detail_url": content_detail_url,
            "docket_text": docket_text,
        }
    )
    # temp.drop_duplicates(inplace=True)
    temp.to_csv(path + "/" + case_identifier + ".csv", index=False)
    return None


if __name__ == "__main__":

    # You can use multiprocessing to apply the functions to metadata files to speed up the process
    # After that, you can aggregate files in each folder to a big csv file.
    # You can find the final results in my Requesters Pay S3 bucket.

    files = glob.glob("Govinfo_metadata/*")
    print(len(files))
    for file in files:
        get_party_name(file)
        get_basic_information(file)
        get_details(file)
