from core.models import StockInfo


def get_col_list_from_db(column):
    col_list = StockInfo.objects.values_list(column)

    return col_list
