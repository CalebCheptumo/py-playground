#greets user whose name has already been stored in username.json
from pathlib import Path
import json

path = Path('files-and-exceptions/username.json') #create a path object that points to username.json
contents = path.read_text() #read the contents of the file
username = json.loads(contents) #use the json.loads() function to read the username back into memory

print(f"Welcome back, {username}!") #greet the user whose name has already been stored in username.json