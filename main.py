# add rubel csv database
#===================================================================
import datetime

from rubelFetcher import dataFetcher
from pepeRandomGenerator import getRandomPepe
from tweetPoster import rubTweetPoster
from placeGenerator import getRandomUkrainianCity
from replyReplier import replyToReplies
from ukraineMemes import rtUkraine
import pytz

def main():
    hasTweeted = False
    if int(datetime.datetime.now().astimezone(pytz.utc).strftime("%H")) == 13 and hasTweeted == False:
        hasTweeted = True
        start_date = str(datetime.datetime.now())[:10].split("-")
        start_date[2] = str(int(start_date[2]) - 15)
        start_date = "-".join(start_date)
        start_date = datetime.datetime.now() - datetime.timedelta(days=365) 
        end_date = datetime.datetime.now()
        rubPrice = dataFetcher(start_date, end_date)
        pepe_path = getRandomPepe()
        random_place = getRandomUkrainianCity()
        matplotlibImg = f"RUB|USD{str(end_date)[:10]}.png"
        rubTweetPoster(rub_price=rubPrice, matplotlib_img=matplotlibImg,
                       pepe_image=pepe_path, place_id=random_place)
        if int(datetime.datetime.now().astimezone(pytz.utc).strftime("%H")) == 14 and hasTweeted == True:
            hasTweeted = False
        if int(datetime.datetime.now().astimezone(pytz.utc).strftime("%M")) <= 2:
            replyToReplies(getRandomPepe(), getRandomPepe())
            rtUkraine()

if __name__ == "__main__":
    main()

