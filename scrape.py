import requests

URL = 'https://www.monster.com/jobs/search/?q=Entry-Level-Software-Developer&where=Remote'
page = requests.get(URL)

