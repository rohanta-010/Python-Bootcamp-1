marks = {"harry": 34, "jack": 45, "lily": 94 }

print(marks.keys())
print(marks.values())
# marks.clear()
marks.pop("lily")
print(marks)


# ============================================================
# PYTHON Dictionary METHODS
# ============================================================


## 1. update() → Update the dictionary IN-PLACE with specified key-value pairs
    # --> dict.update([other], **kwargs)
    # TRAP: Returns None! It does NOT return a new dictionary; it mutates the calling dictionary directly in-place.
    
    # THE OVERWRITE RULE: 
    # If a key already exists, its value is overwritten with the new value.
    # If a key does NOT exist, the key-value pair is inserted into the dictionary.
    
    # FLEXIBILITY (3 Input Formats):
    # 1. Another Dictionary: my_dict.update({'c': 3})
    # 2. Iterable of 2-Element Sequences: List/tuple of pairs like [('c', 3)] or (('c', 3),)
    # 3. Keyword Arguments (**kwargs): my_dict.update(c=3, d=4)
    
    # THE KWARGS TRAP: Keyword argument syntax (c=3) ONLY works if the keys are valid Python identifier strings.
    # You CANNOT use kwargs for integer keys (99=3) or tuple keys ((1,2)=3) for those, you must pass a dict or list of tuples.

my_dict = {'a': 1, 'b': 2}

# Format 1: Passing another dictionary
my_dict.update({'b': 99, 'c': 3}) 
print(my_dict) # Output: {'a': 1, 'b': 99, 'c': 3} , value of key "b" got updated

# Format 2: Passing an iterable of key-value pairs (tuples/lists)
my_dict.update([('d', 4), ('e', 5)])
print(my_dict) # Output: {'a': 1, 'b': 99, 'c': 3, 'd': 4, 'e': 5}

# Format 3: Passing keyword arguments (**kwargs)
my_dict.update(f=6, g=7)
print(my_dict) # Output: {'a': 1, 'b': 99, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

# ---------------------------------------------------------
# THE TRAPS IN ACTION
# ---------------------------------------------------------

# The None Return Trap:
result = my_dict.update({'a': 100})
print(result) # Output: None (Do NOT assign the result of update to a variable!)

# The Kwargs Trap (Non-string keys crash with kwargs):
# my_dict.update(100=200) # SyntaxError: expression cannot contain assignment
# my_dict.update({100: 200}) # Valid! Use dict syntax for numeric keys.


## 2. setdefault() → Return a key's value, or INSERT it with a default if missing
    # --> dict.setdefault(key, [default_value])
    # TRAP (The Naming Trap): Unlike update(), clear(), or other mutation methods, setdefault() does NOT return None. 
    # It always evaluates to the value of the key, making it safe to assign to a variable.
    
    # THE BEHAVIOR:
    # 1. If the key EXISTS: It simply returns the current value (and completely ignores the default_value).
    # 2. If the key is MISSING: It inserts the key into the dictionary with the default_value, and then returns that default_value.
    
    # THE ARGUMENT RULE: If no default_value is provided, it safely defaults to None.
    
    # EXPERT TIP (Grouping Data): setdefault() is the absolute best way to build a dictionary of lists. 
    # Instead of writing an 'if/else' block to check if a list exists before appending to it, setdefault() handles the creation and retrieval in one lightning-fast step!

my_dict = {'a': 1}

# Scenario 1: Key exists
val1 = my_dict.setdefault('a', 100) 
print(val1) # Output: 1 (The existing value is returned; 100 is ignored)

# Scenario 2: Key is missing
val2 = my_dict.setdefault('b', 200) 
print(val2) # Output: 200 (The key 'b' was created with value 200)

print(my_dict) # Output: {'a': 1, 'b': 200}

# Scenario 3: Missing default_value argument
val3 = my_dict.setdefault('c')
print(val3)    # Output: None
print(my_dict) # Output: {'a': 1, 'b': 200, 'c': None}

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Grouping items into lists
# ---------------------------------------------------------
# Let's say we want to group words by their first letter:
words = ["apple", "ant", "bat", "bear", "cat"]
grouped = {}

for word in words:
    first_letter = word[0]
    # If the letter doesn't exist, create an empty list [] and return the list.
    # Then immediately append the word to that list! i.e [].append("apple")
    grouped.setdefault(first_letter, []).append(word)

print(grouped)
# Output: {'a': ['apple', 'ant'], 'b': ['bat', 'bear'], 'c': ['cat']}

## setdefault() is useful when you want to GET a value if it exists, or CREATE a default value if it doesn't and then you can immediately work with the returned value.

# the mormal way 
words = ["apple", "ant", "bat", "bear", "cat"]
grouped = {}

for word in words:
    first_letter = word[0]

    if first_letter not in grouped:
        grouped[first_letter] = []

    grouped[first_letter].append(word)


