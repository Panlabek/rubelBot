import datetime

from rubelFetcher import dataFetcher
from tweetPoster import rubTweetPoster
from placeGenerator import getRandomUkrainianCity
from replyReplier import replyToReplies
# from ukraineMemes import rtUkraine this needs to get fixed
from tagReplier import replyToTags
import pytz

def main():
    tweets, usedTweetList = [], []
    usedTaggedTweets = []
    try:
        while True:
            utcTime = datetime.datetime.now().astimezone(pytz.utc)
            if int(utcTime.strftime("%H")) == 13 and len(tweets) == 0:
                startDate = datetime.datetime.now() - datetime.timedelta(days=365) 
                endDate = datetime.datetime.now()
                rubPrice = dataFetcher(startDate, endDate)
                matplotlibImg = f"RUB|USD{str(endDate)[:10]}.png"
                tweets.append("Tweeted")
                rubTweetPoster(rubPrice=rubPrice, matplotlibImg=matplotlibImg,
                               placeId=getRandomUkrainianCity())
            if int(utcTime.strftime("%H")) == 14 and len(tweets) > 0:
                resp = tweets.clear()
            if int(utcTime.strftime("%M")) % 2 == 0 and int(utcTime.strftime("%S")) == 0:
                replyToReplies(usedTweetList)
            if int(utcTime.strftime("%M")) % 2 == 0 and int(utcTime.strftime("%S")) == 30:
                replyToTags(usedTaggedTweets=usedTaggedTweets)
    except KeyboardInterrupt:
        print("Bot has been turned off")

if __name__ == "__main__":
    main()

