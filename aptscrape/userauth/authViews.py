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


def indexViews(request, auth_form=None, user_form=None, search_form=None):
    # User is logged in
    
    if request.user.is_authenticated():
        user = request.user
        search_form = ListingParams(data=request.POST)
        if request.method == 'POST':
            
            accept_form(request)

            return render(request,
                'tmp.html',
                {'search_form': search_form, 'user': user, 'next_url': '/', })

        #if request method not POST
        else: 
            return render(request,
                'tmp.html',
                {'search_form': search_form, 'user': user, 'next_url': '/', })
    else:
        # User is not logged in
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
            # Success
            return redirect('/')
        else:
            # Failure
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

