from django.contrib import admin
from .models import *

# Register your models here.
class ProductClassAdmin(admin.ModelAdmin):
	list_display = ['name','requires_shipping','track_stock']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','img']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['title','upc','product_class','rating','created_on']

class ProductAttrAdmin(admin.ModelAdmin):
	list_display = ['name','code','product_class']

class ProductImageAdmin(admin.ModelAdmin):
	list_display = ['product','original','display_order','created_date']

class OptionAdmin(admin.ModelAdmin):
	list_display = ['name','group','image']

admin.site.register(ProductClass,ProductClassAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductAttribute,ProductAttrAdmin)
admin.site.register(ProductImage,ProductImageAdmin)
admin.site.register(ProductAttributeValue)
admin.site.register(Option,OptionAdmin)
admin.site.register(ProductGroup)