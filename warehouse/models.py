from django.db import models

class ProductsGroup(models.Model):

    code = models.PositiveIntegerField()
    name = models.CharField(max_length=35)

class Product(models.Model):

    group = models.ForeignKey(ProductsGroup,on_delete=models.CASCADE)
    code  = models.PositiveIntegerField()
    name  = models.CharField(max_length=35)
    price = models.PositiveIntegerField()
