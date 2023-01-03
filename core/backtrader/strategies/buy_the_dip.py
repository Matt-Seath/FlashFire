import backtrader as bt
import yfinance as yf

data = yf.download("BTC-USD", start="2022-12-12")
data.head()