class Employee: 
    
    # __init__() is where we set up the initial data of each object, and self tells Python which particular object that data belongs to.
    def __init__(self, salary, name, bond):
        # `self` refers to the current object.
        # `salary`, 'name' and `bond` are parameters that receive values when we create the object.
        
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        #   Put this name value into the current object's name attribute.
        #   self.name → attribute belonging to the object
        #   name      → parameter value
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
    

e1 = Employee(34000, "John Doe", 4)
print(e1.get_salary())
e1.get_info()
