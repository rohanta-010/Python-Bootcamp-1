marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
marks.append(63) # This will change the original list -> [5, 2, 21, 5, 7, 63]
marks.pop() # by default it removes the last item -> [5, 2, 21, 5, 7]
marks.extend(extra_marks) # -> [5, 2, 21, 5, 7, 53, 23, 32]
print(marks)

# ============================================================
# PYTHON LIST METHODS
# ============================================================


## 1. append() → Add ONE item to the end of the list
    # --> list.append(item)
    # TRAP: This method modifies the original list in-place and evaluates to None.
    # It takes EXACTLY ONE argument. Passing zero or multiple arguments raises a TypeError.
    # It ALWAYS adds the argument as a single, solid object at the very end of the list.
    
    # NESTING TRAP: If you append another list (or any iterable), it does NOT unpack the items. 
    # It adds the entire iterable as a single nested item at the end of the list.
    # Appending an empty list [] adds an empty list as a single item.

numbers = [10, 20, 30]

# Adding a standard integer
numbers.append(40) 
print(numbers) # Output: [10, 20, 30, 40]

# The Nesting Trap: Adding another list
numbers.append([50, 60]) 
print(numbers) # Output: [10, 20, 30, 40, [50, 60]] (Added as ONE single nested item!)

# Adding an empty list
numbers.append([])
print(numbers) # Output: [10, 20, 30, 40, [50, 60], []]


## 2. extend() → Add MULTIPLE items at the end by unpacking an iterable
    # --> list.extend(iterable)
    # TRAP: Like append(), this modifies the list in-place and evaluates to None.
    # It takes STRICTLY ONE argument, which MUST be an iterable (list, tuple, set, string, generator, etc.).
    # Passing zero arguments or a non-iterable (like an integer: numbers.extend(50)) raises a TypeError.
    
    # UNPACKING: Unlike append(), extend() iterates over the argument and appends EACH element individually.
    # STRING TRAP: Passing a string (e.g., numbers.extend("AB")) unpacks each character separately: ['A', 'B'].
    # Passing an empty iterable (e.g., []) leaves the list completely unchanged.

numbers = [10, 20, 30]

# Extending with another list
numbers.extend([40, 50]) 
print(numbers) # Output: [10, 20, 30, 40, 50]

# Extending with a tuple
numbers.extend((60, 70))
print(numbers) # Output: [10, 20, 30, 40, 50, 60, 70]

# The String Trap: Strings are iterables!
numbers.extend("89")
print(numbers) # Output: [10, 20, 30, 40, 50, 60, 70, '8', '9']


## 3. insert() → Add ONE item at a specific index position
    # --> list.insert(index, item)
    # TRAP: Like append() and extend(), this modifies the list in-place and evaluates to None.
    # It takes EXACTLY TWO arguments: the position (index) and the object to insert.
    # The new item takes the specified index, and all existing items from that index onwards are shifted to the right.
    
    # EDGE CASES:
    # 1. Index out of bounds (High): If the index is greater than the length of the list, it safely acts like append() and adds the item to the very end. No IndexError is raised.
    # 2. Negative Indexing: If the index is negative, it inserts the item BEFORE the element currently at that negative index. (e.g., -1 inserts just before the very last item).
    
    # EXPERT TIP: Using list.insert(0, item) to add items to the front of a list is slow (O(n) time) because Python has to shift every single existing item in memory one step to the right. If you need to do this often, use 'collections.deque'!

numbers = [10, 20, 30]

# Standard Insert: Insert 15 at index 2
numbers.insert(2, 15)
print(numbers) # Output: [10, 20, 15, 30]

# Edge Case: Index far beyond the list length
numbers.insert(100, 99)
print(numbers) # Output: [10, 20, 15, 30, 99] (Safely appended to the end!)

# The Negative Index Trap: Insert at -1
numbers.insert(-1, 88)
print(numbers) # Output: [10, 20, 15, 30, 88, 99] (Inserted BEFORE 99!)


