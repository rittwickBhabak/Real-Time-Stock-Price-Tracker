from datetime import datetime
from scraper import scraper
import json 
#well commented
aser=90
list_of_urls = []
with open('company.json', 'r+') as file:
    data = json.load(file)
    list_of_urls = data['companies']

print(f'Time {datetime.now()}')
print('{:15} {:10}'.format('Company', 'Price'))
for company, url in list_of_urls:
    price = scraper(url)[0]
    print(f"{company:{15}} {price:.>{10}}")
