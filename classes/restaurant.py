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

