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


## 7. keys() → Return a dynamic view object containing all dictionary keys
    # --> dict.keys()
    # THE BEHAVIOR: Returns a `dict_keys` view object containing all the keys in the dictionary.
    
    # TRAP (The Index Trap): A view object is iterable (you can loop over it), but it is NOT a list. 
    # Attempting to access an index directly (e.g., keys[0]) raises a TypeError. 
    # To use indexing or list methods, you MUST wrap it: list(my_dict.keys()).
    
    # EXPERT TIP (The "Live Window"): A view object is dynamic, not a static copy. 
    # It acts as a "live window" into the dictionary. If the original dictionary changes, the view object reflects that change instantly!
    
    # EXPERT TIP (Set Operations): Because dictionary keys are guaranteed to be unique and hashable, `dict_keys` objects actually support Set operations (like &, |, -, ^)!

my_dict = {'a': 1, 'b': 2}
keys = my_dict.keys()

print(keys)       # Output: dict_keys(['a', 'b'])
print(type(keys)) # Output: <class 'dict_keys'>

# 1. It is iterable:
for key in keys:
    print(key)    # Prints 'a', then 'b'

# 2. Converting to a real list to enable indexing:
keys_list = list(keys)
print(keys_list)  # Output: ['a', 'b']

# ---------------------------------------------------------
# THE TRAPS & TIPS IN ACTION
# ---------------------------------------------------------

# The Index Trap:
# print(keys[0]) # TypeError: 'dict_keys' object is not subscriptable
print(keys_list[0]) # Valid! Output: 'a'

# Proof of the "Live Window" (Dynamic View):
print(keys) # Output: dict_keys(['a', 'b'])

my_dict['c'] = 3    # We mutate the dictionary AFTER creating the 'keys' variable
print(keys)         # Output: dict_keys(['a', 'b', 'c']) (The view updated automatically!)

# The Set Math Trick:
dict_A = {'x': 1, 'y': 2}
dict_B = {'y': 99, 'z': 100}

# Find common keys instantly using Set Intersection (&)
common_keys = dict_A.keys() & dict_B.keys()
print(common_keys) # Output: {'y'}


## 8. values() → Return a dynamic view object containing all dictionary values
    # --> dict.values()
    # THE BEHAVIOR: Returns a `dict_values` view object containing all the values in the dictionary.
    
    # TRAP (The Index Trap): Just like keys(), this view object is iterable but is NOT a list. 
    # Attempting to access an index directly (e.g., values[0]) raises a TypeError. 
    # To use indexing, you MUST wrap it: list(my_dict.values()).
    
    # EXPERT TIP (The "Live Window"): Exactly like keys(), this is a dynamic view. 
    # If the original dictionary changes, the view object reflects that change instantly!
    
    # TRAP (No Set Math!): Unlike dict_keys, dict_values do NOT support Set operations (&, |, etc.). 
    # Because dictionary values are allowed to be duplicates and unhashable (like lists), Python cannot treat them like Sets.

my_dict = {'a': 1, 'b': 2}
vals = my_dict.values()

print(vals)       # Output: dict_values([1, 2])
print(type(vals)) # Output: <class 'dict_values'>

# 1. It is iterable:
for v in vals:
    print(v)      # Prints 1, then 2

# 2. Converting to a real list to enable indexing:
vals_list = list(vals)
print(vals_list)  # Output: [1, 2]

# ---------------------------------------------------------
# THE TRAPS & TIPS IN ACTION
# ---------------------------------------------------------

# The Index Trap:
# print(vals[0]) # TypeError: 'dict_values' object is not subscriptable
print(vals_list[0]) # Valid! Output: 1

# Proof of the "Live Window" (Dynamic View):
print(vals) # Output: dict_values([1, 2])

my_dict['c'] = 3    # We mutate the dictionary AFTER creating the 'vals' variable
print(vals)         # Output: dict_values([1, 2, 3]) (The view updated automatically!)


