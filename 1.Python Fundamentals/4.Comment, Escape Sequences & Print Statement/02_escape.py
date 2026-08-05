from ast import arguments

'''ast.arguments is not related to Python function arguments directly. It is a class used by the ast module to represent function parameters while analyzing Python code, not while executing it.'''

## from ast import arguments
 ---------------------------------------------
# Imports the 'arguments' class from Python's built-in ast module.

# ast = Abstract Syntax Tree
# Used to analyze Python source code, NOT to execute it.

# 'arguments' represents function parameters in the AST.

# Example:
# def add(a, b):
#     return a + b

## AST:
# FunctionDef
# └── arguments
#     ├── a
#     └── b


## Commonly used in:
# - Linters (Pylint)
# - Formatters (Black)
# - IDEs (VS Code, PyCharm)
# - Code analyzers
# - AI code assistants

# Not needed for normal Python programs unless working with AST.


print("Hey how are you\nI am good\\newline")

print("Hello \" World")

# print() automatically inserts a space between multiple arguments, not "within the arguments."

print('Hello World',"Harry",5) 
'''Here, the print() function takes three arguments: 'Hello World', 'Harry', and 5. It will print them with a space in between each argument. assuming the default separator is a space.
ie sep=" " and end="\n" (newline character) by default.'''

print('Hello World',"Harry",5, sep="/")
print('Hello World', end="..")
print('Harry', end="//")