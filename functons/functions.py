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


