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

## 1.add() → Add an item to the set
    # --> set.add(item)
    # If the item is already present, it does nothing.
    # If the set is empty, it will add the item to the set.
    # If the item is not provided, it will raise a TypeError. EX: numbers.add() ---> TypeError: add() takes exactly one argument (0 given)
    # Because of the hashing rule, the item you put inside add() must be immutable. If you try to do numbers.add([40, 50]) (adding a list), Python will throw a TypeError: unhashable type: 'list'

numbers = {10, 20, 30}  # ---> {10, 20, 30, 40}
numbers.add(40)
print(numbers)


## 2. update() → Add MULTIPLE elements
    # --> set.update(elements) 
    # If the elements are not iterable, it will raise a TypeError. EX: numbers.update(50) ---> TypeError: 'int' object is not iterable
    # If the elements are already present, it does nothing (duplicates are ignored).
    # If the set is empty, it will add the elements to the set.
    # If the elements are empty iterables (like []), it will not change the set.
    # Calling update() with no arguments is perfectly valid. EX: numbers.update() ---> Does nothing and leaves the set unchanged.

numbers = {10, 20, 30}
numbers.update([40, 50, 60]) # iterable list
print(numbers) # Output: {10, 20, 30, 40, 50, 60}

numbers.update({40, 50}) 
print(numbers) # Output: {10, 20, 30, 40, 50, 60} (duplicates 40, 50 are ignored)


## 3. remove() → Remove an item from the set
    # --> set.remove(item)
    # If the item is not found, it raises a KeyError.
    # If the set is empty, it raises a KeyError (because the item is not found).
    # Sets do not allow duplicates, so it simply removes the single unique instance of that item.
    # If the item is not provided, it will raise a TypeError. EX: numbers.remove() ---> TypeError: remove() takes exactly one argument (0 given)

numbers = {10, 20, 30, 40, 50} 
numbers.remove(40)
print(numbers) # Output: {10, 20, 30, 50}


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


## 17. set() → Return a mutable set
    # --> set(iterable)
    # If the iterable is empty, it returns an empty set.
    # If the iterable has items, it returns a mutable set with the items from the iterable
    # If the iterable is not provided, Calling set() with no arguments is perfectly valid
    # If the iterable is modified after the set() call, the set() will not be affected. If the set() is called again, it will return the updated result.
    # In Python, if you use empty curly braces {}, Python creates an empty dictionary, not an empty set. The only way to create an empty set is by calling set() with nothing inside the parentheses.

numbers = frozenset({10, 20, 30}) # here the numbers set become immutable
mutable_numbers = set(numbers) # ---> {10, 20, 30}
print(mutable_numbers) # Output: {10, 20, 30}

# Converting a list with duplicates
my_list = [10, 20, 20, 30]
my_set = set(my_list)
print(my_set) # Output: {10, 20, 30} (duplicates removed)

empty_dict = {}
print(type(empty_dict)) # Output: <class 'dict'>

empty_set = set()       # This is the correct way to make an empty set!
print(type(empty_set))  # Output: <class 'set'>


## 18. del() → Delete a set
    # --> del set
    ## del is a Keyword, not a Function:
    # In Python, del is a built-in statement (like if, for, or return), not a method or a function.
    # Because it is not a function, you should never use parentheses with it.
    # Incorrect: del(numbers) or del()
    # Correct: del numbers

    # If the set has items, it deletes the set.
    # del completely destroys the variable name, regardless of what is inside it. If you have an empty set (numbers = set()) and you use del numbers, the variable numbers is still completely deleted, and trying to print it will give you a NameError.
    # Once deleted, attempting to use or modify the variable will raise a NameError.

    # del is a fundamental Python keyword and not a function, trying to run it by itself without providing a variable behaves differently.
    # If you just type del by itself, or del(), Python will not give you a TypeError. It will give you a SyntaxError before the code even runs, because the grammar of the code is mathematically invalid to the Python interpreter.

numbers = {10, 20, 30}
del numbers # ---> set is deleted
print(numbers) # Output: NameError: name 'numbers' is not defined


## 19. in → Return True if an item is present in the set
    # --> item in set
    # If the set is empty, it returns False.
    # If the set has items, it returns True if an item is present in the set
    # set() creates an empty set. A set is perfectly iterable (even if it's empty). If you run 10 in set(), Python simply checks the empty set, sees that 10 is not there, and returns False.
    # You will only get a TypeError if the thing on the right side of in is a data type that cannot hold multiple items (like a single integer).
    # If you forget to provide the set and just write 10 in , Python will give you a SyntaxError before the code even runs, because the sentence is grammatically incomplete.
    # If the set is modified after the in call, the in will not be affected.

numbers = {10, 20, 30}
result = 10 in numbers # ---> True, because 10 is present in the set
print(result) # Output: True


## 20. not in → Return True if an item is not present in the set
    # --> item not in set
    # If the set is empty, it returns True.
    # If the set has items, it returns True if an item is not present in the set
    # If the set is modified after the not in call, the not in will not be affected. If the not in is called again, it will return the updated result.

numbers = {10, 20, 30}
result = 40 not in numbers # ---> True, because 40 is not present in the set
print(result) # Output: True


## 21.intersection_update() → Update the set with only the items that are present in both sets
    # --> set.intersection_update(set1, set2, ...)
    # Unlike intersection(), this does NOT return a new set. It modifies the original set in-place and returns None.
    # It removes any item from the original set that is not found in the provided sets.
    # If the provided set is empty, it will empty the original set (because they share no common items).
    # If no arguments are provided (e.g., numbers1.intersection_update()), it does nothing and leaves the set unchanged

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
numbers1.intersection_update(numbers2) # ---> {30}
print(numbers1) # Output: {30}

## 22. difference_update() → Remove items from the original set that exist in the provided sets
    # --> set.difference_update(set1, set2, ...)
    # This modifies the original set in-place and returns None.
    # It acts like subtraction: Original Set - Provided Sets.
    # If the provided sets are empty (or share no common items), the original set remains completely unchanged.
    # If no arguments are provided (e.g., numbers.difference_update()), it does nothing and leaves the set unchanged.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Modifies numbers1 by deleting anything that is also in numbers2
numbers1.difference_update(numbers2) 

print(numbers1) # Output: {10, 20}
print(numbers2) # Output: {30, 40, 50} (The provided set is NEVER modified!)


## 23. symmetric_difference_update() → Keep items present in either set, but NOT in both
    # --> set.symmetric_difference_update(set1)
    # TRAP: Unlike difference_update, this method takes EXACTLY ONE argument. 
    # If no argument is provided, or if multiple are provided, it raises a TypeError.
    # It modifies the original set in-place and returns None.
    # If the provided set is empty, the original set remains unchanged.
    # If the sets have zero common items, the original set becomes the union of both sets.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}

# Modifies numbers1: removes 30 (overlap) and adds 40, 50 (unique to numbers2)
numbers1.symmetric_difference_update(numbers2) 

print(numbers1) # Output: {10, 20, 40, 50}
print(numbers2) # Output: {30, 40, 50} (The second set is NEVER modified!)

