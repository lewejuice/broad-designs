from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('order_success/<order_number>', views.order_success, name='order_success'),
]
