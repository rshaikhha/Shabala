# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from forms import SignUpForm
from tokens import account_activation_token
from django.utils.encoding import force_text
from .models import Profile
from django.http import Http404
# Create your views here.

def home (request):
    template = 'home.html'
    context = locals()
    return render(request, template, context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False            
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.profile.email = user.email
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/account_activation_invalid.html')


def profile(request,username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        context = {'profile':profile}
        template = "profile.html"
        return render(request, template, context)
    except:
        raise Http404("User not found!")