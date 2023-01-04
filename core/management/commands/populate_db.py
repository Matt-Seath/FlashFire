from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
from core.models import Stock
from sqlalchemy import create_engine
from flashfire import settings
import pandas as pd
import os





class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        print('Populating the database...')
        current_dir = os.path.dirname(__file__)
        csv = os.path.join(current_dir, 'assets//asx.csv')
        df = pd.read_csv(csv)
        df = df["ASX code"]

        engine = create_engine(settings.DATABASE_URL)


        df.to_sql(Stock, if_exists="replace", con=engine, index=False)

        print("ok")