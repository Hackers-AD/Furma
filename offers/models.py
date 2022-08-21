from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class ConditionalOffer(models.Model):
	# A conditional offer eg: buy one get one
	name = models.CharField(max_length=128,unique=True)
	slug = models.SlugField(max_length=128,unique=True)
	description = models.TextField(blank=True)
	#Types of offer: User, Session, Voucher, Site
	SITE,VOUCHER,USER,SESSION = ('Site','Voucher','User','Session')
	TYPE_CHOICES = (
		(SITE,'Site Offer-available to all user'),
		(VOUCHER,'Voucher offer-available only after entering voucher code'),
		(USER,'User offer-available to certain types of users only'),
		(SESSION,'Session offer-temporary offer, available for the duration of session ')
		) 
	offer_type = models.CharField(max_length=128,default=SITE,choices=TYPE_CHOICES)
	exclusive = models.BooleanField(default=True) #exclusive offer , cannot combine with above

	#Offer status: open, consumed, suspended
	OPEN,SUSPENDED,CONSUMED = ('open','suspended','consumed')
	status = models.CharField(max_length=64,default=OPEN)

	condition = models.ForeignKey('offers.Condition',on_delete=models.CASCADE,related_name="offers")
	benefit = models.ForeignKey('offers.Benefit',on_delete=models.CASCADE,related_name="offer_benefit")

	#Offer priority with multiple offer given
	priority = models.IntegerField(default=0,db_index=True)

	#Offer time-limit
	start_datetime = models.DateTimeField(blank=True,null=True)
	end_datetime = models.DateTimeField(blank=True,null=True)

	#use this field to limit the number of times this offer can be applied in total
	max_global_applications = models.PositiveIntegerField(blank=True,null=True)

	#use this field to limit the number of times this offer can be applied to the single user
	max_user_applications = models.PositiveIntegerField(blank=True,null=True)

	#use this field to limit the no. of times this offer can be applied to a basket
	max_basket_applications = models.PositiveIntegerField(blank=True,null=True)

	#use this field to limit max discount provided by offer
	max_discount = models.DecimalField(max_digits=12,decimal_places=2,default=Decimal("0.00"),null=True,blank=True)


	#field to enforce above limiting fields
	total_discount = models.DecimalField(max_digits=12,decimal_places=2,default=Decimal("0.00"))
	num_applications = models.PositiveIntegerField(default=0)
	num_orders = models.PositiveIntegerField(default=0)

	date_created = models.DateTimeField(auto_now_add=True)


class Benefit(models.Model):
	range = models.ForeignKey('offers.Range',on_delete=models.CASCADE,null=True,blank=True)

	#benefit types
	PERCENTAGE, FIXED, MULTIBUY, FIXED_PRICE=('Percentage','Fixed','Multibuy','Fixed price')
	SHIPPING_PERCENTAGE, SHIPPING_ABSOLUTE, SHIPPING_FIXED_PRICE=('Shipping percentage','Shipping absolute',
		'Shipping fixed price')
	TYPE_CHOICES = (
		(PERCENTAGE,'Discount is a percentage off of the product\'s value'),
		(FIXED,'Discount is a fixed amount off of the product\'s value'),
		(MULTIBUY,'Discount is to give the cheapest product for free'),
		(FIXED_PRICE,'Get the products that meet the condition for a fixed price'),
		(SHIPPING_PERCENTAGE,'Discount is a percentage off of the shipping'),
		(SHIPPING_ABSOLUTE,'Discount is a fixed amount of the shipping cost'),
		(SHIPPING_FIXED_PRICE,'Get shipping for fixed price')
		)
	benefit_type = models.CharField(max_length=128,choices=TYPE_CHOICES,blank=True)

	#value for benefit from one of above types
	value = models.DecimalField(blank=True,null=True,max_digits=12,decimal_places=2)

	#upper limits to discount by this benefit
	max_affected_items = models.PositiveIntegerField(blank=True,null=True)

class Condition(models.Model):
	range = models.ForeignKey('offers.Range',on_delete=models.CASCADE,null=True,blank=True)

	#Condition types to an offer
	COUNT, VALUE, COVERAGE = ('Count','Value','Coverage')
	TYPE_CHOICES=(
		(COUNT,'Depends on number of items in basket that are in condition range'),
		(VALUE,'Depends on value of items in basket that are in condition range'),
		(COVERAGE,'Needs to contain a set number of DISTINCT items  from condition range')
		)
	condition_type = models.CharField(max_length=128,blank=True,choices=TYPE_CHOICES)
	value = models.DecimalField(blank=True,null=True,max_digits=12,decimal_places=2)

class Range(models.Model):
	# Represents a range of products that can be used within an offer.
	name = models.CharField(max_length=128,unique=True)
	slug = models.SlugField(max_length=128,unique=True)
	description = models.TextField(blank=True)

	is_public = models.BooleanField(default=False)
	includes_all_product = models.BooleanField(default=False)
	
	included_products = models.ManyToManyField('catalogue.Product',blank=True,related_name="includes")
	excluded_products = models.ManyToManyField('catalogue.Product',blank=True,related_name="excludes")

	classes = models.ManyToManyField('catalogue.Product',blank=True,related_name="range_classes")
	included_categories = models.ManyToManyField('catalogue.Product',blank=True,related_name="range_categories")
	date_created = models.DateTimeField(auto_now_add=True)