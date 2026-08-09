str1 = "123abc"
print(str1.isalnum) 
# without parentheses, it will print the method object itself, not the result of the method call. To get the actual result, you need to call the method with parentheses like this: str1.isalnum().
# Output:
#         <built-in method isalnum of str object at 0x...>
#         (The memory address will be different on every run.)

print(str1.isalnum())  # This will print True if the string is alphanumeric, otherwise False.

if str1.isalnum():
    print("Yes this string is alphanumeric")

else:
    print("This string is not alphanumeric")

