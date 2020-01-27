from django.contrib import admin
from .models import OrderLineItem, Order

# Register the order to admin panel to oversee orders
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)