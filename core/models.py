from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cash = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)


class Stock(models.Model):
    symbol = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)

class StockPriceMinute(models.Model):
    open = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    high = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    low = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    close = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    volume = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    datetime = models.DateTimeField(auto_now_add=True)

class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="watchlist")


class StockHistory(models.Model):
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="history") 



class StockInfo(models.Model):
    symbol = models.CharField(primary_key=True, max_length=10, unique=True)
    marketCap = models.CharField(max_length=50, null=True)
    averageVolume = models.CharField(max_length=50, null=True)
    dayLow = models.CharField(max_length=50, null=True)
    ask = models.CharField(max_length=50, null=True)
    askSize = models.CharField(max_length=50, null=True)
    volume = models.IntegerField(null=True)
    fiftyTwoWeekHigh = models.CharField(max_length=50, null=True)
    fiftyTwoWeekLow = models.CharField(max_length=50, null=True)
    bid = models.FloatField(null=True)
    tradeable = models.BooleanField(null=True)
    bidSize = models.BigIntegerField(null=True)
    dayHigh = models.FloatField(null=True)
    sector = models.CharField(max_length=50, null=True)
    longBusinessSummary = models.TextField(null=True)
    city = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)
    maxAge = models.PositiveIntegerField(null=True)
    address1 = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=50, null=True)
    ebitdaMargins = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    profitMargins = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    grossMargins = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    operatingCashflow = models.BigIntegerField(null=True)
    revenueGrowth = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    operatingMargins = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    ebitda = models.BigIntegerField(null=True)
    recommendationKey = models.CharField(max_length=15, null=True)
    grossProfits = models.BigIntegerField(null=True)
    freeCashflow = models.BigIntegerField(null=True)
    currentPrice = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    currentRatio = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    returnOnAssets = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    debtToEquity = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    returnOnEquity = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    totalCash = models.BigIntegerField(null=True)
    totalDebt = models.BigIntegerField(null=True)
    totalRevenue = models.BigIntegerField(null=True)
    totalCashPerShare = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    financialCurrency = models.CharField(max_length=7, null=True)
    revenuePerShare = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    quickRatio = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    exchange = models.CharField(max_length=5, null=True)
    shortName = models.CharField(max_length=50, null=True)
    longName = models.CharField(max_length=80, null=True)
    exchangeTimezoneName = models.CharField(max_length=50, null=True)
    exchangeTimezoneShortName = models.CharField(max_length=20, null=True)
    isEsgPopulated = models.BooleanField(null=True)
    gmtOffsetMilliseconds = models.CharField(max_length=10, null=True)
    quoteType = models.CharField(max_length=10, null=True)
    messageBoardId = models.CharField(max_length=20, null=True)
    market = models.CharField(max_length=20, null=True)
    enterpriseToRevenue = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    enterpriseToEbitda = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    fiftyTwoWeekChange = models.DecimalField(max_digits=9, decimal_places=5, null=True)
    sharesOutstanding = models.BigIntegerField(null=True)
    bookValue = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    lastFiscalYearEnd = models.PositiveIntegerField(null=True)
    heldPercentInstitutions = models.DecimalField(max_digits=9, decimal_places=5, null=True)
    netIncomeToCommon = models.BigIntegerField(null=True)
    trailingEps = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    sandp52WeekChange = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    priceToBook = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    heldPercentInsiders = models.DecimalField(max_digits=9, decimal_places=5, null=True)
    nextFiscalYearEnd = models.PositiveIntegerField(null=True)
    mostRecentQuarter = models.PositiveIntegerField(null=True)
    floatShares = models.BigIntegerField(null=True)
    beta = models.DecimalField(max_digits=9, decimal_places=5, null=True)
    enterpriseValue = models.BigIntegerField(null=True)
    priceHint = models.SmallIntegerField(null=True)
    priceToSalesTrailing12Months = models.DecimalField(max_digits=15, decimal_places=3, null=True)
    forwardPe = models.FloatField(null=True)
    previousClose = models.FloatField(null=True)
    regularMarketOpen = models.FloatField(null=True)
    twoHundredDayAverage = models.FloatField(null=True)
    trailingAnnualDividendYield = models.FloatField(null=True)
    payoutRatio = models.FloatField(null=True)
    regularMarketDayHigh = models.CharField(max_length=50, null=True)
    averageDailyVolume10Day = models.CharField(max_length=50, null=True)
    regularMarketPreviousClose = models.CharField(max_length=50, null=True)
    fiftyDayAverage = models.CharField(max_length=50, null=True)
    trailingAnnualDividendRate = models.CharField(max_length=50, null=True)
    openPrice = models.CharField(max_length=50, null=True)
    averageVolume10days = models.CharField(max_length=50, null=True)
    regularMarketDayLow = models.CharField(max_length=50, null=True)
    currency = models.CharField(max_length=50, null=True)
    regularMarketVolume = models.CharField(max_length=50, null=True)
    regularMarketPrice = models.FloatField(null=True)
    logoUrl = models.URLField(null=True)