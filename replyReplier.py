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
    minuser = datetime.timedelta(minutes=70) 
    start_time = datetime.datetime.now() - minuser
    tweets = client.search_recent_tweets(query="to:0xpiplup", start_time=start_time) 
    if tweets.data != None:
        for tweet in tweets.data:
            if tweet.id not in usedTweets:
                usedTweets.append(tweet.id)
                images = (getRandomPepe(), getRandomPepe())
                media_ids = [api.media_upload(i).media_id_string for i in images]
                client.like(tweet_id=tweet.id)
                client.create_tweet(in_reply_to_tweet_id=tweet.id, media_ids=media_ids)
