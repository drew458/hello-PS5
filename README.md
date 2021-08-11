# PS5-scraper

[![MIT License](https://img.shields.io/github/license/drew458/ps5-scraper)](https://opensource.org/licenses/MIT)

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
