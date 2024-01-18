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
