s = {34, 23, 1, 3, 22}

print(s)
s.add(32)
s.add(322)
s.remove(1)
s.remove(434234) # Throws an KeyError because 434234 is not present in the set s
s.discard(42323) # Discard does not throw an error if the element is not present in the set. It simply does nothing.
print(s) # here 

# ============================================================
# PYTHON SET METHODS
# ============================================================

numbers = {10, 20, 30}

## 1. add() → Add ONE immutable item to the set
    # --> set.add(item)
    # TRAP: Modifies the set in-place and evaluates to None.
    # It takes STRICTLY ONE argument. Passing zero arguments raises a TypeError.
    
    # UNHASHABLE TRAP: The item MUST be immutable/hashable (e.g., int, float, str, tuple). 
    # Passing a mutable object (like a list or dict: numbers.add([40, 50])) raises a TypeError: unhashable type: 'list'.
    
    # DUPLICATE BEHAVIOR: Sets only hold unique elements. If the item already exists in the set, it is silently ignored without raising an error.

numbers = {10, 20, 30}

# Standard addition
numbers.add(40)
print(numbers) # Output: {10, 20, 30, 40} (Note: Set element ordering is not guaranteed)

# Adding a duplicate (silently ignored)
numbers.add(10)
print(numbers) # Output: {10, 20, 30, 40}

# The Unhashable Type Trap:
# numbers.add([50, 60]) # ---> TypeError: unhashable type: 'list'

# The Missing Argument Trap:
# numbers.add()         # ---> TypeError: add() takes exactly one argument (0 given)


## 2. update() → Add MULTIPLE elements
    # --> set.update(*iterables)
    # TRAP: Modifies the set in-place and evaluates to None.
    
    # THE TYPE TRAP: The argument(s) MUST be iterable (like a list, tuple, set, or string). 
    # Passing a non-iterable (like a single integer: numbers.update(50)) crashes with a TypeError: 'int' object is not iterable.
    
    # DUPLICATE BEHAVIOR: If elements are already present, it does nothing (duplicates are silently ignored).
    # EDGE CASES: Calling update() with empty iterables (like []), or with no arguments at all, is perfectly valid and safely leaves the set unchanged.
    
    # EXPERT TIP: You can pass multiple iterables at the exact same time separated by commas: numbers.update([1, 2], [3, 4]).

numbers = {10, 20, 30}

# Extending with an iterable (a list)
numbers.update([40, 50, 60]) 
print(numbers) # Output: {40, 10, 50, 20, 60, 30} (Remember: Set order is not guaranteed!)

# Extending with another set (Duplicates 40 and 50 are ignored)
numbers.update({40, 50}) 
print(numbers) # Output: {40, 10, 50, 20, 60, 30}

# The Non-Iterable Trap:
# numbers.update(100) # ---> TypeError: 'int' object is not iterable

# Perfectly valid "do nothing" calls:
numbers.update()
numbers.update([])


## 3. remove() → Remove a SPECIFIC item from the set
    # --> set.remove(item)
    # TRAP: Modifies the set in-place and evaluates to None.
    # Sets do not allow duplicates, so it removes the single unique instance of that item.
    
    # THE ERROR TRAP: If the item is NOT found in the set (or if the set is completely empty), it crashes with a KeyError.
    
    # THE ARGUMENT TRAP: It requires exactly one argument. Calling it empty (numbers.remove()) raises a TypeError.
    
    # EXPERT TIP: Because of the high risk of a KeyError crash, you should only use remove() if you WANT the program to stop when the item is missing. 
    # If you want to safely attempt to remove an item without worrying if it actually exists, use discard() instead!

numbers = {10, 20, 30, 40, 50} 

# Standard Removal
numbers.remove(40)
print(numbers) # Output: {50, 20, 10, 30} (Remember: Order is not guaranteed)

# The Missing Item Trap:
# numbers.remove(100) # ---> KeyError: 100

