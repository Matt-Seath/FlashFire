# Generated by Django 4.1.5 on 2023-09-26 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_watchlistitem_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='stock_id',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='watchlistitem',
            old_name='stock_id',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='watchlistitem',
            old_name='watchlist_id',
            new_name='watchlist',
        ),
    ]
