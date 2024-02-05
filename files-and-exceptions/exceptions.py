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

#the else block
#we can make the program more error resistant by wrapping the line that might produce errors in a try-except block.
#the error occurs on the line that performs the division so that where we'll put the try-except block
#the else block runs if the code in the try block runs successfully.


#handing the FileNotFoundError exception
#the file you are looking for might:
#1. be in a different location
#2. have a different name
#3. not exist at all
#4. be in a different format
#you can handle the FileNotFoundError exception using a try-except block.


#analyzing text
#you can use the split() method to split a string into a list of elements.

#working with multiple files
# count_words() function that counts the approximate number of words in a file.
#count_words() function takes a filename as an argument and tries to count the number of words in the file.
#


#Failing silently
#you cont need to report every exception you catch.
#you want the program to fail silently when an exception occurs and continue on as if nothing happened 
#to make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block.
#syntax: try:
#               print(5 / 0)
#        except ZeroDivisionError:
#               pass
#The pass statement tells Python to do nothing in the block.
#The pass statement also acts as a placeholder. It tells you that you decided to do nothing at a specific point in your program and that you might want to do something there later.


#deciding which errors to report
#1. if the user enters the wrong filename, you can respond silently or you can prompt the user to enter a different filename.
#2. if the file is missing, you can respond silently or you can prompt the user to enter a different filename.
#give user information they need, but dont overwhelm them with details they dont need.



#storing data
#programs will ask users to input certain kind of information.
# a simple way to store user input is storing the data using json module.
#json module allows you to convert simple python data structure into JSON-formatted string and the load the data from thee file the next time the program runs.
#can also use jason to share data between different python programs.
#JSON-  Javascript Object Notation was originally developed by JavaScript, however it has since become a common format used by many languages including python.


#using json.dump() and json.load()
#json.dumps() function takes one argument: the data you want to convert to JSON format.
#json.dumps() return a string.
#syntax: json.dumps(data)