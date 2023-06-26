from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CheckboxForm
from .models import UserProfile, Category


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

            return render(request, 'users/login.html',
                          {'error': 'Invalid credentials'})

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
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user = authenticate(request, email=email, password=password)

        if user is None:

            return render(request, 'users/register.html', {'error': 'Couldn\'t create user'})

        login(request, user)

        return redirect("dashboard")


@login_required
def profile(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CheckboxForm(request.POST)
        if form.is_valid():
            user_profile.categories.clear()
            for option in form.cleaned_data['options']:
                category = Category.objects.create(name=option)
                user_profile.categories.add(category)
        else:
            form = CheckboxForm()

    context = {'user_profile': user_profile, 'form': CheckboxForm}
    return render(request, 'users/profile.html', context)
