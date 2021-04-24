from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('wordcount', views.wc, name='count'),
    path('help',views.help, name='help'),
]
