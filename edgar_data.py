import datetime
import pandas as pd
import glob
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import os
import requests
import json
from bs4 import BeautifulSoup


class EdgarMasterDownloadSelenium():
    
    """
    
    This class downloads the master files of Edgar filing for all companies to a specified folder using Selenium
    
    Although SEC requires User-Agent in headers, this class bypass the requirement
    
    However, if you want quick response in filing, use EdgarRecentFiling or EdgarRecentFilingSelenium for the most
    recent filings.
    
    """
    def __init__(self,start_year = 1993, end_year = 'now',output_folder = 'edgar_master'):
        
        """
        
        Args:
            start_year: must be an integer
            end_year: must be an integer or the string 'now'
            output_folder: must be provided. Make sure it is a new folder without any file
        
        """
        
        
        self.start_year = start_year
        self.end_year = end_year
        self.output_folder = output_folder
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        if '/' not in self.output_folder:
            self.output_folder = os.getcwd()+'/'+self.output_folder
        
        if re.findall('^./',self.output_folder)!=[]:
            self.output_folder = re.sub('^./',os.getcwd()+'/',self.output_folder)
        
        
        
    def get_master_file_url(self):
        
        """
        
        Find all urls of master files
        
        """
        
        if self.end_year == 'now':
            end_year_int = datetime.date.today().year
            end_quarter_int = (datetime.date.today().month - 1) // 3 + 1
        else:
            end_year_int = int(self.end_year)
            end_quarter_int = 4
        years = list(range(self.start_year, end_year_int+(self.end_year != 'now')))
        quarters = ['QTR1', 'QTR2', 'QTR3', 'QTR4']
        history = [(y, q) for y in years for q in quarters]
        
        if self.end_year == 'now':
            for i in range(1, end_quarter_int + 1):
                history.append((end_year_int, 'QTR%s' % i))
        urls = ['https://www.sec.gov/Archives/edgar/full-index/%s/%s/master.idx' % (x[0], x[1]) for x in history]
        urls.sort()
        print('There are {} urls'.format(len(urls)))
        return urls
    
    def get_master_file(self):
        urls = self.get_master_file_url()
        options = Options()
        #options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        prefs = {'download.default_directory' : self.output_folder}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        existing_file_count = len(glob.glob(self.output_folder+'/master*.idx'))
        for i, url in enumerate(urls,start=1):
            driver.get(url) # Download the file to the output folder. Then rename the file.
            time_out_count = 0
            while True:
                current_files = glob.glob(self.output_folder+'/master*.idx')
                if (len(current_files)-existing_file_count==i) or time_out_count>=5:
                    break
                time_out_count+=1
            time.sleep(0.25)
            list_of_files = glob.glob(self.output_folder+'/*.idx')
            latest_file = max(list_of_files, key=os.path.getctime)
            os.rename(latest_file, self.output_folder+'/'+url.split('/')[-3]+'_'+url.split('/')[-2]+'.idx')
        return None
    
    def get_single_master_file(self,master_file_dir):
        
        """
        
        This function read downloaded files and organize the information into a csv file
        
        """
        
        
        with open(master_file_dir,'r') as f:
            lines = f.readlines()
        col_name = re.sub('\s+','',lines[9]).split('|')
        master_file_df = pd.DataFrame()
        master_file_df[col_name[0]] = [re.sub('\s+','',x).split('|')[0] for x in lines[11:]]
        master_file_df[col_name[1]] = [re.sub('\s+','',x).split('|')[1] for x in lines[11:]]
        master_file_df[col_name[2]] = [re.sub('\s+','',x).split('|')[2] for x in lines[11:]]
        master_file_df[col_name[3]] = [re.sub('\s+','',x).split('|')[3] for x in lines[11:]]
        master_file_df[col_name[4]] = [re.sub('\s+','',x).split('|')[4] for x in lines[11:]]
        return master_file_df
    
    def get_master_file_combined(self,return_df = False):
        
        """
        
        This function returns the combined csv file for the date range provided
        
        """
        
        self.get_master_file()
        master_files = glob.glob(self.output_folder+'/*.idx')
        master_file_df_list = []
        for file in master_files:
            master_file_df_list.append(self.get_single_master_file(file))
        master_file_df = pd.concat(master_file_df_list)
        master_file_df.to_csv(self.output_folder+'/master_file_df.csv', index= False)
        
        if return_df == True:
            return master_file_df
        else:
            return None


