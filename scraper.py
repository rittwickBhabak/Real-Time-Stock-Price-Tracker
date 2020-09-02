import requests, bs4


def scraper(url):
    '''Input: url of google search of company name, the result page should contain the stock price with class name "BNeawe iBp4i AP7Wnd". The second match will contain the serach result, (current_price, increment, precentage_increment). This function will return the current (price, status) of the stock. Status is 0 in case of error, otherwise it is 1. If any error happended then surely 'google' has changed the page structure.'''

    try:
        # get the response from the url
        res = requests.get(url)

        # make a beautiful soup object
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # select the span element with jsname='vWLAgc'
        # elements = soup.select('span[jsname="vWLAgc"]') THIS IS WHAT CHROME SHOWING US. BUT THE RESPONSE 
        # WE ARE REVICING ARE DIFFERENT. INSPECT THE ELEMENTS WE ARE RECIEVING THEN WE SHALL GET 
        # SOMETHING ELSE. THIS IS CASE SPECIFIC

        elements = soup.select('div[class="BNeawe iBp4i AP7Wnd"]')   # all divs which have class "BNeawe iBp4i AP7Wnd"

        # elements is a list of matches. In our case the second match contains the stock price
        information = elements[1].getText()
        price, increment, percent_increment = information.split()

        # remove commas from price
        price = price.replace(',','')
        return (price, 1)
    except:
        return (-1,0)