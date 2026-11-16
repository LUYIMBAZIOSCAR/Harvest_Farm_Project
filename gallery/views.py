from django.shortcuts import render

from .models import GalleryCategory, GalleryItem


def gallery_list(request):
    categories = GalleryCategory.objects.all()
    items = GalleryItem.objects.all()
    selected_category = request.GET.get('category', '')
    if selected_category:
        items = items.filter(category__slug=selected_category)
    return render(request, 'gallery/gallery.html', {
        'items': items,
        'categories': categories,
        'selected_category': selected_category,
    })
