#Exceptions - a special Python class designed to held you respond to error s when they arise.
#Python uses special objects called exceptions to manage errors that arise during a program's execution.
#When an error occurs that makes Python unsure what to do next, it creates an exception object.
#if you dont handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
#Exceptions are handled with try-except blocks.
#A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.
#When you use try-except blocks, your programs will continue running even if things start to go wrong.


#Handling the ZeroDivisionError Exception
#When you try to divide by zero, Python raises an exception because it can’t carry out the division.


#using try-except blocks
#write try-except block to handle the exception that was raised.
#syntax: try:
#               print(5 / 0)
#        except ZeroDivisionError:
#               print("You can't divide by zero!")
#The code that could potentially cause an error goes in the try block.

#we put the line that cause the error inside try block.
#python skips over the except block if the code in the try block causes an error.
#python looks for an except block telling it how to respond to the error.



#using exceptions to prevent crashes
#prompt for more valid input instead of crashing.
#example: division calculator

