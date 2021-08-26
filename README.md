# PS5-scraper

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Playstation 5](https://img.shields.io/badge/Playstation%205-003791?style=for-the-badge&logo=playstation-5&logoColor=white)](https://www.playstation.com/en-us/ps5/)
[![MIT License](https://img.shields.io/github/license/drew458/ps5-scraper?style=for-the-badge)](https://opensource.org/licenses/MIT)

BeautifulSoup scraper running queries on the website of the (in)famous Italian store.
The script is compatible with Python 3.x versions.

## Telegram Bot

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/PS5scrapermw_bot)

If you just want to be notified when a PS5 becomes available at Mediaworld, add [the bot](https://t.me/PS5scrapermw_bot) to a Telegram group.

## Configuration
Before starting the script, you need to install the following external modules through CLI (Windows/Linux/Mac):
* `pip3 install requests` (HTTP(S) requests)
* `pip3 install bs4` (BeautifulSoup)

More briefly, just run:
* `pip3 install -r requirements.txt`

To launch the script (without arguments), `cd` into the folder and `python3 main.py`.

## Usage & Features

* The refresh rate is configurable with adjustable delay.  
* Configurable windows notifications (you just need to uncomment lines).  
* Configurable Telegram bot notifications (change where your bot `token` and `chat_id` are stored; if you're thinking to deploy it on Heroku, see below).

When launching the script you can pass it the following arguments:
```
  --help                  Show help                                                               
  --t                     The Telegram bot token.                                                 [string]
  --c                     The Telegram bot chat_id.                                               [string]
```

Example:
```
python3 main.py --t YOURTOKEN --c YOURCHATID
```


## Cloud deployment

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

The script is ready for deployment on Heroku, which is what I use to run it continuously on the cloud. The free tier on Heroku perfectly fits. In this case the Telegram bot token and chat it must go into the virtual environment variables (see the settings page on Heroku's dashboard).

## Future Updates
* Add Amazon as a website to scrape the PS5 availability.
* Add a GUI.
