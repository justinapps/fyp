"""
The scraping happens here.
The listing parameters are passed in by the user in a form and
then put into a Python dict so that they can be used by the
Requests module to create a URL to scrape from.
"""
#Imports for form management
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .scraperParams import ListingParams
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import redirect

#Imports for scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs4
import numpy as np
import string

#Only doing myhome for testing purposes, will implement other
#websites later.

def toDictionary(request):
	minprice = request.POST.get('minprice', '')
	maxprice = request.POST.get('maxprice', '')
	bedrooms = request.POST.get('bedrooms', '')
	#is_furnished = request.POST.get('is_furnished', '')
	
	#myhome dictionary		
	return dict(minprice = minprice,
				maxprice = maxprice,
				bedrooms = bedrooms,
				)

	#cg dictionary will go here


def accept_form(request):

	apt_params = ListingParams #shit from the user form comes here

	paramD = dict()
	if request.method == 'POST':
		form = apt_params(data=request.POST)
		if form.is_valid():
			paramD = toDictionary(request)
			myhome_crawler(paramD)

		else:
			print("Form errors occured in scraper.scrapeViews.py: ")
			print(form.errors)
			

			return redirect('scraper')

	#if len(paramD) == 0:
	#	print()

	print(paramD)
	paramD = dict()

	return render(request, 'scraper/scraper.html', {
		'form': apt_params,
		})




def myhome_crawler(paramD):

	__count = 0
	__page_num = 1

	while __page_num != 2:

		url_base = 'http://www.myhome.ie/rentals/dublin/property-to-rent?format=rss' + '&page=' + str(__page_num)
		resp = requests.get(url_base, params = paramD)
		#print ("the value of the url is {}".format(url_base))
		print(resp.url)
		html = bs4(resp.text, 'html.parser')
		apts = html.findAll('item')
		print('Number of listings on page: ' + str(len(apts)))

		for apt in apts:

			title = apt.find_all('title')[0].text.split(' - ')[0]
			link = apt.find_all('link')[0].text
			price = apt.find_all('price')[0].text.strip('€') #.strip(' / month')
			n_brs = apt.find_all('bedrooms')[0].text.strip(' Bed')

			__count = __count + 1

			print( '('+ str(__count) +'.) ' + title + '\n' + link + '\n' + price + '\n' + n_brs + '\n')

		__page_num = __page_num + 1
		#print(resp.url)

		

		print("myhome shit ran")