# The Missing Argument Trap:
# numbers.remove()    # ---> TypeError: remove() takes exactly one argument (0 given)


## 4. discard() → Remove an item from the set if it exists
    # --> set.discard(item)
    # If the item is not found, it does nothing (no error is raised).
    # If the set is empty, it does nothing.
    # The key difference between remove() and discard() is that remove() will throw a KeyError if the item is missing, while discard() will safely do nothing.
    # If the item is not provided, it will raise a TypeError. EX: numbers.discard() ---> TypeError: discard() takes exactly one argument (0 given)

numbers = {10, 20, 30, 40, 50} 
numbers.discard(40)
print(numbers) # Output: {10, 20, 30, 50}

# Trying to discard an item that isn't there
numbers.discard(99) # Does nothing, no error!


## 5. pop() → Remove and return an arbitrary item from the set
    # --> set.pop()
    # If the set is empty, it raises a KeyError.
    # If the set has only one item, it removes and returns that item.
    # If the set has multiple items, it removes and returns an arbitrary item (based on the underlying hash table, not necessarily the order you added them).
    # If an argument is provided, it will raise a TypeError. EX: numbers.pop(1) ---> TypeError: pop() takes no arguments (1 given)
    # NOTE: Unlike lists, sets do not have indexes, so you cannot specify which item to pop.

numbers = {10, 20, 30} 
removed_item = numbers.pop()

print(removed_item) # Output: Could be 10, 20, or 30 (arbitrary)
print(numbers)      # Output: The set with the remaining two items


## 6. clear() → Remove all items from the set
    # --> set.clear()
    # If the set is empty, it safely does nothing.
    # If the set is not empty, it removes all items, leaving behind an empty set().
    # If any argument is provided, it will raise a TypeError. EX: numbers.clear(1) ---> TypeError: clear() takes no arguments (1 given)

numbers = {10, 20, 30} 
numbers.clear()
print(numbers) # Output: set()


## 7. union() → Return a new set with all items from both sets
    # --> set.union(set1, set2, ...)
    # If the sets are empty, it returns an empty set.
    # If the sets have items, it returns a new set with all items from both (or all) sets.
    # If the sets have duplicate items, it returns a new set with only unique items.
    # Calling union() with no arguments is perfectly valid. EX: numbers.union() ---> Returns a shallow copy of the original set (does not raise an error).

    # You can use the operator | (pipe) to perform a union operation on two sets. It performs the same operation as the union() method. 

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

result = numbers1.union(numbers2) 
print(result) # Output: {10, 20, 30, 40, 50}

result = numbers1 | numbers2 
print(result) # Output: {10, 20, 30, 40, 50}


## 8. intersection() → Return a new set with only the items present in all sets
    # --> set.intersection(set1, set2, ...)
    # If the sets have items, it returns a new set with only the items present in all provided sets.
    # If the sets have no common items, it returns an empty set set().
    # Calling intersection() with no arguments is perfectly valid. EX: numbers1.intersection() ---> Returns a shallow copy of the original set (does not raise an error).

    # You can use the operator & (ampersand) to perform an intersection operation on two sets. It performs the same operation as the intersection() method.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

result = numbers1.intersection(numbers2) 
print(result) # Output: {30}

result = numbers1 & numbers2 
print(result) # Output: {30}


## 9. difference() → Return a new set with items present in the first set but NOT in the provided sets
    # --> set.difference(set1, set2, ...)
    # If the sets are empty, it returns an empty set.
    # If the sets have items, it returns a new set with only the items that are present in the original set but missing from the provided sets.
    # If the sets have no common items, it returns a new set with all items from the original set.
    # Calling difference() with no arguments is perfectly valid. EX: numbers1.difference() ---> Returns a shallow copy of the original set (does not raise an error).
    
    # You can use the operator - (minus) to perform a difference operation on two sets. It performs the same operation as the difference() method.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

