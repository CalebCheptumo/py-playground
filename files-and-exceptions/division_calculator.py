#print(5 / 0) # we get  traceback error message zero division error

#ZeroDivisionError is an exception object.
#we can modify the program , we will tell python what to do when this kind of exception occurs.


try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!") #this is the message that will be printed when the exception occurs. 



print("Give me two numbers, and I'll divide them.") #
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ") # prompt the user to enter the first number
    if first_number == 'q': # if the user enters 'q', the program will break out of the loop.
        break
    second_number =  input("Second number: ") # prompt the user to enter the second number
    if second_number == 'q': # if the user enters 'q', the program will break out of the loop.
        break
    answer = int(first_number) / int(second_number) # the program divides the two numbers and stores the result in the variable answer.
    print(answer)