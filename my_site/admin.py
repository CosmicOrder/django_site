from django.contrib import admin

from my_site.models import OrderDetail, Sample


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    readonly_fields = ['created_at']


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    readonly_fields = ['published_at']
    list_display = ['category', 'description']
