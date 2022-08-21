from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Basket(models.Model):
	#this field is nullable because basket can be owned by anonymous user also
	owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="baskets",verbose_name="Owner")
	#A basket can have many vouchers attached to it but it is common to force one voucher per basket in
	#vouchers = models.ManyToMayField('voucher.Voucher',blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_submitted = models.DateTimeField(null=True,blank=True)

class BasketLine(models.Model):
	#Line of basket (product and quantity)
	basket = models.ForeignKey('basket.Basket',on_delete=models.CASCADE,related_name="lines")
	product = models.ForeignKey('catalogue.Product',on_delete=models.CASCADE,related_name='lines_products')
	quantity = models.PositiveIntegerField(default=1)
	price_currency = models.CharField(max_length=12,default='Dollars')
	price_excl_tax = models.DecimalField(null=True,max_digits=12,decimal_places=2)
	price_incl_tex = models.DecimalField(null=True,max_digits=12,decimal_places=2)
	date_created = models.DateTimeField(auto_now_add=True,db_index=True)