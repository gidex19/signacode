from django import forms
from .models import Customuser

software_list = plan_type = [('Web Application','Web Application'), ('Mobile Application','Mobile Application'), ('Desktop Application','Desktop Application'),
                             ('Chatbot','Chatbot'), ('Web Crawler','Web Crawler'), ('Others','Others')]
category_list = [('Personal Project','Personal Project'), ('Business Project','Business Project'), ('Academic/School Project','Academic/School Project'),
                 ('Research Project','Research Project'), ('Others','Others')]

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Fullname', 'class': 'form-control mb-4', 'id': 'inputUsername'}),
        label="")
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email Email Address', 'class': 'form-control mb-4', 'id': 'inputUsername'}),
        label="")
    phone_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Enter Phone No', 'class': 'form-control mb-4', 'id': 'inputUsername'}),
        label="")
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter Project Details (brief)', 'class': 'form-control mb-4', 'id': 'inputUsername', 'required': 'False'}),
        label="")
    software_type = forms.CharField(
        widget=forms.Select(attrs={'placeholder': 'Select Software Type', 'class': 'form-control mb-4', 'id': 'inputUsername'},
                            choices=software_list), label="Software Type")
    category = forms.CharField(
        widget=forms.Select(
            attrs={'placeholder': 'Select Category', 'class': 'form-control mb-4', 'id': 'inputUsername'},
            choices=category_list), label="")


class LoginForm(forms.Form):
    email_address = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control mb-4', 'id': 'inputemail'}),
        label="")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control ', 'id': 'inputpassword'}), label="")

class SignUpForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control mb-4', 'id': 'inputfullname'}),
        label="")

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control mb-4', 'id': 'inputemail'}),
        label="")
    phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control mb-4', 'id': 'inputphonenumber'}),
        label="")

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control mb-4 ', 'id': 'inputpassword'}),
        label="")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password Again', 'class': 'form-control mb-4', 'id': 'inputpassword'}),
        label="")
