import os

import urllib
import requests


def sendNotification(token, chat_id, found_message):
    """
    Sends a Telegram notification via a bot.
    """

    # Retain the Telegram Bot token from environment variables
    try:
        TOKEN = os.environ["TOKEN"]
    except KeyError:
        TOKEN = token

    # Retain the Telegram chat_id from environment variables
    try:
        CHAT_ID = os.environ["CHAT_ID"]
    except KeyError:
        CHAT_ID = chat_id

    # Send notification
    notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        TOKEN, CHAT_ID, urllib.parse.quote_plus(found_message))
    _ = requests.get(notification_url, timeout=10)
