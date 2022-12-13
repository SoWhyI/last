from django.db import models
from users.models import CustomUser
from products.models import Product
from cart.models import Product_in_cart
from datetime import date
import random
from django.shortcuts import reverse


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=False)
    product_list = models.JSONField(unique=False)
    order_date = models.DateTimeField(("Date"), default=date.today)
    delivery_time = models.DateTimeField(("Date"), default=date.today)
    delivery_status = [
        ('Готовится', 'Готовится'),
        ('Доставляется', 'Доставляется'),
        ('Выполнен', 'Выполнен')
    ]
    status = models.CharField(unique=False, max_length=15, null=True, choices=delivery_status, default='Готовится', verbose_name="Вермя доставки")

    def get_absolute_url(self):
        return reverse('orders:manager_order_details')
