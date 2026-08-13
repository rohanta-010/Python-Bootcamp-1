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

numbers = {10, 20, 30}  # ---> {10, 20, 30, 40}
numbers.add(40)
print(numbers)


## 2. update() → Add MULTIPLE elements
    # --> set.update(elemets) 
    # If the elements are not iterable, it will raise a TypeError. EX: numbers.update(50) ---> TypeError: 'int' object is not iterable
    # If the elements are already present, it does nothing.
    # If the set is empty, it will add the elements to the set.
    # If the elements are empty, it will not change the set.
    # If the elements are not provided, it will raise a TypeError. EX: numbers.update() ---> TypeError: update expected at least 1 argument (0 given)

numbers = {10, 20, 30}  # ---> {10, 20, 30, 40, 50, 60}
numbers.update([40, 50, 60]) # iterable list
print(numbers)

numbers.update({40, 50}) # ---> {10, 20, 30, 40, 50} 
print(numbers)


## 3.remove() → Remove an item from the set
    # --> set.remove(item)
    # If the item is not found, it raises a KeyError.
    # If the set is empty, it raises a KeyError.
    # If the item is found multiple times, it removes only one occurrence (since sets do not allow duplicates, this is not applicable).EX numbers.remove(40) ---> {10, 20, 30, 50, 60}. Here, 40 is removed from the set.
    # If the item is not provided, it will raise a TypeError. EX: numbers.remove() ---> TypeError: remove() takes exactly one argument (0 given)

numbers = {10, 20, 30, 40, 50} # ---> {10, 20, 30, 50}
numbers.remove(40)
print(numbers)


## 4.discard() → Remove an item from the set if it exists
    # --> set.discard(item)
    # If the item is not found, it does nothing.
    # If the set is empty, it does nothing.
    # difference between remove and discard is that remove will throw an error if the item is not present in the set, while discard will not throw an error if the item is not present in the set.

numbers = {10, 20, 30, 40, 50} # ---> {10, 20, 30, 50}
numbers.discard(40)
print(numbers)


## 5.pop() → Remove and return an arbitrary item from the set
    # --> set.pop()
    # If the set is empty, it raises a KeyError.
    # If the set has only one item, it removes and returns that item.
    # If the set has multiple items, it removes and returns an arbitrary item (not necessarily the first item).
    # If the item is provided, it will raise a TypeError. EX: numbers.pop(1) ---> TypeError: pop() takes no arguments (1 given)
    # No argument is needed for pop() method. It removes and returns an arbitrary item from the set. Just an random item is removed from the set, not the first item. 

numbers = {10, 20, 30} # ---> {20, 30}
removed_item = numbers.pop()
print(removed_item)
print(numbers)


## 6.clear() → Remove all items from the set
    # --> set.clear()
    # If the set is empty, it does nothing.
    # If the set is not empty, it removes all items from the set.
    # If the item is provided, it will raise a TypeError. EX: numbers.clear(1) ---> TypeError: clear() takes no arguments (1 given)

numbers = {10, 20, 30} # ---> set()
numbers.clear()
print(numbers)


## 7.union() → Return a new set with all items from both sets
    # --> set.union(set1, set2, ...)
    # If the sets are empty, it returns an empty set.
    # If the sets have items, it returns a new set with all items from both sets.
    # If the sets have duplicate items, it returns a new set with only unique items.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.union() ---> TypeError: union() takes at least 1 argument (0 given)

    # using operartor | (pipe) to perform union operation on two sets. It perform's the same operation as union() method. 

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1.union(numbers2) # ---> {10, 20, 30, 40, 50}
print(result)

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1 | numbers2 # ---> {10, 20, 30, 40, 50}
print(result)


## 8.intersection() → Return a new set with only the items that are present in both sets
    # --> set.intersection(set1, set2, ...)
    # If the sets are empty, it returns an empty set.
    # If the sets have items, it returns a new set with only the items that are present in both sets.
    # If the sets have no common items, it returns an empty set.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.intersection() ---> TypeError: intersection() takes at least 1 argument (0 given)

    # using operator & (ampersand) to perform intersection operation on two sets. It perform s the same operation as intersection() method.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1.intersection(numbers2) # ---> {30}
print(result)

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1 & numbers2 # ---> {30}
print(result)


## 9.difference() → Return a new set with only the items that are present in the first set but not in the second set
    # --> set.difference(set1, set2, ...)
    # If the sets are empty, it returns an empty set.
    # If the sets have items, it returns a new set with only the items that are present in the first set but not in the second set.
    # If the sets have no common items, it returns a new set with all items from the first set.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.difference() ---> TypeError: difference() takes at least 1 argument (0 given)
    
    # using operator - (minus) to perform difference operation on two sets. It perform s the same operation as difference() method.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1.difference(numbers2) # ---> {10, 20}
print(result)

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1 - numbers2 # ---> {10, 20}
print(result)


## 10.symmetric_difference() → Return a new set with only the items that are present in either set but not in both sets
    # --> set.symmetric_difference(set1, set2, ...)
    # If the sets are empty, it returns an empty set.
    # If the sets have items, it returns a new set with only the items that are present in either set but not in both sets.
    # If the sets have no common items, it returns a new set with all items from both sets.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.symmetric_difference() ---> TypeError: symmetric_difference() takes at least 1 argument (0 given)

    # using operator ^ (caret) to perform symmetric difference operation on two sets. It perform s the same operation as symmetric_difference() method.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1.symmetric_difference(numbers2) # ---> {10, 20, 40, 50}
