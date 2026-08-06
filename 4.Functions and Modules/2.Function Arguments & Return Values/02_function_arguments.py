def add(a, b, plus=0): 
    # here plus is a default argument, if we don't pass any value for plus, it will take the default value 0. But in case we pass a value for plus, it will take that value instead of the default value. 
    # "Postional arguments" are those which are passed after the positional arguments. In this case, plus is a positional argument because it is passed after the positional arguments a and b.
    
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)