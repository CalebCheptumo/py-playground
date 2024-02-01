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
