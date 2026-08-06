# a = 4
# b = 2
# c = 1

# average = (a + b + c)/3.0
# print(average)

# a1 = 6
# b1 = 7
# c1 = 12

# average1 = (a1 + b1 + c1)/3
# print(average1)


def average(a, b, c): # these values are called "parameters" of the function average
    d = (a + b + c)/3.0
    # print(d)
    return d  # without return statement, the function will return None by default

o1 = average(3, 5, 1) # we use the return value of the function and store it in a variable o1
o2 = average(4, 2, 1) # these values are passed as "arguments" to the function average

print(o1)
print(o2)