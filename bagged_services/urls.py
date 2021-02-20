from django.urls import path
from . import views

urlpatterns = [
    path('', views.bagged_services, name='bagged_services'),
    path('add/<service_id>/', views.add_to_order, name='add_to_order'),
]