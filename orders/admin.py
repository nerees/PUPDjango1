from django.contrib import admin
from .models import Product, Customer, Status, ProductOrder, Order

class ProductOrderInline(admin.StackedInline):
    model = ProductOrder
    verbose_name = "Product in ORDER"
    verbose_name_plural = "Products in ORDER"

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductOrderInline,
    ]


admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
