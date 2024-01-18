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
for name, number in favorite_numbers.items(): # items() method returns a list of key-value pairs and to iterate through the returned list, we use for loop.
    print(f"{name.title()} 's favorite number is {number}")
