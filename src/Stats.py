import time


def performanceCounter():
    return time.perf_counter()


def getPerformanceResult(start, finish):
    return finish - start


def printPerformanceResult(result):
    print(f"Webpage and tags scraped in {result:0.4f} seconds")


def daysCounter(day):
    if day == 1:
        print("1 day is gone since I started looking at the website...")
    else:
        print("", day, " days are gone since i started looking at the webiste...")
