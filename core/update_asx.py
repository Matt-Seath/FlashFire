from backtest.pipelines.assets_pls import append_csv_to_master

PARAMS = {
    "file": "assets/asx/old_asx_list.csv",
    "column": "ASX code",
    "replace": None,
    "extension": ".AX"
}


def main():
    append_csv_to_master(**PARAMS)
