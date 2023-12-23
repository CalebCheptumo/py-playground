#using range()  function  - to generate a series of numbers 
#range() function takes 3 arguments - start, stop and step size. you can also pass one argument  and it will start the sequence form 0
#range() function  start counting from the first value and stops when it reaches the second value you provided
for value in range(1, 10): # in this case it prints 1 to 9
    print(value)


#using range() to make a list of numbers
#using list() function to convert the range() result to a list.
#syntax: list(range(start, stop))
numbers = list(range(1, 10))
print(numbers)


even_numbers = list(range(2, 11, 2)) # takes 3 arguments teh start of sequence 2, he end of sequence 11, and  step size 2.(even numbers)
print(even_numbers)


# make a list of first 10 square numbers
squares = []
for value in range (1 ,11):
    square = value ** 2
    squares.append(square)
print(squares)


#we can as well write the above code in a more concise way
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)


#simple statistics with a list of numbers
#find min() - minimum number
#find max() - maximum number
#find sum() - sum of a list of numbers

numbers = [1 , 2 ,3 ,0 ,8 , 4, 5 , 10, 9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))



#list comprehensions - allows you to generate  list in just one line of code. it combines for loop and creation of new elements in one line and automatically append each new element. 
#syntax: [expression for value in range(start, stop)] or  [expression for item in iterable]
squares = [value ** 2 for value in range(1 ,11)]
print(squares)