## 9. items() → Return a dynamic view object of all key-value pairs as tuples
    # --> dict.items()
    # THE BEHAVIOR: Returns a `dict_items` view object where each element is a 2-item tuple: (key, value).
    
    # TRAP (The Index Trap): Just like keys() and values(), this is NOT a list. 
    # Attempting to access an index directly (e.g., pairs[0]) raises a TypeError. 
    # To use list indexing, you MUST wrap it: list(my_dict.items()).
    
    # EXPERT TIP (The "Live Window"): This is also a dynamic view. 
    # If the original dictionary changes, the view object reflects the new key-value pairs instantly!
    
    # EXPERT TIP (Tuple Unpacking): This is the #1 most common method used when iterating through a dictionary. 
    # Because it returns a tuple, you can "unpack" the key and the value directly into two separate variables right inside the `for` loop definition!

my_dict = {'a': 1, 'b': 2}
pairs = my_dict.items()

print(pairs)       # Output: dict_items([('a', 1), ('b', 2)])
print(type(pairs)) # Output: <class 'dict_items'>

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: The For-Loop
# ---------------------------------------------------------

# Typical real-world idiomatic usage:
for key, value in my_dict.items():
    print(f"Key: {key} holds Value: {value}")
    
# Output:
# Key: a holds Value: 1
# Key: b holds Value: 2

# ---------------------------------------------------------
# THE TRAPS IN ACTION
# ---------------------------------------------------------

# The Index Trap:
# print(pairs[0]) # TypeError: 'dict_items' object is not subscriptable

# Converting to a list safely enables indexing:
pairs_list = list(pairs)
print(pairs_list[0]) # Valid! Output: ('a', 1)

# Proof of the "Live Window" (Dynamic View):
print(pairs) # Output: dict_items([('a', 1), ('b', 2)])

my_dict['c'] = 3    # We mutate the dictionary AFTER creating the 'pairs' variable
print(pairs)        # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])


## 10. fromkeys() → Create a NEW dictionary from an iterable of keys
    # --> dict.fromkeys(iterable, [default_value])
    # THE CLASS METHOD RULE: You call this directly on the 'dict' keyword/class, NOT on an existing dictionary variable.
    # It takes an iterable (like a list or tuple) and creates a new dictionary, assigning EVERY key the exact same default_value.
    # If no default_value is provided, all keys safely default to None.
    
    # TRAP (The Mutable Default): If the default_value is a mutable object (like an empty list []), ALL keys will point to the EXACT SAME list in memory! Modifying one key's list will modify them all.

keys_list = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys_list, 0)

print(new_dict) # Output: {'a': 0, 'b': 0, 'c': 0}

# ---------------------------------------------------------
# THE MUTABLE DEFAULT TRAP IN ACTION
# ---------------------------------------------------------
# Let's say we want every key to start with an empty list...
trap_dict = dict.fromkeys(['x', 'y'], [])

# We append to 'x', expecting 'y' to remain empty:
trap_dict['x'].append(99)

# But because they share the same memory box, BOTH change!
print(trap_dict) # Output: {'x': [99], 'y': [99]}

# (Fix: Use dictionary comprehension instead: {k: [] for k in ['x', 'y']})

# =========================================================================
# EXPERT TIPS: Real-World Use Cases for dict.fromkeys()
# =========================================================================

# ---------------------------------------------------------
# USE CASE 1: Deduplicating a list while PRESERVING original order
# ---------------------------------------------------------
# TRAP: Using list(set(my_list)) removes duplicates BUT scrambles the original item order.
# Because Python 3.7+ dictionaries officially maintain insertion order, dict.fromkeys() 
# removes duplicates AND keeps the original sequence perfectly intact.

raw_tags = ['python', 'code', 'python', 'django', 'code', 'api']

# Using set() -> Duplicates removed, BUT order is lost:
print(list(set(raw_tags))) # Output: ['api', 'django', 'code', 'python'] (Scrambled!)

