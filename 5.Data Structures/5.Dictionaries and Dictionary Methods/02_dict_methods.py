marks = {"harry": 34, "jack": 45, "lily": 94 }

print(marks.keys())
print(marks.values())
# marks.clear()
marks.pop("lily")
print(marks)


# ============================================================
# PYTHON Dictionary METHODS
# ============================================================


## 1. update() → Update the dictionary with specified key-value pairs
    # --> dict.update(iterable/kwargs)
    # When you prefix a parameter with a double asterisk (**), Python automatically collects all extra keyword arguments passed to the function and stores them inside a standard dictionary (dict). 
    # This modifies the original dictionary in-place and returns None.
    # If a key already exists, its value is overwritten/updated.
    # If a key does NOT exist, it is added to the dictionary.
    # You can pass another dictionary, an iterable of tuples (like [('c', 3)]), or keyword arguments.

my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 99, 'c': 3}) 

print(my_dict) # Output: {'a': 1, 'b': 99, 'c': 3}


dict.update(
    {'c': 3}           # dictionary
)

dict.update(
    [('c', 3)]         # list of pairs
)

dict.update(
    (('c', 3),)        # tuple containing pairs
)


## 2. setdefault() → Return a key's value, or insert it with a default if missing
    # --> dict.setdefault(key, default_value)
    # If the key EXISTS, it simply returns the current value (and completely ignores the default_value).
    # If the key is MISSING, it inserts the key into the dictionary with the default_value, and then returns that value.
    # If no default_value is provided, it defaults to None.

my_dict = {'a': 1}
val1 = my_dict.setdefault('a', 100) # Key exists! Returns 1, dictionary is unchanged.
val2 = my_dict.setdefault('b', 200) # Key missing! Inserts 'b': 200, and returns 200.

print(my_dict) # Output: {'a': 1, 'b': 200}


## 3. pop() → Remove a specified key and return its value
    # --> dict.pop(key, default_value)
    # If the key exists, it deletes the key-value pair from the dictionary and returns the value.
    # If the key is missing and no default_value is provided, it crashes with a KeyError.
    # If the key is missing but a default_value IS provided, it safely returns the default_value instead of crashing.

my_dict = {'a': 1, 'b': 2}
val = my_dict.pop('a') 
print(val)     # Output: 1
print(my_dict) # Output: {'b': 2}

# print(my_dict.pop('c')) # ---> KeyError: 'c'
print(my_dict.pop('c', 'Not Found')) # Output: 'Not Found' (Safe fallback!)


## 4. popitem() → Remove and return the LAST inserted key-value pair
    # --> dict.popitem()
    # In Python 3.7+, dictionaries remember their exact insertion order. This ALWAYS removes the very last inserted key-value pair that is currently in the dictionary
    # It returns the removed pair as a tuple: (key, value).
    # It takes NO arguments. Passing an argument raises a TypeError.
    # If the dictionary is empty, calling popitem() raises a KeyError.

my_dict = {'a': 1, 'b': 2, 'c': 3}
last_item = my_dict.popitem() 

print(last_item) # Output: ('c', 3)
print(my_dict)   # Output: {'a': 1, 'b': 2}


## 5. clear() → Remove all items from the dictionary
    # --> dict.clear()
    # Modifies the original dictionary in-place, leaving it completely empty {}.
    # It evaluates to None.
    # It takes NO arguments.

my_dict = {'a': 1, 'b': 2}
my_dict.clear()

print(my_dict) # Output: {}


## 6. get() → Return the value for a specified key (Safe lookup)
    # --> dict.get(key, default_value)
    # TRAP: Unlike using square brackets (my_dict['c']), get() NEVER raises a KeyError if the key is missing!
    # If the key exists, it returns the value.
    # If the key is missing, it safely returns the default_value.
    # If the key is missing and no default is provided, it safely returns None.

my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))              # Output: 1
print(my_dict.get('c'))              # Output: None
print(my_dict.get('c', 'Missing!'))  # Output: 'Missing!'

# [] = strict lookup
# .get() = safe lookup


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
