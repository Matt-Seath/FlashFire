from django.core.management.base import BaseCommand
from backtest import back_test


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def add_arguments(self, parser) -> None:
        parser.add_argument("stock", type=str, help="Ehhh")
        # return super().add_arguments(parser)

    def handle(self, *args, **options):
        stock = options["stock"].upper()
        back_test.main(stock)

        return 0