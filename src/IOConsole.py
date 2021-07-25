FOUND_MESSAGE = "FOUND IT! Go check it out now at games.mediaworld.it"
START_MESSAGE = "HI! I'm a PS5-availability finder in the MediaWorld website. Let's see if I can find something..."


def printStartMessage():
    print(START_MESSAGE)
    print()


def printFoundMessage():
    print(FOUND_MESSAGE)


def printCheckNumberMessage(count):
    print("Check number", count, ", nothing found, I won't give up...")


def printWaitingStatsMessage():
    print("While waiting, let's see some stats about the execution...")


def getFoundMessage():
    return FOUND_MESSAGE
