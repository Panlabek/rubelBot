import tweepy
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

# to be continued
def ukraineMemes():
    resp = client.search_recent_tweets(query="from:Ukraine -is:reply lang:en", tweet_fields=["text", "source", "context_annotations", "created_at"], max_results=10, # add start time to 1 minute
                                       media_fields=["preview_image_url"], expansions="attachments.media_keys")
    media = {m["media_key"]: m for m in resp.includes["media"]}
    for tweet in resp.data:
        if "attachments" in tweet.data:
            attachments = tweet.data["attachments"]
            media_keys = attachments["media_keys"]
            if media[media_keys[0]].preview_image_url:
                print(media[media_keys[0]].preview_image_url)
ukraineMemes()
