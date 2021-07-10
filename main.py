import time
import requests
from bs4 import BeautifulSoup

import sendTelegramBotNotification as stbn
import checkStrings

# This is a really simple script. The script downloads the page of MediaWorld where the PS5 Digital Edition will be added when available,
# and if found, shows it and emails me.
# If it does not find some text, it waits 5 seconds and downloads the page again.

# Windows notifications
# import sendWindowsNotification as swn

print("HI! I'm a PS5-availability finder in the MediaWorld website. Let's see if I can find something...")
print()

count = 0

# while this is true (it is true by default)
while True:
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
    soup = BeautifulSoup(page.content, "html.parser")

    # retain all the strings inside h1 and h3 tags
    child_soup_h1 = soup.find_all('h1')
    child_soup_h3 = soup.find_all('h3')

    # keywords
    texth1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
    #texth3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito. Per prepararti all'

    # if the keywords are there, keep searching...
    if checkStrings.checkH1(child_soup_h1, texth1) is True:  #and checkStrings.checkH3(child_soup_h3, texth3) is True:
        count = count + 1
        print("Check number", count, ", nothing found, i'll keep trying...")
        # wait 5 minutes
        time.sleep(600)
        # continue with the script
        continue

    # but if the words above don't occur...
    else:
        print("FOUND!!!! Go check it out now!")
        # Windows notification
        # swn.sendNotification()

        # Telegram bot notification
        stbn.sendNotification()
        break
