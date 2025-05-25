from django.forms import ModelForm
from django import forms
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['ClientPicture', 'PhoneNumber', 'email']
        widgets = {
            'ClientPicture': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'PhoneNumber': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 11912345678'
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: teste@salgado.com'
            }),
        }