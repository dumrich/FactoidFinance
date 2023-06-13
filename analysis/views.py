from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def index(request):
    """Redirect to dashboard or login"""
    return redirect("dashboard")

@login_required
def dashboard(request):
    """Main page view for user"""
    context = {}
    return render(request, "analysis/dashboard.html", context)
