import os
import urllib
import requests


def sendNotification():
    TOKEN = os.environ["TOKEN"]
    CHAT_ID = os.environ["CHAT_ID"]

    notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        TOKEN, CHAT_ID, urllib.parse.quote_plus('FOUND!!!! Go check it out now!'))
    _ = requests.get(notification_url, timeout=10)