import datetime
import tweepy
from decouple import config
from pepeRandomGenerator import getRandomPepe
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

def replyToReplies(usedTweets: list[str]) -> str:
    timeDiff = datetime.timedelta(minutes=70) 
    startTime = datetime.datetime.now() - timeDiff
    tweets = client.search_recent_tweets(query="to:0xpiplup", start_time=startTime)
    if tweets.data != None:
        for tweet in tweets.data:
            if tweet.id not in usedTweets:
                tweetData = tweet.text.split()
                if tweetData.count("@0xpiplup") < 2:
                    usedTweets.append(tweet.id)
                    pepeId = api.media_upload(getRandomPepe()).media_id_string
                    pepeId = [pepeId]
                    resp = client.like(tweet_id=tweet.id)
                    resp = client.create_tweet(in_reply_to_tweet_id=tweet.id, media_ids=pepeId)
                    return resp
