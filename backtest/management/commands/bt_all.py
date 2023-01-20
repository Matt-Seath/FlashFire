from django.core.management.base import BaseCommand
from backtest import backtest_all


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def handle(self, *args, **options):
        backtest_all.main()

        return 0
