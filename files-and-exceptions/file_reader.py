#opens pi_digits.txt file , reads the contents of the file, and prints the contents to the screen.
from pathlib import Path #import the Path class from the pathlib module

path = Path("/home/caleb/Documents/CALEBTHEDEV/py-playground/files-and-exceptions/pi_digits.txt") #create a Path object that represents the location of the file on your system
contents = path.read_text() #read the contents of the file and store the contents in a variable
print(contents) #print the contents of the file to the screen

