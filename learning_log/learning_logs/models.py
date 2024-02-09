from django.db import models # import the module models from django.db , this module will help us define the data we want to manage in our app.

class Topic(models.Model): # a model is a class .created a class called Topic that inherits from Model a parent class included in django that defines a model basic functionality.
    """A topic the user is learning about """ # we add two attributes to the Topic class text and date_added
    text = models.CharField(max_length=200) # text is an attribute that will hold the character of the topic. charfield made up of characters or text. we use charfield when we want to store small amount of text eg name, title, city.which 200 characters length.
    date_added = models.DateTimeField(auto_now_add = True) # date_added is an attribute that will hold the date and time the topic was created. we pass the argument auto_now_add = True to tell django to automatically set this attribute to the current date and time whenever the user creates a new topic.

    def __str__(self): # tells django how you want it to represent an instance of the model . we write a method called __str__() that returns the string stored in the text attribute.
        """Return a string representation of the model."""
        return self.text # returns the value of the text attribute when we call __str__() method.

