"""
Using Django's Forms API, grab search parameters for an
apartment from the user. These params will be thrown
into a dictionary and used by the scrapers in scraperParams.py

Required information from the user:
    - minimum price
    - maximum price
    - number of bedrooms
    To be added later (and used by cg):
    - is_furnished (1 for yes, 0 for no)
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from scraper.models import Listing
from scraper.models import CITIES
'''
CITIES = (  
    ('Dublin', 'dublin'),
    ('Cavan', 'cavan'),
    ('Kilkenny', 'kilkenny'),
    ('Meath', 'meath'),
)
'''

#these params need to be put into a dict for Python's
#Requests to be able to use them for URL creation
class ListingParams(forms.ModelForm):

    #city = forms.ChoiceField(widget=forms.Select(choices=CITIES), required=True )


    city = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'City'}))
    minprice = forms.IntegerField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'Minimum price'}))
    maxprice = forms.IntegerField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'Maximum price'}))
    bedrooms = forms.IntegerField(
        required=False, widget=forms.widgets.TextInput(attrs={'placeholder': 'Bedrooms'}), min_value=1, max_value=15
        )
    """
    is_furnished = forms.IntegerField(
        required=False, label='Furnished', min_value=0, max_value=1
        )
    """
    class Meta:
        fields = ['city', 'minprice', 'maxprice', 'bedrooms', 'user']
        model = Listing
        #prevent it from being rendered
        exclude = ('user',)
