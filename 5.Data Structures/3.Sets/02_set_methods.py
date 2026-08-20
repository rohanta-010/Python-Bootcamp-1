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


## 4. discard() → Remove a specific item SAFELY (only if it exists)
    # --> set.discard(item)
    # TRAP: Modifies the set in-place and evaluates to None.
    
    # SAFE METHOD: The primary difference between remove() and discard() is that discard() is completely crash-proof regarding missing items. 
    # If the item is not found (or if the set is already empty), it safely does nothing and moves on. No KeyError is raised!
    
    # THE ARGUMENT TRAP: Just like remove(), it requires exactly one argument. Calling it empty (numbers.discard()) raises a TypeError.
    
    # EXPERT TIP: Default to using discard() for standard set operations. Only use remove() if your program's logic explicitly relies on knowing whether an item was successfully removed or not.

numbers = {10, 20, 30, 40, 50} 

# Standard Removal
numbers.discard(40)
print(numbers) # Output: {50, 20, 10, 30} (Remember: Order is not guaranteed)

# The Safe Failure (Item not in set)
numbers.discard(99) # SAFE: Does absolutely nothing, no crash!
print(numbers)      # Output: {50, 20, 10, 30} (Set remains unchanged)

# The Missing Argument Trap:
# numbers.discard()   # ---> TypeError: discard() takes exactly one argument (0 given)


## 5. pop() → Remove and return an ARBITRARY item
    # --> set.pop()
    # TRAP: Unlike remove() and discard(), this method DOES evaluate to a value (the removed item) while modifying the set in-place.
    
    # THE UNPREDICTABLE TRAP: Because sets are completely unordered and lack indexes, you have ZERO control over which item gets removed. It removes an arbitrary item based on Python's internal memory hashing.
    
    # THE ERROR TRAP: If the set is completely empty, it crashes with a KeyError.
    
    # THE ARGUMENT TRAP: Unlike list.pop(index), set.pop() takes NO arguments. Trying to pass an index (e.g., numbers.pop(0)) crashes with a TypeError.
    
    # EXPERT TIP: Because it is unpredictable, set.pop() is rarely used for specific data manipulation. However, it is fantastic for destroying a set piece-by-piece in a `while` loop (e.g., processing a queue of unique tasks where the order doesn't matter).

numbers = {10, 20, 30, 40}

# Standard Pop (No arguments allowed!)
removed_item = numbers.pop()

print(f"Removed: {removed_item}") # Output: Could be 40, 10, 20, or 30!
print(f"Remaining: {numbers}")    # Output: The set minus the removed item

# The Argument Trap:
# numbers.pop(1) # ---> TypeError: set.pop() takes no arguments (1 given)

# The Empty Set Trap:
# empty_set = set()
# empty_set.pop() # ---> KeyError: 'pop from an empty set'


## 6. clear() → Remove ALL items from the set
    # --> set.clear()
    # TRAP: Modifies the set in-place and evaluates to None.
    # It completely wipes out all elements, leaving behind an empty set.
    # If the set is already empty, it safely does nothing (no errors raised).
    
    # THE EMPTY SET TRAP: Notice the output of an empty set is 'set()' and NOT '{}'. 
    # In Python, '{}' strictly creates an empty DICTIONARY. If you need to create an empty set from scratch, you MUST type 'set()'.
    
    # THE ARGUMENT TRAP: clear() takes NO arguments. Passing anything raises a TypeError.

numbers = {10, 20, 30} 

# Standard Clear
numbers.clear()
print(numbers) # Output: set()

# The Argument Trap:
# numbers.clear(1) # ---> TypeError: set.clear() takes no arguments (1 given)


## 7. union() → Return a NEW set with all unique items from multiple sets
    # --> set.union(*iterables)
    # TRAP: Unlike add() or update(), set math methods DO NOT modify the original set in-place. 
    # They evaluate to a brand NEW set. You must assign the result to a variable!
    
    # DUPLICATE BEHAVIOR: It combines everything but strictly enforces the primary rule of sets: all duplicates are dropped.
    
    # THE OPERATOR TRAP (| vs .union()): 
    # The .union() method is highly flexible and accepts ANY iterable (lists, tuples, strings). 
    # However, the shorthand pipe operator (|) STRICTLY requires both sides to be actual sets!
    
    # EXPERT TIP: Calling union() with no arguments (numbers.union()) is a perfectly valid way to create a shallow copy of a set.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Standard Union (Notice that the duplicate '30' is merged into one)
