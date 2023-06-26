# Generated by Django 4.2.1 on 2023-06-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0021_alter_stockanalysis_marketcap_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockanalysis',
            name='open',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='stockanalysis',
            name='previousclose',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
