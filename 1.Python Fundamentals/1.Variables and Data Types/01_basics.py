# In Python, variables are used to store data that can be used and manipulated throughout a program. A variable is created the moment you assign a value to it using the assignment operator (=).

age = 34 # integer
name = "Harry" # string
cgpa = 4.55 # float

# Rule of defining a variable in Python  
# Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# They can contain letters, numbers, and underscores.
# Variable names are case-sensitive (age and Age are different).
# Avoid using Python keywords (e.g., if, for, while) as variable names.

# 34age = 4 # Invalid because variable cannot start with a number
age = 32 # Valid because variable can start with a number 
# a$$ge = 45 # Invlaid because variables cannot contain special characters other than _
__age = 34
__nice_45 = 34
a_b_c_7 = "Sam"


# Every Python program is loaded into (RAM)memory before execution(i.e line by line), and variables are references to objects stored in memory.
## x = 10
# Python does not simply store x as a box containing 10. Instead:
# 10 is created as an object in memory
# x becomes a reference (name) pointing to that object