import os
import requests


def sendNotification(message):
    # Retain the Telegram Bot token from os environment variables
    TOKEN = os.environ["TOKEN"]
    # Retain the Telegram chat_id from os environment variables
    CHAT_ID = os.environ["CHAT_ID"]

    # Send notification
    notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=Markdown&text=%s' % (
        TOKEN, CHAT_ID, message)
    notify = requests.get(notification_url, timeout=10)