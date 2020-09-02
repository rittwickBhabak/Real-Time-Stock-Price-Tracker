from datetime import datetime
from scraper import scraper

list_of_urls = [
    ['Google', 'https://www.google.com/search?q=tata+steel+stock'],
    ['Alphabet', 'https://www.google.com/search?q=google+stock'],
    ['Airtel', 'https://www.google.com/search?q=airtel+stock'],
    ['Jindal Steel', 'https://www.google.com/search?q=jindal+steel+stock'],
    ['HDFC Bank', 'https://www.google.com/search?q=hdfc+bank+stock+price'],
    ['AXIS Bank', 'https://www.google.com/search?q=axis+bank+stock+price'],
    ['SBIN', 'https://www.google.com/search?q=sbin+stock+price'],
    ['TATA Motors', 'https://www.google.com/search?q=tata+motors+stock+price'],
    ['Mahindra', 'https://www.google.com/search?q=mahindra+share+price'],
    ['ZEEL', 'https://www.google.com/search?q=zeel+stock+price']
]

print(f'Time {datetime.now()}')
print('{:15} {:10}'.format('Company', 'Price'))
for company, url in list_of_urls:
    price = scraper(url)[0]
    print(f"{company:{15}} {price:.>{10}}")