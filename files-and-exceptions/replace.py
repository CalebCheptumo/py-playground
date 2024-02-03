from pathlib import Path

path = Path('files-and-exceptions/learning_python.txt') #using a relative path
contents = path.read_text() #read the contents of the file
print(contents) #print the contents of the file

#lines = contents.splitlines() #split the contents of the file into lines
learning_string = '' #create an empty string to store the contents of the file

#for line in lines: #iterate over the lines in the file
for line in contents.splitlines(): # you can loop directly over the list that splitlines() returns
   modified_line = line.replace('Python', 'C') #replace the word 'Python' with 'C'
   learning_string += modified_line.lstrip() #add the line to the learning_string, removing any leading whitespace
   

print(learning_string) #print the learning_string   