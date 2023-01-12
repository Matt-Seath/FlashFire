from django.core.management.base import BaseCommand
from core import test


class Command(BaseCommand):
    help = 'Populates the database with ASX stock data'

    def handle(self, *args, **options):
        test.main()
        return 0
