from pathlib import Path

path = Path('files-and-exceptions/pi_million_digits.txt') #using a relative path
contents = path.read_text() #start by reading the entire contents of the file

lines = contents.splitlines() # returns a list of all lines in the file the assign the list to variable lines
pi_string = '' #initialize an empty string to hold the digits of pi
for line in lines: #loop that adds line of digits to pi_string
    #pi_string += line #add each line to pi_string
    pi_string += line.lstrip() # remove leading whitespace from each line before adding it to pi_string

birthday = input("Enter your birthday, in the form mmddyy:  ") #prompt the user to enter their birthday
if birthday in pi_string: #check if the birthday appears in the first million digits of pi
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")