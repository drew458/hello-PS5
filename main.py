import time

from src import stats, timeElapsed, sendTelegramBotNotification as stbn, scraper, checkStrings, IOConsole


# This is a really simple script. The script downloads the page of MediaWorld where
# the PS5 Digital Edition will be added when available, and if found, notifies via Telegram bot.
# It keep searching every 10 minutes 'till something shows up.

# To enable Windows notifications, uncomment line below
# import sendWindowsNotification as swn

count = 0
days = 0
weeks = 0

IOConsole.printStartMessage()

# while this is true (it is true by default)
while True:

    # start the count for execution statistics
    startScrape = stats.performanceCounter()

    # Scrape the page
    scrapedPage = scraper.scrapeThePage()

    # Find the H1 tags
    strings_h1 = scraper.retainStringsInH1Class(scrapedPage)
    # strings_h3 = scrapeIt.retainStringsInH3Class(scrapedPage)

    # get statistics about the execution
    finishScrape = stats.performanceCounter()

    # Keywords
    TEXT_H1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
    TEXT_H3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

    # Collecting stats about the conditional statement (if) performance
    startConditionalStatement = stats.performanceCounter()

    # if the keywords are still there, keep searching...
    if checkStrings.checkH1(strings_h1, TEXT_H1) is True:  # and checkStrings.checkH3(strings_h3, texth3) is True
        count = count + 1
        IOConsole.printCheckMessage(count)

        # Collecting stats about the conditional statement (if) performance
        finishConditionalStatement = stats.performanceCounter()

        # Show stats
        IOConsole.printWaitingStatsMessage()
        timeElapsed.checkDaysWeeksElapsed(count, days, weeks)
        stats.printPerformanceResult(stats.getResult(startScrape, finishScrape))
        stats.printConditionalStatementResult(stats.getResult(startConditionalStatement, finishConditionalStatement))
        print()

        # wait 10 minutes
        time.sleep(600)

        # continue with the script (that is, go back at the top of the while loop)
        continue

    # but if the words above don't occur... object found!
    else:
        IOConsole.printStartMessage()

        # To enable Windows notifications, uncomment line below
        # swn.sendNotification()

        # Telegram bot notification
        stbn.sendNotification(IOConsole.getFoundMessage())

        # Adiòs
        break
