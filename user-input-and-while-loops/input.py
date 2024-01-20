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
