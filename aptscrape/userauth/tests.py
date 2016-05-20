from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_signup(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000')
        self.selenium.implicitly_wait(20)
        #find the form element

        username = selenium.find_element_by_id('id_username')

        password = selenium.find_element_by_id('id_password')



        submit = selenium.find_element_by_name('action')

        #Fill the form with data
        username.send_keys('poodle')

        password.send_keys('Lfc123456')



        #submitting the form
        submit.send_keys(Keys.RETURN)


    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')
        #find the form element
        city = selenium.find_element_by_id('id_city')
        minprice = selenium.find_element_by_id('id_minprice')
        maxprice = selenium.find_element_by_id('id_maxprice')
        bedrooms = selenium.find_element_by_id('id_bedrooms')


        submit = selenium.find_element_by_name('action')

        #Fill the form with data
        city.send_keys('cavan')
        minprice.send_keys('333')
        maxprice.send_keys('4444')
        bedrooms.send_keys('3')

        #submitting the form
        submit.send_keys(Keys.RETURN)

"""
class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000')
        self.selenium.implicitly_wait(3)
        #find the form element
        email = selenium.find_element_by_id('id_email')
        username = selenium.find_element_by_id('id_username')
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')


        submit = selenium.find_element_by_name('action')

        #Fill the form with data
        email.send_keys('jpoodle@poodle.com')
        username.send_keys('jpoodle')
        first_name.send_keys('justinas')
        last_name.send_keys('ulevicius')
        password1.send_keys('Lfc123456')
        password2.send_keys('Lfc123456')


        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in selenium.page_source


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')
        #find the form element
        city = selenium.find_element_by_id('id_city')
        minprice = selenium.find_element_by_id('id_minprice')
        maxprice = selenium.find_element_by_id('id_maxprice')
        bedrooms = selenium.find_element_by_id('id_bedrooms')


        submit = selenium.find_element_by_name('action')

        #Fill the form with data
        city.send_keys('cavan')
        minprice.send_keys('333')
        maxprice.send_keys('4444')
        bedrooms.send_keys('3')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in selenium.page_source

"""