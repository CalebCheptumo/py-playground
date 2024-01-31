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

