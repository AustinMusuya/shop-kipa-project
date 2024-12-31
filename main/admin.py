from django.contrib import admin
from .models import Category, Product, SaleDetail, Sales, Supplier, OrderDetail, Orders

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Orders)
admin.site.register(OrderDetail)
admin.site.register(Sales)
admin.site.register(SaleDetail)
