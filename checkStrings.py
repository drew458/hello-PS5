def checkH1(soup_h1, texth1):
    for i in soup_h1:
        if i.string == texth1:
            return True
    return False


def checkH3(soup_h3, texth3):
    for i in soup_h3:
        if i.string == texth3:
            return True
    return False