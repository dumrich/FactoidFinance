from django.urls import path
from . import views

urlpatterns = [
    path("<str:stock_id>", views.stock_detail, name="stock"),
    path("search/", views.stock_search, name="stock_search"),
]
