import backtrader as bt
import backtrader.stores.ibstore as ibstore

def start():
    print("starting backtrader..")
    cerebro = bt.Cerebro()

    store = ibstore.IBStore(port=7496)
    data = store.getdata(
        dataname="MSFT", secType="STK", exchange="SMART", timeframe=bt.TimeFrame.TimeFrame.Seconds)
    cerebro.resampledata(data, timeframe=bt.TimeFrame.TimeFrame.Seconds, compression=15)

    cerebro.run()
start()