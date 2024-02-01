#restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The restaurant's name is {self.restaurant_name.title()} .")
        print(f"The restaurant's cuisine type is {self.cuisine_type.title()} .")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name.title()} is now open. ")

restaurant = Restaurant('kfc', 'fast food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

#call describe_restaurant() and open_restaurant() methods
restaurant.describe_restaurant()
restaurant.open_restaurant()


#three restaurants
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The restaurant's name is {self.restaurant_name.title()} .")
        print(f"The restaurant's cuisine type is {self.cuisine_type.title()} .")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name.title()} is now open. ")
#three instances
restaurant1 = Restaurant('kfc', 'fast food')
restaurant2 = Restaurant('cjs', 'tea')
restaurant3 = Restaurant('dominos', 'pizza')

#Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


#users
class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        """Describe the user"""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()} .")
        print(f"The user's age is {self.age} .")
        print(f"The user's location is {self.location.title()} .")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()} .")


user1 = User('john', 'smith', 20, 'nairobi')
user2 = User('jane', 'doe', 25, 'nakuru')
user3 = User('james', 'bond', 30, 'mombasa')


user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()


#number served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The restaurant's name is {self.restaurant_name.title()} .")
        print(f"The restaurant's cuisine type is {self.cuisine_type.title()} .")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name.title()} is now open. ")

    def set_number_served(self, number_served):
        """Set the number of customers served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increment the number of customers served"""
        self.number_served += additional_served

restaurant = Restaurant('kfc', 'fast food')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(30)
print(restaurant.number_served)


#login attempts
class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe the user"""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()} .")
        print(f"The user's age is {self.age} .")
        print(f"The user's location is {self.location.title()} .")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()} .")

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0

user1 = User('John', 'Doe', 30, 'New York')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)


#ice cream stand
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

ice_cream_stand = IceCreamStand('kfc', 'fast food')
ice_cream_stand.flavors = ['vanilla', 'chocolate', 'strawberry']

ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()


#admin
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


admin = Admin('John', 'Doe', 30, 'New York')
admin.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

admin.describe_user()
admin.show_privileges()


#privileges
class Privileges:
    def __init__(self, privileges=[]):
        """Initialize the privileges attribute"""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has"""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.title()}")
        else:
            print("- This user has no privileges.")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

admin = Admin('John', 'Doe', 30, 'New York')
admin.privileges.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

admin.privileges.show_privileges()



#battery upgrade


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""

        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""

        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""

        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""

        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.descriptive_name())

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()




    