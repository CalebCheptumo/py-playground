#print(5 / 0) # we get  traceback error message zero division error

#ZeroDivisionError is an exception object.
#we can modify the program , we will tell python what to do when this kind of exception occurs.


try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!") #this is the message that will be printed when the exception occurs. 