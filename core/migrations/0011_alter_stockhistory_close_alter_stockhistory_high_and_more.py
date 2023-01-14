# Generated by Django 4.1.5 on 2023-01-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_stockhistory_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='close',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='high',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='low',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='open',
            field=models.FloatField(null=True),
        ),
    ]