print(result)

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
result = numbers1 ^ numbers2 # ---> {10, 20, 40, 50}
print(result)


## 11.issubset() → Return True if all items of the set are present in another set
    # --> set.issubset(set1, set2, ...)
    # If the sets are empty, it returns True.
    # If the sets have items, it returns True if all items of the set are present in another set.
    # If the sets have no common items, it returns False.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.issubset() ---> TypeError: issubset() takes at least 1 argument (0 given)    
    # If the set is modified after the issubset() call, the issubset() will not be affected. If the issubset() is called again, it will return the updated result.

numbers1 = {10, 20, 30}
numbers2 = {10, 20, 30, 40, 50}
result = numbers1.issubset(numbers2) # ---> True, because all items of numbers1 are present in numbers2
print(result) # Output: True


## 12.issuperset() → Return True if all items of another set are present in the set
    # --> set.issuperset(set1, set2, ...)
    # If the sets are empty, it returns True.
    # If the sets have items, it returns True if all items of another set are present in the set.
    # If the sets have no common items, it returns False.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.issuperset() ---> TypeError: issuperset() takes at least 1 argument (0 given)
    # If the set is modified after the issuperset() call, the issuperset() will not be affected. If the issuperset() is called again, it will return the updated result.

numbers1 = {10, 20, 30, 40, 50}
numbers2 = {10, 20, 30}
result = numbers1.issuperset(numbers2) # ---> True, because all items of numbers2 are present in numbers1
print(result) # Output: True


## 13.copy() → Return a shallow copy of the set
    # --> set.copy()
    # If the set is empty, it returns an empty set.
    # If the set has items, it returns a shallow copy of the set.
    # If the set is not provided, it will raise a TypeError. EX: numbers.copy() ---> TypeError: copy() takes no arguments (1 given)
    # If the set is modified after the copy, the copy will not be affected. If the copy is modified, the original set will not be affected.Example: numbers = {10, 20, 30} # ---> {10, 20, 30} numbers_copy = numbers.copy() numbers_copy.add(40) print(numbers) Output: {10, 20, 30} print(numbers_copy) # Output: {10, 20, 30, 40} similarly vice varsa, if the original set is modified, the copy will not be affected. If the copy is modified, the original set will not be affected.

numbers = {10, 20, 30} # immutable. The set itself is actually mutable (which is why you can use .add(40) on it). It is the numbers inside it that are immutable. If you want a truly immutable set where you can't even use .add(), Python has a built-in type called frozenset.
numbers_copy = numbers.copy() # ---> {10, 20, 30}
numbers_copy.add(40) # ---> {10, 20, 30, 40}
print(numbers) # Output: {10, 20, 30} 
print(numbers_copy) # Output: {10, 20, 30, 40}



## 14.len() → Return the number of items in the set
    # --> len(set)
    # If the set is empty, it returns 0.
    # If the set has items, it returns the number of items in the set.
    # If the set is not provided, it will raise a TypeError. EX: len() ---> TypeError: len() takes exactly one argument (0 given)
    # If the set is modified after the len() call, the len() will not be affected. If the len() is called again, it will return the updated length of the set.


numbers = {10, 20, 30}
length = len(numbers) # ---> 3
print(length) # Output: 3


## 15.isdisjoint() → Return True if two sets have no common items
    # --> set.isdisjoint(set1, set2, ...)
    # If the sets are empty, it returns True.
    # If the sets have items, it returns True if two sets have no common items.
    # If the sets have common items, it returns False.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.isdisjoint() ---> TypeError: isdisjoint() takes at least 1 argument (0 given)
    # If the sets are modified after the isdisjoint() call, the isdisjoint() will not be affected. If the isdisjoint() is called again, it will return the updated result.

numbers1 = {10, 20, 30}
numbers2 = {40, 50, 60}
result = numbers1.isdisjoint(numbers2) # ---> True, because numbers1 and numbers2 have no common items
print(result) # Output: True


## 16. frozenset() → Return an immutable set
    # --> frozenset(iterable)
    # If the iterable is empty, it returns an empty frozenset.
    # If the iterable has items, it returns an immutable set with the items from the iterable
    # If the iterable is not provided, Calling frozenset() without providing an iterable will not raise a TypeError; instead, it safely returns an empty, immutable frozenset() object i.e : # Output: frozenset().
    # If the iterable is modified after the frozenset() call, the frozenset() will not be affected. If the frozenset() is called again, it will return the updated result.

numbers = {10, 20, 30}
immutable_numbers = frozenset(numbers) # ---> frozenset({10, 20, 30})
print(immutable_numbers) # Output: frozenset({10, 20, 30})


# Format:
###frozenset(iterable)
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
# immutable_numbers.add(40)    # X AttributeError : AttributeError: 'frozenset' object has no attribute 'add'
# immutable_numbers.remove(10) # X AttributeError : AttributeError: 'frozenset' object has no attribute 'remove'
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
# frozenset() is also valid and returns an empty frozenset.
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
# A frozenset is immutable and can be an element of another set.
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

