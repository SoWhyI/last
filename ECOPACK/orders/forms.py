from django import forms
from . import models


class OrderManage(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('status', 'delivery_time')
        widgets = {
            'delivery_time': forms.TextInput(attrs={'class':'form-control rounded 3', 'type': 'datetime-local'}),
            'status' : forms.Select(attrs={'class':'form-control rounded 3'})
        }