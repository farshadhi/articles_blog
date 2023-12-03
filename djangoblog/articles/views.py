from django.shortcuts import render
from .models import Article

def articles(request):
    articles = Article.objects.order_by('-date')
    data = {
        'articles': articles
    }
    return render(request, 'articles/articles.html', data)

    