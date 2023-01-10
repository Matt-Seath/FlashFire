import csv


def get_symbols(csv_path, search_column, extension=""):
    symbols_list = []
    print("Generating list of Symbols..   ", end="")
    with open(csv_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row[search_column].strip() + extension
            symbols_list.append(symbol)
    print("Done.")

    return symbols_list




