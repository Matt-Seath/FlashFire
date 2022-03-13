import alpaca_trade_api as ata
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Alpaca API using sercet API keys
api = ata.REST(os.environ.get('ALPACA_KEY'), os.environ.get('ALPACA_SECRET'), 
      base_url=os.environ.get('PAPER_URL'))

bar_sets = api.get_barset(['AAPL','TSLA'], 'day')
print (bar_sets)
