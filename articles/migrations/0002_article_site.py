# Generated by Django 4.2.1 on 2023-06-25 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
