import tweepy
from decouple import config
import datetime
from rubelFetcher import dataFetcher
from pepeRandomGenerator import getRandomPepe
import os
from rubelFetcher import dataFetcher
CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_KEY = config("ACCESS_KEY")
ACCESS_SECRET = config("ACCESS_SECRET")
BEARER_TOKEN = config("BEARER_TOKEN")
client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET,
                       bearer_token=BEARER_TOKEN)

auth=tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)

def replyToTags(usedTaggedTweets: list[str]):
    timeDiff = datetime.timedelta(minutes=70) 
    startTime = datetime.datetime.now() - timeDiff
    tweets = client.search_recent_tweets(query="@0xpiplup", start_time=startTime) 
    if tweets.data != None:
        for tweet in tweets.data:
            if tweet.id not in usedTaggedTweets:
                usedTaggedTweets.append(tweet.id)
                tweetData = tweet.text.split()
                if ("price" in tweetData) and (("chart" and "pepe") not in tweetData):
                    priceHandler(tweet=tweet)
                if ("chart" in tweetData) and (("price" and "pepe") not in tweetData):
                    chartHandler(tweet=tweet)
                if ("pepe" in tweetData) and (("price" and "chart") not in tweetData):
                    pepeHandler(tweet=tweet)

def priceHandler(tweet):
    startDate = datetime.datetime.now() - datetime.timedelta(days=365) 
    endDate = datetime.datetime.now()
    rubPrice = dataFetcher(startDate, endDate)
    resp = client.like(tweet_id=tweet.id)
    resp = client.create_tweet(in_reply_to_tweet_id=tweet.id, text=rubPrice)
    return resp

def chartHandler(tweet):
    endDate = datetime.datetime.now()
    if os.path.isfile(f"RUB|USD{str(endDate)[:10]}.png"):
        matplotlibImg = f"RUB|USD{str(endDate)[:10]}.png"
    else:
        startDate = datetime.datetime.now() - datetime.timedelta(days=365) 
        dataFetcher(startDate=startDate, endDate=endDate)
        matplotlibImg = f"RUB|USD{str(endDate)[:10]}.png"
    mediaId = [api.media_upload(matplotlibImg).media_id_string]
    resp = client.like(tweet_id=tweet.id)
    resp = client.create_tweet(in_reply_to_tweet_id=tweet.id, media_ids=mediaId)
    return resp

def pepeHandler(tweet):
    mediaId = [api.media_upload(getRandomPepe()).media_id_string]
    resp = client.like(tweet_id=tweet.id)
    resp = client.create_tweet(in_reply_to_tweet_id=tweet.id, media_ids=mediaId)
    return resp

