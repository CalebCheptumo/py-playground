from pathlib import Path
#addition - catches ValueError.


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