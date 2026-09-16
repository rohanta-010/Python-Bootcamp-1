# Oops is basically a way to model what we write in a program in real world

# Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance created from the template (class.). Eg. Form which contains the data for John Doe

class Employee:
    company = "HP"

    def get_salary(self): 
        # self is important here because self is a way to reference the object of the class which is being created
        # it's mandatory to give the first (1st) parameter as self/other for all the functions/methods we are defining inside a class
        print(self)
        return 34000


e1 = Employee() # An Object of class Employee is created here
print(e1.get_salary()) # Employee e's get salary method is called

print("*")

e2 = Employee()
print(e2.get_salary())
print(e2.company)

print("*")


# ============================================================
## self IN PYTHON CLASSES
# ============================================================

# When we create an object from a class: 
#   e1 = Employee()
#
# and call an instance method:
#   e1.get_salary()
#
# Python automatically passes the object (e1) to the method.

# Internally, this is approximately equivalent to:
#   Employee.get_salary(e1)
#
# Therefore, the method needs a first parameter to receive that object.
# By convention, this first parameter is called `self`.


class Employee:

    def get_salary(self):
        # `self` refers to the current object.
        # If we call e1.get_salary(), self refers to e1.
        # If we call e2.get_salary(), self refers to e2.

        print(self)
        return 34000

print("\n")
e1 = Employee()
e1.get_salary()

print("*")

e2 = Employee()
e2.get_salary()


# ------------------------------------------------------------
## WHAT HAPPENS IF WE DON'T USE self?
# ------------------------------------------------------------

class Employee:

    def get_salary():
        print("Hello")
        return 34000


e1 = Employee()
# e1.get_salary()

# This causes an error: e1.get_salary()

# Why?
#   Python automatically passes e1:
#
# e1.get_salary()
#       ↓
# Employee.get_salary(e1)
#
# But our method is defined as: get_salary()
# It accepts ZERO parameters.
#
# Python is trying to pass 1 argument (e1),but the method has nowhere to receive it.
#
# Error:
# TypeError: Employee.get_salary() takes 0 positional arguments but 1 was given


# ------------------------------------------------------------
## IMPORTANT: self IS NOT A SPECIAL KEYWORD
# ------------------------------------------------------------

# `self` is the standard naming convention.
#
# Python does not force us to use the name `self`.
# We could technically write:


class Employee:

    def get_salary(employee):
        # Here, `employee` receives the current object.
        print(employee)
        return 34000

print("\n")
# This works:

e1 = Employee()
e1.get_salary()

# But using `self` is the standard and recommended convention in Python.


# ------------------------------------------------------------
## SIMPLE MENTAL MODEL
# ------------------------------------------------------------

# e1 = Employee()
#
# e1.get_salary()
#       ↓
# Python automatically passes e1
#       ↓
# Employee.get_salary(e1)
#       ↓
# self receives e1
#
# Therefore:
#
# self = reference to the current object
#
# Example:
#
# e1.get_salary()  → self refers to e1
# e2.get_salary()  → self refers to e2


# ------------------------------------------------------------
## self IS A REFERENCE, NOT THE OBJECT ITSELF
# ------------------------------------------------------------

class Employee:

    def show_object(self):
        print("self:", self)
        print("id(self):", id(self))

print("\n")

e1 = Employee()

print("e1:", e1)
print("id(e1):", id(e1))

e1.show_object()

# The output will show that:
#
# id(self) == id(e1)
#
# because `self` refers to the same object
# that `e1` refers to during this method call.


# ------------------------------------------------------------
## KEY POINTS TO REMEMBER
# ------------------------------------------------------------

# 1. Instance methods normally have a first parameter to receive the current object.
# 2. `self` is the standard name for that parameter.
# 3. Python automatically passes the object when calling an instance method using:
#        e1.get_salary()
# 4. Internally, think of it as:
#        Employee.get_salary(e1)
# 5. `self` allows us to access the current object's attributes and methods.
# 6. Without a parameter to receive the object, Python raises a TypeError.
# 7. `self` is a convention, not a Python keyword.
# ============================================================

