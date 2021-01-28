from django.urls import path
from . import views

urlpatterns = [
    path('design/', views.design, name='design'),
    path('code/', views.code, name='code'),
]