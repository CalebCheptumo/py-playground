#tuples - looks just like a list , except that you use parenthesis instead of square brackets.
#tuples are immutable - you can't modify them
fruits = ("apple", "banana", "strawberry",)
print(fruits)

#you can access elements in a tuple using index position
print(fruits[0])
print(fruits[1])

#include a trailing comma if you want to define a tuple with one element
sides = (4,)

#looping through a tuple
sides = (3,3,9)
for side in sides:
    print(side)

#writing over a tuple
#althoug you cant modify tuple you can assign new value to a variable that rep a tuple.
sides = (3,3,9)
print("Original sides:")
for side in sides:
    print(side)

sides = (4,4,4)
print("\nModified sides:")
for side in sides:
    print(side)
    