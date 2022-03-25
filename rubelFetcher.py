import pandas_datareader.data as web
import matplotlib.pyplot as plt
import random

COLORS = ["midnightblue", "navy", "darkblue", "mediumblue", "blue", "slateblue", "darkslateblue", "mediumslateblue", "mediumpurple",
        "rebeccapurple", "blueviolet", "indigo", "darkorchid", "darkviolet", "mediumorchid", "thistle", "plum", "violet", "purple",
        "darkmagenta", "fuchsia", "magenta", "orchid", "mediumvioletred", "deeppink", "hotpink", "lavenderblush", "palevioletred",
        "crimson", "pink", "lightpink", "ivory", "teal", "darkslategray", "dodgerblue", "steelblue", "lightslategray", "royalblue",
        "ghostwhite", "lavender", "cornflowerblue"]

def dataFetcher(startDate: str, endDate) -> str:
    colorId = random.randrange(0,40)
    color = COLORS[colorId]
    data = web.DataReader(name="RUBUSD=X", data_source="yahoo", start=startDate, end=endDate)
    plt.title("RUB/USD")
    plt.plot(data["Adj Close"], color=color)
    plt.savefig(f"RUB|USD{str(endDate)[:10]}.png")
    data.to_csv(f"RUB|USD{str(endDate)[:10]}.csv")
    return str(data["Adj Close"][-1])[:11]
