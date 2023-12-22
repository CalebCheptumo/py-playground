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


#Changing, Adding, and Removing Elements
#The list are dynamic , meaning you can add,remove and change.


#changing an element in a list
grocery_list[0] = "Rice" #changing he value of first index
print(grocery_list)

grocery_list[3] = "Peanut Butter" #changing the value of last index
print(grocery_list)


#Adding an element to a list
#using append() method - adds new list item to the end.
#append() method takes one argument, the item to add to the list.
grocery_list.append("Groundnuts")
print(grocery_list)

#adding items to an empty list
trip_destinations = []
trip_destinations.append("Maldives")
trip_destinations.append("San Francisco")
trip_destinations.append("New York")
print(trip_destinations)

#inserting elements into a list at any position
#using insert() method - adds new list item at any position.
#insert() method takes two arguments, the item to add to the list and the index position.
todo = ["Do laundry", "Clean room", "Wash dishes"]
todo.insert(0, "Wake up early") #will insert at the beginning of the list
print(todo)


#Removing an element from a list
#using del statement - but you must know the index position of the item you want to remove. You can no longer access the value that was removed.
#del statement deletes an item at a specific index position.
todo = ["Do laundry", "Clean room", "Wash dishes"]
del todo[0] #will delete the first item in the list
print(todo)

#using pop() method to remove an item from a list
#pop() method removes an item from the end of the list and stores it in a variable so you can use it after removing it.

todo = ["Do laundry", "Clean room", "Wash dishes"]
last_todo = todo.pop() #will remove the last item in the list
print(last_todo) 
print(todo)

#use it to print statement
print(f"The last to do was {last_todo} and it was popped")


#using idex position to pop an item from a list
first_todo = todo.pop(0)
print(first_todo)
print(f"The first todo was {first_todo} it was popped using index position")

#Each time you use po() the item is no longer stores in the list

#using remove() method to remove an item from a list if you only know the item and not the index position.
#remove() only removes the first occurrence of the value you specify.
todo = ["Do laundry", "Clean room", "Wash dishes"]
todo.remove("Wash dishes")
print(todo)

todo = ["Do laundry", "Clean room", "Wash dishes"]
done_todo = "Do laundry" #assigning the value to a variable
todo.remove(done_todo)
print(f"The {done_todo} task is completed")