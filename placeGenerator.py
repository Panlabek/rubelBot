import random

def getRandomUkrainianCity() -> str:
    cities = ["Kyiv", "Kharkiv","Odessa","Dnipro","Donetsk","Zaporizhzhia","Lviv",
            "Kryvyi Rih", "Mykolaiv", "Sevastopol", "Mariupol", "Luhansk", "Vinnytsia",
            "Makiivka", "Simferopol", "Chernihiv", "Kherson", "Poltava", "Zhytomyr", "Brovary"] 
    num = random.randrange(0,19)
    return cities[num]
