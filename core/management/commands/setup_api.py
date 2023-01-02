from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import subprocess
import sys
import os


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def handle(self, *args, **options):
        print('Installing Packages...')
        current_dir = os.path.dirname(__file__)
        pkg_1_path = os.path.join(current_dir, 'bin//atreyu-backtrader-api-1.3')
        pkg_2_path = os.path.join(current_dir, 'bin//pythonclient')

        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_1_path])
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_2_path])
        print("Done.")