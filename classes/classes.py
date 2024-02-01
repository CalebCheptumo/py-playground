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

# setting a default value for an attribute
#when an instance is created, attributes can be defined without being passed in as parameters. these attributes can be defined in the __init__() method, where they are assigned a default value.

class Car:
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year): #__init__() method takes in parameters to create an instance representing a particular car. when we make a new car, we'll need to specify a make, model, and year for it.
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value for an attribute

    def get_descriptive_name(self): # define a method called get_descriptive_name() that puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self): #define a method called read_odometer() that lets us read the odometer
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it. ")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have
my_new_car.read_odometer() #call read_odometer() method to see the car's mileage


#modifying attribute values
#we can change the value in three ways:
#1. change the value directly through an instance
#2. set the value through a method
#3. increment the value (add a certain amount to it) through a method

#1. changing the value directly
#setting the odometer_reading attribute's value to 23 directly through the instance

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have
my_new_car.odometer_reading = 23 #setting the odometer_reading attribute's value to 23 directly through the instance. this line tells python to take the instance my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23. we use dot notation to access the attribute odometer_reading and then assign a new value to that attribute.
my_new_car.read_odometer() #call read_odometer() method to see the car's mileage


#2. modifying an attribute's value through a method
#instead of accessing the attribute directly, we pass the new value to a method that handles the updating internally.

class Car:
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year): #__init__() method takes in parameters to create an instance representing a particular car. when we make a new car, we'll need to specify a make, model, and year for it.
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value for an attribute

    def get_descriptive_name(self): # define a method called get_descriptive_name() that puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self): #define a method called read_odometer() that lets us read the odometer
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it. ")

    def update_odometer(self, mileage): #define a method called update_odometer() that lets us update the odometer reading
        """Set the odometer reading to the given value. """
        self.odometer_reading = mileage #take in a mileage parameter and set the odometer_reading attribute to that value

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have

my_new_car.update_odometer(23) #call update_odometer() method and give it 23 as the argument
my_new_car.read_odometer() #call read_odometer() method to see the car's mileage


#extending update_odometer() method to do additional work every time the odometer reading is modified

class Car:
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year): #__init__() method takes in parameters to create an instance representing a particular car. when we make a new car, we'll need to specify a make, model, and year for it.
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value for an attribute

    def get_descriptive_name(self): # define a method called get_descriptive_name() that puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self): #define a method called read_odometer() that lets us read the odometer
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it. ")

    def update_odometer(self, mileage): #define a method called update_odometer() that lets us update the odometer reading
        """Set the odometer reading to the given value. """
        if mileage >= self.odometer_reading: #add a conditional test that makes sure no one tries to roll back the odometer reading
            self.odometer_reading = mileage #take in a mileage parameter and set the odometer_reading attribute to that value
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have

my_new_car.update_odometer(23) #call update_odometer() method and give it 23 as the argument
my_new_car.read_odometer() #call read_odometer() method to see the car's mileage

my_new_car.update_odometer(20) #call update_odometer() method and give it 20 as the argument



#3. incrementing an attribute's value through a method
#incrementing an attribute's value by certain amount rather than set an entirely new value.

class Car:
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year): #__init__() method takes in parameters to create an instance representing a particular car. when we make a new car, we'll need to specify a make, model, and year for it.
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value for an attribute

    def get_descriptive_name(self): # define a method called get_descriptive_name() that puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self): #define a method called read_odometer() that lets us read the odometer
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it. ")

    def update_odometer(self, mileage): #define a method called update_odometer() that lets us update the odometer reading
        """Set the odometer reading to the given value. """
        if mileage >= self.odometer_reading: #add a conditional test that makes sure no one tries to roll back the odometer reading
            self.odometer_reading = mileage #take in a mileage parameter and set the odometer_reading attribute to that value
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): #define a method called increment_odometer() that lets us add a given amount to the odometer reading. takes in a number of miles and adds this value to self.odometer_reading
        """Add the given amount to the odometer reading. """
        self.odometer_reading += miles #add whatever value we specify to the odometer reading

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have

my_used_car.update_odometer(23_500) #call update_odometer() method and give it 23_500 as the argument . we use an underscore when working with larger numbers to make them easier to read
my_used_car.read_odometer() #call read_odometer() method to see the car's mileage

my_used_car.increment_odometer(100) #call increment_odometer() method and give it 100 as the argument
my_used_car.read_odometer() #call read_odometer() method to see the car's mileage

#you can also modify to reject negative increments so no one uses this function to roll back an odometer



#inheritance
#inheritance is a way to form new classes using classes that have already been defined.
#original class is called parent class, and the new class is the child class.
#child class inherits the attributes and methods from its parent class, but it can also define new attributes and methods of its own.
#syntax: class ChildClass(ParentClass): #define the child class with its parent class in parentheses.
#the __init__() method for a child class
#__init__() method initializes any attributes that were defined in the parent __init__() method.


class ElectricCar(Car): # name of the parent class must be included in parentheses in the definition of the child class. the __init__() method takes in the information required to make a Car instance.
    """Represents aspect of a car, specific to electric vehicles"""

    def __init__(self, make, model, year): #initialize attributes of the parent class. takes in the information required to make a Car instance.
        """Initialize attributes of the parent class. """
        super().__init__(make, model, year) #super() function is a special function that helps python make connections between the parent and child class. this line tells python to call the __init__() method from ElectricCar's parent class, which gives an ElectricCar instance all the attributes of its parent class. the name super comes from a convention of calling the parent class a superclass and the child class a subclass.


