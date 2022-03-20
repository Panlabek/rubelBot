# TODO 1
# every time on 1:30 pm local time fetch price of rubel(ohlc) PARTIALY DONE
# create and save matplotlib rubel chart DONE
# save newest rubel price to variable DONE
# OPTIONAL
# add it to database
# TODO 2 
# if its week
# create twitter post that has 
# rubel/usd price
# rubel/gbp price
# rubel/zapsy price
# add matplotlib chart to media and add random frog meme
# if weekend only post memes and retweet ukraine
# if someone replies to post, reply with a meme to him
# TODO 3
# check if ukraine has some memes posted
# if yes retweet it
# TODO 4
# pepe.py that generates random pepe image
# TODO 5
# place id randomly generates place names
#===================================================================
import datetime
from rubelFetcher import dataFetcher
from pepeRandomGenerator import getRandomPepe
from tweetPoster import rubTweetPoster

def main():
    # start_date = str(datetime.datetime.now())[:10].split("-")
    # start_date[2] = str(int(start_date[2]) - 15)
    # start_date = "-".join(start_date)
    start_date = "2020-01-1"
    end_date = str(datetime.datetime.now())[:10]
    rubPrice = dataFetcher(start_date, end_date)
    pepe_path = getRandomPepe()
    matplotlibImg = "RUB|USD2022-03-20.png"
    rubTweetPoster(rub_price=rubPrice, matplotlib_img=matplotlibImg,
                   pepe_image=pepe_path, place_id="Goblin Town")

if __name__ == "__main__":
    main()

