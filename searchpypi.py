#! python3
#! searchpypi.py - Opens several search results.

# Usage: python3 searchpypi.py <search term>


import requests, sys, webbrowser, bs4

print('Searching...') # Show user what is going on while searching the web

res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result
links = soup.select('.package-snippet')
tabsOpen = min(5, len(links)) #change the number depending on number of results you want
for i in range(tabsOpen):
    urltoOpen = 'https://pypi.org' + links[i].get('href')
    print('Opening', urltoOpen)
    webbrowser.open(urltoOpen)