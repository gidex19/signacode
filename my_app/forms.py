from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from .models import Customuser, Interest

software_list = plan_type = [('Web Application','Web Application'), ('Mobile Application','Mobile Application'), ('Desktop Application','Desktop Application'),
                             ('Chatbot','Chatbot'), ('Web Crawler','Web Crawler'), ('Others','Others')]
learn_list =  [('Programming','Programming'), ('Graphics Design','Graphics Design'), ('Animation','Animation'),
                             ('Cryptocurrency','Cryptocurrency'), ('Business Branding','Business Branding'),
                             ('HTML and CSS','HTML and CSS'), ('Python','Python'), ('Javascript','Javascript')]
DEMO_CHOICES =(
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)
category_list = [('Personal Project','Personal Project'), ('Business Project','Business Project'), ('Academic/School Project','Academic/School Project'),
                 ('Research Project','Research Project'), ('Others','Others')]
states_list = (("Abia", "Abia"), ("Adamawa", "Adamawa"), ("Anambra","Anambra"), ("Akwa Ibom", "Akwa Ibom"), ("Bauchi", "Bauchi"),
    ("Bayelsa","Bayelsa"), ("Benue","Benue"), ("Borno","Borno"), ("Cross River","Cross River"), ("Delta", "Delta"), ("Ebonyi", "Ebonyi"),
    ("Enugu", "Enugu"), ("Edo","Edo"), ("Ekiti", "Ekiti"), ("FCT - Abuja", "FCT - Abuja"), ("Gombe", "Gombe"), ("Imo", "Imo") ,
    ("Jigawa", "Jigawa"), ("Kaduna", "Kaduna"), ("Kano", "Kano"), ("Katsina", "Katsina"), ("Kebbi" , "Kebbi"), ("Kogi", "Kogi"),
    ("Kwara", "Kwara") , ("Lagos", "Lagos"), ("Nasarawa", "Nasarawa"), ("Niger", "Niger"), ("Ogun", "Ogun"), ("Ondo", "Ondo"),
    ("Osun", "Osun"), ("Oyo", "Oyo"), ("Plateau", "Plateau"), ("Rivers", "Rivers"), ("Sokoto", "Sokoto"), ("Taraba", "Taraba"),
    ("Yobe", "Yobe"), ("Zamfara", "Zamfara"))
class MtoMForm(ModelForm):
    class Meta:
        model = Customuser
        fields = ('Interests',)
        widgets = {
            'description': forms.Textarea(attrs={'cols':30, 'rows': 10}),
            'Interests': forms.CheckboxSelectMultiple,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Interests'].widget.attrs.update({'class': ' i-field'})
class IForm(ModelForm):
    class Meta:
        model = Interest
        fields = ('my_field',)
        widgets = {
            # 'description': forms.Textarea(attrs={'cols':30, 'rows': 10}),
            'Interests': forms.CheckboxSelectMultiple,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['my_field'].widget.attrs.update({'class': ' i-field'})

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Fullname', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email Email Address', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")
    phone_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Enter Phone No', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter Project Details (brief)', 'class': 'form-control mb-4', 'id': 'inputfield', 'required': 'False'}),
        label="")
    software_type = forms.CharField(
        widget=forms.Select(attrs={'placeholder': 'Select Software Type', 'class': 'form-control mb-4', 'id': 'inputfield'},
                            choices=software_list), label="Software Type")
    category = forms.CharField(
        widget=forms.Select(
            attrs={'placeholder': 'Select Category', 'class': 'form-control mb-4', 'id': 'inputfield'},
            choices=category_list), label="")
class InterestForm(forms.Form):
    location = forms.CharField(
        widget=forms.Select(attrs={'placeholder': 'Select Location', 'class': 'form-control mb-4 inputfield', 'id': 'inputlocation'},
                            choices=states_list), label="Select Your Location")
    learn =  forms.CharField(
        widget=forms.Select(attrs={'placeholder': 'Select your Interests', 'class': 'form-control mb-4 inputfield', 'id': 'inputlearn'},
                            choices=learn_list), label="Select Your Interest")
    # geeks_field = forms.MultipleChoiceField( choices = DEMO_CHOICES)

class LoginForm(forms.Form):
    email_address = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control ', 'id': 'inputfield'}), label="")
        

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
