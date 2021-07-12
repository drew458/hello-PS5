FOUND_MESSAGE = "FOUND IT! Go check it out now at games.mediaworld.it"
START_MESSAGE = "HI! I'm a PS5-availability finder in the MediaWorld website. Let's see if I can find something..."


def printStartMessage():
    print(START_MESSAGE)
    print()


def printFoundMessage():
    print(FOUND_MESSAGE)


def printCheckMessage(count):
    print("Check number", count, ", nothing found, i'll keep trying...")
    print()


def printWaitingStatsMessage():
    print("While I'm waiting, let's see some stats about the execution...")


def getFoundMessage():
    return FOUND_MESSAGE
