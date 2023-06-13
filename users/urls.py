from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    
]
