#Strings - is a series of characters surrounded by single or double quotes or triple quotes for multi-line strings
string1 = "This is a string"
string2 = 'This is also a string'
string3 = """This is a multi-line string"""
print(string1)
print(string2)
print(string3)

#String Concatenation - joining of two or more strings together using the + operator
greeting = "Hello"
name = "Caleb"
message = greeting + name
print(message)

#Changing Case in a String with Methods
country = "kenya"
print(country.title())

#Changing a string to all uppercase or all lowercase
continent = "Africa"
print(continent.upper())
print(continent.lower())

#Using Variables in Strings
#using the f-string method
car_make = "Toyota"
car_model = "Corolla"
car_year = 2020
car_info = f"{car_make} {car_model} {car_year}"
print(car_info)

#Use f-string to compose a full message
car_info = f"My car is a {car_make} {car_model} from the year {car_year}"
print(car_info)

#Adding Whitespace to Strings with Tabs or Newlines
#Adding a tab to a string
print("\tWe use backslash and t to add a tab to a string")
#Adding a newline to a string
print("we use backslash and n to add a newline to a string\nThis is a new line\nThis is another new line")
#You can also combine tabs and newlines
print("Languages\n\tPython\n\tJava")


#Stripping Whitespace
#Using the rstrip() method to remove whitespace from the right side of a string
favorite_song = "YAWA by Fireboy DML "
print(favorite_song.rstrip())
#Using the lstrip() method to remove whitespace from the left side of a string
favorite_song = " YAWA by Fireboy DML"
print(favorite_song.lstrip())
#Using the strip() method to remove whitespace from both sides of a string
favorite_song = " YAWA by Fireboy DML "
print(favorite_song.strip())

#replace() method
#Using the replace() method to replace a word in a string
favorite_song = "YAWA by Fireboy DML"
print(favorite_song.replace("YAWA", "Bandana"))

#Using the count() method to count the number of times a word appears in a string
favorite_song = "YAWA YAWA by Fireboy DML"
print(favorite_song.count("YAWA"))

#Using the find() method to find the index of a word occurrence in a string
favorite_song = "YAWA by Fireboy DML"
print(favorite_song.find("Fireboy"))


#Using the split() method to split a string into a list
ingredients = "milk, sugar, flour, eggs"
print(ingredients.split(","))


#Removing Prefixes and Suffixes from Strings
#Using the removeprefix() method to remove a prefix from a string
portfolio = "https://calebcheptumo.com"
print(portfolio.removeprefix("https://"))
#Using the removesuffix() method to remove a suffix from a string
portfolio = "https://calebcheptumo.com"
print(portfolio.removesuffix(".com"))


#Avoiding Syntax Errors with Strings
#Using apostrophe inside single quotes
gratitude = "I'm grateful to God"
print(gratitude)

#String length
#Using the len() function to get the length of a string
christmass = "Merry Christmass"
print(len(christmass))

#length starts from 0 to the last character
#white space is also counted as a character


#Using Indexes to Access Individual Characters in a String
motivation = "I will never give up"
print(motivation[0]) #prints the first character in the string
print(motivation[7:20]) #prints the characters from index 7 to 11

#Raw Strings
#Using raw strings to ignore escape characters. by adding r before the string
path = r"/home/caleb/Documents/CALEBTHEDEV/py-playground/"
print(path)