my_leaf = ElectricCar('nissan', 'leaf', 2024) #make instance from the child class ElectricCar and store/assign to/ it in my_leaf
print(my_leaf.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have  


#defining attributes and methods for the child class
#you can as well add new attributes and methods to the child class that are not part of the parent class.
#add specific attributes and methods to the child class that are not appropriate for the parent class.

class ElectricCar(Car): # name of the parent class must be included in parentheses in the definition of the child class. the __init__() method takes in the information required to make a Car instance.
    """Represents aspect of a car, specific to electric vehicles"""

    def __init__(self, make, model, year): #initialize attributes of the parent class. takes in the information required to make a Car instance.
        """Initialize attributes of the parent class.
         Then initialize attributes specific to an electric car. """
        super().__init__(make, model, year) #super() function is a special function that helps python make connections between the parent and child class. this line tells python to call the __init__() method from ElectricCar's parent class, which gives an ElectricCar instance all the attributes of its parent class. the name super comes from a convention of calling the parent class a superclass and the child class a subclass.
        self.battery_size = 75 #add an attribute called battery_size and set its initial value to 75 . will only be associated with subclasses like ElectricCar but not with its parent class Car.

    def describe_battery(self): #add a method called describe_battery() that prints information about the battery
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery. ")


my_leaf = ElectricCar('nissan', 'leaf', 2024) #make instance from the child class ElectricCar and store/assign to/ it in my_leaf
print(my_leaf.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have
my_leaf.describe_battery() #call describe_battery() method to see the battery size



#overriding methods from the parent class
#you can override any method from the parent class that doesn't fit what you're trying to model with the child class.
#to do this, you define a method in the child class with the same name as the method you want to override in the parent class.


class ElectricCar(Car): # name of the parent class must be included in parentheses in the definition of the child class. the __init__() method takes in the information required to make a Car instance.
    """Represents aspect of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year): #initialize attributes of the parent class. takes in the information required to make a Car instance.
        """Initialize attributes of the parent class.
         Then initialize attributes specific to an electric car. """
        super().__init__(make, model, year) #super() function is a special function that helps python make connections between the parent and child class. this line tells python to call the __init__() method from ElectricCar's parent class, which gives an ElectricCar instance all the attributes of its parent class. the name super comes from a convention of calling the parent class a superclass and the child class a subclass.
        self.battery_size = 75 #add an attribute called battery_size and set its initial value to 75 . will only be associated with subclasses like ElectricCar but not with its parent class Car.

    def describe_battery(self): #add a method called describe_battery() that prints information about the battery
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery. ")

    def fill_gas_tank(self): #add a method called fill_gas_tank() that's specific to car but doesn't apply to electric cars
        """Electric cars don't have gas tanks. """
        print("This car doesn't need a gas tank! ")





#instances as attributes
#you can break your large class into smaller classes that work together. This approach is called composition.
        
class Car:
    """A simple attempt to represent a car. """

    def __init__(self, make, model, year): #__init__() method takes in parameters to create an instance representing a particular car. when we make a new car, we'll need to specify a make, model, and year for it.
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value for an attribute

    def get_descriptive_name(self): # define a method called get_descriptive_name() that puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self): #define a method called read_odometer() that lets us read the odometer
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it. ")

    def update_odometer(self, mileage): #define a method called update_odometer() that lets us update the odometer reading
        """Set the odometer reading to the given value. """
        if mileage >= self.odometer_reading: #add a conditional test that makes sure no one tries to roll back the odometer reading
            self.odometer_reading = mileage #take in a mileage parameter and set the odometer_reading attribute to that value
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): #define a method called increment_odometer() that lets us add a given amount to the odometer reading. takes in a number of miles and adds this value to self.odometer_reading
        """Add the given amount to the odometer reading. """
        self.odometer_reading += miles #add whatever value we specify to the odometer reading

class Battery: #new class called Battery that doesn't inherit from any other class
    """A simple attempt to model a battery for an electric car. """

    def __init__(self, battery_size=75): #initialize the battery's attributes. the __init__() method has one parameter, battery_size, in addition to self. this parameter has a default value of 75 if no value is provided.
        """Initialize the battery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self): #add a method called describe_battery() that prints information about the battery size
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery. ")

    def get_range(self): #add a method called get_range() that prints a statement about the range this battery provides
        """Print a statement about the range this battery provides. """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge. ")

  
class ElectricCar(Car): # name of the parent class must be included in parentheses in the definition of the child class. the __init__() method takes in the information required to make a Car instance.
    """Represents aspect of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year): #initialize attributes of the parent class. takes in the information required to make a Car instance.
        """Initialize attributes of the parent class.
         Then initialize attributes specific to an electric car. """
        super().__init__(make, model, year) #super() function is a special function that helps python make connections between the parent and child class. this line tells python to call the __init__() method from ElectricCar's parent class, which gives an ElectricCar instance all the attributes of its parent class. the name super comes from a convention of calling the parent class a superclass and the child class a subclass.
        self.battery = Battery() #add an attribute called battery and set its initial value to an instance of Battery. when the __init__() method runs, it stores a Battery instance in the attribute self.battery. this will happen every time the __init__() method is called; any ElectricCar instance will now have a Battery instance created automatically.

  
my_tesla = ElectricCar('tesla', 'model s', 2024) #make instance from the child class ElectricCar and store/assign to/ it in my_tesla
print(my_tesla.get_descriptive_name()) #call get_descriptive_name() method  to see what kind of car we have
my_tesla.battery.describe_battery() #call describe_battery() method to see the battery size
my_tesla.battery.get_range() #call get_range() method to see the range of the battery



#modeling real-world objects -
#Real-world objects can be much more complex, with many more attributes and methods, and relationships with other objects. But the basic process of identifying objects, defining classes, defining attributes and methods, creating instances, and using the objects remains the same.




#Importing classes
#python lets you store classes in modules and then import the classes you need into your main program.


#importing a single class
#store the class in a module, then import the module into your main program.