marks = {"harry": 34, "jack": 45, "lily": 94 }
# we cannot have list as key in dictionary because list is mutable and unhashable. Here hashable means that the object has a hash value which remains constant during its lifetime. If the hash value of an object changes, it can lead to unexpected behavior when using that object as a key in a dictionary. Since lists are mutable and their contents can change, they do not have a fixed hash value and therefore cannot be used as keys in dictionaries. EX: marks = {[1, 2, 3]: "value"} # TypeError: unhashable type: 'list'.

# print(marks, type(marks))
print(marks["lily"])
marks["harry"] = 3
print(marks)