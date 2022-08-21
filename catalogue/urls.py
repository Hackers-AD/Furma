from django.urls import path
from .views import *

urlpatterns = [
	path('',furmaHome.as_view(),name='home'),path('featured',FeaturedView.as_view(),name='featured'),
	path('latest',LatestView.as_view(),name='latest'),path('checkout',Checkout.as_view(),name='checkout'),
	path('product/liked',ProductLiked.as_view(),name="likeproduct"),
	path('product/addtocart',AddProductToCart.as_view(),name="productaddtocart"),
	path('cart',Cart.as_view(),name="cart"),
	path('product/<int:pid>',ProductView.as_view(),name="product"),
]