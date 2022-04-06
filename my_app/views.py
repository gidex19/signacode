from turtle import title
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
from .forms import LoginForm, SignUpForm, ContactForm, InterestForm, MtoMForm, IForm
from .models import Customuser, Learn_Blockchain, Learn_Js, Learn_Python, Post, Technews, ProjectDetail, Payment, Learn_Fullstack, Learn_Techbusiness, Html_And_Css
from signacode.settings import psk, ppk
paystack_secret_key = psk
paystack_public_key = ppk 
paystack = Paystack(secret_key=paystack_secret_key)

# Create your views here.

class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get('button_text')
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")
        print(text)
        if request.is_ajax():
            return JsonResponse({'seconds':'my data recieved' })
        return render(request, 'my_app/test.html')

def ajax_home(request, filled=None):
    posts = Post.objects.all()
    technews = Technews.objects.all()[:4]
    context = {'posts':posts, 'technews': technews, 'filled': filled}
    text = request.GET.get('button_text')
    print(text)
    if request.is_ajax():
        if request.user.is_authenticated:
            user = request.user
            if user.interest_filled == False:
                return JsonResponse({'seconds':'user is logged in but has not filled the interest form' })
            else:
                return JsonResponse({'seconds':'user is logged in but has already filled the interest form' })
        else:
            if request.is_ajax():
                return JsonResponse({'seconds':'user is not logged in' })
    return render(request, 'my_app/ajax_home.html', context )

def home(request):
    posts = Post.objects.all()
    technews = Technews.objects.all()[:8]
    context = {'posts':posts, 'technews': technews}
    text = request.GET.get('button_text')
    print(text)
    if request.is_ajax():
        if request.user.is_authenticated:
            user = request.user
            if user.interest_filled == False:
                return JsonResponse({'status':'User interests not filled'})
        else:
            if request.is_ajax():
                return JsonResponse({'status':'User not logged in' })

    return render(request, 'my_app/home.html', context )



@login_required
def subscribe_hc(request):
    print("we are here at subs FOR JS")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Hc',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)


@login_required
def subscribe_js(request):
    print("we are here at subs FOR JS")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Js',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)




@login_required
def subscribe_python(request):
    print("we are here at subs FOR PYTHON")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Python',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)


@login_required
def subscribe_fullstack(request):
    print("we are here at subs FOR FULLSTACK")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Fullstack',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)    

@login_required
def subscribe_business(request):
    print("we are here at subs FOR BUSINESS")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Business',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)    

@login_required
def subscribe_blockchain(request):
    print("we are here at subs FOR BLOCKCHAIN")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Blockchain',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)    

@login_required
def subscribe_dm(request):
    print("we are here at subs FOR DIGITAL MAKETING")
    amount = 10000
    user = request.user
    full_name = request.user.full_name
    email = request.user.email
    phone = request.user.phone_number

    response = Transaction.initialize(amount=amount, email=email)
    
    ref = response['data']['reference']
    print(full_name)
    print(ref)
    print("-------------------------------------")
    print(response)
    print("--------------------------------------")
    create_pay_instance = Payment.objects.create(customer=user, customers_email=email,
                                                   customers_phone=phone, product_type='Learn Dm',
                                                   reference=ref, amount=amount)    
    a_url = response['data']['authorization_url']
    return redirect(a_url)    


