#import module_name
import greetings
greetings.greet('Alice')

#from module_name import function_name
from greetings import greet
greet('Bob')

#from module_name import function_name as fn
from greetings import greet as gr
gr('Charlie')

#import module_name as mn
import greetings as g
g.greet('Dave')

#from module_name import *
from greetings import *
greet('Eve')