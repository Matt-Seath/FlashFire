from pathlib import Path
import csv


def get_symbols(csv_path, search_column, extension=""):
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
