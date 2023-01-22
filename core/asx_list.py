from pathlib import Path
import csv

DEFAULT_MASTER = "assets/asx/asx_list.csv"
DEFAULT_FILE_PATH = "assets/asx/companies-list.csv"
DEFAULT_COLUMN = "Code"
DEFAULT_REPLACE = "ASX:"
DEFAULT_EXTENSION = ".AX"


def get_list_of_symbols(**kwargs):
    file_path = kwargs["file"] if "file" in kwargs else DEFAULT_FILE_PATH
    column = kwargs["column"] if "column" in kwargs else DEFAULT_COLUMN
    replace = kwargs["replace"] if "replace" in kwargs else DEFAULT_REPLACE
    extension = kwargs["extension"] if "extension" in kwargs else DEFAULT_EXTENSION

    file = Path(file_path)
    if not file.exists():
        print("csv path does not exist.")
        return 1
    symbols_list = []
    print(
        f"\nGenerating list of Symbols with extension: '{extension}'   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if column not in row:
                print(f"{column} column does not exist.")
                return 1
            symbol = row[column].strip() + extension
            symbols_list.append(symbol)
    if replace:
        symbols_list = [symbol.replace(replace, "") for symbol in symbols_list]
    print("Done.")

    return symbols_list


def write_to_master(list_to_add):
    master_list = Path(DEFAULT_MASTER)
    with open(master_list, "w") as csvfile:
        writer = csv.writer(csvfile)
        for item in list_to_add:
            writer.writerow([item])


def get_master_list():
    master_path = Path(DEFAULT_MASTER)
    master_list = []
    if not master_path.exists():
        print("csv path does not exist.")
        return 1
    with open(master_path, newline='') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            master_list.append(*row)

    return master_list


def append_csv_to_csv(**kwargs):

    list_to_add = get_list_of_symbols(**kwargs)
    master_list = get_master_list()
    joined_list = list_to_add + master_list
    final_list = list(dict.fromkeys(joined_list))
    write_to_master(final_list)
