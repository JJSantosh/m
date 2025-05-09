import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * (self.radius **2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

circle=Circle(20)
print("area:",circle.area())
print("perimeter:",circle.perimeter())