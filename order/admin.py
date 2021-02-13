from django.contrib import admin
from .models import Order, Category


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'project_name',
        'category',
        'order_date',
        'order_paid',
        'project_description',
        'target_audience',
        'useful_links',
        'img_file',
        'price',
    )

    ordering = ('order_date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Order, OrdersAdmin)
admin.site.register(Category, CategoryAdmin)