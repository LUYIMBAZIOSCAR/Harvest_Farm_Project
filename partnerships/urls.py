from django.urls import path

from . import views

urlpatterns = [
    path('', views.partnerships, name='partnerships'),
]
