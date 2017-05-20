# Twitter Retweet Bot using Python & Tweepy
A Python-built Twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword value.

What You Need && Need to Know
----------

* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.

`pip install tweepy`

* Make sure you fully understand [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam! 

Instructions
----------

* Out of general OS hygiene, create a new directory to contain all of your retweet bot files.

`mkdir retweet-bot`

* Create a new [Twitter Application](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
* Fill in your keys, tokens, and secrets in the keys.py file.
* Check comments in retweet.py to tweak the retweet bot to your liking.
* Run your retweet.py script. Enjoy! 

`python retweet.py`

Additional Information
----------
* Note: Make sure that your retweet.py and keys.py files are, obviously, in the same directory.
* Create a [Cron Job](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800) or use [Task Scheduler](https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx) to automate this script.
* Consider using a Raspberry Pi to host your retweet bot, so it's always on and always running. :)
