marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
# marks.append(63) # This will change the original list
# marks.pop()
marks.extend(extra_marks)
print(marks)

# ============================================================
# PYTHON LIST METHODS
# ============================================================

numbers = [10, 20, 30, 40]

## 1.append() → Add ONE item at the end
    #  --> list.append(item)
    #  If the item is a list, it will be added as a single item (nested list).
    #  If the item is not a list, it will be added as a single item.
    #  If the item is empty, it will be added as a single item (empty list). EX: numbers.append([]) ---> [10, 20, 30, 40, []]
    #  If the item is not provided, it will raise a TypeError. EX: numbers.append() ---> TypeError: append() takes exactly one argument (0 given)
    #  If the list is empty, it will add the item to the list.

numbers = [10, 20, 30] # ---> [10, 20, 30, 40]
numbers.append(40)
print(numbers)

numbers.append([40, 50]) # ---> [10, 20, 30, [40, 50]]
print(numbers)
# It adds the entire list as one item.


## 2.extend() → Add MULTIPLE items at the end / extend the existing list with items from another iterable
    #  --> list.extend(iterable)    
    #  If the iterable is not a list, it will still work as long as it is iterable (like a tuple, set, etc.). example: numbers.extend((60, 70)) or numbers.extend({80, 90})
    #  If the iterable is empty, it will not change the list.
    #  If the iterable is not provided, it will raise a TypeError. EX: numbers.extend() ---> TypeError: extend() takes exactly one argument (0 given)
    #  If the list is empty, it will add the items from the iterable to the list.

numbers = [10, 20, 30] # ---> [10, 20, 30, 40, 50]
numbers.extend([40, 50])
print(numbers)


## 3.insert() → Add an item at a specific index
    #  --> list.insert(index, item)
    #  If the index is greater than the length of the list, the item will be added at the end.
    #  If the list is empty, the item will be added at index 0.

numbers = [10, 20, 30] # ---> [10, 20, 15, 30]
numbers.insert(2, 15)
print(numbers)


## 4.remove() → Remove the first occurrence/value of an item
    #  --> list.remove(item)   
    #  If the item is not found, it raises a ValueError.
    #  If the item is found multiple times, only the first occurrence is removed.
    #  If the list is empty, it raises a ValueError.

numbers = [10, 20, 30, 20] # ---> [10, 30, 20]
numbers.remove(20)
# numbers.remove(100) # ValueError: list.remove(x): x not in list
print(numbers)


## 5.pop() → Remove an item at a specific index and return it
    #  --> list.pop(index)
    #  If the index is not provided, it removes and returns the last item in the list.
    #  If the index is out of range, it raises an IndexError.
    #  If the list is empty, it raises an IndexError.
    
numbers = [10, 20, 30] # ---> [10, 30]
removed_item = numbers.pop(1)
print(removed_item)
print(numbers)


## 6.index() → Return the index of the first occurrence of an item
    #  --> list.index(item)
    #  If the item is not found, it raises a ValueError.
    #  If the item is found multiple times, it returns the index of the first occurrence.
    #  If the list is empty, it raises a ValueError.

numbers = [10, 20, 30, 20]
index = numbers.index(20)
print(index)  # Output: 1


## 7.count() → Return the number of occurrences of an item
    #  --> list.count(item)
    #  If the item is not found, it returns 0.
    #  If the item is found multiple times, it returns the count of occurrences.
    #  If the list is empty, it returns 0.

numbers = [10, 20, 30, 20]
count = numbers.count(20)
print(count)  # Output: 2


## 8.sort() → Sort the list in ascending order
    #  --> list.sort()
    #  If the list is empty, it remains empty.
    #  If the list contains items of different types or that are not comparable, it raises a TypeError.

numbers = [30, 10, 20]
numbers.sort()  
print(numbers)  # Output: [10, 20, 30]

numbers.sort(reverse=True)  # Sort in descending order
print(numbers)  # Output: [30, 20, 10]


## 9.reverse() → Reverse the order of the list
    #  --> list.reverse()
    #  If the list is empty, it remains empty.
    #  doesn't compare elements → different types are fine 
    #  reverse() does not sort the list, it simply reverses the existing order.

numbers = [10, 20, 30]
numbers.reverse()
print(numbers)  # Output: [30, 20, 10]

items = [10, "hello", 3.14, True]
items.reverse()
print(items) # Output: [True, 3.14, "hello", 10]


## 10.clear() → Remove all items from the list
    #  --> list.clear()
    #  If the list is empty, it remains empty.
    #  clear() does not return any value, it simply empties the list.

numbers = [10, 20, 30]
numbers.clear() 
print(numbers)  # Output: []


## 11.copy() → Return a shallow copy of the list
    #  --> list.copy()
    #  If the list is empty, it returns an empty list.
    #  copy() creates a shallow copy, meaning that it copies the references of the objects in the list, not the objects themselves. If the list contains mutable objects (like other lists), changes to those objects will be reflected in both the original and copied lists. Example: original_list = [[1, 2], [3, 4]]; copied_list = original_list.copy(); copied_list[0][0] = 99; print(original_list)  # Output: [[99, 2], [3, 4]]
    #  If the list contains immutable objects (like numbers, strings, tuples), changes to those objects will not affect the original list. Example: original_list = [1, 2, 3]; copied_list = original_list.copy(); copied_list[0] = 99; print(original_list)  # Output: [1, 2, 3]

numbers = [10, 20, 30]
copied_numbers = numbers.copy()
print(copied_numbers)  # Output: [10, 20, 30]


"""

ADDING
│
├── append()   → add ONE at end
├── extend()   → add MANY
└── insert()   → add at specific INDEX


REMOVING
│
├── remove()   → remove by VALUE
├── pop()      → remove by INDEX
└── clear()    → remove EVERYTHING


SEARCHING
│
├── index()    → VALUE → INDEX
└── count()    → VALUE → HOW MANY?


ORDER
│
├── sort()     → arrange items
└── reverse()  → reverse existing order


COPYING
│
└── copy()     → create a separate list

"""


