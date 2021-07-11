from src import stats


def checkTime(count, days, weeks):
    if (count % 144) == 0:
        days += 1
        count = 0
        stats.daysCounter(days, weeks)
    return count
