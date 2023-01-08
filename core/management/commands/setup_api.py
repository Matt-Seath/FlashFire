from django.core.management.base import BaseCommand
import subprocess
import sys
import os


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def handle(self, *args, **options):
        print('Installing Packages...')
        pkg_1_path = 'assets/atreyu-backtrader-api-1.3'
        pkg_2_path = 'assets/pythonclient'

        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_1_path])
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_2_path])
        print("Done.")