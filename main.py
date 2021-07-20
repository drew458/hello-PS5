import time
from threading import Thread

from src import Stats, TimeElapsed, SendTelegramBotNotification as stbn, Scraper, CheckStrings, hourlyCheck

""" This is a really simple script. The script downloads the page of MediaWorld where the PS5 Digital Edition 
    will be added when available, and if found, notifies via Telegram bot.
    If nothing is found it repeats after 10 minutes.
"""

# Windows notifications
# import sendWindowsNotification as swn

print("HI! I'm a PS5-availability finder in the MediaWorld website. Let's see if I can find something...")
print()

count = 0

# while this is true (it is true by default)
while True:

    # start the timer for execution statistics
    start = Stats.performanceCounter()

    # scrape the page
    scrapedPage = Scraper.scrapeThePage()

    # find the H1 tags
    strings_h1 = Scraper.retainStringsInH1Tags(scrapedPage)

    # start the timer for execution statistics
    finish = Stats.performanceCounter()

    # keywords
    texth1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
    # texth3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

    # perform a check every hour
    new_thread = Thread(target=hourlyCheck.everyHourCheck)
    new_thread.start()

    # if the keywords are still there, keep searching...
    if CheckStrings.checkH1(strings_h1, texth1) is True:  # and checkStrings.checkH3(strings_h3, texth3) is True
        count = count + 1
        print("Check number", count, ", nothing found, i'll keep trying...")

        # wait 10 minutes
        time.sleep(600)

        # Show stats
        print("While I'm waiting, let's see some stats about the execution...")
        print()

        # timeElapsed.checkTime(count)

        Stats.printPerformanceResult(Stats.getPerformanceResult(start, finish))
        print()

        # continue with the script (that is, go back at the top of the while loop)
        continue

    # but if the words above don't occur...
    else:
        print("FOUND!!!! Go check it out now!")

        # Windows notification
        # swn.sendNotification()

        # Telegram bot notification
        stbn.sendNotification()

        # Adios
        break
