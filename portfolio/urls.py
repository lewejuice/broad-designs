from django.urls import path
from . import views

urlpatterns = [
    path('design/', views.all_design, name='design'),
    path('code/', views.all_code, name='code'),
]
