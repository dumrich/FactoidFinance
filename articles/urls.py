from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("category/<str:category_choice>", views.category, name="category"),
    path("article/<int:pk>", views.article_detail, name="article_detail"),
]
