from pathlib import Path

def count_words(path): #define a function called count_words() that takes a path object as an argument.
    """Count the approximate number of words in a file. """
    #try- block to handle the exception that was raised.
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split() #split() method to produce a list of all the words in the file.
        num_words = len(words) #use len() to estimate the number of words in the file.
        print(f"The file {path} has about {num_words} words.")

path = Path("files-and-exceptions/alice.txt") #create a path object that points to alice.txt
count_words(path) #call the count_words() function and pass it the path object pointing to alice.txt.



filenames = ["files-and-exceptions/alice.txt", "files-and-exceptions/siddhartha.txt", "files-and-exceptions/moby_dick.txt"] # Files are stored as simple string
for filename in filenames: 
    path = Path(filename)
    count_words(path)