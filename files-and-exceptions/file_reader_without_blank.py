from pathlib import Path

#the output  has an extra blank line at the end o. the blank line appears because read_text() returns an empty string when it reaches the end of the file; this empty string is displayed as a blank line. If you want to remove the extra blank line, you can use rstrip() on the string that read_text() returns:

path = Path("/home/caleb/Documents/CALEBTHEDEV/py-playground/files-and-exceptions/pi_digits.txt") #create a Path object that represents the location of the file on your system
contents = path.read_text() #read the contents of the file and store the contents in a variable
contents = contents.rstrip() #remove the extra blank line from the end of the string
print(contents) #print the contents of the file to the screen



path = Path("/home/caleb/Documents/CALEBTHEDEV/py-playground/files-and-exceptions/pi_digits.txt") #create a Path object that represents the location of the file on your system
contents = path.read_text().rstrip() #read the contents of the file and store the contents in a variable. 
print(contents) #print the contents of the file to the screen

#method chaining - calling methods on a variable that returns a string, you can call another method on the result. The method rstrip() is called on the result of path.read_text(), and the result of rstrip() is printed to the screen.
