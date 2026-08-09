def add(a, b, plus=0):
    # a and b are required parameters.
    #
    # plus is a parameter with a default value of 0.
    # If we don't provide a value for plus, Python uses 0.
    # If we provide a value for plus, that value replaces the default.
    #
    # Example:
    # add(10, 20)       → a=10, b=20, plus=0
    # add(10, 20, 5)    → a=10, b=20, plus=5
    #
    ### Positional arguments:
    # Arguments are called "positional arguments" when Python matches them to parameters based on their position/order.
    #
    ## Example:
    # add(10, 20, 5)
    #
    # 10 → a  (1st position)
    # 20 → b  (2nd position)
    # 5  → plus (3rd position)
    #
    # Therefore, the order of positional arguments matters.
    #
    ## Example:
    # add(10, 20, 5)  → a=10, b=20, plus=5
    # add(20, 10, 5)  → a=20, b=10, plus=5
    
    x = a + b + plus
    return x


c = add(3, 5, 2) # uses 2 instaed of the default value of 0 for the parameter plus
print(c) 

c1 = add(b=5, a=3) # uses the default value of 0 for the parameter plus, because we didn't provide a value for it
print(c1)
