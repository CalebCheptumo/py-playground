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