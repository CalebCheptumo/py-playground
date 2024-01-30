#functions allow you to break your programs into smaller parts ,each of which does one specific job.
#function block of organized, reusable code that is used to perform a single, related action.
#functions help you follow the DRY principle
#function helps to write code that is clean, readable, and reusable
#syntax of a function 
#def function_name(parameters):
#    """docstring"""
#    function body
#    return expression

def greet_user():
    """Display a simple greeting. """
    print("Hello!")

greet_user()

#when you want to use this function , you call it. A function call tells python to execute the code in the function. To call a function, you write the name of the function, followed by any necessary information in parentheses, such as a name, if the function needs one. Because no information is needed here, calling our function is as simple as entering greet_user().


#structure of a function
#def function_name(parameters):
    #"""docstring"""
   # function body
   # return expression

#def keyword tells python you are defining a function(function definition) ends in a colon
#function_name unique identifier of the function
#any indented lines that follow def function_name(): make up the body of the function
#parameters (or arguments) are values passed into a function , optional
#docstring describes what the function does. Docstring are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.
#function body is a block of statements that perform a specific task, where the function's functionality is expressed
#return statement sends a result back to the code that called the function, used to exit a function and go back to the line of code that called it  

#passing information to a function
#information that is passed to a function is called an argument

def greet_user(username): #username is a parameter, allows the function to accept any value of username you specify
    """Display a simple greeting."""
    print(f"Hello, {username.title()} good morning!")

greet_user('jesse') # passing jesse as an argument to the function greet_user()



#arguments and parameters
#parameter is a piece of information the function needs to do its job
#argument is a piece of information that is passed from a function call to a function
#username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job
#jesse in greet_user('jesse') is an example of an argument, a piece of information that is passed from a function call to a function


#passing arguments
#passing arguments to a function can be done in a number of ways
#positional arguments - need to be in the same order the parameters were written
#keyword arguments- each argument consists of a variable name and a value, and the order of the arguments doesn't matter

#positional arguments
#These are arguments that need to be passed in the same order as the parameters in the function definition.
#The first argument gets assigned to the first parameter, the second argument gets assigned to the second parameter, and so forth.

def describe_pet(animal_type, pet_name): #animal_type and pet_name are parameters
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'simba') #dog is assigned to animal_type and simba is assigned to pet_name , these are arguments


#multiple function calls
#you can call a function as many times as needed

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'simba')
describe_pet('cat', 'mimi')
describe_pet('fish', 'nemo')


#order matters in positional arguments -  make sure the arguments are in the same order as the parameters in the function definition

 
#keyword arguments  - name-value pair that you pass to a function
# You can also pass arguments as key-value pairs, where each argument consists of a variable name and a value. This way, the order of the arguments doesn't matter.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type = 'dog', pet_name = 'simba') #animal_type = 'dog' is a keyword argument
describe_pet(pet_name = 'simba', animal_type = 'dog') #order of the arguments doesn't matter

#be sure to use the exact names of the parameters in the function's definition


#default values 
#You can define a default value for each parameter.
#Python uses the argument value  for a parameter if function call provides one.


def  describe_pet(pet_name, animal_type='dog'): #default value for animal_type is 'dog'
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name = 'simba') #animal_type is not specified, so it defaults to 'dog'
describe_pet('simba') #positional argument , but first parameter needs to be pet_name
describe_pet(pet_name='mimi', animal_type='cat') #describe another animal other than dog(default value) , ignore the default value

#when you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.


#equivalent function calls
#positional arguments, keyword arguments, and default values can all be used together

def describe_pet(pet_name, animal_type ='dog'): #default value for animal_type is 'dog' , argument for pet_name needs to be provided.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


     

#a dog named simba
describe_pet('simba') #positional argument 
describe_pet(pet_name='simba') #keyword argument


#a fish named nemo
describe_pet('nemo', 'fish') #positional arguments
describe_pet(pet_name='nemo', animal_type='fish') #keyword arguments
describe_pet(animal_type='fish', pet_name='nemo') #keyword arguments



#avoiding argument errors
#unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work


def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet() #missing 2 required positional arguments: 'animal_type' and 'pet_name'



#return values - the value the function returns.
#A function can return a value or a set of values. When a function returns a value, the calling line must provide a variable in which to store the return value. A function stops running when it reaches a return statement.

#returning a simple value
#store first and last name separately and then call the function get_formatted_name() to combine them
def get_formatted_name(first_name, last_name): # get_formatted_name() function takes  first_name, last_name as parameters
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}" #full_name is a variable that combines first_name and last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def add_numbers( number1 , number2): #function add_numbers takes two parameters number1 and number2
    """Add two numbers"""
    sum = number1 + number2
    return sum

result = add_numbers(2, 3)
print(result)


#making an argument optional
#sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to
#You can use default values to make an argument optional. 
#expand get_formatted_name() to handle middle names, but middle names aren't always needed, so make the middle name optional

def get_formatted_name(first_name, middle_name, last_name): 
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker') 
print(musician)

#make middle name optional by giving it an empty default value and move it to the end of the list of parameters

def get_formatted_name(first_name, last_name, middle_name=''): 
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'hooker') 
print(musician)

musician =get_formatted_name('john', 'hooker', 'lee')
print(musician)