result = numbers1.union(numbers2) 
print(result) # Output: {40, 10, 50, 20, 30}

# Operator Shorthand (Does the exact same thing)
result_pipe = numbers1 | numbers2 
print(result_pipe) # Output: {40, 10, 50, 20, 30}

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Method vs Operator Flexibility
# ---------------------------------------------------------

# The .union() method safely unpacks a LIST
list_union = numbers1.union([80, 90]) 
print(list_union) # Valid! Output: {80, 10, 90, 20, 30}

# The pipe operator (|) crashes if you give it a LIST
# crash_union = numbers1 | [80, 90] #  TypeError: unsupported operand type(s) for |: 'set' and 'list'


## 8. intersection() → Return a NEW set with only the SHARED items
    # --> set.intersection(*iterables)
    # TRAP: Does not modify the original set in-place. It evaluates to a brand NEW set containing only the items that exist in ALL provided sets.
    
    # NO OVERLAP: If there are absolutely no common items, it safely returns an empty set: set().
    
    # THE OPERATOR TRAP (& vs .intersection()): 
    # Just like union(), the .intersection() method safely accepts ANY iterable (lists, strings, tuples). 
    # However, the shorthand ampersand operator (&) STRICTLY requires actual sets on both sides!
    
    # EXPERT TIP: Calling intersection() with no arguments (numbers1.intersection()) returns a shallow copy of the original set.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Standard Intersection (Only '30' exists in both)
result = numbers1.intersection(numbers2) 
print(result) # Output: {30}

# Operator Shorthand (Does the exact same thing)
result_amp = numbers1 & numbers2 
print(result_amp) # Output: {30}

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Method vs Operator Flexibility
# ---------------------------------------------------------

# The .intersection() method safely checks against a LIST
list_intersect = numbers1.intersection([30, 99, 100]) 
print(list_intersect) # Valid! Output: {30}

# The ampersand operator (&) crashes if you give it a LIST
# crash_intersect = numbers1 & [30, 99, 100] # TypeError: unsupported operand type(s) for &: 'set' and 'list'


## 9. difference() → Return a NEW set with items in the FIRST set, but NOT in the others
    # --> set.difference(*iterables)
    # TRAP: Does not modify the original set in-place. It evaluates to a brand NEW set containing items that exist in the original set, minus any items found in the provided sets.
    
    # THE DIRECTION TRAP (Order Matters!): 
    # Unlike union or intersection, difference is strictly directional. set_A - set_B will give you a completely different result than set_B - set_A.
    
    # THE OPERATOR TRAP (- vs .difference()): 
    # The .difference() method safely accepts ANY iterable (lists, strings, tuples). 
    # However, the shorthand minus operator (-) STRICTLY requires actual sets on both sides.
    
    # EXPERT TIP: Calling difference() with no arguments (numbers1.difference()) returns a shallow copy of the original set.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Standard Difference (What is in 1, that is NOT in 2?)
result = numbers1.difference(numbers2) 
print(result) # Output: {10, 20}

# Operator Shorthand (Does the exact same thing)
result_minus = numbers1 - numbers2 
print(result_minus) # Output: {10, 20}

# The Direction Trap (Reversing the order changes everything!)
reverse_result = numbers2 - numbers1
print(reverse_result) # Output: {40, 50}

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Method vs Operator Flexibility
# ---------------------------------------------------------

# The .difference() method safely checks against a LIST
list_diff = numbers1.difference([30, 99, 100]) 
print(list_diff) # Valid! Output: {10, 20}

# The minus operator (-) crashes if you give it a LIST
# crash_diff = numbers1 - [30, 99, 100] # TypeError: unsupported operand type(s) for -: 'set' and 'list'