result = numbers1.difference(numbers2) 
print(result) # Output: {10, 20}

result = numbers1 - numbers2 
print(result) # Output: {10, 20}


## 10. symmetric_difference() → Return a new set with items present in either set, but NOT in both
    # --> set.symmetric_difference(other_set)
    # TRAP: Unlike union/intersection/difference, this method accepts STRICTLY ONE argument.
    # If no arguments are provided, or if multiple are provided, it raises a TypeError.
    # If the sets are empty, it returns an empty set.
    # If the sets have no common items, it returns a new set with all items from both sets (acting like union).

    # You can use the operator ^ (caret) to perform a symmetric difference operation on two sets. It performs the same operation as the symmetric_difference() method.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

result = numbers1.symmetric_difference(numbers2) 
print(result) # Output: {10, 20, 40, 50}

result = numbers1 ^ numbers2 
print(result) # Output: {10, 20, 40, 50}


## 11. issubset() → Return True if all items of the original set are present in the provided set
    # --> set.issubset(other_set)
    # TRAP: This method accepts STRICTLY ONE argument. Passing multiple sets raises a TypeError.
    # If no argument is provided, it raises a TypeError: issubset() takes exactly one argument (0 given).
    # Math rule: An empty set is a subset of EVERY set. So set().issubset(any_set) is always True.
    # It evaluates instantly, returning a standard True/False boolean.

    # You can use the <= operator to check for a subset.
    # You can use the < operator to check for a "proper subset" (all items exist in the second set, AND the second set is larger).

numbers1 = {10, 20, 30}
numbers2 = {10, 20, 30, 40, 50}

result = numbers1.issubset(numbers2) 
print(result) # ---> True, because all items of numbers1 are in numbers2

# Using the operator:
print(numbers1 <= numbers2) # ---> True


## 12. issuperset() → Return True if all items of the provided set are present in the original set
    # --> set.issuperset(other_set)
    # TRAP: This method accepts STRICTLY ONE argument. Passing multiple sets raises a TypeError.
    # If no argument is provided, it raises a TypeError: issuperset() takes exactly one argument (0 given).
    # Math rule: EVERY set is a superset of an empty set. So any_set.issuperset(set()) is always True.
    # It evaluates instantly, returning a standard True/False boolean.

    # You can use the >= operator to check for a superset.
    # You can use the > operator to check for a "proper superset" (all items from the second set are in the first set, AND the first set is larger).

numbers1 = {10, 20, 30, 40, 50}
numbers2 = {10, 20, 30}

result = numbers1.issuperset(numbers2) 
print(result) # ---> True, because all items of numbers2 are present in numbers1

# Using the operator:
print(numbers1 >= numbers2) # ---> True


## 13. copy() → Return a shallow copy of the set
    # --> set.copy()
    # If the set is empty, it returns a new empty set().
    # If the set has items, it returns a new independent set with the exact same items.
    # It takes NO arguments. Passing an argument raises a TypeError. EX: numbers.copy(1) ---> TypeError: copy() takes no arguments (1 given)
    # Independence: Modifying the original set after copying does NOT affect the copied set, and vice versa.

numbers = {10, 20, 30} 
numbers_copy = numbers.copy() # ---> {10, 20, 30}

# Modifying only the copy
numbers_copy.add(40) 

print(numbers)      # Output: {10, 20, 30} (Original remains untouched)
print(numbers_copy) # Output: {10, 20, 30, 40}


## 14. len() → Return the number of items in the set
    # --> len(set)
    # NOTE: len() is a built-in Python function, not a set method, which is why we don't use dot notation (like set.len()).
    # If the set is empty, it returns 0.
    # If the set has items, it returns the number of items (the count) in the set.
    # If the set is not provided, it will raise a TypeError. EX: len() ---> TypeError: len() takes exactly one argument (0 given)
    # The result of len() is an integer. If the set is modified after the len() call, the previously saved length variable will not be affected. 

