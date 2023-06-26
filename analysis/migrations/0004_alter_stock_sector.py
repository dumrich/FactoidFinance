# Generated by Django 4.2.1 on 2023-06-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_alter_stock_sector_alter_stock_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sector',
            field=models.CharField(choices=[('ENER', 'Energy'), ('MAT', 'Materials'), ('IND', 'Industrials'), ('UTIL', 'Utilities'), ('HEALTH', 'Healthcare'), ('FIN', 'Financials'), ('DISC', 'Consumer Discretionary'), ('STAP', 'Consumer Staples'), ('IT', 'Information Technology'), ('COMM', 'Communication Services'), ('REAL', 'Real Estate')], max_length=100),
        ),
    ]
