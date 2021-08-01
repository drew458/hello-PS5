import time

from src import Stats


def checkDaysWeeksElapsed(count, days, weeks):
    """

    :param count: the number of checks performed
    :param days: the number of days elapsed
    :param weeks: the number of weeks elapsed
    :return: the number of checks performed (0 if one day has gone).
    """
    if (count % 144) == 0:
        days += 1
        count = 0
        Stats.daysCounter(days, weeks)
    return count


def countdown(t):
    """
    Performs a countdown from the parameter time to 0.
    :param t: input time in seconds
    """
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, "until the next try...", end="\r")
        time.sleep(1)
        t -= 1

    print()
    print('Here we go!')
