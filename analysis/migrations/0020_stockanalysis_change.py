# Generated by Django 4.2.1 on 2023-06-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0019_stockanalysis_marketcap'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockanalysis',
            name='change',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
