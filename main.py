import requests
from bs4 import BeautifulSoup
import time
import platform
import os


# This is a really simple script. The script downloads the page of MediaWorld where the PS5 Digital Edition will be added when available,
# and if found, shows it and emails me.
# If it does not find some text, it waits 5 seconds and downloads the page again.

# Windows notifications
if platform.system() == "Windows":
    from win10toast import ToastNotifier
    toaster = ToastNotifier()

print("HI! I'm a PS5-availability finder in the MediaWorld website. Let's see if I can find it...")
print()

count = 0

# while this is true (it is true by default)
while True:
    # set the url
    url = "https://www.mediaworld.it/search/playstation%205?category=Console%20e%20PC%20Gaming&category2=Sony%20Playstation%205&adult=0&orderBy=sortPrice.desc"
    # url2 = "https://www.mediaworld.it/search/playstation%205"

    # set the headers like we are a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the page
    response = requests.get(url, headers=headers)
    # parse the downloaded page and grab all text, then
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word "Digital Edition" occurs on the page is less than 1
    if str(soup).find("Digital Edition") == -1 and str(soup).find_all("h3", string="Playstation 5") == -1:
        count = count + 1
        print("Check number", count, ", nothing found, i'll keep trying...")
        # wait 5 minutes
        time.sleep(300)
        # continue with the script
        continue

    # but if the word "Digital Edition" occurs any other number of times
    else:
        print("FOUND!!!! Go check it out now!")

        #break