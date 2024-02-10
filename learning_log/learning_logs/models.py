from django.db import models # import the module models from django.db , this module will help us define the data we want to manage in our app.

class Topic(models.Model): # a model is a class .created a class called Topic that inherits from Model a parent class included in django that defines a model basic functionality.
    """A topic the user is learning about """ # we add two attributes to the Topic class text and date_added
    text = models.CharField(max_length=200) # text is an attribute that will hold the character of the topic. charfield made up of characters or text. we use charfield when we want to store small amount of text eg name, title, city.which 200 characters length.
    date_added = models.DateTimeField(auto_now_add = True) # date_added is an attribute that will hold the date and time the topic was created. we pass the argument auto_now_add = True to tell django to automatically set this attribute to the current date and time whenever the user creates a new topic.

    def __str__(self): # tells django how you want it to represent an instance of the model . we write a method called __str__() that returns the string stored in the text attribute.
        """Return a string representation of the model."""
        return self.text # returns the value of the text attribute when we call __str__() method.


class Entry(models.Model):  # the Entry class/model inherits from django base model class
    """Something specific learned about a topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # is a ForeignKey instance. foreign key is a database term it  reference to another record in the database, it connects each entry to a specific topic. on_delete=models.CASCADE tells django that when a topic is deleted, all the entries associated with that topic should be deleted as well. its known as cascading delete.
    text = models.TextField() # text is an attribute that will hold the text of the entry. textfield is for long pieces of text, such as a body of an entry or a comment.
    date_added = models.DateTimeField(auto_now_add=True) # date_added is an attribute that will hold the date and time the entry was created. we pass the argument auto_now_add=True to tell django to automatically set this attribute to the current date and time whenever the user creates a new entry.

    class Meta: # nested class inside Entry class to hold extra information for managing a model. it lets us set a special attribute telling django to use Entries when it needs to refer to more than one entry. without this django would refer to multiple entries as Entrys.
        verbose_name_plural = 'entries'

    def __str__(self): # tells django how to represent the model in text format.
        """Return a simple string representing the entry"""
        return f"{self.text[:50]}..." # returns the first 50 characters of the text attribute, followed by an ellipsis, unless the entry is less than 50 characters long.