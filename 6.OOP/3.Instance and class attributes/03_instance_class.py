class Employee: 
    company = "Asus" # This is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")


e1 = Employee(3400, "John", 3, "Tesla")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company) # This will always print the class attribute

# Object introspection : Object introspection in Python is the ability to examine an object's type, attributes, methods, and metadata at runtime.
# hese are special/dunder attributes and methods that Python provides through the object's class and inheritance system
print(dir(e1))


## Quick memory trick:
#
# type(e1)      → "What type is this?"
# dir(e1)       → "What names are available?"
# e1.__dict__   → "What instance data is stored?"
