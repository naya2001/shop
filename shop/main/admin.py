from django.contrib import admin
from .models import Customer, Category, Product, CartElement, Cart, Order, Status, Image

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartElement)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(Image)


