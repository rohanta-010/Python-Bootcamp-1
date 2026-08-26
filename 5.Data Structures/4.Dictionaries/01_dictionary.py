### =========================================================================
### DICTIONARIES: Basics & The Hashability Rule
### =========================================================================

# A Dictionary is a mutable collection of key-value pairs.
# 
# THE GOLDEN RULE OF KEYS: Dictionary keys MUST be hashable.
# Hashable means an object has a fixed hash value that remains consistent during its entire lifetime.
# By locking the key so it never changes, Python can instantly find the associated value in the memory warehouse!

# -> Mutable objects (like lists, sets, or other dictionaries) can change their contents. 
#    Therefore, they are UNHASHABLE and CANNOT be dictionary keys.
# -> Immutable objects (like strings, integers, floats, booleans, and frozensets) ARE hashable.

# ---------------------------------------------------------
# RULE 1: Invalid Keys (Mutable Objects)
# ---------------------------------------------------------
# marks = {[1, 2, 3]: "value"} # TypeError: unhashable type: 'list'
# marks = {{1, 2}: "value"}    # TypeError: unhashable type: 'set'

# ---------------------------------------------------------
# RULE 2: Valid Keys (Immutable Objects)
# ---------------------------------------------------------
locations = {
    "harry": 34,         # String key
    99: "Wayne Gretzky", # Integer key
    (10, 20): "Point A"  # Tuple key (Valid!)
}

# ---------------------------------------------------------
# EXPERT TIP: The Tuple Trap
# ---------------------------------------------------------
# A tuple can be a dictionary key ONLY if all of its internal elements are also hashable.
# valid_tuple_key = {(1, 2, 3): "value"}       # Works! (Contains only ints)
# invalid_tuple_key = {(1, [2, 3]): "value"}   # TypeError: unhashable type: 'list' (The list inside ruins it!)

# =========================================================
# BASIC DICTIONARY OPERATIONS (Creation, Access, Update)
# =========================================================

marks = {"harry": 34, "jack": 45, "lily": 94}

# 1. Printing the dictionary and checking its type
print(marks)       # Output: {'harry': 34, 'jack': 45, 'lily': 94}
print(type(marks)) # Output: <class 'dict'>

# 2. Accessing a value using its exact key (Bracket Notation)
# TRAP: If the key doesn't exist, this throws a KeyError!
print(marks["lily"]) # Output: 94

# 3. Updating a value (In-Place)
# Dictionaries are mutable, meaning we can change the value attached to a key at any time.
marks["harry"] = 3

print(marks) # Output: {'harry': 3, 'jack': 45, 'lily': 94}