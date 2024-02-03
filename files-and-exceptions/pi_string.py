from pathlib import Path

path = Path('files-and-exceptions/pi_digits.txt') #using a relative path
contents = path.read_text() #start by reading the entire contents of the file

lines = contents.splitlines() # returns a list of all lines in the file the assign the list to variable lines
pi_string = '' #initialize an empty string to hold the digits of pi
for line in lines: #loop that adds line of digits to pi_string
    pi_string += line #add each line to pi_string


print(pi_string) #print the string
print(len(pi_string)) # print the length of the string
