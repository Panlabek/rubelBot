import datetime
import tweepy
import os
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET,
                       bearer_token=BEARER_TOKEN)

auth=tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)

def replyToReplies(pepe_image: str, pepe_image2: str):
    minuser = datetime.timedelta(minutes=80) # some kind of god created time delta
    start_time = datetime.datetime.now() - minuser
    tweets = client.search_recent_tweets(query="to:0xpiplup", start_time=start_time) 
    if tweets.data != None:
        for tweet in tweets.data:
            images = (pepe_image, pepe_image2)
            media_ids = [api.media_upload(i).media_id_string for i in images]
            client.create_tweet(in_reply_to_tweet_id=tweet.id, media_ids=media_ids)
