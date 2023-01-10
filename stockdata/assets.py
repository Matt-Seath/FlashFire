import csv


def get_symbols():
    file_path = 'assets//asx.csv'
    symbols_list = []
    print("Generating list of Symbols..   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row["ASX code"].strip() + ".AX"
            symbols_list.append(symbol)
    print("Done.")

    return symbols_list