# {'status': True, 'message': 'Authorization URL created', 'data': {'authorization_url': 'https://checkout.paystack.com/ioyt36us9bc6wc6', 'access_code': 'ioyt36us9bc6wc6', 'reference': '9sxzb9weo8'}}
@login_required
def verify_payments(request):
    print("verifying function")
    paramz = request.GET.get('trxref', 'None')
    user = request.user
    email = request.user.email
    current_user = Customuser.objects.filter(email = email)
    pay_queryobj = Payment.objects.all().filter(reference=paramz, customer=user)
    if pay_queryobj.exists():
        print("it exists")    
        pay_instance = Payment.objects.all().filter(reference=paramz, customer=user).first()
        details = Transaction.verify(reference=paramz)
        status = details['data']['status']
        if status == 'success':
            if pay_instance.product_type == 'Learn Js':
                print("js payment verification ")
                pay_queryobj.update(paid=True)
                current_user.update(js_paid=True)
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the LEARN JAVASCRIPT COURSE')
                return redirect('techschool')
            elif pay_instance.product_type == 'Learn Fullstack':
                print("fullstack payment verification")
                pay_queryobj.update(paid=True)
                current_user.update(html_and_css_paid = True, js_paid=True, python_paid=True, fullstack_paid = True)
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the LEARN FULLSTACK WEB DEVELOPMENT')    
            elif pay_instance.product_type == 'Learn Python':
                print("python payment verification")
                pay_queryobj.update(paid=True)
                current_user.update(python_paid=True)
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the LEARN PYTHON COURSE')
            elif pay_instance.product_type == 'Learn Hc':
                print("python payment verification")
                pay_queryobj.update(paid=True)
                current_user.update(html_and_css_paid=True)
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the HTML AND CSS COURSE')
            elif pay_instance.product_type == 'Learn Blockchain':
                print("blockchain payment verification")
                pay_queryobj.update(paid=True)
                current_user.update(blockchain_paid=True)
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the BLOCKCHAIN COURSE')
            elif pay_instance.product_type == 'Learn Business':
                print("business payment verification")
                pay_queryobj.update(paid=True)
                current_user.update(business_paid=True)        
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the TECH BUSINESS COURSE')
            elif pay_instance.product_type == 'Learn Dm':
                print("digital marketing payment verification")
                pay_queryobj.update(paid=True)
                current_user.update(digital_marketing_paid=True)        
                messages.success(request, f'Hello {user.full_name}, You have successfully registered for the DIGITAL MARKETING COURSE')
            else:
                return redirect('homepage')    
                print("payment plan not know")
        else:
            print("payment not successful")
            messages.info(request, "SORRY!!!.... your payment was not successful please try again")
            return redirect('techschool')
    else:
        print("invalid URL ....queryobject does not exist")
        messages.info(request, "SORRY!!!....user has not registered. You will have to make your payment")
        return redirect('techschool')
            
    return redirect('techschool')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk= pk)
    context = { 'post': post}
    return render(request, 'my_app/post_detail.html', context)

def technews_detail(request, pk):
    technews = get_object_or_404(Technews, pk= pk)
    context = { 'technews': technews}
    return render(request, 'my_app/technews_detail.html', context)


def techschool(request):
    # messages.info(request, "just testing my code to observe something")
    return render(request, 'my_app/techschool.html')


def learn_js(request):
    js_courses = Learn_Js.objects.all()
    first_course = Learn_Js.objects.first()
    return render(request, 'my_app/learn_js.html', {'js_courses': js_courses, 'first_course': first_course })


def learn_python(request):
    py_courses = Learn_Python.objects.all()
    first_course = Learn_Python.objects.first()
    return render(request, 'my_app/learn_python.html', {'py_courses': py_courses, 'first_course': first_course})

def learn_hc(request):
    hc_courses = Html_And_Css.objects.all()
    first_course = Html_And_Css.objects.first()
    return render(request, 'my_app/learn_hc.html', {'hc_courses': hc_courses, 'first_course': first_course})


def learn_blockchain(request):
    blockchain_courses = Learn_Blockchain.objects.all()
    first_course = Learn_Blockchain.objects.first()
    return render(request, 'my_app/learn_blockchain.html', {'blockchain_courses': blockchain_courses, 'first_course': first_course})


def learn_fullstack(request):
    return render(request, 'my_app/learn_fullstack.html')

def learn_branding(request):
    branding_courses = Learn_Techbusiness.objects.all()
    first_course = Learn_Techbusiness.objects.first()
    context = {'branding_courses': branding_courses, 'first_course': first_course}
    return render(request, 'my_app/learn_branding.html', context)


@login_required
def learn_js_detail(request, pk):
    user = request.user
    js_courses = Learn_Js.objects.all()
    print("------------------------------------")
    print(user)
    if user.js_paid:
        course = get_object_or_404(Learn_Js, pk= pk)
    else:
        messages.info(request, "sorry you have not paid for this course. Please purchase course to proceed")
        return redirect('techschool')
    return render(request, 'my_app/learn_js_detail.html', {'course': course, 'js_courses': js_courses })




@login_required
def learn_python_detail(request, pk):
    user = request.user
    if user.python_paid:
        course = get_object_or_404(Learn_Python, pk= pk)
    else:
        messages.info(request, "sorry you have not paid for this course. Please purchase course to proceed")
        return redirect('techschool')
    return render(request, 'my_app/learn_python_detail.html', {'course': course })

def myajaxtestview(request):
    return HttpResponse(request.POST['text'])
    
