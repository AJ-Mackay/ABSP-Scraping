# Module 13 - Web Scraping: Controlling the Browser with the Selenium Module

### SHELL is still not playing fair ###

### NOTE: Use "from selenium" ###
### "import selenium" will NOT work. ###
from selenium import webdriver

# element = returns the first.
# elements = returns a list of all.

# Example 1:
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
elem.click() # simulates clicking on the selected link

elems = browser.find_elements_by_css_selector('p') # Finds all the <p>(paragraph) tags.
len(elems) # Returns '109'

searchElem = browser.find_element_by_css_selector('.search_field') # Finds search box.
searchElem.send_keys('zophie') # Enters the string 'zophie' into the search box.
searchElem.submit() # Submits the search string.

# browser.back() # Same as pressing the back button.
# browser.forward() # Same as clicking forward in the tool bar.
# browser.refresh() # Reloads the page.
# broswer.quit() # Closes browser window.

# Example 2:
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
elem.text # Returns the selected paragraph of text.

elem = browser.find_element_by_css_selector('html') # Returns the entire text of the webpage.

### Full documentation available at selenium-python.readthedocs.org ###
