sentence = "Coding in Python is fun"

ind = sentence.index("Python") 
ind = sentence.find("Python") 

#index and find are similar methods used to locate the position of a substring within a string, but they have some differences. The index method raises a ValueError if the substring is not found, while the find method returns -1 in such cases.
print(ind)