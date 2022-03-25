import numpy
import yfinance as yahooFinance
def convertFromRtoP(rubelPrice: str) -> str:
    gbpRatio = yahooFinance.Ticker("GBPUSD=X").info
    gbpPrice = str(numpy.float64(rubelPrice) / gbpRatio["ask"])
    return gbpPrice[:11]
def convertFromRtoE(rubelPrice: str) -> str:
    euroRatio = yahooFinance.Ticker("EURUSD=X").info
    eurPrice = str(numpy.float64(rubelPrice) / euroRatio["ask"])
    return eurPrice[:11]