class EdgarMasterDownload():
    
    """
    
    This class downloads the master files of Edgar filing for all companies to a specified folder
    
    The different between EdgarMasterDownload and EdgarMasterDownloadSelenium is that this class requires you
    to provide your information in User-Agent. Otherwise SEC will block you.
    
    """
    def __init__(self,user_agent,start_year = 1993, end_year = 'now',output_folder = 'edgar_master'):
        
        """
        
        Args:
            start_year: must be an integer
            end_year: must be an integer or the string 'now'
            output_folder: must be provided. Make sure it is a new folder without any file
            user_agent: this is a string that contains both your name and email address required by SEC.
                        For example, Your Name Your Email Address
        
        """
        
        
        self.start_year = start_year
        self.end_year = end_year
        self.output_folder = output_folder
        self.user_agent = user_agent
        self.headers = {'User-Agent':user_agent,
           'Accept-Encoding': 'gzip, deflate',
           'Host':'www.sec.gov'}
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        if '/' not in self.output_folder:
            self.output_folder = os.getcwd()+'/'+self.output_folder
        
        if re.findall('^./',self.output_folder)!=[]:
            self.output_folder = re.sub('^./',os.getcwd()+'/',self.output_folder)
        
    def get_master_file_url(self):

        """

        Find all urls of master files

        """

        if self.end_year == 'now':
            end_year_int = datetime.date.today().year
            end_quarter_int = (datetime.date.today().month - 1) // 3 + 1
        else:
            end_year_int = int(self.end_year)
            end_quarter_int = 4
        years = list(range(self.start_year, end_year_int+(self.end_year != 'now')))
        quarters = ['QTR1', 'QTR2', 'QTR3', 'QTR4']
        history = [(y, q) for y in years for q in quarters]

        if self.end_year == 'now':
            for i in range(1, end_quarter_int + 1):
                history.append((end_year_int, 'QTR%s' % i))
        urls = ['https://www.sec.gov/Archives/edgar/full-index/%s/%s/master.idx' % (x[0], x[1]) for x in history]
        urls.sort()
        print('There are {} urls'.format(len(urls)))
        return urls  
    
    def get_single_master_file(self,master_file_url):
        lines= requests.get(master_file_url,headers = self.headers).text.splitlines()
        col_name = re.sub('\s+','',lines[9]).split('|')
        master_file_df_temp = pd.DataFrame()
        master_file_df_temp[col_name[0]] = [re.sub('\s+','',x).split('|')[0] for x in lines[11:]]
        master_file_df_temp[col_name[1]] = [re.sub('\s+','',x).split('|')[1] for x in lines[11:]]
        master_file_df_temp[col_name[2]] = [re.sub('\s+','',x).split('|')[2] for x in lines[11:]]
        master_file_df_temp[col_name[3]] = [re.sub('\s+','',x).split('|')[3] for x in lines[11:]]
        master_file_df_temp[col_name[4]] = [re.sub('\s+','',x).split('|')[4] for x in lines[11:]]
        return master_file_df_temp
     
    def get_master_file_combined(self,return_df = False):
        urls = self.get_master_file_url()
        master_file_df_list = []
        for url in urls:
            master_file_df_list.append(self.get_single_master_file(url))
        master_file_df = pd.concat(master_file_df_list)
        
        master_file_df.to_csv(self.output_folder+'/master_file_df.csv', index= False)
        
        if return_df == True:
            return master_file_df
        else:
            return None


