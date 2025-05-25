from django.db import models

from accounts.models import Client

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qt_product = models.PositiveIntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    preparation_time = models.DateTimeField()
    delivery_confimation = models.BooleanField(default=False)
    order_sent = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    HouseNumber = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.client} ordered {self.product}'