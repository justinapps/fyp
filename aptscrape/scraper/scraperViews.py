"""
The scraping happens here.
The listing parameters are passed in by the user in a form and
then put into a Python dict so that they can be used by the
Requests module to create a URL to scrape from.
"""
#Imports for form management
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .scraperParams import ListingParams
from django.template.loader import get_template
from django.template import Context

#need these for registration, login, logout
#from django.contrib.auth.models import User
#from scraper.scraperParams import AuthenticateForm, UserCreateForm, ListingParams
#from django.contrib.auth import login, authenticate, logout

#Imports for scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs4
import numpy as np
import string

#Only doing myhome and cg for testing purposes, will implement other
#websites later.

def toDictionary(request):
    #city = request.POST.get('city', '')
    minprice = request.POST.get('minprice', '')
    maxprice = request.POST.get('maxprice', '')
    bedrooms = request.POST.get('bedrooms', '')
    #is_furnished = request.POST.get('is_furnished', '')
    
    #myhome dictionary      
    return dict(minprice = minprice,
                maxprice = maxprice,
                maxbeds = bedrooms,
                )

    #cg dictionary will go here


def accept_form(request):

    apt_params = ListingParams #shit from the user form comes here

    paramD = dict()
    city = ''
    if request.method == 'POST':
        listing_form = apt_params(data=request.POST)
        if listing_form.is_valid():

            listing = listing_form.save(commit=False)
            listing.user = request.user
            
            listing.save()
            listing_form = ListingParams
            city = request.POST.get('city', '').lower()
            paramD = toDictionary(request)
            cgParamD = dict(
                min_price = paramD['minprice'],
                max_price = paramD['maxprice'],
                bedrooms = paramD['maxbeds'],
                #is_furnished = furnished,
                )

            listings = myhome_crawler(paramD, city)
            #print(listings)
            #cg_crawler(cgParamD, city)


        else:
            print("Form errors occured in scraper.scrapeViews.py, most likely not a POST method: ")
            print(listing_form.errors)

            return redirect('/')

    #if len(paramD) == 0:
    #   print()

    print(paramD)
    #paramD = dict()

    return listings


def myhome_crawler(paramD, city):

    count = 0
    page_num = 1
    apt_list = []
    list_of_apts = [];

    while page_num != 2:

        url_base = 'http://www.myhome.ie/rentals/' + city + '/property-to-rent?format=rss' + '&page=' + str(page_num)
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
            try:
                image = apt.find_all('image')[0].text
            except Exception:
                return

            if len(title) >= 29:
                truncated = title[:27] + '...'
            else:
                truncated = title

            print(image)
            count = count + 1
            apt_list = [title, link, price, n_brs, image, truncated]

            list_of_apts.append(apt_list)

            #print( '('+ str(count) +'.) ' + title + '\n' + link + '\n' + price + '\n' + n_brs + '\n')

        page_num = page_num + 1
        #print(resp.url)

        print("myhome crawler ran")
        return list_of_apts


def find_prices(apartments):

    prices = []
    for rw in apartments:
        price = rw.find('span', {'class': 'price'})
        if price is not None:
            price = float(price.text.strip('â‚¬').strip('�').strip('$').strip('€').strip('£'))
        else:
            price = np.nan
        prices.append(price)
    return prices


def cg_crawler(cgParamD, city):

    count = 0
    listing_n = 0
    results = []

    pagination = np.arange(0, 400, 100)

    for i in pagination:

        url = 'http://' + city + '.craigslist.org/search/apa'
        cgParamD['s'] = str(count*100)
        count = count + 1

        resp = requests.get(url, params=cgParamD)
        print(resp.url)

        txt = bs4(resp.text, 'html.parser')
        apts = txt.findAll(attrs={'class': "row"})

        org_title = [rw.find('a', attrs={'class': 'hdrlnk'}).text for rw in apts]

        #print(title)
        links = [rw.find('a', attrs={'class': 'hdrlnk'})['href'] for rw in apts]
        #print(links)
        price = find_prices(apts)
        #print("number of prices listed" +str(len(price)))
        #print (price)


        size_text = [rw.findAll(attrs={'class': 'housing'})[0].text for rw in apts]

        sizes = [rw.findAll(attrs={'class': 'housing'})[0].text.split(' - ')[1] for rw in apts]
        #print(sizes)
        n_brs = [rw.findAll(attrs={'class': 'housing'})[0].text.split(' - ')[0].replace('/ ', '') for rw in apts]
        #print(n_brs)

        data = np.array([price, sizes, n_brs, org_title, links])
        col_names = ['price', 'size', 'brs', 'org_title', 'link']
        df = pd.DataFrame(data.T, columns=col_names)

        results.append(df)

    results = pd.concat(results, axis=0)


    print("cg crawler ran")