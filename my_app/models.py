from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image
from .validators import image_validator

# Create your models here.

plan_type = (('Learn Js','Learn Js'), ('Learn Python','Learn Python'), ('Digital Marketing','Digital Marketing'), ('Blockchain','Blockchain'))

class Interest(models.Model):
    title = models.CharField(max_length=30, blank=False, default='None' )

    def __str__(self):
        return self.title


class Customuser(AbstractUser):
    full_name = models.CharField(max_length = 35, blank= True)
    phone_number = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length = 100, blank= True)
    interest_filled = models.BooleanField(default=False)
    Interests = models.ManyToManyField(Interest, blank=True)
    
    js_paid = models.BooleanField(default=False)
    html_and_css_paid = models.BooleanField(default=False)
    python_paid = models.BooleanField(default=False)
    fullstack_paid = models.BooleanField(default=False)
    blockchain_paid = models.BooleanField(default=False)
    business_paid = models.BooleanField(default=False)
    digital_marketing_paid = models.BooleanField(default=False)
    js_level = models.IntegerField(default=1, null=False)
    python_level = models.IntegerField(default=1, null=False)
    fullstack_level = models.IntegerField(default=1, null=False)
    blockchain_level = models.IntegerField(default=1, null=False)
    business_level = models.IntegerField(default=1, null=False)
    
    def __str__(self):
        return ('User: {} \n email: {}'.format(self.full_name, self.email))

    # interest = models.ManyToManyField(Customuser, blank=True)


class Technews(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    content = models.TextField() 
    image_url = models.CharField(max_length = 255, blank= True)

    def __str__(self):
        return ('Id: {} : Title: {}'.format(self.id, self.title))

class Learn_Js(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='video_img', validators=[image_validator])
    video = models.FileField(blank = True, null=True, upload_to='course_video')
    duration = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length= 1000, null=True, blank=True, default="No description stated yet...")
    toc = RichTextField(blank=True, null=True)
    overview = RichTextField(blank=True, null=True)
    task_and_projects = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    test_available = models.BooleanField(default=False)
    json_file = models.FileField(blank = True, null=True, upload_to='json_file')
    
    
    def __str__(self):
        return ('Video Id: {} : Title: {}'.format(self.id, self.title))
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (400, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)

class Html_And_Css(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    description = models.CharField(max_length= 1000, null=True, blank=True, default="No description stated yet...")
    toc = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='video_img', validators=[image_validator])
    video = models.FileField(blank = True, null=True, upload_to='course_video')
    duration = models.CharField(max_length=10, blank=True)
    overview = RichTextField(blank=True, null=True)
    task_and_projects = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    test_available = models.BooleanField(default=False)
    json_file = models.FileField(blank = True, null=True, upload_to='json_file')
    
    
    def __str__(self):
        return ('Video Id: {} : Title: {}'.format(self.id, self.title))
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (400, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)

class Learn_Python(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    description = models.CharField(max_length= 1000, blank=True, default="No description stated yet...")
    toc = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='video_img', validators=[image_validator])
    video = models.FileField(blank = True, null=True, upload_to='course_video')
    duration = models.CharField(max_length=10, blank=True)
    duration = models.CharField(max_length=10, blank=True)
    overview = RichTextField(blank=True, null=True)
    task_and_projects = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    test_available = models.BooleanField(default=False)
    json_file = models.FileField(blank = True, null=True, upload_to='json_file')

    def __str__(self):
        return ('Video Id: {} : Title: {}'.format(self.id, self.title))
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (400, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)
    

class Learn_Fullstack(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    description = models.CharField(max_length= 1000, null=True, blank=True, default="No description stated yet...")
    toc = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='video_img', validators=[image_validator])
    video = models.FileField(blank = True, null=True, upload_to='course_video')
    duration = models.CharField(max_length=10, blank=True)
    overview = RichTextField(blank=True, null=True)
    task_and_projects = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    test_available = models.BooleanField(default=False)
    json_file = models.FileField(blank = True, null=True, upload_to='json_file')
    
    
    def __str__(self):
        return ('Video Id: {} : Title: {}'.format(self.id, self.title))
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (400, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)



class Learn_Blockchain(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    description = models.CharField(max_length= 1000, blank=True, default="No description stated yet...")
    toc = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='video_img', validators=[image_validator])
    video = models.FileField(blank = True, null=True, upload_to='course_video')
    duration = models.CharField(max_length=10, blank=True)
    duration = models.CharField(max_length=10, blank=True)
    overview = RichTextField(blank=True, null=True)
    task_and_projects = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    test_available = models.BooleanField(default=False)
    json_file = models.FileField(blank = True, null=True, upload_to='json_file')

    def __str__(self):
        return ('Video Id: {} : Title: {}'.format(self.id, self.title))
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (400, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)

class Learn_Techbusiness(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    description = models.CharField(max_length= 1000, blank=True, default="No description stated yet...")
    toc = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='video_img', validators=[image_validator])
    video = models.FileField(blank = True, null=True, upload_to='course_video')
    duration = models.CharField(max_length=10, blank=True)
    duration = models.CharField(max_length=10, blank=True)
    overview = RichTextField(blank=True, null=True)
    task_and_projects = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    test_available = models.BooleanField(default=False)
    json_file = models.FileField(blank = True, null=True, upload_to='json_file')

    def __str__(self):
        return ('Video Id: {} : Title: {}'.format(self.id, self.title))
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (400, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)



class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=125)
    author = ForeignKey(Customuser, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='post_pics', validators=[image_validator])

    def __str__(self):
        return ('Post: {}, by: {}'.format(self.title, self.author))

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 800 or img.width > 800:
            output_size = (700, 700)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Payment(models.Model):    
    customer = ForeignKey(Customuser, on_delete=models.CASCADE)
    customers_email = models.EmailField(max_length=100, blank=False)
    customers_phone = models.CharField(max_length=11, blank=False)
    product_type = models.CharField(max_length=100, choices=plan_type, blank=False)
    amount = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default=False)
    reference = models.CharField(max_length=100, default='')
    date_created = models.DateTimeField(default=timezone.now)
    # expiry_date = models.DateField(default=timezone.now)