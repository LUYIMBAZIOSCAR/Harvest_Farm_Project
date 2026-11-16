from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Article, ArticleCategory


def article_list(request):
    articles = Article.objects.filter(status='published')
    categories = ArticleCategory.objects.all()
    query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '')

    if query:
        articles = articles.filter(Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(content__icontains=query))

    if selected_category:
        articles = articles.filter(category__slug=selected_category)

    category = None
    if selected_category:
        category = categories.filter(slug=selected_category).first()

    articles = articles.order_by('-published_at')
    return render(request, 'knowledge/article_list.html', {
        'articles': articles,
        'categories': categories,
        'selected_category': selected_category,
        'category': category,
        'query': query,
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='published')
    related_articles = Article.objects.filter(
        status='published',
        category=article.category,
    ).exclude(pk=article.pk).order_by('-published_at')[:3]
    return render(request, 'knowledge/article_detail.html', {
        'article': article,
        'related_articles': related_articles,
    })
