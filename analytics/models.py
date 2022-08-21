from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class ProductRecord(models.Model):
	#Records how popular the product is
	product = models.OneToOneField('catalogue.Product',on_delete=models.CASCADE,related_name="stats")

	#Data used for generating score
	num_views = models.PositiveIntegerField(default=0)
	num_basket_additions = models.PositiveIntegerField(default=0)
	num_purchases = models.PositiveIntegerField(default=0,db_index=True)

	score = models.FloatField(default=0.0)

class UserRecord(models.Model):
	#User's activity records
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	#Browsing stats
	num_product_views = models.PositiveIntegerField(default=0)
	num_basket_additions = models.PositiveIntegerField(default=0)

	#order stats
	num_orders = models.PositiveIntegerField(default=0,db_index=True)
	num_order_lines = models.PositiveIntegerField(default=0,db_index=True)
	num_order_items = models.PositiveIntegerField(default=0,db_index=True)

	total_spent = models.DecimalField(max_digits=12,decimal_places=2,default=Decimal('0.00'))
	date_last_order = models.DateTimeField(null=True,blank=True)

class UserProductView(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userproductviews")
	product = models.ForeignKey('catalogue.Product',on_delete=models.CASCADE,related_name="products")
	date_created = models.DateTimeField(auto_now_add=True)

class UserSearch(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="usersearches")
	query = models.CharField(max_length=255,db_index=True)
	date_created = models.DateTimeField(auto_now_add=True)