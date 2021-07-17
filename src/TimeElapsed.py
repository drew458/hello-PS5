from src import Stats


def checkDaysWeeksElapsed(count, days, weeks):
    if (count % 144) == 0:
        days += 1
        count = 0
        Stats.daysCounter(days, weeks)
    return count
