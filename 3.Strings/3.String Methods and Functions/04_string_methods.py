s = "hello world" # Strings are immutable, original strings values are not changed but just added new strings.

# s[0] = "R" # You cannot do this : TypeError: 'str' object does not support item assignment

a = len(s)
print(a)
print(s.upper(), s)
print(s.lower())
print(s.capitalize()) # first letter of the string is capitalized
print(s.title()) # first letter of each word is capitalized

print("\n") 

text = " hello world "
# whitespace is blank space, tab space, new line etc.
print(text.strip()) # Output: "hello world"  ## removes leading and trailing spaces
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"

print("\n")

text = "Python is fun and fun and fun"

print(text.find("is")) # Output: 7 Index of first occurence
print(text.replace("fun", "awesome")) 

print("\n")

text = "Apples,Bananas,Pineapples"
print(text.split(",")) # when you split a string, it returns a list of strings. The string is split at the specified separator (in this case, a comma).
print(",".join(['Apples', 'Bananas', 'Pineapples'])) # when you join a list of strings, it returns a single string. The strings are joined together with the specified separator (in this case, a comma).

print("\n")

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False