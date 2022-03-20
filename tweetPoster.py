import tweepy
import os
from priceConverter import convertFromRtoP, convertFromRtoE
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
# BEARER_TOKEN = os.getenv("BEARER_TOKEN")
auth=tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)
def rubTweetPoster(rub_price: str, matplotlib_img: str, pepe_image: str, place_id: str):
    # client.create_tweet(text=f"RUB/USD price: {rub_price}", place_id=place_id) 
    gbp_converted = convertFromRtoP(rubelPrice=rub_price)
    eur_converted = convertFromRtoE(rubelPrice=rub_price)
    tweet_text = f"RUB-USD price: {rub_price}\n" \
                f"RUB-EUR price: {eur_converted}\n" \
                f"RUB-GBP price: {gbp_converted}"
    images = (pepe_image, matplotlib_img)
    media_ids = [api.media_upload(i).media_id_string for i in images]
    api.update_status(media_ids=media_ids, status=tweet_text, place_id=place_id)
    # api.update_status_with_media(tweet_text, pepe_image)
