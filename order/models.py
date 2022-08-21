from django.db import models
from django.contrib.auth.models import User
from address.models import Address

# Create your models here.
class Order(models.Model):
	number = models.CharField(max_length=128,db_index=True,unique=True)
	#tracking site from where order is placed
	#site = models.ForeignKey('site.Site',on_delete=models.SET_NULL,null=True,verbose_name="Site")
	basket = models.ForeignKey('basket.Basket',on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Basket")
	user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="User")
	billing_address = models.ForeignKey('order.BillingAddress',on_delete=models.SET_NULL,null=True,blank=True,verbose_name="billing_address")
	currency = models.CharField(max_length=12,default='Dollars')
	total_excl_tax = models.DecimalField(null=True,max_digits=12,decimal_places=2)
	total_incl_tex = models.DecimalField(null=True,max_digits=12,decimal_places=2)
	shipping_excl_tax = models.DecimalField(null=True,max_digits=12,decimal_places=2)
	shipping_incl_tex = models.DecimalField(null=True,max_digits=12,decimal_places=2)
	shipping_address = models.ForeignKey('order.ShippingAddress',on_delete=models.SET_NULL,null=True,blank=True,verbose_name="shipping_address")
	shipping_method = models.CharField(max_length=128,blank=True)
	shipping_code = models.CharField(max_length=128,blank=True,default="")
	date_placed = models.DateTimeField(db_index=True)	

class OrderNote(models.Model):
	#note against an order
	#whenever admin make changes to order, we record that to inform what happened
	order = models.ForeignKey('order.Order',on_delete=models.CASCADE,verbose_name="Order")
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name="User")
	note_type = models.CharField(max_length=128,blank=True) #info,warning,error,system
	message = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)


class ShippingAddress(Address):
	phone_number = models.CharField(max_length=15,blank=True)
	note = models.TextField(blank=True)

class BillingAddress(Address):
	class Meta:
		verbose_name = "Billing Address"
		verbose_name_plural = "Billing Addresses"