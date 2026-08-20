### Dictionary keys must be hashable.
#
# Hashable means an object has a hash value that remains consistent during its lifetime.
#
# -> Mutable objects such as lists can change their contents, so they are not hashable and cannot be dictionary keys.
# -> Mutable objects generally cannot be dictionary keys; immutable/hashable objects can.
#
## Example:
# marks = {[1, 2, 3]: "value"}
#
# TypeError: unhashable type: 'list'
#
# -> Strings and integers are immutable and hashable, so they can be dictionary keys.
#
## Example:
# marks = {"harry": 34, "jack": 45}
# → Valid
#
# -> A tuple can also be a dictionary key if all its elements are hashable.
#
## Example:
# locations = {(10, 20): "Point A"}
# → Valid


marks = {"harry": 34, "jack": 45, "lily": 94 }

print(marks, type(marks))
print(marks["lily"])
marks["harry"] = 3
print(marks)
