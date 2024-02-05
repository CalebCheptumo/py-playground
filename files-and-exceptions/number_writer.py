from pathlib import Path
import json #import the json module


#using json.dumps()
number = [2, 3, 5, 7, 11, 13] #create a list of numbers
path = Path("files-and-exceptions/number.json") #create a path object that points to number.json. choose a file name that ends in .json to indicate that the data is stored in JSON format.
contents = json.dumps(number) #use the json.dumps() function to store the list of numbers in the file number.json. The json.dumps() function takes a piece of data and writes it to a file in JSON format.
path.write_text(contents) #write the contents to the file



#using json.loads()
path = Path("files-and-exceptions/number.json") #create a path object that points to number.json
contents = path.read_text() #read the contents of the file
number = json.loads(contents) #use the json.loads() function to read the list of numbers back into memory. The json.loads() function takes a file object and reads the data from that file into memory.json.loads() function takes JSON-formatted string and returns python 