from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from scraper.scraperParams import ListingParams
from django.template.loader import get_template
from django.template import Context
from scraper.scraperViews import toDictionary, accept_form, myhome_crawler, find_prices, cg_crawler

#need these for registration, login, logout
from django.contrib.auth.models import User
from userauth.forms import AuthenticateForm, UserCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#need these for user profiles
from django.db.models import Count
from django.http import Http404

from scraper.models import Listing

#pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def indexViews(request, auth_form=None, user_form=None, search_form=None, listings=None):
    listings =''
    
    if request.user.is_authenticated():
        #the user is logged in
        user = request.user
        search_form = ListingParams(data=request.POST)
        
        if request.method == 'POST':
            
            listings = accept_form(request)

            #pagination
            
            paginator = Paginator(listings, 40)
            page = request.GET.get('page')
            try:
                lists = paginator.page(page)
            except PageNotAnInteger:
                lists = paginator.page(1)
            except EmptyPage:
                lists = paginator.page(paginator.num_pages)


            return render(request,
                'tmp.html',
                {'search_form': search_form, 'user': user, 'lists': lists, 'next_url': '/', })
        else: 
            return render(request,
                'tmp.html',
                {'search_form': search_form, 'user': user, 'next_url': '/', })


    #user needs to register or log in
    else:
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()
 
        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form})


def loginViews(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        else:
            return indexViews(request, auth_form=form)
    return redirect('/')

 
def logoutViews(request):
    logout(request)
    return redirect('/')


def registerViews(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return indexViews(request, user_form=user_form)
    return redirect('/')
 
 
@login_required
def users(request, username=""):
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        listings = Listing.objects.filter(user=user.id).order_by('-id')
        paginator = Paginator(listings, 5)
        page = request.GET.get('page')
        try:
            searches = paginator.page(page)
        except PageNotAnInteger:
            searches = paginator.page(1)
        except EmptyPage:
            searches = paginator.page(paginator.num_pages)

        if username == request.user.username:
            return render(request, 'user.html', {'user': user, 'searches': searches, })
        return render(request, 'user.html', {'user': user, 'searches': searches,})


