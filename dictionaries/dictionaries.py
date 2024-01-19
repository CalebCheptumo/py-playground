# Python dictionaries allow you to connect pieces of related information.
# Each piece of information in a dictionary is stored as a key-value pair.
# When you provide a key, Python returns the value associated with that key.
# You can loop through all the key-value pairs, all the keys, or all the values.
# You can also store dictionaries inside lists, lists inside dictionaries, or even dictionaries inside other dictionaries.
# Key value pairs are separated by commas.
# A colon separates each key from its associated value.
# You can access the value associated with a key by passing the key name to the dictionary.
# You can use as many key-value pairs as you want in a dictionary.
# key value can be a number, string, list, or even another dictionary.
# A dictionary can be wrapped in braces {}, with a series of key-value pairs inside the braces, or it can be empty {}.
# A simple dictionary
# the dictionary alien_o stores the alien's color and points.
# syntax: dictionary_name = {'key': 'value', 'key': 'value'}
alien_0 = {'color': 'blue', 'points': 5}
print(alien_0['color'])  # Output: blue
print(alien_0['points'])  # Output: 5

# the dictionary user stores the user's username, first name, and last name.
user = {'username': 'caleb', 'first': 'caleb', 'last': 'cheptumo'}
full_name = f"{user['first']} {user['last']}"
print(f"Hello, {full_name.title()}!")  # Output: Hello, Caleb Cheptumo!
# once the user dictionary has been defined, we can pull the values associated with the keys 'username', 'first', and 'last'from the dictionary. Then this value is assigned to variable full_name.

# Access a key that doesn't exist, you'll get an error.( KeyError)
# Use get method which returns None instead of KeyError.

print(user.get('age'))  # Output: None


# Adding New Key-Value Pairs
# dictionaries are dynamic structures , you can add new key-value pairs to a dictionary at any time.
# syntax: dictionary_name['new_key'] = 'new_value'
alien_0 = {'color': 'blue', 'points': 5}
print(alien_0)  # Output: {'color': 'blue', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# Output: {'color': 'blue', 'points': 5, 'x_position': 0, 'y_position': 25}
print(alien_0)

# dictionaries retain their original order. When you print a dictionary or loop through its elements, you will see the elements in the same order in which they were added to the dictionary.
# Starting with an empty dictionary

person = {}
person['name'] = 'caleb'
person['age'] = 25
person['city'] = 'Nakuru'
print(person)  # Output: {'name': 'caleb', 'age': 25, 'city': 'Nakuru'}

# dictionary keys must be immutable - you can use integer,floats, strings, numbers, or tuples as dictionary keys but something like a list can't be used as a dictionary key.

# Modifying Values in a Dictionary
# assigning new value to a existing key
# syntax: dictionary_name['key'] = 'new_value'

person = {'name': 'caleb', 'age': 25, 'city': 'Nakuru'}
print(person)  # Output: {'name': 'caleb', 'age': 25, 'city': 'Nakuru'}
person['age'] = 26
print(person)  # Output: {'name': 'caleb', 'age': 26, 'city': 'Nakuru'}

# alien example - tracking position of alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs -  using del keyword statement
# syntax: del dictionary_name['key']
# del keyword removes the key-value pair permanently.
user = {'username': 'caleb', 'first': 'caleb', 'last': 'cheptumo'}
# Output: {'username': 'caleb', 'first': 'caleb', 'last': 'cheptumo'}
print(user)
del user['username']
print(user)  # Output: {'first': 'caleb', 'last': 'cheptumo'}


# A Dictionary of Similar Objects
# Dictionary is useful the results of a simple poll, where each response is stored as a value associated with a particular person.
# syntax: dictionary_name = {'key': 'value', 'key': 'value'}
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
# Output: {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

# looping through a dictionary
# syntax: for key, value in dictionary_name.items():
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

for key, value in my_dict.items():
    print(f"{key} : {value}")

# using keys() method to loop through all the keys in dictionary
# syntax: for key in dictionary_name.keys():
# useful when you don't need to work with all of the values in a dictionary.
# using keys() method to loop through all the keys in dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(name.title())


cars = {
    'Mustang': 'Ford',
    'Civic': 'Honda',
    'Camry': 'Toyota'
}

for model in cars.keys():
    print(model.title())

for model in cars.keys():  # 'model' will be 'Mustang', then 'Civic', then 'Camry'
    # 'cars[model]' gets the value associated with the current key
    print(f"The {model} is made by {cars[model]}")


# looping in a particular order
# use sorted() function to get a copy of the keys in order.
# syntax: for key in sorted(dictionary_name.keys()):
# sorted() sorts the keys temporarily, in alphabetical order.
# The original order of the keys remains intact in the dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    print(
        f"{name.title()} favorite language is {favorite_languages[name].title()}.")


# looping through all values in a dictionary - values() method
# syntax: for value in dictionary_name.values():
# returns a list of values without any keys.
# it doesn't provide a way to get the corresponding key for any value.
# it doesn't check for duplicates.

cars = {
    'Mustang': 'Ford',
    'Civic': 'Honda',
    'Camry': 'Toyota'
}
for manufacturer in cars.values():
    print(manufacturer.title())

# using set() function to remove duplicates
# syntax: for value in set(dictionary_name.values()):
# set() function returns a list of unique items.
# similar to list or tuple except that each item in the set must be unique.
# sets are also unordered meaning that they dont have index positions.

cars = {'Mustang', 'Civic', 'Camry'}
print(cars)

# creating a set from a list
# syntax: set(list_name)
car_list = ['Ford', 'Civic', 'Camry']
car_set = set(car_list)
print(car_set)


# Nesting - storing a set of dictionaries in a list or a list of items as a value in a dictionary.
# A list of dictionaries
# syntax: list_name = [{dictionary_1}, {dictionary_2}, {dictionary_3}]
alien_0 = {'color': 'blue', 'points': 5}
alien_1 = {'color': 'green', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}
aliens = [alien_0, alien_1, alien_2]    # list of dictionaries
for alien in aliens:
    print(alien)


# empty list to store aliens
aliens = []  # empty list
# make 30 green aliens
# range() function returns a series of numbers starting at 0 and ending at 29.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # append() method adds each new alien to the list aliens.
    aliens.append(new_alien)
# show the first 5 aliens
for alien in aliens[:5]:  # slice the first 5 aliens
    print(alien)
# show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


# use for loop and if statement o change color of aliens.

# empty list to store aliens
aliens = []  # empty list
# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)


# A list in a dictionary
# syntax: dictionary_name = {'key': [list_items]}
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(
    f" you ordered a {pizza['crust']} - crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"{topping}")


# Another example
employees = {
    'caleb': ['Python', 'Java', 'C++'],
    'mary': ['C#', 'Java', 'Python'],
    'jane': ['C++', 'Python', 'C#']
}

# prints all the languages that caleb knows
print(employees['caleb'])  # Output: ['Python', 'Java', 'C++']

employees['caleb'].append('C#')

print(employees['caleb']) # Output: ['Python', 'Java', 'C++', 'C#']
