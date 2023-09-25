from django.db import models
from user.models import User
from uuid import uuid4


class Account(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_username = models.CharField(max_length=50, null=False)
    account_password = models.CharField(max_length=50, null=False)
    is_verified = models.BooleanField(default=False)
    account_type = models.CharField(max_length=20, null=True)
    cushion = models.FloatField(null=True)
    look_ahead_next_change = models.IntegerField(null=True)
    accrued_cash = models.FloatField(null=True)
    available_funds = models.FloatField(null=True)
    buying_power = models.FloatField(null=True)
    equity_with_loan_value = models.FloatField(null=True)
    excess_liquidity = models.FloatField(null=True)
    full_available_funds = models.FloatField(null=True)
    full_excess_liquidity = models.FloatField(null=True)
    full_init_margin_req = models.FloatField(null=True)
    full_main_t_margin_req = models.FloatField(null=True)
    gross_position_value = models.FloatField(null=True)
    init_margin_req = models.FloatField(null=True)
    look_ahead_available_funds = models.FloatField(null=True)
    look_ahead_excess_liquidity = models.FloatField(null=True)
    look_ahead_init_margin_req = models.FloatField(null=True)
    look_ahead_main_t_margin_req = models.FloatField(null=True)
    main_t_margin_req = models.FloatField(null=True)
    net_liquidation = models.FloatField(null=True)
    total_cash_value = models.FloatField(null=True)
    last_updated = models.DateTimeField(auto_now=True)


class StockInfo(models.Model):
    symbol = models.CharField(primary_key=True, max_length=10, unique=True)
    market_cap = models.BigIntegerField(null=True)
    average_volume = models.IntegerField(null=True)
    day_low = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    ask = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    ask_size = models.BigIntegerField(null=True)
    volume = models.IntegerField(null=True)
    open_price = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    fifty_two_week_high = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    fifty_two_week_low = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    bid = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    tradeable = models.BooleanField(null=True)
    bid_size = models.BigIntegerField(null=True)
    day_high = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    sector = models.CharField(max_length=30, null=True)
    long_business_summary = models.TextField(null=True)
    city = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=30, null=True)
    website = models.URLField(null=True)
    max_age = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=50, null=True)
    ebitda_margins = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    profit_margins = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    gross_margins = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    operating_cashflow = models.BigIntegerField(null=True)
    revenue_growth = models.FloatField(null=True)
    operating_margins = models.FloatField(null=True)
    ebitda = models.BigIntegerField(null=True)
    recommendation_key = models.CharField(max_length=15, null=True)
    gross_profits = models.BigIntegerField(null=True)
    free_cashflow = models.BigIntegerField(null=True)
    current_price = models.DecimalField(
        max_digits=9, decimal_places=2, null=True)
    current_ratio = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    return_on_assets = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    debt_to_equity = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    return_on_equity = models.DecimalField(
        max_digits=9, decimal_places=4, null=True)
    total_cash = models.BigIntegerField(null=True)
    total_debt = models.BigIntegerField(null=True)
    total_revenue = models.BigIntegerField(null=True)
    total_cash_per_share = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    financial_currency = models.CharField(max_length=7, null=True)
    revenue_per_share = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    quick_ratio = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    exchange = models.CharField(max_length=5, null=True)
    short_name = models.CharField(max_length=30, null=True)
    long_name = models.CharField(max_length=70, null=True)
    exchange_timezone_name = models.CharField(max_length=30, null=True)
    exchange_timezone_short_name = models.CharField(max_length=20, null=True)
    is_esg_populated = models.BooleanField(null=True)
    gmt_offset_milliseconds = models.CharField(max_length=10, null=True)
    quote_type = models.CharField(max_length=10, null=True)
    message_board_id = models.CharField(max_length=20, null=True)
    market = models.CharField(max_length=10, null=True)
    enterprise_to_revenue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    enterprise_to_ebitda = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    fifty_two_week_change = models.DecimalField(
        max_digits=9, decimal_places=5, null=True)
    shares_outstanding = models.BigIntegerField(null=True)
    book_value = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    last_fiscal_year_end = models.PositiveIntegerField(null=True)
    held_percent_institutions = models.DecimalField(
        max_digits=9, decimal_places=5, null=True)
    net_income_to_common = models.BigIntegerField(null=True)
    trailing_eps = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    s_and_p_52_week_change = models.DecimalField(
        max_digits=10, decimal_places=6, null=True)
    price_to_book = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    held_percent_insiders = models.DecimalField(
        max_digits=9, decimal_places=5, null=True)
    next_fiscal_year_end = models.PositiveIntegerField(null=True)
    most_recent_quarter = models.PositiveIntegerField(null=True)
    float_shares = models.BigIntegerField(null=True)
    beta = models.DecimalField(max_digits=9, decimal_places=5, null=True)
    enterprise_value = models.BigIntegerField(null=True)
    price_hint = models.SmallIntegerField(null=True)
    price_to_sales_trailing_12_months = models.DecimalField(
        max_digits=15, decimal_places=3, null=True)
    forward_p_e = models.FloatField(null=True)
    previous_close = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    regular_market_open = models.FloatField(null=True)
    two_hundred_day_average = models.FloatField(null=True)
    trailing_annual_dividend_yield = models.FloatField(null=True)
    payout_ratio = models.FloatField(null=True)
    regular_market_day_high = models.FloatField(null=True)
    average_daily_volume_10_day = models.IntegerField(null=True)
    regular_market_previous_close = models.DecimalField(
        max_digits=9, decimal_places=3, null=True)
    fifty_day_average = models.FloatField(null=True)
    trailing_annual_dividend_rate = models.CharField(max_length=50, null=True)
    average_volume_10_days = models.FloatField(null=True)
    regular_market_day_low = models.FloatField(null=True)
    currency = models.CharField(max_length=5, null=True)
    regular_market_volume = models.BigIntegerField(null=True)
    regular_market_price = models.FloatField(null=True)
    logo_url = models.URLField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.long_name)


class StockHistory(models.Model):
    stock = models.ForeignKey(
        StockInfo, on_delete=models.CASCADE, related_name="history")
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    volume = models.BigIntegerField(null=True)
    date = models.DateField(null=False)


class Watchlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="watchlists")
    name = models.CharField(max_length=30, null=False)
    date_created = models.DateTimeField(auto_now_add=True)


class WatchlistItem(models.Model):
    watchlist_id = models.ForeignKey(
        Watchlist, on_delete=models.CASCADE, related_name="items")
    stock_id = models.ForeignKey(
        StockInfo, on_delete=models.CASCADE, related_name="watched")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [["watchlist_id", "stock_id"]]


class Position(models.Model):
    account_id = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="positions")
    stock_id = models.ForeignKey(
        StockInfo, on_delete=models.PROTECT, related_name="positions")
    date_added = models.DateTimeField(auto_now_add=True)
