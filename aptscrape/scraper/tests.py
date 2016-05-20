from django.test import TestCase
from django.test.client import Client
from scraper.models import Listing
import datetime

from django.core.urlresolvers import reverse
from scraper.scraperViews import add_listing


# Create your tests here.
class scraperViewsTestCase(TestCase):
	def test_index(self):
		client = Client()
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "New to PadFindr?")

		add_listing('dublin', 100, 1000, 3, 'poodle')



"""
	def test_accept_form(self):
		from scraper.scraperViews import accept_form
		client = Client()
		response = client.get('/')
		request = response.wsgi_request
		self.assertTrue(accept_form(request))
"""