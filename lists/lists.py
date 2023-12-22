#What is a collection of items in a particular order can be of any type  letters, numbers, strings, etc.
#Square brackets [] indicate a list, and individual elements in the list are separated by commas.
#Syntax: list_name = [item1, item2, item3, ...]

grocery_list = ["Milk", "Eggs", "Bread", "Butter"]
print(grocery_list)


#Accessing Elements in a List
#You can access items in the list by their index.
#index starts at 0, not 1.

grocery_list = ["Milk", "Eggs", "Bread", "Butter"]
print(grocery_list[0])


#You can also use string methods in a list.
east_africa_countries = ["kenya", "uganda", "TANZANIA", "rwanda"]
print(east_africa_countries[0].title())
print(east_africa_countries[1].upper())
print(east_africa_countries[2].lower())


#Using Individual Values from a List - building a sentence/message.
east_africa_countries = ["kenya", "uganda", "TANZANIA", "rwanda"]
message = f"I world like to visit {east_africa_countries[3].title()} someday"
print(message)



