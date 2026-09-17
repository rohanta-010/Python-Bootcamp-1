class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now....")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof!")

a = Animal("Dog") # a is directly an Animal object.
a.speak()
print("*")
d = Dog("Bruno")
d.speak()
print(d.location)
