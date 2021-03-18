from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('google-site-verification: google3e1e27baf2f49bd0.html/', views.google, name='google'),
]
