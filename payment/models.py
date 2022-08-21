from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class Transaction(models.Model):
	#transaction for particular payment source
	source = models.ForeignKey('payment.Source',on_delete=models.CASCADE,related_name="transaction")
	amount = models.DecimalField(decimal_places=2,max_digits=12)
	#reference number for transactions
	reference = models.CharField(blank=True,max_length=128)
	status = models.CharField(blank=True,max_length=128)
	date_created = models.DateTimeField(auto_now_add=True,db_index=True)

class Source(models.Model):
	#Source of payment for an order
	order = models.ForeignKey('order.Order',on_delete=models.CASCADE,related_name="Sources")
	source_type = models.ForeignKey('payment.SourceType',on_delete=models.CASCADE,related_name="source_type_source")
	currency = models.CharField(max_length=12,default="Dollars")
	#track various amount associated with this source
	amount_allocated = models.DecimalField(decimal_places=2,max_digits=12,default=Decimal('0.00'))
	amount_debited = models.DecimalField(decimal_places=2,max_digits=12,default=Decimal('0.00'))
	amount_refunded = models.DecimalField(decimal_places=2,max_digits=12,default=Decimal('0.00'))
	reference = models.CharField(blank=True,max_length=255)
	#customer-friendly label for this source
	label = models.CharField(blank=True,max_length=128)

class SourceType(models.Model):
	#Type of payment source
	name = models.CharField(max_length=128)
	code = models.CharField(max_length=128,unique=True)		

class BankCard(models.Model):
	#users bank card details
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bankcards')
	#type of card used: debit,credit,visa,sct
	card_type = models.CharField(max_length=128)
	#Name on the card: often used
	name = models.CharField(max_length=255,blank=True)
	number = models.CharField(max_length=32)
	expiry_date = models.DateField()
	ccv = None