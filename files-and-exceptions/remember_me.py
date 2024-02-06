#prompt the user for their name the first time they run a program ad then remembers their name when tey run the program again.
from pathlib import Path
import json

username = input("What is your name? ") #prompt the user for their name

path = Path('files-and-exceptions/username.json') #create a path object that points to username.json. write thr data from input to the file username.json
contents = json.dumps(username) #use the json.dumps() function to store the username in the file username.json
path.write_text(contents) #write the contents to the file

print(f"We'll remember you when you come back, {username}!") #print a message to the user


#combine the two programs into one file

path = Path('files-and-exceptions/username.json') #create a path object that points to username.json
if path.exists():# exists() method returns True if a file exists and False if it does not.
    contents = path.read_text() #read the contents of the file
    username = json.loads(contents) #use the json.loads() function to read the username back into memory
    print(f"Welcome back, {username}!") #greet the user whose name has already been stored in username.json
else:
    username = input("What is your name? ") #prompt the user for their name
    contents = json.dumps(username) #use the json.dumps() function to store the username in the file username.json
    path.write_text(contents) #write the contents to the file
    print(f"We'll remember you when you come back, {username}!") #print a message to the user


#refactoring
#move the bulk of logic into one or more functions
    
def greet_user():
    """Greet the user by name."""
    path = Path('files-and-exceptions/username.json') #create a path object that points to username.json
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user() #call the function greet_user() to greet the user by name


#refactor greet_user() so its not doing so many different tasks
def get_stored_username(path): #create a function called get_stored_username() that retrieves a stored username
    """Get stored username if available."""
    if path.exists(): #create a path object that points to username.json
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None #return None if the file username.json does not exist
    
def greet_user():
    """Greet the user by name."""
    path = Path('files-and-exceptions/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
