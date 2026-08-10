def factorial(n):
    if n == 0 or n== 1:
        return 1
    return factorial(n - 1) * n

print(factorial(4))

# example: factorial(4) = factorial(3) * 4 = factorial(2) * 3 * 4 = factorial(1) * 2 * 3 * 4 = 1 * 2 * 3 * 4 = 24