class EdgarRecentFiling():
    
    """
    
    This class requests company filing from SEC. 
    The max records is 1,000. For records earlier, use EdgarMasterDownload
    
    """
    
    def __init__(self,user_agent,CIK = None):
        self.CIK = CIK
        self.user_agent = user_agent
        self.headers = {'User-Agent':user_agent,
           'Accept-Encoding': 'gzip, deflate',
           'Host':'www.sec.gov'}
        
        if self.CIK == None:
            print('You need to provide a valid CIK')
        
    def get_CIK(self):
        lines= requests.get('https://www.sec.gov/files/company_tickers.json',headers = self.headers)
        dict_list = json.loads(lines.content)
        #print('get CIK')
        cik = [('0000000000'+str(v['cik_str']))[-10:] for v in dict_list.values()]
        ticker = [v['ticker'] for v in dict_list.values()]
        title = [v['title'] for v in dict_list.values()]
        
        cik_df = pd.DataFrame({'cik':cik,
                               'ticker':ticker,
                               'title':title})
        return cik_df
    
    def get_recent_filing_single(self,limit = 100):
        if self.CIK == 'all':
            print('Please provide a single CIK. If you want recent filings for all CIK, use get_recent_filing and set CIK equals all')
            return None

        if len(self.CIK)<10:
            self.CIK = ('0000000000'+self.CIK)[-10:]
        url = 'https://data.sec.gov/submissions/CIK'+self.CIK+'.json'
        options = Options()
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        driver.get('https://data.sec.gov/submissions/CIK0000320193.json')
        result_dict = json.loads(driver.page_source.split('>')[5].split('</pre')[0])
        #return result_dict
        company_information = pd.DataFrame({'cik':[result_dict['cik']],
                                            'entityType':[result_dict['entityType']],
                                           'sic':[result_dict['sic']],
                                           'sicDescription':[result_dict['sicDescription']],
                                           'insiderTransactionForOwnerExists':[result_dict['insiderTransactionForOwnerExists']],
                                           'insiderTransactionForIssuerExists':[result_dict['insiderTransactionForIssuerExists']],
                                           'name':[result_dict['name']],
                                           'tickers':[result_dict['tickers']],
                                           'exchanges':['|'.join(result_dict['exchanges'])],
                                           'ein':[result_dict['ein']],
                                           'description':[result_dict['description']],
                                           'website':[result_dict['website']],
                                           'investorWebsite':[result_dict['investorWebsite']],
                                           'category':[result_dict['category']],
                                           'fiscalYearEnd':[result_dict['fiscalYearEnd']],
                                           'stateOfIncorporation':[result_dict['stateOfIncorporation']],
                                           'stateOfIncorporationDescription':[result_dict['stateOfIncorporationDescription']],
                                           'address_mailing':['|'.join([v for v in result_dict['addresses']['mailing'].keys()])],
                                           'address_business':['|'.join([v for v in result_dict['addresses']['business'].keys()])],
                                           'phone':[result_dict['phone']],
                                           'flags':[result_dict['flags']]})
        
        filing_detail_df = pd.DataFrame({'accessionNumber':result_dict['filings']['recent']['accessionNumber'],
                                         'filingDate':result_dict['filings']['recent']['filingDate'],
                                         'reportDate':result_dict['filings']['recent']['reportDate'],
                                         'acceptanceDateTime':result_dict['filings']['recent']['acceptanceDateTime'],
                                        'form':result_dict['filings']['recent']['form'],
                                        'filingDate':result_dict['filings']['recent']['filingDate'],
                                        'primaryDocDescription':result_dict['filings']['recent']['primaryDocDescription'],
                                        'items':result_dict['filings']['recent']['items']})
        
        filing_detail_df.sort_values(by = ['filingDate'], ascending=False, inplace = True )
        return (company_information, filing_detail_df.loc[:limit,:])
    

