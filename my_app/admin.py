from django.contrib import admin
from .models import Customuser, Post, Technews, Learn_Js, Learn_Python, Interest, Payment
# Register your models here.
admin.site.register(Customuser)
admin.site.register(Post)
admin.site.register(Technews)
admin.site.register(Learn_Js)
admin.site.register(Learn_Python)
admin.site.register(Interest)
admin.site.register(Payment)
