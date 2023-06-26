# Generated by Django 4.2.1 on 2023-06-23 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis', '0013_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('image_link', models.URLField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('original_link', models.URLField(blank=True, max_length=255, null=True)),
                ('sentiment', models.CharField(blank=True, max_length=20, null=True)),
                ('sentiment_score', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.stock')),
            ],
        ),
    ]