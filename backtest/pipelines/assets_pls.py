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


def append_csv_to_master(**kwargs):

    list_to_add = get_list_of_symbols(**kwargs)
    master_list = get_master_list()
    joined_list = list_to_add + master_list
    final_list = list(dict.fromkeys(joined_list))
    write_to_master(final_list)


def get_cols_rename_dict(csv_path):
    file = Path(csv_path)
    if not file.exists():
        print("csv path does not exist.")
        return 1
    with open(file, mode='r') as infile:
        reader = csv.reader(infile)
        cols_dict = {rows[0]: rows[1] for rows in reader}

        return (cols_dict)


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


def get_shared_values(list_1, list_2):
    list_3 = []
    for item in list_1:
        if item not in list_2:
            list_3.append(item)

    return list_3
