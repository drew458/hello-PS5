import sys
from threading import Thread
import argparse
from src import Stats, TimeElapsed, SendTelegramBotNotification as stbn, Scraper, CheckStrings, HourlyCheck, IOConsole

""" This is a really simple script. The script downloads the page of MediaWorld where the PS5 Digital Edition 
    will be added when available, and if found, notifies via Telegram bot.
    If nothing is found it repeats after 10 minutes.
"""


# To enable Windows notifications, uncomment line below
# import sendWindowsNotification as swn


def main():
    parser = argparse.ArgumentParser(description='Insert the Telegram bot Token and Chat_ID to set notifications')
    parser.add_argument("--t", default=None, type=str, help="The Telegram Bot token")
    parser.add_argument("--c", default=None, type=str, help="The Telegram Bot chat_id")

    args = parser.parse_args()

    count = 0
    days = 0
    weeks = 0

    IOConsole.printStartMessage()

    # while this is true (it is true by default)
    while True:

        # start the timer for execution statistics
        start_scrape = Stats.performanceCounter()

        # scrape the page
        scraped_page = Scraper.scrapeThePage()

        # find the H1 tags
        strings_h1 = Scraper.retainStringsInH1Tags(scraped_page)

        # start the timer for execution statistics
        finish_scrape = Stats.performanceCounter()

        # start collecting stats about the conditional statement (if) performance
        start_conditional_statement = Stats.performanceCounter()

        # start the hourly check thread
        every_hour_plus_1minute_thread = Thread(target=HourlyCheck.everyHourCheck_OneMinuteDelay)
        every_hour_plus_1minute_thread.start()
        every_hour_plus_15secs_thread = Thread(target=HourlyCheck.everyHourCheck_15SecsDelay)
        every_hour_plus_15secs_thread.start()

        # keywords to look for
        TEXT_H1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
        # TEXT_H3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

        # if the keywords are still there, keep searching...
        if CheckStrings.checkH1(strings_h1, TEXT_H1) is True:  # and checkStrings.checkH3(strings_h3, texth3) is True
            count = count + 1
            IOConsole.printCheckNumberMessage(count)

            # finish collecting stats about the conditional statement (if) performance
            finish_conditional_statement = Stats.performanceCounter()

            # Show stats
            IOConsole.printWaitingStatsMessage()
            TimeElapsed.checkDaysWeeksElapsed(count, days, weeks)
            Stats.printPerformanceResult(Stats.getResult(start_scrape, finish_scrape))
            Stats.printConditionalStatementResult(
                Stats.getResult(start_conditional_statement, finish_conditional_statement))
            print()

            # wait 10 minutes
            # time.sleep(600)
            TimeElapsed.countdown(600)

            # continue with the script (that is, go back at the top of the while loop)
            continue

        # but if the words above don't occur... object found!
        else:
            IOConsole.printFoundMessage()

            # To enable Windows notifications, uncomment the line below
            # swn.sendNotification()

            # Telegram bot notification
            if args.t and args.c is not None:
                stbn.sendNotification(args.t, args.c, IOConsole.getFoundMessage())

            break

    # Adiòs
    IOConsole.printAdiosMessage()
    sys.exit()


if __name__ == "__main__":
    main()
