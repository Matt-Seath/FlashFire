from pathlib import Path
import csv


def get_list_of_symbols(csv_path, search_column, extension=""):
    file = Path(csv_path)
    if not file.exists():
        print("csv path does not exist.")
        return 1
    symbols_list = []
    print(
        f"Generating list of Symbols with extension: '{extension}'   ", end="")
    with open(csv_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if search_column not in row:
                print(f"{search_column} column does not exist.")
                return 1
            symbol = row[search_column].strip() + extension
            symbols_list.append(symbol)
    print("Done.")

    return symbols_list


def get_cols_rename_dict(csv_path):
    file = Path(csv_path)
    if not file.exists():
        print("csv path does not exist.")
        return 1
    with open(file, mode='r') as infile:
        reader = csv.reader(infile)
        cols_dict = {rows[0]: rows[1] for rows in reader}

        return cols_dict


def get_cols_whitelist(csv_path):
    cols_whitelist = []
    file = Path(csv_path)
    if not file.exists():
        print("csv path does not exist.")
        return 1
    with open(file, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            cols_whitelist.append(*row)

        return cols_whitelist
