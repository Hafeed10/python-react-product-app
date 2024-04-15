from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    product_brand = models.CharField(max_length=100, null=True, blank=True)
    product_category = models.CharField(max_length=100, null=True, blank=True)
    product_info = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    stock_count = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateField(null=True, blank=True, auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.product_name


class Login(models.Model):
    username = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    password = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return self.username
    


class Signup(models.Model):
     username = models.CharField(max_length=128, blank=True)
     email = models.EmailField(max_length=200, blank=True)
     password = models.CharField(max_length=10, blank=True)
     mother_name = models.CharField(max_length=200, blank=True)
     number = models.CharField(max_length=10, blank=True)


     def __str__(self):
         return self.username
