from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderNote)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)