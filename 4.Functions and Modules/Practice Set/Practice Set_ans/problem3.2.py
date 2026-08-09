square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]

print(list(map(square, list1)))

### map() with lambda
#
# map() applies a function to every item in an iterable.
#
## Syntax:
# map(function, iterable)
#
# lambda x: x ** 2
#     ↑       ↑
#   input   square the input
#
## Example:
# numbers = [1, 2, 3, 4, 5]
#
# squares = list(map(lambda x: x ** 2, numbers))
#
# Output:
# [1, 4, 9, 16, 25]
#
# In Python 3, map() returns a map object (iterator),
# so we use list() when we want to see/store all the results as a list.