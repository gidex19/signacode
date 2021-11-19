from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image
from .validators import image_validator

# Create your models here.
class Customuser(AbstractUser):
    full_name = models.CharField(max_length = 35, blank= True)
    phone_number = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length = 100, blank= True)
    

    def __str__(self):
        return ('User: {} \n email: {}'.format(self.full_name, self.email))
class Technews(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    content = models.TextField() 
    image_url = models.CharField(max_length = 255, blank= True)

    def __str__(self):
        return ('Id: {} : Title: {}'.format(self.id, self.title))

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
    