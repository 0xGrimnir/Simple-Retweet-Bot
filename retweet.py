# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Tyler L. Jones || CyberVox
# Date: Saturday, May 20th - 2017.
# License: MIT License.

import tweepy
from LastRetweet import LastRetweet
import dateparser
import pickle
from time import sleep

# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.
from settings import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    file_lastRetweet = open('lastRetweet.obj', 'rb')
    test = pickle.load(file_lastRetweet)
    file_lastRetweet.close()

except FileNotFoundError:
    print("No last retweet")

except TypeError:
    print("Arg type error")

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!
fetchedTweets = []
for tweet in tweepy.Cursor(api.search, q=hashtag).items(20):
    fetchedTweets.append(tweet)

for tweet in reversed(fetchedTweets):
    try:
        # print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
        print(tweet.created_at)

        # print('Retweet published successfully.')
        if tweet == fetchedTweets[0]:
            lastRetweet = LastRetweet(tweet)
            file_lastRetweet = open('lastRetweet.obj', 'wb')
            pickle.dump(lastRetweet, file_lastRetweet)
            file_lastRetweet.close()
            print(lastRetweet.id)

        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!


    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
