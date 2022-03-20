import pandas_datareader.data as web
import matplotlib.pyplot as plt

def dataFetcher(start_date: str, end_date) -> str:
    data = web.DataReader(name="RUBUSD=X", data_source="yahoo", start=start_date, end=end_date)
    plt.title("RUBEL/USD")
    plt.plot(data["Adj Close"])
    plt.savefig(f"RUB|USD{end_date}.png")
    data.to_csv(f"RUB|USD{end_date}.csv")
    return str(data["Adj Close"][-1])[:11]
