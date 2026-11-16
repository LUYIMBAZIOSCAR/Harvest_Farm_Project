from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_tour, name='book_tour'),
]
