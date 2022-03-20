# TODO 1
# every time on 1:30 pm local time fetch price of rubel(ohlc) PARTIALY DONE
# create and save matplotlib rubel chart DONE
# save newest rubel price to variable DONE
# OPTIONAL
# add it to database
# TODO 2 
# check if ukraine has some memes posted
# if yes retweet it
# TODO 3 
# if its week
# create twitter post that has 
# rubel/usd price
# rubel/gbp price
# rubel/zapsy price
# add matplotlib chart to media and add random frog meme
# if weekend only post memes and retweet ukraine
# if someone replies to post, reply with a meme to him
#===================================================================
import datetime
from rubelFetcher import dataFetcher

def main():
    # start_date = str(datetime.datetime.now())[:10].split("-")
    # start_date[2] = str(int(start_date[2]) - 15)
    # start_date = "-".join(start_date)
    start_date = "2020-01-1"
    end_date = str(datetime.datetime.now())[:10]
    resp = dataFetcher(start_date, end_date)
    print(resp)

if __name__ == "__main__":
    main()

