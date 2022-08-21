from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmailAttachment(models.Model):
	file = models.FileField(upload_to="email/files",blank=True,null=True)
	photo = models.FileField(upload_to="email/photos",blank=True,null=True)

class UserEmail(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_emails",verbose_name="UserEmail")
	email = models.EmailField(null=True, blank=True)
	subject = models.TextField(max_length=255)
	body_text = models.TextField()
	body_html = models.TextField(blank=True)
	attachment = models.ManyToManyField(EmailAttachment,blank=True)
	date_sent = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
	recipient = models.ForeignKey(User,db_index=True,on_delete=models.CASCADE,related_name='notifications')
	# Not all notifications will have a sender.
	sender = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	
	# HTML is allowed in this field as it can contain links
	subject = models.CharField(max_length=255)
	body = models.TextField()

	# Some projects may want to categorise their notifications.  You may want
	# to use this field to show a different icons next to the notification.
	category = models.CharField(max_length=255, blank=True)

	INBOX, ARCHIVE = 'Inbox', 'Archive'
	choices = (
        (INBOX, ('Inbox')),
        (ARCHIVE, ('Archive')))
	location = models.CharField(max_length=32, choices=choices,default=INBOX)

	date_sent = models.DateTimeField(auto_now_add=True, db_index=True)
	date_read = models.DateTimeField(blank=True, null=True)

class ProductAlert(models.Model):
	#product = models.ForeignKey('catalouge.product',on_delete=,models.CASCADE)

	# A user is only required if the notification is created by a
    # registered user, anonymous users will only have an email address
    # attached to the notification
	user = models.ForeignKey(User,blank=True,db_index=True,null=True,on_delete=models.CASCADE,related_name="alerts")
	email = models.EmailField(db_index=True, blank=True)

	# This key are used to confirm and cancel alerts for anon users
	key = models.CharField(("Key"), max_length=128, blank=True, db_index=True)

	# An alert can have two different statuses for authenticated
	# users ``ACTIVE`` and ``CANCELLED`` and anonymous users have an
	# additional status ``UNCONFIRMED``. For anonymous users a confirmation
	# and unsubscription key are generated when an instance is saved for
	# the first time and can be used to confirm and unsubscribe the
	# notifications.# This key are used to confirm and cancel alerts for anon users
	key = models.CharField(("Key"), max_length=128, blank=True, db_index=True)

	# An alert can have two different statuses for authenticated
	# users ``ACTIVE`` and ``CANCELLED`` and anonymous users have an
	# additional status ``UNCONFIRMED``. For anonymous users a confirmation
	# and unsubscription key are generated when an instance is saved for
	# the first time and can be used to confirm and unsubscribe the
	# notifications.

	UNCONFIRMED, ACTIVE, CANCELLED, CLOSED = ('Unconfirmed', 'Active', 'Cancelled', 'Closed')
	STATUS_CHOICES = ((UNCONFIRMED, ('Not yet confirmed')),(ACTIVE,('Active')),(CANCELLED,('Cancelled')),(CLOSED, ('Closed')),)

	status = models.CharField(("Status"), max_length=20,choices=STATUS_CHOICES, default=ACTIVE)

	date_created = models.DateTimeField(("Date created"), auto_now_add=True)
	date_confirmed = models.DateTimeField(("Date confirmed"), blank=True,null=True)

	date_cancelled = models.DateTimeField(("Date cancelled"), blank=True,null=True)
	date_closed = models.DateTimeField(("Date closed"), blank=True, null=True)
