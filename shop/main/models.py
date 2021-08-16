from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    category_title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)


    def __str__(self):
        return self.category_title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product_title = models.CharField(max_length=100)

    def __str__(self):
        return self.product_title


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(null=True)

    image = models.ManyToManyField(Image)

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product_title


class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CartElement(models.Model):
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.cart_product.__str__()


class Cart(models.Model):
    cart_element = models.ManyToManyField(CartElement)


class Status(models.Model):
    status_title = models.CharField(max_length=50)

    def __str__(self):
        return self.status_title


class Order(models.Model):
    order_status = models.ForeignKey(Status, on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)



