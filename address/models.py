from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
	is_3166_1_a2 = models.CharField(primary_key=True,max_length=2,help_text="alpha2 code")
	is_3166_1_a3 = models.CharField(max_length=3,help_text="alpha3 code",blank=True)
	is_3166_1_numeric = models.CharField(max_length=3,blank=True,help_text="Numeric code")
	printable_name = models.CharField(max_length=128,help_text="Common name")
	name = models.CharField(max_length=128,help_text="Official name")
	is_shipping_country = models.BooleanField(default=False)

	def __str__(self):
		return "%s%s%s"%(self.is_3166_1_a2,self.name,self.is_shipping_country)

	class Meta:
		verbose_name = "Countrie"

class Address(models.Model):
	title = models.CharField(max_length=128,help_text="Mr,Miss,Mrs,Dr",blank=True,null=True)
	first_name = models.CharField(max_length=128,help_text="First name",blank=True,null=True)
	last_name = models.CharField(max_length=128,help_text="Last name",blank=True,null=True)
	line1 = models.CharField(max_length=128,help_text="Adress of line1")
	line2 = models.CharField(max_length=128,help_text="Adress of line2",blank=True,null=True)
	line3 = models.CharField(max_length=128,help_text="Adress of line3",blank=True,null=True)
	city = models.CharField(max_length=128,help_text="City name")
	state = models.CharField(max_length=128)
	zipcode = models.IntegerField()
	country = models.ForeignKey(Country,verbose_name="country",on_delete=models.PROTECT)
	search_text = models.CharField(max_length=128,help_text="search text for address",blank=True,null=True)
	def __str__(self):
		return "%s%s%s%s"%(self.first_name,self.city,self.state,self.zipcode)

	class Meta():
		verbose_name = "Addresse"
			

class UserAddress(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_address")
	address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name="user_address_super",blank=True)
	is_default_shipping = models.BooleanField(default=True)
	is_default_billing = models.BooleanField(default=True)
	total_orders_from_address = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)

	def __str__(self):
		return "%s%s%s%s"%(self.user,self.address,self.total_orders_from_address,self.created_on)

	class Meta:
		verbose_name = "User Addresse"