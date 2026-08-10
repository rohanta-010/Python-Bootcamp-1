## Two types of modules in Python: 
# - Built in Modules 
# - External Modules
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html

import math 
import os  # unused import so the color of the import statement is dark blue. It means that the module is imported but not used in the code.
import mymodule # created a module named mymodule.py in the same directory as this file. So, we can import it and use it in this file.


### __pycache__ and .pyc files
#
# When Python imports a Python source module, it may create a __pycache__ folder containing .pyc (compiled bytecode) files.
#
## example, if we have:
#
#     mymodule.py
#
# and write:
#
#     import mymodule
#
# Python may create:
#
#     __pycache__/mymodule.cpython-314.pyc
#
# The location of __pycache__ depends on where the imported module is located. 
# __pycache__ = folder used to store cached .pyc files.
# .pyc = compiled Python bytecode file.
#
# These files are automatically generated and should not normally be committed to Git.

import requests 
# "requests" is an external module which is used to make HTTP requests.

print(math.sqrt(16))
 # here math is a built in module and sqrt is a function in the math module which returns the square root of a number. And "math." is used to access the function in the module.

mymodule.hello() # here mymodule is a module created by me and hello is a function in the mymodule module which prints "Hello Rohan from mymodule.py!" when called. And "mymodule." is used to access the function in the module.

r = requests.get("https://www.google.com")
# get() is a function in the requests module which is used to make a GET request to the specified URL. And "requests." is used to access the function in the module. With the help of requests module we can make HTTP requests to any website and get the response from the website. The response is stored in the variable "r". We can access the response content using r.text which will give us the HTML content of the website.

print(r.text)