## 3. pop() → Remove a specified key and return its value
    # --> dict.pop(key, [default_value])
    # THE BEHAVIOR: It extracts a specific key-value pair, deleting it from the dictionary while evaluating to its value.
    
    # TRAP (The KeyError): 
    # If the key is MISSING and no default_value is provided, the program crashes with a KeyError.
    
    # THE SAFE FALLBACK: 
    # If the key is MISSING but a default_value IS provided, it safely returns that default_value instead of crashing. (The dictionary remains unchanged).
    
    # EXPERT TIP (pop() vs del): 
    # Why use pop() instead of `del my_dict['a']`? Two huge reasons: 
    # 1) pop() gives you the value back so you can assign it or use it immediately. 
    # 2) pop() lets you provide a default fallback to gracefully handle missing keys, whereas `del` will ALWAYS crash if the key is missing!

my_dict = {'a': 1, 'b': 2}

# Scenario 1: Key exists
val = my_dict.pop('a') 
print(val)     # Output: 1 (The value is extracted and saved)
print(my_dict) # Output: {'b': 2} (The key 'a' is gone)

# ---------------------------------------------------------
# THE TRAPS IN ACTION
# ---------------------------------------------------------

# Scenario 2: Key missing (No default fallback)
# print(my_dict.pop('c')) # ❌ KeyError: 'c'

# Scenario 3: Key missing (WITH default fallback)
safe_val = my_dict.pop('c', 'Not Found') 
print(safe_val) # ✅ Valid! Output: 'Not Found' (Safe fallback!)

# Proof the dictionary didn't crash and wasn't altered:
print(my_dict) # Output: {'b': 2}


## 4. popitem() → Remove and return the LAST inserted key-value pair (LIFO order)
    # --> dict.popitem()
    # THE BEHAVIOR: Removes and returns the most recently added key-value pair as a 2-element tuple: (key, value).
    # (Since Python 3.7+, dictionaries officially maintain insertion order, making popitem() operate strictly in LIFO—Last-In, First-Out—order).
    
    # THE ARGUMENT TRAP: Accepts strictly ZERO arguments. Passing anything raises a TypeError.
    
    # THE EMPTY DICTIONARY TRAP: Calling popitem() on an empty dictionary raises a KeyError.
    
    # EXPERT TIP (Tuple Unpacking): 
    # Because popitem() returns a tuple, you can unpack the key and value directly into separate variables in a single line: `key, val = my_dict.popitem()`.

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Standard usage: returns a (key, value) tuple
last_item = my_dict.popitem() 
print(last_item) # Output: ('c', 3)
print(my_dict)   # Output: {'a': 1, 'b': 2}

# Tuple Unpacking in Action
k, v = my_dict.popitem()
print(f"Key: {k}, Value: {v}") # Output: Key: b, Value: 2
print(my_dict)                 # Output: {'a': 1}

# ---------------------------------------------------------
# THE ERROR TRAPS IN ACTION
# ---------------------------------------------------------

# The Argument Trap:
# my_dict.popitem('a') # TypeError: popitem() takes no arguments (1 given)

# The Empty Dictionary Trap:
empty_dict = {}
# empty_dict.popitem() # KeyError: 'popitem(): dictionary is empty'


## 5. clear() → Remove all items, emptying the dictionary IN-PLACE
    # --> dict.clear()
    # TRAP: Returns None! It does NOT evaluate to a new empty dictionary; it mutates the calling dictionary directly in-place.
    
    # THE ARGUMENT TRAP: Accepts strictly ZERO arguments. Passing anything raises a TypeError.
    
    # EXPERT TIP (clear() vs {}): 
    # Using .clear() physically empties the ACTUAL dictionary object in memory. If other variables are pointing to this dictionary, they will all instantly become empty. 
    # Conversely, writing `my_dict = {}` just points that specific label to a brand NEW empty dictionary, leaving the original data intact for any other variables still pointing to it!

my_dict = {'a': 1, 'b': 2}
my_dict.clear()

print(my_dict) # Output: {}

# The None Return Trap:
result = my_dict.clear()
print(result) # Output: None (Do NOT assign the result of an update method to a variable!)

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Memory References
# ---------------------------------------------------------

dict_A = {'x': 100, 'y': 200}
dict_B = dict_A  # Both labels point to the exact same warehouse box in memory

# Using .clear() empties the box itself!
dict_A.clear()   

print(dict_A) # Output: {}
print(dict_B) # Output: {} (dict_B is also empty because the shared data was wiped!)

# Contrast with Reassignment (=):
dict_C = {'z': 300}
dict_D = dict_C

# This doesn't empty the box; it just points dict_C to a NEW, empty box.
dict_C = {}   

print(dict_C) # Output: {}
print(dict_D) # Output: {'z': 300} (dict_D still points to the original, untouched data!)


