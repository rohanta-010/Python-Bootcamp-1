# ============================================================
# SHALLOW COPY vs DEEP COPY
# ============================================================

### Shallow Copy:
# Creates a new outer object, but nested/mutable objects inside it may still be shared.
#
## Example:

print("Shallow copy: ")
numbers = [[10, 20], [30, 40]]
copied_numbers = numbers.copy()

copied_numbers[0][0] = 99

print(numbers)
print(copied_numbers)

# Output:
# [[99, 20], [30, 40]]
# [[99, 20], [30, 40]]
#
# The inner list is shared, so changing it affects both.


### Deep Copy:
# Creates a completely independent copy, including nested objects.
#
## Example:
import copy

print("\nDeep copy: ")
numbers = [[10, 20], [30, 40]]
copied_numbers = copy.deepcopy(numbers)

copied_numbers[0][0] = 99

print(numbers)
print(copied_numbers)

# Output:
# [[10, 20], [30, 40]]
# [[99, 20], [30, 40]]
#
# The nested lists are also copied, so changes do not affect the original.

## MEMORY TRICK:
#
# Shallow copy → New outer object + shared inner objects
# Deep copy    → New outer object + new inner objects
#
# list.copy()          → Shallow copy
# copy.copy()          → Shallow copy
# copy.deepcopy()      → Deep copy
# ============================================================