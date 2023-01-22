from backtest.pipelines.assets_pls import append_csv_to_master

PARAMS = dict(
    file="assets/asx/old_asx_list.csv",
    column="ASX code",
    replace=None,
    extenion=".AX"
)


def main():
    append_csv_to_master(**PARAMS)
