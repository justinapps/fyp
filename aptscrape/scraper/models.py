from django.db import models
from django.contrib.auth.models import User
from userauth.models import UserProfile

CITIES = (  
    ('Dublin', 'dublin'),
    ('Cavan', 'cavan'),
    ('Kilkenny', 'kilkenny'),
    ('Meath', 'meath'),
)

#choices=CITIES

class Listing(models.Model):
	city = models.CharField(max_length=58)
	minprice = models.IntegerField()
	maxprice = models.IntegerField()
	bedrooms = models.IntegerField()
	user = models.ForeignKey(User, null=True, blank=True) #allow us to link searches to user who done it
