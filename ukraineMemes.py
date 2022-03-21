import tweepy
import datetime
import os
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET)
def rtUkraine():
    minuser = datetime.timedelta(minutes=80) # some kind of god created time delta
    start_time = datetime.datetime.now() - minuser
    tweets = client.search_recent_tweets(query="from:ukraine -is:reply", start_time=start_time)
    if tweets.data != None:
        for tweet in tweets:
            client.retweet(tweet_id=tweet.id)
        
