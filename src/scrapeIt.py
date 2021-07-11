import requests
from bs4 import BeautifulSoup


def scrapeThePage():
    # set the url
    url = "https://games.mediaworld.it/"
    # url3 = "https://www.mediaworld.it/search/playstation%205?category=Console%20e%20PC%20Gaming&category2=Sony%20Playstation%205&adult=0&orderBy=sortPrice.desc"
    # url2 = "https://www.mediaworld.it/search/playstation%205"

    # set the headers like we are a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the page
    page = requests.get(url, headers=headers)
    # parse the downloaded page and grab all text, then
    scraped_page = BeautifulSoup(page.content, "html.parser")

    return scraped_page


def retainStringsInH1Class(soup):
    # retain all the strings inside h1 tags
    strings = soup.find_all('h1')
    return strings

# def retainStringsInH3Class(soup):
#    # retain all the strings inside h3 tags
#    strings = soup.find_all('h3')
#    return strings
