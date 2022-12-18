from django.contrib import admin
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    display_list=('user',)
admin.site.register(Customer)

class OrderAdmin(admin.ModelAdmin):
    list_display=('customer',)
admin.site.register(Order)

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order',)
admin.site.register(OrderItem)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=('order',)
admin.site.register(ShippingAddress)
