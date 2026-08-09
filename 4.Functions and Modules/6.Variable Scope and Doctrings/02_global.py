# "global" keyword is used to modify a global variable inside a function

def sum(a, b):
    print("Hey I am summing ")
    c = a + b
    global z # Please modify global z
    z = 0 # This will refer to global z and not create a local variable, changing the value of global z to 0
    return c 

z = 3
print(sum(3, 12))
print(z) # here z is 0 because we modified the global variable z = 3 in the sum function