## 6. get() → Return the value for a specified key (Safe Lookup)
    # --> dict.get(key, [default_value])
    # THE BEHAVIOR: Retrieves the value associated with the specified key.
    
    # TRAP (Strict Lookup vs. Safe Lookup): 
    # Using square brackets (e.g., my_dict['c']) is a "Strict Lookup". If the key is missing, your program crashes immediately with a KeyError.
    # Using .get() is a "Safe Lookup". It NEVER raises a KeyError!
    
    # DEFAULT RULES:
    # 1. If the key EXISTS: It returns the actual value.
    # 2. If the key is MISSING (No default provided): It safely evaluates to None.
    # 3. If the key is MISSING (Default provided): It safely evaluates to the default_value.
    
    # EXPERT TIP (When to use which?): 
    # Use .get() when you are dealing with unpredictable data (like web APIs or user inputs) where missing keys are expected.
    # Use [] when a missing key means there is a fatal flaw in your logic, and you WANT the program to "fail fast" and crash so you can fix the bug.

my_dict = {'a': 1, 'b': 2}

# Scenario 1: Key exists
print(my_dict.get('a'))              # Output: 1

# Scenario 2: Key is missing (Defaults to None)
print(my_dict.get('c'))              # Output: None

# Scenario 3: Key is missing (Custom fallback provided)
print(my_dict.get('c', 'Missing!'))  # Output: 'Missing!'

# ---------------------------------------------------------
# THE STRICT VS SAFE TRAP IN ACTION
# ---------------------------------------------------------

# Strict Lookup (Crashes!):
# print(my_dict['c']) # KeyError: 'c'

# Safe Lookup (Graceful fallback):
user_profile = {"name": "Harry"}
age = user_profile.get("age", "Age not provided")
print(age) # Valid! Output: 'Age not provided'


## 7. keys() → Return a dynamic view object containing all dictionary keys.
    # --> dict.keys()
    # Returns a 'dict_keys' view object. 
    # DYNAMIC VIEW: If the original dictionary changes, the view object reflects the change instantly!
    # It is iterable (you can loop over it), but it is NOT a standard list. To use list methods, wrap it like this: list(my_dict.keys()).

my_dict = {'a': 1, 'b': 2}

keys = my_dict.keys()

print(keys)
# Output: dict_keys(['a', 'b'])

print(type(keys))
# Output: <class 'dict_keys'>

# It is iterable:
for key in keys:
    print(key)

# Convert to a real list:
keys_list = list(keys)

print(keys_list)
# Output: ['a', 'b']

print(type(keys_list))
# Output: <class 'list'>


## 8. values() → Return a view object displaying a list of all values
    # --> dict.values()
    # Returns a 'dict_values' view object containing just the values.
    # Just like keys(), it updates dynamically if the original dictionary changes.

my_dict = {'a': 1, 'b': 2}
print(my_dict.values()) # Output: dict_values([1, 2])


## 9. items() → Return a view object of all key-value pairs as tuples
    # --> dict.items()
    # Returns a 'dict_items' view object where each item is a tuple: (key, value).
    # EXPERT TIP: This is the #1 most common method used when iterating through a dictionary in a for loop!

my_dict = {'a': 1, 'b': 2}
print(my_dict.items()) # Output: dict_items([('a', 1), ('b', 2)])

# Typical real-world usage:
# for key, value in my_dict.items():
#     print(f"Key: {key} holds Value: {value}")


## 10. fromkeys() → Create a NEW dictionary from an iterable of keys
    # --> dict.fromkeys(iterable, default_value)
    # NOTE: This is a class method. You call it directly on the 'dict' keyword, not on an existing dictionary.
    # It takes an iterable (like a list or tuple of strings) and assigns EVERY key the exact same default_value.
    # If no default_value is provided, all keys are assigned None.
    # TRAP: If the default_value is mutable (like an empty list []), ALL keys will point to the EXACT SAME list in memory!

keys_list = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys_list, 0)

print(new_dict) # Output: {'a': 0, 'b': 0, 'c': 0}

## Real-World Use Cases for dict.fromkeys()

# -------------------------------------------------------------------------
# USE CASE 1: Deduplicating a list while PRESERVING original order
# -------------------------------------------------------------------------
    # TRAP: Using list(set(my_list)) removes duplicates BUT scrambles the original item order.
    # Because Python 3.7+ dictionaries maintain insertion order, dict.fromkeys() 
    # removes duplicates AND keeps the original sequence intact.

raw_tags = ['python', 'code', 'python', 'django', 'code', 'api']

# Using set() -> Duplicates removed, BUT order is lost:
print(list(set(raw_tags))) # Output: ['api', 'django', 'code', 'python'] (Order scrambled!)

