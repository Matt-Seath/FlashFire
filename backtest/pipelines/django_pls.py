from backtrader.feeds import PandasData
from django_pandas.io import read_frame
import pandas as pd


class DjangoDataFeed(PandasData):

    def __init__(self, queryset):
        self.queryset = queryset.values(
            "date", "open", "close", "high", "low", "volume")
        df = read_frame(self.queryset)

        df['datetime'] = pd.to_datetime(df['date'])
        df.set_index('datetime', inplace=True)
        self.p.dataname = df
        super().__init__()
