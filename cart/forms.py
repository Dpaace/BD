from dataclasses import fields
from django import forms

from register.models import AddBook
from .models import ShippingAddress



class shipping(forms.ModelForm):
    class Meta:
        model =ShippingAddress
        fields = ("__all__")

class order_quantity(forms.ModelForm):
    class Meta:
        model =AddBook
        fields = ['quantity']