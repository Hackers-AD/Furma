from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EmailAttachment)
admin.site.register(UserEmail)
admin.site.register(Notification)
admin.site.register(ProductAlert)