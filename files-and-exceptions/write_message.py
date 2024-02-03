from pathlib import Path

path = Path('files-and-exceptions/write_message.txt') #using a relative path
path.write_text("I love programming.") # write_text() method takes a single argument, the string you want to write to the file.

#python can only write strings to a text file. If you want to write numerical data to a text file, you'll have to convert the data to a string first using the str() function.
#syntax: path.write_text(str(3.14159))
