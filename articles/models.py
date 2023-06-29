from django.db import models
from datetime import datetime
from django.utils.text import slugify
from analysis.models import Stock


class Article(models.Model):
    """
    Represents a singular news article
    """
    title = models.CharField(max_length=455, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    image_link = models.URLField(max_length=255, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    original_link = models.URLField(max_length=255, null=True, blank=True)
    sentiment = models.CharField(max_length=20, blank=True, null=True)
    sentiment_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    stock = models.ForeignKey(
        Stock, blank=True, null=True, on_delete=models.CASCADE)

    site = models.CharField(max_length=255, null=True, blank=True)

    source_link_2 = models.URLField(max_length=255, null=True, blank=True)
    source_link_3 = models.URLField(max_length=255, null=True, blank=True)
    source_link_4 = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def serialized_date(self):
        return self.date.strftime('%Y-%m-%d')

    @serialized_date.setter
    def serialized_date(self, value):
        self.date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').date()
