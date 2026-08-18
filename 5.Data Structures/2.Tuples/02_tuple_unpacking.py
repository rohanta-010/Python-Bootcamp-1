###Tuple Unpacking

# Unpacking means assigning the individual values of a tuple to separate variables.
#
## Example:

print("Default unpacking: ")
tu = (3, 2, 45)
a, b, c = tu
# Python assigns:
# a = 3
# b = 2
# c = 45
print(a,b,c)

# The number of variables must normally match the number of values in the tuple. Here 3 values → 3 variables
# If the numbers don't match, Python raises ValueError.



## Extended unpacking:
#
print("\nDefault unpacking: ")
a, *b = tu
# Python assigns:
# a = 3
# b = [2, 45]
print(a,b)

# * means "collect the remaining values".