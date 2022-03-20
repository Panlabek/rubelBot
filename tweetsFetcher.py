import tweepy
import os

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN= os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=BEARER_TOKEN, access_token=ACCESS_KEY, access_token_secret=ACCESS_SECRET, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

def tweetContextFinder(queryString: str) -> list[str]:
    tweets = client.search_recent_tweets(query=queryString, max_results=100, expansions="author_id", user_fields=["profile_image_url"])
    return tweets
tweets = tweetContextFinder("from:hentaiavenger66 -is:retweet lang:en") #-is:reply
users = {u["id"]: u for u in tweets.includes["users"]}

for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(user.profile_image_url)