# Using dict.fromkeys() -> Duplicates removed AND original order preserved:
clean_tags = list(dict.fromkeys(raw_tags))
print(clean_tags) # Output: ['python', 'code', 'django', 'api']


# -------------------------------------------------------------------------
# USE CASE 2: Batch initializing default statuses, flags, or counters
# -------------------------------------------------------------------------
    # When initializing system monitoring, task queues, or default user settings,
    # dict.fromkeys() sets a collection of keys to the exact same default value in a single line.

servers = ['server_alpha', 'server_beta', 'server_gamma']

# Batch setting all servers to an initial "Offline" status
server_status = dict.fromkeys(servers, "Offline")

print(server_status) 
# Output: {'server_alpha': 'Offline', 'server_beta': 'Offline', 'server_gamma': 'Offline'}


# -------------------------------------------------------------------------
# USE CASE 3: Building fast O(1) membership lookup tables
# -------------------------------------------------------------------------
    # Converting a list of items (e.g., forbidden words, allowed IDs) into dictionary keys 
    # allows lightning-fast O(1) constant time lookups via hash values instead of scanning a list.

forbidden_words = ['spam', 'scam', 'phishing', 'malware']

# Convert list to dict keys with a dummy True value
blacklisted = dict.fromkeys(forbidden_words, True)

user_input = "scam"

# Checking key existence in a dictionary is practically instantaneous
if blacklisted.get(user_input):
    print("Blocked!") # Output: Blocked!


## 11. copy() → Return a shallow copy of the dictionary
    # --> dict.copy()
    # Returns a completely new, independent dictionary with the exact same key-value pairs.
    # It takes NO arguments.
    # Independence: Modifying the outer structure (adding/removing keys) of the copy does NOT affect the original, and vice versa.

original = {'a': 1, 'b': 2}
my_copy = original.copy()

# Modifying only the copy
my_copy['c'] = 3 

print(original) # Output: {'a': 1, 'b': 2} (Original remains untouched!)
print(my_copy)  # Output: {'a': 1, 'b': 2, 'c': 3}


## 12. dict() → Create a new dictionary object
    # --> dict(iterable/kwargs)
    # NOTE: dict() is a built-in Python type constructor, not a method on an existing dictionary.
    # Calling dict() with no arguments creates an empty dictionary {}.
    # You can pass keyword arguments (dict(a=1, b=2)) or an iterable of pairs (dict([('a', 1), ('b', 2)])).
    # TRAP: If you use keyword arguments, the keys must be valid Python variable names (you can't do dict(1='a')).

empty_dict = dict() 
print(empty_dict) # Output: {}

# Converting a list of tuples into a dictionary
pairs = [('x', 10), ('y', 20)]
new_dict = dict(pairs)
print(new_dict) # Output: {'x': 10, 'y': 20}


## 13. len() → Return the total number of key-value pairs in the dictionary
    # --> len(dict)
    # NOTE: len() is a built-in function, so we don't use dot notation.
    # If the dictionary is empty, it returns 0.
    # It counts the number of PAIRS, not the total number of individual keys and values combined.

my_dict = {'a': 1, 'b': 2, 'c': 3}
length = len(my_dict) 

print(length) # Output: 3


## 14. del → Delete a specific key, or delete the entire variable from memory
    # --> del dict_variable[key]  OR  del dict_variable
    # KEYWORD vs FUNCTION: `del` is a built-in Python statement/keyword, NOT a function (no parentheses).
    # If you use it with a key (del my_dict['a']), it removes that specific key-value pair.
    # TRAP: If you try to delete a key that does not exist, it raises a KeyError. (Use .pop() if you want a safe fallback!)
    # If you use it on the whole variable (del my_dict), it completely destroys the dictionary from memory.

my_dict = {'a': 1, 'b': 2}

# Deleting a specific key
del my_dict['a']
print(my_dict) # Output: {'b': 2}

# Deleting the entire variable
del my_dict
# print(my_dict) # ---> NameError: name 'my_dict' is not defined


## 15. in / not in → Return True if a KEY is present or missing in the dictionary
    # --> key in dict
    # TRAP: These operators ONLY check the dictionary's KEYS. They do NOT search the values!
    # If the dictionary is empty, 'in' safely returns False, and 'not in' safely returns True.
    # EXPERT TIP: Just like sets, dictionaries use hash values (the warehouse trick). Checking if a key exists using 'in' is incredibly fast (O(1) lookup time), even if the dictionary has millions of items!

my_dict = {'a': 1, 'b': 2}

# Checking Keys
print('a' in my_dict)      # Output: True
print('z' not in my_dict)  # Output: True

# The Trap: Checking Values
print(1 in my_dict)        # Output: False (1 is a value, but 'in' only looks at keys!)

# If you actually need to check if a VALUE exists, you must use .values():
print(1 in my_dict.values()) # Output: True
