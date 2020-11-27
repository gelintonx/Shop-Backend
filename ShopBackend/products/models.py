from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name