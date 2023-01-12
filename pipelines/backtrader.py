from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime
from backtrader.feed import DataBase
from backtrader import date2num
from django.db import connection


class MySQLData(DataBase):
    params = (
        ('dbHost', None),
        ('dbUser', None),
        ('dbPWD', None),
        ('dbName', None),
        ('ticker', 'ISL'),
        ('fromdate', datetime.datetime.min),
        ('todate', datetime.datetime.max),
        ('name', ''),
    )

    def start(self):
        with connection.cursor as cursor:
            self.stockdata = cursor.execute(
                "SELECT id FROM stocks WHERE ticker LIKE '" + self.p.ticker + "' LIMIT 1")
            self.stock_id = self.stockdata.fetchone()[0]
            # self.result = self.engine.execute("SELECT `date`,`open`,`high`,`low`,`close`,`volume` FROM `eoddata` WHERE `stock_id` = 10 AND `date` between '"+self.p.fromdate.strftime("%Y-%m-%d")+"' and '"+self.p.todate.strftime("%Y-%m-%d")+"' ORDER BY `date` ASC")
            self.result = cursor.execute("SELECT `date`,`open`,`high`,`low`,`close`,`volume` FROM `eoddata` WHERE `stock_id` = " + str(
                self.stock_id) + " AND `date` between '"+self.p.fromdate.strftime("%Y-%m-%d")+"' and '"+self.p.todate.strftime("%Y-%m-%d")+"' ORDER BY `date` ASC")

    def _load(self):
        one_row = self.result.fetchone()
        if one_row is None:
            return False
        self.lines.datetime[0] = date2num(one_row[0])
        self.lines.open[0] = float(one_row[1])
        self.lines.high[0] = float(one_row[2])
        self.lines.low[0] = float(one_row[3])
        self.lines.close[0] = float(one_row[4])
        self.lines.volume[0] = int(one_row[5])
        self.lines.openinterest[0] = -1
        return True