## 4. remove() → Remove the FIRST occurrence of a specific value
    # --> list.remove(value)
    # TRAP: This method modifies the original list in-place and evaluates to None. It does NOT return the removed item!
    # It searches the list from left to right and removes ONLY the very first instance of the exact value you pass in.
    
    # THE ERROR TRAP: If the value does not exist in the list (or if the list is completely empty), it crashes with a ValueError.
    
    # EXPERT TIP: Because of the ValueError crash risk, it is best practice to check if the item exists using the 'in' operator before trying to remove it.
    # e.g., if 20 in numbers: numbers.remove(20)

numbers = [10, 20, 30, 20]

# Removes ONLY the first 20 it finds
numbers.remove(20) 
print(numbers) # Output: [10, 30, 20] (The second 20 is still there!)

# The Error Trap: Trying to remove an item that doesn't exist
# numbers.remove(100) # ---> ValueError: list.remove(x): x not in list

# Safe Removal Example:
if 100 in numbers:
    numbers.remove(100)
else:
    print("Item not found, safe to continue!") # Output: Item not found, safe to continue!


## 5. pop() → Remove an item by INDEX and return it
    # --> list.pop([index])
    # TRAP: Unlike remove() or append(), this method modifies the list AND evaluates to the removed item (it does NOT return None).
    # The index argument is OPTIONAL. If you don't provide one, it defaults to -1 (removes and returns the very LAST item).
    
    # THE ERROR TRAP: If the list is completely empty, or if you provide an index that is out of bounds, it crashes with an IndexError.
    
    # EXPERT TIP: Using pop() with no arguments to remove the last item is extremely fast (O(1) time). However, using pop(0) to remove the first item is slow (O(n) time) because Python has to shift every remaining item one step to the left!

numbers = [10, 20, 30, 40]

# Standard Pop: Remove and return the item at index 1
removed_item = numbers.pop(1)
print(removed_item) # Output: 20
print(numbers)      # Output: [10, 30, 40]

# Default Pop: No argument provided (removes the last item)
last_item = numbers.pop()
print(last_item)    # Output: 40
print(numbers)      # Output: [10, 30]

# The Error Trap:
# numbers.pop(100) # ---> IndexError: pop index out of range

# empty_list = []
# empty_list.pop() # ---> IndexError: pop from empty list


## 6. index() → Return the index of the FIRST occurrence of a specific value
    # --> list.index(value, [start], [end])
    # TRAP: Unlike the previous adding/removing methods, this does NOT modify the list! It simply evaluates to an integer (the index).
    # It searches the list from left to right and returns the position of ONLY the very first instance it finds.
    
    # THE ERROR TRAP: Just like remove(), if the value does not exist in the list, it crashes with a ValueError.
    
    # EXPERT TIP: You can pass optional 'start' and 'end' arguments to limit your search to a specific slice of the list. 
    # Also, to completely avoid the ValueError crash, always verify the item is in the list first using the 'in' operator!

numbers = [10, 20, 30, 20, 40]

# Standard Search: Returns the index of the very first '20'
first_index = numbers.index(20)
print(first_index) # Output: 1

# The Error Trap:
# numbers.index(100) # ---> ValueError: 100 is not in list

# Safe Search Example:
if 100 in numbers:
    print(numbers.index(100))
else:
    print("Not found!") # Output: Not found!

# EXPERT TIP: Searching with a start position
# Let's find the index of '20', but tell Python to start searching from index 2
second_index = numbers.index(20, 2)
print(second_index) # Output: 3


## 7. count() → Return the total number of times a specific value appears
    # --> list.count(value)
    # TRAP: Like index(), this does NOT modify the list! It simply evaluates to an integer.
    # SAFE METHOD: Unlike remove() or index(), this method NEVER crashes with a ValueError. 
    # If the item is not found (or if the list is completely empty), it safely returns 0.
    
    # EXPERT TIP: count() has to scan the entire list from start to finish (O(n) time). 
    # If you need to count the occurrences of EVERY item in a large list, do not use a loop with .count()! 
    # Instead, import 'Counter' from the 'collections' module—it counts everything in a single, lightning-fast pass.

