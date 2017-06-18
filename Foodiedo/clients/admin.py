from django.contrib import admin

from .models import (
    Category,
    Product,
    Status,
    Order,
)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 3


class OrderInline(admin.TabularInline):
    model = Order
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('category',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    inlines = [OrderInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)
    list_filter = ('status',)