numbers = {10, 20, 30}
length = len(numbers) 

print(length) # Output: 3


## 15. isdisjoint() → Return True if two sets have no common items
    # --> set.isdisjoint(other_iterable)
    # TRAP: This method accepts STRICTLY ONE argument (which can be any iterable: list, tuple, set, etc.).
    # If no argument is provided, it raises a TypeError: isdisjoint() takes exactly one argument (0 given).
    # Passing multiple arguments also raises a TypeError.
    # Empty set behavior: If either set is empty, they have no common items, so it returns True.
    # Returns True if intersection is empty, False if they share at least one element.

numbers1 = {10, 20, 30}
numbers2 = {40, 50, 60}

result = numbers1.isdisjoint(numbers2) 
print(result) # Output: True (no items in common)

# Also works with lists/tuples:
print(numbers1.isdisjoint([30, 40])) # Output: False (30 is in common)


## 16. frozenset() → Return an immutable set
    # --> frozenset(iterable)
    # NOTE: frozenset() is a built-in Python type constructor, not a set method.
    # Returns an immutable, hashable version of a set that CANNOT be changed (no add/remove methods).
    # If no argument is provided, it safely returns an empty frozenset().
    # The elements inside the iterable MUST be hashable/immutable.
    # Modifying the original iterable after creating a frozenset will NOT affect the frozenset.
    # Key Power: Because frozensets are immutable, they CAN be used as dictionary keys or stored inside another set!

numbers = {10, 20, 30}
immutable_numbers = frozenset(numbers) 

print(immutable_numbers) # Output: frozenset({10, 20, 30})

# Attempting to modify raises an AttributeError:
# immutable_numbers.add(40) # ---> AttributeError: 'frozenset' object has no attribute 'add'


# Format:
### frozenset(iterable)
#
# frozenset() creates an immutable version of a set.
#
## Example:
#
# numbers = {10, 20, 30}
# immutable_numbers = frozenset(numbers)
# print(immutable_numbers)
# Output: frozenset({10, 20, 30})
#
# A frozenset cannot be modified.
#
# immutable_numbers.add(40)    # X AttributeError: 'frozenset' object has no attribute 'add'
# immutable_numbers.remove(10) # X AttributeError: 'frozenset' object has no attribute 'remove'
#
# The iterable can be a list, tuple, set, string, etc.
#
# frozenset([10, 20, 30]) -> frozenset({10, 20, 30})
#
#
## Empty iterable:
#
# frozenset([]) -> frozenset()
#
# frozenset() is also valid and safely returns an empty frozenset.
#
# If the original iterable is modified after creating the frozenset, the existing frozenset is NOT affected.
#
## Example:
#
# numbers = {10, 20, 30}
# immutable_numbers = frozenset(numbers)
#
# numbers.add(40)
#
# print(numbers)
# → {10, 20, 30, 40}
#
# print(immutable_numbers)
# → frozenset({10, 20, 30})
#
#
## IMPORTANT:
# A normal set is mutable and cannot be an element of another set.
# A frozenset is immutable and CAN be an element of another set.
#
# set       → mutable
# frozenset → immutable
#
## MEMORY TRICK:
# frozenset = "frozen" set → cannot be changed
# By locking the contents so they can never change, the hash value never changes, and Python never loses the item in the warehouse!


## 17. set() → Return a new mutable set object
    # --> set(iterable)
    # NOTE: set() is a built-in Python type constructor, not a method on an existing set.
    # If the iterable is empty, it returns an empty set.
    # If the iterable has items, it returns a new mutable set with the unique items from the iterable.
    # Calling set() with no arguments is perfectly valid; it creates an empty set().
    # Modifying the original iterable after calling set() will NOT affect the new set.
    
    # TRAP: In Python, using empty curly braces {} creates an empty dictionary, not an empty set. 
    # The ONLY way to create an empty set is by calling set() with nothing inside the parentheses.

