from cProfile import label
from django.forms import ModelForm
from django import forms
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'price', 'address', 'bathrooms', 'bedrooms', 'squares', 'description', 'image']
    
        labels = {
            'title': 'Title',
            'price': 'Price',
            'address': 'Address',
            'bathrooms': 'Bathrooms',
            'bedrooms': 'Bedrooms',
            'squares': 'Squares',
            'description': 'Description',
            'image': 'Image',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'squares': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }