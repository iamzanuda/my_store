from django.contrib import admin

from .models import Product, Size, Color


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_price', 'category')
    list_filter = ('category', 'colors', 'sizes')
    search_fields = ('name', 'description')
    filter_horizontal = ('sizes', 'colors')

admin.site.register(Product, ProductAdmin)
