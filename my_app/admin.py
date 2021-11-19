from django.contrib import admin
from .models import Customuser, Post, Technews
# Register your models here.
admin.site.register(Customuser)
admin.site.register(Post)
admin.site.register(Technews)