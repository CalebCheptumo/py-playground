#Python has three types of numbers - int, float, complex
#integer - whole number (positive or negative) without decimals example 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#float - number with decimal point. Example 1.0, 2.0, 3.0, 4.0, 5.0, 6.0
#complex - number with real and imaginary parts. Example 1 + 2j, 2 + 4j, 3 + 6j , 1j, 2j, 3j


#You can perform arithmetic operations on integers, floats and complex numbers
#Integers arithmetic operations 

add = 1 + 2
print(add)
sub = 3 - 1
print(sub)
mul = 3 * 2 
print(mul)
div = 2 / 1
print(div)
mod = 3 % 2 #modulus operator - returns the remainder of the division
print(mod)
exp = 2 ** 3 #exponent operator - raises a number to a power
print(exp)
floor_div = 3 // 2 #floor division - returns the quotient without the remainder
print(floor_div)

#Floats arithmetic operations
add = 1.4 + 8.0 
print(add)
sub = 3.74 - 0.8466
print(sub)
mul = 0.5 * 2.5
print(mul)
div = 2.5 / 0.5 
print(div)
mod = 3.5 % 2.5
print(mod)
exp = 2.5 ** 3.5
print(exp)


#integers and floats arithmetic operations
# divide two integers results always a float

div = 2 / 1
print(div)

add = 1 + 4.0
print(add)
mul = 2 * 0.2 
print(mul)


#complex numbers arithmetic operations

add = 1 + 2j + 3 + 4j
print(add)
sub = 3 - 1j - 1 + 2j
print(sub)
mul = 3 * 2j * 2 + 4j
print(mul)
div = 2 / 1j / 1 + 2j
print(div)


#Grouping digits of numbers with underscores
#You can group digits of numbers with underscores to make them more readable
#This is only available in Python 3.6 and above
#This is useful when working with large numbers
kenyan_population = 52_000_000
print(kenyan_population)


#Multiple Assignment
#You can assign values to multiple variables in one line
#Helps to make your code shorter and more readable
#You separate the variables with commas

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


#Constants
#A constant is a variable whose value cannot be changed
#Use all uppercase letters to name constants

PI = 3.14

#Conversion using int(), float() and complex() functions

x = int(2.5)
print(x)
y = float(5)
print(y)
z = complex(8)
print(z)


#Comparison Operators - used to compare values and return True or False
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)


