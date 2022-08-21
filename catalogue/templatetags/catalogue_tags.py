from django import template
from django.contrib.auth.models import User
from wishlists.models import WishList,Line
from catalogue.models import *

register = template.Library()

@register.filter
def trucatetext(title,truncate_length):
	pass

@register.filter
def userlikedproduct(user,product):
	liked = False
	wishlists = []
	if user.is_authenticated:
		wishlists = WishList.objects.filter(owner=user)
	for wishlist in wishlists:
		wishlines = Line.objects.filter(wishlist=wishlist,product=product)
		for line in wishlines:
			liked = True
	return liked

@register.filter #register.simple_tags
def get_wishlistcount(user):
	wishlinecount = 0
	wishlists = []
	if user.is_authenticated:
		wishlists = WishList.objects.filter(owner=user)
	for wishlist in wishlists:
		wishlines = Line.objects.filter(wishlist=wishlist)
		wishlinecount += len(wishlines)
	return wishlinecount