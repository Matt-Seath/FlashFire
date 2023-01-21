from django.core.management.base import BaseCommand
from backtest import backtest_all


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def add_arguments(self, parser) -> None:
        parser.add_argument("strategy", type=str, help="Insert Strat")

    def handle(self, *args, **options):
        strategy = options["strategy"].lower()
        backtest_all.main(strategy)

        return 0
