# Generated by Django 4.2.1 on 2023-06-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0018_alter_stockanalysis_sharesoutstanding'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockanalysis',
            name='marketCap',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
