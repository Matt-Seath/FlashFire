from django.core.management.base import BaseCommand
from django.db import connection
from .progress_bar import bar
import csv
import os


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')
        with open(csv_path, newline='') as csvfile:
            data = csv.DictReader(csvfile)

            total_rows = 0
            for row in data:
                total_rows += 1

            csvfile.seek(0)
        
        with open(csv_path, newline='') as csvfile:
            stocks = csv.DictReader(csvfile)
            
            with connection.cursor() as cursor:
                print('Clearing Table..')
                cursor.execute("DELETE FROM core_stock;")
                print('Populating Stocks...')

                for i, row in enumerate(stocks):
                    symbol = row["ASX code"]
                    company = row["Company name"]
                    exchange = "ASX"
                    query_params = (i + 1, symbol, company, exchange)
                    try:
                        cursor.execute("INSERT INTO core_stock (id, symbol, company, exchange) VALUES (%s, %s, %s, %s)",(query_params))
                    except:
                        print(query_params)
                    
                    bar("Populating Stock Table", (i + 1), total_rows, symbol)

            print("")
            print("")
            print("done.")
