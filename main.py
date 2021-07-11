import time

from src import stats, timeElapsed, sendTelegramBotNotification as stbn, scraper, checkStrings


# This is a really simple script. The script downloads the page of MediaWorld where
# the PS5 Digital Edition will be added when available, and if found, notifies via Telegram bot.
# It keep searching every 10 minutes 'till something shows up.

# To enable Windows notifications, uncomment line below
# import sendWindowsNotification as swn

print("HI! I'm a PS5-availability finder in the MediaWorld website. Let's see if I can find something...")
print()

count = 0
days = 0
weeks = 0
FOUND_MESSAGE = "FOUND!!!! Go check it out now!"

# while this is true (it is true by default)
while True:

    # start the count for execution statistics
    start = stats.performanceCounter()

    # Scrape the page
    scrapedPage = scraper.scrapeThePage()

    # Find the H1 tags
    strings_h1 = scraper.retainStringsInH1Class(scrapedPage)
    # strings_h3 = scrapeIt.retainStringsInH3Class(scrapedPage)

    # get statistics about the execution
    finish = stats.performanceCounter()

    # Keywords
    texth1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
    texth3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

    # if the keywords are still there, keep searching...
    if checkStrings.checkH1(strings_h1, texth1) is True:  # and checkStrings.checkH3(strings_h3, texth3) is True
        count = count + 1
        print("Check number", count, ", nothing found, i'll keep trying...")
        print()

        # wait 10 minutes
        time.sleep(600)

        # Show stats
        print("While I'm waiting, let's see some stats about the execution...")
        timeElapsed.checkTime(count, days, weeks)
        stats.printPerformanceResult(stats.getPerformanceResult(start, finish))
        print()

        # continue with the script (that is, go back at the top of the while loop)
        continue

    # but if the words above don't occur... object found!
    else:
        print(FOUND_MESSAGE)

        # To enable Windows notifications, uncomment line below
        # swn.sendNotification()

        # Telegram bot notification
        stbn.sendNotification(FOUND_MESSAGE)

        # Adios
        break
