from django.contrib import admin
from .models import Services, Category


class ServiceAdmin(admin.ModelAdmin):
    """ Fields needed for the services """

    list_display = (
        'name',
        'category',
        'price',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    """ Fields needed for the categories """

    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Services, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
