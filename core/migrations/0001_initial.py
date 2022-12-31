# Generated by Django 4.1.4 on 2022-12-31 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255, unique=True)),
                ('company', models.CharField(max_length=255)),
                ('exchange', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cash', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='core.stock')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='core.stock')),
            ],
        ),
        migrations.CreateModel(
            name='LatestTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('size', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='latest', to='core.stock')),
            ],
        ),
    ]
