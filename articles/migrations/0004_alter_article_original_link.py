# Generated by Django 4.2.1 on 2023-06-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_image_link_alter_article_original_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='original_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
