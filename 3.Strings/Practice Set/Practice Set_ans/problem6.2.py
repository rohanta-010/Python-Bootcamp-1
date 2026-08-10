string1 = "45554"

## Method 1: Using slicing
if(string1 == string1[::-1]):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")

## Method 2: Using a loop
is_palindrome = True        

for i in range(len(string1) // 2): # here we only need to iterate through half of the string because we are comparing characters from the start and end of the string moving towards the center.
   ##  Reason:
   # - Remaining comparisons would be duplicates.
   # - Middle character (if any) doesn't need comparison.
    if string1[i] != string1[len(string1) - 1 - i]:
        is_palindrome = False
        break       
if is_palindrome:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome") 
