from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):

        data = pd.DataFrame({
            'symbol':["A"],
            'company':['Python Programming'],
            'exchange':["asx"]
        })
        print(data)
        print("")
        with connection.cursor() as cursor:
            cols = "`,`".join([str(i) for i in data.columns.tolist()])
            cursor.execute("delete from core_stock;")
            # Insert DataFrame recrds one by one.
            for i,row in data.iterrows():
                sql = "INSERT INTO `core_stock` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
                cursor.execute(sql, tuple(row))
                print(sql, tuple(row))

                # the connection is not autocommitted by default, so we must commit to save our changes
                connection.commit()
        print("Done.")