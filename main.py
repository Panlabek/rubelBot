# TODO 1
# every time on 1:30 pm local time fetch price of rubel(ohlc) PARTIALY DONE
# TODO 2 
# if its week
# if weekend only post memes and retweet ukraine
# check if ukraine has some memes posted
# if yes retweet it
# OPTIONAL
# rubel/zapsy price
# add rubel csv database
#===================================================================
import datetime

from rubelFetcher import dataFetcher
from pepeRandomGenerator import getRandomPepe
from tweetPoster import rubTweetPoster
from placeGenerator import getRandomUkrainianCity
from replyReplier import replyToReplies

def main():
    start_date = str(datetime.datetime.now())[:10].split("-")
    start_date[2] = str(int(start_date[2]) - 15)
    start_date = "-".join(start_date)
    start_date = datetime.datetime.now() - datetime.timedelta(days=365) 
    end_date = datetime.datetime.now()
    rubPrice = dataFetcher(start_date, end_date)
    pepe_path = getRandomPepe()
    random_place = getRandomUkrainianCity()
    matplotlibImg = "RUB|USD2022-03-20.png"
    rubTweetPoster(rub_price=rubPrice, matplotlib_img=matplotlibImg,
                   pepe_image=pepe_path, place_id=random_place)
    # replyToReplies(getRandomPepe(), getRandomPepe())

if __name__ == "__main__":
    main()

