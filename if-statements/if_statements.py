# if statements - allows you to examine the current state of a program and respond appropriately to that state.

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Kinds of tests
# 1. conditional tests - expression that can be evaluated as True of False
# python uses the values treu or false to decide whether to execute a code in if statement . if a condition test is true python executes the code following if statement , if its false python ignores the code.
# checking for equality
car = 'bmw'  # sets the value of car to 'bmw' (= a statement)
car == 'bmw'  # checks whether the value of car is 'bmw' (== ask question)
# this will be true
# ignoring cases when checking for equality
# testing equality is case sensitive
car = 'Audi'
car == 'audi'
# this will be false
# you can convert the variable to lowercase before doing comparison
car = 'Audi'
car.lower() == 'audi'
# will be true

# checking for inequality by using inequality operator (!=)- to determine whether two values are not equal

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")
# compares the value of requested_topping to the value anchovies . if the two value dont match python returns true . python returns false if they match
# the value of requested_topping is not anchovies


# numerical comparisons
age = 18
age == 18
# true

# check if two numbers are not equal
answer = 17
if answer != 42:
    print('That is not correct answer. Please try again!')


# including mathematical comparison
age = 19
age < 21
# True
age <= 21
# True
age > 21
# False
age >= 21
# False


# Checking multiple conditions- suing the keywords (and) & (or)
# use the keyword and to combine two conditional tests.
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# False
# use the keyword or to it passes whether or both of the individual tests passes
# or expression fails only when both individual  tests fail
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
# True


# Checking whether a value is in a list - using keyword (in)
requested_topping = ['mushroom', 'onions', 'pineapple']
'mushroom' in requested_topping
# True
'pepperoni' in requested_topping
# False


# Checking whether a value is not on the list - using keyword (not)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()} , you can post a response if you wish.")


# boolean expression another name for conditional expression after it has been evaluated.
# always used to keep track of certain conditions - whether game is running, whether a user can edit certain content on a website.
game_active = True
can_edit = False
