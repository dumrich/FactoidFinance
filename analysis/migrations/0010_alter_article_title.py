# Generated by Django 4.2.1 on 2023-06-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0009_article_content_article_date_article_image_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
