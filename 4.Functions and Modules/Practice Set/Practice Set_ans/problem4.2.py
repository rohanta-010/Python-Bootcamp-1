def sum_of_digits(n):
    if n == 0:
        return 0
    
    return (n%10) + sum_of_digits(n//10)

print(sum_of_digits(1234))

### Recursive function to find the sum of digits
#
## Example:
# 1234 → 1 + 2 + 3 + 4 = 10
#
# n % 10 → gets the last digit
# n // 10 → removes the last digit
#
#
# 1234 % 10 = 4
# 1234 // 10 = 123
#
# Base case:
# if n == 0:
#     return 0
#
# The base case stops the recursion when there are
# no more digits left.
#
# Recursive step:
# return (n % 10) + sum_of_digits(n // 10)
#
# Example:
# sum_of_digits(1234)
# = 4 + sum_of_digits(123)
# = 4 + 3 + sum_of_digits(12)
# = 4 + 3 + 2 + sum_of_digits(1)
# = 4 + 3 + 2 + 1 + sum_of_digits(0)
# = 10

# everytime (n%10) values are added to the sum, but here the sum is not stored in a variable, instead it is returned to the previous function call. So, the sum is calculated in the return statement itself. Previous function call is waiting for the return value of the current function call. When the current function call returns, the previous function call adds the returned value to its own (n%10) value and returns it to its previous function call. This process continues until the base case is reached and the final sum is returned to the original function call.