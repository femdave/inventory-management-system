from django.db import models
from accounts.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    description = models.CharField(max_length=500, null=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_unit = models.IntegerField(default=0, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