# Converting a frozenset back to a mutable set
frozen_numbers = frozenset({10, 20, 30}) 
mutable_numbers = set(frozen_numbers) 
print(mutable_numbers) # Output: {10, 20, 30}

# Converting a list with duplicates (A pro trick to remove duplicates!)
my_list = [10, 20, 20, 30]
my_set = set(my_list)
print(my_set) # Output: {10, 20, 30}

# The Empty Set vs Empty Dictionary Trap
empty_dict = {}
print(type(empty_dict)) # Output: <class 'dict'>

empty_set = set()       # This is the correct way to make an empty set!
print(type(empty_set))  # Output: <class 'set'>


## 18. del → Delete a set variable from memory
    # --> del set_variable
    # KEYWORD vs FUNCTION: `del` is a built-in Python statement/keyword, NOT a function or method.
    # Idiomatic usage is WITHOUT parentheses: `del numbers`.(Idiomatic usage : common phrases derived from machinery, computers, and digital tools, as well as writing code that feels natural and follows the best practices of a specific programming language)
    # Writing `del()` or typing `del` alone causes a parse-time `SyntaxError` because the grammar is incomplete.
    #
    # Effect: `del` unbinds the variable name entirely and removes it from the local/global namespace.
    # If no other references exist, Python's garbage collector reclaims the memory.
    # Removes Labels: del deletes the variable name (label), not the actual data in memory.
    # Breaks Links: It unbinds the name from the local or global namespace.
    # Lowers Count: It drops the object's reference counter by 1.
    # Triggers Cleanup: The garbage collector deletes the data only when its reference count hits 0.To help you app
    # Result: Attempting to access or print the variable after using `del` raises a NameError.

numbers = {10, 20, 30}

# Deleting the variable completely
del numbers 

# Attempting to print the deleted variable
# print(numbers) # Output: NameError: name 'numbers' is not defined


## 19. in (Membership Operator) → Return True if an item is present in the set
    # --> item in set
    # NOTE: 'in' is a Python membership operator, not a set method.
    # If the set is empty, it safely returns False (e.g., 10 in set() ---> False).
    # It evaluates instantly, returning a standard True/False boolean.
    
    # SyntaxError: If you just write '10 in', Python throws a SyntaxError because the sentence is grammatically incomplete.
    # TypeError: If the right side of 'in' is not a collection/iterable (e.g., 10 in 5), Python raises a TypeError.
    
    # EXPERT TIP: Using 'in' on a set is incredibly fast! Because sets use hash values (the warehouse trick), Python finds the item instantly without scanning the whole set. (This is called O(1) time complexity).

numbers = {10, 20, 30}
result = 10 in numbers 
print(result) # Output: True (because 10 is present)


## 20. not in (Membership Operator) → Return True if an item is NOT present in the set
    # --> item not in set
    # NOTE: 'not in' is the exact inverse of the 'in' operator.
    # If the set is empty, it always returns True (e.g., 40 not in set() ---> True).
    # It evaluates instantly, returning a standard True/False boolean.
    
    # Just like 'in', checking 'not in' is incredibly fast for sets (O(1) lookup time) because Python just checks the hash table directly to see if the shelf is empty.
    # The same SyntaxError (incomplete sentence) and TypeError (right side is not an iterable) rules apply here.

numbers = {10, 20, 30}
result = 40 not in numbers 

print(result) # Output: True (because 40 is safely missing from the set)


## 21. intersection_update() → Update the set, keeping only items found in both (or all) sets
    # --> set.intersection_update(*others)
    # TRAP: Unlike intersection(), this does NOT return a new set. It modifies the original set in-place and evaluates to None.
    # It removes any item from the original set that is not found in the provided iterable(s).
    # If a provided iterable is empty, it completely empties the original set (because there are no common items).
    # If no arguments are provided, it simply does nothing and leaves the original set unchanged.
    # The arguments can be ANY iterable (lists, tuples, other sets, etc.).

    # You can use the augmented assignment operator &= to perform this exact same in-place operation.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

