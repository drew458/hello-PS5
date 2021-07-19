def checkH1(strings_h1, text_h1):
    """Checks if the string in h1 tags is present.

        :param strings_h1: A list with all the strings contained in the H1 tags.
        :param text_h1: the string to look for inside the tags.
        :return: True if the text is present in the tags, False otherwise
        :rtype: Boolean
    """

    for i in strings_h1:
        if i.string == text_h1:
            return True
    return False

# Check if the string in h3 class is present
# def checkH3(soup_h3, texth3):
    """Checks if the string in h3 tags is present.

            :param strings_h3: A list with all the strings contained in the H3 tags.
            :param text_h3: the string to look for inside the tags.
            :return: True if the text is present in the tags, False otherwise
            :rtype: Boolean
    """

#    for i in soup_h3:
#        if i.string == texth3:
#            return True
#    return False
