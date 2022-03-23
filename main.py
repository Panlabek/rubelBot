import datetime

from rubelFetcher import dataFetcher
from tweetPoster import rubTweetPoster
from placeGenerator import getRandomUkrainianCity
from replyReplier import replyToReplies
# from ukraineMemes import rtUkraine this needs to get fixed
import pytz

def main():
    tweets = []
    usedTweetList = []
    try:
        while True:
            if int(datetime.datetime.now().astimezone(pytz.utc).strftime("%H")) == 13 and len(tweets) == 0:
                start_date = str(datetime.datetime.now())[:10].split("-")
                start_date[2] = str(int(start_date[2]) - 15)
                start_date = "-".join(start_date)
                start_date = datetime.datetime.now() - datetime.timedelta(days=365) 
                end_date = datetime.datetime.now()
                rubPrice = dataFetcher(start_date, end_date)
                random_place = getRandomUkrainianCity()
                matplotlibImg = f"RUB|USD{str(end_date)[:10]}.png"
                tweets.append("Tweeted")
                rubTweetPoster(rub_price=rubPrice, matplotlib_img=matplotlibImg,
                               place_id=random_place)
            if int(datetime.datetime.now().astimezone(pytz.utc).strftime("%H")) == 14 and len(tweets) > 0:
                tweets.clear()
            if int(datetime.datetime.now().astimezone(pytz.utc).strftime("%M")) % 2 == 0 and int(datetime.datetime.now().astimezone(pytz.utc).strftime("%S")) == 0:
                replyToReplies(usedTweetList)
                 
    except KeyboardInterrupt:
        print("Bot has been stopped")

if __name__ == "__main__":
    main()

