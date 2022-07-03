from dataclasses import fields
from django import forms
from .models import AddBook, Contact, UserP
from cart.models import *


class add_book(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ("__all__")



class update_book(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ("__all__")


class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("__all__")

class shipping_order(forms.ModelForm):
    class Meta:
        model =ShippingAddress
        fields = ['status']

class Update_form(forms.ModelForm):
    class Meta:
        model = UserP
        fields = ("__all__")