from django.core.management.base import BaseCommand
from backtest import back_test


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def handle(self, *args, **options):
        back_test.main()
        return 0
