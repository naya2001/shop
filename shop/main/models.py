from django.db import models
from django.contrib.auth.models import User


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
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title


class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    #first_name = models.CharField(max_length=30, null=True)
    #last_name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=100, null=True)
    #email = models.EmailField()

   # def __str__(self):
     #   return self.user.username
        #return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    @property
    def cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.total_price for item in orderitems])
        return total

    #def save(self, *args, **kwargs):
     #   self.is_complete = True
      #  super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    amount = models.IntegerField(default=1)

    @property
    def total_price(self):
        total = self.product.price * self.amount
        return total

