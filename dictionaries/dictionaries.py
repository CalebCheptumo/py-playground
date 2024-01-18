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
alien_0 = {'color': 'blue', 'points': 5}
print(alien_0['color'])  # Output: blue
print(alien_0['points'])  # Output: 5

# the dictionary user stores the user's username, first name, and last name.
user = {'username': 'caleb', 'first': 'caleb', 'last': 'cheptumo'}
full_name = f"{user['first']} {user['last']}"
print(f"Hello, {full_name.title()}!")  # Output: Hello, Caleb Cheptumo!
# once the user dictionary has been defined, we can pull the values associated with the keys 'username', 'first', and 'last'from the dictionary. Then this value is assigned to variable full_name.

# Adding New Key-Value Pairs
