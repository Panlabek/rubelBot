import datetime

from rubelFetcher import dataFetcher
from tweetPoster import rubTweetPoster
from placeGenerator import getRandomUkrainianCity
from replyReplier import replyToReplies
# from ukraineMemes import rtUkraine this needs to get fixed
import pytz

def main():
    tweets, usedTweetList = [], []
    try:
        while True:
            utc_time = datetime.datetime.now().astimezone(pytz.utc)
            if int(utc_time.strftime("%H")) == 13 and len(tweets) == 0:
                start_date = datetime.datetime.now() - datetime.timedelta(days=365) 
                end_date = datetime.datetime.now()
                rubPrice = dataFetcher(start_date, end_date)
                matplotlibImg = f"RUB|USD{str(end_date)[:10]}.png"
                tweets.append("Tweeted")
                rubTweetPoster(rub_price=rubPrice, matplotlib_img=matplotlibImg,
                               place_id=getRandomUkrainianCity())
            if int(utc_time.strftime("%H")) == 14 and len(tweets) > 0:
                tweets.clear()
            if int(utc_time.strftime("%M")) % 2 == 0 and int(utc_time.strftime("%S")) == 0:
                replyToReplies(usedTweetList)
                 
    except KeyboardInterrupt:
        print("Bot has been turned off")

if __name__ == "__main__":
    main()

