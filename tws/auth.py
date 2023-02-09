from ib_insync import *


def main():
    # util.startLoop()  # uncomment this line when in a notebook

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)

    account = ib.accountSummary()
    # convert to pandas dataframe:

    for item in account:
        print(f"{item.tag}: {item.value}")

    ib.disconnect()


if __name__ == "__main__":
    main()
