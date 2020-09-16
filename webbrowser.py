# Module 13 - Web Scraping: The webbrowser Module

import webbrowser, sys, pyperclip

# webbrowser.open('https://www.automatetheboringstuff.com') # Wouldn't run in Shell.

sys.argv # ['webbrowser.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if (len(sys.argv) > 1:
    # ['webbrowser.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