# Using dict.fromkeys() -> Duplicates removed AND original order preserved:
clean_tags = list(dict.fromkeys(raw_tags))
print(clean_tags) # Output: ['python', 'code', 'django', 'api']


# -------------------------------------------------------------------------
# USE CASE 2: Batch initializing default statuses, flags, or counters
# -------------------------------------------------------------------------
# When initializing system monitoring, task queues, or default user settings,
# dict.fromkeys() sets a collection of keys to the exact same state in a single line.

servers = ['server_alpha', 'server_beta', 'server_gamma']

# Batch setting all servers to an initial "Offline" status
server_status = dict.fromkeys(servers, "Offline")

print(server_status) 
# Output: {'server_alpha': 'Offline', 'server_beta': 'Offline', 'server_gamma': 'Offline'}


# -------------------------------------------------------------------------
# USE CASE 3: Building fast O(1) membership lookup tables
# -------------------------------------------------------------------------
# Converting a list of items (e.g., forbidden words, allowed IDs) into dictionary keys 
# allows lightning-fast O(1) constant time lookups via hash values (the warehouse trick) instead of slowly scanning a list.

forbidden_words = ['spam', 'scam', 'phishing', 'malware']

# Convert list to dict keys with a dummy True value
blacklisted = dict.fromkeys(forbidden_words, True)

user_input = "scam"

# Checking key existence in a dictionary is practically instantaneous
if blacklisted.get(user_input):
    print("Blocked!") # Output: Blocked!


## 11. copy() → Return a SHALLOW copy of the dictionary
    # --> dict.copy()
    # THE BEHAVIOR: Returns a completely new dictionary object initialized with the exact same key-value pairs.
    # THE ARGUMENT RULE: Accepts strictly ZERO arguments.
    
    # THE INDEPENDENCE RULE (Outer Structure): Adding, removing, or overwriting keys in the new dictionary does NOT affect the original dictionary.
    
    # TRAP (The Shallow Copy Trap): The copy is strictly "shallow". If the dictionary contains MUTABLE values (like lists, sets, or nested dictionaries), the new dictionary merely points to the exact same nested memory boxes! Modifying the INSIDE of those nested objects will affect BOTH dictionaries.
    
    # EXPERT TIP (The Deepcopy Fix): If you need a completely independent clone of a dictionary that contains nested mutable data, you must import the `copy` module and use `copy.deepcopy()`.

original = {'a': 1, 'b': 2}
my_copy = original.copy()

# Modifying the outer structure (adding a new key) is completely safe
my_copy['c'] = 3 

print(original) # Output: {'a': 1, 'b': 2} (Original remains untouched!)
print(my_copy)  # Output: {'a': 1, 'b': 2, 'c': 3}

# ---------------------------------------------------------
# THE SHALLOW COPY TRAP IN ACTION
# ---------------------------------------------------------
nested_dict = {'user': 'harry', 'scores': [90, 85]}
shallow = nested_dict.copy()

# If we append a new score to the nested list inside the copy...
shallow['scores'].append(100)

# It corrupts the original too, because both dictionaries point to the exact same list in memory!
print(nested_dict) # Output: {'user': 'harry', 'scores': [90, 85, 100]}
print(shallow)     # Output: {'user': 'harry', 'scores': [90, 85, 100]}

# ---------------------------------------------------------
# EXPERT TIP: The Deepcopy Fix
# ---------------------------------------------------------
import copy

nested_dict2 = {'user': 'lily', 'scores': [95, 99]}
deep = copy.deepcopy(nested_dict2)

# If we append to the deep copy...
deep['scores'].append(100)

# The original is totally safe, because deepcopy() created brand new boxes for EVERYTHING inside!
print(nested_dict2) # Output: {'user': 'lily', 'scores': [95, 99]}
print(deep)         # Output: {'user': 'lily', 'scores': [95, 99, 100]}


