from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django import forms


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название")
    price = models.FloatField(max_length=9, null=True, verbose_name="Цена")
    size = models.CharField(max_length=3, null=True, verbose_name="Объем")
    layer = [
        ('однослойный', 'однослойный'),
        ('многослойный', 'многослойный')
    ]
    layer_field = models.CharField(unique=False, max_length=15, null=True, choices=layer, verbose_name="Количество слоев")
    category = models.CharField(max_length=25, null=True, verbose_name="Категория")
    description = models.TextField(max_length=500, verbose_name="Описание")
    photo = models.ImageField(upload_to='uploads/', null=True, verbose_name="Фотография")
    quantity_in_cart = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list')