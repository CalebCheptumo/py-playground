from pathlib import Path

path = Path('files-and-exceptions/guest_book.txt') #using a relative path


while True: #create an infinite loop
   guest_name = input("Please enter your name: ") #prompt the user to enter their name
   if guest_name == 'q': #if the user enters 'q', break the loop
       break
   else:
    existing_guests = path.read_text() #read the contents of the file
    existing_guests += guest_name + '\n' #add the new guest's name to the existing guests
    path.write_text(existing_guests) #write the updated list of guests to the file
    
    print("Welcome, " + guest_name + "!") #welcome the new guest

print("Thank you for visiting!") #thank the guests for visiting    