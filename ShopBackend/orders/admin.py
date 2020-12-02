from django.contrib import admin

from orders.models import Order
from orders.models import OrderDetail


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'shop_user', 'creation_datetime', 'status')
    list_filter = ['status', 'creation_datetime']
    search_fields = ['code', 'shop_user']
    inlines = [OrderDetailsInline]