def greet_user(username, greeting="Hello"): # function greet_user takes two parameters: username and greeting. greeting has a default value of "Hello"
    """This function greets the user with an optional custom greeting."""
    print(f"{greeting}, {username}!")

greet_user("Alice")  # Outputs: Hello, Alice!
greet_user("Bob", "Welcome")  # Outputs: Welcome, Bob!



#returning a dictionary
#A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.

def build_person(first_name, last_name): #build_person() function takes first_name and last_name as parameters and puts them into a dictionary
    """Return a dictionary of information about a person"""
    person= {'first':first_name, 'last': last_name} #person is a dictionary that stores value of first_name is stored with the key 'first' and value of last_name is stored with the key 'last'
    return person # return the dictionary

musician = build_person('jimi', 'hendrix')
print(musician)


#extending to accept optional values

def build_person(first_name, last_name, age= None): #age is an optional parameter with a special value None, which is used when a variable has no specific value assigned to it
    """Return a dictionary of information about a person"""
    person= {'first':first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)



#using a function with a while loop

#def get_formatted_name(first_name, last_name):
 #   """Return a full name, neatly formatted"""
  #  full_name = f"{first_name} {last_name}"
   # return full_name.title()

#This is an infinite loop!
#while True:
 #   print("\nPlease tell me your name:")
  #  f_name = input("First name: ")
   # l_name = input("Last name: ")

    #formatted_name = get_formatted_name(f_name, l_name)
    #print(f"\nHello, {formatted_name}")


#adding quit to infinity loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit)")

        f_name = input("First name: ")
        if f_name == 'q':
            break
        l_name = input("Last name: ")
        if l_name == 'q':
            break

        formatted_name = get_formatted_name(f_name,l_name)
        print(f"\nHello, {formatted_name}!")



#passing a list

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


def print_fruits(fruits):
    """Print all elements in a list"""
    for fruit in fruits:
        print(fruit)

fruit_list = ['apple', 'banana', 'cherry']
print_fruits(fruit_list)



#modifying a list in a function
# the function can permanently modify the list, and the changes are reflected in the original list

#start with some designs that need to be printed
unprinted_designs = ['Phone case', 'robot pendant', 'dodecahedron'] # list of designs that need to be printed
completed_models = [] # empty list to store completed models

#simulate printing each design , until none are left
#move each design to completed_models after printing
while unprinted_designs: 
    current_design = unprinted_designs.pop() 
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


#refactoring

def print_models(unprinted_designs, completed_models): #function print_models() takes two parameters: a list of designs that need to be printed and a list of completed models
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs: 
        current_design = unprinted_designs.pop() 
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models): #function show_completed_models() takes a list of completed models as a parameter and displays each model that was printed
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['Phone case', 'robot pendant', 'dodecahedron'] # list of designs that need to be printed
completed_models = [] # empty list to store completed models

print_models(unprinted_designs, completed_models) #call print_models() with the two lists
show_completed_models(completed_models) #call show_completed_models() with the list of completed models

#every function should have one specific job. The first function prints each design, and the second displays the completed models. This is more beneficial than using one function to do both jobs.

#preventing a function from modifying a list
#syntax function_name(list_name[:]) - the slice notation [:] makes a copy of the list to send to the function

print_models(unprinted_designs[:], completed_models) #call print_models() with the two lists



#passing an arbitrary number of arguments
#Python allows a function to collect an arbitrary number of arguments from the calling statement

def make_pizza(*toppings): #the asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple
    """Print the list of toppings that have been requested"""
    print(toppings) #print the tuple of toppings

make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Python packs the arguments into a tuple, even if the function receives only one value

#looping through all values in a tuple

def make_pizza(size, *toppings): # python assigns the first value it receives to the parameter size and packs the rest of the values into the tuple toppings
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size} inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")


make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

#generic parameter *args - collects arbitrary positional arguments like a tuple

def print_args(*args):  #function print_args() accepts an arbitrary number of arguments and prints each argument
    """Print all arguments"""
    for arg in args: # iterate over the arguments tuple and print each value
        print(arg)

print_args('apple', 'banana', 'cherry')

# syntax *kwargs  which collects any remaining keyword arguments into a dictionary:
# parameter **kwargs used to collect nonspecific keyword arguments
def print_kwargs(**kwargs): #function print_kwargs() accepts an arbitrary number of keyword arguments and prints each argument
    """Print all keyword arguments"""
    print(kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

#using arbitrary keyword arguments
#example is building user profiles

def build_profile(first, last, **user_info): #function build_profile()  takes in a first and last name, and then it allows the user to pass in as many name-value pairs as they want
    """Build a dictionary containing everything we know about a user """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') #build_profile() takes in a first and last name, and then it allows the user to pass in as many name-value pairs as they want
print(user_profile) # returns a dictionary containing everything we know about a user



#storing your functions in modules
#storing your function in a separate file called a module then importing that module into your main program.
#an import statement tells Python to make the code in a module available in the currently running program file.
#this allows you to hide the details of your program's code and focus on its higher-level logic
#it also allows you to reuse functions in many different programs
#ways to import a module
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn   
#from module_name import *



#importing an entire module
#a module is a file ending in .py that contains the code you want to import into your program
#syntax import module_name


#importing specific function
#syntax from module_name import function_name
#you can as well import multiple functions from a module by separating each function's name with a comma
#syntax from module_name import function_0, function_1, function_2


