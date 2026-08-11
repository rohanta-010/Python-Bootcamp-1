a = (3, 2, 22, 13)

print(a)
print(a[2])
a[3] = 32 # TypeError: 'tuple' object does not support item assignment

b = (3, ) # This is a tuple with a single element. The comma is necessary to distinguish it from a regular parenthesis.