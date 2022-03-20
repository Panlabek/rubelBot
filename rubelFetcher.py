import pandas_datareader.data as web
import matplotlib.pyplot as plt
import random

COLORS = ["midnightblue", "navy", "darkblue", "mediumblue", "blue", "slateblue", "darkslateblue", "mediumslateblue", "mediumpurple",
        "rebeccapurple", "blueviolet", "indigo", "darkorchid", "darkviolet", "mediumorchid", "thistle", "plum", "violet", "purple",
        "darkmagenta", "fuchsia", "magenta", "orchid", "mediumvioletred", "deeppink", "hotpink", "lavenderblush", "palevioletred",
        "crimson", "pink", "lightpink", "ivory", "teal", "darkslategray", "dodgerblue", "steelblue", "lightslategray", "royalblue",
        "ghostwhite", "lavender", "cornflowerblue"]

def dataFetcher(start_date: str, end_date) -> str:
    color_id = random.randrange(0,40)
    color = COLORS[color_id]
    data = web.DataReader(name="RUBUSD=X", data_source="yahoo", start=start_date, end=end_date)
    plt.title("RUB/USD")
    plt.plot(data["Adj Close"], color=color)
    plt.savefig(f"RUB|USD{str(end_date)[:10]}.png")
    data.to_csv(f"RUB|USD{str(end_date)[:10]}.csv")
    return str(data["Adj Close"][-1])[:11]
