# PS5-scraper

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/PS5scrapermw_bot)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com)
[![Playstation 5](https://img.shields.io/badge/Playstation%205-003791?style=for-the-badge&logo=playstation-5&logoColor=white)](https://www.playstation.com/en-us/ps5/)
[![MIT License](https://img.shields.io/github/license/drew458/ps5-scraper?style=for-the-badge)](https://opensource.org/licenses/MIT)

BeautifulSoup scraper running queries on the website of the (in)famous Italian store.
The script is compatible with Python 3.x versions.

## Telegram Bot
If you just want to be notified when a PS5 becomes available at Mediaworld, add [the bot](https://t.me/PS5scrapermw_bot) to a Telegram group.

## Configuration
Before starting the script, you need to install the following external modules through CLI (Windows/Linux/Mac):
* `pip3 install requests` (HTTP(S) requests)
* `pip3 install bs4` (BeautifulSoup)

More briefly, just run:
* `pip3 install -r requirements.txt`

To run the script, `cd` into the folder and `python3 main.py`.

## Usage & Features

The refresh rate is configurable with adjustable delay.  
Configurable windows notifications (you just need to uncomment lines).  
Configurable Telegram bot notifications (change where your bot `token` and `chat_id` are stored; if you're thinking to deploy it on Heroku, see below).

## Cloud deployment

The script is ready for deployment on Heroku, which is what I use to run it on the cloud and get the Telegram bot notifications.  
The free tier on Heroku perfectly fits. In this case the bot token and chat it must go into the virtual environment variables (see the settings page on Heroku's dashboard).

## Future Updates
* Displaying some more stats about the usage and elapsed time.
* Add a GUI.
