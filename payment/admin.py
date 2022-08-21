from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Source)
admin.site.register(SourceType)
admin.site.register(BankCard)