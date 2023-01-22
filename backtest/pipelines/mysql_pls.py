from core.models import StockInfo


def get_col_list_from_db(column, filters, all=True, limit=1):
    if limit and not all:
        col_list = StockInfo.objects.values_list(column, flat=True)[:limit]
    else:
        col_list = StockInfo.objects.filter(**filters).values_list(column, flat=True)

    return list(col_list)
