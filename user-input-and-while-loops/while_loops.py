# A while loop in Python repeatedly executes a target statement as long as a given condition is true.
# syntax: while expression:
#           statement(s)

# Example 1: Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1 # i = i + 1



#count form 1 to 5
current_number = 1 # start at 1
while current_number <= 5: # while loops as long as i is less than or equal to 5
    print(current_number)
    current_number += 1


#define a quit value

prompt = "\n Tell me something ,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


#fix printing quit
    
prompt = "\n Tell me something ,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)



#using a flag
# used to control how long the program runs
#flag is a boolean variable that signals when some conditions has been meet.
# if flag is True the loop continues
# if it becomes False the loop stops
        

#example
active = True #initializing the flag to True
while active: 
    print("Inside while loop")

    user_input = input("Do you want to continue: ")
    if user_input == 'no':
        active = False
        print("Loop has ended")



#using break to exit a loop
#break statement directs the flow of your program , you can use it to control which lines of code are executed and which aren't
#break statement immediately exits the loop it is in
        
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # will run forever unless it reaches a break statement
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"i'd love to go to {city.title()}!")


# you can use break statement in any of python's loops
        

#using continue in a loop
#continue statement tells python to ignore the rest of the loop and return to the beginning
#continue statement returns to the beginning of the loop based on the result of a conditional test
#continue statement is used to skip the rest of the code inside the enclosing loop for the current iteration and move on to the next iteration of the loop.
        
current_number = 0
while current_number < 10:
    current_number += 1 # increment current_number by 1
    if current_number % 2 == 0: # if modulo of current_number is 0
        continue  # continue to the beginning of the loop

    print(current_number)


#avoiding infinite loops
#Avoiding infinite loops in a while loop involves ensuring that the condition for the while loop will eventually become false. 

x = 1
while x <= 5:
    print(x)
    x += 1 # increment x by 1

#if you omit the line x += 1 , the loop will run forever because the conditional test x <= 5 will never evaluate to False
    


#while loop with lists and dictionaries
#you can use while loops to modify or move items between lists, or to iterate over dictionaries in combination with other functions

#moving items from one list to another
#consider a list of newly registered but unverified users of a website.
    
#start with users that need to be verified,
#and an empty list to hold confirmed users.
    
unconfirmed_users = ['jamo', 'phil' ,'mercy'] # list of unconfirmed users
confirmed_users = [] # empty list to hold confirmed users

#verify each user until there are no more unconfirmed users.
#move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop() # remove the last item in the list and store it in current_user
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) # add current_user to the end of the list


#display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# since mercy  is the last item in the list , she will be the first user to be verified
    


#While loop with dictionaries
# Start with a dictionary of unprocessed responses
responses = {
    'alice': 'blue',
    'brian': None,
    'candace': 'green',
}

# While there are still unprocessed responses
while None in responses.values():
    # Find the first unprocessed user
    for user, response in responses.items():
        if response is None:
            print(f"{user}, please submit your response.")
            new_response = input("Enter your response: ")
            responses[user] = new_response
            break
    



#removing all instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] # list of pets
print(pets)

while 'cat' in pets: # while 'cat' is in pets
    pets.remove('cat') # remove 'cat' from pets

print(pets)