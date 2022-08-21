from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import *
from wishlists.models import WishList,Line as wishlistLine
from analytics.models import *
from django.utils import timezone
from django.templatetags.static import static

import random
import re
# Create your views here.
class furmaHome(View):
	def get(self,request):
		goptions = Option.objects.all()
		products = Product.objects.all()
		products = random.sample(list(products),9)
		pimages = []
		for product in products:
			pimg = ProductImage.objects.filter(product=product)[0]
			pimages.append(pimg)

		wishlines = wishlistLine.objects.all()
		return render(request,'catalogue/home.html',{'wishlines':wishlines,'options':goptions,
			'products':products,'pimages':pimages})

class FeaturedView(View):
	def get(self,request):
		products = Product.objects.all()
		products = random.sample(list(products),6)
		pimages = []
		for product in products:
			pimg = ProductImage.objects.filter(product=product)[0]
			pimages.append(pimg) 
		return render(request,'catalogue/featured.html',{'products':products,'pimages':pimages})

class LatestView(View):
	def get(self,request):
		products = Product.objects.all()
		products = random.sample(list(products),6)
		pimages = []
		for product in products:
			pimg = ProductImage.objects.filter(product=product)[0]
			pimages.append(pimg) 
		return render(request,'catalogue/latest.html',{'products':products,'pimages':pimages})

class Checkout(View):
	def get(self,request):
		return render(request,'catalogue/checkout.html',{})

class ProductLiked(View):
	def get(self,request):
		wishlist = None
		pid = None
		liked = True

		if request.GET.get('product_id',""):
			pid = request.GET['product_id']
		product=Product.objects.get(id=pid)

		if request.user.is_authenticated:
			wishlist = WishList.objects.get_or_create(owner=request.user)[0]

		if wishlist and pid:
			line = wishlistLine.objects.filter(wishlist=wishlist,product=product)
			if len(line) > 0:
				line.delete()
				liked = False
			else:
				line = wishlistLine.objects.create(wishlist=wishlist,product=product)
		if liked:
			return JsonResponse({'img':"<img src='%s' class='heart'>"%static('catalogue/img/core-img/redheart.png'),'liked':liked})
		else:
			return JsonResponse({'img':"<img src='%s' class='heart'>"%static('catalogue/img/core-img/heart.png'),'liked':liked})

class AddProductToCart(View):
	def get(self,request):
		return JsonResponse({'btncontent':"<span class='fa fa-check'></span> Added to Cart"})

class Cart(View):
	def get(self,request):
		products = Product.objects.all()
		products = random.sample(list(products),6)
		pimages = []
		for product in products:
			pimg = ProductImage.objects.filter(product=product)[0]
			pimages.append(pimg) 
		return render(request,'catalogue/cart.html',{'products':products,'pimages':pimages})

class ProductView(View):
	def get(self,request,pid):
		p = Product.objects.get(id=pid)
		pimg = ProductImage.objects.filter(product=p)

		products = Product.objects.all()
		products = random.sample(list(products),6)

		pimages = []
		for product in products:
			product_image = ProductImage.objects.filter(product=product)[0]
			pimages.append(product_image)
		return render(request,'catalogue/product.html',{'products':products,'pimages':pimages,'p':p,'pimg':pimg})