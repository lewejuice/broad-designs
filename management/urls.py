from django.urls import path
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path('add-service/', views.add_service, name='add_service'),
    path('edit-service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete-service-page/<int:service_id>/', views.delete_service_page, name='delete_service_page'),
    path('delete-service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('add-project/', views.add_project, name='add_project'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete-project-page/<int:project_id>/', views.delete_project_page, name='delete_project_page'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('order-info/<order_number>/', views.order_info, name='order_info'),
]
