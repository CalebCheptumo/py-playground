from pathlib import Path

path = Path('files-and-exceptions/pi_digits.txt') #using a relative path
contents = path.read_text() #start by reading the entire contents of the file
#lines = contents.splitlines() # returns a list of all lines in the file the assign the list to variable lines
#for line in lines: #the loop then prints each line of the file
for line in contents.splitlines(): # you can loop directly over the list that splitlines() returns
    print(line) # since we haven't made any modifications to the file, the output will be the same as the original file