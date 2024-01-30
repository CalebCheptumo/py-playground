import pizza #imports the module then makes two calls to make_pizza():, python looks for the module pizza.py and copies all the functions from it into this program

pizza.make_pizza(16, 'pepperoni') # to call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#syntax: module_name.function_name()