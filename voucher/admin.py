from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(VoucherSet)
admin.site.register(Voucher)
admin.site.register(VoucherApplication)