## 12. dict() → Create a new dictionary object (Built-in Constructor)
    # --> dict([iterable], **kwargs)
    # THE TYPE RULE: dict() is a built-in Python type constructor, NOT a method called on an existing dictionary.
    
    # THE BEHAVIOR:
    # 1. No Arguments: Calling dict() creates an empty dictionary {}.
    # 2. Iterable of Pairs: You can pass a list/tuple of 2-item sequences (like [('a', 1), ('b', 2)]).
    # 3. Keyword Arguments: You can pass **kwargs (like a=1, b=2).
    
    # TRAP (The Kwargs Naming Trap): If you use keyword arguments (dict(a=1)), the keys MUST be valid Python identifier strings (variable names). You CANNOT use numbers or tuples as keys this way!
    
    # EXPERT TIP (dict() vs {}): While literal syntax `{}` is slightly faster and preferred for writing out hard-coded data, the dict() constructor shines when dynamically converting data (like zipping two lists together).

# Scenario 1: Empty Dictionary
empty_dict = dict() 
print(empty_dict) # Output: {}

# Scenario 2: Keyword Arguments
kwarg_dict = dict(name="Harry", age=34)
print(kwarg_dict) # Output: {'name': 'Harry', 'age': 34}

# Scenario 3: Iterable of Pairs
pairs = [('x', 10), ('y', 20)]
new_dict = dict(pairs)
print(new_dict)   # Output: {'x': 10, 'y': 20}

# ---------------------------------------------------------
# THE KWARGS TRAP IN ACTION
# ---------------------------------------------------------

# Keyword keys must be valid variable names!
# bad_dict = dict(1="a", 2="b") # SyntaxError: expression cannot contain assignment
# (Fix: Use literal syntax {1: "a", 2: "b"} or dict([(1, "a"), (2, "b")]))

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: The zip() Trick
# ---------------------------------------------------------
# The absolute best use of the dict() constructor is combining two parallel lists:

keys_list = ['user1', 'user2', 'user3']
vals_list = ['harry', 'jack', 'lily']

# zip() pairs them up: ('user1', 'harry'), ('user2', 'jack')...
# dict() instantly converts those pairs into a dictionary!
users = dict(zip(keys_list, vals_list))

print(users) 
# Output: {'user1': 'harry', 'user2': 'jack', 'user3': 'lily'}


## 13. len() → Return the total number of key-value pairs in the dictionary
    # --> len(dictionary)
    # THE TYPE RULE: len() is a built-in Python function, NOT a dictionary method. You wrap the dictionary inside it; you do not use dot notation.
    
    # THE BEHAVIOR: Returns an integer representing the total count of key-value PAIRS in the dictionary. 
    # It does NOT count the keys and values as separate items.
    # If the dictionary is empty {}, it returns 0.
    
    # EXPERT TIP (O(1) Time Complexity): Python dictionaries are highly optimized. 
    # The dictionary secretly keeps a running tally of its size at all times. When you call len(), Python doesn't actually count the items one by one—it just instantly reads that tally! This makes len() lightning fast (O(1)), even on dictionaries with millions of items.

my_dict = {'a': 1, 'b': 2, 'c': 3}
length = len(my_dict) 

print(length) # Output: 3

# Counting an empty dictionary
empty_dict = {}
print(len(empty_dict)) # Output: 0

# ---------------------------------------------------------
# THE COUNTING RULE IN ACTION
# ---------------------------------------------------------
# A nested dictionary still only counts as ONE value for its specific key!

nested = {
    'user1': {'name': 'Harry', 'age': 34},
    'user2': {'name': 'Lily', 'age': 94}
}

print(len(nested)) # Output: 2 (There are only 2 top-level pairs here: 'user1' and 'user2')


## 14. del → Delete a specific key-value pair, or destroy the entire variable
    # --> del dictionary[key]  OR  del dictionary
    # THE KEYWORD RULE: `del` is a built-in Python statement/keyword, NOT a function or method. You do not use parentheses.
    
    # THE BEHAVIOR:
    # 1. Targeted Deletion: `del my_dict['a']` removes that specific key-value pair in-place.
    # 2. Total Destruction: `del my_dict` completely destroys the variable name/reference from memory.
    
    # TRAP (The KeyError): If you try to delete a specific key that does NOT exist, it crashes with a KeyError! 
    # (Reminder: Use my_dict.pop('key', default_fallback) if you need safe deletion without crashes).
    
    # EXPERT TIP (del vs .clear()): 
    # my_dict.clear() empties the "box" but keeps the variable alive (it becomes {}). 
    # `del my_dict` sets the box on fire. The variable label ceases to exist entirely!

