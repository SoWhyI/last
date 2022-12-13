from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False,blank=True, max_length=30, verbose_name='Имя')
    surname = models.CharField(null=False,blank=True, max_length=30, verbose_name='Фамилия')
    email = models.EmailField(blank=True, max_length=254, verbose_name='Почта')
