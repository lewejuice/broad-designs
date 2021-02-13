from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('add/<service_id>/', views.add_to_order, name='add_to_order'),
    path('project_form/', views.project_form, name='project_form'),
]
