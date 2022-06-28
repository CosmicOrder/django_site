from django.contrib import admin

from my_site.models import OrderDetail


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    readonly_fields = ['created_at']
