from django.contrib import admin #importing the admin module from django.contrib
from .models import Topic , Entry #importing the Topic model from the models module in the same directory

admin.site.register(Topic) #registering the Topic model with the admin site. manage our model through the admin site.
admin.site.register(Entry) #registering the Entry model with the admin site. manage our model through the admin site.
