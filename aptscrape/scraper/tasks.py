from celery import task
from scraper.models import Listing
from django.contrib.auth.models import User

from scraper.scraperViews import toDictionary, accept_form, myhome_crawler, find_prices, cg_crawler, let_crawler

"""
Celery Beat runs this task every minute.

Scrapes the websites and puts all into a data structure.

Scrapes it again after a minute and puts all into another data structure.

Compares the two lists, if anything is in the second list that isn't in the
first one, it notifies the user with those new items.
"""

import requests
from bs4 import BeautifulSoup as bs4
import string

@task()
def add():
    listings_init = []
    listings_2nd = []
    new_listings = []
    #current_user = request.user
    #u_id = current_user.id
    #print(u_id)
    #get first listing from user
    listing = Listing.objects.filter(user_id=3)[0]
    print(listing.city)
    #return listing.maxprice

    #city = listing.city
    city = 'cavan'

    paramD = dict(
        minprice = listing.minprice,
        maxprice = listing.maxprice,
        maxbeds = listing.bedrooms,
        )

    page_num = 1

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

        if link not in listings_init and link not in listings_2nd:
            print ("New listing found!")
            listings_2nd.append(link)
            new_listings.append(title + ' - ' + link)


    if len(listings_2nd) > 0:
        print('Sending mail!')
        #msg = '\n'.join(send_list)
        #m = email.message.Message()
        #m.set_payload(msg)
        #gm.send(m, ['recipient_email@mydomain.com'])
        listings_init += listings_2nd
        listings_2nd = []
        new_listings = []


    return type(listings_init)

