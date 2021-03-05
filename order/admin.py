from django.contrib import admin
from .models import Order


class OrdersAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date', 'order_total', 'stripe_pid')

    fields = ('project_name', 'target_audience', 'project_description',
              'img_file', 'useful_links', 'username', 'project_services',
              'order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total')

    ordering = ('-date',)


# Register your models here.
admin.site.register(Order, OrdersAdmin)