numbers = [10, 20, 30, 20, 20]

# Standard Count: How many times does 20 appear?
total_twenties = numbers.count(20)
print(total_twenties) # Output: 3

# The Safe Fallback: Item not in list
total_hundreds = numbers.count(100)
print(total_hundreds) # Output: 0 (No crash!)

# Empty list behavior
empty_list = []
print(empty_list.count(10)) # Output: 0


## 8. sort() → Sort the list in ascending order (IN-PLACE)
    # --> list.sort(key=None, reverse=False)
    # TRAP: This method modifies the original list in-place and evaluates to None! 
    # (Never do: my_list = my_list.sort() — you will lose your list entirely!)
    
    # THE ERROR TRAP: Python needs to know how to mathematically/alphabetically compare the items. 
    # If the list contains mixed, uncomparable types (like integers and strings), it crashes with a TypeError.
    
    # EXPERT TIP 1: You can use the 'reverse=True' argument to sort backwards (descending).
    # EXPERT TIP 2: You can use the 'key' argument to pass a function for custom sorting (like sorting strings by length instead of alphabetically).
    # EXPERT TIP 3: If you want to keep your original list unsorted and create a brand-new sorted copy, do NOT use list.sort(). Instead, use Python's built-in sorted(list) function!

numbers = [30, 10, 20, 50, 40]

# Standard Sort (Ascending)
numbers.sort() 
print(numbers) # Output: [10, 20, 30, 40, 50]

# Reverse Sort (Descending)
numbers.sort(reverse=True) 
print(numbers) # Output: [50, 40, 30, 20, 10]

# The Type Error Trap:
# mixed_list = [10, "Apple", 20]
# mixed_list.sort() # ---> TypeError: '<' not supported between instances of 'str' and 'int'

# EXPERT TIP: Custom Sorting using 'key'
words = ["strawberry", "apple", "fig", "banana"]

# Sort by the LENGTH of the string (shortest to longest) instead of alphabetically
words.sort(key=len)
print(words) # Output: ['fig', 'apple', 'banana', 'strawberry']


## 9. reverse() → Reverse the current order of the list (IN-PLACE)
    # --> list.reverse()
    # TRAP: Just like append() and sort(), this method modifies the original list in-place and evaluates to None.
    # (Never do: my_list = my_list.reverse() — you will wipe out your list!)
    
    # HOW IT WORKS: It blindly flips the list front-to-back. It does NOT sort the items mathematically or alphabetically. 
    # Because it doesn't compare the elements, a list with mixed data types is perfectly fine (no TypeError!).
    
    # EXPERT TIP: If you want to keep your original list intact and create a brand-new reversed copy, do NOT use list.reverse(). 
    # Instead, use list slicing: reversed_list = my_list[::-1] 
    # OR use Python's built-in function: reversed_list = list(reversed(my_list))

numbers = [10, 20, 30]

# Standard Reverse
numbers.reverse()
print(numbers) # Output: [30, 20, 10]

# Mixed Data Types are totally fine!
items = [10, "hello", 3.14, True]
items.reverse()
print(items) # Output: [True, 3.14, 'hello', 10]

# EXPERT TIP: Creating a reversed copy WITHOUT modifying the original
original = ['A', 'B', 'C']
new_reversed_list = original[::-1] # Slicing magic!

print(original)          # Output: ['A', 'B', 'C'] (Original is safe!)
print(new_reversed_list) # Output: ['C', 'B', 'A'] (Brand new list!)


