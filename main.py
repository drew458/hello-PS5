import time

from src import Stats, TimeElapsed, SendTelegramBotNotification as stbn, Scraper, CheckStrings, IOConsole


# This is a really simple script. The script downloads the page of MediaWorld where
# the PS5 Digital Edition will be added when available, and if found, notifies via Telegram bot.
# It keep searching every 10 minutes 'till something shows up.

# To enable Windows notifications, uncomment line below
# import sendWindowsNotification as swn


def main():
    count = 0
    days = 0
    weeks = 0

    IOConsole.printStartMessage()

    # while this is true (it is true by default)
    while True:

        # start the count for execution statistics
        startScrape = Stats.performanceCounter()

        # Scrape the page
        scrapedPage = Scraper.scrapeThePage()

        # Find the H1 tags
        strings_h1 = Scraper.retainStringsInH1Class(scrapedPage)
        # strings_h3 = scrapeIt.retainStringsInH3Class(scrapedPage)

        # get statistics about the execution
        finishScrape = Stats.performanceCounter()

        # Keywords
        TEXT_H1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
        TEXT_H3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

        # Collecting stats about the conditional statement (if) performance
        startConditionalStatement = Stats.performanceCounter()

        # if the keywords are still there, keep searching...
        if CheckStrings.checkH1(strings_h1, TEXT_H1) is True:  # and checkStrings.checkH3(strings_h3, texth3) is True
            count = count + 1
            IOConsole.printCheckMessage(count)

            # Collecting stats about the conditional statement (if) performance
            finishConditionalStatement = Stats.performanceCounter()

            # Show stats
            IOConsole.printWaitingStatsMessage()
            TimeElapsed.checkDaysWeeksElapsed(count, days, weeks)
            Stats.printPerformanceResult(Stats.getResult(startScrape, finishScrape))
            Stats.printConditionalStatementResult(
                Stats.getResult(startConditionalStatement, finishConditionalStatement))
            print()

            # wait 10 minutes
            # time.sleep(600)
            TimeElapsed.countdown(600)

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


if __name__ == "__main__":
    main()
