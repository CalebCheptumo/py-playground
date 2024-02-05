#prompt the user for their name the first time they run a program ad then remembers their name when tey run the program again.
from pathlib import Path
import json

username = input("What is your name? ") #prompt the user for their name

path = Path('files-and-exceptions/username.json') #create a path object that points to username.json. write thr data from input to the file username.json
contents = json.dumps(username) #use the json.dumps() function to store the username in the file username.json
path.write_text(contents) #write the contents to the file

print(f"We'll remember you when you come back, {username}!") #print a message to the user