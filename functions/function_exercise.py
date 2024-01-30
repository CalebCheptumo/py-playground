#message

def display_message():
    """Display a simple message"""
    print("I am learning about functions in python")

display_message()


#favorite book

def favorite_book(title):
    """Display a message about someone's favorite book"""
    print(f"My favorite book is {title.title()}")

favorite_book('alice in wonderland')



#t-shirt
def make_shirt(size, message):
    """Display a message about the size of the shirt and the message printed on it"""
    print(f"The size of the shirt is {size} and the message printed on it is {message}")

make_shirt('large', 'hello world') #positional arguments
make_shirt(size='large', message='hello world') #keyword arguments


#large shirts
def make_shirt(size='large', message='I love Python'):
    """Display a message about the size of the shirt and the message printed on it"""
    print(f"The size of the shirt is {size} and the message printed on it is {message}")

make_shirt()



#cities

def describe_city(city, country='Kenya'):
    """Display a message about a city and the country it is in"""
    print(f"{city.title()} is in {country.title()}")


describe_city('nairobi')
describe_city('mombasa')
describe_city('kampala', 'uganda')