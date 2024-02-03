from pathlib import Path

contents = "I love programming.\n" # define variable contents that will hold the entire contents of the file
contents += "I love creating new games.\n" #use the += operator to add a new line to the contents of the file
contents += "I also love finding meaning in large datasets.\n"


path = Path('files-and-exceptions/programming.txt') #using a relative path
path.write_text(contents) # write_text() method takes the contents of the file as a single argument, the string you want to write to the file.

# you can use spaces,tab characters, and blank lines to format the output of your text files to make them easier to read.

