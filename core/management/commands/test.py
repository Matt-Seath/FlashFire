from django.core.management.base import BaseCommand
from core import update_asx


class Command(BaseCommand):
    help = 'Populates the database with ASX stock data'

    def handle(self, *args, **options):
        update_asx.main()
        return 0
