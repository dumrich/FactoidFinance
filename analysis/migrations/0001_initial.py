# Generated by Django 4.2.1 on 2023-06-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_name', models.CharField(max_length=120)),
                ('ticker', models.CharField(max_length=6, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shares_outstanding', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sector', models.CharField(choices=[('ENER', 'Energy'), ('MAT', 'Materials'), ('IND', 'Industrials'), ('UTIL', 'Utilities'), ('HEALTH', 'Healthcare'), ('FIN', 'Financials'), ('DISC', 'Consumer Discretionary'), ('STAP', 'Consumer Staples'), ('IT', 'Information Technology'), ('COMM', 'Communication Services'), ('REAL', 'Real Estate')], max_length=10)),
            ],
        ),
    ]
