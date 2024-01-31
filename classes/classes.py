#classes combine functions and data into one neat package that can be used in flexible and efficient ways.
#object oriented programming - OOP - is a way of organizing code so that it is easy to reuse and easy to build upon.
#classes are a way of organizing information and actions into reusable blueprints.
#objects are instances of classes.
#when  you create individual objects from the class, each object is automatically set up with its own data.
#making an object from a class is called instantiation, and you work with instances of a class.
#A class is a code template for creating objects. Objects have member variables and have behavior associated with them. 
#In Python, a class is created by the keyword class



#creating and using a class
#you can model almost anything using classes.

#creating the dog class
#each instance created from the dog class will store a name and an age, and we'll give each dog the ability to sit() and roll_over()

class Dog: #define a class called Dog that inherits from the base class object, by convention, capitalized names refer to classes in Python. no parentheses in the class definition because we're creating this class from scratch.
    """A simple attempt to model a dog""" #docstring - describes what this class does. docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the classes in your programs.

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting. ")

    def roll_over(self):
        """Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over!")
