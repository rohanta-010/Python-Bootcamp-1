sentence = "Coding in Python is fun"

# print(sentence.count("a","e","i","o","u")) 
# This line will raise an error because the count method only takes one argument, which is the substring to count.

# Method 1: Using the count method for each vowel separately
print(sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u")) 
# This line will correctly count the number of vowels in the sentence.

# Method 2: Using a loop to count vowels
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence.lower(): 
    if(char in vowels):
        sum += 1

print(f"There are {sum} vowels in this sentence")