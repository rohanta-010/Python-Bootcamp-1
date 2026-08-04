from ast import arguments


print("Hey how are you\nI am good\\newline")

print("Hello \" World")

# print() automatically inserts a space between multiple arguments, not "within the arguments."

print('Hello World',"Harry",5) 
'''Here, the print() function takes three arguments: 'Hello World', 'Harry', and 5. It will print them with a space in between each argument. assuming the default separator is a space.
ie sep=" " and end="\n" (newline character) by default.'''

print('Hello World',"Harry",5, sep="/")
print('Hello World', end="..")
print('Harry', end="//")