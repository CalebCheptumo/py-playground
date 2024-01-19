# person
person = {'first_name': 'John', 'last_name': 'Doe',
          'age': 30, 'city': 'Maldives'}
first_name = person['first_name']
last_name = person['last_name']
age = person['age']
city = person['city']
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Age: {age}")
print(f"City: {city}")


# Favorite number
favorite_numbers = {
    'caleb': 9,
    'jane': 7,
    'james': 3,
    'josh': 5,
    'jacob': 2
}

caleb = favorite_numbers['caleb']
jane = favorite_numbers['jane']
james = favorite_numbers['james']
josh = favorite_numbers['josh']
jacob = favorite_numbers['jacob']

print(f"Caleb's favorite number is {caleb}")
print(f"Jane's favorite number is {jane}")
print(f"James's favorite number is {james}")
print(f"Josh's favorite number is {josh}")
print(f"Jacob's favorite number is {jacob}")


# using loop
# items() method returns a list of key-value pairs and to iterate through the returned list, we use for loop.
for name, number in favorite_numbers.items():
    print(f"{name.title()} 's favorite number is {number}")


# Glossary
# A glossary is a dictionary that contains key-value pairs that describe a word or phrase.
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")


# Rivers
rivers = {
    'turkana': 'kenya',
    'ewaso': 'kenya',
    'tana': 'kenya',
}
for river in rivers.keys():
    print(f"The {river.title()} river runs through {rivers[river].title()}")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())


# Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

pollsters = ['jen', 'sarah', 'edward', 'phil', 'james', 'jacob', 'josh']
for pollster in pollsters:
    if pollster in favorite_languages.keys():
        print(f"{pollster.title()}, thank you for taking the poll.")
    else:
        print(f"{pollster.title()}, please take the poll.")


# People
# dictionary  person_1 that stores information about a person .
person_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'Maldives'
}
person_2 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Maldives'
}

person_3 = {
    'first_name': 'James',
    'last_name': 'Doe',
    'age': 20,
    'city': 'Maldives'
}

# list people that contains dictionaries
people = [person_1, person_2, person_3]

for person in people:  # loop through the list
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person["city"]

    print(f"Full Name : {full_name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")

# Pets

pet_1 = {
    'animal_type': 'dog',
    'owner': 'james',
}

pet_2 = {
    'animal_type': 'cat',
    'owner': 'jane',
}

pet_3 = {
    'animal_type': 'rabbit',
    'owner': 'josh',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    animal = pet['animal_type']
    owner = pet['owner']

    print(f"{owner.title()} owns a {animal}.")


# Favorite places
    favorite_places = {
        'annette': ['nairobi', 'mombasa', 'kisumu'],
        'james': ['malindi', 'lamu', 'watamu'],
        'jane': ['kakamega', 'eldoret', 'nakuru'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
