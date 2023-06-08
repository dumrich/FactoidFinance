from django.db import models
from django.conf import settings

class Stock(models.Model):
    """
    Represents a Stock only. Not other securities for now...
    """

    # Identifying Profile Details
    firm_name = models.CharField(max_length=120, blank=False, null=False)
    ticker = models.CharField(max_length=6, blank=False, null=True)

    # Basic Trading Details (calc Market Cap)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shares_outstanding = models.BigIntegerField(blank=True, null = True)

    # Timestamp Details
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Sectors
    sector = models.CharField(max_length=10, choices=settings.SECTOR_CHOICES)    

    def __str__(self):
        return self.ticker

class StockProfile(models.Model):
    """
    Security Analysis Fields
    """
    pass

    
