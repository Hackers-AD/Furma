from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''class UserSearch(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="usersearches")
	text = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "User Search"
		verbose_name_plural = "User Searches"'''