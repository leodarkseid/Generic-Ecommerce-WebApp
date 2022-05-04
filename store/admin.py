from django.contrib import admin

from store.models import Product, ShippingAddress, Customer, Order, OrderItem

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

# Register your models here.
