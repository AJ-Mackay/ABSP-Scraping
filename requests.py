# Module 13 - Web Scraping: Downloading from the Web with the Requests Module

### For SOME reason, the Shell is not playing fair today ###
### The code all works when passed to the Shell line by line ###
### But not when it is saved to a script and run. ###

### Below are the notes from this lesson ###

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code # Returns 200
len(res.text) # Returns '178978'
print(res.text[:500])

res.raise_for_status() # Raises an exception if download had issues.

badRes = requests.get('https://automatetheboringstuff.com/shash')
badRes.raise_for_status() # Returns 'HTTPError: 404 Client Error: Not Found'

### Now the code is not working in the Shell AT ALL ###

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

# More details for the Requests Module available at 'requests.readthedocs.org'
