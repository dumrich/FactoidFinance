# Generated by Django 4.2.1 on 2023-06-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_stock_isetforfund_alter_stock_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='firm_name',
            field=models.CharField(max_length=256),
        ),
    ]