from django.contrib import admin
from .models import *
from register.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(AddBook)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
