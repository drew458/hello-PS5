import time

from src import Stats


def checkDaysWeeksElapsed(count, days, weeks):
    if (count % 144) == 0:
        days += 1
        count = 0
        Stats.daysCounter(days, weeks)
    return count


# input time in seconds
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, "until the next try...", end="\r")
        time.sleep(1)
        t -= 1

    print('Here we go!')
