import requests
from bs4 import BeautifulSoup


class Scraper:
    #Specify url when instantiating Scraper class
    def __init__(self, url):
        self.url = url
        self.results = self.scrape()

    #get html and parse into specific element/attribute
    def scrape(self):

        #get html from Monster.com
        URL = self.url
        page = requests.get(URL)

        #parse html with BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')
        #All Jobs on page
        results = soup.find(id="ResultsContainer")

        return results

    #print all jobs
    def clean_scrape(self):
        
        #Individual Jobs
        job_elems = self.results.find_all('section', class_='card-content')

        for job_elem in job_elems:
            #Each job_elem is a new BeautifulSoup object
            title_elem = job_elem.find('h2', class_='title')
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')

            #Skips elements that would break loop
            if None in (title_elem, company_elem, location_elem):
                continue

            #Remove tags and anchors 
            print(title_elem.text.strip())
            print(company_elem.text.strip())
            print(location_elem.text.strip())
            print()

    #Print jobs for specific language
    def apply_link(self, language):

        lang_jobs = self.results.find_all('h2', string=lambda text: language in text.lower())
        for job in lang_jobs:
            link = job.find('a')['href']
            print(job.text.strip())
            print(f"Apply here: {link}\n")




