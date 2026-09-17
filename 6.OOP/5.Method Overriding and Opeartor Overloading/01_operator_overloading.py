class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def sum(self, p): # self refers to the object calling the method => Point.sum(p1, p2)
        return Point((self.x + p.x), (self.y + p.y)) # We're creating a new Point object: Point(9, 5)
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

p = p1.sum(p2) # Returns a new point which is sum of p1 and p2, where p is the third (3rd) point object : p  → (9, 5)
p.print_point()
print("*)
p = p1 + p2 # We overloaded the + Operator by writing __add__ function
p.print_point()
