from django.contrib import admin
from .models import Services, Category


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Services, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
