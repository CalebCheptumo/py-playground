# Python dictionaries allow you to connect pieces of related information.
# Each piece of information in a dictionary is stored as a key-value pair.
# When you provide a key, Python returns the value associated with that key.
# You can loop through all the key-value pairs, all the keys, or all the values.
# You can also store dictionaries inside lists, lists inside dictionaries, or even dictionaries inside other dictionaries.

# A simple dictionary
# the dictionary alien_o stores the alien's color and points.
alien_0 = {'color': 'blue', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# the dictionary user stores the user's username, first name, and last name.
user = {'username': 'caleb', 'first': 'caleb', 'last': 'cheptumo'}
print(f"User's fullname is {user['first'].title()} {user['last'].title()}")
