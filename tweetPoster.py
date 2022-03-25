import tweepy
from priceConverter import convertFromRtoP, convertFromRtoE
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
def rubTweetPoster(rubPrice: str, matplotlibImg: str, placeId: str):
    gbpConverted = convertFromRtoP(rubelPrice=rubPrice)
    eurConverted = convertFromRtoE(rubelPrice=rubPrice)
    tweetText = f"RUB-USD price: {rubPrice}\n" \
                f"RUB-EUR price: {eurConverted}\n" \
                f"RUB-GBP price: {gbpConverted}"
    images = (getRandomPepe(), matplotlibImg)
    mediaIds = [api.media_upload(i).media_id_string for i in images]
    tweet = client.create_tweet(text=tweetText, media_ids=mediaIds, place_id=placeId)
    return tweet
