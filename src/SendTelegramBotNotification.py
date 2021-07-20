import os

import urllib
import requests


def sendNotification(found_message):
    """
    Sends a Telegram notification via a bot.
    """

    # Retain the Telegram Bot token from environment variables
    TOKEN = os.environ["TOKEN"]
    # Retain the Telegram chat_id from environment variables
    CHAT_ID = os.environ["CHAT_ID"]

    # Send notification
    notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        TOKEN, CHAT_ID, urllib.parse.quote_plus(found_message))
    _ = requests.get(notification_url, timeout=10)
