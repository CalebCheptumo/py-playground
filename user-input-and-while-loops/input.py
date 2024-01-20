# input() -function - prompts user to enter input
# input() -function - returns string value
# int() -function - converts string to integer
# float() -function - converts string to float
# str() -function - converts integer to string
# str() -function - converts float to string
# syntax: variable = input("prompt")

name = input("Enter your name: ")
print(f"hello {name}")

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# use easy and simple prompts
# add a space at the end of the prompt to make it easier for the user to provide input
# multiline prompt - use \n to add a new line in the prompt

prompt = "If you tell us who you are, we can personalize the messages you see."
# +=  operator takes the string that was stored in prompt and adds the new string onto the end
prompt += "\nWhat is your first name? "


name = input(prompt)
print(f"Hello, {name}!")


# using int() to accept numerical input
# input() function interprets everything as a string

age = input("How old are you .? ")
print(f"Your age is {age}")
age = int(age)  # convert string to integer
print(age >= 18)


# use int() to convert the string returned from input() to an integer
# syntax: variable = int(input("prompt"))

weight = input("How many pounds do you weigh? ")
weight = int(weight)

if weight >= 100:
    print("Please unfat")
else:
    print("Please eat more")


# Modulo operator (%) - divides one number by another number and returns the remainder
# modulo operator doesn't tell you how many times one number fits into another
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

number = input("Enter a number, and ill tell you if it even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
