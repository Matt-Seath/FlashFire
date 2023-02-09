from django.core.management.base import BaseCommand
from tws import auth


class Command(BaseCommand):
    help = 'TWS'

    def handle(self, *args, **options):
        auth.main()
        return 0
