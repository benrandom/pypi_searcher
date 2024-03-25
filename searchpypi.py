#! python3
#! searchpypi.py - Opens several search results.

import argparse
import requests
import sys
import webbrowser
import bs4

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Opens several search results from PyPI.')
    parser.add_argument('search_term', metavar='search_term', type=str, nargs='+', help='The term to search on PyPI')
    parser.add_argument('-n', '--tabs', type=int, default=5, help='Number of browser tabs to open (default: 5)')
    args = parser.parse_args()

    search_term = ' '.join(args.search_term)
    num_tabs = args.tabs

    print('Searching...') # Show user what is going on while searching the web

    res = requests.get('https://pypi.org/search/?q=' + search_term)
    res.raise_for_status()

    # Retrieve top search result links
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Open a browser tab for each result
    links = soup.select('.package-snippet')
    tabsOpen = min(num_tabs, len(links)) # change the number depending on number of results you want
    for i in range(tabsOpen):
        urltoOpen = 'https://pypi.org' + links[i].get('href')
        print('Opening', urltoOpen)
        webbrowser.open(urltoOpen)

if __name__ == "__main__":
    main()