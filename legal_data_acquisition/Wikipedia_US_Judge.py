import pandas as pd
import requests
from bs4 import BeautifulSoup


class GetUSJudge():
    
    """
    
    This class extract judges information from Wikipedia
    
    Use get_USCA_judge and get_USDC_judge to get judges. 
    Both methods return a tuple of current judges and former judges
    
    
    """
    def __init__(self):
        
        pass
    
    def get_USCA_wiki_link(self):
    
        """

        Get the wiki links for US Court of Appeals

        """

        url = 'https://en.wikipedia.org/wiki/United_States_courts_of_appeals'

        result = requests.get(url)
        soup = BeautifulSoup(result.content,'html')

        usca_links = [x.get('href') for x in soup.find_all('a') if ' Circuit' in x.text and 'United_States_Court_of_Appeals' in x.get('href')]

        usca_links = list(set(usca_links))
        usca_links = ['https://en.wikipedia.org/'+x for x in usca_links]

        return usca_links
    
    def get_current_judge_table(self,url):
        wiki_tables = pd.read_html(url)

        for wiki_table in wiki_tables:
            col_name = [x[0] if type(x)!=int else str(x) for x in wiki_table.columns]
            if all([x in col_name for x in ['Title','Judge','Duty station']]):
                col_name_new = [x if x==y else x+' '+y for x,y in wiki_table.columns ]
                wiki_table.columns = col_name_new
                wiki_table.drop(columns=['#'],inplace=True)
                wiki_table['Court'] = url.split('wiki/')[-1].replace('_',' ')
                return wiki_table
    
    def get_USCA_judge(self):
        usca_links = self.get_USCA_wiki_link()
        
        usca_former_judge_list = []
        usca_current_judge_list = []
        for link in usca_links:
            usca_former_judge_list.append(self.get_former_judge_table(link))
            usca_current_judge_list.append(self.get_current_judge_table(link))
        
        usca_former_judge_df = pd.concat(usca_former_judge_list)
        usca_current_judge_df = pd.concat(usca_current_judge_list)
        
        return (usca_current_judge_df,usca_former_judge_df)
    
    def get_USDC_wiki_link(self):
    
        """

        Get the wiki links for US District Court 

        """

        url = 'https://en.wikipedia.org/wiki/United_States_courts_of_appeals'

        result = requests.get(url)
        soup = BeautifulSoup(result.content,'html')

        usdc_links = [x.get('href') for x in soup.find_all('a') if 'District of' in x.text and 'District_Court' in x.get('href')]

        usdc_links = list(set(usdc_links))
        usdc_links = ['https://en.wikipedia.org/'+x for x in usdc_links]

        return usdc_links
    
    def get_former_judge_table(self,url):
        wiki_tables = pd.read_html(url)

        for wiki_table in wiki_tables:
            col_name = [x for x in wiki_table.columns]
            if all([x in col_name for x in ['Judge','Reason fortermination','Born–died']]):
                wiki_table.drop(columns=['#'],inplace=True)
                wiki_table['Court'] = url.split('wiki/')[-1].replace('_',' ')
                return wiki_table
    
    def get_USDC_judge(self):
        usdc_links = self.get_USDC_wiki_link()
        
        usdc_former_judge_list = []
        usdc_current_judge_list = []
        
        for link in usdc_links:
            usdc_former_judge_list.append(self.get_former_judge_table(link))
            usdc_current_judge_list.append(self.get_current_judge_table(link))

        usdc_former_judge_df = pd.concat(usdc_former_judge_list)
        usdc_current_judge_df = pd.concat(usdc_current_judge_list)
        
        return (usdc_current_judge_df,usdc_former_judge_df)

