from django.core.management.base import BaseCommand
from asx import update_db


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        update_db.main()
        return 0