my_dict = {'a': 1, 'b': 2, 'c': 3}

new_dict = my_dict

# Scenario 1: Deleting a specific key
del my_dict['a']
print(my_dict) # Output: {'b': 2, 'c': 3}

# ---------------------------------------------------------
# THE KEYERROR TRAP IN ACTION
# ---------------------------------------------------------
# del my_dict['z'] # KeyError: 'z'
# (Fix: use my_dict.pop('z', None))

# ---------------------------------------------------------
# THE DESTRUCTION TRAP (Variable Deletion)
# ---------------------------------------------------------
# Scenario 2: Deleting the entire variable
del my_dict
print(new_dict) # but the other one refered still remains the same with no changes 

# The variable label 'my_dict' no longer exists in Python's memory!
# print(my_dict) # NameError: name 'my_dict' is not defined


## 15. in / not in → Check if a KEY exists in the dictionary (Membership Testing)
    # --> key in dictionary
    # THE KEYWORD RULE: 'in' and 'not in' are built-in Python operators. They evaluate to a boolean (True or False).
    
    # TRAP (The Key-Only Trap): These operators ONLY check the dictionary's KEYS. They do absolutely nothing with the values! 
    # Searching for a value using `in dictionary` will return False (unless that value also happens to be a key).
    
    # EXPERT TIP (O(1) Lightning Speed vs O(n) Slow Scan): 
    # Because dictionary keys are hashed (the warehouse trick), checking `key in my_dict` is practically instantaneous (O(1) time complexity) even with millions of items. 
    # However, checking `value in my_dict.values()` is SLOW (O(n)) because values aren't hashed—Python has to manually scan every single value one by one!

my_dict = {'a': 1, 'b': 2}

# ---------------------------------------------------------
# CHECKING KEYS (Fast O(1) Lookup)
# ---------------------------------------------------------
print('a' in my_dict)      # Output: True
print('z' in my_dict)      # Output: False
print('z' not in my_dict)  # Output: True

# Empty dictionaries safely return False without crashing
empty_dict = {}
print('a' in empty_dict)   # Output: False

# ---------------------------------------------------------
# THE VALUE TRAP IN ACTION
# ---------------------------------------------------------

# We know the value 1 is inside the dictionary...
print(1 in my_dict)        # Output: False (1 is a value, but 'in' ONLY looks at keys!)

# THE FIX: If you MUST check for a value, explicitly use .values()
print(1 in my_dict.values()) # Output: True (Just be aware this is slower on huge dictionaries!)


'''

ADDING & UPDATING
│
├── update()       → add/overwrite MANY pairs
└── setdefault()   → add ONE pair (ONLY if missing) + returns value


REMOVING
│
├── pop()          → remove by KEY (safe with default, returns value)
├── popitem()      → remove LAST inserted pair (returns tuple)
└── clear()        → remove EVERYTHING


ACCESSING (SAFE LOOKUP)
│
└── get()          → get VALUE by KEY (returns None, NO KeyError)


VIEWS (THE LIVE WINDOWS)
│
├── keys()         → view all KEYS
├── values()       → view all VALUES
└── items()        → view all PAIRS as (key, value) tuples


CREATING & COPYING
│
├── fromkeys()     → create NEW dict from an iterable of keys
└── copy()         → create a separate dictionary (Shallow copy)


======================================================
BONUS: BUILT-INS & KEYWORDS
======================================================
│
├── len()          → HOW MANY pairs?
├── in / not in    → check if KEY exists (Super fast O(1))
└── del            → STRICT remove by key (or destroy variable)

'''