numbers1.intersection_update(numbers2) 
print(numbers1) # Output: {30} (Original set is modified!)

# Using the operator:
numbers3 = {5, 10, 15}
numbers3 &= {10, 20, 30} 
print(numbers3) # Output: {10}


## 22. difference_update() → Remove items from the original set that exist in the provided sets
    # --> set.difference_update(*others)
    # TRAP: This modifies the original set in-place and evaluates to None.
    # It acts like subtraction: Original Set - Provided Iterable(s).
    # If the provided iterables are empty (or share no common items), the original set remains completely unchanged.
    # If no arguments are provided, it simply does nothing and leaves the set unchanged.
    # The arguments can be ANY iterable (lists, tuples, other sets, etc.).

    # You can use the augmented assignment operator -= to perform this exact same in-place operation.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Modifies numbers1 by deleting anything that is also in numbers2
numbers1.difference_update(numbers2) 

print(numbers1) # Output: {10, 20} (Original set is modified!)
print(numbers2) # Output: {30, 40, 50} (The provided set is NEVER modified!)

# Using the operator:
numbers3 = {1, 2, 3, 4, 5}
numbers3 -= {4, 5, 6} 
print(numbers3) # Output: {1, 2, 3}


## 23. symmetric_difference_update() → Keep items present in either set, but NOT in both
    # --> set.symmetric_difference_update(other_iterable)
    # TRAP: Unlike difference_update(), this method accepts STRICTLY ONE argument. 
    # If no argument is provided, or if multiple are provided, it raises a TypeError.
    # It modifies the original set in-place and evaluates to None.
    # If the provided iterable is empty, the original set remains completely unchanged.
    # If the sets have zero common items, the original set becomes the union of both.
    # The argument can be ANY iterable (lists, tuples, other sets, etc.).

    # You can use the augmented assignment operator ^= to perform this exact same in-place operation.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Modifies numbers1: removes 30 (overlap) and adds 40, 50 (unique to numbers2)
numbers1.symmetric_difference_update(numbers2) 

print(numbers1) # Output: {10, 20, 40, 50} (Original set is modified!)
print(numbers2) # Output: {30, 40, 50} (The provided set is NEVER modified!)

# Using the operator:
numbers3 = {1, 2, 3}
numbers3 ^= {3, 4, 5} 
print(numbers3) # Output: {1, 2, 4, 5}


"""

ADDING
│
├── add()           → add ONE item
└── update()        → add MANY items (modifies in-place)

REMOVING
│
├── remove()        → remove by VALUE (raises KeyError if missing)
├── discard()       → remove by VALUE (safe, no error)
├── pop()           → remove & return a RANDOM item
├── clear()         → remove EVERYTHING (empties the set)
└── del             → delete the ENTIRE variable from memory

MATH OPERATIONS (Returns a NEW set)
│
├── union()         → ALL unique items from all sets
├── intersection()  → ONLY items present in ALL sets
├── difference()    → items in FIRST set, but NOT in others
└── symmetric_difference() → items in EITHER set, but NOT both

MATH UPDATES (Modifies ORIGINAL set in-place)
│
├── intersection_update()         → keep ONLY common items
├── difference_update()           → remove items found in others
└── symmetric_difference_update() → keep EITHER, but NOT both

COMPARISONS & SEARCHING (Returns True / False)
│
├── issubset()      → are ALL our items inside the other set?
├── issuperset()    → do WE contain all items of the other set?
├── isdisjoint()    → do they share ZERO common items?
├── in              → is this specific item PRESENT?
└── not in          → is this specific item MISSING?

UTILITY & CREATION
│
├── set()           → create a mutable set (or remove duplicates)
├── frozenset()     → create an IMMUTABLE set (can be hashed)
├── copy()          → create a separate set i.e Shallow copy
└── len()           → count total number of items

"""
