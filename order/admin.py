from django.contrib import admin
from .models import Order


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'project_name',
        'target_audience',
        'project_description',
        'img_file',
        'useful_links',
        'username',
        'order_paid',
        'price',
        'order_date',
        'project_services',
    )

    readonly_fields = ['order_number', 'order_date', 'order_paid', 'price']

    ordering = ('order_date',)


# Register your models here.
admin.site.register(Order, OrdersAdmin)
