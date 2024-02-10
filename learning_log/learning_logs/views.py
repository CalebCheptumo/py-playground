from django.shortcuts import render #import the render() function from django.shortcuts module which renders the response based on the data provided by views


def index(request): #define a function called index that takes in a request object. the request object is required by django for all views.
    """The homepage for learning log"""
    return render(request, 'learning_log/index.html') #call the render() function with two arguments: the original request object and a template it can use to build the page. 
