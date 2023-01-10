from django.core.management.base import BaseCommand
from core import update_db


class Command(BaseCommand):
    help = 'Populates the database with ASX stock data'

    def handle(self, *args, **options):
        update_db.main()
        return 0
