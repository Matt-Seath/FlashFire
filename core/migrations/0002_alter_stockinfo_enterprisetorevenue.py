# Generated by Django 4.1.5 on 2023-01-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='enterpriseToRevenue',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
