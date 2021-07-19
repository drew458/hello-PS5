import schedule
import datetime
import time
from src import scraper, checkStrings, sendTelegramBotNotification


def job():
    """
    Scrapes the page, checks if the string inseide the tags is present and then sends a notification.
    """

    # Scrape the page
    scrapedPage = scraper.scrapeThePage()

    # Find the H1 tags
    strings_h1 = scraper.retainStringsInH1Tags(scrapedPage)

    # Keywords
    texth1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
    texth3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

    if not checkStrings.checkH1(strings_h1, texth1) is True:
        print("FOUND!!!! Go check it out now!")

        # Windows notification
        # swn.sendNotification()

        # Telegram bot notification
        sendTelegramBotNotification.sendNotification()
    else:
        print("Hourly check of", datetime.datetime.now().hour, ":", datetime.datetime.now().minute,
              ", nothing found...")


def everyHourCheck():
    """
    Does the complete job of scraping and sending a notification, every hour.
    """

    schedule.every().day.at("09:01").do(job)
    schedule.every().day.at("10:01").do(job)
    schedule.every().day.at("11:01").do(job)
    schedule.every().day.at("12:01").do(job)
    schedule.every().day.at("13:01").do(job)
    schedule.every().day.at("14:01").do(job)
    schedule.every().day.at("15:01").do(job)
    schedule.every().day.at("16:01").do(job)
    schedule.every().day.at("17:01").do(job)
    schedule.every().day.at("18:01").do(job)
    schedule.every().day.at("19:01").do(job)
    schedule.every().day.at("20:01").do(job)
    schedule.every().day.at("21:01").do(job)
    schedule.every().day.at("22:01").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
