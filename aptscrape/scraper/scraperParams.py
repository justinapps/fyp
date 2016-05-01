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

#these params need to be put into a dict for Python's
#Requests to be able to use them for URL creation
class ListingParams(forms.Form):

    minprice = forms.IntegerField(required=False, label='Minimum price')
    maxprice = forms.IntegerField(required=False, label='Maximum price')
    bedrooms = forms.IntegerField(
        required=False, label='Bedrooms', min_value=1, max_value=15
        )
    """
    is_furnished = forms.IntegerField(
        required=False, label='Furnished', min_value=0, max_value=1
        )
    
    """
