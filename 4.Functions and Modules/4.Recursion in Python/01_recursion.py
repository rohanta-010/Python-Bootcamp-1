''' 
 values:  0 1 1 2 3 5 8 13
 indices: 0 1 2 3 4 5 6.....

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)

'''

def fib(n):
    ## Base case of recursion
    # Base case = the condition that stops recursion; without it, recursive calls continue until Python reaches its recursion limit.
    # RecursionError: maximum recursion depth exceeded
    # If no base case is defined, the recursion will go on infinitely and will result in a stack overflow error. 
    # For example: fib(4) = fib(2) + fib(3) = fib(0) + fib(1) + fib(1) + fib(2) = fib(-2) + fib(-1) + fib(-1) + fib(0) + fib(-1) + fib(0) + fib(0) + fib(1). 
    if(n == 0 or n == 1):
        return n

    return fib(n-2) + fib(n-1)

print(fib(6))


fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0      +   1    + fib(1) + fib(2) + fib(3) + fib(4)
0      +   1    +   1    + fib(0) + fib(1) + fib(1) + fib(2)+ fib(4)
0      +   1    +   1    +   0    +   1    +   1    + fib(0) + fib(1) + fib(2) + fib(3)
0      +   1    +   1    +   0    +   1    +   1    +   0    +   1    + fib(0) + fib(1) + fib(3)
0      +   1    +   1    +   0    +   1    +   1    +   0    +   1    +   0    +   1    + fib(1) + fib(2)
0      +   1    +   1    +   0    +   1    +   1    +   0    +   1    +   0    +   1    +   1    + fib(0) + fib(1)
0      +   1    +   1    +   0    +   1    +   1    +   0    +   1    +   0    +   1    +   1    +   0    +   1