## 10. symmetric_difference() → Return a NEW set with items in EITHER set, but NOT both
    # --> set.symmetric_difference(iterable)
    # TRAP: Does not modify the original set in-place. It evaluates to a brand NEW set containing only the "uniques" from both sides (effectively removing the overlap).
    
    # THE ARGUMENT TRAP: Unlike union/intersection/difference, this method accepts STRICTLY ONE argument. 
    # If no arguments are provided, or if multiple are provided, it raises a TypeError.
    
    # THE OPERATOR TRAP (^ vs .symmetric_difference()): 
    # The .symmetric_difference() method safely accepts ANY iterable (lists, strings, tuples). 
    # However, the shorthand caret operator (^) STRICTLY requires actual sets on both sides.
    
    # EDGE CASE: If the sets have no common items, it acts exactly like a union().

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Standard Symmetric Difference (Drops the shared '30')
result = numbers1.symmetric_difference(numbers2) 
print(result) # Output: {40, 10, 50, 20} (Order is not guaranteed)

# Operator Shorthand (Does the exact same thing)
result_caret = numbers1 ^ numbers2 
print(result_caret) # Output: {40, 10, 50, 20}

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Method vs Operator Flexibility
# ---------------------------------------------------------

# The method safely checks against a LIST
list_sym = numbers1.symmetric_difference([30, 99, 100]) 
print(list_sym) # Valid! Output: {99, 100, 20, 10}

# The caret operator (^) crashes if you give it a LIST
# crash_sym = numbers1 ^ [30, 99, 100] # TypeError: unsupported operand type(s) for ^: 'set' and 'list'

# The Multiple Argument Trap:
# numbers1.symmetric_difference(numbers2, {80}) # TypeError: symmetric_difference() takes exactly one argument (2 given)


## 11. issubset() → Return True if ALL items in the original set are present in the provided set
    # --> set.issubset(iterable)
    # TRAP: Does not return a new set. It evaluates instantly to a standard Boolean (True or False).
    
    # THE ARGUMENT TRAP: This method accepts STRICTLY ONE argument. 
    # Passing zero arguments, or passing multiple, raises a TypeError.
    
    # THE OPERATOR TRAP (<= vs .issubset()): 
    # The .issubset() method safely accepts ANY iterable (lists, strings, tuples). 
    # However, the shorthand subset operator (<=) STRICTLY requires actual sets on both sides.
    
    # EXPERT TIP 1: The empty set is mathematically a subset of EVERY set. set().issubset(any_set) is ALWAYS True.
    # EXPERT TIP 2 (PROPER SUBSETS): You can use the strictly-less-than operator (<) to check for a "proper subset". 
    # This means all items exist in the second set, AND the second set is strictly larger (they are not exactly equal).

numbers1 = {10, 20, 30}
numbers2 = {10, 20, 30, 40, 50}

# Standard Subset Check
result = numbers1.issubset(numbers2) 
print(result) # Output: True (All items of numbers1 are in numbers2)

# Operator Shorthand (Does the exact same thing)
print(numbers1 <= numbers2) # Output: True

# Proper Subset Check (< operator)
# True because numbers1 is smaller than numbers2
print(numbers1 < numbers2) # Output: True 
# False because they are completely equal (not strictly smaller)
print(numbers1 < {10, 20, 30}) # Output: False

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: Method vs Operator Flexibility
# ---------------------------------------------------------

# The method safely checks against a LIST
print(numbers1.issubset([10, 20, 30, 40, 50])) # Valid! Output: True

# The <= operator crashes if you give it a LIST
# print(numbers1 <= [10, 20, 30, 40, 50]) # TypeError: unsupported operand type(s) for <=: 'set' and 'list'


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


## 13. copy() → Return a SHALLOW copy of the set
    # --> set.copy()
    # TRAP: Does not modify the set in-place. It evaluates to a brand NEW, independent set.
    
    # INDEPENDENCE: Modifying the original set after copying does NOT affect the copied set, and vice versa. 
    # (If you simply do `set_B = set_A`, they point to the exact same memory, so changing one changes both. copy() prevents this!)
    
    # THE ARGUMENT TRAP: It takes exactly NO arguments. Passing anything raises a TypeError.
    
    # EXPERT TIP: Because sets enforce the rule that their contents MUST be immutable (like ints, strings, tuples), the distinction between a "shallow copy" and a "deep copy" doesn't actually matter here like it does for lists!

numbers = {10, 20, 30} 
numbers_copy = numbers.copy() 

# Modifying only the copy
numbers_copy.add(40) 

# Proof of Independence:
print(numbers)      # Output: {10, 20, 30} (Original remains untouched)
print(numbers_copy) # Output: {40, 10, 20, 30}


