from core import asx_list

PARAMS = {
    "file": "assets/asx/old_asx_list.csv",
    "column": "ASX code",
    "replace": None,
    "extension": ".AX"
}


def main():
    asx_list.append_csv_to_csv(**PARAMS)
