from pathlib import Path

path = Path('files-and-exceptions/guest.txt') #using a relative path

guest_name = input("What is your name? ") #prompt the user for their name

path.write_text(guest_name) #write the user's name to the file