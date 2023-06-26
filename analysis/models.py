from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from datetime import datetime


class Stock(models.Model):
    """
    Represents a Stock only. Not other securities for now...
    """

    # Identifying Profile Details
    firm_name = models.CharField(max_length=256, blank=False, null=True)

    ticker = models.CharField(max_length=12, blank=False, null=True)
    cusip = models.CharField(max_length=9, blank=True, null=True)
    isin = models.CharField(max_length=12, blank=True, null=True)
    cik = models.CharField(max_length=10, blank=True, null=True)

    # Basic Trading Details (calc Market Cap)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    shares_outstanding = models.BigIntegerField(blank=True, null=True)
    market_cap = models.BigIntegerField(blank=True, null=True)

    # Timestamp Details
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Sectors
    sector = models.CharField(
        max_length=100, null=True)

    isEtfOrFund = models.BooleanField(
        default=False, verbose_name="ETF or Index Fund", null=True, blank=True)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if is_new:
            self.ticker = self.ticker.upper()
            self.sector = slugify(self.sector)
            super().save(*args, **kwargs)

            analysis = StockAnalysis(stock=self)
            analysis.save()
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.ticker


class StockAnalysis(models.Model):
    """
    Security Analysis Fields
    """
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, null=True)

    # What Exchange does the stock belong to
    exchange = models.CharField(
        max_length=100, null=True)

    # Price and shares outstanding (Market Cap, other calcs)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    sharesOutstanding = models.BigIntegerField(blank=True, null=True)
    marketCap = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    change = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True)

    # Earnings Data
    revenuettm = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)
    incomettm = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)

    # Dividend Data
    dividendps = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    dividend_date = models.CharField(max_length=30, blank=True, null=True)

    # Volume
    volume = models.BigIntegerField(blank=True, null=True)

    # Open and Close
    open = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    previousclose = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)

    eps = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    pe = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.stock.ticker.upper()
