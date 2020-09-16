# Module 13 - Web Scraping: Parsing HTML with the Beautiful Soup Module

# import bs4, requests

# res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
# res.raise_for_status()

### THIS IS WHEN THE SHELL BROKE, AGAIN. Hence typing out the lesson below ###

# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
# elems[0].text.strip() # Returns '$26.95'

### Program written during lesson: ###

import bs4, requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newBuyBoxPrice') # Inspect > Copy > Selector (CSS Selector in anything that is not Chrome)


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-dp-1593275994/dp/1593275994/')
print('The price is ' + price)

### Raises an exception: ###
### 'HTTPError 503 Server Error: Service Unavailable for url: ###
### https://www.amazon.com/...' ###
