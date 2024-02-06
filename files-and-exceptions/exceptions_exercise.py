from pathlib import Path
#addition - catches ValueError.
import json


print("Give me two numbers, and I'll add them.") 
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ") 
    if first_number == 'q': 
        break
    second_number =  input("Second number: ") 
    if second_number == 'q': 
        break
    try:
        answer = int(first_number) + int(second_number) 
    except ValueError:
        print("You can't add strings!")
    else:
        print(answer)




#addition calculator

path = Path('files-and-exceptions/guest_book.txt') #using a relative path


while True: #create an infinite loop
    try:
        num1 = input("Please enter the first number (or 'q' to quit): ")
        if num1.lower() == 'q': #if the user enters 'q', break the loop
            break
        num1 = int(num1)

        num2 = input("Please enter the second number (or 'q' to quit): ")
        if num2.lower() == 'q': #if the user enters 'q', break the loop
            break
        num2 = int(num2)

    except ValueError:
        print("You've entered an invalid number. Please try again.")
    else:
        sum = num1 + num2
        print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum) + ".")

print("Thank you for using the calculator!") #thank the user for using the calculator



#cats and dogs

path = Path('files-and-exceptions/cats.txt') #using a relative path
contents = path.read_text() #read the contents of the file
print(contents) #print the contents of the file


path = Path('files-and-exceptions/dogs.txt') #using a relative path
contents = path.read_text() #read the contents of the file
print(contents) #print the contents of the file


#cats and dogs file not found
path = Path('cats.txt') 
try:
    contents = path.read_text() #read the contents of the file
    print(contents) #print the contents of the file
except FileNotFoundError:
    print("The file " + str(path) + " was not found.")

#silent cats and dogs file not found
path = Path('cats.txt')
try:
    contents = path.read_text() #read the contents of the file
    print(contents) #print the contents of the file
except FileNotFoundError:
    pass



#favorite number

favorite_number = input("What's your favorite number? ") #ask the user for their favorite number
path = Path('files-and-exceptions/favorite_number.json') #create a path object that points to favorite_number.json
contents = json.dumps(favorite_number) #convert the favorite number to a string
path.write_text(contents) #write the favorite number to the file
print("Thanks! I'll remember that.") #thank the user for their favorite number


#favorite number reads value
path = Path('files-and-exceptions/favorite_number.json') #create a path object that points to favorite_number.json
contents = path.read_text() #read the contents of the file
favorite_number = json.loads(contents) #convert the string to a number
print("I know your favorite number! It's " + str(favorite_number) + ".") #print the favorite number
