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
    # If the elements are not provided, it will raise a TypeError. EX: numbers.update() ---> TypeError: update expected at least 1 argument, got 0

numbers = {10, 20, 30}  # ---> {10, 20, 30, 40, 50, 60}
numbers.update([40, 50, 60])
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

    # using operartor | (pipe) to perform union operation on two sets. It perform s the same operation as union() method. 

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
    # If the set is modified after the copy, the copy will not be affected. If the copy is modified, the original set will not be affected ex for example: numbers = {10, 20, 30} # ---> {10, 20, 30} numbers_copy = numbers.copy() numbers_copy.add(40) print(numbers) Output: {10, 20, 30} print(numbers_copy) # Output: {10, 20, 30, 40} similarly vice varsa, if the original set is modified, the copy will not be affected. If the copy is modified, the original set will not be affected.

numbers = {10, 20, 30}
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
    # If the iterable is not provided, it will raise a TypeError. EX: frozenset() ---> TypeError: frozenset() takes exactly one argument (0 given)
    # If the iterable is modified after the frozenset() call, the frozenset() will not be affected. If the frozenset() is called again, it will return the updated result.

numbers = {10, 20, 30}
immutable_numbers = frozenset(numbers) # ---> frozenset({10, 20, 30})
print(immutable_numbers) # Output: frozenset({10, 20, 30})


## 17. set() → Return a mutable set
    # --> set(iterable)
    # If the iterable is empty, it returns an empty set.
    # If the iterable has items, it returns a mutable set with the items from the iterable
    # If the iterable is not provided, it will raise a TypeError. EX: set() ---> TypeError: set() takes exactly one argument (0 given)
    # If the iterable is modified after the set() call, the set() will not be affected. If the set() is called again, it will return the updated result.

numbers = frozenset({10, 20, 30})
mutable_numbers = set(numbers) # ---> {10, 20, 30}
print(mutable_numbers) # Output: {10, 20, 30}


## 18. del() → Delete a set
    # --> del set
    # If the set is empty, it does nothing.
    # If the set has items, it deletes the set.
    # If the set is not provided, it will raise a TypeError. EX: del() ---> TypeError: del() takes exactly one argument (0 given)
    # If the set is modified after the del() call, the del() will not be affected. If the del() is called again, it will return the updated result.

numbers = {10, 20, 30}
del numbers # ---> set is deleted
print(numbers) # Output: NameError: name 'numbers' is not defined


## 19. in → Return True if an item is present in the set
    # --> item in set
    # If the set is empty, it returns False.
    # If the set has items, it returns True if an item is present in the set
    # If the set is not provided, it will raise a TypeError. EX: 10 in set() ---> TypeError: argument of type 'set' is not iterable
    # If the set is modified after the in call, the in will not be affected. If the in is called again, it will return the updated result.

numbers = {10, 20, 30}
result = 10 in numbers # ---> True, because 10 is present in the set
print(result) # Output: True


## 20. not in → Return True if an item is not present in the set
    # --> item not in set
    # If the set is empty, it returns True.
    # If the set has items, it returns True if an item is not present in the set
    # If the set is not provided, it will raise a TypeError. EX: 10 not in set() ---> TypeError: argument of type 'set' is not iterable
    # If the set is modified after the not in call, the not in will not be affected. If the not in is called again, it will return the updated result.

numbers = {10, 20, 30}
result = 40 not in numbers # ---> True, because 40 is not present in the set
print(result) # Output: True


## 21.intersection_update() → Update the set with only the items that are present in both sets
    # --> set.intersection_update(set1, set2, ...)
    # If the sets are empty, it does nothing.
    # If the sets have items, it updates the set with only the items that are present in both sets.
    # If the sets have no common items, it updates the set to be empty.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.intersection_update() ---> TypeError: intersection_update() takes at least 1 argument (0 given)
    # If the set is modified after the intersection_update() call, the intersection_update() will not be affected. If the intersection_update() is called again, it will return the updated result.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
numbers1.intersection_update(numbers2) # ---> {30}
print(numbers1) # Output: {30}

## 22.difference_update() → Update the set with only the items that are present in the first set but not in the second set
    # --> set.difference_update(set1, set2, ...)
    # If the sets are empty, it does nothing.
    # If the sets have items, it updates the set with only the items that are present in the first set but not in the second set.
    # If the sets have no common items, it updates the set to be the same as the first set.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.difference_update() ---> TypeError: difference_update() takes at least 1 argument (0 given)
    # If the set is modified after the difference_update() call, the difference_update() will not be affected. If the difference_update() is called again, it will return the updated result.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
numbers1.difference_update(numbers2) # ---> {10, 20}
print(numbers1) # Output: {10, 20}


## 23.symmetric_difference_update() → Update the set with only the items that are present in either set but not in both sets
    # --> set.symmetric_difference_update(set1, set2, ...)
    # If the sets are empty, it does nothing.
    # If the sets have items, it updates the set with only the items that are present in either set but not in both sets.
    # If the sets have no common items, it updates the set to be the same as the union of both sets.
    # If the sets are not provided, it will raise a TypeError. EX: numbers.symmetric_difference_update() ---> TypeError: symmetric_difference_update() takes at least 1 argument (0 given)
    # If the set is modified after the symmetric_difference_update() call, the symmetric_difference_update() will not be affected. If the symmetric_difference_update() is called again, it will return the updated result.

numbers1 = {10, 20, 30}
numbers2 = {30, 40, 50}
numbers1.symmetric_difference_update(numbers2) # ---> {10, 20, 40, 50}
print(numbers1) # Output: {10, 20, 40, 50}

