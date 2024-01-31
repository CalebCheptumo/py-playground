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