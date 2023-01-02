import backtrader as bt

from atreyu_backtrader_api import IBData
import test_printer

import datetime as dt
from datetime import datetime, date, time

cerebro = bt.Cerebro()


data = IBData(host='127.0.0.1', port=7496, clientId=35,
               name="AAPL",  # Data name
               dataname='AAPL',     # Symbol name
               secType='STK',       # SecurityType is STOCK 
               exchange='SMART',    # Trading exchange IB's SMART exchange 
               currency='USD',      # Currency of SecurityType
               backfill_start=False,
               backfill=False,
               what='TRADES', # TRADES or MIDPOINT
               rtbar=True
              )

cerebro.adddata(data)

# Add the test strategy
cerebro.addstrategy(test_printer.TestPrinter)

cerebro.run()