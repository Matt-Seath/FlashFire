# Generated by Django 4.1.5 on 2023-01-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_stockinfo_enterprisetorevenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='operatingMargins',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='priceToSalesTrailing12Months',
            field=models.DecimalField(decimal_places=3, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='recommendationKey',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='revenueGrowth',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]
