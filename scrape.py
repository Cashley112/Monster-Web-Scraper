import requests
from bs4 import BeautifulSoup

#get html from Monster.com
URL = 'https://www.monster.com/jobs/search/?q=Entry-Level-Software-Developer&where=Remote'
page = requests.get(URL)

#parse html with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#All Jobs on page
results = soup.find(id="ResultsContainer")
#Individual Jobs
job_elems = results.find_all('section', class_='card-content')


# for job_elem in job_elems:
    # print(job_elem, end='\n'*2)

def clean_scrape():
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

