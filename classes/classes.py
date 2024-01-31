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


#the __init__() method
#a function that is part of a class is a method.
##concept in function apply in class
#the __init__() method is  a special method that python runs automatically whenever we create a new instance based on the Dog class
##__init__() has leading and trailing double underscores, a convention that helps prevent Python's default method names from conflicting with your method names.
#in our case we defined the __init__() to have three parameters : self,name and age
#self parameter is required in the method definition and must come first before the other parameters.
#self must be included in the definition  because when python calls this method later (to create instance of Dog) the method call will automatically pass the self argument.
#every method call associated with a class automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.
#when we make an instance of Dog, python will call the __init__() method from the Dog class. we'll pass Dog() a name and an age as arguments; self is passed automatically, so we don't need to pass it. whenever we want to make an instance from the Dog class, we'll provide values for only the last two parameters, name and age.
#two variables defined in the __init__() method have the prefix self. any variable prefixed with self is available to every method in the class, and we'll also be able to access these variables through any instance created from the class.
#self.name = names takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance being created. the same process happens with self.age = age. variables that are accessible through instances like this are called attributes.
#Dog class has two other methods defined: sit() and roll_over(). because these methods don't need additional information like a name or age, we just define them to have one parameter, self. the instances we create later will have access to these methods.
#sit() and roll_over() have print() call that output text to the screen. there are no other actions associated with sit() and roll_over() for now, but they could do just about anything you tell them to.
        



#making an instance from a class
#think of a class as a set of instructions for how to make an instance. the class Dog is a set of instructions that tells python how to make individual instances representing specific dogs.
        

class Dog:
    """A simple attempt to model a dog"""

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
#we tell python to create a dog whose name is 'simba' and whose age is 4. when python reads this line, it calls the __init__() method in Dog with the arguments 'simba' and 4. the __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided. the __init__() method has no explicit return statement, but python automatically returns an instance representing this dog. we assign that instance to the variable my_dog. the naming convention is helpful here: we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.
my_dog = Dog('simba', 4) #we create an instance of dog and store it in my_dog
print(f"My dog's name is {my_dog.name} .")
print(f"My dog is {my_dog.age} years old. ")




#accessing attributes
#use dot notation to access the attributes of an instance.
#syntax: instance_name.attribute_name
my_dog.name #access the value of my_dog's attribute name by writing: my_dog.name
#same approach as self.name / self.age in the class definition



#calling methods
#after we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
#syntax: instance_name.method_name()

my_dog = Dog('simba', 4) #we create an instance of dog and store it in my_dog
my_dog.sit() #call sit() method
my_dog.roll_over() #call roll_over() method


#creating multiple instances
#we can create as many instances from one class as we need, as long as we give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

my_dog = Dog('simba', 4) #we create an instance of dog and store it in my_dog
your_dog = Dog('lucy', 3) #we create an instance of dog and store it in your_dog

print(f"My dog's name is {my_dog.name} .")
print(f"My dog is {my_dog.age} years old. ")
my_dog.sit() #call sit() method for my_dog instance of Dog class 

print(f"\nYour dog's name is {your_dog.name} .")
print(f"Your dog is {your_dog.age} years old. ")
your_dog.sit()



#working with classes and instances
#you can use classes to represent many real-world situations.
#You can modify the attributes of an instance directly or write methods that update attributes in specific ways.


#the car class
class Car:
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year): #__init__() method takes in parameters to create an instance representing a particular car. when we make a new car, we'll need to specify a make, model, and year for it.
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self): # define a method called get_descriptive_name() that puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have