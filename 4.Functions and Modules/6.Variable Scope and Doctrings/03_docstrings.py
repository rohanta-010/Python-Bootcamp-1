# "docstring" is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object. Without docstrings, it is difficult to understand the purpose of a function or a module. Docstrings are used to document the code and provide information about the functionality of the code.


def sum(a, b): 
    '''This function is used to sum two numbers'''
    c = a + b  
    return c

print(sum.__doc__)