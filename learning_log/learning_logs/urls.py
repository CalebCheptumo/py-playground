"""Defines URL patterns for learning_logs."""

from django.urls import path #import the path function from django.urls module which is needed to map URLs to views.
from . import views #import the views module from the same directory

app_name = 'learning_logs' #variable app_name is set to 'learning_logs' tells django to distinguish this urls.py file from urls.py files of the same name in other apps within the project.
urlpatterns = [
    # Home page
    path('', views.index, name='index'), #the path function takes three arguments: a string that helps django route the request to the appropriate view, the view that will manage the request, and a unique name we can use to refer to this URL pattern. django calls index() function from views.py file whenever the URL requested matches the pattern defined in the first argument. the name='index' helps us refer to this URL pattern in other code sections of the project.
]