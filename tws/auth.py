import os
from ib_insync import *
from dotenv import load_dotenv

from django.contrib.auth.models import User
from core.models import Account

load_dotenv()
ACCOUNT_NO = os.environ["ACCOUNT_NO"]


labels_to_snake_case = {
    'AccountType': 'account_type',
    'Cushion': 'cushion',
    'LookAheadNextChange': 'look_ahead_next_change',
    'AccruedCash': 'accrued_cash',
    'AvailableFunds': 'available_funds',
    'BuyingPower': 'buying_power',
    'EquityWithLoanValue': 'equity_with_loan_value',
    'ExcessLiquidity': 'excess_liquidity',
    'FullAvailableFunds': 'full_available_funds',
    'FullExcessLiquidity': 'full_excess_liquidity',
    'FullInitMarginReq': 'full_init_margin_req',
    'FullMaintMarginReq': 'full_main_t_margin_req',
    'GrossPositionValue': 'gross_position_value',
    'InitMarginReq': 'init_margin_req',
    'LookAheadAvailableFunds': 'look_ahead_available_funds',
    'LookAheadExcessLiquidity': 'look_ahead_excess_liquidity',
    'LookAheadInitMarginReq': 'look_ahead_init_margin_req',
    'LookAheadMaintMarginReq': 'look_ahead_main_t_margin_req',
    'MaintMarginReq': 'main_t_margin_req',
    'NetLiquidation': 'net_liquidation',
    'TotalCashValue': 'total_cash_value'
}


def update_account():
    # util.startLoop()  # uncomment this line when in a notebook

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)
    account = ib.accountSummary(ACCOUNT_NO)

    data = dict()
    data["pk"] = ACCOUNT_NO
    user = User.objects.get(pk=1)
    data["user_id"] = user

    for item in account:
        data[labels_to_snake_case[item.tag]] = item.value

    entry = Account(**data)
    try:
        entry.save()
        print("Success!")
    except Exception as e:
        print(e)

    ib.disconnect()


def get_watchlists():

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=2)

    # Get the list of managed accounts
    accounts = ib.managedAccounts()

    # Get the watchlists for the first managed account
    ib.reqAccountUpdatesMulti(accounts[0], modelCode='')

    # Wait for updates to be received
    while ib.waitOnUpdate(timeout=9):
        ib.updateMktDepth(False)
        ib.updateAccountValue(False)

    # Get the watchlists for the first managed account
    watchlists = ib.watchlists()

    # Print the watchlist information
    for watchlist in watchlists:
        print(f"Watchlist: {watchlist.name}")
        for contract in watchlist.contracts:
            print(f"Symbol: {contract.symbol}, Exchange: {contract.exchange}")

    # Disconnect from TWS/IBGW
    ib.disconnect()


def main():
    update_account()


if __name__ == "__main__":
    main()
