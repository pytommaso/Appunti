
# FUNCTION TEMPLATE

def function(a,b, c=0, *args):
        '''explaination'''
        pass

function(required/positional_argument, default_2 = 0,
         default_1 = 'string', *args, **kwargs)
*args = arbitrary number of arguments               # returns a tuple
*kwargs = arbitrary number of keyword arguments     # returns a dictionary

help(function) => "explaination"


# *args   **kwargs
def myfunc(*args):
    print(args)         # returns a tuple
myfunc(3,'ciao',44)

def myfunc2(**kwargs):
    print(kwargs)       # returns a dictionary
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit')
myfunc2(fruit = 'apple', veggie = 'lettuce')