@login_required
def test(request, course, pk):
    user = request.user
    course = course.lower()
    def verify_paid_for_each_course(course, user, pk):
        pk = int(pk)
        # print(f'course: {course} ----- user: {user.email}')
        if course == 'learn-js':
            # print(user.email)
            if user.js_paid == True:
                if Learn_Js.objects.filter(id=pk).exists():
                    c = Learn_Js.objects.filter(id=pk).first()
                    if c.test_available == True:
                        print(c.test_available)
                        print("user as paid for js course and test is available for course")
                        # messages.info(request, "No test is available for the course you requested")
                        return True
                    else:
                        print("psid user but no test available for dis course")
                        print(c.test_available)
                        messages.success(request, "No test is available for the course you requested")

                        # messages.info(request, "No test available for this course")
                        return redirect('techschool')
                        
                else:
                    messages.info(request, "Course does not exist ")
                    return redirect('techschool')
            else:
                # messages.info(request, "ony paid users can visit the requested page")
                return redirect('techschool')
        elif course == 'learn-python':
            
            if user.python_paid == True:
                if Learn_Python.objects.filter(id=pk).exists():
                    c = Learn_Python.objects.filter(id=pk).first()
                    if c.test_available == True:
                        print(c.test_available)
                        print("user as paid for python course and test is available for course")
                        # messages.info(request, "No test is available for the course you requested")
                        return True
                    else:
                        print("paid user but no test available for dis course")
                        print(c.test_available)
                        messages.success(request, "No test is available for the course you requested")

                        # messages.info(request, "No test available for this course")
                        return redirect('techschool')
                        
                else:
                    messages.info(request, "Course does not exist ")
                    return redirect('techschool')
            else:
                # messages.info(request, "ony paid users can visit the requested page")
                return redirect('techschool')
        elif course == 'learn-blockchain':
            if user.blockchain_paid == True:
                if Learn_Blockchain.objects.filter(id=pk).exists():
                    c = Learn_Blockchain.objects.filter(id=pk).first()
                    if c.test_available == True:
                        print(c.test_available)
                        print("user as paid for js course and test is available for course")
                        # messages.info(request, "No test is available for the course you requested")
                        return True
                    else:
                        print("psid user but no test available for dis course")
                        print(c.test_available)
                        messages.success(request, "No test is available for the course you requested")

                        # messages.info(request, "No test available for this course")
                        return redirect('techschool')
                        
                else:
                    messages.info(request, "Course does not exist ")
                    return redirect('techschool')
            else:
                # messages.info(request, "ony paid users can visit the requested page")
                return redirect('techschool')
        else:
            print("no such course exists in the database")
            return False    
    
    
    # print(verify_paid_for_each_course(course , user, pk))
    if verify_paid_for_each_course(course, user, pk)==True:
        '/media/json_file/english.json'
        json_name = '/media/json_file/' + course + str(pk) + '.json'
        print(json_name)
        context = {'json_name': json_name}
        return render(request, 'my_app/test.html', context)    
    else:
        messages.success(request, "No test available")
        return redirect('techschool')
    return render(request, 'my_app/test.html')


def ace(request):
    
    #response = requests.get("http://api.open-notify.org/astros.json")
    response = requests.get("https://newsapi.org/v2/everything?q=keyword&apiKey=5cfc4aeaa97d4e58a66e5d19bcc1953a")
    data = response.text
    datas = json.loads(data)
    articles_list = datas['articles']
    # print(articles_list)
    for article in articles_list:
        print(article['title'])
        print(article['description'])
        print(article['content'])
        print(article['urlToImage'])
        Technews.objects.create(title=article['title'], content=article['content'], image_url = article['urlToImage'] )
        print("=====================saved to the database===========================")

    course = Learn_Js.objects.last()
    return render(request, 'my_app/ace.html', {'course': course })

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
                    # messages.success(request, 'Login Succesful')
                    login(request, custom_user)
                    print("Hello custom_user.full_name, You have been logged in successfully...would you love to fill in your interests?")
                    messages.success(request, f'Hello {custom_user.full_name} \n, You have been logged in successfully...would you love to fill in your interests?')
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

def interests(request):
    if request.method=='POST':
        form = InterestForm(request.POST)
        mform = IForm(request.POST)
        context = {'form':form, 'mform':mform}
        if form.is_valid():    
            item1 = form.cleaned_data.get('location')
            data = form.cleaned_data.get('')
            # m_data = mform.cleaned_data['my_field']
            print("form is valid")
            print(item1)
            # print(m_data)
    else:
        form = InterestForm()
        mform = MtoMForm()
        context = {'form':form, 'mform':mform}
        print("form is not valid")    
        return render(request, 'my_app/interests.html', context)
    return render(request, 'my_app/interests.html', context)
    
def modal(request):
    return render(request, 'my_app/modal.html')

def services(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone_number')
            details = form.cleaned_data.get('details')
            software_type = form.cleaned_data.get('software_type')
            category = form.cleaned_data.get('category')
            ProjectDetail.objects.create(full_name = full_name, email = email, phone = phone,
             details = details, software_type = software_type, category = category )
            messages.success(request, 'Thank You!!! \nYour message has been recieved. \nWe will get back to you shortly')
            print('form submitted')
            
            return redirect('homepage')

    else:
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