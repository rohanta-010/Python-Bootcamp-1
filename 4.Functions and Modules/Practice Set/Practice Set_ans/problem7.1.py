def fibonacci(n):
    '''
    Print the first n Fibonacci numbers using recursion.
    '''
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    for i in range(n): # this loop will run n times and will call the fib function for each value of i from 0 to n-1. It will print the first n Fibonacci numbers.
        print(fib(i), end=" ")

# Example usage
fibonacci(10)   # Prints: 0 1 1 2 3 5 8 13 21 34
