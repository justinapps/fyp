from django.db import models
from django.contrib.auth.models import User
from userauth.models import UserProfile

class Listing(models.Model):
	city = models.CharField(max_length=58)
	minprice = models.IntegerField()
	maxprice = models.IntegerField()
	bedrooms = models.IntegerField()
	user = models.ForeignKey(User, null=True, blank=True) #allow us to link searches to user who done it
