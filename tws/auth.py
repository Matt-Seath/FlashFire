from ib_insync import *


def get_account_info():
    # util.startLoop()  # uncomment this line when in a notebook

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)

    account = ib.accountSummary()
    # convert to pandas dataframe:

    for item in account:
        print(f"{item.tag}: {item.value}")

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
    get_watchlists()


if __name__ == "__main__":
    main()
