from pathlib import Path

path = Path('files-and-exceptions/pi_million_digits.txt') #using a relative path
contents = path.read_text() #start by reading the entire contents of the file

#lines = contents.splitlines() # returns a list of all lines in the file the assign the list to variable lines
pi_string = '' #initialize an empty string to hold the digits of pi
#for line in lines: #loop that adds line of digits to pi_string
for line in contents.splitlines(): # you can loop directly over the list that splitlines() returns
    #pi_string += line #add each line to pi_string
    pi_string += line.lstrip() # remove leading whitespace from each line before adding it to pi_string

print(f"{pi_string[:52]}...")
print(len(pi_string))