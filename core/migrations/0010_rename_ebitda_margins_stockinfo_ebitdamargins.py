# Generated by Django 4.1.5 on 2023-01-05 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_max_age_stockinfo_maxage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockinfo',
            old_name='ebitda_margins',
            new_name='ebitdaMargins',
        ),
    ]