from unicodedata import name
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from paystackapi.verification import Verification
import json
import requests
from django.views.generic import View
from django.contrib.auth.hashers import *
from .forms import LoginForm, SignUpForm, ContactForm, InterestForm, MtoMForm
from .models import Customuser, Learn_Blockchain, Learn_Js, Learn_Python, Post, Technews, Payment, Learn_Fullstack, Learn_Techbusiness, Html_And_Css
from signacode.settings import psk, ppk
paystack_secret_key = psk
paystack_public_key = ppk
paystack = Paystack(secret_key=paystack_secret_key)

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk= pk)
    context = { 'post': post}
    return render(request, 'my_app/post_detail.html', context)



def technews_detail(request, pk):
    technews = get_object_or_404(Technews, pk= pk)
    context = { 'technews': technews}
    return render(request, 'my_app/technews_detail.html', context)

def techschool(request):
    return render(request, 'my_app/techschool.html')


def home(request, filled=None):
    print(f'filled: {filled}')
    print(type(filled))
    posts = Post.objects.all()
    technews = Technews.objects.all()[:4]
    context = {'posts':posts, 'technews': technews, 'filled': filled}
    return render(request, 'my_app/home.html', context )


def interests(request):
    form = InterestForm()

    return render(request, 'my_app/interests.html', {'form':form})

def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email_address')
            password = form.cleaned_data.get('password')
            email = email.lower()
            if Customuser.objects.filter(email = email).exists():
                custom_user = authenticate(request, username = email , password=password)
                if custom_user is not None:
                    messages.success(request, 'Login Succesful')
                    login(request, custom_user)
                    messages.success(request, f'Hello {custom_user.full_name} \n, You have been logged in successfully...')
                    if custom_user.interest_filled:
                        # print("user has filled his interest details")
                        return redirect('homepage', filled="True")
                    else:
                        # print("user has not filled his interests detailed")
                        return redirect('homepage', filled="False")
                    return redirect('homepage')
                    #print('user has been logged in')
                    return redirect('homepage')
                elif custom_user is None:
                    #print('message section')
                    messages.warning(request, 'Incorrect email address or password')
            else:
                messages.warning(request, 'Incorrect email address or password')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'my_app/login.html', {'form': form})

def services(request):
    form = ContactForm()

    return render(request, 'my_app/services.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def technews(request):
    technews = Technews.objects.all()
    p = Paginator(technews, 12)
    page = request.GET.get('page')
    technews_list = p.get_page(page)
    return render(request, 'my_app/technews.html', {'technews': technews, 'technews_list': technews_list})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            def verify_doesnt_exists():
                if Customuser.objects.filter(email = email).exists():
                    messages.warning(request, 'This email has been used already')
                    print("email address already exists")
                    return False
                elif Customuser.objects.filter(phone_number = phone_number).exists():
                    messages.warning(request, 'This phone number has already been used before')
                    print("phone_number already exists")
                    return False
                else:
                    return True
            if password1 == password2:
                if verify_doesnt_exists():
                    hashed = make_password(password1, salt = None, hasher='default')

                    Customuser.objects.create(username=email, full_name=full_name, email=email, phone_number=phone_number, password = hashed)
                    custom_user = authenticate(username=email, password=password1,)
                    current_user = Customuser.objects.filter(email=email).first()
                    current_instance = Customuser.objects.filter(email=email)
                    messages.success(request, 'Account Successfully Created')
                    return redirect('login')

                    # user_id = current_user.id
                    # current_instance.update(ref_code = ref_url,  referrer= referrer)

                    # print(ref_url)
                    # print(referrer)


            else:
                messages.warning(request, 'Passwords Don\'t Match')
    else:
        form = SignUpForm()


    return render(request, 'my_app/signup.html', {'form': form})

login_required
def profile(request):
    current_user = request.user
    print(current_user)
    return render(request, 'my_app/profile.html', {'user': current_user})

def about(request):

    return render(request, 'my_app/about.html')

