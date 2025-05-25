from django.forms import ModelForm
from django import forms
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'qt_product', 'address', 'HouseNumber']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control'
            }),

            'qt_product': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 1'
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Avenida Luís Viana Filho'
            }),
            'HouseNumber': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Se não tiver é só deixar em branco'
            }),

        }