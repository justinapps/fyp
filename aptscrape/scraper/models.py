from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
	city = models.CharField(max_length=58)
	minprice = models.IntegerField()
	maxprice = models.IntegerField()
	bedrooms = models.IntegerField()
	#user = models.ForeignKey(User) #allow us to link searches to user who done it
