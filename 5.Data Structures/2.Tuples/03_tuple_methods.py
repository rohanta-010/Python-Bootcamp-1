## THE GOLDEN RULE OF TUPLES: IMMUTABILITY
    # Because tuples cannot be changed after creation, they DO NOT have methods 
    # for adding, removing, or sorting items. They only have TWO searching methods!

# -------------------------------------------------------------------------
## 1. count() → Return the total number of occurrences of an item
# -------------------------------------------------------------------------
    # --> tuple.count(value)
    # SAFE METHOD: Just like list.count(), this NEVER crashes with a ValueError. 
    # If the item is not found, it safely returns 0.

t = (3, 12, 1, 54, 23, 12)

# Count how many times 12 appears
total_twelves = t.count(12)
print(total_twelves) # Output: 2

# Item not found
print(t.count(100))  # Output: 0


# -------------------------------------------------------------------------
## 2. index() → Return the index of the FIRST occurrence of an item
# -------------------------------------------------------------------------
    # --> tuple.index(value, [start], [end])
    # THE ERROR TRAP: Just like lists, if the value does not exist in the tuple, it crashes with a ValueError. 
    
    # EXPERT TIP: Always verify the item is in the tuple first using the 'in' operator to avoid crashing your program!

t = (3, 12, 1, 54, 23, 12)
#   (0,  1, 2,  3,  4,  5)

# Find the position of the first 3
first_index = t.index(3)
print(first_index) # Output: 0

# Find the position of the first 12
first_twelve = t.index(12)
print(first_twelve) # Output: 1 (Notice it completely ignores the second '12' at index 5)

# The Error Trap:
# t.index(99) # ---> ValueError: tuple.index(x): x not in tuple

# Safe Search Example:
if 99 in t:
    print(t.index(99))
else:
    print("Not found in tuple!") # Output: Not found in tuple!