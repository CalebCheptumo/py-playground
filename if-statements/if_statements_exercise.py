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


favorite_fruits = ['mango', 'apple', 'pineapple', 'watermellon']
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


# Hello admin
users = ['admin', 'ian', 'jane', 'mary', 'morine']
for user in users:
    if user == 'admin':
        print(f"Hello {user} would you like to see a status report?")
    else:
        print(f"Hello {user} thank you for logging in again")


# no user
users = []
if users:
    for user in users:
        print(f"Adding {user}")
    print("Finished adding users ")
else:
    print("We need to find some users!")


# checking username
current_users = ['admin', 'ian', 'jane', 'mary', 'morine']
current_users_lower = [user.lower() for user in current_users]

new_users = ['doe', 'mary', 'martin', 'ariana', 'ann']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Enter new username")
    else:
        print("username is available")


# ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number == 4:
        print("4th")
    elif number == 5:
        print("5th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    elif number == 9:
        print("9th")
