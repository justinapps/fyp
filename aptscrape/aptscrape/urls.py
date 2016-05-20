"""aptscrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin

from contact import contactViews
from scraper import scraperViews

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	#admin site docs app
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^contact/$', contactViews.contact, name='contact'), #contact form
    url(r'^scraper/$', scraperViews.accept_form, name='scraper'),

    url(r'^$', 'userauth.authViews.indexViews'),
    url(r'^login$', 'userauth.authViews.loginViews'),
    url(r'^logout$', 'userauth.authViews.logoutViews'),
    url(r'^signup$', 'userauth.authViews.registerViews'),

    #user profiles
    url(r'^users/$', 'userauth.authViews.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'userauth.authViews.users'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#scraper.scraperViews.accept_form
"""
its making the form in iindexViews but thats it. its never calling the shit from scraperViews so need to fix that somehow.
"""