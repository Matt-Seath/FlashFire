from django.core.management.base import BaseCommand
from core import stock_info, stock_history


class Command(BaseCommand):
    help = 'Populates the database with ASX stock data'

    def handle(self, *args, **options):
        stock_info.main()
        stock_history.main()
        return 0
