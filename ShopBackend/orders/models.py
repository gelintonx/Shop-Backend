import uuid

from django.db import models

from authService.models import ShopUser
from products.models import Product


class Order(models.Model):
    code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    shop_user = models.ForeignKey(ShopUser, on_delete=models.RESTRICT)
    creation_datetime = models.DateField(auto_now_add=True)

    ORDER_STATUS = (
        ('CART', 'Order is on cart.'),
        ('RECEIVED', 'Order has been received.'),
        ('PROCESSING', 'Order is processing.'),
        ('COMPLETED', 'Order is completed.'),
    )
    #TODO: Discuss order status

    status = models.CharField(max_length=25, choices=ORDER_STATUS, blank=False)

    def __str__(self):
        return self.code + " " + self.shop_user.username + " " + str(self.creation_datetime) + " " + self.status


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    units = models.PositiveIntegerField()
    current_product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + " " + str(self.units) + " " + str(self.current_product_price)
