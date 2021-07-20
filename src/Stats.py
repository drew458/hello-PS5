import time

from src import SendTelegramBotNotification

def performanceCounter():
    return time.perf_counter()


def getResult(start, finish):
    return finish - start


def printPerformanceResult(result):
    print(f"* Webpage and tags scraped in {result:0.4f} seconds")


def printConditionalStatementResult(result):
    print(f"* String presence check completed in {result:0.4f} seconds")


def daysCounter(day, weeks):
    if day % 7 == 0:
        weeks += 1
        weeksCounter(weeks)
    if day == 1:
        print("* 1 day is gone since I started looking at the website...")
    else:
        print("* ", day, " days are gone since I started looking at the webiste...")


def weeksCounter(week):
    if week == 1:
        MESSAGE = "Guten Tag. One week is gone since I started looking at the website, nothing found so far..."
        SendTelegramBotNotification.sendNotification(MESSAGE)
    else:
        MESSAGE = (
            "Guten Tag. ", week, " weeks are gone since I started looking at the website, nothing found so far...")
        SendTelegramBotNotification.sendNotification(MESSAGE)
