from pathlib import Path

path = Path('files-and-exceptions/gloria.txt') #using a relative path

try:
    contents = path.read_text() #read the contents of the file
    contents = contents.lower()

    count_the = contents.count('the') #count the number of times the word 'the' appears in the file 
    count_the_space = contents.count(' the ') #count the number of times the word 'the' appears in the file with spaces

    print("The word 'the' appears " + str(count_the) + " times in the file.")
    print("The word 'the' appears " + str(count_the_space) + " times in the file with spaces.")
except FileNotFoundError: #we use the FileNotFoundError exception to handle the case where the file does not exist.
    print(f"Sorry, the file {path} does not exist.") #print a message if the file does not exist.