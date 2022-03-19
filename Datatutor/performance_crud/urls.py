from unicodedata import name
from django import views

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simple', views.user, name='simple'),
    path('performance_forms', views.performance_forms, name='performance_forms')
]
