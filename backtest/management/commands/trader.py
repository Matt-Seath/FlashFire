from django.core.management.base import BaseCommand
from backtest import trader


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def handle(self, *args, **options):
        trader.main()
        return 0