## 10. clear() → Remove all items from the list
    # --> list.clear()
    # TRAP: This method modifies the original list in-place and evaluates to None.
    # It completely wipes out all elements, leaving behind an empty list [].
    # If the list is already empty, it safely does nothing (no errors raised).
    
    # EXPERT TIP: There is a massive difference between 'my_list.clear()' and 'my_list = []'.
    # 'my_list.clear()' empties the EXACT list in memory. If other variables are linked to that same list, they will be emptied too!
    # 'my_list = []' just reassigns your variable to a brand NEW empty list, leaving the original data intact for any other variables still pointing to it.

numbers = [10, 20, 30]

# Standard Clear
numbers.clear() 
print(numbers) # Output: []

# ---------------------------------------------------------
# EXPERT TIP IN ACTION: .clear() vs = []
# ---------------------------------------------------------

# Scenario A: Using .clear() (Affects all linked variables)
list_a = [1, 2, 3]
list_b = list_a       # list_b points to the EXACT SAME list in memory as list_a

list_a.clear()        # Empties the actual list in memory
print(list_b)         # Output: [] (list_b is wiped out too!)

# Scenario B: Using = [] (Safely reassigns without destroying)
list_x = [1, 2, 3]
list_y = list_x       # list_y points to the same list

list_x = []           # Points list_x to a brand NEW empty list
print(list_y)         # Output: [1, 2, 3] (list_y is safe and still holds the original data!)


## 11. copy() → Return a SHALLOW copy of the list
    # --> list.copy()
    # TRAP: Unlike append() or sort(), this method DOES return a value (the new list object) and does NOT modify the original list.
    # It creates a "shallow copy." This means it builds a brand new outer list, but fills it with REFERENCES to the exact same items that were in the original list.
    
    # THE NESTING TRAP: If your list contains flat, immutable objects (like integers, strings, tuples), the copy behaves perfectly safely. 
    # BUT, if your list contains MUTABLE objects (like nested lists or dictionaries), modifying the INSIDE of those nested objects will affect BOTH the original and the copy!
    
    # EXPERT TIP 1: You can also create a shallow copy using list slicing, which is very common in Python: new_list = my_list[:]
    # EXPERT TIP 2: If you have nested lists/dicts and need a true, 100% completely independent copy, you must use a "Deep Copy" by importing Python's built-in 'copy' module.

# ---------------------------------------------------------
# Scenario A: Flat list with immutable objects (SAFE)
# ---------------------------------------------------------
original = [10, 20, 30]
copied = original.copy()

# Modifying a flat item in the copy
copied[0] = 99 

print(original) # Output: [10, 20, 30] (Original is perfectly safe!)
print(copied)   # Output: [99, 20, 30]


# ---------------------------------------------------------
# Scenario B: Nested list with mutable objects (THE TRAP)
# ---------------------------------------------------------
nested_original = [[1, 2], [3, 4]]
nested_copy = nested_original.copy()

# Modifying the inner list inside the copy
nested_copy[0][0] = 99 

# Both lists are affected because they share the same inner list in memory!
print(nested_original) # Output: [[99, 2], [3, 4]]  <-- DISASTER!
print(nested_copy)     # Output: [[99, 2], [3, 4]]



import copy

# 1. THE SHALLOW COPY PROBLEM 
original_list = [[1, 2], [3, 4]]
shallow_copied_list = original_list.copy()

# Modifying the nested mutable object affects BOTH lists
shallow_copied_list[0][0] = 99
print(f"Original after shallow copy: {original_list}") 
# Output: [[99, 2], [3, 4]]


# 2. THE DEEP COPY SOLUTION
original_list_2 = [[1, 2], [3, 4]]
# copy.deepcopy() recursively copies all nested objects
deep_copied_list = copy.deepcopy(original_list_2)

# Modifying the nested object now ONLY affects the copied list
deep_copied_list[0][0] = 99
print(f"Original after deep copy: {original_list_2}")
# Output: [[1, 2], [3, 4]]
print(f"Deep copied list:         {deep_copied_list}")
# Output: [[99, 2], [3, 4]]


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
└── copy()     → create a separate list i.e Shallow copy (default)

"""


