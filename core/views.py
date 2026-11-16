from django.shortcuts import get_object_or_404, render

from gallery.models import GalleryItem
from knowledge.models import Article
from .models import FarmInformation


def home(request):
    farm = FarmInformation.objects.filter(is_active=True).first()
    featured_articles = Article.objects.filter(status='published').order_by('-published_at')[:3]
    featured_gallery = GalleryItem.objects.filter(is_featured=True).order_by('-created_at')[:6]
    context = {
        'farm': farm,
        'featured_articles': featured_articles,
        'featured_gallery': featured_gallery,
    }
    return render(request, 'core/home.html', context)


def about(request):
    farm = get_object_or_404(FarmInformation, is_active=True)
    context = {'farm': farm}
    return render(request, 'core/about.html', context)
