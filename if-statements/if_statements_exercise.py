# Conditional tests
month = 'January'
print("Is month == 'January'? True.")
print("month == 'January'")

print("\nIs month == 'February'? False")
print("month == 'February'")


print("Test 1: Is 'python' == 'python'? I predict True.")
print('python' == 'python')

print("\nTest 2: Is 'python' != 'java'? I predict True.")
print('python' != 'java')


print("\nTest 3: Is 'Python'.lower() == 'python'? I predict True.")
print('Python'.lower() == 'python')

print("\nTest 4: Is 'JAVA'.lower() == 'java'? I predict True.")
print('JAVA'.lower() == 'java')

languages = ['python', 'java', 'c++', 'javascript']
print("\nTest 13: Is 'python' in languages? I predict True.")
print('python' in languages)

print("\nTest 14: Is 'ruby' in languages? I predict False.")
print('ruby' in languages)

print("\nTest 15: Is 'ruby' not in languages? I predict True.")
print('ruby' not in languages)

print("\nTest 16: Is 'python' not in languages? I predict False.")
print('python' not in languages)


# alien colors
alien_color = 'green'
if alien_color == 'green':
    print("You have earned 5 points ")
if alien_color == 'red':
    print("You have 0earned 0 point")


alien_color = 'green'
if alien_color == 'green':
    print("You earned 50 points")
else:
    print("You earned 10 point")


alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points")
elif alien_color == 'yellow':
    print("You earned 10 points")
elif alien_color == 'red':
    print("You earned 15 points")

age = 18
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
elif age >= 65:
    print("Elder")


favorite_fruits = ['mango','apple','pineapple','watermellon']
if 'mango' in favorite_fruits:
    print("i like mango")
if 'orange' in favorite_fruits:
    print("i really like orange")
if 'apple' in favorite_fruits:
    print("i like apple")
if 'pineapple' in favorite_fruits:
    print("i like pineapple")
if 'avocado' in favorite_fruits:
    print("i like avocado")
if 'watermellon' in favorite_fruits:
    print("i like watermellon")

