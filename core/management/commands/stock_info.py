from django.core.management.base import BaseCommand
from core import stock_info


class Command(BaseCommand):
    help = 'Populates the database with ASX stock data'

    def handle(self, *args, **options):
        stock_info.main()
        return 0
