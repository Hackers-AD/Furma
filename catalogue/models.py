from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductClass(models.Model):
	"""
	Used for defining options and attributes for a subset of products.
	E.g. Books, DVDs and Toys. A product can only belong to one product class.

	At least one product class must be created when setting up a new Oscar deployment."""
	name = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128,unique=True)
	requires_shipping = models.BooleanField(default=True) #some product dont require shipping like buiklding website for other
	track_stock = models.BooleanField(default=True)


	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = "Product Class"
		verbose_name_plural = "Product Classes"


class Category(models.Model):
	"""
    A product category. Merely used for navigational purposes; has no
    effects on business logic.

    Uses django-treebeard.
    """
	name = models.CharField(max_length=255,db_index=True)
	description = models.TextField(blank=True)
	img = models.FileField(upload_to="categories",blank=True,null=True)
	slug = models.SlugField(max_length=255,db_index=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

class Product(models.Model):
	upc = models.CharField(max_length=64,blank=True,null=True,unique=True) #universal product code
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	product_class = models.ForeignKey('catalogue.ProductClass',null=True,blank=True,on_delete=models.PROTECT)
	product_attributes = models.ManyToManyField('catalogue.ProductAttribute',blank=True)
	categories = models.ManyToManyField('catalogue.Category')
	rating = models.FloatField(null=True,editable=True)
	is_discountable = models.BooleanField(default=True)
	created_on = models.DateTimeField(null=True,blank=True,auto_now_add=True)
	slug = models.SlugField(max_length=255, unique=False) ##used for generating valid url

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

class ProductAttribute(models.Model):
	#Defines an attribute for a product class. (For example, number_of_pages for a 'book' class)
	product_class = models.ForeignKey('catalogue.ProductClass',on_delete=models.CASCADE,null=True,blank=True)
	name = models.CharField(max_length=128)
	code = models.SlugField(max_length=128)

	def __str__(self):
		return "%s%s%s"%(self.name,"=>",self.code)

	class Meta:
		verbose_name = "Product Attribute"
		verbose_name_plural = "Product Attributes"

class ProductAttributeValue(models.Model):
	#specifies value of attrbutes for particular product
	product = models.ForeignKey('catalogue.Product',on_delete=models.CASCADE,related_name="productattrvalues")
	attribute = models.ForeignKey('catalogue.ProductAttribute',on_delete=models.CASCADE,related_name="productattrs")

	value_text = models.TextField(blank=True, null=True)
	value_integer = models.IntegerField(blank=True, null=True, db_index=True)
	value_boolean = models.NullBooleanField(blank=True, db_index=True)
	value_float = models.FloatField(blank=True, null=True, db_index=True)
	value_richtext = models.TextField(blank=True, null=True)
	value_date = models.DateField(blank=True, null=True, db_index=True)
	value_datetime = models.DateTimeField(blank=True, null=True, db_index=True)
	value_file = models.FileField(upload_to="product/attributes/", max_length=255,blank=True, null=True)
	value_image = models.ImageField(upload_to="product/attributes/", max_length=255, blank=True, null=True)
	

class ProductImage(models.Model):
	product = models.ForeignKey('catalogue.Product',on_delete=models.PROTECT)
	original = models.FileField(upload_to="Product/Images")
	caption  = models.CharField(max_length=200,blank=True)
	display_order = models.PositiveIntegerField(default=0)
	created_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)

	def __str__(self):
		return str(self.original)

	class Meta:
		verbose_name = "Product Image"
		verbose_name_plural = "Product Images"

class ProductGroup(models.Model):
	#Gouping by room,period,category
	name = models.CharField(max_length=128)

	def __str__(self):
		return str(self.name)

class Option(models.Model):
	#Living Room,Dinign Room,Chairs,Tables,Vintage,antique
	group = models.ForeignKey('catalogue.ProductGroup',on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	image = models.FileField(upload_to="product/group/images",blank=True)
	slug = models.SlugField(max_length=128,unique=True,blank=True)

	def __str__(self):
		return str(self.name)
