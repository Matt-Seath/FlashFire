# Generated by Django 4.1.5 on 2023-01-05 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_stockinfo_longname_alter_stockinfo_shortname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockinfo',
            name='dateShortInterest',
        ),
        migrations.RemoveField(
            model_name='stockinfo',
            name='fundInceptionDate',
        ),
        migrations.RemoveField(
            model_name='stockinfo',
            name='lastDividendDate',
        ),
        migrations.RemoveField(
            model_name='stockinfo',
            name='lastSplitDate',
        ),
    ]
