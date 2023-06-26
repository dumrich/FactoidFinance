from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from .models import Stock, StockAnalysis


@login_required
def stock_detail(request, stock_id):
    """Main page view for user"""
    if stock_id.upper() != stock_id:
        return redirect("stock", stock_id=stock_id.upper())

    stock = get_object_or_404(
        Stock,
        Q(ticker=stock_id) | Q(cusip=stock_id) | Q(
            isin=stock_id) | Q(cik=stock_id)
    )
    stock_analysis = StockAnalysis.objects.get(stock=stock)

    return render(request, "analysis/stock_detail.html",
                  {"stock": stock, "details": stock_analysis})


@login_required
def stock_search(request):
    """Search for stock"""
    return redirect("stock", stock_id=request.GET.get('search-field'))
