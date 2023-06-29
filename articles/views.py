from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Article
from users.models import UserProfile
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@login_required
def index(request):
    """Redirect to dashboard or login"""
    return redirect("dashboard")


@login_required
def dashboard(request):
    """Main page view for user"""
    user_profile = UserProfile.objects.get(user=request.user)

    categories = user_profile.categories.all()
    categories_articles = []

    for category in categories:
        categories_articles.append(
            Article.objects.filter(stock__sector=category.name).order_by('-id')[:4]
        )

    latest_article = Article.objects.latest('id')
    main_articles = Article.objects.filter(id__in=[270, 206, 303, 272])[1:4]

    return render(request, 'articles/dashboard.html',
                  {'latest_article': latest_article,
                   'main_articles': main_articles,
                   'profile_arts': zip(categories, categories_articles),
                   'profile': user_profile})


@login_required
def category(request, category_choice):
    """Main page view for user"""
    articles = Article.objects.filter(stock__sector=category_choice)
    paginator = Paginator(articles, 12)
    page_no = int(request.GET.get('page'))

    context = {"articles": paginator.page(page_no)}

    return render(request, "articles/category.html", context)


@login_required
def article_detail(request, pk):
    """Main page view for user"""
    article = Article.objects.get(id=pk)
    context = {"article": article}

    return render(request, "articles/post_details.html", context)
