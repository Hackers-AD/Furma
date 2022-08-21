from django.contrib import admin
from .models import *

# Register your models here.
class WishListAdmin(admin.ModelAdmin):
	list_display = ['owner','name','visibility','date_created']

class LineAdmin(admin.ModelAdmin):
	list_display = ['wishlist','product','quantity','title']

admin.site.register(WishList,WishListAdmin)
admin.site.register(Line,LineAdmin)