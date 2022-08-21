from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
# Create your models here.
class VoucherSet(models.Model):
	#Collection of Vouchers
	name = models.CharField(max_length=100)
	count = models.PositiveIntegerField() #min num of vouchers in the set
	code_length = models.IntegerField(default=12) #max voucher code length is 12 eg: xxxx-xxxx-xxxx
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField()
	offer = models.OneToOneField('offers.ConditionalOffer',on_delete=models.CASCADE,null=True,blank=True,
		limit_choices_to={'offer_type':"Voucher"},related_name="Offers")

class Voucher(models.Model):
	#A voucher.  This is simply a link to a collection of offers.
	name = models.CharField(max_length=128)
	code = models.CharField(max_length=128,unique=True,db_index=True)
	offer = models.OneToOneField('offers.ConditionalOffer',on_delete=models.CASCADE,
		limit_choices_to={'offer_type':"Voucher"},related_name="voucher_set")
	SINGLE_USE, MULTI_USE, ONCE_PER_CUSTOMER = ('Single use','Multi-use','Once per customer')
	USAGE_CHOICES = (
		(SINGLE_USE,'Can be used once by one customer'),
		(MULTI_USE,'Can be used multiple times by multiple customers'),
		(ONCE_PER_CUSTOMER,'Can only be used once per customer')
		)
	usage = models.CharField(max_length=128,choices=USAGE_CHOICES,default=MULTI_USE)
	start_datetime = models.DateTimeField(db_index=True)
	end_datetime = models.DateTimeField(db_index=True)

	num_basket_additions = models.PositiveIntegerField(default=0)
	num_orders = models.PositiveIntegerField(default=0)

	total_discount = models.DecimalField(max_digits=12,decimal_places=2,default=Decimal("0.00"))
	voucher_set = models.ForeignKey('voucher.VoucherSet',on_delete=models.CASCADE,related_name="vouchers",
		null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)


class VoucherApplication(models.Model):
	#Tracking how often voucher has been use in order
	voucher = models.ForeignKey('voucher.Voucher',on_delete=models.CASCADE,related_name="applications")
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="voucher_user",null=True,blank=True)
	order = models.ForeignKey('order.Order',on_delete=models.CASCADE,related_name="order_voucher")
	date_created = models.DateTimeField(auto_now_add=True)