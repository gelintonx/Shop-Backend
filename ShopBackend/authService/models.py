from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class ShopUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(default=None)
   

    def __str__(self):
        return self.username

        