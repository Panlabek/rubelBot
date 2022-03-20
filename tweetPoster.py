import tweepy
import os
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
# BEARER_TOKEN = os.getenv("BEARER_TOKEN")
auth=tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)
def rubTweetPoster(rub_price: int, matplotlib_img: str, pepe_image: str, place_id: str):
    # client.create_tweet(text=f"RUB/USD price: {rub_price}", place_id=place_id) 
    tweet_text = f"RUB-USD price: {rub_price}"
    images = (pepe_image, matplotlib_img)
    media_ids = [api.media_upload(i).media_id_string for i in images]
    api.update_status(media_ids=media_ids, status=tweet_text)
    # api.update_status_with_media(tweet_text, pepe_image)
