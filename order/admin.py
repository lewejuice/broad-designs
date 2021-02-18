from django.contrib import admin
from .models import Order, Category


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'target_audience',
        'project_description',
        'img_file',
        'useful_links',
        'username',
        'order_paid',
        'price',
        'category',
        'order_date',
        'project_services',
    )

    readonly_fields = ['order_date', 'order_paid', 'price']

    ordering = ('order_date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Order, OrdersAdmin)
admin.site.register(Category, CategoryAdmin)
