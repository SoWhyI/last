from django.db import models
from django.forms import fields
from .models import Product
from django import forms


class UserImage(forms.ModelForm):
    class Meta:
        # To specify the model to be used to create form
        model = Product
        # It includes all the fields of model
        fields = ('name', 'price', 'size', 'layer_field', 'category', 'description', 'photo')
