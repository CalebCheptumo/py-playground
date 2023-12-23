#Looping - is a way of repeatedly execute a block of code .
# for loop , while loop and nested loop are the types of loops in python.

# for loop - is used to iterate over a sequence like list,string
# for loop is often used when you want to perform an action certain number of times or for each time in a sequence.
#for loop syntax
#for variable in sequence :
    #code to be executed


fruits = ["Apple", "Orange", "Banana", "Mango", "Watermelon"]
for fruit in fruits: # for every fruit in fruits list print the fruit name.
   print(fruit)

#do more with for loop
students = ["Mary", "Ian", "Jude", "James", "Purity"]
for student in students:
   print(f" Hello {student} , school will be opening on 9th January 2024 ")
   print("Please come with your fees")
print("Merry Christmas and Happy New Year") #no indentation thus, not part of the loop block thus executed once.
