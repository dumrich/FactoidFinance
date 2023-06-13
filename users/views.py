from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, get_user_model

class LoginView(View):
    """User login implementation"""

    def get(self, request):
        context = {}

        return render(request, "users/login.html", context)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is None:

            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

        login(request, user)

        return redirect("dashboard")

class SignUpView(View):
    """User signup implementation"""

    def get(self, request):
        context = {}

        return render(request, "users/register.html", context)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()
        user = User.objects.create_user(username=username, email=email, password=password)
        user = authenticate(request, email=email, password=password)

        if user is None:

            return render(request, 'users/register.html', {'error': 'Couldn\'t create user'})

        login(request, user)

        return redirect("dashboard")
