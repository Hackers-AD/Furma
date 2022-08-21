from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WishList(models.Model):
	#represent USer widhlist of products #only authenticated user have wishlists
	owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="wishlists")
	name = models.CharField(default="Default",max_length=255)
	#privacy of user wishlist
	PUBLIC, PRIVATE, SHARED = ('Public', 'Private', 'Shared')
	VISIBILITY_CHOICES = (
		(PRIVATE, ("Private- only the owner can see the wishlists")),
		(SHARED, "Shared- only the owner and people who have access can see the wishlists"),
		(PUBLIC, "Public- Everbody can see the wishlists")
		)
	visibility = models.CharField(max_length=25,default=PRIVATE,choices=VISIBILITY_CHOICES)
	date_created = models.DateTimeField(auto_now_add=True,db_index=True,editable=False)

	def __str__(self):
		return str(self.owner)

class Line(models.Model):
	#An entry in each wishlist
	wishlist = models.ForeignKey('wishlists.WishList',on_delete=models.CASCADE,related_name="line")
	product = models.ForeignKey('catalogue.Product',on_delete=models.CASCADE,related_name="wishlists_line",null=True,blank=True)
	quantity = models.PositiveIntegerField(default=1)
	title = models.CharField(max_length=255,default="Product Title") #store title in case product is deleted

	def __str__(self):
		return str(self.wishlist)