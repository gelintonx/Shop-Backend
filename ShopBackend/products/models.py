from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default=None, null=False)

    def __str__(self):
        return self.name