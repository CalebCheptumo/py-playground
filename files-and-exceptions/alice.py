from pathlib import Path #import the Path class from the pathlib module


#will get FileNotFoundError since the file does not exist
#path = Path("alice.txt") #create a path object that points to alice.txt
#contents = path.read_text(encoding="utf-8") #the encoding argument tells python how to read the file. utf-8 is one of the most common encoding schemes. 


#handle the exception
path = Path("alice.txt") #create a path object that points to alice.txt
try:
    contents = path.read_text(encoding="utf-8") #the encoding argument tells python how to read the file. utf-8 is one of the most common encoding schemes.
except FileNotFoundError: #we use the FileNotFoundError exception to handle the case where the file does not exist.
    print(f"Sorry, the file {path} does not exist.") #print a message if the file does not exist.