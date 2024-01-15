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

# Simple if statement
# conditional_test = 'A'
# if conditional_test:
# do something

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")


# if else statement -  when you want to take one action when a condition test passes and a differnet action in all other cases
# else statement allows you to define an action or set of actions that are executed when the condition test fails
age = 17
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry , you are too young to vote")
    print("Please register to vote as soon you turn 18")

# if condition passes first block is executed , else second block
# only works when you want python to execute one of the two possible actions.

# if-elif-else chain - test more than two possible situations
# determine admission rate
age = 12
if age < 4:
    print("Your admission cost is Ksh 0")
elif age < 18:
    print("Your admission cost is Ksh 250")
else:
    print("Your admission cost is Ksh 400")


# using multiple elif block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 250
elif age < 65:
    price = 400
else:
    price = 200  # people older than 65
print(f"your admission cost is ksh {price}")


# omitting the else block - python does not require an end of if-elif chain - its clear to use an additional elif statement
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 250
elif age < 65:
    price = 400
elif age >= 65:  # assigns price when person is 65 or older
    price = 200

print(f"Your admission cost is ksh {price}")


# testing multiple condition
# if-elif-else chain is only appropriate to use when you just need one test to pass.- as soon python finds on test that passes it skips the rest test
# use series of if statement with no elif or else to check all conditions of interest
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")
print("\nFinished making your pizza")
