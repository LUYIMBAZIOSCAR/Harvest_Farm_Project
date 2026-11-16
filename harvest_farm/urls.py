from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('knowledge/', include('knowledge.urls')),
    path('gallery/', include('gallery.urls')),
    path('partnerships/', include('partnerships.urls')),
    path('book-tour/', include('bookings.urls')),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
