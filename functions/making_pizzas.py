#import pizza #imports the module then makes two calls to make_pizza():, python looks for the module pizza.py and copies all the functions from it into this program
#from pizza import make_pizza #imports the function make_pizza() from the module pizza
#from pizza import make_pizza as mp #import renames the function make_pizza() to mp()
#import pizza as p # module pizza is given an alias p
from pizza import *




#pizza.make_pizza(16, 'pepperoni') # to call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#syntax: module_name.function_name()

#make_pizza(16, 'pepperoni') # You dont need to use the dot notation when you call a function using this syntax of specifying the function name only, because you have explicitly imported the function make_pizza() in the import statement
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')


#p.make_pizza(16, 'pepperoni') 
#p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni') # you call function by name since every function is imported
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')