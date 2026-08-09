# "lambda" is a keyword in Python that is used to create anonymous functions. These functions are also known as lambda functions. Lambda functions can take any number of arguments but can only have one expression. The expression is evaluated and returned.
square = lambda x: x*x 
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x, y: x+y
'''
As good as writing
def sum(x, y):
    return x + y
'''

print(square(3)) # here we are calling the lambda function square with the argument 3 i.e x, which will return 9.
print(sum(3, 62)) # here we are calling the lambda function sum with the arguments 3 and 62 i.e x and y, which will return 65.