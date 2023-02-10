import subprocess
import sys
import os
from django.core.management.base import BaseCommand
from pathlib import Path


def setup_packages():
    print('Installing Packages...')
    pkg_1_path = 'assets/packages/atreyu-backtrader-api-1.3'
    pkg_2_path = 'assets/packages/pythonclient'

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", pkg_1_path])
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", pkg_2_path])
    print("Done.")


def edit_env():
    username = input("IBKR username:  ").strip()
    password = input("IBKR password:  ").strip()
    account_no = input("IBKR acc number:  ").strip()

    file = open(".env", "w+", newline="\n")
    file.write(f"USERNAME='{username}'\n")
    file.write(f"PASSWORD='{password}'\n")
    file.write(f"ACCOUNT_NO='{account_no}'\n")
    file.close()
    print("Done.")
    return 0


def setup_env():
    print("Searching for '.env'")
    file = Path(".env")
    if file.exists() and not file.is_dir():
        print("'.env' found")
        while True:
            ans = input(
                "Overwrite existing environment variables? (y/N):   ").strip().lower()
            if ans == "y":
                edit_env()
                return 0
            if ans == "n" or ans == "":
                print("Setup complete.")
                return 0
    else:
        print("env file doesn't exist yet, creating one now!")
        edit_env()
        return 0


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def handle(self, *args, **options):
        setup_env()
