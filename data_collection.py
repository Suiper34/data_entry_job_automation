import lxml
import requests
from bs4 import BeautifulSoup

ZILLOW_CLONE = 'https://appbrewery.github.io/Zillow-Clone/'

# get zillow html
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0'
}
zillow_web = requests.get(ZILLOW_CLONE, headers=header)
zillow_web.raise_for_status()
zillow_html = zillow_web.text

entry_soup = BeautifulSoup(zillow_html, 'lxml')

price_list = []
try:
    # rent prices
    for span in entry_soup.find_all(
            name='span', class_='PropertyCardWrapper__StyledPriceLine'):
        if '+' in span.getText():
            price = round(float(
                (span.getText()
                 ).split('$')[1].split('+')[0].replace(',', '')
            )
            )
            price_list.append(price)
        else:
            price = round(float(
                (span.getText()
                 ).split('$')[1].split('/')[0].replace(',', '')
            )
            )
            price_list.append(price)

except ValueError as ve:
    print('exception:', ve)


# property address links
address_links = [
    anchor.get('href') for anchor in entry_soup.find_all(
        name='a', class_='property-card-link'
    )
]

# property addresses
property_addresses = [
    address.getText().strip() for address in entry_soup.select(
        'a.StyledPropertyCardDataArea-anchor address'
    )
]