## 14. len() → Return the total number of items in the set
    # --> len(set)
    # TRAP: len() is a built-in Python function, NOT a set method. 
    # This is why we write len(numbers) instead of numbers.len(). Trying to use dot notation will crash with an AttributeError.
    
    # THE ARGUMENT TRAP: It takes exactly ONE argument. Passing nothing (len()) or passing multiple arguments raises a TypeError.
    
    # INDEPENDENCE: The result is a standard integer. If you modify the set later, the previously saved length variable will NOT update automatically.
    
    # EXPERT TIP: Because of how Python sets are built under the hood (as hash tables), len() evaluates instantly—no matter if your set has 3 items or 3 million items!

numbers = {10, 20, 30}
length = len(numbers) 

print(length) # Output: 3

# Proving it doesn't update dynamically:
numbers.add(40)
print(length)       # Output: 3 (Still holds the old value)
print(len(numbers)) # Output: 4 (The current length)

# The Built-In Function Trap:
# numbers.len() # ---> AttributeError: 'set' object has no attribute 'len'


## 15. isdisjoint() → Return True if two sets have NO common items
    # --> set.isdisjoint(iterable)
    # TRAP: Does not return a new set. It evaluates instantly to a standard Boolean (True or False).
    
    # THE ARGUMENT TRAP: This method accepts STRICTLY ONE argument. 
    # Passing zero arguments, or passing multiple, raises a TypeError.
    
    # FLEXIBILITY: Just like other named methods (union, intersection), this safely accepts ANY iterable (lists, strings, tuples, etc.).
    
    # EMPTY SET RULE: An empty set shares nothing with any other set. Therefore, set().isdisjoint(any_iterable) is ALWAYS True.
    
    # EXPERT TIP (Speed!): You might think isdisjoint() is just a shortcut for checking `len(set_A & set_B) == 0`. 
    # However, isdisjoint() is highly optimized under the hood. It stops searching (short-circuits) the exact millisecond it finds a single match, making it significantly faster than doing full set math!

numbers1 = {10, 20, 30}
numbers2 = {40, 50, 60}

# Standard check (Zero overlap)
result = numbers1.isdisjoint(numbers2) 
print(result) # Output: True (no items in common)

# Overlap check
print(numbers1.isdisjoint({30, 40})) # Output: False (They share '30')

# ---------------------------------------------------------
# FLEXIBILITY IN ACTION: Checking against other iterables
# ---------------------------------------------------------
# Works perfectly against a LIST
print(numbers1.isdisjoint([80, 90, 100])) # Valid! Output: True

# Works perfectly against a STRING
# (Note: numbers1 contains ints, so there is no overlap with string chars)
print(numbers1.isdisjoint("hello")) # Valid! Output: True


## 16. frozenset() → Return an IMMUTABLE set
    # --> frozenset([iterable])
    # TRAP: frozenset() is a built-in Python type constructor, NOT a set method. 
    # It creates a frozen (unchangeable) version of a set. Because it is immutable, methods like add(), remove(), or clear() do not exist.
    
    # THE EMPTY ARGUMENT RULE: If no argument is provided, it safely returns an empty frozenset().
    
    # INDEPENDENCE: Modifying the original iterable after creating a frozenset will NOT affect the frozenset.
    
    # KEY POWER (Hashability!): Standard sets are mutable, meaning they are "unhashable" and CANNOT be placed inside another set or used as Dictionary keys. 
    # Frozensets solve this! Because they are frozen/hashable, you CAN use them as dict keys or store them inside other sets!

numbers = {10, 20, 30}
immutable_numbers = frozenset(numbers) 

print(immutable_numbers) # Output: frozenset({10, 20, 30})

# The Modification Trap:
# immutable_numbers.add(40) # ---> AttributeError: 'frozenset' object has no attribute 'add'

# ---------------------------------------------------------
# KEY POWER IN ACTION: Nesting Sets & Dict Keys
# ---------------------------------------------------------

# A standard set CANNOT go inside a set:
# my_set = { {1, 2}, {3, 4} } # TypeError: unhashable type: 'set'

# But frozensets work perfectly!
nested_sets = {frozenset({1, 2}), frozenset({3, 4})}
print(nested_sets) # Valid! Output: {frozenset({1, 2}), frozenset({3, 4})}


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
